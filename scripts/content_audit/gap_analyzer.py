"""
Gap Analyzer for [YOUR-DOMAIN] Content Audit

Provides three types of SEO analysis:
1. Keyword Gap Analysis - Find queries with impressions but no matching content
2. CTR Optimization Candidates - Pages with high impressions but low CTR
3. Cannibalization Detection - Multiple pages competing for same keywords

v2.1: Added Russian text normalization (lemmatization, stop words)
"""

import csv
import zipfile
import io
import re
from typing import Dict, List, Optional, Tuple, Set
from pathlib import Path
from dataclasses import dataclass, field
from collections import defaultdict

# Try to import pymorphy3 for lemmatization (optional but recommended)
try:
    import pymorphy3
    MORPH = pymorphy3.MorphAnalyzer()
    HAS_PYMORPHY = True
except ImportError:
    MORPH = None
    HAS_PYMORPHY = False
    print("Warning: pymorphy3 not installed. Using basic normalization only.")
    print("Install with: pip install pymorphy3")


# Russian stop words (prepositions, conjunctions, particles, pronouns)
RUSSIAN_STOP_WORDS = {
    # Prepositions
    'в', 'на', 'с', 'со', 'к', 'ко', 'по', 'за', 'из', 'от', 'до', 'для', 'при',
    'без', 'под', 'над', 'про', 'между', 'через', 'около', 'у', 'о', 'об',
    # Conjunctions
    'и', 'а', 'но', 'или', 'что', 'как', 'чтобы', 'если', 'когда', 'потому',
    'так', 'тоже', 'также', 'либо', 'то', 'ни', 'не',
    # Particles
    'бы', 'ли', 'же', 'вот', 'ведь', 'уже', 'ещё', 'еще', 'лишь', 'только',
    'даже', 'именно', 'почти', 'всё', 'все',
    # Pronouns
    'я', 'ты', 'он', 'она', 'оно', 'мы', 'вы', 'они',
    'мой', 'твой', 'его', 'её', 'наш', 'ваш', 'их',
    'этот', 'тот', 'такой', 'какой', 'который', 'чей',
    'сам', 'самый', 'весь', 'каждый', 'любой', 'другой', 'иной',
    # Common words to skip
    'это', 'быть', 'был', 'была', 'были', 'будет', 'есть', 'нет',
    'можно', 'нужно', 'надо', 'очень', 'много', 'мало',
}


class RussianNormalizer:
    """
    Normalizes Russian text for SEO keyword matching.

    Applies:
    1. Lowercase conversion
    2. Stop words removal
    3. Lemmatization (word base form) using pymorphy3
    """

    def __init__(self):
        self.morph = MORPH
        self.stop_words = RUSSIAN_STOP_WORDS
        self._cache: Dict[str, str] = {}

    def normalize_word(self, word: str) -> Optional[str]:
        """
        Normalize a single word to its base form.
        Returns None if word is a stop word or too short.
        """
        word = word.lower().strip()

        # Skip short words and stop words
        if len(word) <= 2 or word in self.stop_words:
            return None

        # Check cache
        if word in self._cache:
            return self._cache[word]

        # Lemmatize if pymorphy is available
        if self.morph:
            parsed = self.morph.parse(word)
            if parsed:
                # Get the most likely normal form
                normal_form = parsed[0].normal_form
                self._cache[word] = normal_form
                return normal_form

        # Fallback: return word as-is
        self._cache[word] = word
        return word

    def normalize_phrase(self, phrase: str) -> Set[str]:
        """
        Normalize a phrase to a set of base forms.
        Removes stop words and applies lemmatization.

        Example:
            "премиаты купить в москве" -> {"премиата", "купить", "москва"}
            "женские лоферы на каблуке" -> {"женский", "лофер", "каблук"}
        """
        # Remove non-alphanumeric (keep Cyrillic and Latin)
        phrase = re.sub(r'[^\w\s]', ' ', phrase.lower())

        words = phrase.split()
        normalized = set()

        for word in words:
            norm = self.normalize_word(word)
            if norm:
                normalized.add(norm)

        return normalized

    def similarity_score(self, query: str, keywords: Set[str]) -> float:
        """
        Calculate similarity score between a query and a set of keywords.
        Both are normalized before comparison.

        Returns:
            Float between 0.0 (no match) and 1.0 (full match)
        """
        query_normalized = self.normalize_phrase(query)

        if not query_normalized:
            return 0.0

        # Keywords should already be normalized
        matches = query_normalized & keywords

        return len(matches) / len(query_normalized)


@dataclass
class QueryData:
    """Data for a search query from Yandex/GSC."""
    query: str
    impressions: int = 0
    clicks: int = 0
    ctr: float = 0.0
    position: float = 0.0
    source: str = "yandex"  # "yandex" or "gsc"


@dataclass
class KeywordGap:
    """A keyword opportunity without matching content."""
    query: str
    yandex_impressions: int = 0
    yandex_clicks: int = 0
    yandex_position: float = 0.0
    gsc_impressions: int = 0
    gsc_clicks: int = 0
    gsc_position: float = 0.0
    matching_pages: List[str] = field(default_factory=list)
    gap_type: str = "no_content"  # "no_content", "weak_content", "off_topic"


@dataclass
class CTRCandidate:
    """A page that could benefit from CTR optimization."""
    url: str
    title: str
    impressions: int
    clicks: int
    current_ctr: float
    position: float
    expected_ctr: float
    potential_clicks: int
    source: str  # "yandex", "gsc", or "combined"


@dataclass
class CannibalizationGroup:
    """A group of pages competing for the same keyword."""
    keyword: str
    pages: List[Dict]  # List of {url, title, clicks, impressions, position}
    total_impressions: int
    total_clicks: int
    recommendation: str


class GapAnalyzer:
    """Analyzes content gaps, CTR opportunities, and cannibalization."""

    # Expected CTR by position (approximate, based on industry averages)
    EXPECTED_CTR_BY_POSITION = {
        1: 28.0,
        2: 15.0,
        3: 11.0,
        4: 8.0,
        5: 7.0,
        6: 5.0,
        7: 4.0,
        8: 3.0,
        9: 2.5,
        10: 2.0,
        # Positions 11+ get ~1%
    }

    def __init__(self, webmasters_dir: str = "research/webmasters"):
        self.webmasters_dir = Path(webmasters_dir)
        self.yandex_queries: Dict[str, QueryData] = {}
        self.gsc_queries: Dict[str, QueryData] = {}
        self.normalizer = RussianNormalizer()

    def load_query_data(self) -> Tuple[int, int]:
        """
        Load query data from Yandex and GSC reports.
        Returns tuple of (yandex_count, gsc_count).
        """
        yandex_count = self._load_yandex_queries()
        gsc_count = self._load_gsc_queries()
        return yandex_count, gsc_count

    def _load_yandex_queries(self) -> int:
        """Load queries from Yandex Webmaster CSV (query report, not pages)."""
        yandex_files = list(self.webmasters_dir.glob("[YOUR-DOMAIN]_*.csv"))

        for csv_path in yandex_files:
            try:
                with open(csv_path, 'r', encoding='utf-8') as f:
                    first_line = f.readline()
                    # Query file has "Query" column, not "Path"
                    if '"Query"' not in first_line and 'Query,' not in first_line:
                        continue

                    f.seek(0)  # Reset to beginning
                    reader = csv.DictReader(f)

                    for row in reader:
                        query = row.get('Query', '').strip().lower()
                        if not query:
                            continue

                        try:
                            impressions = int(float(row.get('Impressions', '0').replace(',', '').replace(' ', '') or '0'))
                            clicks = int(float(row.get('Clicks', '0').replace(',', '').replace(' ', '') or '0'))
                            ctr_str = row.get('CTR %', '').replace('%', '').replace(',', '.').strip()
                            ctr = float(ctr_str) if ctr_str else 0.0
                            position = float(row.get('Avg. position', '0').replace(',', '.') or '0')
                        except (ValueError, AttributeError):
                            continue

                        self.yandex_queries[query] = QueryData(
                            query=query,
                            impressions=impressions,
                            clicks=clicks,
                            ctr=ctr,
                            position=position,
                            source="yandex"
                        )

                    print(f"Loaded {len(self.yandex_queries)} Yandex queries from {csv_path.name}")
                    return len(self.yandex_queries)

            except Exception as e:
                print(f"Error reading {csv_path}: {e}")
                continue

        return 0

    def _load_gsc_queries(self) -> int:
        """Load queries from GSC ZIP export."""
        gsc_files = list(self.webmasters_dir.glob("*Performance*.zip"))

        if not gsc_files:
            return 0

        latest_gsc = max(gsc_files, key=lambda p: p.stat().st_mtime)

        try:
            with zipfile.ZipFile(latest_gsc, 'r') as zf:
                # Find queries file
                queries_file = None
                for name in zf.namelist():
                    if 'запрос' in name.lower() or 'queries' in name.lower():
                        queries_file = name
                        break

                if not queries_file:
                    return 0

                with zf.open(queries_file) as f:
                    content = f.read().decode('utf-8')
                    reader = csv.DictReader(io.StringIO(content))

                    for row in reader:
                        query = None
                        clicks = impressions = 0
                        ctr = position = 0.0

                        for key in row.keys():
                            key_lower = key.lower()
                            if 'запрос' in key_lower or 'query' in key_lower or 'top queries' in key_lower:
                                query = row[key].strip().lower()
                            elif 'клик' in key_lower or 'click' in key_lower or 'kлик' in key_lower:
                                try:
                                    clicks = int(row[key].replace(',', '').replace(' ', ''))
                                except (ValueError, AttributeError):
                                    clicks = 0
                            elif 'показ' in key_lower or 'impression' in key_lower:
                                try:
                                    impressions = int(row[key].replace(',', '').replace(' ', ''))
                                except (ValueError, AttributeError):
                                    impressions = 0
                            elif 'ctr' in key_lower:
                                try:
                                    ctr_str = row[key].replace('%', '').replace(',', '.').strip()
                                    ctr = float(ctr_str) if ctr_str else 0.0
                                except (ValueError, AttributeError):
                                    ctr = 0.0
                            elif 'позиц' in key_lower or 'position' in key_lower:
                                try:
                                    position = float(row[key].replace(',', '.'))
                                except (ValueError, AttributeError):
                                    position = 0.0

                        if query:
                            self.gsc_queries[query] = QueryData(
                                query=query,
                                impressions=impressions,
                                clicks=clicks,
                                ctr=ctr,
                                position=position,
                                source="gsc"
                            )

                    print(f"Loaded {len(self.gsc_queries)} GSC queries from {latest_gsc.name}")
                    return len(self.gsc_queries)

        except Exception as e:
            print(f"Error loading GSC queries: {e}")
            return 0

    def find_keyword_gaps(
        self,
        pages: List[Dict],
        min_impressions: int = 50,
        max_results: int = 50
    ) -> List[KeywordGap]:
        """
        Find queries with impressions but no matching content on the site.

        Uses Russian text normalization (lemmatization) so that:
        - "премиаты" matches "премиата"
        - "женские лоферы" matches "женский лофер"

        Args:
            pages: List of page data dicts with 'top_keywords' field
            min_impressions: Minimum impressions to consider
            max_results: Maximum number of gaps to return

        Returns:
            List of KeywordGap objects sorted by total impressions
        """
        # Build NORMALIZED keyword index from existing content
        existing_keywords_normalized: Set[str] = set()

        for page in pages:
            # Normalize keywords from top_keywords field
            keywords_str = page.get('top_keywords', '')
            if keywords_str:
                for kw in keywords_str.split(','):
                    normalized = self.normalizer.normalize_phrase(kw.strip())
                    existing_keywords_normalized.update(normalized)

            # Also normalize words from page titles and H1
            title = page.get('title', '')
            h1 = page.get('h1', '')
            meta = page.get('meta_description', '')

            for text in [title, h1, meta]:
                if text:
                    normalized = self.normalizer.normalize_phrase(text)
                    existing_keywords_normalized.update(normalized)

        print(f"Built normalized keyword index with {len(existing_keywords_normalized)} unique terms")

        # Merge Yandex and GSC queries
        all_queries: Dict[str, KeywordGap] = {}

        for query, data in self.yandex_queries.items():
            if data.impressions >= min_impressions:
                gap = KeywordGap(
                    query=query,
                    yandex_impressions=data.impressions,
                    yandex_clicks=data.clicks,
                    yandex_position=data.position
                )
                all_queries[query] = gap

        for query, data in self.gsc_queries.items():
            if query in all_queries:
                all_queries[query].gsc_impressions = data.impressions
                all_queries[query].gsc_clicks = data.clicks
                all_queries[query].gsc_position = data.position
            elif data.impressions >= min_impressions:
                gap = KeywordGap(
                    query=query,
                    gsc_impressions=data.impressions,
                    gsc_clicks=data.clicks,
                    gsc_position=data.position
                )
                all_queries[query] = gap

        # Filter to find gaps using NORMALIZED matching
        gaps = []
        for query, gap in all_queries.items():
            # Calculate similarity score using normalization
            similarity = self.normalizer.similarity_score(query, existing_keywords_normalized)

            if similarity < 0.3:  # Less than 30% match = no content
                gap.gap_type = "no_content"
                gaps.append(gap)
            elif similarity < 0.6:  # 30-60% match = weak content
                gap.gap_type = "weak_content"
                gaps.append(gap)
            # 60%+ match = content exists, skip

        # Sort by total impressions
        gaps.sort(key=lambda g: g.yandex_impressions + g.gsc_impressions, reverse=True)

        return gaps[:max_results]

    def find_ctr_candidates(
        self,
        pages: List[Dict],
        min_impressions: int = 50,
        max_results: int = 30
    ) -> List[CTRCandidate]:
        """
        Find pages with high impressions but low CTR that could be optimized.

        Args:
            pages: List of page data dicts with metrics
            min_impressions: Minimum impressions to consider
            max_results: Maximum number of candidates to return

        Returns:
            List of CTRCandidate objects sorted by potential clicks
        """
        candidates = []

        for page in pages:
            # Get combined metrics
            yandex_impressions = page.get('yandex_impressions') or 0
            yandex_clicks = page.get('yandex_clicks') or 0
            gsc_impressions = page.get('gsc_impressions') or 0
            gsc_clicks = page.get('gsc_clicks') or 0

            total_impressions = yandex_impressions + gsc_impressions
            total_clicks = yandex_clicks + gsc_clicks

            if total_impressions < min_impressions:
                continue

            # Use average position from both sources
            yandex_pos = page.get('yandex_position') or 0
            gsc_pos = page.get('gsc_position') or 0

            if yandex_pos and gsc_pos:
                avg_position = (yandex_pos + gsc_pos) / 2
            else:
                avg_position = yandex_pos or gsc_pos or 20

            # Calculate current CTR
            current_ctr = (total_clicks / total_impressions * 100) if total_impressions > 0 else 0

            # Get expected CTR for this position
            pos_int = min(int(avg_position), 10)
            expected_ctr = self.EXPECTED_CTR_BY_POSITION.get(pos_int, 1.0)

            # Only include if current CTR is significantly below expected
            if current_ctr < expected_ctr * 0.7:  # 30% or more below expected
                potential_clicks = int(total_impressions * (expected_ctr / 100) - total_clicks)

                if potential_clicks > 5:  # At least 5 potential additional clicks
                    candidates.append(CTRCandidate(
                        url=page.get('url', ''),
                        title=page.get('title', '')[:80],
                        impressions=total_impressions,
                        clicks=total_clicks,
                        current_ctr=round(current_ctr, 2),
                        position=round(avg_position, 1),
                        expected_ctr=expected_ctr,
                        potential_clicks=potential_clicks,
                        source="combined"
                    ))

        # Sort by potential clicks
        candidates.sort(key=lambda c: c.potential_clicks, reverse=True)

        return candidates[:max_results]

    def find_cannibalization(
        self,
        pages: List[Dict],
        min_pages: int = 2,
        max_groups: int = 20
    ) -> List[CannibalizationGroup]:
        """
        Find groups of pages competing for the same keywords.

        Uses normalized keywords so "лоферы", "лоферов", "лоферами"
        are all treated as the same keyword "лофер".

        Args:
            pages: List of page data dicts with 'top_keywords'
            min_pages: Minimum pages to form a cannibalization group
            max_groups: Maximum number of groups to return

        Returns:
            List of CannibalizationGroup objects
        """
        # Build NORMALIZED keyword -> pages mapping
        keyword_pages: Dict[str, List[Dict]] = defaultdict(list)

        for page in pages:
            keywords_str = page.get('top_keywords', '')
            if not keywords_str:
                continue

            # Only look at top 5 keywords (most important)
            raw_keywords = [k.strip() for k in keywords_str.split(',')[:5]]

            # Track which normalized keywords we've added for this page (avoid duplicates)
            added_keywords: Set[str] = set()

            for raw_keyword in raw_keywords:
                # Normalize keyword to base form
                normalized = self.normalizer.normalize_word(raw_keyword)

                if normalized and normalized not in added_keywords:
                    added_keywords.add(normalized)

                    page_data = {
                        'url': page.get('url', ''),
                        'title': page.get('title', '')[:60],
                        'yandex_clicks': page.get('yandex_clicks') or 0,
                        'gsc_clicks': page.get('gsc_clicks') or 0,
                        'total_clicks': (page.get('yandex_clicks') or 0) + (page.get('gsc_clicks') or 0),
                        'yandex_impressions': page.get('yandex_impressions') or 0,
                        'gsc_impressions': page.get('gsc_impressions') or 0,
                        'total_impressions': (page.get('yandex_impressions') or 0) + (page.get('gsc_impressions') or 0),
                        'position': page.get('yandex_position') or page.get('gsc_position') or 0
                    }
                    keyword_pages[normalized].append(page_data)

        # Find groups with multiple pages
        groups = []
        for keyword, page_list in keyword_pages.items():
            if len(page_list) >= min_pages:
                # Remove duplicate pages (same URL)
                seen_urls: Set[str] = set()
                unique_pages = []
                for p in page_list:
                    if p['url'] not in seen_urls:
                        seen_urls.add(p['url'])
                        unique_pages.append(p)

                if len(unique_pages) < min_pages:
                    continue

                # Calculate totals
                total_impressions = sum(p['total_impressions'] for p in unique_pages)
                total_clicks = sum(p['total_clicks'] for p in unique_pages)

                # Generate recommendation
                if len(unique_pages) >= 5:
                    recommendation = "CRITICAL: Consolidate into 1-2 pillar articles"
                elif len(unique_pages) >= 3:
                    recommendation = "Consider merging similar content"
                else:
                    recommendation = "Review for overlap, may be intentional"

                # Sort pages by clicks
                sorted_pages = sorted(unique_pages, key=lambda p: p['total_clicks'], reverse=True)

                groups.append(CannibalizationGroup(
                    keyword=keyword,
                    pages=sorted_pages,
                    total_impressions=total_impressions,
                    total_clicks=total_clicks,
                    recommendation=recommendation
                ))

        # Sort by number of pages (worst cannibalization first)
        groups.sort(key=lambda g: len(g.pages), reverse=True)

        return groups[:max_groups]

    def generate_analysis(self, pages: List[Dict]) -> Dict:
        """
        Run all analyses and return combined results.

        Args:
            pages: List of page data dicts

        Returns:
            Dict with 'keyword_gaps', 'ctr_candidates', 'cannibalization'
        """
        # Load query data first
        yandex_count, gsc_count = self.load_query_data()
        print(f"Loaded {yandex_count} Yandex queries, {gsc_count} GSC queries")

        # Run analyses
        keyword_gaps = self.find_keyword_gaps(pages)
        ctr_candidates = self.find_ctr_candidates(pages)
        cannibalization = self.find_cannibalization(pages)

        return {
            'keyword_gaps': keyword_gaps,
            'ctr_candidates': ctr_candidates,
            'cannibalization': cannibalization,
            'query_counts': {
                'yandex': yandex_count,
                'gsc': gsc_count
            }
        }


if __name__ == "__main__":
    # Quick test
    import json

    analyzer = GapAnalyzer()
    yandex_count, gsc_count = analyzer.load_query_data()
    print(f"\nLoaded: {yandex_count} Yandex queries, {gsc_count} GSC queries")

    # Sample top queries
    print("\nTop 10 Yandex queries by impressions:")
    top_yandex = sorted(analyzer.yandex_queries.values(), key=lambda q: q.impressions, reverse=True)[:10]
    for q in top_yandex:
        print(f"  {q.query}: {q.impressions} impressions, {q.clicks} clicks, pos {q.position:.1f}")

    print("\nTop 10 GSC queries by impressions:")
    top_gsc = sorted(analyzer.gsc_queries.values(), key=lambda q: q.impressions, reverse=True)[:10]
    for q in top_gsc:
        print(f"  {q.query}: {q.impressions} impressions, {q.clicks} clicks, pos {q.position:.1f}")

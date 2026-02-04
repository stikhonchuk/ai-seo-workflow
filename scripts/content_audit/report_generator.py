"""
Report Generator for [YOUR-DOMAIN] Content Audit
Generates CSV and JSON reports from collected page data.
Includes SEO gap analysis: keyword gaps, CTR optimization, cannibalization.
"""

import json
import csv
from typing import List, Dict, Any, Optional
from pathlib import Path
from datetime import datetime

try:
    from .gap_analyzer import GapAnalyzer
except ImportError:
    from gap_analyzer import GapAnalyzer


class ReportGenerator:
    """Generates CSV and JSON reports from audit data."""

    def __init__(self, output_dir: str = "research/content-audit"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        # Generate date suffix for all reports
        self.date_suffix = datetime.now().strftime('%Y-%m-%d')

    def generate_csv(self, pages: List[Dict], filename: str = None) -> Path:
        """Generate CSV report from page data."""
        if filename is None:
            filename = f"site-content-audit-{self.date_suffix}.csv"
        output_path = self.output_dir / filename

        # Define column order
        columns = [
            'url',
            'lastmod',
            'content_type',
            'title',
            'h1',
            'meta_description',
            'word_count',
            'top_keywords',
            'yandex_clicks',
            'yandex_impressions',
            'yandex_ctr',
            'yandex_position',
            'gsc_clicks',
            'gsc_impressions',
            'gsc_ctr',
            'gsc_position',
            'total_clicks',
            'total_impressions',
            'status',
            'error'
        ]

        with open(output_path, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.DictWriter(f, fieldnames=columns, extrasaction='ignore')
            writer.writeheader()

            for page in pages:
                # Format keywords as comma-separated string
                if 'top_keywords' in page and isinstance(page['top_keywords'], list):
                    page['top_keywords'] = ', '.join(page['top_keywords'])

                # Calculate total clicks and impressions
                yandex_clicks = page.get('yandex_clicks') or 0
                gsc_clicks = page.get('gsc_clicks') or 0
                yandex_impressions = page.get('yandex_impressions') or 0
                gsc_impressions = page.get('gsc_impressions') or 0

                page['total_clicks'] = yandex_clicks + gsc_clicks if (yandex_clicks or gsc_clicks) else None
                page['total_impressions'] = yandex_impressions + gsc_impressions if (yandex_impressions or gsc_impressions) else None

                # Set status
                if 'error' in page and page['error']:
                    page['status'] = 'error'
                elif page.get('word_count', 0) > 0:
                    page['status'] = 'ok'
                else:
                    page['status'] = 'no_content'

                writer.writerow(page)

        return output_path

    def generate_json(self, pages: List[Dict], filename: str = None) -> Path:
        """Generate JSON report with full data and summary statistics."""
        if filename is None:
            filename = f"site-content-audit-{self.date_suffix}.json"
        output_path = self.output_dir / filename

        # Calculate summary statistics
        summary = self._calculate_summary(pages)

        # Prepare output structure
        report = {
            "generated": datetime.now().isoformat(),
            "total_pages": len(pages),
            "summary": summary,
            "pages": pages
        }

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)

        return output_path

    def _calculate_summary(self, pages: List[Dict]) -> Dict[str, Any]:
        """Calculate summary statistics from page data."""
        summary = {
            "by_type": {},
            "avg_word_count": 0,
            "total_word_count": 0,
            "pages_with_errors": 0,
            "pages_with_yandex_data": 0,
            "pages_with_gsc_data": 0,
            "top_performing_pages": [],
            "content_gaps": []
        }

        total_words = 0
        valid_pages = 0
        pages_by_type = {}
        pages_with_metrics = []

        for page in pages:
            # Count by type
            content_type = page.get('content_type', 'unknown')
            pages_by_type[content_type] = pages_by_type.get(content_type, 0) + 1

            # Word count
            word_count = page.get('word_count', 0)
            if word_count > 0:
                total_words += word_count
                valid_pages += 1

            # Errors
            if page.get('error'):
                summary['pages_with_errors'] += 1

            # Yandex data
            if page.get('yandex_clicks') is not None:
                summary['pages_with_yandex_data'] += 1

            # GSC data
            if page.get('gsc_clicks') is not None:
                summary['pages_with_gsc_data'] += 1

            # Collect pages with any metrics (prefer Yandex, fallback to GSC)
            yandex_clicks = page.get('yandex_clicks') or 0
            gsc_clicks = page.get('gsc_clicks') or 0
            total_clicks = yandex_clicks + gsc_clicks

            yandex_impressions = page.get('yandex_impressions') or 0
            gsc_impressions = page.get('gsc_impressions') or 0
            total_impressions = yandex_impressions + gsc_impressions

            if total_clicks > 0 or yandex_clicks > 0 or gsc_clicks > 0:
                pages_with_metrics.append({
                    'url': page['url'],
                    'title': page.get('title', ''),
                    'yandex_clicks': yandex_clicks,
                    'gsc_clicks': gsc_clicks,
                    'total_clicks': total_clicks,
                    'yandex_impressions': yandex_impressions,
                    'gsc_impressions': gsc_impressions,
                    'total_impressions': total_impressions,
                    'yandex_position': page.get('yandex_position', 0),
                    'gsc_position': page.get('gsc_position', 0)
                })

        summary['by_type'] = pages_by_type
        summary['avg_word_count'] = round(total_words / valid_pages) if valid_pages > 0 else 0
        summary['total_word_count'] = total_words

        # Top performing pages by total clicks (Yandex + GSC)
        if pages_with_metrics:
            top_pages = sorted(pages_with_metrics, key=lambda p: p['total_clicks'], reverse=True)[:10]
            summary['top_performing_pages'] = top_pages

        # Identify content gaps (pages with low word count)
        low_content_pages = [
            {
                'url': p['url'],
                'title': p.get('title', ''),
                'word_count': p.get('word_count', 0)
            }
            for p in pages
            if 0 < p.get('word_count', 0) < 300
        ]
        summary['content_gaps'] = low_content_pages[:20]  # Top 20 pages needing content

        return summary

    def generate_markdown_summary(
        self,
        pages: List[Dict],
        filename: str = None,
        include_gap_analysis: bool = True
    ) -> Path:
        """
        Generate a markdown summary highlighting content gaps and opportunities.

        Args:
            pages: List of page data dicts
            filename: Output filename (default: content-gaps-YYYY-MM-DD.md)
            include_gap_analysis: Whether to run SEO gap analysis
        """
        if filename is None:
            filename = f"content-gaps-{self.date_suffix}.md"
        output_path = self.output_dir / filename

        summary = self._calculate_summary(pages)

        # Run gap analysis if requested
        gap_analysis = None
        if include_gap_analysis:
            try:
                analyzer = GapAnalyzer()
                gap_analysis = analyzer.generate_analysis(pages)
            except Exception as e:
                print(f"Warning: Gap analysis failed: {e}")

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("# SEO Content Audit Report\n\n")
            f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

            # Overview
            f.write("## Overview\n\n")
            f.write(f"- **Total Pages Analyzed:** {len(pages)}\n")
            f.write(f"- **Total Word Count:** {summary['total_word_count']:,}\n")
            f.write(f"- **Average Word Count:** {summary['avg_word_count']:,}\n")
            f.write(f"- **Pages with Yandex Data:** {summary['pages_with_yandex_data']}\n")
            f.write(f"- **Pages with GSC Data:** {summary['pages_with_gsc_data']}\n")
            if gap_analysis:
                f.write(f"- **Yandex Queries Analyzed:** {gap_analysis['query_counts']['yandex']}\n")
                f.write(f"- **GSC Queries Analyzed:** {gap_analysis['query_counts']['gsc']}\n")
            f.write(f"- **Pages with Errors:** {summary['pages_with_errors']}\n\n")

            # By content type
            f.write("## Content by Type\n\n")
            for content_type, count in sorted(summary['by_type'].items(), key=lambda x: x[1], reverse=True):
                f.write(f"- **{content_type}:** {count} pages\n")
            f.write("\n")

            # Top performing
            if summary['top_performing_pages']:
                f.write("## Top 10 Performing Pages (by clicks)\n\n")
                f.write("| # | Page | Yandex | GSC | Total | Position |\n")
                f.write("|---|------|--------|-----|-------|----------|\n")
                for i, page in enumerate(summary['top_performing_pages'], 1):
                    title = page['title'][:55] + "..." if len(page['title']) > 55 else page['title']
                    yandex_pos = page.get('yandex_position', 0) or 0
                    gsc_pos = page.get('gsc_position', 0) or 0
                    avg_pos = (yandex_pos + gsc_pos) / 2 if (yandex_pos or gsc_pos) else 0
                    f.write(f"| {i} | [{title}]({page['url']}) | {page['yandex_clicks']} | "
                           f"{page['gsc_clicks']} | {page['total_clicks']} | {avg_pos:.1f} |\n")
                f.write("\n")

            # === SEO GAP ANALYSIS SECTIONS ===

            if gap_analysis:
                self._write_keyword_gaps_section(f, gap_analysis.get('keyword_gaps', []))
                self._write_ctr_optimization_section(f, gap_analysis.get('ctr_candidates', []))
                self._write_cannibalization_section(f, gap_analysis.get('cannibalization', []))

            # Content gaps (low word count)
            if summary['content_gaps']:
                f.write("## Low Content Pages (<300 words)\n\n")
                f.write("Pages that may need expansion:\n\n")
                f.write("| # | Page | Words |\n")
                f.write("|---|------|-------|\n")
                for i, page in enumerate(summary['content_gaps'][:20], 1):
                    title = page['title'][:65] + "..." if len(page['title']) > 65 else page['title']
                    f.write(f"| {i} | [{title}]({page['url']}) | {page['word_count']} |\n")
                f.write("\n")

        return output_path

    def _write_keyword_gaps_section(self, f, keyword_gaps: List) -> None:
        """Write keyword gaps section to markdown file."""
        if not keyword_gaps:
            return

        f.write("---\n\n")
        f.write("## 🔍 Keyword Gap Analysis\n\n")
        f.write("Queries with impressions but no matching content on the site:\n\n")
        f.write("| # | Query | Yandex Imp. | GSC Imp. | Position | Gap Type |\n")
        f.write("|---|-------|-------------|----------|----------|----------|\n")

        for i, gap in enumerate(keyword_gaps[:30], 1):
            query = gap.query[:40] + "..." if len(gap.query) > 40 else gap.query
            yandex_imp = gap.yandex_impressions or "-"
            gsc_imp = gap.gsc_impressions or "-"
            position = gap.yandex_position or gap.gsc_position or "-"
            if isinstance(position, float):
                position = f"{position:.1f}"

            gap_icon = "❌" if gap.gap_type == "no_content" else "⚠️"
            f.write(f"| {i} | {query} | {yandex_imp} | {gsc_imp} | {position} | {gap_icon} {gap.gap_type} |\n")

        f.write("\n**Legend:** ❌ no_content = полностью отсутствует, ⚠️ weak_content = частичное покрытие\n\n")

    def _write_ctr_optimization_section(self, f, ctr_candidates: List) -> None:
        """Write CTR optimization section to markdown file."""
        if not ctr_candidates:
            return

        f.write("---\n\n")
        f.write("## 📈 CTR Optimization Candidates\n\n")
        f.write("Pages with high impressions but low CTR — improve title/description:\n\n")
        f.write("| # | Page | Impressions | CTR | Expected | Potential |\n")
        f.write("|---|------|-------------|-----|----------|----------|\n")

        for i, candidate in enumerate(ctr_candidates[:20], 1):
            title = candidate.title[:50] + "..." if len(candidate.title) > 50 else candidate.title
            current_ctr = f"{candidate.current_ctr:.1f}%"
            expected_ctr = f"{candidate.expected_ctr:.0f}%"
            f.write(f"| {i} | [{title}]({candidate.url}) | {candidate.impressions} | "
                   f"{current_ctr} | {expected_ctr} | +{candidate.potential_clicks} clicks |\n")

        f.write("\n**Action:** Улучшить title и meta description для повышения CTR\n\n")

    def _write_cannibalization_section(self, f, cannibalization: List) -> None:
        """Write cannibalization section to markdown file."""
        if not cannibalization:
            return

        f.write("---\n\n")
        f.write("## ⚠️ Keyword Cannibalization\n\n")
        f.write("Multiple pages competing for the same keywords:\n\n")

        for group in cannibalization[:15]:
            severity = "🚨" if len(group.pages) >= 5 else "⚠️" if len(group.pages) >= 3 else "ℹ️"
            f.write(f"### {severity} `{group.keyword}` ({len(group.pages)} pages)\n\n")
            f.write(f"**Total:** {group.total_clicks} clicks, {group.total_impressions} impressions\n\n")
            f.write(f"**Recommendation:** {group.recommendation}\n\n")

            f.write("| Page | Clicks | Impressions | Position |\n")
            f.write("|------|--------|-------------|----------|\n")

            for page in group.pages[:7]:  # Show top 7 pages per group
                title = page['title'][:45] + "..." if len(page['title']) > 45 else page['title']
                position = page['position']
                if isinstance(position, float) and position > 0:
                    position = f"{position:.1f}"
                else:
                    position = "-"
                f.write(f"| [{title}]({page['url']}) | {page['total_clicks']} | "
                       f"{page['total_impressions']} | {position} |\n")

            if len(group.pages) > 7:
                f.write(f"| *...and {len(group.pages) - 7} more pages* | | | |\n")

            f.write("\n")

    def generate_all(self, pages: List[Dict]) -> Dict[str, Path]:
        """Generate all report formats."""
        return {
            'csv': self.generate_csv(pages),
            'json': self.generate_json(pages),
            'markdown': self.generate_markdown_summary(pages)
        }


if __name__ == "__main__":
    # Quick test with sample data
    generator = ReportGenerator()

    sample_pages = [
        {
            'url': 'https://[YOUR-DOMAIN]/blogs/blog/test-1',
            'lastmod': '2026-01-15',
            'content_type': 'blog',
            'title': 'Test Article 1',
            'h1': 'Test H1',
            'meta_description': 'Test description',
            'word_count': 1500,
            'top_keywords': ['обувь', 'лоферы', 'стиль'],
            'gsc_clicks': 50,
            'gsc_impressions': 1000,
            'gsc_ctr': 5.0,
            'gsc_position': 8.2
        },
        {
            'url': 'https://[YOUR-DOMAIN]/collection/loafers',
            'lastmod': '2026-01-20',
            'content_type': 'collection',
            'title': 'Loafers Collection',
            'h1': 'Loafers',
            'meta_description': 'Shop loafers',
            'word_count': 250,
            'top_keywords': ['лоферы', 'купить'],
            'gsc_clicks': None,
            'gsc_impressions': None
        }
    ]

    paths = generator.generate_all(sample_pages)
    print("Generated reports:")
    for format_type, path in paths.items():
        print(f"  {format_type}: {path}")

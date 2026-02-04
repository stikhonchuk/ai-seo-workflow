#!/usr/bin/env python3
"""
Content Audit Utility for [YOUR-DOMAIN]
Main CLI entry point.

Usage:
    python scripts/content_audit/main.py --full
    python scripts/content_audit/main.py --sitemap-only
    python scripts/content_audit/main.py --update-webmaster
"""

import argparse
import sys
import json
import os
from pathlib import Path
from datetime import datetime
from tqdm import tqdm

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from sitemap_parser import SitemapParser
from page_scraper import PageScraper
from keyword_extractor import KeywordExtractor
from webmaster_data import WebmasterDataParser
from report_generator import ReportGenerator


CACHE_FILE = Path("research/content-audit/.cache.json")
LOG_FILE = Path("research/content-audit/audit-log.txt")


class ContentAuditor:
    """Main content audit orchestrator."""

    def __init__(self, output_format='both'):
        self.sitemap_parser = SitemapParser()
        self.page_scraper = PageScraper(delay=0.5)
        self.keyword_extractor = KeywordExtractor()
        self.webmaster_parser = WebmasterDataParser()
        self.report_generator = ReportGenerator()
        self.output_format = output_format
        self.output_dir = Path("research/content-audit")
        self.cache = {}

    def log(self, message: str):
        """Log message to both console and file."""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_msg = f"[{timestamp}] {message}"
        print(log_msg)

        LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(log_msg + '\n')

    def load_cache(self):
        """Load cached page data."""
        if CACHE_FILE.exists():
            try:
                with open(CACHE_FILE, 'r', encoding='utf-8') as f:
                    self.cache = json.load(f)
                self.log(f"Loaded cache with {len(self.cache)} entries")
            except Exception as e:
                self.log(f"Cache load error: {e}")
                self.cache = {}

    def save_cache(self, pages: list):
        """Save page data to cache."""
        try:
            CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
            cache_data = {p['url']: p for p in pages}
            with open(CACHE_FILE, 'w', encoding='utf-8') as f:
                json.dump(cache_data, f, ensure_ascii=False, indent=2)
            self.log(f"Saved {len(cache_data)} entries to cache")
        except Exception as e:
            self.log(f"Cache save error: {e}")

    def _create_latest_symlinks(self, csv_path=None, json_path=None, md_path=None):
        """Create symlinks to latest reports for easy access."""
        symlinks = [
            (csv_path, "site-content-audit-latest.csv"),
            (json_path, "site-content-audit-latest.json"),
            (md_path, "content-gaps-latest.md")
        ]

        for source, link_name in symlinks:
            if source is None:
                continue

            link_path = self.output_dir / link_name

            # Remove old symlink if it exists
            if link_path.exists() or link_path.is_symlink():
                link_path.unlink()

            # Create new symlink (relative to output directory)
            try:
                os.symlink(source.name, link_path)
            except Exception as e:
                self.log(f"Warning: Could not create symlink {link_name}: {e}")

    def run_sitemap_only(self):
        """Run sitemap parsing only."""
        self.log("Starting sitemap-only mode...")

        self.log("Fetching sitemap.xml...")
        entries = self.sitemap_parser.fetch_and_parse(filter_content=True)

        stats = self.sitemap_parser.get_stats()
        self.log(f"Sitemap parsed successfully")
        self.log(f"  Total URLs: {stats['total']}")
        self.log(f"  Blog + Collection: {stats['blog_and_collection']}")
        self.log(f"  By type: {stats['by_type']}")

        return entries

    def run_full_audit(self, force_refresh=False):
        """Run full content audit."""
        self.log("=" * 70)
        self.log("STARTING FULL CONTENT AUDIT")
        self.log("=" * 70)

        # Load cache
        if not force_refresh:
            self.load_cache()

        # Step 1: Parse sitemap
        self.log("\n[1/5] Parsing sitemap...")
        entries = self.sitemap_parser.fetch_and_parse(filter_content=True)
        self.log(f"Found {len(entries)} blog and collection pages")

        # Step 2: Scrape pages
        self.log("\n[2/5] Scraping pages...")
        pages_data = []

        with tqdm(total=len(entries), desc="Scraping pages") as pbar:
            for entry in entries:
                # Check cache
                if not force_refresh and entry.url in self.cache:
                    cached = self.cache[entry.url]
                    # Use cache if lastmod matches
                    if cached.get('lastmod') == entry.lastmod:
                        pages_data.append(cached)
                        pbar.update(1)
                        continue

                # Scrape page
                page_data = self.page_scraper.scrape(entry.url)

                # Extract keywords
                if page_data.content_text and not page_data.error:
                    keywords = self.keyword_extractor.extract(page_data.content_text, top_n=10)
                    page_data.top_keywords = keywords

                # Convert to dict
                page_dict = {
                    'url': page_data.url,
                    'lastmod': entry.lastmod,
                    'content_type': entry.content_type,
                    'title': page_data.title,
                    'h1': page_data.h1,
                    'meta_description': page_data.meta_description,
                    'word_count': page_data.word_count,
                    'top_keywords': page_data.top_keywords,
                    'error': page_data.error
                }

                pages_data.append(page_dict)
                pbar.update(1)

        self.log(f"Scraped {len(pages_data)} pages")

        # Save intermediate cache
        self.save_cache(pages_data)

        # Step 3: Extract keywords (already done in scraping)
        self.log("\n[3/5] Keywords extracted during scraping")

        # Step 4: Load webmaster data
        self.log("\n[4/5] Loading webmaster data...")
        self.webmaster_parser.load_latest_reports()
        pages_data = self.webmaster_parser.enrich_page_data(pages_data)
        self.log("Webmaster data enrichment complete")

        # Step 5: Generate reports
        self.log("\n[5/5] Generating reports...")
        if self.output_format in ('csv', 'both'):
            csv_path = self.report_generator.generate_csv(pages_data)
            self.log(f"CSV report: {csv_path}")

        if self.output_format in ('json', 'both'):
            json_path = self.report_generator.generate_json(pages_data)
            self.log(f"JSON report: {json_path}")

        # Always generate markdown summary
        md_path = self.report_generator.generate_markdown_summary(pages_data)
        self.log(f"Markdown summary: {md_path}")

        # Create symlinks to latest reports for easy access
        self._create_latest_symlinks(csv_path if self.output_format in ('csv', 'both') else None,
                                     json_path if self.output_format in ('json', 'both') else None,
                                     md_path)

        self.log("\n" + "=" * 70)
        self.log("AUDIT COMPLETE")
        self.log("=" * 70)

        return pages_data

    def update_webmaster_only(self):
        """Update only webmaster data (re-enrich existing cache)."""
        self.log("Updating webmaster data only...")

        # Load cache
        self.load_cache()
        if not self.cache:
            self.log("ERROR: No cache found. Run --full first.")
            return

        pages_data = list(self.cache.values())

        # Load and enrich
        self.log("Loading latest webmaster reports...")
        self.webmaster_parser.load_latest_reports()
        pages_data = self.webmaster_parser.enrich_page_data(pages_data)

        # Save cache
        self.save_cache(pages_data)

        # Generate reports
        self.log("Generating reports...")
        self.report_generator.generate_all(pages_data)

        self.log("Webmaster data update complete")


def main():
    parser = argparse.ArgumentParser(
        description="Content Audit Utility for [YOUR-DOMAIN]",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/content_audit/main.py --full
  python scripts/content_audit/main.py --sitemap-only
  python scripts/content_audit/main.py --update-webmaster
  python scripts/content_audit/main.py --full --output json
        """
    )

    parser.add_argument('--full', action='store_true',
                       help='Run full content audit (sitemap + scraping + webmaster)')
    parser.add_argument('--sitemap-only', action='store_true',
                       help='Only fetch and parse sitemap.xml')
    parser.add_argument('--update-webmaster', action='store_true',
                       help='Update webmaster data only (uses cache)')
    parser.add_argument('--output', choices=['csv', 'json', 'both'], default='both',
                       help='Output format (default: both)')
    parser.add_argument('--force-refresh', action='store_true',
                       help='Force refresh all pages (ignore cache)')

    args = parser.parse_args()

    # Validate arguments
    if not (args.full or args.sitemap_only or args.update_webmaster):
        parser.print_help()
        sys.exit(1)

    # Create auditor
    auditor = ContentAuditor(output_format=args.output)

    # Run appropriate mode
    try:
        if args.sitemap_only:
            auditor.run_sitemap_only()
        elif args.update_webmaster:
            auditor.update_webmaster_only()
        elif args.full:
            auditor.run_full_audit(force_refresh=args.force_refresh)

    except KeyboardInterrupt:
        auditor.log("\n\nAudit interrupted by user")
        sys.exit(1)
    except Exception as e:
        auditor.log(f"\n\nERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()

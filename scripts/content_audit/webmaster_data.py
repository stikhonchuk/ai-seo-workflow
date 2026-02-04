"""
Webmaster Data Parser for [YOUR-DOMAIN]
Parses Yandex Webmaster and Google Search Console reports to enrich page data.
"""

import gzip
import csv
import zipfile
import io
from typing import Dict, Optional, List
from pathlib import Path
from dataclasses import dataclass


@dataclass
class WebmasterMetrics:
    """Metrics from webmaster tools for a specific URL."""
    url: str
    yandex_clicks: Optional[int] = None
    yandex_impressions: Optional[int] = None
    yandex_ctr: Optional[float] = None
    yandex_position: Optional[float] = None
    gsc_clicks: Optional[int] = None
    gsc_impressions: Optional[int] = None
    gsc_ctr: Optional[float] = None
    gsc_position: Optional[float] = None


class WebmasterDataParser:
    """Parses Yandex Webmaster and GSC data files."""

    def __init__(self, webmasters_dir: str = "research/webmasters"):
        self.webmasters_dir = Path(webmasters_dir)
        self.url_metrics: Dict[str, WebmasterMetrics] = {}

    def parse_yandex_csv(self, csv_path: Path) -> Dict[str, WebmasterMetrics]:
        """
        Parse Yandex Webmaster pages CSV file.
        Format: Path,Dates range,Impressions,Clicks,CTR %,Avg. position,...
        """
        url_data = {}

        try:
            with open(csv_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)

                for row in reader:
                    path = row.get('Path', '').strip()
                    if not path:
                        continue

                    # Build full URL
                    url = f"https://[YOUR-DOMAIN]{path}"

                    # Parse metrics
                    try:
                        impressions = int(float(row.get('Impressions', '0').replace(',', '').replace(' ', '') or '0'))
                    except (ValueError, AttributeError):
                        impressions = None

                    try:
                        clicks = int(float(row.get('Clicks', '0').replace(',', '').replace(' ', '') or '0'))
                    except (ValueError, AttributeError):
                        clicks = None

                    try:
                        ctr_str = row.get('CTR %', '').replace('%', '').replace(',', '.').strip()
                        ctr = float(ctr_str) if ctr_str else None
                    except (ValueError, AttributeError):
                        ctr = None

                    try:
                        position = float(row.get('Avg. position', '').replace(',', '.') or '0')
                    except (ValueError, AttributeError):
                        position = None

                    url_data[url] = WebmasterMetrics(
                        url=url,
                        yandex_clicks=clicks,
                        yandex_impressions=impressions,
                        yandex_ctr=ctr,
                        yandex_position=position
                    )

        except Exception as e:
            print(f"Error parsing Yandex CSV {csv_path}: {e}")

        return url_data

    def parse_gsc_zip(self, zip_path: Path) -> Dict[str, WebmasterMetrics]:
        """
        Parse Google Search Console ZIP export.
        Looks for 'Страницы.csv' (Pages.csv) inside the ZIP.
        """
        url_data = {}

        try:
            with zipfile.ZipFile(zip_path, 'r') as zf:
                # Look for pages file (could be named differently due to encoding)
                pages_file = None
                for name in zf.namelist():
                    # Check for common variations of "Pages" in Russian
                    if 'страниц' in name.lower() or 'pages' in name.lower():
                        pages_file = name
                        break

                if not pages_file:
                    # Try to find the largest CSV file as fallback
                    csv_files = [n for n in zf.namelist() if n.lower().endswith('.csv')]
                    if csv_files:
                        # Get the file with most data (likely pages)
                        pages_file = max(csv_files, key=lambda n: zf.getinfo(n).file_size)

                if pages_file:
                    with zf.open(pages_file) as f:
                        # Decode with UTF-8 (GSC exports are UTF-8)
                        content = f.read().decode('utf-8')
                        reader = csv.DictReader(io.StringIO(content))

                        for row in reader:
                            # GSC Pages CSV columns (Russian):
                            # Страница, Клики, Показы, CTR, Позиция
                            # Or in English: Page, Clicks, Impressions, CTR, Position

                            url = None
                            clicks = impressions = ctr = position = None

                            # Try both Russian and English column names
                            for key in row.keys():
                                key_lower = key.lower()
                                if 'страниц' in key_lower or 'page' in key_lower or 'url' in key_lower:
                                    url = row[key]
                                # Handle both "Клики" (Cyrillic K) and "Kлики" (Latin K + Cyrillic)
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
                                        ctr = float(ctr_str) if ctr_str else None
                                    except (ValueError, AttributeError):
                                        ctr = None
                                elif 'позиц' in key_lower or 'position' in key_lower:
                                    try:
                                        position = float(row[key].replace(',', '.'))
                                    except (ValueError, AttributeError):
                                        position = None

                            if url:
                                url_data[url] = WebmasterMetrics(
                                    url=url,
                                    gsc_clicks=clicks,
                                    gsc_impressions=impressions,
                                    gsc_ctr=ctr,
                                    gsc_position=position
                                )

        except Exception as e:
            print(f"Error parsing GSC ZIP {zip_path}: {e}")

        return url_data

    def load_latest_reports(self) -> Dict[str, WebmasterMetrics]:
        """
        Load the latest available webmaster reports.
        Returns a dictionary mapping URLs to their metrics.
        """
        url_metrics = {}

        # Find latest Yandex CSV file (pages export)
        yandex_files = list(self.webmasters_dir.glob("[YOUR-DOMAIN]_*.csv"))
        if yandex_files:
            # Filter to only pages files (have "Path" column, not "Query")
            pages_files = []
            for f in yandex_files:
                try:
                    with open(f, 'r', encoding='utf-8') as csvfile:
                        first_line = csvfile.readline()
                        # Check if it's a pages file (has "Path") vs query file (has "Query")
                        if '"Path"' in first_line or 'Path,' in first_line:
                            pages_files.append(f)
                except Exception:
                    continue

            if pages_files:
                latest_yandex = max(pages_files, key=lambda p: p.stat().st_mtime)
                print(f"Loading Yandex data from: {latest_yandex.name}")
                yandex_data = self.parse_yandex_csv(latest_yandex)
                url_metrics.update(yandex_data)

        # Find latest GSC ZIP file
        gsc_files = list(self.webmasters_dir.glob("*Performance*.zip"))
        if gsc_files:
            latest_gsc = max(gsc_files, key=lambda p: p.stat().st_mtime)
            print(f"Loading GSC data from: {latest_gsc.name}")
            gsc_data = self.parse_gsc_zip(latest_gsc)

            # Merge GSC data with existing Yandex data
            for url, gsc_metrics in gsc_data.items():
                if url in url_metrics:
                    # Merge with existing Yandex data
                    url_metrics[url].gsc_clicks = gsc_metrics.gsc_clicks
                    url_metrics[url].gsc_impressions = gsc_metrics.gsc_impressions
                    url_metrics[url].gsc_ctr = gsc_metrics.gsc_ctr
                    url_metrics[url].gsc_position = gsc_metrics.gsc_position
                else:
                    # Add new GSC-only entry
                    url_metrics[url] = gsc_metrics

        self.url_metrics = url_metrics
        return url_metrics

    def get_metrics_for_url(self, url: str) -> Optional[WebmasterMetrics]:
        """Get metrics for a specific URL."""
        # Try exact match first
        if url in self.url_metrics:
            return self.url_metrics[url]

        # Try without protocol/domain (path only)
        from urllib.parse import urlparse
        parsed = urlparse(url)
        path = parsed.path

        for metric_url, metrics in self.url_metrics.items():
            if urlparse(metric_url).path == path:
                return metrics

        return None

    def enrich_page_data(self, pages: List[Dict]) -> List[Dict]:
        """
        Enrich page data dictionaries with webmaster metrics.
        Expects list of dicts with 'url' key.
        """
        for page in pages:
            url = page.get('url', '')
            metrics = self.get_metrics_for_url(url)

            if metrics:
                # Yandex metrics
                page['yandex_clicks'] = metrics.yandex_clicks
                page['yandex_impressions'] = metrics.yandex_impressions
                page['yandex_ctr'] = metrics.yandex_ctr
                page['yandex_position'] = metrics.yandex_position
                # GSC metrics
                page['gsc_clicks'] = metrics.gsc_clicks
                page['gsc_impressions'] = metrics.gsc_impressions
                page['gsc_ctr'] = metrics.gsc_ctr
                page['gsc_position'] = metrics.gsc_position
            else:
                # Yandex metrics
                page['yandex_clicks'] = None
                page['yandex_impressions'] = None
                page['yandex_ctr'] = None
                page['yandex_position'] = None
                # GSC metrics
                page['gsc_clicks'] = None
                page['gsc_impressions'] = None
                page['gsc_ctr'] = None
                page['gsc_position'] = None

        return pages


if __name__ == "__main__":
    # Quick test
    parser = WebmasterDataParser()
    print("Loading webmaster reports...")

    metrics = parser.load_latest_reports()
    print(f"\nLoaded metrics for {len(metrics)} URLs")

    if metrics:
        print("\nSample entries (first 5):")
        for i, (url, metric) in enumerate(list(metrics.items())[:5], 1):
            print(f"{i}. {url}")
            if metric.yandex_clicks is not None or metric.yandex_impressions is not None:
                print(f"   Yandex: {metric.yandex_clicks} clicks, {metric.yandex_impressions} impressions, "
                      f"pos={metric.yandex_position}")
            if metric.gsc_clicks is not None or metric.gsc_impressions is not None:
                print(f"   GSC: {metric.gsc_clicks} clicks, {metric.gsc_impressions} impressions, "
                      f"pos={metric.gsc_position}")

"""
Sitemap Parser for SEO Content Audit
Fetches and parses sitemap.xml, filters for blog and collection pages.
"""

import requests
from xml.etree import ElementTree
from typing import List, Dict, Optional
from dataclasses import dataclass
from datetime import datetime

try:
    from .config import SITEMAP_URL, USER_AGENT
except ImportError:
    # Fallback defaults if config not set up
    SITEMAP_URL = None
    USER_AGENT = "Mozilla/5.0 (compatible; content-audit/1.0)"


@dataclass
class SitemapEntry:
    """Represents a single URL entry from sitemap."""
    url: str
    lastmod: Optional[str]
    content_type: str  # 'blog', 'collection', 'product', 'other'


class SitemapParser:
    """Parses sitemap.xml and filters relevant pages."""

    NAMESPACES = {
        'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'
    }

    def __init__(self, sitemap_url: str = None):
        self.sitemap_url = sitemap_url or SITEMAP_URL
        if not self.sitemap_url:
            raise ValueError("sitemap_url required. Set in config.py or pass as argument.")
        self.entries: List[SitemapEntry] = []

    def fetch_sitemap(self) -> str:
        """Fetch sitemap XML content from URL."""
        response = requests.get(
            self.sitemap_url,
            headers={'User-Agent': USER_AGENT},
            timeout=30
        )
        response.raise_for_status()
        return response.text

    def parse(self, xml_content: str) -> List[SitemapEntry]:
        """Parse sitemap XML and extract URL entries."""
        root = ElementTree.fromstring(xml_content)
        entries = []

        # Find all <url> elements
        for url_elem in root.findall('sm:url', self.NAMESPACES):
            loc = url_elem.find('sm:loc', self.NAMESPACES)
            lastmod = url_elem.find('sm:lastmod', self.NAMESPACES)

            if loc is not None and loc.text:
                url = loc.text.strip()
                lastmod_text = lastmod.text.strip() if lastmod is not None and lastmod.text else None
                content_type = self._determine_content_type(url)

                entries.append(SitemapEntry(
                    url=url,
                    lastmod=lastmod_text,
                    content_type=content_type
                ))

        self.entries = entries
        return entries

    def _determine_content_type(self, url: str) -> str:
        """Determine content type based on URL path."""
        if '/blogs/' in url or '/blog/' in url:
            return 'blog'
        elif '/collection/' in url or '/collections/' in url:
            return 'collection'
        elif '/product/' in url or '/products/' in url:
            return 'product'
        else:
            return 'other'

    def filter_blog_and_collections(self) -> List[SitemapEntry]:
        """Return only blog and collection pages."""
        return [
            entry for entry in self.entries
            if entry.content_type in ('blog', 'collection')
        ]

    def get_all(self) -> List[SitemapEntry]:
        """Return all parsed entries."""
        return self.entries

    def fetch_and_parse(self, filter_content: bool = True) -> List[SitemapEntry]:
        """Convenience method to fetch and parse in one call."""
        xml_content = self.fetch_sitemap()
        self.parse(xml_content)

        if filter_content:
            return self.filter_blog_and_collections()
        return self.entries

    def get_stats(self) -> Dict:
        """Return statistics about parsed sitemap."""
        type_counts = {}
        for entry in self.entries:
            type_counts[entry.content_type] = type_counts.get(entry.content_type, 0) + 1

        return {
            'total': len(self.entries),
            'by_type': type_counts,
            'blog_and_collection': len(self.filter_blog_and_collections())
        }


if __name__ == "__main__":
    # Quick test
    parser = SitemapParser()
    print(f"Fetching sitemap from {parser.sitemap_url}...")

    entries = parser.fetch_and_parse(filter_content=False)
    stats = parser.get_stats()

    print(f"\nSitemap Statistics:")
    print(f"  Total URLs: {stats['total']}")
    print(f"  By type:")
    for content_type, count in stats['by_type'].items():
        print(f"    - {content_type}: {count}")
    print(f"  Blog + Collection: {stats['blog_and_collection']}")

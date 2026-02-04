"""
Page Scraper for [YOUR-DOMAIN]
Extracts title, H1, meta description, and content from pages.
"""

import requests
from bs4 import BeautifulSoup
from typing import Dict, Optional, List
from dataclasses import dataclass, field
import time
import re


@dataclass
class PageData:
    """Extracted data from a single page."""
    url: str
    title: Optional[str] = None
    h1: Optional[str] = None
    meta_description: Optional[str] = None
    word_count: int = 0
    content_text: str = ""
    top_keywords: List[str] = field(default_factory=list)
    error: Optional[str] = None


class PageScraper:
    """Scrapes individual pages for SEO-relevant content."""

    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (compatible; [YOUR-PROJECT]-content-audit/1.0)',
        'Accept': 'text/html,application/xhtml+xml',
        'Accept-Language': 'ru-RU,ru;q=0.9,en;q=0.8'
    }

    def __init__(self, delay: float = 0.5):
        self.delay = delay  # Delay between requests in seconds
        self.session = requests.Session()
        self.session.headers.update(self.HEADERS)

    def scrape(self, url: str) -> PageData:
        """Scrape a single page and extract data."""
        page_data = PageData(url=url)

        try:
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            response.encoding = 'utf-8'

            soup = BeautifulSoup(response.text, 'lxml')

            # Extract title
            title_tag = soup.find('title')
            if title_tag:
                page_data.title = title_tag.get_text(strip=True)

            # Extract H1 (first one)
            h1_tag = soup.find('h1')
            if h1_tag:
                page_data.h1 = h1_tag.get_text(strip=True)

            # Extract meta description
            meta_desc = soup.find('meta', attrs={'name': 'description'})
            if meta_desc and meta_desc.get('content'):
                page_data.meta_description = meta_desc['content'].strip()

            # Extract main content text
            content_text = self._extract_content(soup)
            page_data.content_text = content_text
            page_data.word_count = self._count_words(content_text)

        except requests.RequestException as e:
            page_data.error = str(e)
        except Exception as e:
            page_data.error = f"Parse error: {str(e)}"

        return page_data

    def _extract_content(self, soup: BeautifulSoup) -> str:
        """Extract main text content from page."""
        # Try to find main content area FIRST before removing anything
        main_content = None

        # InSales-specific and common content selectors
        content_selectors = [
            # InSales specific
            '.article-content',
            '.static-text',
            '.article_content',
            '.article_page',
            '.article-page',
            '#article',
            '.blog-article',
            '.blog_article',
            # Standard blog selectors
            'article',
            '.blog-content',
            '.post-content',
            '.entry-content',
            # E-commerce selectors
            '.product-description',
            '.collection-description',
            '.description',
            # Generic selectors
            'main',
            '.main-content',
            '#content',
            '.content',
            '#main'
        ]

        for selector in content_selectors:
            if selector.startswith('.') or selector.startswith('#'):
                main_content = soup.select_one(selector)
            else:
                main_content = soup.find(selector)
            if main_content:
                # Check if it has substantial content (not just navigation)
                text = main_content.get_text(separator=' ', strip=True)
                if len(text) > 100:  # At least 100 characters
                    break
                else:
                    main_content = None

        # If we found content, clean it up
        if main_content:
            # Remove unwanted elements within the content
            for tag in main_content.find_all(['script', 'style', 'button', 'form', 'input', 'noscript', 'iframe']):
                tag.decompose()

            text = main_content.get_text(separator=' ', strip=True)
            # Clean up whitespace
            text = re.sub(r'\s+', ' ', text)
            return text

        return ""

    def _count_words(self, text: str) -> int:
        """Count words in text (handles Russian text)."""
        if not text:
            return 0
        # Split by whitespace and count non-empty tokens
        words = [w for w in text.split() if len(w) > 0]
        return len(words)

    def scrape_batch(self, urls: List[str], progress_callback=None) -> List[PageData]:
        """Scrape multiple pages with delay between requests."""
        results = []

        for i, url in enumerate(urls):
            page_data = self.scrape(url)
            results.append(page_data)

            if progress_callback:
                progress_callback(i + 1, len(urls), url, page_data)

            # Delay between requests (except for last one)
            if i < len(urls) - 1:
                time.sleep(self.delay)

        return results


if __name__ == "__main__":
    # Quick test
    scraper = PageScraper()

    test_url = "https://[YOUR-DOMAIN]/blogs/blog/chto-takoe-lofery"
    print(f"Scraping: {test_url}")

    data = scraper.scrape(test_url)

    print(f"\nResults:")
    print(f"  Title: {data.title}")
    print(f"  H1: {data.h1}")
    print(f"  Meta Description: {data.meta_description[:100]}..." if data.meta_description else "  Meta Description: None")
    print(f"  Word Count: {data.word_count}")
    if data.error:
        print(f"  Error: {data.error}")

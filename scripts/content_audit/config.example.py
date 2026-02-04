"""
Configuration for Content Audit Utility

Copy config.example.py to config.py and update with your project settings.
"""

# Your website domain (without https://)
DOMAIN = "www.example.com"

# Sitemap URL
SITEMAP_URL = f"https://{DOMAIN}/sitemap.xml"

# User agent for requests
USER_AGENT = f"Mozilla/5.0 (compatible; content-audit/1.0; +https://{DOMAIN})"

# URL patterns to include in audit (regex patterns)
# Default: blog posts and collection/category pages
INCLUDE_PATTERNS = [
    r'/blogs?/',      # Blog posts
    r'/collection/',  # Collections/categories
    r'/category/',    # Alternative category pattern
]

# URL patterns to exclude (regex patterns)
EXCLUDE_PATTERNS = [
    r'/tag/',         # Tag pages
    r'/author/',      # Author pages
    r'\?',            # URLs with query parameters
]

# Yandex Webmaster file pattern (glob)
# Files are typically named: www.example.com_*.csv
YANDEX_FILE_PATTERN = f"{DOMAIN}_*.csv"

# GSC export file pattern (glob)
GSC_FILE_PATTERN = f"*{DOMAIN}*Performance*.zip"

# Minimum word count threshold for content gaps report
MIN_WORD_COUNT = 300

# Output directory (relative to project root)
OUTPUT_DIR = "research/content-audit"

# Webmaster data directory (relative to project root)
WEBMASTERS_DIR = "research/webmasters"

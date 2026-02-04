---
name: analyze-webmaster
description: Analyze Yandex Webmaster reports and generate insights
---

# Analyze Webmaster

When this skill is invoked:

1. Determine report date:
   - If user specifies a date (e.g., /analyze-webmaster 2026-01-27), use that
   - Otherwise, use today's date
   - Format: YYYY-MM-DD

2. Locate Yandex Webmaster files in research/webmasters/:
   - Search for *.csv.gz files (query reports)
   - Search for *.zip files (performance exports)
   - If files not found, ask user to upload them first

3. Extract and process data:
   - Extract .csv.gz file (search queries with 7 days of data)
   - Extract .zip file (contains Russian CSV files: Запросы, Страницы, Устройства, etc.)
   - Use proper UTF-8 encoding for Russian text
   - Handle both formats automatically

4. Analyze key metrics:
   - Overall performance: clicks, impressions, CTR, average position
   - Top queries by clicks and impressions
   - Brand vs generic query breakdown
   - Query intent categories (navigational, informational, transactional)
   - Top performing pages
   - Device breakdown (mobile vs desktop)
   - Geographic distribution
   - Search appearance features

5. Identify opportunities:
   - High impression, low CTR queries (title/description optimization)
   - Queries ranking 4-10 (quick win potential)
   - Content gaps (queries without matching pages)
   - Successful content patterns to replicate
   - Brand-specific opportunities

6. Generate report:
   - Save as: research/webmasters/analysis-[YYYY-MM-DD].md
   - Include: executive summary, key metrics, top performers, opportunities
   - Add visual data tables (markdown format)
   - Provide actionable recommendations with estimated impact
   - Include strategic insights and growth potential

7. Clean up:
   - Keep original .csv.gz and .zip files
   - Keep extracted CSV files for reference
   - Keep generated report

8. Provide user with:
   - Path to generated report
   - Summary of key findings (3-5 bullet points)
   - Top 3 actionable recommendations
   - Estimated growth potential

Note: This skill uses the Bash agent to process CSV files efficiently using command-line tools for large datasets.

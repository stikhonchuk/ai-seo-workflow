---
name: analyze-gsc
description: Analyze Google Search Console query trend reports
---

# Analyze Gsc

When this skill is invoked:

1. Determine report date:
   - If user specifies a date (e.g., /analyze-gsc 2026-01-27), use that
   - Otherwise, use today's date
   - Format: YYYY-MM-DD

2. Locate GSC files in research/webmasters/:
   - Search for *.csv.gz files with query trend data
   - These files contain: Query column + 7 daily impression columns
   - File format: www.[YOUR-DOMAIN]_[ID].csv.gz
   - If file not found, ask user to export from Google Search Console

3. Extract and process data:
   - Extract .csv.gz file (7-day query impression trends)
   - Parse CSV with proper encoding (UTF-8 for Russian queries)
   - Filter out empty rows (queries with no impressions)
   - Most queries (90%+) will be empty - this is normal

4. Analyze key metrics:
   - Date range from CSV headers
   - Total queries vs queries with impressions
   - Total impressions across all queries
   - Top queries by total impressions (7-day sum)
   - Daily impression trends per query

5. Categorize queries:
   - Brand queries (Premiata, Baldinini, Hogan, Hotto, Bagatto, etc.)
   - Size conversion queries (размер, см, итальянский, стелька)
   - Product queries (кроссовки, обувь, куртка, джинсы)
   - Informational queries (что за бренд, история, описание)
   - Navigational queries (brand names only)

6. Identify trends and patterns:
   - Queries with increasing daily impressions
   - Queries with decreasing trends
   - Spike queries (sudden high impressions)
   - Consistent performers
   - Seasonal patterns (jacket queries in cold weather, etc.)

7. Compare with Yandex data (if available):
   - Which queries perform better on Google vs Yandex?
   - Platform-specific opportunities
   - Content gaps visible only in GSC data

8. Generate report:
   - Save as: research/webmasters/gsc-analysis-[YYYY-MM-DD].md
   - Include: executive summary, date range, data quality note
   - Top performers table (query + 7 daily impressions + total)
   - Category breakdown with percentages
   - Trend analysis with specific examples
   - Cross-platform insights (if Yandex data exists)
   - Actionable recommendations
   - Growth opportunities with estimated impact

9. Provide user with:
   - Path to generated report
   - Key findings (3-5 bullets):
     * Total queries with impressions vs total in file
     * Total impressions for 7-day period
     * Top performing query categories
     * Notable trends or patterns
   - Top 3 actionable recommendations
   - Next steps

Note: GSC query trend reports typically show impression counts only (not clicks/CTR/position). This is supplementary data to full Yandex Webmaster reports.

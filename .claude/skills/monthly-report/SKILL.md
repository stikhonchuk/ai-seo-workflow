---
name: monthly-report
description: Generate monthly SEO performance report
---

# Monthly Report

When this skill is invoked:

1. Determine the month to report on:
   - If user specifies a month (e.g., /monthly-report 2026-02), use that
   - Otherwise, use previous month
   - Format: YYYY-MM

2. Create report file:
   - Use template from: research/analytics/monthly-reports/REPORT_TEMPLATE.md
   - Save as: research/analytics/monthly-reports/report-[YYYY-MM].md
   - Replace all [placeholders] with actual data or instructions to fill

3. Create data snapshot directory:
   - Create: research/analytics/data-snapshots/[YYYY-MM]/
   - Add README.md with instructions for data collection

4. Remind user to collect data from:
   - Yandex.Metrica (traffic, conversions, behavior)
   - Yandex Webmaster (indexing, rankings, errors)
   - Google Search Console (supplementary data)
   - Google Analytics 4 (supplementary data)

5. Update the report with:
   - Baseline data from website audit (if first report)
   - Month-over-month comparisons
   - Progress on critical issues from audit
   - Schema implementation progress
   - Content publication progress

6. Provide user with:
   - Path to new report file
   - Checklist of data to collect
   - Instructions for finalizing report

Note: This creates the report structure. User must fill in actual metrics from analytics tools.

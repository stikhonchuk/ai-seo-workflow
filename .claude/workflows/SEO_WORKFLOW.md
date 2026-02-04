# SEO Workflow for [YOUR-DOMAIN]

## Overview
Complete SEO optimization workflow for shoe e-commerce website, covering keyword research, content planning, and content creation.

---

## Phase 1: Website Analysis & Audit

### 1.1 Current State Assessment
- [ ] Analyze existing website structure
- [ ] Review current product categories
- [ ] Identify existing content assets
- [ ] Check current SEO implementation (meta tags, headings, alt texts)
- [ ] Analyze site speed and technical SEO
- [ ] Review mobile responsiveness

### 1.2 Target Audience Definition
- [ ] Define primary customer personas
- [ ] Identify customer pain points
- [ ] Map customer journey stages
- [ ] Determine search intent patterns

---

## Phase 2: Keyword Research

### 2.1 Seed Keyword Collection
- [ ] Product-focused keywords (shoe types, brands)
- [ ] Informational keywords (how-to, guides)
- [ ] Commercial keywords (best shoes for, reviews)
- [ ] Local keywords (if applicable)

### 2.2 Keyword Research Tools
- **Free Tools:**
  - Google Keyword Planner
  - Google Search Console (existing data)
  - Google Trends
  - AnswerThePublic
  - Ubersuggest (limited free)

- **Paid Tools (optional):**
  - Ahrefs
  - SEMrush
  - Moz Keyword Explorer

### 2.3 Keyword Analysis Criteria
For each keyword, document:
- Search volume (monthly)
- Keyword difficulty (competition)
- Search intent (informational, commercial, transactional, navigational)
- Current ranking (if any)
- Business relevance (1-10 score)
- Priority level (High/Medium/Low)

### 2.4 Keyword Categorization
Organize keywords by:
- **Transactional:** Buy, shop, order (product pages)
- **Commercial:** Best, review, comparison (buying guides)
- **Informational:** How to, what is, guide (blog content)
- **Navigational:** Brand names, specific products

---

## Phase 3: Competitor Analysis

### 3.1 Identify Competitors
- [ ] Direct competitors (similar shoe e-commerce sites)
- [ ] Indirect competitors (general footwear retailers)
- [ ] Content competitors (shoe blogs, review sites)

### 3.2 Competitor Research
For each competitor:
- [ ] What keywords are they ranking for?
- [ ] What content types do they produce?
- [ ] What's their content frequency?
- [ ] What's their backlink profile like?
- [ ] What content gaps exist?

### 3.3 Opportunity Identification
- [ ] Keywords competitors rank for but you don't
- [ ] Content topics they're missing
- [ ] Better content angle opportunities
- [ ] Link building opportunities

---

## Phase 4: Content Strategy & Publication Plan

### 4.1 Content Pillars
Define 4-6 main content themes:
- Example: "Shoe Care & Maintenance"
- Example: "Shoe Buying Guides"
- Example: "Fashion & Style Tips"
- Example: "Shoe Technology & Innovation"
- Example: "Foot Health & Comfort"

### 4.2 Content Types
- **Product Pages:** Optimized product descriptions
- **Category Pages:** Collection overviews
- **Blog Articles:** Educational, informational content
- **Buying Guides:** Comparison and recommendation content
- **How-to Guides:** Practical tutorials
- **FAQ Pages:** Common questions answered
- **Video Content:** Unboxing, reviews, styling tips

### 4.3 Content Calendar Template
For each content piece:
- Title (working title)
- Primary keyword
- Secondary keywords (2-5)
- Search intent
- Content type
- Target word count
- Target audience
- Publication date
- Author/Responsible person
- Status (Planning/Research/Writing/Editing/Published)
- Internal linking opportunities
- CTA (Call to Action)

### 4.4 Publication Frequency
- Week 1-4: 2-3 articles per week (foundation building)
- Month 2-3: 2 articles per week (consistent publishing)
- Month 4+: 1-2 articles per week (maintenance + updates)

---

## Phase 5: Content Creation Guidelines

### 5.1 SEO Writing Best Practices
- **Title Tag:** Include primary keyword, keep under 60 characters
- **Meta Description:** Compelling summary with keyword, 150-160 characters
- **URL Structure:** Short, descriptive, include keyword
- **Headings:** H1 (one per page), H2, H3 hierarchy with keywords
- **Keyword Usage:** Natural placement, avoid keyword stuffing
- **Content Length:** Min 800 words for blog posts, 1,500+ for pillar content
- **Images:** Optimized file size, descriptive alt text with keywords
- **Internal Links:** 3-5 relevant internal links per article
- **External Links:** 1-2 authoritative sources
- **CTA:** Clear call-to-action in each piece

### 5.2 Content Structure Template
```
1. Catchy Title (with primary keyword)
2. Introduction (hook + what reader will learn)
3. Table of Contents (for long articles)
4. Main Content (H2 sections with H3 subsections)
5. Key Takeaways / Summary
6. FAQ Section (optional but recommended)
7. Call-to-Action
8. Related Articles/Products
```

### 5.3 E-commerce Specific Elements
- Product schema markup
- Customer reviews integration
- Product comparison tables
- Size guides
- Shipping/return information
- Trust signals (security badges, guarantees)

---

## Phase 6: Content Optimization & Publishing

### 6.1 Pre-Publishing Checklist
- [ ] Primary keyword in title, first paragraph, and conclusion
- [ ] Secondary keywords naturally distributed
- [ ] All images compressed and have alt text
- [ ] Internal links added (minimum 3)
- [ ] External authoritative links added (1-2)
- [ ] Meta title and description optimized
- [ ] URL is SEO-friendly
- [ ] Mobile-friendly formatting
- [ ] Schema markup added (where applicable)
- [ ] CTA is clear and compelling

### 6.2 Post-Publishing Tasks
- [ ] Submit URL to Google Search Console
- [ ] Share on social media channels
- [ ] Add to email newsletter (if applicable)
- [ ] Monitor for indexing
- [ ] Track initial rankings

---

## Phase 7: Monitoring & Improvement

### 7.1 Monthly Content Audit (End of Month)

**Run before monthly report and next month planning:**

```bash
# Full content audit (~10 minutes)
venv/bin/python scripts/content_audit/main.py --full
```

**What it does:**
- Scans all blog and collection pages (~585 pages)
- Extracts: title, H1, meta, word count, top keywords
- Enriches with GSC data (clicks, impressions, positions)
- Generates reports: CSV, JSON, Markdown

**Output files:**
```
research/content-audit/
├── site-content-audit.csv      # Main report (Excel-friendly)
├── site-content-audit.json     # Full data + statistics
├── content-gaps.md             # Low word count pages
└── audit-log.txt               # Execution log
```

**How to use:**
1. **For monthly report:** Use current metrics from CSV
2. **For planning next month:** Check existing topics to avoid duplication
3. **For content gaps:** Review `content-gaps.md` for improvement opportunities
4. **For tracking progress:** Compare metrics month-over-month

**Frequency:**
- **Required:** Last day of each month (before monthly report)
- **Optional:** Mid-month update (`--update-webmaster` for faster GSC refresh)

### 7.2 Key Metrics to Track
- **Rankings:** Track keyword positions (weekly/monthly)
- **Traffic:** Organic sessions, pageviews, bounce rate
- **Engagement:** Time on page, pages per session
- **Conversions:** Goal completions, revenue from organic
- **Technical:** Page speed, crawl errors, indexing status
- **Content Quality:** Word count, keyword coverage (from audit)

### 7.3 Tools for Monitoring
- Google Search Console
- Google Analytics 4
- Yandex Webmaster
- Content Audit Utility (scripts/content_audit/)
- Rank tracking tools (SERPWatcher, Ahrefs, SEMrush)
- Page speed tools (PageSpeed Insights, GTmetrix)

### 7.4 Content Updates
- Review and update content every 6 months
- Refresh statistics and outdated information
- Add new sections based on user questions
- Improve underperforming content (use content-gaps.md)
- Consolidate thin or duplicate content
- Expand low word count pages (<300 words)

---

## Phase 8: Link Building Strategy

### 8.1 Internal Linking
- Link from high-authority pages to new content
- Create topic clusters around pillar content
- Use descriptive anchor text

### 8.2 External Link Building
- Guest posting on fashion/lifestyle blogs
- Product reviews and collaborations
- Resource page link building
- Broken link building
- Digital PR and brand mentions
- Social media engagement

---

## Success Metrics & Goals

### Month 1-3 (Foundation)
- 20-30 pieces of optimized content published
- Basic technical SEO issues resolved
- Keyword tracking setup complete
- 10-20% increase in organic traffic

### Month 4-6 (Growth)
- 50+ total optimized pages
- Ranking in top 20 for 30+ target keywords
- 30-50% increase in organic traffic
- Initial conversion tracking and optimization

### Month 7-12 (Scaling)
- 100+ total optimized pages
- Ranking in top 10 for 50+ target keywords
- 100%+ increase in organic traffic
- Established authority in niche
- Consistent monthly organic revenue growth

---

## Next Steps
1. Complete website audit
2. Execute keyword research
3. Create detailed content calendar
4. Begin content production
5. Monitor and iterate

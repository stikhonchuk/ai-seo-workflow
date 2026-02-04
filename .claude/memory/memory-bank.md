# Memory Bank: [YOUR-PROJECT] SEO Project

## Purpose
This file stores long-term knowledge, insights, and learnings from your SEO optimization project. It serves as a persistent memory that carries forward across sessions.

---

## Project Context

### Website Information
- **Domain:** [YOUR-DOMAIN]
- **Industry:** [YOUR-INDUSTRY]
- **Target Market:** [YOUR-MARKET]
- **Primary Search Engine:** [Google/Yandex/Both]
- **Content Language:** [LANGUAGE]

### Business Model
- [Describe your business model]
- [Product categories]
- [Target audience]

---

## Key Insights & Learnings

### SEO Strategy Insights

#### Market-Specific Notes
- *Add learnings specific to your market*

#### E-commerce SEO Learnings
- Product pages need minimum 500 words of unique content
- Category pages should have 400-600 words of unique content
- User reviews are powerful for both SEO and conversions
- Schema markup is critical (Product, Review, BreadcrumbList)
- Internal linking between blog content and products drives conversions

#### Content Strategy Insights
- **Buying guides** perform best for commercial intent keywords
- **How-to guides** build authority and attract informational traffic
- **Long-tail keywords** are easier to rank for initially
- **Seasonal content** should be published 2-3 months in advance
- **2,000+ word guides** tend to rank better than shorter articles

#### Image Requirements
- **Hero image mandatory** for every blog post
- **Specifications:** 16:9 aspect ratio, 1920x1080px recommended
- **No text on images** - Text overlays added in CMS
- **No faces/logos** - Avoid licensing issues
- Use consistent style across all images

---

## Important Decisions & Rationale

### Strategic Decisions

#### Content Frequency: 2 Articles/Week
**Rationale:**
- Sustainable pace for quality content
- Allows time for proper keyword research and optimization
- 8-10 articles/month = 100+ articles in 12 months
- Quality over quantity for long-term SEO success

#### Content Mix: 50% Buying Guides, 25% How-To, 25% Other
**Rationale:**
- Buying guides target commercial intent (higher conversion)
- How-to content builds authority and trust
- Mix serves different stages of buyer journey

---

## Research Data

### Keyword Research

#### Seed Keywords Identified
*Add your keywords here as you research*

#### Target Keyword Ranges
- **High competition:** 10,000+ monthly searches
- **Medium competition:** 1,000-10,000 monthly searches
- **Low competition (long-tail):** 100-1,000 monthly searches
- **Initial focus:** Medium and low competition for quick wins

### Content Ideas Bank

#### Evergreen Topics
- *Add evergreen content ideas*

#### Seasonal Topics
- **Spring/Summer:** *Add seasonal ideas*
- **Fall/Winter:** *Add seasonal ideas*

#### Problem-Solving Content
- *Add problem-solving content ideas*

---

## Tools & Resources

### Essential SEO Tools
- **Google Search Console** - Primary search engine
- **Google Analytics 4** - Traffic analysis
- **Google Keyword Planner** - Keyword research
- **Yandex Webmaster** - If targeting Russian market
- **Yandex Wordstat** - Russian keyword research

### Content Creation Tools
- **Grammarly** - Grammar checking
- **Hemingway Editor** - Readability testing
- **TinyPNG** - Image compression

---

## Content Audit Utility

### Purpose
Python utility for analyzing existing site content to avoid duplication when creating new content.

### Location
`scripts/content_audit/` - See README.md for documentation

### Monthly Workflow
**Run BEFORE creating monthly report (last day of month)**

```bash
python scripts/content_audit/main.py --full
```

### Output Files
```
research/content-audit/
├── site-content-audit.csv      # Main report (Excel-friendly)
├── site-content-audit.json     # Full data + statistics
├── content-gaps.md             # Low word count pages
└── audit-log.txt               # Execution log
```

---

## Common Issues & Solutions

### Problem: Low Rankings Despite Good Content
**Potential Solutions:**
- Check technical SEO (indexing, speed, mobile)
- Improve internal linking to that page
- Add more external backlinks
- Update content with fresh information
- Enhance user engagement signals

### Problem: High Bounce Rate on Product Pages
**Potential Solutions:**
- Improve product descriptions
- Add better images and videos
- Include customer reviews
- Add related product recommendations
- Check page load speed

---

## Quarterly Review Checklist

### Every 3 Months Review:
- [ ] Top 20 performing articles
- [ ] Bottom 20 performing articles (improve or remove)
- [ ] Keyword ranking changes
- [ ] Organic traffic trends
- [ ] Conversion rate from organic traffic
- [ ] New competitor activities
- [ ] Technical SEO health
- [ ] Content gaps and opportunities
- [ ] Update content calendar for next quarter

---

## Lessons Learned

### What's Working Well
*Track successful tactics and strategies*

### What Needs Improvement
*Track challenges and areas for optimization*

### Key Mistakes to Avoid
*Document errors and how to prevent them*

---

**Last Updated:** [DATE]
**Next Review:** [DATE] (3 months)

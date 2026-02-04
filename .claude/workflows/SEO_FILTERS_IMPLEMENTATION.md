# InSales SEO Filters Implementation Guide

**Platform Feature:** InSales-specific automated landing pages
**Documentation:** https://www.insales.ru/collection/doc-products/product/seo-filtry
**Purpose:** Create 100-200+ optimized landing pages for long-tail keyword targeting

---

## What Are SEO Filters?

**Definition:** SEO filters are auto-populated subcategories that create dedicated landing pages for specific product combinations based on parameters (brand, color, size, material, etc.).

**How They Work:**
- Select parameters (e.g., Brand=Premiata, Color=White, Type=Sneakers)
- System automatically populates matching products
- Creates clean URL: `/collection/premiata-white-sneakers`
- Automatically added to sitemap.xml
- No manual content creation needed

**Key Benefits:**
- ✅ Capture long-tail keyword traffic
- ✅ Create 100-200+ indexed pages with minimal effort
- ✅ SEO-friendly URLs (not query parameters)
- ✅ Auto-updates as inventory changes
- ✅ Improves user navigation

---

## Implementation Strategy for [YOUR-DOMAIN]

### Phase 1: Brand Filters (Priority 1)
**Timeline:** Week 1-2
**Effort:** 5-10 hours total

Create one filter per brand (33 filters total):

**Main Priority Brands:**
1. INUIKII (⭐ main brand - luxury winter boots)
2. Premiata (⭐ main brand - premium Italian sneakers)

**Italian Designer Brands (21 filters):**
3. Baldinini
4. Doucal's
5. Gianmarco Lorenzi
6. Giorgio Fabiani
7. Nila&Nila
8. Pertini
9. Voile Blanche
10. Byblos
11. D.A.T.E.
12. Iceberg
13. Lab Milano
14. Luca Guerrini
15. Luigi Traini
16. Marzetti
17. Nando Muzi
18. Pakerson
19. Renzi
20. L.Traini
21. Tuffoni
22. Vittorio Virgili

**International Brands (4 filters):**
23. Stuart Weitzman
24. Goodman
25. Wonders
26. Lemon Jelly

**Contemporary Brands (8 filters):**
27. Bagatto
28. Barcly
29. Donna Soft
30. Fruit
31. Left and Right
32. Lesilla
33. SHADA

**Meta Tag Format:**
- Title: `{Brand} купить в Москве | Официальный интернет-магазин [YOUR-PROJECT].ru`
- Description: `{Brand} - оригинальная обувь от итальянского производителя. Доставка по России. ✓ Гарантия качества ✓ Размеры в наличии`

### Phase 2: Brand + Product Type (Priority 2)
**Timeline:** Week 3-4
**Effort:** 8-12 hours
**Target:** 50 filters

Top 10 brands × 5 main product types = 50 filters

**Product Types:**
- Кроссовки (Sneakers)
- Сапоги (Boots)
- Ботильоны (Booties)
- Туфли (Pumps)
- Босоножки (Sandals)

**Examples:**
- INUIKII сапоги → `/collection/inuikii-boots`
- Premiata кроссовки → `/collection/premiata-sneakers`
- Baldinini туфли → `/collection/baldinini-pumps`
- Stuart Weitzman ботильоны → `/collection/stuart-weitzman-booties`

**Meta Tag Format:**
- Title: `{Brand} {Product Type} купить | {Brand} {Product Type} в Москве - [YOUR-PROJECT]`
- Description: `{Brand} {Product Type} - купить оригинальную обувь от итальянского бренда. ✓ Официальный магазин ✓ Доставка по России ✓ Гарантия`

### Phase 3: Color Variations (Priority 3)
**Timeline:** Month 2
**Effort:** 5-8 hours
**Target:** 25 filters

5 popular colors × 5 product types = 25 filters

**Top Colors:**
- Черный (Black)
- Белый (White)
- Бежевый (Beige)
- Коричневый (Brown)
- Красный (Red)

**Examples:**
- Белые кроссовки → `/collection/white-sneakers`
- Черные сапоги → `/collection/black-boots`
- Бежевые туфли → `/collection/beige-pumps`

**Meta Tag Format:**
- Title: `{Color} {Product Type} купить в Москве | Итальянская обувь - [YOUR-PROJECT]`
- Description: `{Color} {Product Type} из Италии. ✓ 30+ брендов ✓ Оригинальная продукция ✓ Доставка по России`

### Phase 4: Triple Combinations (Priority 4)
**Timeline:** Month 3
**Effort:** 10-15 hours
**Target:** 30-50 filters

Top brands × popular colors × product types

**High-Value Examples:**
- Premiata белые кроссовки (Premiata white sneakers)
- INUIKII черные сапоги (INUIKII black boots)
- Baldinini бежевые туфли (Baldinini beige pumps)
- Stuart Weitzman черные ботильоны (Stuart Weitzman black booties)

**When to Create:**
Only create if keyword research shows >200 monthly searches for the combination.

---

## Step-by-Step Creation Process

### 1. Access SEO Filters
1. Log in to InSales admin panel
2. Navigate to **Товары → На сайте**
3. Select parent category (e.g., "Женская обувь")
4. Click **SEO-фильтры** option

### 2. Configure Filter Settings

**Basic Settings:**
- **Название** (Name): Descriptive name (e.g., "INUIKII Сапоги")
- **Адрес** (URL): Custom slug (e.g., `inuikii-boots`) or auto-transliteration
- **Родительская категория** (Parent): Select appropriate category

**Parameters:**
- Select parameters from dropdowns (Brand, Color, Material, etc.)
- For multiple values: Use OR logic (Red OR Blue)
- For multiple parameters: Use AND logic (Nike AND White AND Sneakers)

**SEO Metadata:**
- **Title**: Keyword-optimized title (60 characters max)
- **Meta Description**: Compelling description (155 characters max)
- **Доп. описание** (Additional Description): 200-300 words unique content

### 3. Content Optimization (For High-Priority Filters)

Add 200-300 word unique content for filters targeting keywords with >500 monthly searches.

**Content Template:**
```
[Brand/Category] в интернет-магазине [YOUR-PROJECT].ru

[Opening paragraph about the product category - 50-80 words]

Почему выбирают [Brand/Category]:
• [Benefit 1]
• [Benefit 2]
• [Benefit 3]
• [Benefit 4]

[Brand story or product features - 100-150 words]

[Closing with CTA - 30-50 words]
```

### 4. Quality Checks

Before publishing each filter:
- [ ] At least 5 products populate the filter
- [ ] URL is clean and descriptive
- [ ] Meta title includes target keyword
- [ ] Meta description is compelling
- [ ] Unique content added (if high-priority)
- [ ] Filter appears in category navigation

---

## Technical Considerations

### robots.txt Compatibility

**CRITICAL:** Verify that SEO filter URLs are NOT blocked by robots.txt.

Current issue: `Disallow: /*?*` blocks query parameters

**What to Check:**
1. Verify filters use clean URLs: `/collection/filter-name` ✅ (GOOD)
2. NOT query parameters: `/collection?filter=name` ❌ (BLOCKED)

InSales documentation indicates clean URL structure, but verify in practice.

**Action:** After creating first test filter, check in robots.txt tester tool.

### Sitemap Integration

- ✅ Filters automatically added to sitemap.xml
- ✅ Crawlable by Yandex and Google
- ⚠️ May need internal linking for visibility (see below)

### Internal Linking Strategy

To maximize filter visibility and indexing:

**1. Homepage Links:**
- Feature 5-10 popular filters in homepage sections
- Example: "Популярные подборки" section with INUIKII, Premiata filters

**2. Category Page Sidebars:**
- Add "Popular Brands" widget linking to brand filters
- Add "Shop by Color" widget linking to color filters

**3. Blog Article Links:**
- Link from relevant articles to matching filters
- Example: "Best Italian Sneakers 2026" → link to Premiata filter, Voile Blanche filter

**4. Footer Navigation:**
- Add "Popular Collections" section with top 10-15 filters

**5. Product Pages:**
- Cross-link to related filters
- Example: On Premiata sneaker product → link to "All Premiata Sneakers" filter

### Performance & Scalability

**No Documented Limits:**
- Can create hundreds of filters
- Products auto-populate (no manual management)
- Updates automatically when inventory changes

**Best Practices:**
- Don't create filters with <5 products (thin content)
- Monitor filter performance monthly
- Remove underperforming filters with 0 traffic after 6 months
- Prioritize based on keyword search volume

---

## Keyword Research Integration

**Before Creating Filters:**

1. Complete Yandex Wordstat research for all combinations
2. Create spreadsheet with columns:
   - Filter combination
   - Estimated monthly searches
   - Competition level
   - Priority (High/Medium/Low)

**Prioritization Criteria:**
- **High Priority:** >500 monthly searches
- **Medium Priority:** 200-500 monthly searches
- **Low Priority:** <200 monthly searches

**Focus Areas:**
- High-priority filters: Add 200-300 word unique content
- Medium-priority filters: Optimize meta tags only
- Low-priority filters: Create only if minimal effort

---

## Measurement & Optimization

### Track These Metrics Monthly:

**In Yandex.Metrica:**
- Sessions to filter pages
- Bounce rate per filter
- Conversion rate per filter
- Revenue from filter pages

**In Yandex Webmaster:**
- Filter pages indexed (target: 100%)
- Keyword rankings for filter target keywords
- Click-through rate from search results

**Performance Benchmarks:**
- Indexed filters: >90% within 30 days
- Avg. CTR from search: >2%
- Conversion rate: Similar to category pages
- Traffic per filter: Varies by keyword volume

### Monthly Optimization Tasks:

1. **Review Performance** (1 hour)
   - Identify top 10 performing filters
   - Identify bottom 10 underperformers

2. **Optimize Top Performers** (2 hours)
   - Add unique content if not present
   - Improve meta descriptions
   - Build more internal links

3. **Fix Underperformers** (1 hour)
   - Check if keyword has search volume
   - Improve meta tags
   - Add internal links
   - If 0 traffic after 6 months → remove

4. **Expand Winners** (2 hours)
   - Create similar filters based on top performers
   - Example: If "Premiata white sneakers" performs well, create "Voile Blanche white sneakers"

---

## Expected Results

### 30-Day Goals:
- 33 brand filters created (Phase 1)
- 90%+ filters indexed by Yandex
- Filters appear in internal navigation
- Baseline traffic established

### 60-Day Goals:
- 83 total filters (Phase 1 + Phase 2)
- 10+ filters ranking in top 20 for target keywords
- 5-10% traffic increase from filter pages

### 90-Day Goals:
- 100+ total filters (Phase 1-3)
- 20+ filters ranking in top 10
- 15-25% traffic increase from long-tail queries
- Clear ROI data on which combinations work best

### 6-Month Goals:
- 150-200 total filters
- 50+ filters driving consistent monthly traffic
- 30-40% of total organic traffic from filter pages
- Established process for ongoing filter creation

---

## Common Issues & Solutions

### Issue 1: Filter Not Appearing in Sitemap
**Cause:** May be disabled or parent category issue
**Solution:** Check filter status, verify parent category settings

### Issue 2: No Products Populating Filter
**Cause:** Parameter combination too restrictive
**Solution:** Review product attributes, adjust parameters

### Issue 3: Filter Not Ranking
**Causes:**
- Not indexed yet (wait 30 days)
- No internal links
- No unique content
- Low search volume keyword

**Solutions:**
- Build internal links from blog/category pages
- Add 200-300 word unique content
- Verify keyword has search volume in Yandex Wordstat

### Issue 4: Duplicate Content Concerns
**Cause:** Multiple filters with same products
**Solution:** Add unique descriptions to differentiate, or use canonical tags if InSales supports

### Issue 5: Filter Blocked by robots.txt
**Cause:** Using query parameters instead of clean URLs
**Solution:** Verify with InSales support, may need robots.txt adjustment

---

## Checklist: Creating a New SEO Filter

**Before Creation:**
- [ ] Keyword research completed for this combination
- [ ] Search volume >100 monthly searches
- [ ] Competitor analysis shows ranking opportunity

**During Creation:**
- [ ] Descriptive name entered
- [ ] Custom URL slug set (clean, keyword-rich)
- [ ] Parent category selected
- [ ] Parameters configured correctly
- [ ] At least 5 products will populate
- [ ] Meta title optimized (60 chars, includes keyword)
- [ ] Meta description compelling (155 chars, includes CTA)

**After Creation:**
- [ ] Verify products auto-populated correctly
- [ ] Check filter appears on site navigation
- [ ] Test URL loads correctly
- [ ] Add to internal linking plan
- [ ] Add to tracking spreadsheet
- [ ] Schedule content addition (if high-priority)

**30 Days After:**
- [ ] Check indexing status in Yandex Webmaster
- [ ] Review traffic in Yandex.Metrica
- [ ] Check keyword ranking position
- [ ] Decide on optimization needs

---

## Resources & Tools

**InSales Documentation:**
- SEO Filters Guide: https://www.insales.ru/collection/doc-products/product/seo-filtry

**Keyword Research Tools:**
- Yandex Wordstat: https://wordstat.yandex.ru/
- Serpstat: https://serpstat.com/
- SE Ranking: https://seranking.com/

**Tracking & Analytics:**
- Yandex.Metrica (traffic, conversions)
- Yandex Webmaster (indexing, rankings)
- Google Search Console (supplementary data)

**Internal Documentation:**
- Keyword Research Template: `.claude/workflows/KEYWORD_RESEARCH_TEMPLATE.md`
- Content Writing Guide: `.claude/workflows/CONTENT_WRITING_GUIDE.md`
- Monthly Report Template: `research/analytics/monthly-reports/REPORT_TEMPLATE.md`

---

## Questions & Support

**InSales Support:**
- Check plan includes SEO filters feature
- Technical questions about filter functionality
- URL structure verification

**SEO Strategy Questions:**
- Which filter combinations to prioritize?
- How much content to add?
- Internal linking best practices?

→ Refer to keyword research data and monthly performance reports

---

**Last Updated:** January 27, 2026
**Next Review:** After completing Phase 1 (33 brand filters)

# SEO Master Workflow

## Overview

This is the **master workflow** for the SEO project. All other workflows, skills, and scripts are referenced from here. Follow phases 1-4 sequentially during initial setup, then cycle through phases 5-8 monthly.

→ See `client.md` for company info, domains, services, content pillars, and audiences.

---

## Workflow Map

```
INITIAL SETUP (once):
  Phase 1: Audit ──→ Phase 2: Keywords ──→ Phase 3: Competitors ──→ Phase 4: Strategy
                                                                          │
MONTHLY CYCLE (repeat): ◄────────────────────────────────────────────────┘
  Phase 5: Write ──→ Phase 6: Review & Publish ──→ Phase 7: Amplify (SMM)
      │                                                       │
      │                   Phase 8: Link Building (ongoing) ◄──┘
      │                                                       │
      └──── Monthly Close: Audit → Report → Plan Next Month ──┘
```

## Skills & Scripts Map

| Skill/Script | Phase | Model | Purpose |
|---|---|---|---|
| `/brainstorm` | 1, 4 | **Opus** | Content ideation, strategy brainstorming |
| `/writing-guide` | 5 | **Sonnet** | Load writing standards and content templates |
| `/review-article` | 6 | **Multi** | 8-critic content review before publishing |
| `/create-social-posts` | 7 | **Sonnet** | Generate social media posts from published article |
| `/monthly-report` | Monthly | **Sonnet** | Generate monthly performance report |
| `/analyze-gsc` | Monthly | **Sonnet** | Analyze Google Search Console data |
| `/analyze-webmaster` | Monthly | **Sonnet** | Analyze Yandex Webmaster data |
| `/start-session` | Every session | — | Load context, show current phase and next actions |
| `/end-session` | Every session | — | Save progress, workflow compliance check, commit |
| `content_audit/main.py` | 1, Monthly | script | Scrape & analyze site content |
| `process_keywords.py` | 2 | script | Process keyword CSV exports |

## Session Wrapper

Every working session follows this pattern:
```
/start-session → See current phase and next actions
     ↓
Work on current phase tasks
     ↓
/end-session → Save progress, check workflow compliance, commit
```

---

## Phase 1: Website Analysis & Audit

**Goal:** Understand current state of all sites
**Duration:** 1-2 sessions
**Phase gate:** Audit complete, baseline metrics documented in `research/content-audit/`

### Actions

1. **Run content audit script:**
   ```bash
   venv/bin/python scripts/content_audit/main.py --full --all
   ```
   → See [monthly-content-audit.md](monthly-content-audit.md) for detailed instructions and output files.

2. **Analyze audit results:**
   - [ ] Review existing page inventory (content-audit CSV)
   - [ ] Identify keyword cannibalization (duplicate keywords across pages)
   - [ ] List thin content pages (<300 words) from content-gaps.md
   - [ ] Check current SEO implementation (meta tags, headings, alt texts)
   - [ ] Check schema markup → See `client.md#schema-markup` for required types

3. **Technical SEO check:**
   - [ ] Site speed analysis
   - [ ] Mobile responsiveness
   - [ ] XML sitemap validation
   - [ ] robots.txt review

4. **Verify target audience alignment:**
   → See `client.md#target-audiences` for defined personas

5. **Document baseline metrics:**
   - Save to: `research/content-audit/baseline-[YYYY-MM-DD].md`

**Optional:** Use `/brainstorm` (Opus) to ideate on content strategy directions based on audit findings.

### Phase 1 Output
- `research/content-audit/[site]/site-content-audit-latest.csv`
- `research/content-audit/[site]/content-gaps-latest.md`
- `research/content-audit/baseline-[date].md`

---

## Phase 2: Keyword Research

**Goal:** Build prioritized keyword list for all languages
**Duration:** 2-3 sessions
**Phase gate:** Priority keywords documented, keyword mapping complete
**Reference:** [KEYWORD_RESEARCH_TEMPLATE.md](KEYWORD_RESEARCH_TEMPLATE.md)

### Actions

1. **Collect seed keywords** by service/content pillar:
   → See `client.md#seed-keyword-areas` for starting keywords
   → See `client.md#content-pillars` for topic categories

2. **Use research tools:**
   - Google Keyword Planner → export CSV
   - Yandex Wordstat → export CSV (for RU market)
   - Google Search Console → existing performance
   - Google Trends → seasonal patterns

3. **Process keyword exports:**
   ```bash
   # Place CSV exports in research/keywords/input/
   venv/bin/python scripts/process_keywords.py
   # Output: research/keywords/output/en/ and /ru/
   ```

4. **Analyze and prioritize:**
   - For each keyword: volume, difficulty, intent, relevance (1-10)
   - Categorize: Transactional / Commercial / Informational / Navigational
   - Select top 50 priority keywords

5. **Create keyword mapping:**
   - Map keywords to content types and target pages
   → See `client.md#site-structure` for valid page patterns

### Phase 2 Output
- `research/keywords/seed-keywords.md`
- `research/keywords/priority-keywords.md` (top 50)
- `research/keywords/output/en/keywords-en.csv`
- `research/keywords/output/ru/keywords-ru.csv`

---

## Phase 3: Competitor Analysis

**Goal:** Understand competitive landscape, find content gaps
**Duration:** 1-2 sessions
**Phase gate:** Competitor profiles documented, opportunities identified

### Actions

1. **Identify competitors:**
   → See `client.md#competitors` for initial competitor list

2. **For each competitor (5-10):**
   - [ ] What keywords are they ranking for?
   - [ ] What content types do they produce?
   - [ ] What's their content frequency?
   - [ ] What services do they highlight?
   - [ ] What content gaps exist?

3. **Identify opportunities:**
   - [ ] Keywords competitors rank for but we don't
   - [ ] Content topics they're missing
   → See `client.md#competitive-advantages` for positioning angles
   - [ ] Comparison article opportunities

### Phase 3 Output
- `research/competitors/competitor-analysis.md`

---

## Phase 4: Content Strategy & Publication Plan

**Goal:** Create actionable content calendar for first 3 months
**Duration:** 1-2 sessions
**Phase gate:** Content calendar created with article briefs
**Reference:** [CONTENT_CALENDAR_TEMPLATE.md](CONTENT_CALENDAR_TEMPLATE.md)

### Actions

1. **Define content calendar** using keyword priorities:
   → See `client.md#publishing-schedule` for frequency and schedule
   → See `client.md#content-pillars` for topic categories
   → See `client.md#content-types` for article formats

2. **Create article briefs** with:
   - Title (working), primary keyword, language
   - Secondary keywords, search intent
   - Content type, target word count
   - Target audience → See `client.md#target-audiences`
   - CTAs → See `client.md#ctas`
   - Internal linking targets → See `client.md#site-structure`

3. **Use `/brainstorm` (Opus)** for topic ideation if needed

### Phase 4 Output
- `content/calendars/[MONTH]_CONTENT_CALENDAR.md`

---

## Phase 5: Content Creation (Monthly Cycle)

**Goal:** Write SEO-optimized articles per calendar
**Model recommendation:** **Sonnet** for drafting, **Opus** for complex/nuanced content
**Phase gate:** Draft complete, saved to `content/drafts/`

### Actions

1. **Load writing standards:**
   - Run `/writing-guide` (Sonnet) to load content templates and requirements
   - Reference `.claude/prompts/content-generation.md` for article type prompts

2. **Write article following standards:**
   → See `client.md#content-standards` for word count, keyword density, link requirements
   → See `client.md#ctas` for call-to-action language
   → See `client.md#market-separation-rules` for bilingual rules
   → See `client.md#brand` for visual style and image requirements

3. **Save draft:**
   - Save to: `content/drafts/[slug]-[lang].md`
   - Include YAML frontmatter: keyword, secondary keywords, intent, word count target

### Phase 5 References
- `/writing-guide` skill — loads writing standards
- `.claude/prompts/content-generation.md` — article type prompt templates
- [CONTENT_WRITING_GUIDE.md](CONTENT_WRITING_GUIDE.md) — full reference document

---

## Phase 6: Review & Publish

**Goal:** Quality-gate articles and publish
**Phase gate:** All critics ≥7, overall ≥8

### Actions

1. **Run multi-critic review:**
   ```
   /review-article [filename]
   ```
   - 8 critics run in optimized order (Haiku → Sonnet → Opus)
   - Review saved to: `content/reviews/review-[filename]-[date].md`

2. **Score interpretation:**
   - ≥8 overall: Ready to publish
   - 6-7: Fix issues, re-review
   - <6: Major revision needed

3. **Fix issues and re-review** until passing

4. **Pre-publishing checklist:**
   - [ ] Primary keyword in title, intro, conclusion
   - [ ] Meta title (50-60 chars), meta description (150-160 chars)
   - [ ] All images have alt text
   - [ ] Internal links validated (3+) → See `client.md#site-structure` for valid URLs
   - [ ] External links to authoritative sources (1-2)
   - [ ] Schema markup added → See `client.md#schema-markup`
   - [ ] Mobile-friendly formatting
   - [ ] CTA clear → See `client.md#ctas`

5. **Post-publishing:**
   - [ ] Submit URL to search engines → See `client.md#domains` for which engines per site
   - [ ] Move article to `content/published/`
   - [ ] Update content calendar status

---

## Phase 7: Social Media Amplification

**Goal:** Repurpose published article across social channels
**Model recommendation:** **Sonnet**
**Reference:** [SMM_WORKFLOW.md](SMM_WORKFLOW.md) — channel-specific strategies

### Actions

1. **Generate social posts:**
   ```
   /create-social-posts [published-article]
   ```
   - Creates 10+ platform-specific posts
   - 7-day publishing schedule with UTM links
   → See `client.md#social-media-channels` for channel list, tones, and rules

2. **Review and publish** per schedule in `content/social/`

3. **Track engagement** weekly per channel

### Connection to SEO Workflow
- SMM amplification starts **after** article is published (Phase 6 complete)
- Each published article triggers one `/create-social-posts` cycle
- Social posts drive initial traffic, supporting early SEO signals

---

## Phase 8: Link Building (Ongoing, Month 3+)

**Goal:** Build authority through internal and external links

### Internal Linking
- Link from high-authority pages to new content
- Create topic clusters around content pillars → See `client.md#content-pillars`
- Use descriptive anchor text
- Cross-link between language versions via hreflang (not in-content)

### External Link Building
→ Tactics depend on client industry. Typical approaches:
- Industry directories and listings
- Guest posting on industry blogs
- Linkable resources (templates, frameworks, tools)
- Case studies shared in industry publications

---

## Monthly Close Cycle

**Timing:** Last working day of each month
**Purpose:** Measure, report, plan next month
**This cycle connects Phase 7 back to Phase 5 for the next month.**

### Step 1: Run Content Audit
```bash
venv/bin/python scripts/content_audit/main.py --full --all
```
→ See [monthly-content-audit.md](monthly-content-audit.md) for details.

### Step 2: Analyze Search Data
If data exports are available:
```
/analyze-gsc [date]          # Google Search Console trends (Sonnet)
/analyze-webmaster [date]    # Yandex Webmaster analysis (Sonnet)
```

### Step 3: Generate Monthly Report
```
/monthly-report [YYYY-MM]    # (Sonnet)
```
Uses content audit data + search analytics to create performance report.
Save to: `research/analytics/monthly-reports/report-[YYYY-MM].md`

### Step 4: Plan Next Month
1. Review content calendar — what was published, what was missed
2. Check content-gaps.md — new gaps to address
3. Review keyword rankings — new opportunities
4. Create next month's content calendar: `content/calendars/[MONTH]_CONTENT_CALENDAR.md`
5. Update `progress.md` with new monthly goals

### Monthly Close Output
- `research/content-audit/[site]/site-content-audit-[date].csv`
- `research/analytics/monthly-reports/report-[YYYY-MM].md`
- `content/calendars/[NEXT-MONTH]_CONTENT_CALENDAR.md`

---

## Success Metrics

→ See `client.md#project-goals` for specific targets and quarterly milestones.

### Generic Milestones by Phase
| Period | Content | Rankings | Traffic |
|--------|---------|----------|---------|
| Month 1-3 | Foundation content (2-3x articles/month) | Building index | 10-20% growth |
| Month 4-6 | Steady cadence | Top-20 for 20+ keywords | 30-50% growth |
| Month 7-12 | Full production | Top-10 for 30+ keywords | 100%+ growth |

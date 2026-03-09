---
name: writing-guide
description: Load writing standards and content templates for article creation. Use when starting to write or edit an article.
---

# Writing Guide Skill

**Recommended Model: Sonnet** — structured, efficient for loading and applying writing rules. Use Opus for complex/nuanced content.

When this skill is invoked, load the writing standards and present them as actionable guidance for the current writing task.

## Usage
- `/writing-guide` — Load full writing standards for new article
- `/writing-guide [content-type]` — Load standards for specific type (how-to, case-study, comparison, strategy, checklist, faq)
- `/writing-guide --checklist` — Show pre-publishing checklist only

## Model
**Recommended: Sonnet** — structured, efficient for loading and applying writing rules.
Use **Opus** only for complex/nuanced content that requires deep linguistic judgment.

## Execution Steps

### 1. Load Writing Standards

Read these files:
- `.claude/workflows/CONTENT_WRITING_GUIDE.md` — Full writing reference (structure, SEO rules, formatting)
- `.claude/client/client.md` — Client-specific data (CTAs, brand, audiences, content standards)
- `.claude/prompts/content-generation.md` — Article type prompt templates

### 2. Load Client Context

From `client.md`, extract and present:
- **Content standards:** word count, keyword density, link requirements
- **CTAs:** primary and secondary in both languages
- **Brand:** visual style, colors, image requirements
- **Market rules:** language separation rules
- **Target audiences:** who we're writing for
- **Content pillars:** which topics to focus on

### 3. Present Writing Brief

Based on content type (from parameter or ask user), present:

**Article Type Templates:**

| Type | Min Words | Focus | Key Elements |
|------|-----------|-------|--------------|
| How-To Tutorial | 1,800 | Step-by-step guide | HowTo schema, numbered steps, prerequisites |
| Case Study | 1,800 | Client results | Before/after metrics, timeline, ROI |
| Strategy Guide | 2,000 | Comprehensive education | Framework, comparison table, expert examples |
| Comparison Article | 1,800 | Fair tool/approach comparison | Comparison table, pros/cons, verdict |
| Service Guide | 2,000 | How agency helps | Process overview, results, CTA |
| Checklist/Template | 2,500 | Actionable resource | Checkbox items, priority indicators |
| FAQ Page | 1,500 | Common questions | FAQPage schema, direct answers |

### 4. Present Checklist

```markdown
## Pre-Writing Checklist
- [ ] Primary keyword identified
- [ ] Secondary keywords listed (3-5)
- [ ] Search intent determined (informational/commercial/transactional)
- [ ] Target audience selected → See client.md#target-audiences
- [ ] Content type chosen
- [ ] Word count target set (min from table above)
- [ ] Internal link targets identified → See client.md#site-structure
- [ ] CTA selected → See client.md#ctas

## Writing Standards
- [ ] Title includes primary keyword
- [ ] Primary keyword in first paragraph
- [ ] Keyword density: 0.7-1.0% (natural)
- [ ] H1 → H2 → H3 heading hierarchy
- [ ] Internal links: 3-5 per 1,000 words
- [ ] External links: 1-2 authoritative sources
- [ ] FAQ section included (enables FAQPage schema)
- [ ] Hero image prompt created (16:9, 1920x1080, no text/faces)

## Post-Writing Checklist (before /review-article)
- [ ] Meta title: 50-60 characters with keyword
- [ ] Meta description: 150-160 characters with CTA
- [ ] URL slug: short, keyword-inclusive, lowercase hyphens
- [ ] Schema markup type noted (Article, HowTo, FAQPage)
- [ ] CTA placed after value delivery, max 1 per 500 words
- [ ] Market separation rules followed → See client.md#market-separation-rules
- [ ] YAML frontmatter complete
```

### 5. Next Step Guidance

After presenting the brief:
- "Standards loaded. Ready to write. When the draft is complete, run `/review-article` to quality-check before publishing."
- If user provides a specific article to write, proceed directly to writing.

## Notes
- This skill loads reference material — it does NOT write the article itself
- The actual writing uses Sonnet (or Opus for complex topics)
- After writing, always run `/review-article` (Phase 6 in SEO Workflow)
- For article prompt templates by type, see `.claude/prompts/content-generation.md`

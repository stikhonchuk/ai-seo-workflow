---
name: review-article
description: Run multi-critic review on content drafts for SEO, language, E-E-A-T, intent, readability, and commercial integration
---

# Review Article Skill

When this skill is invoked, run a comprehensive multi-critic review on a content article.

## Usage
- `/review-article` - Review the most recent article in content/drafts/
- `/review-article [filename]` - Review specific file
- `/review-article --critic=seo` - Run only SEO critic
- `/review-article --critic=russian` - Run only Russian language critic
- `/review-article --critic=eeat` - Run only E-E-A-T critic
- `/review-article --critic=intent` - Run only User Intent critic
- `/review-article --critic=readability` - Run only Readability critic
- `/review-article --critic=commercial` - Run only Commercial critic
- `/review-article --critic=images` - Run only Image Prompt critic
- `/review-article --quick` - Run condensed review (summary only)

## Execution Steps

### 1. Locate Article
- If filename provided, find in `content/drafts/` or absolute path
- If no filename, find most recently modified `.md` file in `content/drafts/`
- If no drafts found, ask user for file path

### 2. Read Article and Extract Metadata
- Read the full article content
- Extract from YAML frontmatter or content:
  - Primary keyword
  - Secondary keywords
  - Target URL
  - Content type (educational, buying guide, size guide, category)
  - Target word count

### 3. Load Critic Guidelines
Read the relevant critic files from `.claude/critics/`:
- `seo-critic.md`
- `russian-language-critic.md`
- `eeat-critic.md`
- `user-intent-critic.md`
- `readability-critic.md`
- `commercial-critic.md`
- `image-prompt-critic.md`

### 4. Run Critics (Sequential or Selected)

#### Model Assignments (Cost/Quality Optimization)
| Critic | Model | Reasoning |
|--------|-------|-----------|
| SEO | **Sonnet** | Structured analysis, keyword counting, technical checks |
| Russian Language | **Opus** | Deep linguistic understanding, nuance detection, native-quality assessment |
| E-E-A-T | **Sonnet** | Pattern matching for trust signals, factual evaluation |
| User Intent | **Sonnet** | Intent classification, content gap analysis |
| Readability | **Haiku** | Mechanical: sentence/paragraph counting, structure checks |
| Commercial | **Haiku** | Checklist: CTA counting, link inventory |
| Image Prompts | **Haiku** | Checklist validation, pattern matching |

#### Execution Order (Parallel where possible)
1. **Parallel batch 1 (Haiku):** Readability + Commercial + Image Prompts (fast, independent)
2. **Parallel batch 2 (Sonnet):** SEO + E-E-A-T + User Intent
3. **Sequential (Opus):** Russian Language (most expensive, run last)

This order optimizes for:
- Cost efficiency (cheap critics first to catch obvious issues)
- Time (parallel execution where possible)
- Quality (Opus for the most nuanced evaluation)

#### If `--critic` flag specified:
Run only the specified critic with its assigned model.

#### If `--quick` flag specified:
Run all critics with Haiku for quick scoring (less detailed but faster/cheaper).

#### Default (full review):
Run all 7 critics with their assigned models, generating full reports.

### 4b. Load SEO Context (for SEO Critic)
Before running SEO critic, load these context files:
- `research/keywords/SEO_GAPS_ANALYSIS.md` - keyword targets
- `research/keywords/seo_wizard_export.tsv` - current rankings
- `content/calendars/JANUARY_2026_CONTENT_CALENDAR.md` - internal link targets

### 5. Generate Combined Report

Create report at: `content/reviews/review-[article-filename]-[YYYY-MM-DD].md`

#### Report Structure:

```markdown
# Content Review: [Article Title]

**Review Date:** [YYYY-MM-DD]
**Article:** [filename]
**Primary Keyword:** [keyword]
**Word Count:** [count]

---

## Executive Summary

### Overall Score: X/10

| Critic | Score | Status |
|--------|-------|--------|
| SEO | X/10 | [Pass/Needs Work/Fail] |
| Russian Language | X/10 | [Pass/Needs Work/Fail] |
| E-E-A-T | X/10 | [Pass/Needs Work/Fail] |
| User Intent | X/10 | [Pass/Needs Work/Fail] |
| Readability | X/10 | [Pass/Needs Work/Fail] |
| Commercial | X/10 | [Pass/Needs Work/Fail] |
| Image Prompts | X/10 | [Pass/Needs Work/Fail] |

### Publication Readiness: [Ready / Needs Revision / Major Rewrite]

### Top 5 Priority Fixes
1. [Most critical issue from any critic]
2. [Second priority]
3. [Third priority]
4. [Fourth priority]
5. [Fifth priority]

---

## Detailed Reviews

### SEO Critic Review
[Full SEO review output]

---

### Russian Language Critic Review
[Full language review output]

---

### E-E-A-T Critic Review
[Full E-E-A-T review output]

---

### User Intent Critic Review
[Full intent review output]

---

### Readability Critic Review
[Full readability review output]

---

### Commercial Integration Critic Review
[Full commercial review output]

---

### Image Prompt Critic Review
[Full image prompt review output]

---

## Revision Checklist

### Critical (Must Fix Before Publishing)
- [ ] [Issue 1]
- [ ] [Issue 2]

### Major (Should Fix)
- [ ] [Issue 1]
- [ ] [Issue 2]

### Minor (Nice to Have)
- [ ] [Issue 1]
- [ ] [Issue 2]

---

## Recommended Next Steps
1. [First action]
2. [Second action]
3. [Third action]

---

*Review generated by [YOUR-DOMAIN] Content Critic System*
*Reviewed by: [list of critics run]*
```

### 6. Summary Output to User

After generating the report, provide:

1. **File path** to saved review
2. **Overall score** and publication readiness
3. **Top 3 issues** that need immediate attention
4. **Quick wins** that can be fixed easily
5. **Question**: Would you like me to fix any issues automatically?

## Scoring Guidelines

### Individual Critic Scores
- **9-10**: Excellent, publication ready
- **7-8**: Good, minor improvements possible
- **5-6**: Acceptable, some issues to address
- **3-4**: Needs work, significant issues
- **1-2**: Major rewrite needed

### Overall Score Calculation
Weighted average:
- SEO: 25%
- Russian Language: 20%
- E-E-A-T: 15%
- User Intent: 15%
- Readability: 10%
- Commercial: 10%
- Image Prompts: 5%

### Publication Readiness
- **Ready**: All critics ≥7, overall ≥8
- **Needs Revision**: Any critic 5-6, or overall 6-7
- **Major Rewrite**: Any critic <5, or overall <6

## Notes

- This skill reads content but does NOT modify it automatically
- Always ask before making changes
- Reviews are saved for tracking improvement over time
- Can be run multiple times as article is revised

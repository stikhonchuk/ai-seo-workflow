---
name: create-social-posts
description: Generate social media posts from a blog article for all client channels (→ See client.md#social-media) (LinkedIn, Telegram, Instagram, X, VK)
---

# Create Social Posts Skill

**Recommended Model: Sonnet** — creative content generation with structured output.
**Workflow Position:** Phase 7 (Social Media Amplification) → See SEO_WORKFLOW.md

→ See `client.md#social-media-channels` for channel list, tones, and rules.
→ See `client.md#utm-convention` for UTM parameter format.

When this skill is invoked, generate a complete set of social media posts from a blog article for all channels listed in `client.md#social-media-channels`.

## Usage
- `/create-social-posts` — Use most recent article in `content/drafts/` or `content/published/`
- `/create-social-posts [filename]` — Use specific blog article
- `/create-social-posts --channel=linkedin` — Generate for one channel only
- `/create-social-posts --channel=telegram` — Telegram only (RU)
- `/create-social-posts --channel=instagram` — Instagram only
- `/create-social-posts --channel=x` — X/Twitter only
- `/create-social-posts --channel=vk` — VKontakte only (RU)

## Execution Steps

### 1. Locate Source Article

- If filename provided, find in `content/drafts/`, `content/published/`, or absolute path
- If no filename, find most recently modified `.md` file in `content/drafts/` or `content/published/`
- If no articles found, ask user for file path

### 2. Read Article and Extract Key Points

Read the full article content and extract:

- **Main thesis** (1 sentence)
- **3-7 key insights** (each becomes standalone post material)
- **1 surprising/counterintuitive fact**
- **1 actionable tip** (for video content)
- **1 discussion question** (for polls)
- **1 data point or statistic** (for shareable graphic)
- **Primary keyword** (from frontmatter or content)
- **Article language** (EN or RU)
- **Target segment** (Small Business, E-commerce, Startup, Enterprise)

### 3. Load Workflow Guidelines

Read `.claude/workflows/SMM_WORKFLOW.md` for:
- Channel-specific tone and format rules
- Publishing schedule
- Quality checklist

### 4. Generate Posts for Each Channel

#### LinkedIn (EN)

Generate 3 posts:

**Post 1: Key Insight (Day 1)**
- Format: Text post with suggested image description
- Length: 150-300 words
- Structure: Hook → Insight → Takeaway → CTA
- Include: "First comment: [link to article with UTM]"
- Hashtags: 2-3 relevant

**Post 2: Carousel Outline (Day 2)**
- Format: Slide-by-slide content (5-7 slides)
- Slide 1: Bold headline hook
- Slides 2-6: One key point per slide
- Final slide: CTA + brand mention
- Caption: 50-100 words

**Post 3: Engagement Post (Day 4)**
- Format: Poll OR discussion question
- Related to article topic
- Designed to generate comments

#### Telegram (RU)

Generate 2 posts:

**Post 1: Long-form Expert Post (Day 1)**
- Format: 500-1500 word post in Russian
- Must be written natively in Russian (NOT translated)
- Structure: Headline → Problem → Analysis → Key Points → Takeaway → Link
- Include relevant emoji markers (📌, 💡, 🔗)
- Hashtags in Russian

**Post 2: Resource Post (Day 7)**
- Format: Quick tip or checklist (50-200 words in Russian)
- Include: Downloadable resource suggestion (template, checklist)
- CTA to article or product

#### Instagram (EN)

Generate 3 posts:

**Post 1: Reel Script (Day 3)**
- Format: 60-second video script
- Structure:
  - 0-3s: Hook (text overlay suggestion)
  - 3-15s: Problem
  - 15-45s: Solution/tips (numbered)
  - 45-55s: Result
  - 55-60s: CTA
- Caption: 100-200 words + hashtags (5-10)
- Suggest: Audio style (trending, voiceover, talking head)

**Post 2: Carousel (Day 2)**
- Format: 5-7 slide descriptions
- Slide content: Large text, one point per slide
- Caption: 100-150 words + hashtags

**Post 3: Story Ideas (Day 5)**
- Format: 2-3 story frame suggestions
- Include: Poll sticker, question sticker, or quiz
- Quick, interactive, drives engagement

#### X/Twitter (EN)

Generate 1 post:

**Post 1: Thread (Day 2)**
- Format: 7-10 tweets
- Tweet 1: Hook + "🧵"
- Tweets 2-8: One point per tweet, numbered
- Tweet 9: Summary
- Tweet 10: CTA + link (with UTM)
- End with "Like + RT if helpful 🔄"

#### VKontakte (RU)

Generate 1 post:

**Post 1: Community Post (Day 4)**
- Format: 200-400 word post in Russian
- Adapted from Telegram content (NOT identical)
- More casual, community-oriented tone
- Include image/infographic suggestion
- Hashtags in Russian

### 5. Generate 7-Day Schedule

Create publishing schedule table:

| Day | Channel | Post Type | Status |
|-----|---------|-----------|--------|
| Day 1 | LinkedIn | Key Insight | Draft |
| Day 1 | Telegram | Long-form Expert | Draft |
| Day 2 | X/Twitter | Thread | Draft |
| Day 2 | Instagram | Carousel | Draft |
| Day 3 | Instagram | Reel | Draft |
| Day 4 | LinkedIn | Engagement | Draft |
| Day 4 | VKontakte | Community Post | Draft |
| Day 5 | Instagram | Story | Draft |
| Day 7 | LinkedIn | Thought Leadership angle | Draft |
| Day 7 | Telegram | Resource/Template | Draft |

### 6. Save Output

Save generated posts to: `content/social/[article-slug]-social-[YYYY-MM-DD].md`

Structure of output file:

```markdown
# Social Media Posts: [Article Title]

**Source Article:** [filename]
**Generated:** [YYYY-MM-DD]
**Article Language:** [EN/RU]

---

## LinkedIn Posts

### LI-1: Key Insight (Day 1)
[content]

### LI-2: Carousel (Day 2)
[slide content]

### LI-3: Engagement (Day 4)
[content]

---

## Telegram Posts (RU)

### TG-1: Expert Post (Day 1)
[content in Russian]

### TG-2: Resource Post (Day 7)
[content in Russian]

---

## Instagram Posts

### IG-1: Reel Script (Day 3)
[script]

### IG-2: Carousel (Day 2)
[slide content]

### IG-3: Story Ideas (Day 5)
[frames]

---

## X/Twitter Thread

### X-1: Thread (Day 2)
[tweets]

---

## VKontakte Post

### VK-1: Community Post (Day 4)
[content in Russian]

---

## Publishing Schedule

[schedule table]

---

## UTM Links

[pre-built UTM links for each post]
```

### 7. Summary Output to User

After generating, provide:

1. **File path** to saved social posts
2. **Post count** per channel
3. **Key hook/angle** used across posts
4. **Suggested visual assets** needed
5. **Question**: "Would you like me to adjust any posts or generate for additional channels?"

## Quality Rules

- Russian content MUST be written natively, not translated
- Each post adapted for platform (never cross-post verbatim)
- All links include UTM parameters
- LinkedIn: NO links in post body (first comment only)
- Instagram: "Link in bio" only (no external links in posts)
- Follow 4-1-1 rule across weekly content mix
- Hashtags appropriate per platform (2-3 LinkedIn, 5-10 Instagram, 1-2 X)

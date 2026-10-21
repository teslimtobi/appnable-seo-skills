---
name: seo-article-writer
description: For Appnable and its products (KoKoodi, StGatherly). Write publish-ready SEO blogs from approved topics as Word documents, following Marketing's Appnable Blog Writing Guidelines and pre-publish checklist, Appnable's company knowledge and its humanizing rules. Blogs are 1,000–1,500 words in UK English, human-sounding and Appnable-specific (never generic), with the primary keyword in the title, URL and first 100 words (max 4–5 uses), inline-linked statistics ("According to stats by…"), a mid-blog selling section, a Solution page link, two FAQs ending with the FAQ page link, Appnable "Read also" links, one call to action and a credited cover image from approved free libraries (never AI images). Use whenever the user asks to write, draft, rewrite or produce blogs, articles or SEO content for Appnable, KoKoodi or StGatherly, or "the articles" for approved topics, and whenever they ask to humanize text or make it sound less AI-generated.
---

# Appnable SEO Blog Writer

Turn approved topics into Appnable blogs that pass Marketing's pre-publish checklist first time and read like an Appnable expert wrote them. Topics come from the `seo-keyword-research` skill; if the author hasn't approved a topic and keywords yet, confirm them first.

**Rule hierarchy:** the author's instructions in the conversation → files in `references/company-docs/` → the **Appnable Blog Writing Guidelines** (`references/appnable-blog-guidelines.md`) → the other reference files → the defaults here. If a draft fails one checklist item, it is not ready to publish.

## Read first, every time

1. `references/appnable-company.md`: who Appnable is, its voice, the five solutions, the group and products, case studies.
2. Every file in `references/company-docs/` (brand, vision and mission, service sheets). These override the company summary where they differ.
3. `references/appnable-blog-guidelines.md`: Marketing's rules, checklist and open questions.
4. `references/humanizing-rules.md`: banned words, rhythm, transitions, anti-generic rules.
5. `references/image-sources.md`: allowed image sources and how to credit the cover image.
6. `references/appnable-links.md`: Solution, contact, case study and product URLs, FAQ page, published blogs.
7. `references/review-lessons.md`: what reviewers have corrected before. **Every lesson there is a rule.**

## Before writing: gather inputs

- **Approved title, primary keyword and 2–4 supporting keywords.**
- **Primary keyword not already used** by another blog (Published blogs in `appnable-links.md`, or the author's tracker).
- **Solution page link** for the topic (from `appnable-links.md`).
- **FAQ page URL.** Not on the site yet: ask the author. If they don't have one, leave a clearly marked `[FAQ page URL]` placeholder and list it as an open checklist item.
- **Related Appnable blogs** for "Read also". If there are fewer than two, leave the Read also parts out (allowed for the first one or two blogs).
- **The selling angle:** which Appnable service, product or case study the blog naturally leads to.

Ask for anything missing in one message. Never invent Appnable URLs, blog titles, products, clients or figures.

## Step 1: Research sources

- **Use:** official bodies (ONS, ICO, FCA, gov.uk), vendor documentation (Microsoft Learn), peer-reviewed research, established analysts (Gartner, McKinsey, Forrester), reputable press.
- **Avoid:** competitor blogs, Wikipedia, AI-generated summaries, unsourced statistics.
- **Recent:** nothing older than three years unless historical; say the year in the sentence.
- **Original:** link the original report, not one quoting it. **Relevant:** confirm each source supports the exact claim.

No source, no claim.

## Step 2: Write the blog

### Header block (above the title, for the editor; not published)

```
Primary keyword: [keyword] (used [N] times)
Supporting keywords: [kw 1], [kw 2], [kw 3]
URL slug: /blog/[keyword-only-slug]
Meta description: [140–160 characters] ([N] characters)
Title length: [N] characters
Cover image: [description] | Source: [Site] ([photographer/artist]) | [image URL or search URL]
Cover image alt text: [what the image shows]
appnable.com
```

### Structure (in this order)

1. **Title (H1):** one only, under 60 characters, primary keyword near the start, a clear benefit.
2. **Introduction (80–120 words):** the reader's real problem in a concrete scene from their world, and what they'll learn. Primary keyword in the first 100 words. It must not read like any other company's intro.
3. **Body: 3–5 H2 sections**, H3s for sub-points, never skip a level. Don't spend the body re-explaining what vendor documentation already covers (link to it in a sentence instead). Include:
   - **A "where doing it yourself stalls" section** before the selling section: specific, honest failure points (wrong process chosen, permissions, systems outside Microsoft 365, exceptions, ownership, audit) so the reader sees why expertise matters.
   - **A workflow illustration** for any automation or process topic: Trigger → Automation action → Approval / validation → Business outcome, filled with one concrete example, made with `scripts/workflow_diagram.py`, with a caption, alt text and four short bullets explaining each step. Other topics: at least one visual that tells the story.
   - **One mid-blog selling section** (usually the third or fourth H2, around the middle). Show how Appnable solves the problem the blog has just described, grounded in a real case study figure or a specific service or product from `appnable-company.md`, with the Solution page link here. Helpful and specific, not a sales pitch: what Appnable did, for whom (as published), and the result.
   - **One inline "Read also"** mid-blog where it fits (if related blogs exist).
4. **Conclusion (60–100 words)** under a question H2 naming the value ("Ready to get more value from [topic]?") or "Final thoughts". Follow the reviewer's model in `review-lessons.md`: what the reader may already have, what Appnable does about it, who it's for, then **one call to action naming the business outcome** ("Contact Appnable to discuss your [topic] opportunities", linked to https://www.appnable.com/contact/).
5. **Read also (H2):** 2–3 related Appnable blogs (if available).
6. **FAQs (H2):** two, each question as an H3.
7. **No References section.**

Length: **1,000–1,500 words**, body + FAQs. Never over 1,500.

### Keywords

- Primary keyword in the **title, URL slug and first 100 words**; exact phrase **4–5 times at most**; natural variations otherwise.
- Each supporting keyword used naturally in the body; one in at least one FAQ question.
- No stuffing. If a keyword sounds forced, rephrase or drop it. Final read: every chosen keyword appears naturally and none were missed.

### Statistics and links

- **Statistics:** when a fact needs a number, write "According to stats by [Source], …" with the hyperlink on the words **stats by [Source]**: "According to [stats by the ONS](url), over half of UK firms…". With several statistics in one blog, vary the phrasing ("[the ICO's 2025 figures](url) show…") so it doesn't become a pattern, always linking the source name.
- Every statistic, quote and data point is hyperlinked where it appears; links open in a new tab when published.
- **Solution link:** at least one, descriptive anchor text naming the service.
- **Read also:** **Read also:** [Exact title of the Appnable blog](url). Real, published Appnable blogs only.

### FAQs

Two real questions (sales calls, comments, Google "People also ask"), written as a reader types them. Answer in **40–60 words**, directly in the first sentence, ending with "See more on our [FAQ page](FAQ page URL)." Use a supporting keyword in at least one question. List both questions in the delivery summary so the author can check they exist on the FAQ page.

### Products and clients

- **StGatherly** and **KoKoodi** are Appnable's own products; **Pendroply** is a client-based app. Label them correctly and never describe a product beyond what the reference files or author supply.
- Use case studies exactly as published on appnable.com (named where the site names them, anonymous where it doesn't). Never add client names, quotes or figures beyond that without written approval.
- Appnable implements **Odoo** for ERP. Don't claim Dynamics 365 work.

### Writing style

- **UK English** throughout (organise, optimise, licence/license, programme, colour, centre, analyse, behaviour, enrol, travelling; dates as "12 October 2026"); consistent spelling, punctuation and terminology.
- **Appnable's voice:** plain, confident, specific, slightly dry; claims backed by delivered work (see the voice examples in `appnable-company.md`).
- **For a busy decision-maker:** lead with the answer, then explain; active voice.
- **Short:** paragraphs of 3–4 sentences; most sentences under 25 words; bullets or a short table for steps, options or comparisons.
- **Transitions:** natural ones where they genuinely link ideas; never forced, never the same twice in a row; no filler (Furthermore, Moreover, Additionally).
- **Not generic:** every section should contain at least one thing only Appnable would say: a case study figure, a named tool from its stack, a concrete scene from legal, financial services, pharmaceuticals or government, or a clear position.
- **Technical accuracy:** explain acronyms on first use; name versions and dates where they matter ("as of October 2026"); flag technical claims for SME review.

### Commercial value test

Before delivering, ask: *if a reader finished this blog and went to Microsoft's (or any vendor's) site instead of contacting Appnable, would they have lost anything?* If not, the blog is too generic. Rewrite the middle so it covers what the documentation doesn't, and prove Appnable's value with a published case study.

### Images

**No AI-generated images.** Diagrams drawn for the article (such as the workflow illustration) are fine. Suggest a cover image and any helpful in-blog visuals from the sources in `references/image-sources.md` only (Unsplash, Pexels, Pixabay, unDraw, ManyPixels, Streamline HQ), with search terms, alt text and the cover image source in the header block. If you can't confirm a specific image page, give the site's search URL and terms rather than inventing an image link. Remind the author to compress each image to under 200 KB.

## Step 3: Humanize (two-pass edit, every blog)

Apply `references/humanizing-rules.md` to the full draft:

1. **Diagnose:** uniform sentence rhythm, predictable word choices, filler transitions, banned words, rule-of-three lists, em dashes, colon-led summaries, generic advice.
2. **Rewrite:** vary sentence length sharply, active voice, natural cadence, abstract claims made concrete with Appnable specifics.
3. **Verify:** if a sentence would read as formulaic to a person or an AI detector, loosen it.

Keep keywords, figures and links exactly intact through the edit.

## Step 4: Check the draft

Run the full review in the `seo-blog-checklist` skill (`../seo-blog-checklist/SKILL.md`) and fix everything it fails before delivering. Its automated part is:

```bash
python scripts/seo_check.py blog.docx --keyword "Copilot readiness assessment" \
  --supporting "Copilot data security" "Microsoft 365 consultancy"
```

The checker covers Marketing's checklist (length, title and meta, keyword placement and count, structure, FAQs, links, no references, UK spelling) plus the humanizing rules (banned words, em dashes, rule-of-three lists, sentence-length variety, filler transitions), the cover image source and the mid-blog selling section. Fix every FIX; review every WARN. Then do your own final read for flow, keyword naturalness and anything generic.

## Step 5: Deliver

Read the `docx` skill, then create one Word document per blog: real Heading 1/2/3 styles, real lists, clickable hyperlinks. Use the Appnable brand colours from `appnable-company.md` (H1 #1A1A1A, H2 #4F6B12, H3 #595959; green #A0C63F and grey #818181 in images). Never navy or blue. On a new page at the end, add **"Pre-publish checklist"** with every item from the guidelines, ☑ where the draft passes and ☐ where a person must still act (images, SME technical review, marketing review, read aloud, Grammarly UK, FAQ page match, any placeholders).

In the chat, summarise briefly: word count, keyword count, the selling angle used, open checklist items, technical claims for SME review, and the two FAQ questions. Remind the author about the two reviews (technical and marketing) and to log the primary keyword in the tracker.

## Humanizing text on request

When the author pastes text and asks to humanize it (or make it sound less AI-generated), apply `references/humanizing-rules.md` and **return only the humanized text** unless they ask for an editorial note. Keep keywords, figures and links unchanged.

## Optional: external humanizer (e.g. Stealth Writer)

Only if the author still wants to use one after the built-in edit:

1. If Claude in Chrome tools are available and the humanizer tab is open, work there; otherwise give the author text to paste.
2. Split into parts under the tool's word limit (default 1,000), breaking at headings: `python scripts/seo_check.py blog.docx --keyword "…" --chunks 1000`.
3. Leave out the header block, links and checklist; plain text only. Tell the author the primary keyword count per part and to freeze all chosen keywords.
4. When the text returns: restore keywords, UK spelling, links and the checklist; re-run the checker; rebuild the Word file.

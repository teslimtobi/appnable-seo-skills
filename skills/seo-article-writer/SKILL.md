---
name: seo-article-writer
description: For Appnable and its products (including KoKoodi). Write complete, publish-ready SEO articles (blog posts) from approved topics and focus keyphrases, in the author's house style, delivered as downloadable Word documents. Each article has a keyphrase line, meta description and site name above the title, the keyphrase used exactly 7 times (title, intro, at least two headings, body, conclusion), about 1,500 words, an FAQ section, four "Read also"/"Also read" in-text links whose anchor text is the linked page's title, and a numbered reference list. Use this skill whenever the user asks to write, draft or produce SEO content, SEO articles, blog posts for a website, or "the articles" for topics from keyword research, and when they ask to prepare an article for a humanizer such as Stealth Writer. Follow the author's own instructions wherever they differ from these defaults.
---

# SEO Article Writer

Turn approved topics into finished SEO articles that match the author's house style. Topics usually come from the `seo-keyword-research` skill; if the user hasn't approved a topic and keyphrase yet, confirm them first.

**The author's instructions always win.** Every rule below is a default. If the author states a different word count, keyphrase count, citation style, spelling, tone or format, follow the author.

## Company context: Appnable

These skills are built for **Appnable** and its products. Unless the author names a different company, assume all research and writing is for Appnable.

- **Company:** Appnable, a UK-based Microsoft 365 consultancy (website: appnable.com).
- **What it does:** Microsoft 365 consulting, AI-powered Office automation, branded digital solutions such as Office templates and document systems, and integrations with Power Platform and SharePoint.
- **Flagship product:** KoKoodi (kokoodi.com), an AI Office automation platform for document intelligence, Office automation, workflows and compliance.
- **Target readers:** legal, financial and professional services firms; partners, COOs, finance directors, practice managers, IT and operations leads.
- **Market and spelling:** UK first, so use UK English (organise, licence, programme) unless the author says otherwise.
- **Call to action:** end each article with 1–2 sentences inviting readers to contact Appnable or book a KoKoodi demo, matched to the topic.
- **Topic fit:** prefer topics that lead naturally to Appnable's services or KoKoodi, such as Microsoft 365, Copilot, Power Automate, SharePoint, document automation, Office templates, and AI for legal and finance.

Check appnable.com and kokoodi.com for current services, product details and existing articles before each project, since they change over time. If the sites block automated access, ask the author for the details or article links rather than guessing.

## Inputs

- Approved title(s) and focus keyphrase(s), plus secondary keywords if available.
- The website/company the article is for (default: Appnable, so `appnable.com` goes above the title and the call to action points to Appnable or KoKoodi).
- Any internal articles to link to (titles + URLs from the company's own site).
- Defaults if not stated: ~1,500 words, keyphrase × 7, 4 in-text links, Word output, UK English.

## Step 1: Research real sources

Search the web for 4+ credible sources per article (official docs, research firms, industry reports, regulators, reputable publications). Prefer pages you actually fetched or that appeared in search results. Note each source's **page title** and **exact URL**.

Only use facts and statistics you found in those sources, and attribute them in the sentence ("McKinsey estimates…"). Never invent statistics, quotes, URLs or article titles. If the author asked for internal links to their own site but you can't find or verify those pages, say so and ask for the titles and URLs instead of guessing; a broken link hurts SEO.

## Step 2: Write the article

Read `references/style-template.md` before writing; it holds the house layout and voice, with a skeleton.

### Header block (above the title, exactly this order)

```
Keyphrase: [Keyphrase in Title Case] (used 7 times in the article)
Meta description: [≤155 characters, includes the keyphrase, written as a hook]
[company-domain.com]
```

### Title (H1)
Build the keyphrase into the title itself, ideally at the start: "Microsoft 365 Automation: 7 Ways to Save Hours Every Week".

### Body structure (default)
1. **Introduction** (2 short paragraphs): hook the reader with their problem, use the keyphrase in the first paragraph, then tell them what the article covers and invite them to keep reading.
2. **"What Is [Keyphrase]?"** (H2, keyphrase #3): plain-English definition and how it works.
3. **"Why / Benefits of [Keyphrase] …"** (H2, keyphrase #4): the case for it, with a sourced statistic.
4. **Main practical section** (H2), e.g. "7 Practical Ways to …", with numbered H3 sub-points, each a short paragraph. Mention the keyphrase in the section intro.
5. **"How to Start / Choose …"** (H2, often a keyphrase heading): numbered steps.
6. **Cons / mistakes / risks** (H2): bullet points with a bold lead-in.
7. **Frequently Asked Questions** (H2): 3–4 real questions (from Google "People also ask"), each as an H3 with a 2–3 sentence answer.
8. **Final Thoughts** (H2): recap, keyphrase used once, then a short call to action for the company.
9. **References** (H2).

Adapt headings to the topic; keep the keyphrase placement rules.

### Keyphrase rules
- Use the exact keyphrase **7 times**, counted from the title through the conclusion (the header block and references don't count).
- Must appear in: the title, the introduction, and **at least two H2 headings**. Spread the rest through the body and conclusion.
- Don't use the exact phrase anywhere else; use natural variations ("automating your Microsoft tools") so the count stays exact.

### In-text links ("Read also")
- Exactly **4** per article, each on its own line directly after the paragraph it supports.
- Alternate the lead-in: **Also read:** / **Read also:**
- The anchor text is the **title of the page being linked** (an article or report title), hyperlinked to its URL. Never print a raw URL in the body and don't use "Click here".
  - Good: **Read also:** [The Economic Potential of Generative AI: The Next Productivity Frontier](url)
  - Avoid: Read also: Click here to explore Copilot docs (https://…)
- Link to the external sources from Step 1 by default. If the author provides internal articles from their own site, use those instead.

### References
Numbered list at the end: `Publisher, "Page title." full-URL` with the URL hyperlinked. Include every source used in the article (normally the same 4 as the in-text links).

### Voice
Simple, direct, conversational English; short paragraphs (2–4 sentences); speak to the reader as "you"; use transition words (Also, Furthermore, Additionally, However) without overdoing them; bold lead-ins on list items. Details in `references/style-template.md`.

## Step 3: Check before delivering

Run the checker on each finished .docx:

```bash
python scripts/seo_check.py article.docx --keyphrase "Microsoft 365 automation"
```

It reports the keyphrase count (title → conclusion), whether it's in the title, intro and how many headings, word count excluding references, and the number of "Read also/Also read" links. Fix anything off, then re-run. Target: keyphrase 7, ≥2 headings, ~1,500 words (±5%), 4 links.

## Step 4: Deliver as Word documents

Read the `docx` skill, then create **one .docx per article** (e.g. `Microsoft_365_Automation_Article.docx`). Use real Word headings (Heading 1 for the title, Heading 2 for sections, Heading 3 for sub-points and FAQ questions), real numbered/bulleted lists, and clickable hyperlinks. Present the files and summarise in a few lines: keyphrase count, word count, and any links or facts the author should double-check.

## Optional: preparing for a humanizer (e.g. Stealth Writer)

If the author wants to run the articles through a humanizer:

1. If Claude in Chrome tools are available and the author's humanizer tab is open, work in that tab; otherwise give the author text to paste.
2. Split each article into parts **under the tool's word limit** (default 1,000 words), breaking at headings.
3. Leave out the header block, the "Read also" lines and the references; humanizers break hyperlinks. Plain text only (no markdown).
4. For each part, tell the author how many times the keyphrase appears, and remind them to freeze/protect the keyphrase if the tool allows.
5. When the humanized text comes back, check the keyphrase is still used exactly 7 times (restore exact wording if the tool changed it), put the header block, "Read also" links and references back in their places, and rebuild the Word files. `python scripts/seo_check.py article.docx --keyphrase "…" --chunks 1000` writes the parts to text files automatically.

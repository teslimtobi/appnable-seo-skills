---
name: seo-keyword-research
description: For Appnable and its products (including KoKoodi). Research high-ranking SEO keywords (long-tail and short-tail) and propose blog topics tied to Appnable's five service areas (Microsoft 365/Copilot, Automation, Custom software, ERP, Compliance-led technology), using free SEO tools (Google Keyword Planner, Google Trends, Search Console, Ahrefs free tools, Semrush free account, Ubersuggest, AnswerThePublic, AlsoAsked) plus live Google results. For each topic, picks one primary keyword and 2–4 supporting keywords, confirms search volume, checks the content tracker so no primary keyword is reused, and delivers a keyword research Word document for approval. Use this skill whenever the user asks for SEO topic ideas, keyword research, a primary or focus keyword, "what should we write about", blog ideas, or says they need to research topics before writing, even if they don't say "keyword research". Run this BEFORE the seo-article-writer skill; topics only go to writing once the author approves them.
---

# Appnable SEO Keyword Research

Find topics Appnable can realistically rank for, choose one primary keyword and 2–4 supporting keywords per topic, and hand the author a short Word document to approve. Writing is a separate step (`seo-article-writer`) that starts only after approval.

The **Appnable Blog Writing Guidelines** from Marketing set the rules. Read the keyword section in `../seo-article-writer/references/appnable-blog-guidelines.md` before starting. The author's instructions in the conversation override any default here.

## Company context: Appnable

Read `../seo-article-writer/references/appnable-company.md` (who Appnable is, its five solutions, products and case studies) and every file in `../seo-article-writer/references/company-docs/` before researching. Topics must fit what Appnable actually delivers.

- **Company:** Appnable Ltd, a UK enterprise consultancy since 2003, working "where documents, compliance and Microsoft 365 meet" (appnable.com).
- **Solutions:** custom software · automation · Microsoft 365 and Copilot · ERP and business systems (Odoo) · consulting.
- **Own products:** KoKoodi (AI Office automation platform) and StGatherly (membership, communications and giving platform). **Client-based app:** Pendroply. Label them correctly.
- **Group:** Wingato (engineering, delivery, R&D).
- **Readers:** decision-makers and technical buyers in **legal, financial services, pharmaceuticals and government**.
- **Market:** United Kingdom. Research UK search data; use UK English.

### The five keyword groups (start here)

Every topic must tie to a service Appnable sells. These are Marketing's starting keywords:

| Service area | Primary keyword | Supporting keywords |
| --- | --- | --- |
| Microsoft 365 / Copilot | Microsoft Copilot consultant UK | Copilot readiness assessment, Copilot data security, Microsoft 365 consultancy |
| Automation | business process automation UK | workflow automation for regulated industries, Power Automate consultant, AI automation platform |
| Custom software | custom software development UK | bespoke business software, software development for financial services, legal tech development |
| ERP | ERP implementation UK | ERP consultancy, Dynamics 365 implementation*, replacing spreadsheets with ERP |
| Compliance-led technology | technology consultancy for regulated industries | GDPR compliant software, data governance consultancy, digital transformation for law firms |

\* **Appnable implements Odoo, not Dynamics 365** (appnable.com/solutions). Until Marketing confirms otherwise, don't propose Dynamics 365 keywords; use Odoo equivalents such as "Odoo implementation UK" and flag the swap in the research document.

Use these as seeds. Also consider keywords for KoKoodi and StGatherly (e.g. membership management software UK, charity donation platform, Gift Aid software) when the author asks for product topics. A blog's primary keyword can be one of them or a closely related long-tail variant found in research (e.g. "Copilot readiness assessment" as a primary keyword for a readiness blog).

## Inputs

Use what the author already gave; ask only for what's missing, in one message:

- Number of topics (default: 2) and, if they have a preference, which service area(s).
- Any topic ideas they already have.
- The content tracker, or the list of published blogs and their primary keywords (also in `../seo-article-writer/references/appnable-links.md`).

## Step 1: Check what already exists

Read the Published blogs table in `appnable-links.md` (or the tracker the author shares) and note every primary keyword already used. **Never propose a primary keyword that another blog already targets**; they would compete in search. Note related blogs that could become "Read also" links.

## Step 2: Pull keyword data

Use the best data source available, in this order:

1. **Connected SEO connectors** (Ahrefs, Semrush, Search Console). If none are loaded, search the connector directory (`search_mcp_registry` with `["seo", "ahrefs", "semrush", "keywords"]`) and offer any that fit.
2. **The author's browser** (Claude in Chrome, if available) for free tools they're signed into.
3. **Free public tools and live Google results** via web search and fetch.
4. **No tool access:** do the qualitative research and leave volume as "verify in [tool]" with the checklist in Step 6.

| Tool | Free tier | Use it for |
| --- | --- | --- |
| Google Keyword Planner | Free with a Google Ads account | UK monthly search ranges, related keywords |
| Google Trends | Free | Rising or falling interest in the UK, seasonality |
| Google Search Console | Free (site owner) | Queries appnable.com already appears for; quick wins |
| Google search | Free | Autocomplete, "People also ask", "Related searches", who ranks now |
| Ahrefs Free Keyword Generator / Webmaster Tools | Free, limited | Keyword ideas, rough difficulty, questions |
| Semrush free account | ~10 requests/day | UK volume, keyword difficulty (KD%), intent |
| Ubersuggest | ~3 searches/day | Volume, difficulty, content ideas |
| AnswerThePublic / AlsoAsked | Limited free | Question keywords for H2s and FAQs |

**Never invent numbers.** Only report volume, difficulty or CPC a tool actually returned, naming the tool and "UK". Otherwise write "verify in [tool]". The guidelines require search volume to be confirmed, so flag every unconfirmed figure.

## Step 3: Choose the keywords

For each candidate, look at page one of Google UK and judge:

- **High-ranking and relevant:** real UK search demand, tied to an Appnable service.
- **Long-tail vs short-tail:** short-tail terms have more volume but are hard to rank for; long-tail terms (4+ words) are easier and closer to buying intent. Prefer long-tail unless the data shows a short-tail term is winnable.
- **Intent:** informational, commercial or transactional. Match the blog type to what already ranks.
- **Not already used** as a primary keyword (Step 1).

Then pick **one primary keyword** and **2–4 supporting keywords** per topic, plus 1–2 "People also ask" questions for the FAQs (one should contain a supporting keyword).

## Step 4: Draft the SEO basics per topic

- **Working title:** under 60 characters, primary keyword near the start, clear benefit. Give the character count.
- **URL slug:** `/blog/` + short, lowercase, hyphenated, keyword only, no dates or stop words.
- **Meta description:** 140–160 characters, includes the primary keyword. Give the character count.
- **Keyword placement plan:** primary keyword in the title, URL and first 100 words; exact phrase 4–5 times at most in the blog; supporting keywords used naturally in the body and one FAQ question.
- **Suggested Solution page** to link to, and **suggested "Read also" blogs** (if any exist).
- **Suggested call to action** (book a demo, download a lead magnet, or contact us; the site's main CTA is Book a call, https://www.appnable.com/contact/).
- **Selling angle:** the Appnable service, product or case study (from `appnable-company.md`) the blog's mid-section will feature.

## Step 5: Deliver the keyword research document

Read the `docx` skill, then create `Keyword_Research_Appnable.docx` with:

1. **Heading:** "SEO Keyword Research: [N] Topics for Appnable", with the date.
2. **Summary table** (one column per topic): Service area · Primary keyword · Supporting keywords · Long/short-tail · UK search volume (tool) · Difficulty (tool) · Search intent · Working title (characters) · URL slug · Meta description (characters).
3. **One section per topic:** why this topic (business fit, in 1–2 sentences), the keyword data with sources, FAQ question ideas, placement plan, selling angle, suggested Solution page, Read also candidates and CTA.
4. **Already-used primary keywords** checked (from the tracker), so reviewers can see no duplicates.
5. **How to verify** (numbered): Keyword Planner for UK volume; Semrush/Ahrefs for difficulty and current rankers; Google "People also ask" for FAQs; Search Console after publishing.

Keyword research only; no blog drafts in this document. Use UK English.

## Step 6: Get approval

Present the file and ask the author to approve, swap or tweak the topics. Remind them to log each approved primary keyword in the content tracker. Once approved, use the `seo-article-writer` skill.

---
name: seo-keyword-research
description: For Appnable and its products (including KoKoodi). Research SEO keywords and propose blog/article topic ideas for a website or client, using free SEO tools (Google Keyword Planner, Google Trends, Search Console, Ahrefs free tools, Semrush free account, Ubersuggest, AnswerThePublic, AlsoAsked) plus live Google results, then deliver a keyword research Word document for the author to approve. Use this skill whenever the user asks for SEO topic ideas, keyword research, a focus keyphrase, "what should we write about", content ideas for a company blog, or says they need to research topics before writing SEO content, even if they don't say "keyword research" explicitly. Run this BEFORE the seo-article-writer skill; topics only go to writing once the author approves them.
---

# SEO Keyword Research

Find topics a business can realistically rank for, pick one focus keyphrase per topic, and hand the author a short Word document they can approve. Writing the articles is a separate step (the `seo-article-writer` skill) and only starts after the author approves the topics.

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

## Inputs to collect

Use what the user already gave you; ask only for what's missing, in one question.

- **The website or company** (default: Appnable, appnable.com; KoKoodi topics go to kokoodi.com when the author says so).
- **Number of topics** (default: 2).
- **Target market / country** (default: United Kingdom; affects volumes and spelling).
- **Any topics or keywords the author already has in mind.**

## Step 1: Understand the business

Search the web for the company and read its site (homepage, services, product pages, existing blog). Note:

- What it sells and to whom (industries, roles, company size).
- Existing blog topics, so new topics don't duplicate them, and so they can later serve as internal links.
- Brand or product names worth mentioning in a call to action.

If the site blocks automated access, use search snippets, company profiles (LinkedIn, RocketReach, Crunchbase) and tell the author what you couldn't see.

## Step 2: Generate seed keywords

From what the business sells, write 10–20 seed phrases the target buyer would type into Google. Favour problem-and-solution phrasing ("automate approvals", "document automation for law firms") over brand jargon.

## Step 3: Pull data from SEO tools

Use the best data source available, in this order:

1. **Connected SEO connectors.** Check the tool list for Ahrefs, Semrush, Google Search Console or similar connectors. If none are loaded, search the connector directory (`search_mcp_registry` with keywords like `["seo", "ahrefs", "semrush", "keywords"]`) and offer any that fit. A connector gives real volume and difficulty numbers, so it is worth one check.
2. **The author's browser** (Claude in Chrome, if available). Free tools the author is signed into can be read directly.
3. **Free public tools via web search/fetch**, and live Google results (see the table below).
4. **No tool access at all**: do the qualitative research (SERPs, People also ask, competitor pages) and give the author the verification checklist from Step 6 to fill in the numbers themselves.

| Tool | Free tier | Use it for |
| --- | --- | --- |
| Google Keyword Planner | Free with a Google Ads account (no spend needed) | Monthly search ranges by country, related keywords |
| Google Trends | Free | Rising vs falling interest, seasonality, regional demand |
| Google Search Console | Free (site owner) | Queries the site already gets impressions for; quick wins |
| Google search itself | Free | Autocomplete, "People also ask", "Related searches", who ranks now |
| Ahrefs Free Keyword Generator / Webmaster Tools | Free, limited | Keyword ideas, rough difficulty, question keywords |
| Semrush free account | ~10 requests/day | Volume, keyword difficulty (KD%), intent label |
| Ubersuggest | ~3 searches/day free | Volume, SEO difficulty, content ideas |
| AnswerThePublic / AlsoAsked | Limited free searches | Question-style keywords for H2s and FAQs |
| Moz Keyword Explorer | Limited free queries | Difficulty and SERP analysis |

**Never invent numbers.** Only report search volume, difficulty or CPC that a tool actually returned, and name the tool and country. If you couldn't get a number, write "verify in [tool]" rather than estimating. Made-up metrics get repeated in client reports and destroy trust.

## Step 4: Choose the topics

For each candidate keyphrase, look at page one of Google and judge:

- **Search intent**: informational (how/what), commercial (best, vs, tools for), transactional. Match the article type to what already ranks.
- **Rankability**: if page one is all huge brands, prefer a longer, more specific phrase.
- **Business fit**: the article should lead naturally to the company's service or product.
- **Freshness**: avoid topics the site already covers well.

Pick one **focus keyphrase** per topic (usually 2–5 words) and 4–6 **secondary keywords** plus a few related terms (LSI) to use naturally. Write a working title with the keyphrase built into it, a URL slug, and a meta description (under 155 characters, keyphrase included).

## Step 5: Plan keyphrase placement

The writing skill uses the keyphrase **7 times** by default. Plan where:

1. Title (H1)
2. Introduction, first paragraph
3. An H2 (e.g., "What Is [keyphrase]?")
4. A second H2 (e.g., "Benefits of [keyphrase] for …")
5. Body text
6. A third H2 or body text
7. Conclusion

The meta description also contains the keyphrase but doesn't count toward the 7.

## Step 6: Deliver the keyword research document

Create a Word document (read the `docx` skill first) named `Keyword_Research_[Company].docx` with:

1. **Heading**: "SEO Keyword Research: [N] Topics for [Company]" and one sentence on what the company sells and to whom.
2. **Summary table**, one column per topic, rows: Focus keyphrase · Article title · URL slug · Search intent · Target reader · Volume / difficulty (with tool name, or "verify") · Keyphrase uses (7).
3. **One section per topic**: focus keyphrase, why this topic (1–2 sentences on business fit), secondary keywords (bullets), related terms (bullets), meta description, keyphrase placement plan (numbered 1–7), and suggested internal links (existing posts on the company site, if found).
4. **How to verify these keywords**: a numbered checklist (Keyword Planner for volume by country; Semrush/Ahrefs for difficulty and current rankers; Google "People also ask" for extra H2s/FAQs; Search Console after publishing to track impressions and position).

Keep it to just the keyword research; no article drafts in this document.

## Step 7: Get approval

End by presenting the file and asking the author to approve, swap or tweak the topics. Once approved, use the `seo-article-writer` skill to write the articles.

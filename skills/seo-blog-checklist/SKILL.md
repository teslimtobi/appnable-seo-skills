---
name: seo-blog-checklist
description: For Appnable and its products (KoKoodi, StGatherly). Review any blog draft against Marketing's Appnable Blog Writing Guidelines pre-publish checklist plus Appnable's own rules (UK English, humanizing rules, mid-blog selling section, credited non-AI cover image, "According to stats by…" links), and report pass/fail for every item with exact fixes. Works on Word files, pasted text or a linked document, whoever wrote the blog. Use this skill whenever the user asks to check, review, proofread, QA, audit or approve a blog or article, asks "is this ready to publish", "does this pass the checklist", "run the checklist", wants a marketing or pre-publish review, or shares a draft and asks what's missing. Also used by the seo-article-writer skill as its final check.
---

# Appnable Blog Checklist

Check a blog against every rule a blog must pass before it goes live, and tell the author exactly what to fix. **If a draft fails one checklist item, it is not ready to publish.**

The rules live in the writer skill's reference files; read them first, every time:

- `../seo-article-writer/references/appnable-blog-guidelines.md`: Marketing's pre-publish checklist and rules (the source of truth, with the original PDF beside it).
- `../seo-article-writer/references/humanizing-rules.md`: banned words, rhythm, transitions, anti-generic rules.
- `../seo-article-writer/references/appnable-company.md` and `../seo-article-writer/references/company-docs/`: what Appnable does, products, case studies (to judge accuracy and the selling section).
- `../seo-article-writer/references/image-sources.md`: approved image sources.
- `../seo-article-writer/references/appnable-links.md`: Solution, contact and FAQ links, and published blogs (to spot a reused primary keyword).
- `../seo-article-writer/references/review-lessons.md`: past reviewer feedback; every lesson is a checklist rule.

The author's instructions in the conversation override these defaults.

## Step 1: Get the draft and its keywords

- **Word file:** use it directly.
- **Pasted text or another format:** save it as a .docx first (read the `docx` skill), keeping headings as Heading 1/2/3 and links as hyperlinks, so the checker can read the structure.
- **Primary and supporting keywords:** take them from the header block ("Primary keyword:", "Supporting keywords:") or ask the author. Without the primary keyword, half the checklist can't be checked.

## Step 2: Run the automated checks

```bash
python ../seo-article-writer/scripts/seo_check.py blog.docx --keyword "primary keyword" \
  --supporting "supporting 1" "supporting 2"
```

FIX = fails a rule, WARN = likely problem to judge, INFO = reference.

## Step 3: Do the checks a script can't

Read the whole blog and judge:

- **Keywords:** used naturally, not forced; none of the chosen keywords missed; primary keyword not already used by another published blog.
- **Brand voice and accuracy:** sounds like Appnable (plain, confident, specific); nothing misrepresents Appnable's services or products (e.g. ERP is Odoo; StGatherly and KoKoodi are Appnable's own products; Pendroply is a client app); case studies match appnable.com exactly; no unapproved client names or data.
- **Sources:** each link actually supports its claim, is credible, is the original source, and is no older than three years (year stated) unless historical. No competitor blogs, Wikipedia or AI summaries.
- **Selling section:** sits mid-blog, is specific (a real case study figure or named service/product), and helps rather than pitches.
- **Commercial value:** the blog shows why a reader should engage Appnable rather than do it themselves. It doesn't just repeat vendor documentation, it has a section on where DIY stalls, and a reader who left for Microsoft's site would lose something.
- **Visual story:** automation or process blogs have the Trigger → Automation action → Approval / validation → Business outcome illustration with caption, alt text and step bullets.
- **Not generic and human-sounding:** varied sentence rhythm, no formulaic phrasing, concrete scenes from legal, financial services, pharmaceuticals or government; an intro no other firm could reuse.
- **FAQs:** real questions, answered in the first sentence; flag that both questions must exist on the website's FAQ page.
- **Call to action:** exactly one, clear, matched to the topic.
- **Images:** no AI images; cover image from an approved source and credited; alt text present.
- **Technical claims:** list every technical claim, step or product/version statement for the subject-matter expert.

## Step 4: Report

Reply with a short verdict first: **Ready to publish** / **Not ready: [N] items to fix**. Then a table with one row per item, in this order:

| # | Checklist item | Status | What to fix |
| --- | --- | --- | --- |

Statuses: ✅ Pass · ❌ Fail · ⚠️ Check by hand (a person must confirm). Rows:

**Marketing's pre-publish checklist**
1. 1,500 words or fewer (body + FAQs); 1,000–1,500 target
2. Keywords researched with the Claude keyword research skill
3. Primary keyword in the title, URL and first 100 words
4. Supporting keywords used naturally in the body
5. No keyword stuffing (primary keyword 4–5 times at most); none missed
6. Title under 60 characters; meta description 140–160 characters
7. UK English throughout (Grammarly or similar set to UK English: ⚠️ for a person)
8. Spelling, punctuation and terminology consistent
9. Brand voice and expertise; accurate, not misrepresented
10. Every statistic, quote and data point hyperlinked where it appears; no reference list
11. One internal link to an Appnable Solution page
12. Two FAQs, each answer ending with a link to the FAQ page
13. Two or three "Read also" links to Appnable blogs (✅ if left out of the first one or two blogs)
14. One clear call to action
15. Images compressed and not high definition (⚠️ for a person)
16. Technical claims checked by a subject-matter expert (⚠️ for a person; list the claims)
17. Proofread and read aloud once for flow (⚠️ for a person)

**Appnable additions**
18. Structure: intro 80–120 words; 3–5 H2s; no skipped heading levels; conclusion 60–100 words ending with the CTA
19. Humanizing rules: no banned words, rule-of-three lists or excess em dashes; varied sentences; not generic
20. Mid-blog selling section, specific and accurate
21. Statistics written as "According to stats by [Source]" with the link on the source
22. Cover image from an approved library, source credited, alt text; no AI images
23. Commercial value: why Appnable rather than DIY; a "where DIY stalls" section; not a repeat of vendor documentation
24. Conclusion follows the reviewer's model: question heading, tangible business outcome, one outcome-named CTA
25. Workflow illustration (Trigger → Action → Approval / validation → Outcome) or another story-telling visual

Keep each "What to fix" note to one line and quote the exact sentence or heading where useful. After the table, list the technical claims for SME review and the two FAQ questions to match on the FAQ page.

## Step 5: Offer the fixes

Offer to fix everything marked ❌ (and the ⚠️ items Claude can act on). If the author agrees, edit the draft, keeping their wording wherever it already passes, re-run Steps 2–4, and deliver the updated Word file with a **"Pre-publish checklist"** page at the end (☑ for passes, ☐ for items a person must still complete). Remind the author about the two reviews before publishing: technical and marketing.

# Appnable Blog Writing plugin for Claude (v2.0.0)

An SEO blog agent for Appnable (appnable.com) and KoKoodi (kokoodi.com), built on Marketing's **Appnable Blog Writing Guidelines**.

- **seo-keyword-research** skill: UK keyword research with free SEO tools, using the five Appnable keyword groups; one primary + 2-4 supporting keywords per topic; checks the tracker so no primary keyword is reused; Word report for approval.
- **seo-article-writer** skill: 1,000-1,500-word blogs in UK English with the primary keyword in the title, URL and first 100 words (max 4-5 uses), inline source links (no reference list), one Solution page link, two FAQs ending with the FAQ page link, "Read also" links to Appnable blogs, one call to action, and the pre-publish checklist attached. Includes a checker script.
- **seo-blog-checklist** skill: reviews any blog draft (Word or pasted) against the pre-publish checklist and Appnable rules, item by item, with fixes.
- **/seo-article** command: research, approval, then writing.
- **/seo-checklist** command: run the checklist on a draft.

Keep `skills/seo-article-writer/references/appnable-links.md` up to date (FAQ page, Solution pages, published blogs).

## Changes in 2.0.0
- Plugin renamed from appnable-seo to Appnable Blog Writing (appnable-blog-writing). Skills and commands are unchanged. Remove the old appnable-seo plugin after installing this one.

## Changes in 1.4.2
- Appnable brand colours (green #A0C63F, grey #818181) added to the company file and used in images, the workflow diagram and Word headings. No navy.

## Changes in 1.4.0
- Reviewer feedback from the Microsoft 365 Automation blog added as rules (`references/review-lessons.md`): show why Appnable rather than DIY, don't repeat vendor documentation, a "where DIY stalls" section, the reviewer's model CTA tied to a business outcome, and a workflow illustration.
- New `scripts/workflow_diagram.py` draws the Trigger -> Automation action -> Approval / validation -> Business outcome illustration (not AI-generated, under 200 KB).
- Checklist skill: three new items (commercial value, outcome-led CTA, story-telling visual). Checker: image and DIY-section checks.

## Changes in 1.3.0
- New seo-blog-checklist skill and /seo-checklist command, so any draft can be checked, whoever wrote it. The writer skill now uses it as its final check.

## Changes in 1.2.0
- Appnable company knowledge from appnable.com: solutions, voice, group (Wingato, KoKoodi, StGatherly), products vs client apps (Pendroply), case studies.
- `references/company-docs/` folder for Appnable documents (read before every task).
- Mid-blog selling section in every blog, grounded in a real case study or service.
- Humanizing rules built in: banned words, rule-of-three, em dashes, sentence rhythm, anti-generic rules; "humanize this" returns only the text.
- No AI images: approved free libraries only, with the cover image source credited.
- Statistics written as "According to stats by [Source]" with the link on "stats by [Source]".
- Real links file: Solutions, Case studies, Contact, product sites. ERP is Odoo, not Dynamics 365.
- Checker extended for all of the above.

## Changes in 1.1.0
- Rebuilt around the Appnable Blog Writing Guidelines and pre-publish checklist.
- Primary keyword max 4-5 uses (was exactly 7); length 1,000-1,500 words max (was ~1,500).
- Sources hyperlinked inline; reference list removed.
- "Read also" now links to Appnable blogs only (1 inline + block of 2-3), optional for the first blogs.
- Two FAQs of 40-60 words, each ending with the FAQ page link.
- UK English, transitional paragraph openers, cliché ban, acronym rule, SME review flags.
- New checker covering every automatable checklist item.

---
description: Run the full Appnable SEO blog workflow, from keyword research to checklist-ready Word drafts
argument-hint: "[number of topics, service area or topic idea]"
---

Run the Appnable SEO blog workflow for: $ARGUMENTS

1. Use the `seo-keyword-research` skill to research keywords and topics for Appnable (or KoKoodi if named), check the content tracker for primary keywords already used, and deliver the keyword research Word document.
2. Stop and ask the author to approve, swap or tweak the topics. Do not start writing until they approve.
3. Once approved, use the `seo-article-writer` skill to write each blog in line with the Appnable Blog Writing Guidelines, run the checker, and deliver one Word document per blog with the pre-publish checklist attached.
4. Summarise what's still open on the checklist (images, SME technical review, marketing review, FAQ page match) and remind the author to log each primary keyword in the content tracker.
5. If the author wants to humanize the blogs, follow the humanizer section of `seo-article-writer`.

The author's own instructions override any default; Marketing's guidelines override the skills' other defaults.

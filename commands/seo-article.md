---
description: Run the full Appnable SEO workflow, from keyword research to finished Word articles
argument-hint: "[number of topics or a topic idea]"
---

Run the Appnable SEO content workflow for: $ARGUMENTS

1. Use the `seo-keyword-research` skill to research topics for Appnable (or KoKoodi if named) and deliver the keyword research Word document.
2. Stop and ask the author to approve, swap or tweak the topics. Do not start writing until they approve.
3. Once approved, use the `seo-article-writer` skill to write each article as its own Word document, run the checker, and report the keyphrase count, word count and links.
4. If the author wants to humanize the articles, follow the humanizer section of `seo-article-writer`.

The author's own instructions override any default in either skill.

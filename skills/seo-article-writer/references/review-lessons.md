# Lessons from reviews (read before every blog)

Feedback from Appnable reviewers on published or draft blogs. Each lesson is now a rule. Add new feedback here as it arrives (date, blog, what was said, the rule).

## October 2026: "Microsoft 365 Automation" blog (reviewer comments in Word)

### 1. Commercial value: answer "why Appnable, not DIY?"

> "The article is too generic... it does not sufficiently demonstrate why a potential client should engage Appnable rather than implement these solutions independently... A potential client could read the article, visit Microsoft's website and never return to Appnable."

**Rules:**
- Don't spend the blog explaining what a vendor's own documentation already explains (how to build a Power Automate approval flow, how Copilot summarises email). Acknowledge it in a sentence, link to it if useful, and move on.
- Spend the space on what the documentation doesn't cover: which processes are worth automating, permissions and data exposure, systems outside Microsoft 365, exception handling, ownership, audit and compliance in regulated sectors.
- Include a section on **where doing it yourself stalls** (specific, honest failure points) before the selling section, so the selling section answers a problem the reader now recognises.
- The selling section must show **what Appnable adds** that the reader can't get from the docs: process review first, measured accuracy, real software where the platform stops, integration with existing systems, and **proof** from published case studies.
- Test before delivery: *if a reader finished this blog and went to Microsoft's (or any vendor's) site instead of contacting Appnable, would they have lost anything?* If not, rewrite.

### 2. Call to action tied to a tangible business outcome

The reviewer's model CTA (H2 heading, then the paragraph, then the CTA link):

> **Ready to get more value from Microsoft 365?**
> Your organisation may already have the tools needed to eliminate repetitive tasks, improve document workflows and reduce administrative overhead. At Appnable, we help businesses identify automation opportunities, design secure workflows and integrate Microsoft 365 with their existing systems. Whether you're exploring your first automation project or looking to modernise complex processes, our team can help you identify where automation could deliver the greatest value.
> Contact Appnable to discuss your automation opportunities.

**Rules:**
- Use this structure for the conclusion: a question heading naming the value ("Ready to get more value from [topic]?"), what the reader may already have, what Appnable does about it, who it's for, then one CTA naming the outcome ("Contact Appnable to discuss your [topic] opportunities", linked to https://www.appnable.com/contact/).
- Adapt the wording to each topic rather than pasting it, keeping it within 60–100 words. This approved model is exempt from the rule-of-three check, but adapted versions should vary the rhythm.
- The conclusion H2 can be the question heading instead of "Final thoughts".

### 3. Show the story visually

> "Visual elements to tell the story of what you are trying to communicate always help. A simple workflow illustration showing Trigger – automation action – approval/validation – business outcome is often more engaging."

**Rules:**
- Every automation or process blog includes a **workflow illustration**: Trigger → Automation action → Approval / validation → Business outcome, filled in with one concrete example from the blog (e.g. signed engagement letter → filed and details extracted → risk team checks → matter opens same day, logged for audit).
- Make it with `scripts/workflow_diagram.py` (a simple diagram drawn for the article, not an AI image), under 200 KB, with a caption and alt text. Follow it with four short bullets explaining each step.
- Other topics: include at least one visual that tells the story (a diagram, a before/after table, or a step graphic), from `image-sources.md` or drawn for the article.

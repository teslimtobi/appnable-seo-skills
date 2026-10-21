# Image rules and sources

**Never use AI-generated images.** Use only these free libraries, or simple diagrams drawn for the article (e.g. `scripts/workflow_diagram.py`), credited as "Illustration by Appnable". Suggest a cover image and any in-blog visuals with the exact search terms to use, and always record the cover image source.

## Stock photos

| Source | Best for | Licence | Search tips |
| --- | --- | --- | --- |
| [Unsplash](https://unsplash.com) | Modern offices, high-res hardware, server rooms, coding/screen setups | Unsplash Licence: free commercial and non-commercial use, no attribution required | "cloud computing", "server rack", "data architecture", "office dashboard" |
| [Pexels](https://www.pexels.com) | Clean corporate setups, digital workflows, modern laptops, tech collaboration | Pexels Licence: free commercial use, no attribution needed, modifications allowed | "automation", "workflow", "robotics", "cybersecurity" |
| [Pixabay](https://pixabay.com) | Abstract digital graphics, network diagrams, AI nodes, server illustrations | Pixabay Content Licence: free commercial use, no attribution | Filter by Vector graphics or Illustrations for technical concept diagrams |

## Vector and illustration libraries (good for automation and systems topics)

| Source | Highlights |
| --- | --- |
| [unDraw](https://undraw.co/illustrations) | Open-source SVG illustrations for tech products, dashboards and automated workflows. Set the colour to Appnable green **#A0C63F** on the site before downloading. |
| [ManyPixels](https://www.manypixels.co/gallery) | Free vector illustrations: modern tech, analytics, bot automation, cloud icons |
| [Streamline HQ](https://www.streamlinehq.com) | Free tiers for UI icons, micro-illustrations and workflow connectors |

Enterprise and automation topics often look sharper with clean vectors, isometric diagrams or system illustrations than with generic stock photography.

## What to write in each blog

In the header block:

```
Cover image: [short description] | Source: [Site] ([photographer/artist if shown]) | [direct image URL, or search URL with terms]
Cover image alt text: [describes what the image shows]
```

Plus, for each suggested in-blog visual: where it goes, search terms, source site, alt text.

If you can't confirm a specific image page, give the search URL and terms instead of inventing an image link. Remind the author to compress each image to under 200 KB (not high definition) and to avoid people-heavy photos that look like stock clichés (handshakes, people pointing at screens).

## If Claude can't reach the image sites

Claude's workspace can't download from Unsplash, Pexels or Pixabay directly. When a real image file is needed in the Word document:

1. Download the unDraw collection from GitHub (reachable from the workspace): `curl -sL -o undraw.zip https://codeload.github.com/balazser/undraw-svg-collection/zip/refs/heads/main` (unDraw illustrations, free to use with no attribution; collection under MIT licence).
2. Pick the illustration that matches the blog's story (e.g. `reviewed-docs.svg` for approvals and audit), replace `var(--primary-svg-color)` with Appnable green `#A0C63F`, and render it to a 1200 × 630 PNG on a light background (`#F3F4F0`) with `cairosvg` and Pillow. Compress to under 200 KB.
3. Credit it in the header block: `Source: unDraw by Katerina Limpitsouni (undraw.co), free to use with no attribution required`.
4. For a photo instead (Unsplash, Pexels, Pixabay), give the author the search link and terms; they download it and record the photographer.

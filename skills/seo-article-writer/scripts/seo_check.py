#!/usr/bin/env python3
"""Check an SEO article .docx against the house rules, and optionally split it
into humanizer-sized plain-text parts.

Usage:
  python seo_check.py article.docx --keyphrase "AI document automation"
  python seo_check.py article.docx --keyphrase "..." --chunks 1000 [--outdir parts/]

Counting rules:
  - The article runs from the first Heading 1 (the title) to the "References" heading.
  - Header lines above the title (Keyphrase:, Meta description:, domain) are ignored.
  - "Read also:" / "Also read:" lines are counted as links and excluded from word count.
"""
import argparse, os, re, sys
from docx import Document

READ_RE = re.compile(r'^\s*(also read|read also)\s*:', re.I)


def load(path):
    doc = Document(path)
    paras = []
    started = False
    for p in doc.paragraphs:
        text = p.text.strip()
        try:
            style = (p.style.name if p.style is not None else '') or ''
        except Exception:
            style = ''
        if not style and p._p.pPr is not None and p._p.pPr.pStyle is not None:
            style = p._p.pPr.pStyle.val or ''
        style = re.sub(r'heading\s*(\d)', r'heading \1', style.lower())
        level = 0
        m = re.search(r'heading (\d)', style)
        if m:
            level = int(m.group(1))
        if not started:
            if level == 1:
                started = True
            else:
                continue
        if level and text.lower().rstrip(':') == 'references':
            break
        if text:
            paras.append({'text': text, 'level': level, 'style': style})
    return paras


def count_phrase(text, phrase):
    return len(re.findall(re.escape(phrase), text, flags=re.I))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('docx')
    ap.add_argument('--keyphrase', required=True)
    ap.add_argument('--target', type=int, default=7)
    ap.add_argument('--words', type=int, default=1500)
    ap.add_argument('--chunks', type=int, default=0, help='max words per humanizer part')
    ap.add_argument('--outdir', default='.')
    a = ap.parse_args()

    paras = load(a.docx)
    if not paras:
        sys.exit('No Heading 1 title found; is the title styled as Heading 1?')

    kp = a.keyphrase
    title = paras[0]['text']
    body = [p for p in paras if not READ_RE.match(p['text'])]
    links = [p for p in paras if READ_RE.match(p['text'])]
    first_body = next((p['text'] for p in body[1:] if not p['level']), '')
    headings = [p for p in body[1:] if p['level'] >= 2]
    kp_headings = [h['text'] for h in headings if count_phrase(h['text'], kp)]
    total = sum(count_phrase(p['text'], kp) for p in body)
    words = sum(len(p['text'].split()) for p in body)

    ok = lambda b: 'OK ' if b else 'FIX'
    print(f'Article: {title}')
    print(f'[{ok(total == a.target)}] Keyphrase "{kp}" used {total} times (target {a.target})')
    print(f'[{ok(count_phrase(title, kp) > 0)}] Keyphrase in title')
    print(f'[{ok(count_phrase(first_body, kp) > 0)}] Keyphrase in first paragraph')
    print(f'[{ok(len(kp_headings) >= 2)}] Keyphrase in {len(kp_headings)} headings: {kp_headings}')
    print(f'[{ok(abs(words - a.words) <= a.words * 0.05)}] Word count {words} (target ~{a.words}, excl. links/references)')
    print(f'[{ok(len(links) == 4)}] "Read also/Also read" links: {len(links)}')

    if a.chunks:
        os.makedirs(a.outdir, exist_ok=True)
        import math
        n = max(1, math.ceil(words / a.chunks))
        goal = words / n  # balance parts evenly, using as few as the limit allows
        parts, cur, cur_w = [], [], 0
        for p in body:
            w = len(p['text'].split())
            # break at a heading once the part nears its share, or before overflowing the limit
            if cur and ((p['level'] and cur_w >= goal * 0.85 and len(parts) < n - 1) or cur_w + w > a.chunks):
                parts.append(cur); cur, cur_w = [], 0
            cur.append(p); cur_w += w
        if cur:
            parts.append(cur)
        base = os.path.splitext(os.path.basename(a.docx))[0]
        for i, part in enumerate(parts, 1):
            text = '\n\n'.join(p['text'] for p in part)
            fn = os.path.join(a.outdir, f'{base}_part{i}.txt')
            open(fn, 'w').write(text)
            print(f'Part {i}: {len(text.split())} words, keyphrase x{count_phrase(text, kp)} -> {fn}')


if __name__ == '__main__':
    main()

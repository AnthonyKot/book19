#!/usr/bin/env python3
"""Rewrite every essay's prev/next nav in READING order (ORDER below). Ends link to Contents.
Idempotent. Book 19: numeric order for now; re-order after the virality scoring if wanted."""
import glob, os, re
ORDER = ["01", "02", "03", "04", "05", "06"]
root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
byno = {os.path.basename(f)[:2]: f for f in glob.glob(os.path.join(root, "chapters", "[0-9]*.html"))}
assert set(byno) == set(ORDER), (set(byno) ^ set(ORDER))
files = [byno[n] for n in ORDER]
for i, f in enumerate(files):
    prev = '<a href="%s">← Previous</a>' % os.path.basename(files[i-1]) if i > 0 else '<span></span>'
    nxt = '<a href="%s">Next →</a>' % os.path.basename(files[i+1]) if i+1 < len(files) else '<span></span>'
    nav = '<nav class="chapter-nav" aria-label="Essay navigation">\n  %s\n  <a href="../index.html">Contents</a>\n  %s\n</nav>' % (prev, nxt)
    s = open(f, encoding="utf-8").read()
    s2 = re.sub(r'<nav[^>]*class="chapter-nav"[^>]*>.*?</nav>', nav, s, flags=re.S)
    assert s2 != s or nav in s, ("nav block not found", f)
    if s2 != s: open(f, "w", encoding="utf-8").write(s2); print("  rewrote", os.path.basename(f))

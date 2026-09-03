#!/usr/bin/env bash
# Book 19 v0.1 — link check across the site (pages, not drafts). Gating.
set -u; cd "$(dirname "$0")"
python3 - <<'PY' || exit 1
import glob, os, re, sys
bad = 0
for f in [p for p in glob.glob('**/*.html', recursive=True) if not p.startswith(('drafts/', 'scripts/'))]:
    for m in re.findall(r'(?<![\w-])(?:href|src)="([^"#?:]+)"', open(f, encoding='utf-8').read()):
        if m.startswith(('http', '//', 'mailto')): continue
        t = os.path.normpath(os.path.join(os.path.dirname(f), m))
        if os.path.isdir(t): t = os.path.join(t, 'index.html')
        if not os.path.exists(t): print("  BROKEN  %s -> %s" % (f, m)); bad += 1
print("  %d broken link(s)" % bad); sys.exit(1 if bad else 0)
PY
echo PASS

#!/usr/bin/env bash
# Book 19 — standing verification. ./verify.sh [NN] [--strict]
#   link check across site pages (gating); checks/structure.py (essays); checks/claims.py (advisory unless --strict)
set -u; cd "$(dirname "$0")"
fail=0; FILTER=""; STRICT=""
for a in "$@"; do case "$a" in --strict) STRICT=1;; *) FILTER="$a";; esac; done
python3 - <<'PY' || fail=1
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
if ls chapters/[0-9]*.html >/dev/null 2>&1; then
  python3 checks/structure.py $FILTER || fail=1
  echo "== claims =="
  if [ -n "$STRICT" ]; then python3 checks/claims.py $FILTER || fail=1; else python3 checks/claims.py --advisory $FILTER; fi
fi
[ $fail = 0 ] && echo PASS || { echo FAIL; exit 1; }

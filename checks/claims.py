#!/usr/bin/env python3
"""Claims gate (ported from book17, 2026-09-03). Every <!-- CHECK: id --> in an essay has a row in
checks/claims/NN.tsv and vice versa; statuses must be `checked-by:<who>:<YYYY-MM-DD>`, `inference`
or `open`. Rows still carrying the legacy bare `verified` are reported as UNSTAMPED; `open` rows
are reported. Exit 1 on mismatch, unstamped or open (use --advisory to report only). Filter: NN."""
import glob, os, re, sys
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.join(here, "..")
args = sys.argv[1:]; advisory = "--advisory" in args
flt = next((a for a in args if re.fullmatch(r"\d\d", a)), None)
rows = {}
for tsv in sorted(glob.glob(os.path.join(here, "claims", "*.tsv"))):
    if flt and not os.path.basename(tsv).startswith(flt): continue
    for line in open(tsv, encoding="utf-8"):
        if not line.strip() or line.startswith("#") or line.startswith("id\t"): continue
        f = line.rstrip("\n").split("\t")
        if len(f) < 5: print("  MALFORMED  %s: %s" % (os.path.basename(tsv), line[:60])); continue
        if f[0] in rows: print("  DUPLICATE  %s" % f[0])
        rows[f[0]] = f
markers = {}
for path in sorted(glob.glob(os.path.join(root, "chapters", "*.html"))):
    b = os.path.basename(path)
    if b.startswith("_") or (flt and not b.startswith(flt)): continue
    for m in re.findall(r"<!--\s*CHECK:\s*([A-Za-z0-9_.-]+)", open(path, encoding="utf-8").read()):
        markers.setdefault(m, []).append(b)
bad = 0
for m in sorted(set(markers) - set(rows)): print("  NO ROW     %s  (%s)" % (m, ", ".join(markers[m]))); bad += 1
for r in sorted(set(rows) - set(markers)): print("  NO MARKER  %s" % r); bad += 1
unst = [k for k, f in rows.items() if f[4].strip() == "verified"]
opens = [k for k, f in rows.items() if f[4].strip() == "open"]
badst = [k for k, f in rows.items() if not (f[4].strip() in ("verified", "inference", "open") or re.fullmatch(r"checked-by:[^:]+:\d{4}-\d{2}-\d{2}", f[4].strip()))]
for k in badst: print("  BAD STATUS %s  %r" % (k, rows[k][4]))
for k in sorted(opens): print("  OPEN       %s  %s" % (k, rows[k][1][:60]))
if unst: print("  UNSTAMPED  %d row(s) still 'verified' without verifier/date: %s" % (len(unst), ", ".join(sorted(unst)[:6]) + (" …" if len(unst) > 6 else "")))
print("  %d marker(s), %d row(s), %d mismatch(es), %d unstamped, %d open" % (len(markers), len(rows), bad, len(unst), len(opens)))
sys.exit(0 if advisory else (1 if (bad or unst or opens or badst) else 0))

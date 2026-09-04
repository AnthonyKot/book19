#!/usr/bin/env bash
# scripts/revise-codex.sh NN — sol-only revision pass from drafts/NN.revise.brief.md; retries on capacity.
set -uo pipefail
cd "$(dirname "$0")/.."
n="${1:?essay number}"; brief="drafts/$n.revise.brief.md"; log="drafts/$n.codex-revise.log"
for attempt in 1 2 3 4 5 6; do
  echo "=== revise attempt $attempt gpt-5.6-sol $(date +%H:%M)" >> "$log"
  codex exec --skip-git-repo-check -m gpt-5.6-sol -s danger-full-access -C "$(pwd)" "$(cat "$brief")" < /dev/null >> "$log" 2>&1
  grep -q "at capacity" <(tail -n 5 "$log") || break
  sleep 180
done
[ -f "drafts/reviews/$n-applied.md" ] && echo "revise $n complete" >> "$log" || echo "revise $n ended without applied log" >> "$log"

#!/usr/bin/env bash
# Usage: scripts/ideate.sh <slug> "<seed text>"   — runs the ideation metaprompt as a one-shot Claude call.
# The seed is the only thing that changes between runs; the shape stays fixed in the metaprompt.
set -eu; cd "$(dirname "$0")/.."
slug="$1"; seed="$2"; mkdir -p "drafts/ideation/$slug/sources"
prompt=$(sed -e "s|{{SEED}}|$seed|" -e "s|{{SLUG}}|$slug|" scripts/prompts/idea-metaprompt.md)
claude -p --dangerously-skip-permissions "$prompt"

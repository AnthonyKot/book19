# The Third Engine (Book 19) — v0.1

Income outside software for the Book 18 reader: a forty-year-old enterprise developer in the Netherlands
with A2 Dutch, English/Russian/Polish, ~EUR 100k, regulatory literacy and an engineering habit, looking at 2030.

**v0.1 is the research phase in public.** No essays yet. The site has the method, the reader's edge
inventory, thirteen agent-written research memos with their saved sources, and two triages to nine candidates.

- `index.html` — candidates under test and the memo list. `about.html` — method, gates, honesty rules.
- `research/<slug>/index.html` — rendered memos; `research/<slug>/sources/` — the excerpts they rely on.
- `drafts/research/<slug>/` — the memos' working folders (brief, findings.md, sources). `drafts/notes/` —
  the editor's notes and triage. `drafts/reviews/` — the crowdfunding runs.
- `scripts/render.py` renders memos into the site; `./verify.sh` checks links. `CONTEXT.md` — decision record.

Same pattern as the eighteen books before it: static HTML, a decision record, checks that fail the build.

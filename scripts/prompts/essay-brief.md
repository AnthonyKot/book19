# Drafting brief — Book 19 essay {{NN}} ({{FILE}})

You are drafting one essay for *The Third Engine* (`/home/diablo/book19`): income outside software
for an experienced developer in the Netherlands. Work only inside that directory, except that you
read `/home/diablo/book18/chapters/01-connected-product-operations.html` and
`/home/diablo/book18/chapters/04-asset-intelligence.html` as finished examples of tone, HTML
skeleton, economics table and reading list, and `/home/diablo/book18/checks/claims/06.tsv` plus
`/home/diablo/book18/resources/sources/06/SOURCES.md` as format examples.

Read, in order: `CONTEXT.md` (all; your contract is in section 6), `AGENT.md`, `TEMPLATE.md`,
`drafts/edge-inventory.md`, your pitch `{{PITCH}}`, and the memos the pitch cites (under
`drafts/research/`, `drafts/ideation/`, `drafts/notes/`), including their saved excerpts, which you
may reuse by copying the excerpt file into your own `excerpts/` folder with its provenance line.

## Files you own (create; never touch anything else; do not run git)

- `chapters/{{FILE}}` — the essay. Copy the exact skeleton of book 18's chapter 01, with the brand
  changed to "The Third <span>Engine</span>", the kicker "Essay {{N}} of 6 · <candidate name> · from
  pitch {{P}}", and one extra section `section.whyyou` between `changed` and `sale` (see TEMPLATE.md).
  Leave the chapter-nav as `<span></span>` / Contents / `<span></span>`.
- `checks/claims/{{NN}}.tsv` — `id	claim	source_url	source_locator	status`, ids `{{NN}}-slug`,
  status `checked-by:codex:2026-09-05` / `inference` / `open`. Ship with zero `open`.
- `resources/sources/{{NN}}/SOURCES.md` and `resources/sources/{{NN}}/excerpts/<slug>.txt` — one
  excerpt per checked row: URL, fetch date, verbatim passage. A checked row without an excerpt is
  not checked.
- `drafts/{{NN}}.notes.md` — optional.

## What the essay must do

Follow the contract, AGENT.md's priority stack and pre-ship test, and TEMPLATE.md's eleven beats.
2,400–3,600 visible words; lede ≤130 words; one exact verdict string from CONTEXT section 7 in
`div.verdict-box` with the single assumption that would most change it. The "Why you" section
must answer the Dutch-language gate for this exact channel honestly and name the precedent firm
with its independent trace. Settle the pitch's "number to settle first" and test its kill fact
from sources; where the record cannot, say so in the essay. Research live with WebSearch and
WebFetch; primary sources first; enacted separated from proposed; no numbers from memory. Every
price in the economics section is a labelled hurdle unless it has its own checked row. The
ninety-day plan runs alongside a day job with at most EUR 5,000 pre-evidence spend.

Voice: plain, adult, analytical. Paragraphs under 150 words, sentences under 40.

## Before you finish

Run `python3 checks/structure.py {{NN}}` and `python3 checks/claims.py {{NN}}` from
`/home/diablo/book19` until both pass. Reply in at most 200 words: the checker lines, the verdict,
checked / inference row counts, excerpt count, and anything the contract asked for that the record
could not settle.

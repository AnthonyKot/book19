# Review and additions pass — ideation results for one seed (book 19)

First read `/home/diablo/book19/scripts/prompts/idea-metaprompt.md` in full: it defines the eight-part
shape, including part 8, the precedent, which the ideation run did not have. Then read
`/home/diablo/book19/drafts/edge-inventory.md`, the two triage notes under `drafts/notes/`, and the file
under review: `/home/diablo/book19/drafts/ideation/{{SLUG}}/ideas.md` with its `sources/`.

Your job, for the seed "{{SLUG}}":

1. **Precedent test.** For every kept idea, find the real, named small firm elsewhere (US, China,
   Germany, Poland, UK; not the Netherlands) that already earns its living on this shape. Firm's own
   site plus one independent trace. Save each as `sources/precedent-<id>.txt` with URL, publisher,
   fetch date 2026-09-04, and the lines that matter (what it sells, to whom, price if stated, size, age).
   No precedent found after a fair search: say so and downgrade the idea to WATCH; never invent one.
2. **Verify what the run marked unverified.** Every date, threshold or price marked "from knowledge,
   unverified" gets one attempt. EUR-Lex often refuses fetches: use the Official Journal PDF links,
   the Commission's policy pages, Rijksoverheid, RVO, NEN, or a trade-body summary, and save the
   excerpt. Record what stayed unverified.
3. **Re-screen** each idea against all eight parts. Keep, downgrade to WATCH, or cut, with the part
   that decided it.
4. **Additions.** Up to two new ideas, precedent-led: a firm you found elsewhere that has no Dutch
   equivalent and fits all eight parts for this reader, inside this seed. {{EXTRA}}
5. Budget: at most twenty-five fetches. Save every fetched page. Do not run git. Write
   `/home/diablo/book19/drafts/ideation/{{SLUG}}/ideas-reviewed.md` incrementally: per idea, the eight
   parts with verified/estimate marks and the precedent paragraph; the verdicts table; the additions;
   ≤120 honest words on what the precedent test changed.

Final reply ≤200 words: verdicts in one line each, the precedents found, and the one idea you would fund.

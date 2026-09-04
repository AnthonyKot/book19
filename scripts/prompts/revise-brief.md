# Revision brief — Book 19 essay {{NN}} (apply the panel review)

Essay {{NN}} of `/home/diablo/book19` (`chapters/{{FILE}}`, `checks/claims/{{NN}}.tsv`,
`resources/sources/{{NN}}/`) has been panel-reviewed. The consolidated review is
`drafts/reviews/{{NN}}-codex.md`; the two underlying reports are `drafts/reviews/{{NN}}-flash.md`
and `{{NN}}-pro.md` (the consolidator already adjudicated them; where it rejected a reviewer's
suggestion, leave that alone).

Work only inside `/home/diablo/book19` and only in the essay-{{NN}} files plus
`drafts/reviews/{{NN}}-applied.md`. Do not touch other essays, `CONTEXT.md`, `index.html`,
`AGENT.md`, `README.md`. Do not run git. All rules in `AGENT.md`, `TEMPLATE.md` and
`scripts/prompts/essay-brief.md` bind: the contract in CONTEXT §6, the reader's confirmed
constraints, the priority stack, the pre-ship test, the eleven beats including `section.whyyou`,
the claims schema with saved excerpts, word bounds 2,400–3,600, sentences under 40 words.

Apply every finding in the consolidated review, in rank order. For each: fix it, or reject it
with a reason grounded in a saved excerpt. A finding that a claim is unsupported is fixed by
weakening the claim to what the source says, or by fetching the source and saving the excerpt,
never by deleting the marker. Every figure in the economics stays a design hurdle unless it has
its own checked row. If a finding would change the verdict, apply the verdict the evidence
supports and say so in the applied log. Status for rows whose source you actually read:
`checked-by:codex:{{DATE}}`.

Then run `python3 checks/structure.py {{NN}}` and `python3 checks/claims.py {{NN}}` until both
pass, walk AGENT.md's pre-ship test, and write `drafts/reviews/{{NN}}-applied.md`: one numbered
entry per finding saying what changed or why it was rejected.

Reply in at most 200 words: checker lines, verdict (changed or not, and why), checked /
inference counts, anything left unresolved.

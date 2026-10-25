# Proving run A-005 — DESIGN.md in the new format, shelf consulted, lint clean

Run: 2026-10-24. Subject: Linkstash (~/workspace/linkstash), a real
project whose live DESIGN.md is the old prose format. Artifact in this
folder: `DESIGN.md`, the same system re-drafted in the suite's new
registry format. The project's own file was not overwritten; adoption
in the project repo is the owner's call.

## Criterion (from the A-005 record)

"a real project's DESIGN.md drafted with the shelf consulted and
written in the new format, linted clean."

## Shelf consultation

Per the shelf's load discipline (index first, at most one or two
files): `linear.app/DESIGN.md` was read. What was actually taken:
principles, not tokens — a single chromatic accent with a contracted
meaning, hairline borders doing the separation work shadows usually
do, and a product canvas that reads as a tool. Linkstash is light
where Linear is near-black, so no token values crossed over; the
consultation is recorded here because the format demands honesty
about it, and the Known Gaps section of the draft says the same.

## Evidence

- Registry parses as YAML; all 15 `{token.refs}` in component
  bindings resolve; 10 colours, 4 type scales, 4 radii, 6 spacing
  tokens, 6 components.
- `npx @google/design.md lint DESIGN.md` final result: **0 errors,
  0 warnings** (1 info token-summary). First pass had 4 errors
  (`letterSpacing: "0"` is not a valid dimension; needs `0px`) and 4
  warnings (orphaned danger/on-danger/surface-raised, missing
  `primary`). Fixes were substantive, not cosmetic: the delete
  confirmation became a real `button-danger` registry entry, the
  unused `surface-raised` was deleted rather than decorated, and the
  letterSpacing values were corrected.
- Contrast pairs computed with `scripts/contrast-check.py` (the
  A-006 script, doing double duty): ink/paper 15.5:1, ink-muted/paper
  6.2:1, on-accent/accent 4.9:1, danger/surface 6.5:1 — all PASS AA.
  The draft's accessibility section carries these computed numbers;
  the first draft's hand-estimated numbers were wrong in all four
  cases and were replaced, which is itself the argument for the
  registry-plus-tooling format.

## Findings written back

1. The linter expects a `primary` colour; the suite template names
   the role `accent`. The draft defines both with one value and
   records the mismatch in Known Gaps. The template should rule on
   this once (adapt-cycle material), or every project draft will
   improvise its own answer.
2. The suite template has no elevation registry section, so the one
   permitted shadow lives in prose only. Recorded in Known Gaps.
3. OKLCH-native projects (Linkstash's live tokens are OKLCH) need a
   conversion step into hex for this format; the conversion is
   mechanical but must be declared, which the draft's Exports
   section does.

## Verdict

Criterion met in full: real project, shelf consulted under its load
discipline, new format, lint clean with the fixes recorded. A-005 is
ready to promote EXPOSED → ADAPTED.

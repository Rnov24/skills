# Absorb report: Jakeschincariol/replica-skill

- Source: https://github.com/Jakeschincariol/replica-skill · Commit: 77c9436fb3d18c3d58169efb8caf4fe906b0dc51 · Licence: MIT (© 2026 Jake Schincariol) — text may be adapted with credit; tools vendored with credit headers
- Date: 2026-10-24 · Run by: orchestrator (gluttony run 8)

## Licence ruling (decided before any adaptation)

The repo carries an MIT licence. Text is adapted (rewritten into suite
conventions, credited in the skill footer and here), and the
standard-library tools are vendored into `scripts/` with a credit line
under the shebang. One local patch: `scripts/reviews.py`'s default
themes path now points at the vendored `scripts/reviews-themes.json`.

## Intake vetting

- Six Python tools (`parity.py`, `imgdiff.py`, `reviews.py`,
  `contrast.py`, `sweep.py`, `listing.py`): standard library only, no
  network calls, no subprocess, no credential access; file writes only
  to paths given via `--out`. Clean.
- No hooks, installers, or executable content beyond the tools and
  their test suite. Upstream tests run at intake: 57 tests, all pass.
- Nothing upstream was executed against any external system; the tools
  were run only on local sample files during validation.

## Inventory

| Unit | Purpose (theirs, one line) | Ships besides prose | Size |
|---|---|---|---|
| replica-recon | Reverse-engineer an app into screens, flows, inferred data model, feature matrix | recon-map.md template, features.csv template | 134 lines |
| replica-architect | Plan stack, schema, and API for a clone from the recon map | architecture.md template | 115 lines |
| replica-design | Rebuild a design system as tokens + component specs, with WCAG checker | tokens.json template, contrast.py (152 lines) | 99 lines |
| replica-build | Rebuild screen by screen from the recon map, ticking the feature matrix | — | 87 lines |
| replica-backend | Auth, database, Stripe payments, email, jobs, security checklist | — | 90 lines |
| replica-test | Test plan from recon flows, Playwright e2e, severity bug reports | test-plan.md, bug-report.md, e2e.example.spec.ts | 87 lines |
| replica-diff | Feature parity score + colour-blind layout screenshot diff | parity.py (228 lines), imgdiff.py (456 lines) | 93 lines |
| replica-entrepreneur | Mine real user reviews into ranked complaints, fix plan, positioning angle | reviews.py (311 lines), themes.json | 112 lines |
| replica-brand | Name and rebrand the clone; sweep for original leftovers | sweep.py (177 lines), brand templates | 110 lines |
| replica-launch | Landing page, pricing, store listing linted against store limits | listing.py (181 lines), listing.example.json | 100 lines |
| replica-deploy | Preflight-gated deploy on the user's own domain | preflight.md | 104 lines |

## Audit and verdicts

| Unit | Pros (mechanisms the suite lacks) | Cons / overlap ruling | Verdict |
|---|---|---|---|
| replica-recon | Product-level teardown the suite has no verb for: stable screen IDs (S##) and flow IDs (F##) with states, an inferred data model carrying evidence + confidence per entity, a weighted feature matrix as a parity contract, an explicit cannot-clone scoping step, honest S/M/L/XL sizing, and clean-room rules (public sources + own account only, no code/assets/private APIs) as a hard gate. `research` answers questions from sources; `study` extracts design DNA only. Neither produces a buildable product map. | Its output folder (`replica/`) is pack-specific; the suite registers the same outputs as RECON.md + FEATURES.csv artifacts instead. | ABSORB-NEW as `skills/recon/` (phase: discover) — the pack's core mechanism, on ground the suite does not cover. |
| replica-architect | One rule the suite states nowhere: hard invariants found in recon (double-booking) are database constraints, not UI checks; and schema work that inherits the inferred model's evidence/confidence instead of treating inference as fact. | The rest — stack default table, API-per-flow table, build order — duplicates `model` (ERD/API), `spec`, and `tickets`. A clone-only architecture skill would fork the model phase. | MERGE-INTO `model` — new "From a recon map" section (confidence carryover + invariant-as-constraint). Stack table and prose rejected. |
| replica-diff | Two tested, stdlib-only instruments: weighted parity scoring (must 3 / should 2 / could 1, partial = half, skip and added features excluded, missing must-haves = not shippable) and a colour-blind layout diff (edge maps per grid cell) designed so a deliberate rebrand does not pollute the score. `verify` demands evidence but owns no measuring instrument for parity claims. | A standalone diff skill would only ever run inside a recon project; as a `verify` section with vendored tools it serves any match-an-existing-product claim. | MERGE-INTO `verify` — new "Parity measurement" section; `parity.py` + `imgdiff.py` vendored to `scripts/`. |
| replica-entrepreneur | Review mining with the suite's own evidence ethics, made mechanical: never fabricate, every quote verbatim + linked (the tool drops link-less rows), sample size always stated, themes under 3 reviews or one source marked thin, low-rating/unmatched list surfaced for hand reading. The suite's `research` has citation discipline for documents but no review-corpus protocol or ranking tool. | Positioning/fix-plan output overlaps `define-product`; it lands as evidence inside the RESEARCH artifact feeding define-product, not as its own phase. | MERGE-INTO `research` — new "Review mining" section; `reviews.py` + themes vendored to `scripts/` (`reviews-themes.json`). |
| replica-brand | One checkable mechanism: the leftover sweep — the original's name (including inside identifiers), domains, and brand colours searched across contents and filenames, exit 1 blocks launch. Naming filters and the trademark screening table are sound but are advice, and palette/voice work is already owned by `design` (incl. the brand-systems reference shelf). | A brand skill would duplicate `design`; the sweep is the only part that is a gate rather than guidance. | MERGE-INTO `ship` — sweep added to the readiness list for rebuilt products; `sweep.py` vendored to `scripts/`. Naming/trademark/voice prose rejected as covered. |
| replica-design | "Measure, don't guess" token extraction from screenshots is good practice. | Duplicates `design` + `study` (design-DNA extraction already measures roles/scales from screenshots) and its `contrast.py` duplicates the suite's existing `scripts/contrast-check.py` (A-006). A second design-system skill violates the one-workflow rule. | REJECT — fully covered by existing skills and script. |
| replica-build | Per-screen definition-of-done and build log are tidy. | Duplicates `implement` (thin verifiable slices, ticket execution); its only clone-specific act — ticking FEATURES.csv — is already assigned to `implement` in the FEATURES.csv registry entry. | REJECT — covered by `implement`. |
| replica-backend | Sensible checklist (webhook idempotency, second-user authorization test, test-mode first). | A prose checklist with no artifact or gate of its own; auth rules per operation already live in `model`'s API conventions (incl. idempotency) and enforcement testing belongs to `verify`'s floor check. Absorbing it would create a second, weaker implement. | REJECT — generic checklist, mechanisms already owned. |
| replica-test | Edge-case enumeration per flow and fixed bug format are competent. | Duplicates `verify` (evidence gate) and `debug` (red-first fix loop); its severity taxonomy would fork `review`'s finding vocabulary. Playwright/axe specifics are tooling prose the suite deliberately keeps out of phase skills. | REJECT — covered by `verify` + `debug`. |
| replica-launch | Store-limit linting is mechanical and correct. | `listing.py` serves one narrow scenario (clone shipped to app stores); landing/pricing prose overlaps `define-product` and `design` copy references. The tool stays in the upstream repo for anyone who needs it. | REJECT — niche, tool-locked to the clone-to-store path. |
| replica-deploy | Preflight-as-gate matches suite instincts. | Duplicates `ship` end to end: readiness list, human grant before the irreversible step, user performs account/payment steps. DNS/email tables are reference prose, not mechanism. | REJECT — covered by `ship`. |

Counts: ABSORB-NEW ×1, MERGE ×4, REJECT ×6 of 11 units. All six Python
tools were vetted; four are vendored (`parity.py`, `imgdiff.py`,
`reviews.py`, `sweep.py`), two are not (`contrast.py` duplicates an
existing suite script, `listing.py` rejected with its unit).

## Integration performed

Prepared as a staged diff on 2026-10-24, pending human gate:

- `skills/recon/SKILL.md`: new 23rd suite skill (phase: discover),
  rewritten to suite shape — purpose, clean-room rules as gate, process,
  human gate, anti-patterns, upstream credit footer.
- `templates/recon.md` + `templates/features.csv`: the recon map and
  feature matrix as suite templates (features template generalised
  from the upstream booking-specific example).
- `docs/ARTIFACTS.md`: RECON.md and FEATURES.csv registered with
  triggers, owners, consumers, gates.
- `skills/model/SKILL.md`: "From a recon map" section (MERGE from
  replica-architect).
- `skills/verify/SKILL.md`: "Parity measurement" section (MERGE from
  replica-diff).
- `skills/research/SKILL.md`: "Review mining" section (MERGE from
  replica-entrepreneur).
- `skills/ship/SKILL.md`: leftover sweep added to readiness (MERGE
  from replica-brand).
- `scripts/parity.py`, `scripts/imgdiff.py`, `scripts/reviews.py`,
  `scripts/reviews-themes.json`, `scripts/sweep.py`: vendored (MIT,
  credit lines added; reviews.py default themes path repointed).
- `README.md`: `recon` added to the Discover-and-define skill list.
- `docs/ADAPTATIONS.md`: A-009 filed at EXPOSED.
- `docs/SYNTHESIS.md`: v1.14.0 lineage note.
- `VERSION`: bumped to 1.14.0.
- Index regenerated (`docs/SKILL_INDEX.md`, `skills-index.json`): 23 skills.

Validation: all SKILL.md frontmatter valid (name matches directory),
template references resolve, vendored tools smoke-tested (parity on the
template matrix, reviews on a sample corpus, sweep on the suite repo,
imgdiff self-check on generated PNGs), upstream test suite passed at
intake (57 tests).

## Review

- Fidelity axis: PASS. The absorbed mechanisms survive in substance —
  recon's inventory/matrix/clean-room protocol is complete, and the
  four vendored tools are byte-identical apart from the credit line
  (and reviews.py's themes path). Merged sections keep the upstream
  numbers and thresholds (weights, thin-theme rule, sweep exit code).
- Fit axis: PASS. One new skill on empty ground (discover had no
  product-teardown verb); four merges strengthen existing phases
  instead of forking them; six units rejected so the suite stays one
  workflow, not two — the replica pipeline remains expressible as
  recon → brief/define-product → model → design → implement → verify
  → ship inside the suite.
- Human gate: pending.

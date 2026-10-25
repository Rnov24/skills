# Adaptation log — the wheel

Every permanent change this suite makes to itself in response to observed
work is recorded here by the `adapt` skill: the phenomenon, the counter,
the expected effect, and the verdict of later runs. Rejected and reverted
adaptations stay in the log. The wheel remembers.

| ID | Filed | Phenomenon (short) | Counter (short) | Status |
|---|---|---|---|---|
| A-001 | 2026-10-21 | Suite was static after shipping; learning lived only in retros of other projects | Added the adaptation loop itself (`adapt` skill, this log, staged absorption in gluttony, finder-miss logging) | ADAPTED (v1.3.0) |
| A-002 | 2026-10-21 | Gluttony run on Nutlope/hallmark: suite design layer lacked a pattern library, a copy reference, mechanical slop gates, and any design-extraction verb | Absorbed hallmark's macrostructure + pruned component libraries, slop gates, state/motion canon, OKLCH/responsive foundations, token exports, copy reference, and the study skill (audit: docs/audit/absorbed/2026-10-21-hallmark.md) | ADAPTED (v1.8.0, promoted 2026-10-22 by the Kopi Pesisir proving run, docs/proving-runs/2026-10-22-a002/) |
| A-003 | 2026-10-21 | Gluttony run on NTCoding/claude-skillz (data-visualization): the suite had no chart discipline at all while the owner's work is full of dashboards and research figures | Absorbed as new `data-viz` skill, fully rewritten (source repo has no licence, so mechanisms only, no text) with DESIGN.md token rule and accessibility gate added (audit: docs/audit/absorbed/2026-10-21-claude-skillz-dataviz.md) | ADAPTED (v1.8.0, promoted 2026-10-22 by the Iris figure proving run, docs/proving-runs/2026-10-22-a003/) |
| A-004 | 2026-10-22 | Gluttony run on a pasted 20-law UX instruction set: ux-heuristics.md specified mechanics (targets, states, input geometry) but never the decision laws behind them — no choice budget, convention, grouping, default-safety, or completion-state rules | 16 of 20 laws merged into ux-heuristics.md as checkable rules (new "Choice, grouping, and convention" section plus additions to Forms, Feedback, and Lists); 4 rejected as already covered (Fitts size, Zeigarnik, Prägnanz, Tesler) (audit: docs/audit/absorbed/2026-10-22-ux-laws.md) | ADAPTED (v1.9.0, promoted 2026-10-22 by the two-target audit proving run, docs/proving-runs/2026-10-22-a004/) |
| A-005 | 2026-10-23 | Gluttony run on VoltAgent/awesome-design-md (84 brand DESIGN.md extractions): design work had no full-depth DESIGN.md examples to consult, and the suite's own DESIGN.md format was prose-only where the reference corpus is machine-readable | Owner's gate ruling: taken as a DESIGN.md reference, not digested — all 84 files vendored verbatim as the `references/brand-systems/` shelf (INDEX + provenance + quality caveats), and templates/design.md adopts the corpus format (frontmatter token registry, lint gate, Known Gaps, Responsive, font substitutes); the prepared rule/archetype merges were withdrawn and stay recorded in the audit for future adapt cycles (audit: docs/audit/absorbed/2026-10-23-awesome-design-md.md) | ADAPTED (v1.15.0, promoted 2026-10-24 by the Linkstash DESIGN.md proving run, docs/proving-runs/2026-10-24-a005/) |
| A-006 | 2026-10-23 | Gluttony run on miqdadbadjuber/anti-slop: a second anti-slop system whose core duplicates the suite's taste core almost entirely, but whose satellites held six mechanisms the suite lacked — dead-control discipline beyond form submits, a recorded click-through as review evidence, a body-of-copy tell set with false-positive discipline, three accessibility specifics (non-text contrast, keyboard occlusion, Escape), a comment-value test for the build phase, and a working contrast calculator for arbitrary pairs | Merged as fragments only: 1 checkbox into taste-core.md + 1 into review-rubric.md + the FAQ/self-audit/body-tells/what-not-to-flag set into copy.md, 3 rules + reference table into ux-heuristics.md, a Comments section into implement, and the contrast checker adapted to scripts/contrast-check.py (selftest repointed at the ux-heuristics table); core, ui, layoutmobile units, the mode/install machinery, the tier taxonomy, the Liveliness dials, and the MCP wrapper rejected (audit: docs/audit/absorbed/2026-10-23-anti-slop.md) | ADAPTED (v1.15.0, promoted 2026-10-24 by the Linkstash copy-pass proving run, docs/proving-runs/2026-10-24-a006/) |

| A-007 | 2026-10-23 | Gluttony run on anthropics/skills frontend-design: five AI default clusters, a two-pass uniqueness check, and the Chanel restraint principle duplicated design's taste layer as a standalone prompt but held checkable mechanisms the suite lacked | Merged as mechanisms only into design (two-pass review in the preview block, cluster rules in taste-core, default bans in templates/design.md); standalone skill rejected (audit: docs/audit/absorbed/2026-10-23-anthropic-frontend-design.md) | ADAPTED (v1.15.0, promoted 2026-10-24 by the Linkstash landing-page preview proving run, docs/proving-runs/2026-10-24-a007/) |
| A-008 | 2026-10-23 | Gluttony run on anthropics/skills mcp-builder + webapp-testing: the suite had no MCP authoring/evaluation discipline and no deterministic local-server test runner | mcp-builder absorbed as new skill (phase: build) with vendored references and evaluation harness; webapp-testing rejected as prose, its with_server.py merged into scripts/with-server.py (audit: docs/audit/absorbed/2026-10-23-anthropic-mcp-and-testing.md) | ADAPTED (v1.15.0, promoted 2026-10-24 by the MCP server + with-server proving run, docs/proving-runs/2026-10-24-a008/) |
| A-010 | 2026-10-25 | Fix-first tidy-up at the owner's instruction: every runtime tool the suite's skills quote lived in repo-root scripts/, which the installer never copies, so all installed copies carried dangling references; no install-time validation existed to catch it | Moved the 7 runtime tools into their owning skills' scripts/ folders (mcp-builder precedent); installer now regenerates the index, validates frontmatter/script refs/compilation pre-install, verifies copies post-install, validates the staged agy plugin, and gains --check; templates/design.md rules primary=accent alias and gains an elevation section | ADAPTED (v1.15.1, promoted 2026-10-25 — repair, proved by --check before/after) |
| A-011 | 2026-10-26 | Gluttony run on google/elephant-goldfish-model (EGM): brainstorm and draft held mechanisms the suite lacked — mandatory alternatives with rejection reasons, an every-file implementation list, a fresh-session bar for specs, a six-lens parallel swarm, critique-first with counter-arguments, a readiness gate, and a synthesizer step for parallel findings — but as standalone skills they duplicate brief/grill and spec | Batch 1 merges only: alternatives + file list + no-code + fresh-session/Heilmeier bar into spec (template gains Alternatives and Detailed implementation sections), lens swarm + critique-first + readiness gate into grill, synthesizer step into orchestrate, readiness rule into brief; banned-word lists, RFC/SITEMAP steps, per-section approval gates, save-location gate, and silent no-code enforcement rejected (audit: docs/audit/absorbed/2026-10-26-elephant-goldfish-model.md) | EXPOSED (staged for v1.16.0; batches 1+2 adapted, combined diff at human gate) |
| A-009 | 2026-10-24 | Gluttony run on Jakeschincariol/replica-skill (11 clone-building skills): the suite had no product-teardown verb (research answers questions, study extracts design DNA, neither maps an existing product into screens/flows/inferred model/feature matrix), no parity instrument for match-an-existing-product claims, no review-mining protocol, and no leftover-identity check before shipping a rebuild | `replica-recon` absorbed as new `recon` skill (phase: discover) with RECON.md + FEATURES.csv artifacts registered; merges: replica-architect → `model` (confidence carryover, invariant-as-DB-constraint), replica-diff → `verify` (parity section + vendored parity.py/imgdiff.py), replica-entrepreneur → `research` (review-mining section + vendored reviews.py/themes), replica-brand → `ship` (sweep gate + vendored sweep.py); 6 units rejected as duplicates of design/study, implement, verify/debug, ship (audit: docs/audit/absorbed/2026-10-24-replica-skill.md) | ADAPTED (v1.15.0, promoted 2026-10-24 by the Linktree recon proving run, docs/proving-runs/2026-10-24-a009/) |

Full candidate records are appended below the table as they are filed.

## A-001: the adaptation loop

- Status: ADAPTED · Filed: 2026-10-21
- Source signal: repeated correction — the suite's owner kept extending the
  suite by hand (router hardening, installers, design references) because no
  mechanism existed to turn run experience into suite changes.
- Phenomenon: v1.0.0 and v1.1.0 shipped strong gates but no self-modification
  path; every improvement required an ad-hoc request.
- Counter: the `adapt` skill, this log, EXPOSED → ADAPTED staging for
  gluttony absorptions, and automatic routing-miss logging in the finder.
- Expected effect: suite changes after v1.3.0 cite an A-entry and evidence;
  improvements stop depending on the owner remembering to ask.
- Decision: approved by the owner on creation, 2026-10-21.

## A-002: hallmark absorption — proving run and promotion

- Status: ADAPTED · Filed: 2026-10-21 · Promoted: 2026-10-22 (v1.8.0)
- Source signal: absorption (gluttony run 1, Nutlope/hallmark) held at
  EXPOSED since v1.5.0 pending a proving run.

### Phenomenon
The design layer absorbed from hallmark (macrostructure and component
libraries, slop gates, eight-state canon, OKLCH/responsive foundations,
copy reference, study skill) had never been exercised as one system in a
single run. Its individual gates were audited on paper only.

### Counter
No suite text changed at absorption time. The proving run itself is the
counter-evidence: two contrast briefs in
`docs/proving-runs/2026-10-22-a002/`, chosen to stress the mechanisms'
failure modes rather than flatter them.

### Proving pair 1 — full page
- Brief (verbatim in `brief-page.md` in the run folder): a one-page
  landing page for a fictional Cirebon coffee roastery that must show a
  testimonial section and a product catalogue, while no product photos,
  no real testimonials, and no sales numbers exist, stock and generated
  imagery are banned, the budget is zero, and the page must hold at
  320px with exactly one accent colour.
- Reasoning trace: preserved in `reasoning-trace.md` in the run folder —
  pre-flight (fresh project, nothing to preserve, the system-stack
  exception recorded with its reason), the preview block, and the
  rotation pick. Pick: 11 Catalogue. Stat-Led was rejected because no
  real metric exists and its index entry forbids invented numbers;
  Quote-Led was rejected because no real quote exists; Photographic and
  Bento were also rejected with stated reasons.
- Output: `index.html` + `style.css` in the run folder, with the
  orchestrator's own renders saved beside them (render-page-1280.png,
  render-page-320.png).

### Proving pair 2 — component scope
- Brief (verbatim in `brief-component.md`): one standalone registration
  form component, all user states shown.
- Output: `form-states.html` + `form.css` in the run folder (render in
  render-form-1280.png). Component-scope mode fired and the page
  machinery stood down in writing; the forced-state preview renders the
  eight-state contract's own list in its own order.

### Findings writeback
Full review in `review.md` in the run folder. One rework fix: the
resting form-control border measured 2.85:1 against the 3:1
UI-component floor and was darkened to 3.62:1 — the rule this confirms
is that the contrast gate covers component boundaries, not only text,
and an OKLCH lightness-gap screen is not a substitute for computing
floored pairs. Two interpretations were recorded rather than reworked:
the error slot's stable *minimum* height holds even when a wrapped
three-part message grows the field, and a brief-forced, pre-recorded
font exception is a decision, not a drift.

### Expected effect (as filed at absorption, now checked)
Design runs pick a named macrostructure with rejected alternatives on
record, refuse invented proof at the gate, and ship checkable state and
geometry discipline for components. The proving run did all three under
briefs designed to tempt the opposite.

### Blast radius
Promotion changes no skill text; it changes the trust level of the
design shelf. If a later real-project run shows the mechanisms failing
in a framework codebase (this run was standalone HTML/CSS), the pair
rots per the adapt skill and A-002 returns to EXPOSED until re-proven.

### Decision
Proving run ordered by the owner on 2026-10-22 ("jalankan proving run
buat promosi A-002/A-003"). Orchestrator review verdicts: spec PASS,
quality PASS after one rework round. Promoted to ADAPTED by the
orchestrator under that order, v1.8.0.

## A-003: data-viz absorption — proving run and promotion

- Status: ADAPTED · Filed: 2026-10-21 · Promoted: 2026-10-22 (v1.8.0)
- Source signal: absorption (gluttony run 2, NTCoding/claude-skillz
  data-visualization) held at EXPOSED since v1.6.0 pending a proving run.

### Phenomenon
The suite's chart discipline (perceptual encoding order, chart selection
by question, colour and accessibility gates, annotation rules) had never
been run against real computed data with traps present.

### Counter
No suite text changed at absorption time. The proving run in
`docs/proving-runs/2026-10-22-a003/` is the counter-evidence.

### Proving pair
- Brief (verbatim in `brief.md` in the run folder): a figure set for an
  Iris classification lab report (150 rows, 3 species, a nominal species
  column encoded as integers, cleaning defects in single digits next to
  the 150-row total, four model accuracies claimed to cluster at
  92–99%), readable by colour-blind readers, in print and on screen,
  with pie charts, rainbow ramps, and truncated bar axes banned.
- Reasoning trace: the five questions answered per figure in
  `summary.md` in the run folder, with the explicit refusal to compute
  any correlation against the nominal `Species_Encoded` column and its
  reason (the integers are arbitrary labels; a coefficient would
  measure the coding, not the data).
- Output: `make_figures.py` (seed 42, loads the dataset at runtime) and
  four 300 dpi figures in the run folder — scatter with colour plus
  distinct markers, box-plus-strip distribution, split-panel cleaning
  counts, and an accuracy dot plot — plus per-figure data tables and
  the full plotted data in `figures-data.csv`.

### Findings writeback
Full review in `review.md` in the run folder. The orchestrator re-ran
the script and got byte-identical figures and identical numbers before
its fix (150 rows, 1 duplicate, 0 missing; accuracies 93.33, 97.78,
95.56, 91.11). One rework fix: the cleaning panel's automatic ticks
landed on 0.25 steps for count data; the panel now takes integer ticks
only — the rule confirmed is that count axes take integer ticks. The
brief disagreed with the data twice (Random Forest 91.11% sits below
the claimed band; missing values are 0), and both real values were
plotted and reported unchanged, which is the honesty behaviour the
skill exists to produce.

### Expected effect (as filed at absorption, now checked)
Figure work in this suite chooses encodings by perceptual accuracy,
never lets colour carry information alone, and refuses encodings that
lie (truncated bars, nominal correlations, crushed scales). The
proving run exercised each of those under a brief that tempted all of
them, and held.

### Blast radius
Promotion changes no skill text beyond the status line in
skills/data-viz/SKILL.md. The proof covers matplotlib research
figures; product-dashboard rendering (SVG/Canvas thresholds) remains
proven only on paper, and a future dashboard run that breaks those
rules re-opens this entry.

### Decision
Proving run ordered by the owner on 2026-10-22 (same order as A-002).
Orchestrator review verdicts: spec PASS, quality PASS after one rework
round. Promoted to ADAPTED by the orchestrator under that order,
v1.8.0.

## A-004: UX-law rules — proving run and promotion

- Status: ADAPTED · Filed: 2026-10-22 · Promoted: 2026-10-22 (v1.9.0)
- Source signal: absorption (gluttony run 3, pasted 20-law UX
  instruction set) held at EXPOSED since v1.7.0 pending a proving run.

### Phenomenon
The 18 decision-law checkboxes merged into ux-heuristics.md had never
been applied to a real interface. Rules that cannot be applied
consistently, or that catch nothing real, are decoration in checklist
form.

### Counter
No suite text changed. The proving run in
`docs/proving-runs/2026-10-22-a004/` is the counter-evidence: an audit
of the 18 rules against two of the owner's real products, chosen as a
contrast pair — the NetAcad AI Assistant extension popup (a dense
settings-and-actions surface) and the EXAMIND login/register screens
(a focused auth flow, served from the owner's local build).

### Proving pair
- Brief: `brief.md` in the run folder — exactly the 18 rules in scope,
  one PASS/FAIL/NA verdict per rule per target, evidence labelled
  RENDER, DOM/HTML, or SOURCE with file:line, FAILs quoting the rule
  and naming the element, and an explicit warning that an
  unreproducible FAIL would be overturned as a false positive.
- Reasoning trace: the auditor's method and its six disclosed wording
  ambiguities are in `report.md` in the run folder; the renders it
  judged from are filed beside it (target-a-*.png, target-b-*.png).
- Output: `audit.md` in the run folder — 36 verdicts. Target A: 14
  PASS, 4 FAIL. Target B: 17 PASS, 1 FAIL. No NA on either target,
  with the two nearest NA candidates examined in writing.

### Findings writeback
Full review in `review.md` in the run folder. The orchestrator
re-derived all five FAILs from primary source evidence and all five
reproduce; three PASSes were spot-checked in source and also
reproduce; false positives: zero. The five FAILs are not scattered:
four sit in state communication over time (idle Pause/Stop that can
be pressed and manufacture state, a completion answered with a
present-tense "running" message that auto-clears, progress counters
the backend already returns and the popup never renders), and
Goal-Gradient failed on both products independently for the same
underlying reason. The auditor's six wording ambiguities (Serial
Position's scope, Doherty's "on the control itself", when a default
becomes a commitment, Peak-End's flow scope, Goal-Gradient on
conditional steps, Miller's screen-to-session mapping) are recorded
in the review as watched items: one exposure does not earn a rule
rewrite, and a second run tripping on the same wording is the signal
for a clarification candidate.

### Expected effect (as filed at absorption, now checked)
A reviewer judging a screen against ux-heuristics.md can reach
verdicts another reviewer reproduces, and the decision laws catch
real defects the mechanics-only checklist could not name. In this
run every FAIL survived independent re-verification and the tally
separated a dense, state-heavy surface (4 FAILs) from a disciplined
flow (1 FAIL).

### Blast radius
Promotion changes no rule text. The proof covers two surface genres
(extension settings popup, web auth flow); dashboard and in-exam
surfaces — where several of these laws bite harder — are unproven
ground for the ruleset, and a run there that produces false
positives re-opens this entry.

### Decision
Proving run ordered by the owner on 2026-10-22. Orchestrator review
verdicts: spec PASS, quality PASS, zero false positives. Promoted to
ADAPTED by the orchestrator under that order, v1.9.0. With this
promotion every gluttony absorption in the suite stands at ADAPTED;
the wheel's EXPOSED queue is empty.

## A-005: awesome-design-md as the DESIGN.md reference shelf

- Status: ADAPTED · Promoted: 2026-10-24 (v1.15.0) · Filed: 2026-10-23
- Promotion evidence: `docs/proving-runs/2026-10-24-a005/report.md`.
- Source signal: absorption (gluttony run 4, VoltAgent/awesome-design-md,
  MIT, commit 3b605329240ce735b510037cca322f1831fdd7f8).
- Phenomenon: the suite's design phase writes DESIGN.md constitutions but
  carried no worked examples of the artifact at full depth, while an
  84-file corpus of exactly that artifact existed upstream in a
  machine-readable format the suite's prose-only template did not speak.
- Counter (as ruled by the owner at the human gate, 2026-10-23: "ambil
  aja sebagai referensi design md"): the corpus is taken as a reference,
  not digested into rules. All 84 DESIGN.md files are vendored verbatim
  at `skills/design/references/brand-systems/` with an INDEX carrying
  load discipline, provenance, and quality caveats (3 files with broken
  YAML frontmatter, 10 legacy-format files, `ex-*` generator filler to
  skip, signature-copy cautions). The suite's own template adopts the
  corpus's format so references and constitutions speak the same
  language: frontmatter token registry as the single source (prose
  states roles, never restates values), the lint gate, Known Gaps,
  Responsive, and font-substitute lines. The mechanism merges prepared
  during the audit (taste-core and style-directions rules, the X1–X7
  component annex) were withdrawn under the same ruling; they remain
  fully recorded in the absorb report as candidates for future adapt
  cycles, and none of them is in force.
- Expected effect: when a brief names a brand direction, or a draft
  DESIGN.md needs a full-depth example, the design phase consults one or
  two named reference files instead of improvising from memory; new
  constitutions are written in the lintable registry format from the
  start.
- Blast radius: the shelf is reference data behind an index, loaded on
  demand; it changes no rule in force. The template change is
  prospective — existing projects' DESIGN.md files are not migrated.
- Decision: owner's ruling at the gate, 2026-10-23. Promotion from
  EXPOSED requires a proving run: a real project's DESIGN.md drafted
  with the shelf consulted and written in the new format, linted clean.

## A-006: anti-slop absorption — fragments, not the system

- Status: ADAPTED · Promoted: 2026-10-24 (v1.15.0) · Filed: 2026-10-23
- Promotion evidence: `docs/proving-runs/2026-10-24-a006/report.md`.
- Source signal: absorption (gluttony run 5, miqdadbadjuber/anti-slop,
  MIT, commit c93d08c7c94ab6f4db9ccc2e0f4f6e6121006d3e).
- Phenomenon: the upstream core is a rival anti-slop constitution
  (C-1..C-5, R-01..R-38, a delivery gate) written to sit on top of a
  project's DESIGN.md — the exact seat the suite's taste core occupies
  since A-002. Audited rule by rule, 35 of its 38 rules duplicate suite
  coverage, usually in a weaker or prose form, and two conflict
  outright (its absolute em-dash ban against copy.md's prescribed
  em-dash use; its dark-mode toggle clause against the design skill's
  no-unasked-themes anti-pattern). The yield was in the satellites and
  the seams: six mechanisms the suite genuinely lacked.
- Counter: fragments, each landed where the suite already keeps that
  kind of rule — dead-control checkbox (taste-core), click-through
  evidence (review-rubric), copy tells + false-positive discipline
  (copy.md), non-text contrast / keyboard occlusion / Escape +
  unrounded-threshold discipline and the reference table
  (ux-heuristics), the comment-value test (implement), and the contrast
  calculator (scripts/contrast-check.py, adapted; its selftest now
  recomputes the table in ux-heuristics.md, so doc and tool cannot
  drift). The core, both remaining design satellites, the
  mode-resolution and install-wizard machinery, the three-tier rule
  taxonomy, the Liveliness dials, and the hand-rolled MCP wrapper were
  rejected with reasons in the audit.
- Expected effect: reviews catch dead controls with a recorded
  click-through instead of discovering them in use; copy audits flag
  clusters of tells without sanding off the user's voice; contrast
  claims about built UI are computed by a chainable script instead of
  estimated; comment slop is judged in the build phase by a named test.
- Blast radius: every merge is additive — one checkbox, one section, or
  one script at a time — and no rule in force changed meaning. The one
  contradiction found (em dashes) was resolved in the suite's favour
  and recorded. If a fragment proves noisy in real reviews (the
  what-not-to-flag discipline is the guard), the adapt loop revises it.
- Decision: staged at EXPOSED pending the owner's human gate on the
  absorb report; promotion requires a proving run that uses the
  fragments on real work — a design review run with the click-through
  check, or a copy pass audited against the new copy.md sections.

## A-007: Anthropic frontend-design absorption — principles and calibration merged into design

- Status: ADAPTED · Promoted: 2026-10-24 (v1.15.0) · Filed: 2026-10-23
- Promotion evidence: `docs/proving-runs/2026-10-24-a007/report.md`.
- Source signal: absorption (gluttony run 6, anthropics/skills target
  `skills/frontend-design`, Apache-2.0, commit dbd4588f9e1033efb41dad4bef2f7947c8993d44).
- Phenomenon: Anthropic's `frontend-design` provides a concise calibration
  cataloguing 5 concrete AI design default clusters (cream+terracotta,
  near-black+acid, broadsheet hairline, SaaS card kit, template chrome with
  middle dots and '→' buttons), a two-pass uniqueness check before code, and
  the Chanel single-boldness restraint principle. As a standalone skill it is a
  pure guidance prompt that would violate the suite's "one taste core" law; as
  extracted mechanisms it directly strengthens the design preview block and
  taste-core rulebook.
- Counter: merged mechanisms into `skills/design/SKILL.md` (two-pass uniqueness
  review in preview block; Chanel restraint in build discipline),
  `skills/design/references/taste-core.md` (checkable rules for template chrome,
  default AI clustering, and single-word headline accents), and
  `templates/design.md` (default bans list). Standalone skill rejected to
  preserve one workflow.
- Expected effect: preview blocks catch generic prompt defaults before code is
  written; review gates flag unmotivated template chrome and signature AI
  aesthetic tells mechanically.
- Blast radius: strictly additive checks on design artifacts and preview
  gates. No existing valid designs broken.
- Decision: staged at EXPOSED pending human gate on absorb report.

## A-008: Anthropic mcp-builder and with-server absorption (v1.13.0)

- Status: ADAPTED · Promoted: 2026-10-24 (v1.15.0) · Filed: 2026-10-23
- Promotion evidence: `docs/proving-runs/2026-10-24-a008/report.md`.
- Source signal: absorption (gluttony run 7, anthropics/skills targets
  `skills/mcp-builder` and `skills/webapp-testing`, Apache-2.0, commit dbd4588f9e1033efb41dad4bef2f7947c8993d44).
- Phenomenon: the suite lacked specialized discipline for building and
  evaluating Model Context Protocol (MCP) servers, tool discovery conventions,
  and behavioral annotations. In parallel, running test commands against local web
  servers lacked a clean lifecycle runner.
- Counter: `mcp-builder` absorbed as new skill in `phase: build` (4-phase protocol,
  naming conventions, Zod/Pydantic schemas, tool annotations, MCP Inspector
  verification, and 10-question evaluation harness) with vendored language references.
  `webapp-testing` rejected as standalone skill to prevent boilerplate bloat, but its
  underlying `with_server.py` helper merged into `scripts/with-server.py` for
  deterministic local test lifecycle execution.
- Expected effect: agents can author, lint, inspect, and evaluate MCP tool servers
  systematically; testing workflows can spin up background servers reliably.
- Blast radius: `mcp-builder` is an independent build-discipline skill; `scripts/with-server.py`
  is a standalone utility. Zero regression on existing skills.
- Decision: staged at EXPOSED pending human gate on absorb report.



## A-009: replica-skill absorption — recon skill, parity and review-mining instruments (v1.14.0)

- Status: ADAPTED · Promoted: 2026-10-24 (v1.15.0) · Filed: 2026-10-24
- Promotion evidence: `docs/proving-runs/2026-10-24-a009/report.md`.
- Source signal: absorption (gluttony run 8, Jakeschincariol/replica-skill,
  MIT, commit 77c9436fb3d18c3d58169efb8caf4fe906b0dc51).
- Phenomenon: an 11-skill pack for cloning apps end to end. Its pipeline
  mostly re-implements suite phases under clone names (architect ≈ model,
  build ≈ implement, test ≈ verify/debug, deploy ≈ ship, design ≈ design +
  study), but four mechanisms cover ground the suite lacked: product-level
  reverse engineering into a buildable map with a feature-matrix parity
  contract, weighted parity + colour-blind layout-diff instruments,
  verbatim-and-linked review mining with thin-theme discipline, and a
  mechanical leftover-identity sweep before shipping a rebuild.
- Counter: ABSORB-NEW ×1 (`recon`, phase: discover, with RECON.md and
  FEATURES.csv registered as artifacts with trigger, owner, and human
  gate); MERGE ×4 (architect → model, diff → verify, entrepreneur →
  research, brand → ship, with parity.py, imgdiff.py, reviews.py +
  themes, and sweep.py vendored into `scripts/`); REJECT ×6.
- Expected effect: "build something like X" work starts from evidence
  (a map and a matrix) instead of model memory; parity claims carry a
  printed number; competitor-review claims carry verbatim, linked
  quotes and a stated sample size.
- Blast radius: one new discover-phase skill, four additive sections in
  existing skills, five vendored stdlib scripts. No rule in force
  changed meaning; contrast.py and listing.py deliberately not taken
  (duplicate of scripts/contrast-check.py; niche store lint).
- Decision: approved by the owner at the human gate on 2026-10-24 and
  released as v1.14.0 (commit eb6aaa4) at EXPOSED; promotion requires a
  proving run — a real recon of an existing product carried through to
  a parity score.

## Batch promotion, 2026-10-24 (v1.15.0): the EXPOSED queue empties again

At the owner's instruction ("prove semua"), all five EXPOSED
adaptations were put through real proving runs on the same day. Each
run's full evidence lives in its folder; the one-line verdicts:

- A-005 (design shelf + registry format): Linkstash's DESIGN.md
  re-drafted in the new format with the shelf consulted under its
  load discipline; `npx @google/design.md lint` clean (0 errors,
  0 warnings) after substantive fixes. `docs/proving-runs/2026-10-24-a005/`
- A-006 (anti-slop fragments): full-corpus copy audit of Linkstash's
  21 UI strings against copy.md's tests — zero violations, with the
  what-not-to-flag discipline documentedly clearing the two
  near-misses; contrast-check.py pairs all PASS.
  `docs/proving-runs/2026-10-24-a006/`
- A-007 (frontend-design calibration): two-pass uniqueness review on
  a real Linkstash landing-page brief — six default elements cut
  against named rules before any code. `docs/proving-runs/2026-10-24-a007/`
- A-008 (mcp-builder + with-server): an MCP server built to the
  skill's protocol and evaluated 9/9 through the official client;
  with-server.py ran a real app end to end (201/200, clean
  teardown). Writeback: the `mcp<2` pin note now lives in the skill.
  `docs/proving-runs/2026-10-24-a008/`
- A-009 (recon + parity/review-mining/sweep merges): Linktree
  reverse-engineered from public sources only into RECON.md +
  FEATURES.csv, then scored by the vendored parity tool (0.0
  baseline, 8 must-haves enumerated, 2 skip rows excluded with
  reasons); source conflicts recorded, not averaged.
  `docs/proving-runs/2026-10-24-a009/`

All five are ADAPTED as of v1.15.0. The wheel's EXPOSED queue is
empty. Promotion was executed by the orchestrator on the owner's
instruction; release (commit, push, reinstall) follows the same
human gate as every prior promotion.

## A-010: fix-first tidy-up — scripts travel with their skill, installer validates (v1.15.1)

- Status: ADAPTED · Filed: 2026-10-25 · Promoted: 2026-10-25 (v1.15.1)
- Source signal: owner instruction ("rapihin biar mudah dipake"),
  scoped to the fix-first option: repair what is broken before any
  redesign. A repo audit found the real breakage first: every runtime
  tool the suite's skills quote (`parity.py`, `imgdiff.py`,
  `with-server.py`, `reviews.py`, `sweep.py`, `contrast-check.py`)
  lived in the repo-root `scripts/` folder, which the installer
  never copies — so every installed copy in Claude Code, Codex, and
  agy carried dangling references. The A-006 note had recorded this
  since 2026-10-23 as "not a current problem"; the audit proved it
  was one: `install.py --check` (new) failed on all 14 script files
  in the live v1.15.0 installs before the fix.
- Counter: the seven runtime tools moved into their owning skill's
  `scripts/` folder (verify: parity/imgdiff/with-server; research:
  reviews + themes; ship: sweep; design: contrast-check), following
  the mcp-builder precedent of skill-local scripts. The skill texts
  already said `scripts/<tool>`; the move makes those words true in
  an installed copy, so no prose had to change beyond one clarifying
  line per skill. The installer now regenerates the index, validates
  frontmatter, script references (suite-owned prose only — the
  vendored brand-systems shelf is excluded), and compilation before
  installing, verifies installed copies afterwards, validates the
  staged agy plugin, and gains a `--check` mode that diagnoses an
  install without touching it. Two A-005 format findings were also
  ruled on once, in `templates/design.md`: `primary` is defined as
  the linter's alias of `accent` (same value, always), and the
  registry gains an `elevation` section.
- Expected effect: `python3 scripts/parity.py` and its siblings work
  from an installed skill the first time a user runs them, and a
  broken install is a checkable fact instead of a confusing failure.
- Blast radius: file moves only (git mv, history kept); no skill
  text, rule, or verdict changed meaning. Repo-root `scripts/` keeps
  suite tooling only (install/generate_index/find_skill).
- Decision: executed on the owner's choice of the fix-first option,
  2026-10-25; promotion is immediate (this is a repair, not an
  absorption — the proving run is the --check output before/after
  plus running every moved tool from its new home).
- Promotion evidence: `install.py --check --all` on v1.15.0 installs
  failed on 14 missing script files; after the move, the suite
  validates clean, `--dry-run --all` passes with the staged plugin
  validated, and parity / contrast-check / with-server / reviews /
  sweep were each run from their new skill-local paths.

## A-011: Elephant-Goldfish batches 1+2 — EGM merges (EXPOSED)

- Status: EXPOSED · Filed: 2026-10-26 · Staged for v1.16.0
- Source signal: gluttony run 9 on google/elephant-goldfish-model
  (Apache-2.0 © Google LLC, commit
  3d0b34821ce88ad328b0c9bf0e06d7eb5f1cd669), at the owner's
  instruction ("serap dulu yang bisa di serap"). Three parallel
  auditors compared all seven upstream skills against the suite at
  v1.15.1; batch 1 acts on the brainstorm and draft audits only.
- Phenomenon: the suite's spec had no mandatory alternatives
  section, no every-file implementation list, and no check that a
  stranger could understand it; the grill had no parallel
  multi-lens pass and no formal readiness gate before reviewers
  were spawned; parallel reviewers' findings arrived raw, with no
  dedup step anywhere in the suite.
- Counter: merges into existing skills, no new skill. `spec` gains
  the Alternatives rule, the Detailed Implementation file list,
  the no-code rule, and the fresh-session bar with the Heilmeier
  eight questions; `templates/spec.md` gains Alternatives
  considered and Detailed implementation sections. `grill` gains
  the six-lens swarm (optional, at most two rounds), the
  critique-first rule, and the readiness gate. `orchestrate`
  gains the synthesizer step for parallel reviewers. `brief`
  gains the readiness rule. `docs/WORKFLOW.md` names the
  Elephant-Goldfish flow; `docs/ARTIFACTS.md` tightens the SPEC.md
  gate to match.
- Rejected in batch 1: banned-adjective and banned-apology lists,
  RFC publish and SITEMAP registration, per-section approval
  gates, the save-location gate, and the silent no-code
  enforcement (no meta-talk, no summaries, freeze on
  contradiction) — the last because it contradicts the suite's
  evidence-before-claims and ledger discipline; the no-code
  mechanism itself survives in `spec`.
- Expected effect: specs that a fresh session can actually execute
  from, with rejected alternatives on record so the next worker
  does not re-litigate them, and parallel reviews that arrive as
  one deduplicated report instead of overlapping raw findings.
- Decision: pending human gate for the combined batches 1+2.
  Batch 2 is adapted (review Goldfish protocol + triage, orchestrate
  range re-derivation, implement receiving triage, recon bootstrap
  mode, verify drift sweep with registered DRIFT_REPORT.md); its
  verdicts are in the same audit file. Nothing is committed until
  the owner approves the combined diff.
- Promotion evidence: none yet — EXPOSED until a real run uses
  the new spec sections and the lens swarm and the retro records
  that they held.

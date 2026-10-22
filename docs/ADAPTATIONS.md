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
| A-004 | 2026-10-22 | Gluttony run on a pasted 20-law UX instruction set: ux-heuristics.md specified mechanics (targets, states, input geometry) but never the decision laws behind them — no choice budget, convention, grouping, default-safety, or completion-state rules | 16 of 20 laws merged into ux-heuristics.md as checkable rules (new "Choice, grouping, and convention" section plus additions to Forms, Feedback, and Lists); 4 rejected as already covered (Fitts size, Zeigarnik, Prägnanz, Tesler) (audit: docs/audit/absorbed/2026-10-22-ux-laws.md) | EXPOSED (v1.7.0, pending promotion by adapt after a proving run) |

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

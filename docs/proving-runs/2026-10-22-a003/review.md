# Orchestrator review — proving run A-003 (data-viz absorption)

Reviewer: the orchestrator, 2026-10-22. The worker's report was treated
as a pointer, not evidence.

## Checks the orchestrator ran itself

- Re-ran `make_figures.py` from a clean state: exit 0, output numbers
  identical to the worker's report (150 rows, 1 duplicate, 0 missing,
  accuracies 93.33 / 97.78 / 95.56 / 91.11), and the four PNG files
  were byte-identical to the worker's run (matching md5sums before
  the review fix below). The run is deterministic.
- Grepped the script: no correlation call against the encoded species
  column (the trap is refused in a code comment and in summary.md),
  no pie, no rainbow/jet colormap anywhere.
- Visually inspected all four figures. Figure 1 uses position on
  common scales with the Okabe-Ito palette plus a distinct marker
  per species. Figure 2 separates species by position with box plots
  and raw points. Figure 3 splits the 150-row total and the
  single-digit defects into two panels with their own zero-based
  scales. Figure 4 is a dot plot with exact value labels, not bars.
  Every figure carries its title, one-sentence takeaway, and source
  line inside the image.

## Findings

- **F1 (fixed in rework round 1).** Figure 3 Panel B's automatic
  y-ticks landed on 0.25 steps for count data, implying a precision
  counts do not have — against the skill's own "ticks sit at
  meaningful intervals" rule. Fix applied in make_figures.py
  (integer ticks for the defects panel), the script re-ran clean,
  and the regenerated figure was visually re-verified: ticks are
  now 0, 1, 2. Rule confirmed: count axes take integer ticks.
- **F2 (not a defect — the run's strongest evidence).** The real
  data disagreed with the brief twice: Random Forest scored 91.11%,
  just below the brief's claimed 92–99% band, and missing values are
  0, not a small positive count. The worker plotted and reported
  both real values unchanged, did not re-roll the split, and did
  not tune a model to fit the brief. A proving run whose numbers
  bend toward the brief would prove nothing; this one held.
- **F3 (minor, noted, not blocking).** In Figure 2 the box plots'
  unfilled flier circles sit among the filled species markers and
  take a second look to distinguish. The plotted data points remain
  unambiguous (filled, species-coloured, species-shaped), and the
  summary's table reproduces the distribution numerically. Recorded
  for the next figure run, not reworked here.

## Verdicts

- Spec verdict: **PASS.** All four brief questions are answered by
  the chart type the skill prescribes for that question, the nominal
  encoding trap is refused explicitly with its reason, and the
  data-table / CSV fallback exists for every figure.
- Quality verdict: **PASS after one rework fix (F1).** The
  accessibility gate holds with evidence (backup channel per
  species, known-safe palette with hexes recorded, 300 dpi, bars
  at zero, dot plot where bars would have lied), and the five
  questions are answered per figure in summary.md.

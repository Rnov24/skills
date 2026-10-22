# Orchestrator review — proving run A-002 (hallmark absorption)

Reviewer: the orchestrator, 2026-10-22. The worker's report was treated
as a pointer, not evidence. Everything below was re-checked against the
files and fresh renders.

## Checks the orchestrator ran itself

- Grep sweeps re-run on all four output files: no `gradient`, no
  external URL, no `<script`, no `<img`, no `src=` — zero matches,
  confirming the worker's claims.
- Token audit of style.css: exactly 8 `oklch(` values, all inside the
  `:root` block; exactly one accent token (`oklch(44% 0.13 40)`),
  everything else warm neutrals tinted to hue 70.
- Fresh headless-Chromium renders by the orchestrator (saved as
  render-page-1280.png, render-page-320.png, render-form-1280.png):
  the page reads as a broadsheet catalogue, placeholders are visibly
  placeholders with subject + target size, the class schedule is a
  real table, the 320px render stacks cleanly with no horizontal
  overflow, and the form preview shows all eight states labelled,
  with the focus ring, error glyph + message, success glyphs, and
  loading spinner all visible.
- Formal WCAG contrast computed by the orchestrator from the OKLCH
  tokens (closing worker concern 4): ink on paper 16.60:1, muted ink
  8.45:1, accent on paper 7.55:1, on-accent on accent 7.54:1, danger
  7.41:1, success 7.37:1 — every text pair clears 4.5:1 by a wide
  margin.

## Findings

- **F1 (fixed in rework round 1).** The resting form-control border
  token `--rule-2` at 66% lightness measured **2.85:1** on paper, just
  under the suite's 3:1 UI-component floor. The worker had screened
  text pairs only. Fix applied and recorded in form.css: the token
  is darkened to 60% in form.css only, re-measured at **3.62:1**.
  Rule confirmed: the contrast gate covers component boundaries,
  not only text, and a lightness-gap screen is not a substitute for
  computing the pairs that carry a floor.
- **F2 (accepted, rule interpretation recorded).** The three-part
  error message wraps to three lines and grows that field's note
  area past the 1lh slot minimum. The eight-state contract as written
  requires a stable *minimum* height, which holds, and helper/error
  never coexist. A fixed height would clip the message, which is the
  worse failure. No change; the interpretation is recorded here so a
  future run does not re-litigate it.
- **F3 (accepted, exception stands).** The serif system stack is a
  deliberate exception to taste-core's banned-default rule, forced by
  the brief's system-stacks-only, zero-budget constraints, and
  recorded with its reasoning in reasoning-trace.md before the build.
  This is the exception mechanism working as designed: an exception
  that is written down before it ships is a decision, not a drift.
- **F4 (accepted limitation).** Forced states are class mirrors of
  the pseudo-class declarations (verified in render for focus), and
  the restacked schedule table was not screen-reader tested. Both
  are honest limits of a static proving artifact and are recorded in
  the worker's concerns; neither undermines what this run proves,
  because the CSS declarations themselves are the mechanism under
  test and they are identical in both forms.

## Verdicts

- Spec verdict: **PASS.** Both briefs are answered in full — the page
  carries hero, 6-product catalogue, 3-class schedule, testimonial
  section and contact footer, and the component deliverable renders
  the contract's own eight states. The two traps fired correctly:
  Stat-Led and Quote-Led were rejected in writing because no real
  metric or quote exists, and the testimonial section is an honest
  labelled empty state with zero invented quotes, ratings, or
  numbers (the orchestrator re-audited the rendered numbers against
  the worker's inventory; everything present is catalogue authoring
  the packet explicitly allowed).
- Quality verdict: **PASS after one rework fix (F1).** Pre-flight,
  preview block, rotation pick with reasons, archetype picks with
  knob values, imagery gate, component-scope stand-down, and input
  geometry (44px shared control height, 1px border in every state,
  reserved outline slot) are all present in the artifacts and hold
  under the orchestrator's own checks.

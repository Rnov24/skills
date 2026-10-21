---
name: using-rnov-skills
description: The router for the rnov24 suite. Use at the start of any product, design, or engineering task to decide which flow applies, which artifacts the task needs, and which skill runs next.
---

# Using rnov24 skills

You are entering a workflow, not a toolbox. Your first job on any task is to
classify it and pick the flow. Do not start producing artifacts or code before
this classification exists, even if only as three lines in the run ledger.

## Classify the task

Answer four questions:

1. **Size.** One sitting, one session, or many sessions? Many sessions means
   the work needs a ticket graph and probably a wayfinder-style map before
   anything else.
2. **Novelty.** Is the problem understood, or is the request a guess at a
   problem? Unclear problem goes to `brief` first. Always.
3. **Surface.** Does it touch users, data, or a consumed interface? Users
   trigger the product and design phases. Persisted data triggers `model`
   for the ERD. A consumed boundary triggers `model` for API documentation.
4. **Risk.** Irreversible actions, production data, money, or other people's
   work raise the gate level: human approvals and blind review stop being
   optional.

## Standard flows

- **New product or major feature:** setup (if absent) → brief → research (if
  facts are missing) → grill → define-product → design → model → spec →
  tickets → implement → review → verify → ship → retro.
- **Feature in an existing product:** brief (short) → grill (only the new
  decisions) → define-product (delta stories) → design/model deltas → spec →
  tickets → implement → review → verify → ship.
- **Bug:** debug (red feedback loop first) → implement the fix as one ticket →
  review → verify. Escalate to grill only if three fixes fail.
- **Refactor or architecture change:** grill → spec → tickets → implement →
  review → verify. Add model if invariants or data change.
- **Design-only task:** brief → design → keyframe gate. No engineering phases
  until the keyframe is approved.
- **Question:** research. One file, primary sources, done.

## Rules

- Skipping a phase is fine; skipping it silently is not. Record the skip and
  the reason in the run ledger.
- If `setup-workspace` has never run on this repo, run it before the first
  real flow. Every later phase assumes its layout exists.
- When two skills seem to apply, the earlier phase in the pipeline wins. A
  design argument during implement is a grill that was skipped; go back.

## Anti-patterns

- Opening a PRD for a typo fix, or skipping one for a new product.
- Letting the size of the request set the process instead of its risk.
- Treating this router as paperwork: the classification is three lines, the
  cost of skipping it is a wrong workflow for a week.

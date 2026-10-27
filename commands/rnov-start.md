---
description: Start here. Say what you want in plain words; the router picks the flow and the first skill.
argument-hint: "[what you want to do]"
---
# /rnov-start

Follow the `using-rnov-skills` skill.

## Steps

1. Read the entry map:

## Front door

- `/rnov-start` [what you want to do] — Start here. Say what you want in plain words; the router picks the flow and the first skill.

## The two paths

- `/rnov-new` [what you want to build] — Start something new, from scratch.
  Flow: `setup → brief → research → grill → define-product → design → model → spec → tickets → implement → review → verify → ship → retro`
- `/rnov-improve` [what to improve] — Improve something that already exists.
  Flow: `brief → grill → define-product → design → model → spec → tickets → implement → review → verify → ship`

## Improve a UI surface

- `/rnov-improve-ui` [UI surface to improve] — Improve a UI surface, audit first.
  Flow: `design → implement → review → verify`

## Fix

- `/rnov-fix` [what is broken] — Fix a bug.
  Flow: `debug → implement → review → verify`

## Audits

- `/rnov-goldfish` [path to SPEC.md or design doc] — Goldfish this spec: five fresh-context stages that test whether a stranger could understand and re-implement it.
- `/rnov-bootstrap` [repo root or directory] — Document an undocumented codebase bottom-up into per-directory README contracts, leaf first.
- `/rnov-drift` [directory to sweep] — Check whether the code has drifted: sweep a tree's SPEC.md, DESIGN.md, and README contracts against the current code and report only the divergences.

## Shape of the suite

The suite is one pipeline entered through two paths: `/rnov-new` starts something new and `/rnov-improve` improves what exists. `/rnov-fix` joins the pipeline at implement, skipping setup through tickets. Audits run before changes. Whenever a task matches no command, `/rnov-start` decides.

2. classify per `using-rnov-skills` and load one skill

## Output

The next skill to run, with the classification in three lines.

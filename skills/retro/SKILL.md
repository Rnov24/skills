---
name: retro
description: Close the loop after a ship, a failure, or a capped loop — record what the artifacts say happened and file each lesson where the next run will read it. Use at the end of every significant run.
---

# Retro

A workflow that does not learn is just paperwork with good posture. The
retro is short, evidence-based, and ends with filings, not feelings.

## Process

1. **Read the run, not your memory of it.** Ledger, packets, reports,
   verdicts, rework rounds. Where did rounds accumulate? Which gate caught
   what? Which artifact was wrong, missing, or ignored — and which phase
   owned it?
2. **Name the three kinds of finding:** a worker lesson (a packet that was
   unclear, a scope that was wrong), a suite lesson (a gate that fired too
   late, a template field nobody used), and a workspace lesson (a constraint
   the floor should now enforce, a glossary term that caused confusion).
3. **File each lesson where the next run reads it.** Constraint lessons amend
   CONSTRAINTS.md (the floor rises, with the incident as the reason). Suite
   lessons become issues or edits against this suite. Project lessons go to
   the project's own notes or ADR set. A lesson recorded in the retro file
   and nowhere else is a lesson scheduled to be re-learned at full price.
4. **Close the run.** RETRO.md from `templates/retro.md`, linked from the
   ledger. Open findings that were parked get their trigger for reopening
   stated, or they get closed honestly as accepted risks with a name
   attached.

## Rules

- Numbers over impressions: rounds, findings per axis, escapes (defects
  found after the gate that should have caught them). An escape is the most
  valuable datum in the retro; it indicts a specific gate.
- Blame the artifact or the process, never the worker's character; the fix
  is a better packet, gate, or template.
- Keep it to a page. A retro nobody reads is worse than none, because it
  performs learning instead of doing it.

## Anti-patterns

- A victory-lap retro after a smooth run that skips the near-misses.
- Lessons phrased as virtues ("communicate better") instead of filings
  ("packet template gains a field for X").

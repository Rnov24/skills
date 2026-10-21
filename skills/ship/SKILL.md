---
name: ship
description: Ship finished work — launch readiness, git discipline, pull requests, and the human grant for irreversible actions. Use when verified work is ready to merge, release, or deploy.
---

# Ship

Shipping is the phase where preparation meets consequence. The suite's rule
is simple: everything up to the irreversible moment is the agent's job to
prepare; the irreversible moment itself belongs to the human's grant.

## Readiness

Walk the launch list before asking for any grant: verify phase passed on the
exact artifact being shipped, review verdicts closed or parked with rulings,
migrations carry rollback notes, configuration and secrets are present in
the target environment (checked, not assumed), monitoring or at least a
named human watching the first hour, and the rollback path is written down
before it is needed.

## Git discipline

- Small, honest commits on save points; messages that say what changed and
  why, in the project's voice.
- Branches land by the repo's convention (merge, squash, or PR) — recorded
  in setup, not improvised per ship.
- Dangerous operations — force-push, history rewrite, deleting shared
  branches — always need an explicit grant, every time, no standing
  permission.

## The grant

Ask once, precisely: what will happen, to what, with what allowance, and
what the rollback is. "Deploy build 1.4.2 to production; database migration
0007 runs and is reversible; rollback is redeploy 1.4.1." A grant covers
exactly that action. Anything discovered mid-ship that changes the action
voids the grant and gets a new ask.

## Pull requests

A PR body carries: the change and its why, the tickets and AC IDs it closes,
the evidence from verify (commands and outcomes), what was deliberately not
touched, and risks or concerns worth a reviewer's first look. Reviewers
should never have to reconstruct the story from the diff.

## After landing

Confirm the shipped state from the target's own signals (health endpoint,
release page, user-visible check), not from the deploy tool's optimism.
Then hand off to `retro` while the run is still warm.

## Anti-patterns

- Shipping on a green local run with the target environment unchecked.
- Bundling an unreviewed fix into a release because the window was open.
- Announcing "deployed" before the confirmation check returns.

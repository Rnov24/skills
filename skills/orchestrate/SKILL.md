---
phase: control
keywords: delegate, delegasi, subagent, worker, parallel, packet, dispatch, orkestrasi, agy, assign task
name: orchestrate
description: The orchestrator protocol for the main agent. Use whenever work is delegated to subagents or external worker agents, run in parallel, or accepted from a worker — packets, report schema, dual review, rework loop, escalation.
---

# Orchestrate

The main agent is an orchestrator, not the fastest pair of hands. It owns the
plan, the artifacts, the gates, and the verdicts. Workers own bounded units
of execution. This skill is the contract between them.

## The unit of delegation is a packet file

Never delegate from chat memory. For each unit of work, write a packet file
(`templates/packet.md`) containing:

- **Stable header, byte-identical across packets in a run:** suite rules, repo
  layout, constraint floor, verdict vocabulary. Stability is not tidiness; it
  is what makes worker context cheap and behaviour predictable.
- **Ticket pointer:** the ticket ID and the artifact paths the worker must
  read (spec sections, AC IDs, DESIGN.md, API.md). Pointers, not pasted
  prose. One source of truth per meaning.
- **Scope:** the one coherent change this packet exists to make, the files it
  may touch, and the files it must not touch.
- **Acceptance:** the AC IDs it must satisfy and the exact verification
  commands to run, copied from the ticket.
- **Report contract:** the report file path and the schema below.

One packet, one coherent change. If a packet needs the word "and" to describe
its change twice, it is two packets.

## The report schema is fixed

Workers return a report file (`templates/report.md`) and nothing else is
treated as a result:

- status: DONE, DONE_WITH_CONCERNS, NEEDS_CONTEXT, or BLOCKED
- commits or files changed
- one-line test summary (full output lives in files, not the report)
- concerns, each tied to a file, an AC ID, or a decision the worker did not
  feel authorised to make
- footer: checks run, checks skipped and why

A worker that finishes without a report has not finished. A report that
claims success without evidence is a false report, and the orchestrator says
so in the ledger.

## Acceptance is the orchestrator's job

**The worker's report is never acceptance evidence.** For every returned
packet the orchestrator:

1. Reads the diff or the artifact itself, not the summary of it.
2. Builds the review package from the base recorded *before* dispatch. Never
   reconstruct the base afterwards; a guessed base silently truncates
   multi-commit work.
3. Runs the ticket's verification commands itself, or reads fresh output from
   having run them.
4. Records the verdict against the packet's AC IDs.

## Dual verdicts, never merged

Every unit gets two independent verdicts, reported side by side:

- **Spec verdict:** does it satisfy the ticket and its AC IDs, completely and
  without scope creep?
- **Quality verdict:** is it well built — tests real, constraints respected,
  no silent weakening of the floor?

One axis may never mask the other. Spec-perfect but rotten is REWORK.
Beautiful but off-spec is REWORK.

For non-code artifacts (PRD, DESIGN, ERD, API docs), the same two verdicts
apply against the artifact's gate checklist in `docs/ARTIFACTS.md`.

## Verdict vocabulary

- **ACCEPT** — both verdicts pass; the unit joins the integration line.
- **REWORK** — findings listed, each with file and line or artifact section;
  the packet returns to a worker with the findings appended.
- **ESCALATE** — the loop cap is hit, a decision belongs to the human, or two
  verdicts conflict irreconcilably. Escalation includes the full finding
  history, not a summary.

## The rework loop is bounded

Maximum five rounds per unit. Rounds 1–3 resume the same worker, which holds
the context of its own mistakes. Rounds 4–5 go to a fresh, stronger worker
with the finding history attached — a worker that has failed three times at
the same unit is telling you something. At the cap, remaining findings are
parked only by a written ruling in the ledger, naming who ruled and why.
Silent discards are forbidden; a finding nobody ruled on is an open finding.

Receiving a review works the same way in reverse: verify each finding against
the code or artifact before acting on it, push back with evidence when a
finding is wrong, and never perform gratitude instead of verification.

## Parallel safety

- The ticket graph's unblocked frontier is the only legal parallel schedule.
  If it is not on the frontier, it does not start.
- One writer per file set. Two packets that can touch the same files run in
  sequence or in separate worktrees, and the packet says which.
- Workers never share mutable state: no shared scratch files, no "read the
  other's report for context". Coordination happens through artifacts the
  orchestrator curates.
- Integration is a role, not an accident: the orchestrator merges accepted
  units onto the integration line and re-runs the floor checks after each
  merge.

## The ledger

The orchestrator keeps a run ledger (a file, not memory): packets dispatched,
bases recorded, verdicts, rework rounds, rulings, skipped phases with
reasons, and grants received. The ledger survives context loss; a fresh
orchestrator session must be able to reconstruct the run from the ledger and
the artifacts alone. Anything not in the ledger is re-derived or re-asked,
never assumed.

## Escalation rules

Escalate to the human when: a gate needs approval, a loop hits its cap, a
worker reports BLOCKED twice on the same unit, scope must grow beyond the
approved artifacts, or an irreversible action needs a grant. Escalate with
the artifact and the exact decision needed, in one message. Do not escalate
vibes; escalate decisions.

## Anti-patterns

- Delegating a whole feature as one packet.
- Pasting the spec into the packet instead of pointing at it (the copy drifts
  the moment the spec is edited).
- Reading the report and accepting without opening the diff.
- Pre-judging findings in a reviewer's prompt ("this is probably fine, just
  check") — reviewers get the artifact and the contract, never the
  orchestrator's hopes.
- Restarting a stuck worker from scratch instead of resuming it with the
  findings.

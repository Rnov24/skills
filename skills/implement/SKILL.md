---
phase: build
keywords: implement, implementasi, coding, build feature, kerjakan, execute ticket, prototype, prototyping
name: implement
description: Execute tickets as bounded, test-first, verifiable slices. Use when implementing from a spec and ticket graph, whether as the orchestrator's worker or directly — including prototype work and receiving-review fixes.
---

# Implement

Implementation is the phase the other phases exist to make boring. The
ticket says what, the spec says why, the artifacts say how it must look and
behave. Your job is a faithful, verifiable slice — not a reinterpretation.

## Worker protocol

1. **Read by pointer.** The packet names the ticket, the spec sections, the
   AC IDs, and the artifacts. Read them. If a pointer is missing or an
   artifact contradicts the ticket, stop and report NEEDS_CONTEXT; guessing
   across a contradiction is how suites lose trust in workers.
2. **Work in your boundary.** Touch the files the ticket claims. Needing a
   file outside the claim is information: report it, do not quietly expand.
3. **Report in the schema.** Status, files changed, one-line test summary,
   concerns. The report is a map for the reviewer, not a defence brief.

## Test-first at the agreed seams

- The red step is real: write the failing test at the seam the spec named,
  watch it fail for the expected reason, then implement until it passes,
  then refactor with the test as a safety net.
- Tests attach to behaviour and AC IDs, never to implementation trivia. A
  test that breaks when a private helper is renamed is a liability wearing a
  costume.
- When no seam exists for what the ticket needs, that is a spec finding.
  Raise it; do not test around it with mocks of everything.

## Thin slices, save points

- Implement in increments that each leave the system working and verified.
  Commit at save points: a green increment committed is worth more than a
  brilliant uncommitted hour.
- Keep the diff inside the ticket. Drive-by refactors, formatting sweeps,
  and "while I was in there" fixes go in the report as proposals, not in the
  change.

## Prototypes

When a ticket's job is to answer a design question (does this state model
feel right, does this interaction work), build it throwaway on purpose:
ugly internals allowed, one command to run, the question written at the top.
A prototype's deliverable is the answer, recorded in the ticket or an ADR —
never the code, which is deleted or quarantined so it cannot be mistaken
for a foundation.

## Comments

A comment earns its place only with information the code does not
already show: why a choice was made, a constraint the code must not
break, a workaround and what would retire it, an edge case the lines
below are defending against, a contract with a caller. Comments that
restate the code, narrate the workflow ("now we loop through the
items"), decorate with banners or separators, label the obvious, or
sign and date the work are slop and are removed on sight.

Length is part of the test, not an exception to it: a true, valuable
comment padded into a paragraph — reasoning chains, issue numbers,
version history — is still slop. One line; two at most, when the second
carries a new fact. The long reasoning belongs in the packet, the
report, or an ADR, where the suite already routes it. A cleanup pass
over comments touches comment lines only — never code, identifiers, or
formatting in the same pass, so its diff can be verified at a glance.

## Receiving review

When findings come back: verify each against the code before acting, fix
what is real, and where a finding is wrong, answer with evidence in the
report. Never fix performatively to end the loop; the loop ends when the
findings are addressed, and the reviewer verdicts each one ADDRESSED or NOT
ADDRESSED.

Triage each finding before touching code, into CONTEST or PROPOSE FIX.
A CONTEST needs exact evidence defending the current text; a PROPOSE FIX
needs a precise replacement, not a direction. PROPOSE FIX items may be
applied as one batch once the human has accepted them; CONTEST items are
never auto-accepted. When the human walks the findings one by one, defer
all edits until every item is decided, then apply the accepted batch.
The decisions live in the report and the ledger, never in memory.

## Anti-patterns

- Writing the implementation first and shopping for a test that passes
  afterwards.
- Expanding scope because the better design became visible mid-ticket; file
  it, finish the slice.
- Reporting DONE with checks skipped and no reason recorded.

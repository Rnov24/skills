---
phase: build
keywords: bug, error, debugging, gagal, broken, rusak, regression, regresi, slow, lambat, not working
name: debug
description: Diagnose bugs and performance regressions with a red-capable feedback loop before any theory. Use when something fails, breaks, or regresses — and when fixes have already failed once.
---

# Debug

Debugging without a feedback loop is literature. This skill forbids
theorising until a loop exists that can prove a theory wrong.

## The gate

Before any diagnosis is written down, name the loop: **one command** that is
fast, deterministic, and already goes red on the exact symptom — a failing
test, a reproduction script, a curl against the broken endpoint, a replayed
trace. If no such command exists, building it is the first task. A loop that
goes red on something similar but not identical diagnoses a different bug.

## Process

1. **Reproduce and minimise.** Shrink the failing case until removing any
   element makes it pass. Half of all root causes are obvious at the minimal
   case, and the minimal case becomes the regression test.
2. **Hypothesise in writing, one variable at a time.** Each hypothesis names
   the observation that would kill it. Test the cheapest killer first.
3. **Instrument at the boundary.** Logs and probes go where the hypothesis
   says the truth changes value, tagged so they can be removed in one sweep
   when the bug dies.
4. **Fix the cause, verify with the original loop.** The loop going green on
   the minimal case and on the original symptom are both required; one
   without the other is a coincidence with good PR.
5. **Regression-test it.** The minimal case becomes a permanent test citing
   the bug. A bug fixed without a test is a bug scheduled to return.

## The three-failure rule

Three failed fixes means the problem is not where you think it is. Stop
fixing. Question the architecture or the assumption underneath, write down
what the failures have in common, and involve the human. A fourth attempt on
the same theory is not persistence; it is the definition of the loop this
rule exists to break.

## Performance regressions

Same discipline, different loop: a benchmark or profile that reproduces the
regression with numbers. Bisect to the change, fix or revert with the number
attached. "It feels faster now" is not a result, in either direction.

## Anti-patterns

- Shotgun changes: three fixes at once, then attributing the cure to the
  favourite.
- Reading code until an explanation feels satisfying, then fixing the
  feeling.
- Leaving debug instrumentation in the shipped code.

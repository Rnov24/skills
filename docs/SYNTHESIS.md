# Synthesis: how this suite was designed

This suite was not written from a blank page. In October 2026 the full local
skill library — 121 installed skills plus the older workspace set, 175 entries
before deduplication — was audited skill by skill: purpose, concrete pros,
concrete cons, and a verdict of adopt, adapt, merge, or drop. The five audit
files live in `docs/audit/` and total roughly 2,100 lines. This document is
the design record of what the audit produced.

## Verdict totals

Across the five batches, 124 distinct skills were audited: 36 adopted in
substance, 55 adapted, 13 merged into a stronger neighbour, 17 dropped, and 3
marked out of scope for a development, design, and product suite (marketing
video and social content skills among them).

## What each predecessor did best — and where it stopped

**Addy Osmani's agent-skills** supplied the engineering gates: the hard
spec gate, the constraint floor that may only rise, the five-axis review with
a mutation check, and doubt-driven blind review. It has no product artifacts
at all, no traceability, and its routing is by task verb rather than artifact
state.

**Matt Pocock's skills** supplied the artifact discipline: specs synthesised
from conversation, tickets as a graph with blocking edges, glossary and ADR
capture at the moment a decision resolves, and two-axis review that never
lets one axis mask the other. It has no product front end, no design phase,
no ERD or API artifacts, and its delegation has no contract layer — no packet
or report schema, no per-ticket gate, no escalation semantics.

**Superpowers** supplied the strongest orchestration machinery: dispatch as
an artifact (a task-brief file in, a report file out), dual-verdict task
review against a diff package built from a base recorded before dispatch, and
a bounded rework loop with adjudication instead of silent discards. Its
review machinery is git-diff-based and code-only, and it has no artifact
chain beyond spec and plan.

**Atelier and the design shelf** supplied the design constitution chain —
brief to DESIGN.md to approved keyframes — and council review with a hard
two-round stop. The audit found at least fourteen copies of the same anti-slop
taste manifesto wearing different clothes; the suite keeps one taste core as
checkable rules inside DESIGN.md and drops the rest.

**The product shelf** was the thinnest. The existing PRD skill had a good
discovery gate and an honesty rule (unknowns are labelled TBD, never
invented), but emitted one monolithic document with no persona depth, no
checkable acceptance format, and no handoff to design, data, or API. The
product phase of this suite is largely new construction, built to the audit's
gap list. Kaggi's gate, grant, and journal mechanics — built for data-science
competitions — turned out to be the best model for human approval points and
were generalised into the suite's gate system.

## Decisions that shaped the suite

1. **One workflow, not a toolbox.** A router skill and a phase map replace
   per-skill discovery. Skills are phases and disciplines inside one pipeline.
2. **Artifact triggers over artifact habits.** Every document in the registry
   names the condition that justifies creating it. This is the direct answer
   to "workflow must be artifact-based, but not files for the sake of files".
3. **Traceability IDs from story to verdict.** No predecessor had the chain
   story → acceptance criterion → ticket → test → review verdict. It is the
   suite's backbone and its definition of done.
4. **One canonical packet, one canonical report, one verdict vocabulary.**
   Worker type (native subagent, external CLI agent, human) changes the
   transport, never the contract.
5. **Review is re-based from diffs to artifacts.** Code review keeps the diff
   package; product and design artifacts get the same dual-verdict treatment
   against their own gates.
6. **Every loop has a cap and every cap has an escalation.** Rework stops at
   five rounds, design council at two, debugging at three failed fixes. At
   the cap, a human rules, and the ruling is written down.

## What was deliberately left out

Writing-craft skills, teaching skills, exercise scaffolding, marketing and
social content production, competition-specific tooling, and tool-locked
setup skills (one vendor's hooks, one framework's test migrator) were dropped
or left as standalone tools. A suite that routes everything routes nothing.

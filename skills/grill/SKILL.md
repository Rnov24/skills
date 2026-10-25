---
phase: discover
keywords: grill, decisions, keputusan, stress test, uji rencana, assumptions, asumsi, trade-off, interview
name: grill
description: Stress-test a plan, design, or decision tree one question at a time until every branch resolves. Use when a plan has unexplored decisions, hidden assumptions, or trade-offs nobody has named — before spec or PRD work hardens it.
---

# Grill

A grill is a relentless interview with a structure: the decision tree. Its
job is to find every decision the plan quietly depends on and force it into
the open while changing it is still cheap.

## Process

1. **Build the frontier.** List the open decisions. A decision joins the
   frontier only when every decision it depends on has resolved — never ask
   a question whose prerequisites are still open, because its answer would
   be built on sand.
2. **One question at a time.** Sharp and short. The person answers, the
   answer lands, the tree updates. No option decks, no lectures between
   questions; a wall of choices teaches the person to skim, and skimmed
   answers are how bad decisions get ratified.
3. **Facts are delegated, decisions are not.** When a question needs a fact
   (what a library supports, what the data looks like), send a worker or look
   it up. Never ask the human a question the codebase or the docs can answer.
4. **Capture inline, the moment a branch resolves.** A term with a settled
   meaning goes into GLOSSARY.md. A decision that passes the three-gate test
   (hard to reverse, surprising without context, a real trade-off) becomes
   an ADR. Documents written "later, from memory" are documents written
   wrong.
5. **End states.** The grill ends when the frontier is empty, or when the
   remaining decisions are explicitly parked with an owner and a trigger for
   reopening them.

## Rules

- The grill serves the plan, not the interrogator. When the person is tired
  or the remaining branches are low-stakes, park them and say so.
- Push back with evidence when an answer contradicts a constraint or an
  earlier decision. Naming the contradiction is respect; quietly recording
  both answers is not.
- **Critique first.** Lead with what is wrong, missing, or risky before
  naming what is good. For every strategy on the table, state the
  strongest counter-argument to it and whether that counter-argument
  holds. Agreement is earned by surviving scrutiny, not granted by
  default; praise without substance is noise, not encouragement.
- Alternatives get one honest paragraph each when a decision is genuinely
  contested, recorded in the ADR — not a sales deck for the favourite.

## Lens swarm (optional, delegated)

When the direction is genuinely open or the stakes are high, the grill
may run a parallel lens swarm on the anchored hypothesis instead of
arguing it out in one session. Each lens is a fresh worker that receives
only the hypothesis and the artifacts it needs — no conversation history,
no author claims, no earlier verdicts. The six lenses are: Contrarian
(YAGNI — does this need to exist, or does an existing library, service,
or API already solve most of it?), Cost and quota (peak load, storage,
token or compute budget, quota ceilings at scale), UX and ergonomics
(is the surface intuitive, do errors tell the user what to do next?),
Migration and compatibility (how existing clients and data move, what
breaks, how rollback works), Observability (can on-call trace and
triage this at 3 AM?), and Tech debt (what coupling or brittle state
does this leave behind in two years?).

The swarm runs at most twice per hypothesis; after the second round its
findings are either resolved into the decision tree, recorded as ADRs,
or parked with an owner and a trigger. Findings are deduplicated before
they reach the human (see `orchestrate` for the synthesizer step); a
list of raw, overlapping findings is not a result.

**Readiness gate.** Do not spawn the swarm until the hypothesis is
anchored in two or three sentences the human recognises as their own
and the human confirms readiness. A review of an unanchored idea is
noise, and a same-context opinion is not a fresh-context review.

## Anti-patterns

- Asking three questions in one message to save time; it saves nothing and
  loses the thread.
- Grilling settled ground to look thorough.
- Letting the grill produce only conversation: if no glossary term, ADR, or
  brief amendment came out of a hard answer, the capture step failed.
- Spawning reviewers before the hypothesis is anchored; the swarm then
  argues about a moving target and its findings cannot land anywhere.

<!-- Credit: lens swarm, critique-first rule, and readiness gate adapted
from google/elephant-goldfish-model (Apache-2.0, commit
3d0b34821ce88ad328b0c9bf0e06d7eb5f1cd669), skill egm-brainstorm.
Mechanisms rewritten into suite conventions; see
docs/audit/absorbed/2026-10-26-elephant-goldfish-model.md (A-011). -->

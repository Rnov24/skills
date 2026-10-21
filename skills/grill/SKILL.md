---
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
- Alternatives get one honest paragraph each when a decision is genuinely
  contested, recorded in the ADR — not a sales deck for the favourite.

## Anti-patterns

- Asking three questions in one message to save time; it saves nothing and
  loses the thread.
- Grilling settled ground to look thorough.
- Letting the grill produce only conversation: if no glossary term, ADR, or
  brief amendment came out of a hard answer, the capture step failed.

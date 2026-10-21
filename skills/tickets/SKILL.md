---
name: tickets
description: Break a spec into tracer-bullet tickets with blocking edges. Use when a spec is approved and work must be scheduled across sessions or workers — each ticket independently verifiable, the graph computable into a parallel frontier.
---

# Tickets

A ticket list is a reading order. A ticket graph is a schedule. This skill
produces the graph.

## Ticket shape

Each ticket, from `templates/ticket.md`, is a tracer bullet: a thin slice
that cuts through every layer it touches and ends in something verifiable,
never a horizontal slice ("all the database work") that proves nothing until
the end. Every ticket declares:

- what it covers — spec sections and AC IDs, by reference
- the change in one paragraph
- **blocked by:** the tickets that must land first (edges are data, written
  in the ticket, not implied by list position)
- files it expects to touch (its ownership claim for parallel safety)
- verification commands and the AC checks that prove it
- size; a ticket bigger than a session is split, and the split trigger is
  objective ("touches a second subsystem") not a feeling

## The frontier

The frontier is the set of tickets whose blockers have all landed. The
frontier — computed from the edges, never eyeballed — is the only set of
tickets that may run in parallel, and `orchestrate` schedules from it.
When the frontier is wider than the worker pool, order by risk: the ticket
most likely to invalidate other tickets goes first.

## Rules

- Every spec section and AC ID is covered by at least one ticket; the
  coverage check is mechanical and runs before implementation starts.
- A ticket discovered mid-run to be wrong is amended in the open, with the
  reason; edges are re-checked after every amendment.
- Integration is scheduled, not hoped for: the final ticket on any branch of
  the graph is the integration and floor-check ticket.

## Anti-patterns

- Tickets written as a numbered to-do list with hidden dependencies.
- One mega-ticket titled "implement the feature".
- Edges recorded in the orchestrator's head instead of in the tickets, where
  a fresh session can compute them.

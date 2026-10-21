---
phase: define
keywords: prd, persona, user story, acceptance criteria, requirements, product, produk, mvp, fitur
name: define-product
description: Define the product layer — PRD, personas, and user stories with checkable acceptance criteria. Use when a brief is approved and a new product or user-facing feature needs its requirements fixed before design and engineering begin.
---

# Define product

This phase converts an approved brief into the three artifacts that design
and engineering will be held to: the PRD, the personas, and the stories.
They are separate files on purpose. One monolithic document blurs three
different conversations — why, who, and what exactly — and each blurs the
others' gates.

## Discovery gate

Do not draft anything until three questions have real answers:

1. What is the problem, in the words of the person who has it? (From the
   brief; if it is not there, go back to `brief`.)
2. How will anyone know this worked — which metric, at what baseline, moving
   to what target, measured how?
3. What constrains the solution — platform, budget, deadline, existing
   systems, regulation?

An answer that does not exist yet is written as `TBD` with an owner. Unknowns
are labelled, never invented. A fabricated constraint is worse than a missing
one because everything downstream will trust it.

## PRD.md

From `templates/prd.md`. It carries: the problem, the goal and success
metrics (baseline, target, instrumentation), scope and an explicit non-goal
list, assumptions and open questions as living logs, the stakeholder list and
who signs off, and links — never copies — to personas and stories. Keep it
about the why and the boundary; behaviour detail belongs to stories.

## PERSONAS.md

From `templates/persona.md`. A persona earns its place only if a design or
scope decision would change because of it. Each persona carries: goals, the
job they are hiring the product for, constraints (device, time, skill,
context), and the failure mode that loses them. Demographic detail without
behavioural consequence is decoration; cut it.

## STORIES.md

From `templates/stories.md`. Each story gets an ID (`US-01`...) and:

- the persona and the want, in one sentence
- **acceptance criteria** with IDs (`AC-01.1`...), each written to be
  checkable by a person who was not in the room: Given/When/Then, or a
  measurable condition with a number in it
- priority (must / should / could) and a rough size; a story too big to test
  is two stories

The vague-versus-concrete test applies to every criterion: "the page loads
fast" fails; "the exam list renders within 1.5s on a mid-range Android phone
on 4G" passes. If a criterion cannot be checked, it is a wish, and wishes do
not go into tickets.

## Handoffs

This phase emits, and the next phases consume:

- to `design`: personas and the PRD goal — flows are written per persona
- to `model`: the entities and rules implied by the stories
- to `spec`: story IDs and their AC IDs, which the spec must cite and the
  review must eventually verdict, one by one

## Gate

The human approves the PRD. Approval means: the problem is right, the
metrics are the ones success will be judged by, and the non-goals are truly
out. Stories may keep evolving after the gate; their changes are amendments
with dates, not silent edits.

## Anti-patterns

- One mega-document that mixes PRD, personas, and stories.
- Metrics with no baseline ("increase engagement") — unmeasurable at the end
  exactly as at the start.
- Acceptance criteria written as restatements of the story ("user can log in"
  as the AC for "user logs in").
- Personas invented to fill the template rather than to change a decision.

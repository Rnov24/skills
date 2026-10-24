---
phase: design
keywords: erd, database, schema, skema, api, endpoint, domain model, table, tabel, relasi, data model
name: model
description: Model the domain, data, and interfaces — DOMAIN.md, ERD.md, and API.md as first-class artifacts. Use when a project has entities with lifecycles, persisted data, schema changes, or a boundary other systems consume.
---

# Model

Code forgives a fuzzy model for about a week. Data does not forgive it at
all. This phase gives the project three artifacts that engineering usually
leaves implicit until they hurt: the domain model, the data model, and the
interface contracts.

## DOMAIN.md

From `templates/domain.md`, fed by the stories. For each entity: what it is
in one sentence of the project's own language, its lifecycle states and the
transitions allowed between them, and its invariants — the rules that must
hold no matter which screen or endpoint touches it. Every term that lands
here with a project-specific meaning also lands in GLOSSARY.md. Vague entity
names are resolved here, at document prices, not later at migration prices.

## ERD.md

From `templates/erd.md`. Every table traces to a domain entity; a table with
no entity is either a missing entity or a table that should not exist. Every
relationship states cardinality, optionality, and the deletion rule (cascade,
restrict, soft-delete, null-out) with the reason. Schema changes after the
gate become their own tickets with migration and rollback notes — never a
quiet edit inside a feature ticket.

## API.md

From `templates/api.md`. Every operation states: purpose, caller, inputs with
types and constraints, outputs, error cases with their shapes, and the auth
rule. The document opens with the conventions that apply everywhere —
versioning, breaking-change policy, error envelope, pagination, idempotency —
stated once, not rediscovered per endpoint. An interface designed here is a
deep module on purpose: a small surface that hides real complexity, with the
hidden part named so implementers know what they are allowed to assume.

## From a recon map

When a RECON.md feeds this phase, its inferred model arrives with
evidence and a confidence per entity. Carry both into ERD.md: a
high-confidence entity becomes schema; a guess becomes schema plus an
open question, never silent fact. The hard invariants the recon
observed (the double-booking that must never happen, the balance that
must never go negative) are database problems, not UI problems: they
land as unique or exclusion constraints or check constraints in the
schema, with the enforcement point named in DOMAIN.md.

## Consistency gate

Before this phase exits, the three artifacts are checked against each other
and against STORIES.md: every story's data needs exist in the ERD, every
endpoint serves a story or a named system need, every invariant in DOMAIN.md
has an enforcement point (schema constraint, API validation, or a test) —
an invariant enforced nowhere is a hope.

## Anti-patterns

- Designing the schema from the screens ("we need a column for this label").
- API endpoints that mirror table structure instead of user intent.
- Recording the model after implementation, as documentation theatre; the
  artifacts are inputs to tickets, or they are fiction.

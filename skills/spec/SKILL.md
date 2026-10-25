---
phase: plan
keywords: spec, specification, spesifikasi, technical plan, rencana teknis
name: spec
description: Synthesise the conversation and the upstream artifacts into one executable spec. Use when a feature or change is understood well enough to hand to implementers and needs a single document that settles what will be built.
---

# Spec

A spec is a synthesis, not a new interview. Everything it needs already
exists in the conversation and the upstream artifacts; the spec's job is to
gather it into one document a worker can execute without re-asking, and to
expose what is still missing.

## Process

1. **Gather by pointer.** Brief, PRD, stories, DESIGN.md, DOMAIN/ERD/API,
   ADRs. The spec cites them; it does not copy them. Copied content drifts.
   If a predecessor concepts brief exists, cite it as the intake source;
   do not re-interview for facts it already settles.
2. **Write SPEC.md** from `templates/spec.md`: problem and goal in a
   paragraph, the solution outline, per-area detail that cites story IDs,
   the alternatives considered and why each lost, a detailed implementation
   list naming every file with its rationale, the test seams (where behaviour
   will be verified, agreed before code exists), constraints inherited from
   CONSTRAINTS.md, and out-of-scope stated as plainly as scope.
3. **The open-questions stop.** After the draft, list every open question and
   assumption in one block. If any of them change behaviour, the spec does
   not proceed to tickets until the human answers or explicitly parks them.
   A spec that glides past its own unknowns manufactures rework.
4. **Assumptions block.** Every assumption the spec makes is listed under a
   visible "Assumptions I am making" heading. Assumptions discovered later
   to be wrong are how specs fail; assumptions written down are how they
   get caught in review.

## Rules

- The spec names its seams before implementation: the exact interfaces where
  tests will attach. "We will test it thoroughly" is not a seam.
- **Alternatives are mandatory.** Every spec records the alternatives
  considered and the specific reason each one lost (complexity, cost,
  performance, scalability, team familiarity, or another named reason). A
  spec that proposes a single path without showing what else was weighed
  fails the fresh-session bar below.
- **Detailed implementation lists every file.** One unified list names every
  file to be created, changed, or deleted, each with what changes and why.
  Include documentation, schema, config, proto, and test files. A file the
  plan touches but does not name is a file the implementer will invent.
- **No code in the spec.** The spec carries prose, short pseudocode, API
  shapes, and schemas. Implementation code belongs in the implementation
  phase, not in the document that is supposed to stay readable after the
  code has changed.
- **The fresh-session bar.** A spec passes when a competent engineer, or a
  fresh AI session unfamiliar with the codebase, can read it alone and
  understand the feature, the business motivation, the trade-offs, the
  major risks and how they are mitigated, and why the rejected alternatives
  lost. If that reader has to ask what the feature is for, what it costs,
  how long it takes, or how success will be checked, the spec is not done.
  Those eight questions (objective in plain words, how it is done today
  and its limits, what is new and why it should work, who cares and what
  difference success makes, risks and payoffs, cost, timeline, and the
  mid-term and final checks) are the Heilmeier catechism, and the spec
  answers each one somewhere, in its own sections, without inventing
  numbers it does not have.
- Size honesty: a spec that cannot be ticketed into independently
  verifiable slices is too big; send it back to be split, not forward to be
  suffered.
- The spec is the contract the review's spec axis will judge against. Write
  it like the reviewer is hostile and literal, because the good ones are.

## Anti-patterns

- Re-interviewing the human for facts already settled in the grill or the
  PRD; synthesis means using what exists.
- Burying decisions in prose where a ticket cannot cite them.
- A spec with no out-of-scope section; its scope will be defined by the
  first worker's imagination instead.
- A spec that proposes one path and never names what else was considered;
  the rejected alternatives are the guardrail that stops the next worker
  from re-litigating them, or from quietly choosing one of them.
- A spec that carries implementation code; code in the spec is the first
  thing to go stale, and it teaches the implementer to copy instead of
  to follow the plan.

<!-- Credit: Alternatives rule, every-file implementation list, no-code
rule, and fresh-session bar adapted from google/elephant-goldfish-model
(Apache-2.0, commit 3d0b34821ce88ad328b0c9bf0e06d7eb5f1cd669), skills
egm-draft and resources/document_standards/feature-spec-standard.md and
heilmeier-standard.md. Mechanisms rewritten into suite conventions; see
docs/audit/absorbed/2026-10-26-elephant-goldfish-model.md (A-011). -->

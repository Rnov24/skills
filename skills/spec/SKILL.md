---
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
2. **Write SPEC.md** from `templates/spec.md`: problem and goal in a
   paragraph, the solution outline, per-area detail that cites story IDs,
   the test seams (where behaviour will be verified, agreed before code
   exists), constraints inherited from CONSTRAINTS.md, and out-of-scope
   stated as plainly as scope.
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

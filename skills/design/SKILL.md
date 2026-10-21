---
name: design
description: The design phase — DESIGN.md constitution, user flows, keyframe approval, component discovery, and bounded council review. Use for any user-facing surface being built, redesigned, or given a new visual direction.
---

# Design

Design in this suite is a constitution, not a mood. The constitution is
DESIGN.md: a file of checkable rules that every worker reads and every
review enforces. Taste that lives only in a prompt dies with the session;
taste written as rules survives it.

## The constitution chain

1. **Inputs.** The PRD goal and PERSONAS.md. Design serves a product
   decision; a direction that ignores the personas is art practice, which is
   fine elsewhere.
2. **DESIGN.md** from `templates/design.md`: product character in one
   paragraph, then tokens (colour, type scale, spacing, radius, elevation),
   layout rules, component rules, motion rules, and the bans list. Every rule
   is written so a reviewer can point at a screen and say whether it holds.
   "Clean and modern" is not a rule. "No gradient backgrounds; elevation only
   via the three named shadows" is.
3. **USERFLOW.md** from `templates/userflow.md`, per persona: entry, happy
   path, failure paths, exit states. A screen that no flow reaches is scope
   nobody approved.
4. **Keyframes.** For a new direction or a redesign, produce reference
   keyframes (rendered images the human can judge, not code) for the
   load-bearing screens. Implementation does not start until the human
   approves the keyframes. Aesthetic bets are gated, always — overnight or
   not.

## One taste core

The suite carries a single anti-slop core, applied through DESIGN.md rather
than as a separate manifesto per project: no default purple gradients, no
generic card grids standing in for a layout idea, no lorem ipsum in judged
artifacts, typography chosen and scaled deliberately, motion that explains a
state change or is removed. Project character customises the core via
DESIGN.md; it does not replace it with a new manifesto per screen.

## Build discipline

- **Search before building.** Components, patterns, and interactions are
  looked up in the project's system and in known registries before anything
  custom is written. A custom component is a decision, and it cites why the
  existing ones failed.
- **Direction is dealt, not vibes.** When exploring directions, generate
  genuinely different candidates (different archetypes, not different accent
  colours) and judge them as images side by side.
- **Look-and-fix loop.** Built UI is screenshotted in a real browser and
  compared against the keyframe and DESIGN.md. Differences are findings,
  batched, and fixed in passes — never one screenshot per micro-fix.

## Council review, bounded

Design review runs as a small council: distinct lenses (typography/layout,
interaction, accessibility, product fit) review the same artifact and record
dissent rather than averaging into mush. Maximum two rounds. After round
two, unresolved disagreements go to the human with both positions in one
paragraph each. A council that cannot stop is a meeting, and meetings are
what this suite exists to replace.

## Anti-patterns

- Starting implementation and "designing in code" for a new direction.
- Fourteen taste documents that contradict each other by lunch.
- Reviewing a screenshot against adjectives instead of against DESIGN.md
  rules.
- Dark mode, extra themes, or extra directions nobody asked for, smuggled in
  as thoroughness.

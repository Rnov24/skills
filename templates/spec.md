# Spec: <feature or change>

- Upstream: brief <link> · PRD <link> · stories <IDs> · DESIGN <link> ·
  domain/ERD/API <links> · ADRs <links>

## Problem and goal
< One paragraph, synthesised from the brief. >

## Solution outline
< The shape of the answer in a few paragraphs. >

## Detail
< Per area. Each section cites the story IDs it realises. Behaviour is
  stated exactly once, here or upstream — never both. >

## Alternatives considered
< Each alternative weighed, and the specific reason it lost (complexity,
  cost, performance, scalability, team familiarity, or another named
  reason). A spec that proposes a single path without this section fails
  the fresh-session bar. >

## Detailed implementation
< One unified list. Every file to be created, changed, or deleted, each
  with what changes and why. Include documentation, schema, config,
  proto, and test files. No implementation code here; short pseudocode,
  API shapes, or schemas are allowed. >

## Test seams
< The interfaces where tests attach, agreed before code exists, per area. >

## Constraints inherited
< From CONSTRAINTS.md and the ADRs; cited, not restated. >

## Out of scope
< As explicit as the scope. >

## Assumptions I am making
< Every assumption, numbered. Reviewers attack this list first. >

## Open questions
< Answered, or parked with an owner and a trigger. A spec with behaviour-
  changing open questions does not proceed to tickets. >

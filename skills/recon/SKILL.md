---
phase: discover
keywords: recon, reverse engineer, clone, kompetitor, competitor teardown, feature matrix, tiru aplikasi, rebuild app
name: recon
description: Reverse-engineer an existing product into a buildable map — screen and flow inventory, inferred data model with evidence, and a weighted feature matrix. Use when the work starts from a product that already exists: a competitor to rebuild, a reference app to match, or a legacy system nobody documented.
---

# Recon

Recon turns "build me something like X" from a memory exercise into an
evidence exercise. The deliverable is a map the rest of the suite can build
from: what the product does, screen by screen and flow by flow, what data
it must hold, and which parts of it are not yours to rebuild. Downstream,
`model` turns the inferred model into a schema, `define-product` decides
what your version is, and `verify` scores parity against the feature
matrix this skill writes.

## The clean-room rules

These are not negotiable, and they are the gate this skill exits through:

- **Functionality and UX patterns only.** Recon studies what a product
  does and how a user moves through it. It never takes the product's
  source code, assets, logos, copy, or private APIs.
- **Public sources and the user's own account only.** Never log into an
  account that is not the user's, never bypass a paywall or a login,
  never read the product's bundles or network calls to copy endpoints.
  Public API documentation is fine.
- **Check the terms.** If the user's account terms forbid building a
  competing product from that account, say so and work from public
  sources only.
- **Screenshots are reference, never deliverable.** They live with the
  recon artifacts, feed design study and parity diffing, and never ship
  inside the product being built.

## Process

1. **Scope first, with a human yes.** Which product, which platform,
   which slice. "All of Notion" is not a project; "pages, blocks, and
   sharing" is. Default to the core loop, the one flow users pay for.
   Record who the resulting product is for; that answer decides later
   what parity even means.
2. **List the sources before reading any of them.** A sources table with
   a URL on every row, in order of value: help centre and docs, pricing
   page (what they gate is what matters), changelog, store listing,
   public walkthroughs, marketing site, the user's own account, public
   API docs.
3. **Inventory the screens.** One row per screen in RECON.md with a
   stable ID (S01, S02, ...): route or how you reach it, purpose, key
   components, and every state seen — empty, loading, filled, error,
   permission denied, mobile. An empty state you did not record is an
   empty state nobody will build.
4. **Trace the flows.** F01, F02, ...: a goal, the screens it passes
   through, the happy-path click count (it becomes the number to beat),
   and the edge cases visible along the way.
5. **Infer the data model, with evidence.** Entities, fields, and
   relationships, each carrying its evidence (screen IDs, form fields,
   help articles) and a confidence: high, medium, or guess. Guesses are
   marked as guesses; `model` inherits the confidence, not just the
   shape.
6. **Write the feature matrix.** FEATURES.csv from
   `templates/features.csv`: feature, area, priority (must / should /
   could), whether the original has it, the clone column starting at
   `no`, and notes. This file is the parity contract `verify` scores.
7. **Name what cannot be cloned.** Licensed content, the network and
   its users, data the product owns, partner deals, regulated licences.
   These land as `skip` rows with the reason written down, not as
   silent gaps.
8. **Size it honestly.** Screen, flow, and entity counts, the hard
   parts (realtime, sync, payments, integrations, offline), and a size:
   S (a weekend), M (weeks), L (a quarter), XL (rescope it). No
   promises of a perfect replica; parity is a number `verify` will
   report, not a vibe set here.

## Gate

The human approves scope, the out-of-scope list, and the size before any
downstream phase consumes the map. A recon map built on the wrong slice
is worse than none, because everything after it inherits the error.

## Anti-patterns

- Planning the rebuild from memory of the product instead of from the
  map. That is how half the product goes missing.
- Treating the inferred model as observed fact. Confidence labels exist
  so `model` knows what still needs checking.
- Recording features without states. The states are where rebuilds
  actually fail.
- Quietly dropping the cannot-clone list because it complicates the
  pitch. It is the part that keeps the project legal.

---

*Adapted from `replica-recon` in Jakeschincariol/replica-skill (MIT,
commit 77c9436fb3d18c3d58169efb8caf4fe906b0dc51) — gluttony run 8,
A-009. Full audit: `docs/audit/absorbed/2026-10-24-replica-skill.md`.*

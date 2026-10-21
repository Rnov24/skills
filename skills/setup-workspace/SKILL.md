---
phase: control
keywords: setup, repo setup, initialize, inisialisasi, constraints, tracker, scaffold, first time, repo baru
name: setup-workspace
description: One-time setup of a repository for the rnov24 workflow. Use when a repo will be worked on with this suite for the first time — artifact layout, tracker conventions, glossary, and the CONSTRAINTS.md quality floor.
---

# Setup workspace

Run once per repository, before the first real flow. Everything later assumes
this layout exists. Setup is a conversation with the human, not a silent
scaffold: the choices below are theirs, recorded once so no agent has to
re-ask or re-invent them.

## Establish

1. **Artifact layout.** Where product artifacts live (`docs/`), where ADRs
   live (`docs/adr/`), where tickets live (files in `docs/tickets/` or the
   project's tracker — pick one, write it down), and where run state lives
   (`.work/`, git-ignored).
2. **Tracker and labels.** If an external tracker is used, record how tickets
   map to it and the triage vocabulary: what the states are, what each state
   means, and who may move a ticket between them.
3. **Domain layout.** Single-context (one GLOSSARY.md, ADRs in one folder) or
   multi-context (a map file pointing at per-area glossaries). Default to
   single until the repo proves it needs more.
4. **CONSTRAINTS.md.** The quality floor, from `templates/constraints.md`.
   Every dimension gets a rule, a `Checked by` command, and a `Runs at`
   stage. A dimension without a command is a wish; either find the command
   or move the dimension to a human-checked list, honestly labelled.
5. **Branch and integration conventions.** Where accepted work lands, who
   integrates, and the guardrails: which git operations need a human grant
   (force-push, history rewrite, deleting branches others use).

## Rules

- Setup records decisions; it does not make them silently. Ask, then write.
- Every command written into CONSTRAINTS.md is run once during setup and must
  pass on the untouched repo, or be marked as aspirational with an owner and
  a ticket. A floor that starts red teaches everyone to ignore it.
- Re-run setup only when the repo's reality changes (new tracker, new area),
  and amend the files rather than regenerating them.

## Anti-patterns

- Copying another repo's constraints wholesale; the floor must describe this
  repo's checks or it describes nothing.
- Setting up the full layout for a throwaway experiment. Prototype work uses
  the `prototype` discipline inside `implement`, not a workspace.

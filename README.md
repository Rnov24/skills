# rnov24/skills

An artifact-based product, design, and engineering workflow for agent teams,
built and maintained by Rijal (rnov24).

Most skill collections hand an agent a pile of independent tricks. This suite
is one workflow. A main agent acts as **orchestrator**: it routes work through
phases, delegates bounded packets to subagents, and accepts nothing on a
worker's word — every claim is checked against an artifact, a diff, or a
command that was actually run.

Work moves as **artifacts**, not chat. A brief, a PRD, personas, user stories
with acceptance criteria, a DESIGN constitution, a domain model, an ERD, API
documentation, a spec, a ticket graph, worker packets and reports, and review
verdicts. Each artifact has an owner phase, a template, a consumer, and a gate.
An artifact is created only when its trigger fires — never "just in case".

## The workflow

```
setup-workspace
      |
  brief --> research --> grill --> define-product
                                        |  (BRIEF, RESEARCH, ADRs, GLOSSARY,
                                        |   PRD, PERSONAS, STORIES + AC)
                                        v
                              design ------ model
                              (DESIGN,      (DOMAIN, ERD,
                               USERFLOW)     API)
                                        |
                                        v
                              spec --> tickets --> implement --> review
                                        |              ^   |        |
                                        |              +- debug     v
                                        +------------ verify --> ship --> retro
```

Phases can be skipped when their trigger does not fire. A one-file bug fix
does not need a PRD. A new product does not get to skip one. The triggers are
written in `docs/ARTIFACTS.md`.

## Skills

**Control**
- `using-rnov-skills` — the router. Start here; it maps a situation to a flow.
- `orchestrate` — the orchestrator protocol: packets, report schema, dual
  review, rework loop, parallel safety, escalation.
- `setup-workspace` — one-time repo setup: artifact layout, tracker, glossary,
  `CONSTRAINTS.md` quality floor.

**Discover and define**
- `brief` — turn a raw request into an approved problem brief.
- `research` — answer a question from primary sources into a durable file.
- `recon` — reverse-engineer an existing product into a buildable map:
  screens, flows, inferred data model, and a weighted feature matrix.
- `grill` — stress-test a plan one decision at a time; decisions land as ADRs
  and glossary terms the moment they resolve.
- `define-product` — PRD, personas, and user stories with checkable
  acceptance criteria and traceability IDs.

**Design and model**
- `design` — the design constitution (DESIGN.md), user flows, keyframe gate,
  component discovery before custom builds, council review with a hard stop.
- `model` — domain model, ERD, and API documentation as first-class artifacts.

**Plan and build**
- `spec` — synthesise the conversation and artifacts into one spec a worker
  can execute without re-asking.
- `tickets` — break a spec into tracer-bullet tickets with blocking edges;
  the unblocked frontier is what may run in parallel.
- `implement` — execute tickets: worker protocol, test-first at agreed seams,
  thin verifiable slices.
- `debug` — diagnosis loop gated on a feedback command that already goes red.
- `mcp-builder` — design, implement, and evaluate Model Context Protocol
  servers in TypeScript or Python with strict tool naming and schemas.


**Assure and ship**
- `review` — two-axis review (standards and spec) plus blind doubt review for
  risky decisions; verdicts recorded against acceptance-criteria IDs.
- `verify` — evidence before claims; the constraint floor may only rise.
- `ship` — launch readiness, git discipline, PR, release grant.
- `retro` — close the loop: what the artifacts say actually happened, and what
  changes in the suite or the workspace.

**Suite maintenance**
- `adapt` — the adaptation loop (the wheel). Turns escapes, repeated
  findings, finder misses, and repeated corrections from real runs into
  evidence-backed changes to the suite, logged in `docs/ADAPTATIONS.md`.
- `gluttony` — slash command, `/gluttony <skill-repo-url>`. Absorbs an
  external skill repository into the suite: full audit, per-skill verdicts,
  adaptation into suite conventions, human gate before anything lands.

## Install

Global installs for Claude Code, Codex, and Antigravity (as an agy plugin)
via one installer: `python3 scripts/install.py --all`. Details, the safety
model, and uninstall live in `docs/INSTALL.md`.

## Repository layout

```
skills/<name>/SKILL.md     the skills themselves
docs/SKILL_INDEX.md        generated index of every skill (name, phase, keywords)
skills-index.json          the same index, machine-readable, for scripts/find_skill.py
scripts/                   generate_index.py, find_skill.py, install.py (suite tooling only; every runtime tool lives in its owning skill's scripts/ folder, so installed skills work standalone)
templates/                 one template per artifact
docs/WORKFLOW.md           the phase map, gates, and traceability rules
docs/ARTIFACTS.md          the artifact registry: triggers, owners, consumers
docs/SYNTHESIS.md          how this suite was designed and what it took from where
docs/audit/                the full pro/cons audit of 130+ predecessor skills
```

## Lineage

This suite is an original synthesis, distilled from an audit of the skill
collections it grew out of — Addy Osmani's agent-skills, Matt Pocock's skills,
the Superpowers collection, Atelier, and a shelf of design and product skills.
The audit, including what was rejected and why, lives in `docs/audit/`.
Credit and per-mechanism sources are listed in `docs/SYNTHESIS.md`.

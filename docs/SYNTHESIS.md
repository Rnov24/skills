# Synthesis: how this suite was designed

This suite was not written from a blank page. In October 2026 the full local
skill library — 121 installed skills plus the older workspace set, 175 entries
before deduplication — was audited skill by skill: purpose, concrete pros,
concrete cons, and a verdict of adopt, adapt, merge, or drop. The five audit
files live in `docs/audit/` and total roughly 2,100 lines. This document is
the design record of what the audit produced.

## Verdict totals

Across the five batches, 124 distinct skills were audited: 36 adopted in
substance, 55 adapted, 13 merged into a stronger neighbour, 17 dropped, and 3
marked out of scope for a development, design, and product suite (marketing
video and social content skills among them).

## What each predecessor did best — and where it stopped

**Addy Osmani's agent-skills** supplied the engineering gates: the hard
spec gate, the constraint floor that may only rise, the five-axis review with
a mutation check, and doubt-driven blind review. It has no product artifacts
at all, no traceability, and its routing is by task verb rather than artifact
state.

**Matt Pocock's skills** supplied the artifact discipline: specs synthesised
from conversation, tickets as a graph with blocking edges, glossary and ADR
capture at the moment a decision resolves, and two-axis review that never
lets one axis mask the other. It has no product front end, no design phase,
no ERD or API artifacts, and its delegation has no contract layer — no packet
or report schema, no per-ticket gate, no escalation semantics.

**Superpowers** supplied the strongest orchestration machinery: dispatch as
an artifact (a task-brief file in, a report file out), dual-verdict task
review against a diff package built from a base recorded before dispatch, and
a bounded rework loop with adjudication instead of silent discards. Its
review machinery is git-diff-based and code-only, and it has no artifact
chain beyond spec and plan.

**Atelier and the design shelf** supplied the design constitution chain —
brief to DESIGN.md to approved keyframes — and council review with a hard
two-round stop. The audit found at least fourteen copies of the same anti-slop
taste manifesto wearing different clothes; the suite keeps one taste core as
checkable rules inside DESIGN.md and drops the rest.

**The product shelf** was the thinnest. The existing PRD skill had a good
discovery gate and an honesty rule (unknowns are labelled TBD, never
invented), but emitted one monolithic document with no persona depth, no
checkable acceptance format, and no handoff to design, data, or API. The
product phase of this suite is largely new construction, built to the audit's
gap list. Kaggi's gate, grant, and journal mechanics — built for data-science
competitions — turned out to be the best model for human approval points and
were generalised into the suite's gate system.

## Decisions that shaped the suite

1. **One workflow, not a toolbox.** A router skill and a phase map replace
   per-skill discovery. Skills are phases and disciplines inside one pipeline.
2. **Artifact triggers over artifact habits.** Every document in the registry
   names the condition that justifies creating it. This is the direct answer
   to "workflow must be artifact-based, but not files for the sake of files".
3. **Traceability IDs from story to verdict.** No predecessor had the chain
   story → acceptance criterion → ticket → test → review verdict. It is the
   suite's backbone and its definition of done.
4. **One canonical packet, one canonical report, one verdict vocabulary.**
   Worker type (native subagent, external CLI agent, human) changes the
   transport, never the contract.
5. **Review is re-based from diffs to artifacts.** Code review keeps the diff
   package; product and design artifacts get the same dual-verdict treatment
   against their own gates.
6. **Every loop has a cap and every cap has an escalation.** Rework stops at
   five rounds, design council at two, debugging at three failed fixes. At
   the cap, a human rules, and the ruling is written down.

## What was deliberately left out

Writing-craft skills, teaching skills, exercise scaffolding, marketing and
social content production, competition-specific tooling, and tool-locked
setup skills (one vendor's hooks, one framework's test migrator) were dropped
or left as standalone tools. A suite that routes everything routes nothing.

## v1.4.0 note — design references

The design skill now carries a distilled reference shelf
(`skills/design/references/`): a checkable taste core and review rubric from
the impeccable lineage, and UX heuristics plus condensed direction, palette,
typography, and motion data from ui-ux-pro-max (MIT). The full upstream
databases were deliberately not vendored; the reference file records when to
consult them upstream instead.

## v1.10.0 note — awesome-design-md as reference shelf (A-005, EXPOSED)

Gluttony run 4 audited VoltAgent/awesome-design-md (MIT © VoltAgent,
commit 3b605329240ce735b510037cca322f1831fdd7f8): 84 DESIGN.md
extractions of real brand sites, 46,710 lines. At the human gate the
owner ruled the corpus be taken as a DESIGN.md reference rather than
digested into suite rules. It is therefore vendored verbatim at
`skills/design/references/brand-systems/` (with its licence, an index,
and recorded quality caveats), and `templates/design.md` adopts the
corpus's format — frontmatter token registry as the single source,
the `design.md lint` gate, Known Gaps and font-substitute honesty
sections, and a Responsive section. The rule and archetype merges
prepared during the audit were withdrawn under the ruling and remain
recorded, not in force, in the full audit:
`docs/audit/absorbed/2026-10-23-awesome-design-md.md`.

## v1.11.0 note — anti-slop fragments (A-006, EXPOSED)

Gluttony run 5 audited miqdadbadjuber/anti-slop (MIT © Miqdad
Badjuber, commit c93d08c7c94ab6f4db9ccc2e0f4f6e6121006d3e): a core
anti-slop rulebook (C-1..C-5, R-01..R-38) plus five satellite skills
and a contrast checker. The core is a second taste manifesto and was
rejected as a unit — the suite's taste core already holds that seat —
along with its UI and mobile satellites, its session-mode and install
machinery, its tier taxonomy, and its MCP wrapper. Six mechanisms the
suite lacked were merged as fragments, each credited where it landed:
dead-control and click-through evidence rules, the copy tell set with
its false-positive discipline, three accessibility specifics and the
contrast reference table, the comment-value test in `implement`, and
the contrast calculator at `scripts/contrast-check.py` (adapted, MIT,
credit in its header; its selftest recomputes the table in
ux-heuristics.md). The upstream em-dash ban contradicts copy.md and
was rejected. Full audit:
`docs/audit/absorbed/2026-10-23-anti-slop.md`.

## v1.12.0 note — Anthropic frontend-design calibration (A-007, EXPOSED)

Gluttony run 6 audited anthropics/skills target `skills/frontend-design`
(Apache-2.0 © Anthropic, commit dbd4588f9e1033efb41dad4bef2f7947c8993d44):
guidance for intentional visual design and non-templated UI. As a standalone
skill it is a guidance prompt that duplicates the suite's design phase and would
violate the "one taste core" rule. Its concrete mechanisms were extracted and
merged into `design`: the 5 AI design default cluster calibrations and the
single-word headline accent ban into `taste-core.md`, the two-pass default-ness
review gate into `skills/design/SKILL.md`'s preview block, the Chanel restraint
law (spend boldness in one place, keep the rest quiet) into build discipline, and
default anti-slop bans into `templates/design.md`. Full audit:
`docs/audit/absorbed/2026-10-23-anthropic-frontend-design.md`.

## v1.13.0 note — MCP builder & test runner tooling (A-008, EXPOSED)

Gluttony run 7 audited anthropics/skills targets `skills/mcp-builder` and
`skills/webapp-testing` (Apache-2.0 © Anthropic, commit dbd4588f9e1033efb41dad4bef2f7947c8993d44).
`mcp-builder` was absorbed as the 22nd suite skill (`skills/mcp-builder/`, phase: build),
supplying the 4-phase protocol for authoring and evaluating Model Context Protocol
servers: tool naming standards (`{service}_{action}_{resource}`), input/output
schemas (Zod/Pydantic), tool annotations (`readOnlyHint`, `destructiveHint`,
`idempotentHint`, `openWorldHint`), context pagination, and an objective 10-question
XML evaluation harness. `webapp-testing` was rejected as standalone prose (Playwright
boilerplate), but its `with_server.py` lifecycle tool was adapted into
`scripts/with-server.py` for deterministic local test execution. Full audit:
`docs/audit/absorbed/2026-10-23-anthropic-mcp-and-testing.md`.


## v1.14.0 note — replica-skill: recon, parity, review mining (A-009, EXPOSED)

Gluttony run 8 audited Jakeschincariol/replica-skill (MIT © Jake
Schincariol, commit 77c9436fb3d18c3d58169efb8caf4fe906b0dc51): eleven
skills for cloning an app clean-room style, with six stdlib Python tools
(upstream tests: 57, all passing at intake). One unit was absorbed new —
`replica-recon` became the suite's 23rd skill, `recon` (phase: discover),
with RECON.md and FEATURES.csv registered as artifacts. Four units merged
as mechanisms only: replica-architect's confidence carryover and
invariant-as-database-constraint rule into `model`; replica-diff's parity
scoring and colour-blind layout diff into `verify`, with `parity.py` and
`imgdiff.py` vendored to `scripts/`; replica-entrepreneur's
verbatim-and-linked review mining into `research`, with `reviews.py` and
its themes vendored; replica-brand's leftover-identity sweep into
`ship`'s readiness list, with `sweep.py` vendored. Six units were
rejected as duplicates of existing phases (design, build, backend, test,
launch, deploy), along with `contrast.py` (duplicates
`scripts/contrast-check.py`) and `listing.py` (store-listing lint, too
niche to vendor). Full audit:
`docs/audit/absorbed/2026-10-24-replica-skill.md`.

## v1.15.0 note — batch proving runs: A-005 through A-009 promoted

Five proving runs executed 2026-10-24 on the owner's instruction,
each on real work (the Linkstash project carried four of them;
Linktree's public surface carried the fifth). All five adaptations
promoted EXPOSED → ADAPTED; evidence in `docs/proving-runs/2026-10-24-a00{5,6,7,8,9}/`.
One writeback landed with the promotion: `skills/mcp-builder/SKILL.md`
now records the `mcp<2` pin (SDK 2.x renamed FastMCP), found when the
A-008 server failed at import on an unpinned install. Two format
findings were recorded for a future adapt cycle rather than fixed
mid-run: the design.md linter expects a `primary` colour where the
suite template says `accent`, and the template has no elevation
registry section.

## v1.15.1 note — fix-first tidy-up (A-010, ADAPTED)

At the owner's "rapihin biar mudah dipake", scoped to the fix-first
option: the seven runtime tools (`parity.py`, `imgdiff.py`,
`with-server.py`, `reviews.py`, `sweep.py`, `contrast-check.py`)
moved from repo-root `scripts/` into their owning skills' `scripts/`
folders, so installed skills work standalone — the dangling-reference
problem recorded since A-006. The installer now validates the suite
before installing (index regeneration, frontmatter, script
references, compilation), verifies installed copies afterwards,
validates the staged agy plugin, and offers `--check` for diagnosis
without installing. `templates/design.md` rules the A-005 findings
once: `primary` is the linter's alias of `accent`, and the registry
gains an `elevation` section.

## v1.16.0 note — Elephant-Goldfish, batch 1: brainstorm + draft (A-011, EXPOSED)

Gluttony run 9 audited google/elephant-goldfish-model (Apache-2.0 ©
Google LLC, commit 3d0b34821ce88ad328b0c9bf0e06d7eb5f1cd669):
seven skills, nine reviewer personas, five document standards. Batch 1
covers brainstorm and draft only; the review and bootstrap audits
landed in the same run and are verdicts for batch 2.

Neither upstream skill survived as a standalone skill: brainstorm
collides with `brief` in pipeline position and with `grill` in
interrogation posture, draft collides with `spec` in purpose and
content. Their mechanisms were merged instead. Into `spec`: the
mandatory Alternatives section with a rejection reason per
alternative, the Detailed Implementation list naming every file with
its rationale, the no-code rule, and the fresh-session bar (a reader
unfamiliar with the codebase must understand the feature, its
motivation, its trade-offs and risks, and why the alternatives lost),
with the Heilmeier eight questions as the check for what "understand"
means. Into `grill`: the six-lens parallel swarm as an optional
delegated pass, the critique-first rule with a counter-argument per
strategy, and the readiness gate before any reviewer is spawned.
Into `orchestrate`: the synthesizer step that dedups parallel
findings, groups them by suite severity, and writes the consolidated
report before notifying. Into `brief`: the readiness rule that no
reviewer is spawned before the problem is anchored. Rejected from
batch 1: the banned-adjective and banned-apology lists (style
policing, no mechanical check), the RFC publish and SITEMAP steps,
the per-section approval gates (the suite's human gates are the
brief, the PRD, keyframes, and grants), the save-location gate, and
the silent no-code enforcement with its no-summary and no-meta-talk
rules, which contradict the suite's evidence and ledger discipline.
The no-code mechanism itself survives in `spec`; only its silent
enforcement was rejected. Full audit:
`docs/audit/absorbed/2026-10-26-elephant-goldfish-model.md`.

Batch 2 (same run, same commit, at the owner's instruction to
wait for it before any gate) merges the review side and the
codebase side. Into `review`: the Goldfish protocol as five
stages over a semantic split of the document, fresh-context
reviewers only, one re-audit per stage, consolidated findings
feeding the suite's per-AC and unit verdicts, plus CONTEST vs
PROPOSE FIX triage and the three bars (context sufficiency as a
prerequisite fail, zero-assumption re-implementation, zero-decision
readiness). Into `orchestrate`: re-derive line ranges from the
semantic target on every re-audit, and name the
synthesizer-vs-direct dispatch choice in the packet. Into
`implement`: the same triage on the receiving side, edits deferred
until every finding is decided. Into `recon`: bootstrap mode for
the team's own undocumented tree, with sentinel markers as the
mechanical preservation rule. Into `verify`: the drift sweep,
differences-only, with ADR checks and a registered report
location. Rejected from batch 2: loop-until-zero findings (the
suite's five-round cap governs), the memory checklist for triage
decisions, the shortname resolver, the preset modal system, and
the syntax-tree claim for drift detection, which no mechanism in
the skill file supports.

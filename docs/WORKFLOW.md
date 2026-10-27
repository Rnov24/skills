# Workflow

The suite is a pipeline of phases. Each phase consumes artifacts, produces
artifacts, and ends at a gate. The orchestrator (see the `orchestrate` skill)
owns movement between phases; phase skills own the work inside them.

## Principles

1. **Artifacts over chat.** If a decision, requirement, or verdict matters, it
   lives in a file with an owner and a template. Chat is for reaching the
   artifact, never for storing it.
2. **Triggers, not habit.** Every artifact has a creation trigger in
   `ARTIFACTS.md`. No trigger, no file. This is the rule that keeps the
   workflow from becoming document theatre.
3. **The worker's report is never acceptance evidence.** The orchestrator
   reviews the diff or the artifact itself and runs the checks. A report only
   tells the reviewer where to look.
4. **Decisions stay with the human, facts go to workers.** Research,
   extraction, and verification are delegable. Scope, trade-offs, and grants
   are not.
5. **Every loop is bounded.** Reviews, rework, and design passes all have a
   hard round cap and an escalation path. Nothing iterates forever.
6. **Traceability is cheap and mandatory.** IDs link story → acceptance
   criterion → spec section → ticket → test → review verdict. If a link is
   missing, the chain — and the claim built on it — is incomplete.

## Beyond web

The pipeline is a decision-and-evidence pipeline, not a web pipeline. The
entry layer is domain-neutral (the two paths, fix, and the audits name no
technology). The phase skills are software-flavoured by history (`model`
assumes an ERD and an API, `implement` assumes code); outside software, those
phases are skipped with a recorded reason, per the router's existing skipping
rule, and the gates that do not assume software — human approvals, review,
verify — still apply. For example, a non-software deliverable (an analysis
report, a video series) enters through `/rnov-new` or `/rnov-improve`, runs
brief → grill → define → spec → tickets → review → verify → ship, and skips
design, model, and implement-as-code with reasons recorded. The router's
Domain question is what makes the skip explicit at classification time
instead of discovered mid-run. This makes the entry and the routing
domain-neutral; it does not rewrite the phase skills for other domains. A
phase skill that cannot serve a domain is skipped, not forced.

## Elephant-Goldfish flow

The suite's phases already run the Elephant-Goldfish shape, and the
names are now used for it. The Elephant is the deep-context work:
grill (with an optional lens swarm) and spec, where every design
judgment is forced into the document before code exists. The Goldfish
is the fresh-context check: a reviewer who receives only the spec and
the files it references, never the conversation that produced them,
and must be able to understand the feature from that alone. Design is
the new code — when the code becomes too large for a human to review
in full, the spec is the artifact a human can still stand behind.
The Goldfish protocol itself (comprehension, critic, and readiness
passes over a spec) lives in `review`; this workflow only states the
shape so the phases are read as one flow instead of separate tricks.

## Phases and gates

For entry points and standard flows, see [`docs/ENTRY.md`](ENTRY.md).

| Phase | Skill | Main artifacts | Gate to exit |
|---|---|---|---|
| Setup | `setup-workspace` | layout, CONSTRAINTS.md, GLOSSARY.md | layout exists, floor checks run green once |
| Brief | `brief` | BRIEF.md | human approves the problem statement and scope |
| Research | `research` | RESEARCH-<topic>.md | claims cite primary sources; open questions listed |
| Grill | `grill` | ADR-*.md, GLOSSARY.md updates | decision frontier empty or explicitly parked |
| Define | `define-product` | PRD.md, PERSONAS.md, STORIES.md | human approves PRD; every story has checkable AC |
| Design | `design` | DESIGN.md, USERFLOW.md, keyframes | human approves keyframes against DESIGN.md |
| Model | `model` | DOMAIN.md, ERD.md, API.md | model reviewed against stories; contracts consistent |
| Spec | `spec` | SPEC.md | spec names its seams; alternatives recorded with rejection reasons; every file listed with rationale; open questions answered or parked; passes the fresh-session bar |
| Tickets | `tickets` | tickets/*.md with blocking edges | every spec section covered; frontier computable |
| Implement | `implement` (+ `debug` when stuck) | code, PACKET/REPORT files per ticket | per-ticket dual review passes |
| Review | `review` | REVIEW.md verdicts per AC ID | no unresolved Critical; rework loop within cap; specs pass the Goldfish protocol before implementation |
| Verify | `verify` | fresh command output | all CONSTRAINTS checks green at the raised floor |
| Ship | `ship` | PR, release notes | human grant for irreversible actions |
| Retro | `retro` | RETRO.md, suite/workspace changes | lessons filed where the next run will read them |

## Traceability

- Stories are `US-01`, `US-02`, ... in STORIES.md.
- Acceptance criteria are `AC-01.1`, `AC-01.2`, ... under their story.
- SPEC.md sections cite the story IDs they realise.
- Tickets cite the spec sections and AC IDs they cover.
- Tests cite the AC ID they prove (in the test name or a comment).
- REVIEW.md records one verdict per AC ID: PASS, FAIL, or PARKED with a ruling.

A claim of "done" for a story is exactly the set of its AC verdicts. Nothing
else counts.

## Human gates and grants

Four moments always belong to the human: approving the brief, approving the
PRD, approving design keyframes, and granting irreversible actions (deploy,
submit, delete, send). A grant is explicit, one-time, and names the action and
its allowance ("deploy this build to production"), never a blanket "go ahead".
Agents prepare everything up to the gate so the human's decision is the only
remaining work.

## Skipping phases

Skipping is normal and expected. The orchestrator records skipped phases in
the run ledger with the reason ("bug fix with a red test: brief, PRD, design
not triggered"). What is not allowed is skipping silently, or skipping a gate
whose trigger fired.

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

## Phases and gates

| Phase | Skill | Main artifacts | Gate to exit |
|---|---|---|---|
| Setup | `setup-workspace` | layout, CONSTRAINTS.md, GLOSSARY.md | layout exists, floor checks run green once |
| Brief | `brief` | BRIEF.md | human approves the problem statement and scope |
| Research | `research` | RESEARCH-<topic>.md | claims cite primary sources; open questions listed |
| Grill | `grill` | ADR-*.md, GLOSSARY.md updates | decision frontier empty or explicitly parked |
| Define | `define-product` | PRD.md, PERSONAS.md, STORIES.md | human approves PRD; every story has checkable AC |
| Design | `design` | DESIGN.md, USERFLOW.md, keyframes | human approves keyframes against DESIGN.md |
| Model | `model` | DOMAIN.md, ERD.md, API.md | model reviewed against stories; contracts consistent |
| Spec | `spec` | SPEC.md | spec names its seams; open questions answered or parked |
| Tickets | `tickets` | tickets/*.md with blocking edges | every spec section covered; frontier computable |
| Implement | `implement` (+ `debug` when stuck) | code, PACKET/REPORT files per ticket | per-ticket dual review passes |
| Review | `review` | REVIEW.md verdicts per AC ID | no unresolved Critical; rework loop within cap |
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

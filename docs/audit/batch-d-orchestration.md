# Audit Batch D — Orchestration, Planning & Execution Discipline

Scope: the superpowers set in `~/workspace/skills/` (15 skills, reached via symlinks into `~/workspace/skills/superpowers/skills/`), plus `local-agy-delegation`, `local-superpowers` (bundle note), `local-brain-grade`, and the `~/workspace/skills/agy-delegation` + `~/workspace/skills/brain-grade` duplicates.

Duplicate findings, checked by diff before auditing:

- **Superpowers copies are identical.** All 15 SKILL.md files under `~/workspace/custom-skills/local-superpowers/skills/` are byte-identical to the upstream copies in `~/workspace/skills/superpowers/skills/`. Audit each skill once; there is no local evolution to preserve.
- **`local-superpowers` itself is not a real bundle index.** Its root SKILL.md is an 8-line "Recovered skill notes" stub with a connector reminder. It carries no routing, no inventory, no version info. Treat it as a container directory only.
- **agy-delegation: the `local-` copy has the better content, the `skills/` copy has the better packaging.** `~/workspace/custom-skills/local-agy-delegation/SKILL.md` (137 lines) is newer: wrapper v2, mandatory `--dry-run`, canonical packet template, utilization playbook with measured waste baseline (126 runs, 20% empty), routing table, JSON usage telemetry. But it has **no YAML frontmatter** (starts directly with `# agy-delegation`), so skill discovery by description cannot fire. The `~/workspace/skills/agy-delegation/SKILL.md` (122 lines) has proper `name`/`description` frontmatter but older v1 content. Merge: local content + the frontmatter from the older copy.
- **brain-grade: the original is the better copy.** `~/workspace/skills/brain-grade/SKILL.md` (321 lines; the path is a symlink to `~/skills/brain-grade`) carries full frontmatter (license, author, version) and both collector scripts. `local-brain-grade` (315 lines) strips the frontmatter and appends a generic connector note, adding nothing of substance.

Verdict tally for this batch: **ADOPT 7 · ADAPT 9 · DROP 1** (17 skills audited).

---

## 1. subagent-driven-development (superpowers) — ADOPT

**Purpose:** Execute an implementation plan by dispatching a fresh implementer subagent per task, with a spec+quality task review after each and a whole-branch review at the end.

**Pros**
- The most complete delegation protocol in the batch: dispatch is a constructed artifact, not a chat message — a task-brief file extracted from the plan (single source of requirements, exact values live only there), plus where the task fits, interfaces/decisions from earlier tasks, pre-resolved ambiguities, and a named report file with a report contract. The implementer returns only status, commits, a one-line test summary, and concerns; the full report is a file, so the controller's context stays clean.
- Two-stage review done right: the reviewer receives the brief, the report, and a **review package file** (commit list + stat + full diff) generated from a BASE recorded before dispatch — with an explicit warning that `HEAD~1` silently truncates multi-commit tasks. Both verdicts (spec compliance AND code quality) are mandatory; "⚠️ Cannot verify from diff" items must be resolved by the controller personally before the task closes.
- A real rework loop with a breaker: max 5 fix rounds; rounds 1–3 resume the original implementer, rounds 4–5 switch to a fresh implementer on a more capable model; re-reviews are scoped to the fix diff and verdict each finding ADDRESSED / NOT ADDRESSED. At the cap the controller adjudicates — park with a ledgered ruling, or rule on load-bearing findings — and **silent discards are forbidden**. Minor findings never enter the loop; they are ledgered and triaged at the final review.
- Durable state: a per-plan workspace and `progress.md` ledger whose first line names the plan, designed explicitly to survive context compaction ("controllers that lost their place have re-dispatched entire completed task sequences — the single most expensive failure observed"). Pre-flight conflict scan (task-pair interface table + per-task self-consistency) before Task 1, model-selection rules per role (including "always specify the model explicitly" and "turn count beats token price"), and an exhaustive "Rulings I made" list surfaced to the human at finish.
- Anti-pre-judging rule for reviewers: never instruct a reviewer to ignore/soften a finding ("do not flag", "at most Minor" in your own prompt means stop) — adjudication happens in the loop, not in the prompt.

**Cons**
- Git/commit-centric throughout: the review package, BASE/HEAD ranges, and ledger completion lines all assume every task ends in commits on a branch. It does not transfer directly to non-code artifacts (PRD, DESIGN, ERD) without redefining what the "diff" and "package" are.
- Heavy per-task cost: one fresh implementer + one reviewer + possible re-reviews per task. It acknowledges the cost but offers no budget cap or quota check; small plans can cost more in orchestration than in work.
- "Continuous execution / rulings not stalls" deliberately removes human checkpoints between tasks. That is a posture choice that fits autonomous runs but conflicts with artifact-approval workflows where the human wants to approve a PRD or DESIGN before downstream work starts.
- Depends on its own helper scripts (`sdd-workspace`, `task-brief`, `review-package`) and template files; porting the protocol to another harness means porting the scripts too.

## 2. agy-delegation (local copy) — ADOPT

**Purpose:** Delegate bounded implementation work to the headless agy worker on the user's Google quota, with the main agent as planner and independent reviewer.

**Pros**
- Clean role separation stated as law: driver plans and reviews, worker implements, and **"the worker's report is never acceptance evidence — verify the diff and run the checks yourself."** The after-run protocol is concrete: read `result.txt` (empty result + exit 0 = failed run), review the actual `git diff`, run the project's checks yourself, then accept / follow-up packet / discard.
- Packet design is the best in the batch for a single dispatch: a byte-identical stable header (standing instructions, permission posture, report format — which is also what makes prompt caching work), one coherent bounded change ("if you catch yourself writing 'and also', split it"), and a mandatory report footer (branch, commit hash, files changed, checks run with results, anything left undone).
- Operational realism no other skill matches: session resume by registry instead of wasteful fresh re-analysis, a routing playbook by task type (effort/model/timeout per class), a measured waste baseline (20% empty results pre-v2) with named causes, failure-mode catalogue (empty result exit 0, missing exit-code file, stale resumed sessions, same-repo registry races on parallel runs), preflight order (`agy-stats.sh` → `/usage` → `--dry-run` always), and quota routing across model families when a window runs dry.
- Structured reporting is supported properly: `--report-schema` JSON-schema reports for recurring report types, plus automatic `usage.txt` telemetry (including cache-read ratio) extracted from the JSON envelope — verification that caching/resume actually worked, not just hope.

**Cons**
- Entirely specific to one worker (agy), one wrapper script, one machine's paths and quota windows. The transferable protocol (packet shape, resume, routing, review) is entangled with agy flags and model IDs that churn per release.
- No formal acceptance verdict: the review protocol ends in a human-style judgment (accept / fix packet / discard) but defines no verdict record, no severity taxonomy, and no cap on follow-up fix packets — the rework loop is unbounded and unlogged compared to SDD's 5-round breaker.
- As noted above, the better copy lost its YAML frontmatter, so as packaged it cannot be discovered by description matching.
- Parallel guidance is thin and mostly a warning (registry race on the same repo); it does not define per-worker worktree isolation for parallel writes.

## 3. writing-plans (superpowers) — ADOPT

**Purpose:** Turn a spec into a bite-sized implementation plan whose tasks carry every decision an implementer who has never seen the codebase cannot make alone.

**Pros**
- Artifact discipline the rnov24 suite needs: every plan starts with Goal, Architecture, Tech Stack, a **Spec path** (the plan argues from the spec, so the spec travels with it), **Global Constraints** copied verbatim from the spec, and a **Review Focus** section — the five uncovered input classes/failure modes most likely to bite a real user, each pinned to a test in the owning task. Spec silence is explicitly not permission for an input to break the program.
- Task structure is built for isolated subagent execution: Files (create/modify/test with exact paths), and **Interfaces — Consumes / Produces with exact signatures** — which is exactly how a fresh implementer learns what neighbouring tasks use without reading the whole plan.
- Right-sizing and proportion rules with a self-review that catches both failure directions: steps that decide nothing ("handle edge cases", "TBD") and plans that transcribe the whole program (plan longer than the code = replace bodies with signatures + test assertions). Also spec-coverage and type-consistency checks across tasks.
- Ends with an explicit execution-method handoff (subagent-driven vs native inline, with a recommendation and its reason), so planning and execution stay separate decisions.

**Cons**
- Assumes the unit of work is always code with tests and commits; there is no equivalent task template for producing/reviewing non-code artifacts (persona, userflow, ERD, API docs), which the rnov24 workflow explicitly wants.
- The mandatory header and per-step Expected-output style can bloat small plans despite the proportion check; the check is self-applied, with no external gate.
- Plan location and naming are superpowers-conventional (`docs/superpowers/plans/…`); adopting means remapping to the rnov24 artifact layout.

## 4. verification-before-completion (superpowers) — ADOPT

**Purpose:** Forbid any completion/success claim that is not backed by a fresh verification command run and read in the same message.

**Pros**
- A compact, portable gate function: IDENTIFY the proving command → RUN it fresh and full → READ output and exit code → VERIFY against the claim → only then claim, with evidence. Easy to embed as the final step of any worker report contract or orchestrator acceptance check.
- Names the exact failure it prevents in delegation: "Agent completed — requires VCS diff showing changes; agent reports 'success' is not sufficient", and "Requirements met — requires a line-by-line checklist, tests passing is not sufficient." This is the acceptance-evidence rule the whole suite needs.
- Claim-by-claim evidence table (tests, linter, build, bug fixed, regression red-green) doubles as a checklist for what a report must attach.

**Cons**
- Pure prohibition form: it says what never counts as evidence but defines no positive evidence format (no report fields, no artifact to file the output in), so each adopting skill must invent its own.
- "Fresh, in this message" is calibrated for a single session; in a delegated pipeline the orchestrator must translate it into "the verifier ran it after the worker's last change", which the skill does not spell out.
- No severity or partial-result handling: a suite with one unrelated pre-existing failure has no defined verdict under this skill alone.

## 5. systematic-debugging (superpowers) — ADOPT

**Purpose:** Force root-cause investigation (four phases) before any fix is proposed, for any bug, test failure, or unexpected behaviour.

**Pros**
- Phase discipline is concrete and checkable: read errors fully, reproduce consistently, check recent changes, instrument component boundaries in multi-layer systems, trace data flow backward to the source — then pattern analysis against working examples, then a single written hypothesis tested with the smallest change, then one fix at a time with a failing test first.
- Contains the batch's clearest **escalation rule for failed rework**: if 3+ fixes have failed, stop — that pattern means the architecture is wrong, and the next step is a discussion with the human, not fix #4. This pairs directly with SDD's fix-loop breaker.
- Red-flag and rationalization tables are written from observed failure behaviour ("just try changing X", "one more fix attempt" after 2+ failures), making it usable as a worker-packet constraint for debugging delegations.

**Cons**
- Solo-operator framing: no guidance on delegating a debugging task (what evidence a debugging subagent must return, how its hypothesis log should be formatted), so an orchestrator must wrap it.
- The process is linear and can be slow for trivial, already-understood failures; its own answer is "process is fast for simple bugs", which is asserted rather than tiered (no fast path definition).
- Supporting techniques live in sibling files (root-cause-tracing, defense-in-depth, condition-based-waiting) that must travel with it.

## 6. using-git-worktrees (superpowers) — ADOPT

**Purpose:** Guarantee feature work happens in an isolated workspace — detect existing isolation, prefer the platform's native worktree tool, fall back to manual git worktrees safely.

**Pros**
- Detection before creation, with the two traps named: harness-created isolation you cannot see by eyeballing, and the submodule false positive for `GIT_DIR != GIT_COMMON`. Prevents the phantom-state mistake of running `git worktree add` when a native tool owns placement/branching/cleanup.
- Safety checks that matter for parallel delegated work: verify the worktree directory is git-ignored before creating anything (an unignored `.worktrees/` commits the whole tree), consent before creating, clean-baseline test run so later failures are attributable.
- Graceful degradation: sandbox denial → tell the user and work in place, rather than failing the task.

**Cons**
- Setup-only: it creates isolation but says nothing about assigning worktrees per parallel worker, naming conventions across plans, or reconciling worktree state with a progress ledger (SDD assumes it, neither skill specifies the mapping).
- Baseline-failure handling stops at "report and ask"; no rule for proceeding on a known-red baseline with the failures recorded as pre-existing.

## 7. finishing-a-development-branch (superpowers) — ADOPT

**Purpose:** Close a finished branch safely: verify the full suite on the actual tree, detect the environment, present the integration menu, execute the choice, clean up only what you own.

**Pros**
- Integration is treated as the human's decision, with a fixed menu (merge locally / push + PR / keep as-is) and environment-aware variants (detached HEAD loses the merge option). Discard exists only as an explicit human request gated on typing `discard`, with the full deletion list shown first.
- Merge-safety sequencing is correct and specific: merge first, verify tests on the merged result, only then remove worktree and branch; a red merged result stops everything with nothing pushed. Worktree cleanup is provenance-based — only remove worktrees under `.worktrees/`/`worktrees/`, and a refused removal (files exist nowhere else) escalates to the human with the file list instead of `--force`.
- Rationalization table covers the real temptations (force-push on rejection, cleaning "stale-looking" foreign worktrees, assuming the base branch).

**Cons**
- End-of-pipe only: it assumes reviews already happened elsewhere; its test gate is a full-suite run, not an acceptance check against spec/acceptance criteria.
- Menu and cleanup prose is long and exact-wording-oriented ("present the menu exactly as written"), which fits superpowers' voice but is brittle to transplant into a differently-styled suite.

## 8. brainstorming (superpowers) — ADAPT

**Purpose:** Turn an idea into an approved design before any implementation, via collaborative dialogue scaled to the size of the work.

**Pros**
- Triage before process: classify the request as **spike / bounded / architectural**, announce the classification so the human can override, and scale the artifact to the path (2–3 sentence probe + nod; short in-chat design + explicit yes; full written spec + plan). The ratchet is one-way — hidden complexity upgrades the path mid-task, nothing downgrades.
- The approval gate is precise about a subtle failure: approval of one stage is not approval of the next ("conversational design approval only permits writing the spec; written-spec approval only permits invoking writing-plans") — exactly the discipline an artifact-based workflow (PRD → DESIGN → plan) needs between artifacts.
- Intent handling is good: write back a short understanding note separating what the user said from assumptions, invite correction, and carry that note into the design artifact. Architectural path adds spec self-review (placeholder scan, internal consistency, scope, ambiguity) and decomposition of oversized requests into sub-projects, each with its own spec → plan → implementation cycle.

**Cons**
- One-question-at-a-time, section-by-section approval is slow and chat-bound; it assumes a present, responsive human and offers no asynchronous/artifact-review mode (leave the spec, collect comments later).
- The hard-gate is absolute — no implementation action at all before the path's approvals — which conflicts with trusted autonomous delegation for routine work; the rnov24 suite will need risk-tiered gates rather than one gate for everything.
- The visual-companion machinery (browser mockup offers, just-in-time rules) is harness-specific bulk that does not transfer to a headless orchestrator context.

## 9. executing-plans (superpowers) — ADAPT

**Purpose:** Execute a plan inline in the current session (no per-task subagents), keeping the ledger, TDD, and a single final whole-branch review as the compensating controls.

**Pros**
- Honest cost model: states plainly what inline execution gives up (fresh context and a second pair of eyes per task) and what replaces each (brief-as-spec, ledger-as-memory, TDD as per-task gate, final reviewer). Shares the exact workspace/ledger format with SDD, so a plan can switch executors mid-flight and resume from the same ledger.
- A real **completion contract** per task, enforced by tooling: every named test exists and ran, every `Expected:` line was compared against real output, every deviation has a `Ruling:` line — and the `task-done` script runs the tests and only writes the completion line if they pass. Bookkeeping is required to ride along with the work call, never as its own call.
- Final-review findings are re-graded by effect on a real user, not by the reviewer's label or the spec's silence ("the label graded the spec's silence; grade what the person gets"), then exactly one fix pass, each fix proven RED→GREEN with a green suite; no re-review dispatch, with the reasoning stated.

**Cons**
- Deliberately weaker assurance than SDD (one review, at the end, possibly a self-review when no subagent tool exists — the skill itself admits this is weaker and punts the sufficiency decision to the human). As a default mode for the rnov24 suite it under-serves the "review hasil yang baik" requirement; it is a budget mode, not the standard.
- Large overlap with SDD (setup, ledger, rulings, four stop conditions, finish ritual are near-duplicated); adopting both means maintaining two copies of the same protocol that can drift.
- The one-fix-pass/no-second-review rule for final findings is a cost decision presented as principle; for high-risk changes it removes the scoped re-review that SDD correctly insists on.

## 10. dispatching-parallel-agents (superpowers) — ADAPT

**Purpose:** Fan independent problem domains out to parallel subagents with isolated context, one agent per domain, then review and integrate the results.

**Pros**
- The independence test is the valuable core: parallelize only when failures/domains are independent, understandable without each other's context, and free of shared state — with the negative cases spelled out (related failures, exploratory debugging, shared resources). Grouping failures by domain before dispatch is a concrete, reusable step.
- Prompt structure guidance is sound and minimal: focused scope, self-contained context (paste the actual error messages and test names), explicit constraints ("do NOT change production code"), and a specific expected output (summary of root cause and changes).
- Integration step exists and is ordered: read each summary, check for conflicts, run the full suite, spot-check because "agents can make systematic errors".

**Cons**
- Thinnest protocol in the batch: no isolation mechanism for parallel **writers** (no worktree-per-agent, agents in its own example all fix files in one tree), no report schema beyond "summary", no per-agent verification gate, no failure/timeout handling, no cap on fan-out.
- Examples are debugging-only (failing test files); it gives no guidance for parallelizing planned feature work, design exploration, or review — the cases an orchestrator fans out most.
- "Dispatch all in the same response" is a harness-specific mechanic stated as the parallelism rule; the underlying principle (independent dispatch, single integration point) needs restating per platform.

## 11. test-driven-development (superpowers) — ADAPT

**Purpose:** Enforce test-first development: write a failing test, watch it fail for the right reason, write minimal code to pass, refactor — with no production code before a failing test.

**Pros**
- The RED-verification step is the part most TDD descriptions skip and this one mandates: a test that passes immediately, or fails on a typo, proves nothing; the failure reason must match the missing behaviour. The reviewer-facing corollary — a green run of your one test file is **not** a green suite, run the project's full suite, and any red test you saw and didn't report is "a report falsified by omission" — is a strong report-honesty rule for delegated work.
- Good-test criteria are operational (one behaviour, name describes behaviour, assert on real behaviour not mock behaviour, name the production change that would make the test fail) via the linked `writing-good-tests.md`.
- Worked bug-fix example and a verification checklist make it directly insertable into implementer packets as the per-task quality gate (both SDD and executing-plans lean on it).

**Cons**
- The absolutist enforcement ("write code before the test? Delete it. Don't keep it as reference, don't look at it") is calibrated for a solo agent writing code live; applied literally to delegated/generated work it destroys reviewable output instead of flagging a process violation, and it fits UI/design/docs work poorly — a large part of the rnov24 scope.
- No proportionality: prototypes and generated/config code are exceptions only "with the human's permission", leaving the orchestrator no standing rule for when a lighter gate (characterization tests, screenshot/visual checks) is acceptable.
- Long rationalization/red-flag apparatus duplicates the same persuasion pattern as its sibling skills; transplanting all of it inflates the suite's token budget.

## 12. requesting-code-review (superpowers) — ADAPT

**Purpose:** Dispatch a fresh code-reviewer subagent with precisely crafted context (never session history) after tasks/features and before merge.

**Pros**
- Context-crafting principle is right and quotable: the reviewer gets a description, the plan/requirements, and a BASE..HEAD range — evaluation lives in the reviewer's context, only findings return. Its rationalization table also makes the orchestrator's case: reviewing the diff inline burns the coordinator's context that should be spent driving work.
- Feedback triage is defined (Critical now, Important before proceeding, Minor later, push back with technical reasoning when the reviewer is wrong), matching the severity flow SDD's loop consumes.

**Cons**
- As a standalone skill it is largely a pointer: the actual reviewer instructions live in the external `code-reviewer.md` template, and SDD already embeds a stricter version of the same dispatch (diff-as-file, dual verdicts, scoped re-review). Adopting both creates two review protocols; the rnov24 suite should keep one.
- Its SHA advice (`git rev-parse HEAD~1`) directly contradicts SDD's hard-won rule to use the BASE recorded before dispatch — evidence the two skills were not written against each other. Anyone merging them must resolve this in SDD's favour.
- No verdict format of its own (the example shows free-form Strengths/Issues/Assessment), so findings arrive in whatever shape the reviewer chooses.

## 13. receiving-code-review (superpowers) — ADAPT

**Purpose:** Handle incoming review feedback with technical verification instead of performative agreement or blind implementation.

**Pros**
- The response pattern is a genuine safeguard for an orchestrator consuming reviewer output: READ fully → restate/UNDERSTAND → VERIFY against the codebase → EVALUATE for this codebase → respond technically → implement one item at a time, testing each. "If any item is unclear, stop and clarify all items before implementing any" prevents the common partial-understanding failure.
- Source-aware scepticism: external-reviewer suggestions get five concrete checks (correct here? breaks anything? why does current code exist? all platforms? reviewer missing context?), plus a YAGNI check that greps for actual usage before "implementing properly" — a good brake on reviewer-driven scope creep.
- Pushback is legitimized with a method (technical reasoning, working tests/code as evidence, escalate architectural conflicts to the human), and correcting your own wrong pushback is modelled factually without grovelling.

**Cons**
- A meaningful slice is one project's social style guide — the blanket ban on any gratitude expression ("Thanks for [anything]") and on phrases like "Great point!" is superpowers-house voice, not a transferable correctness rule; transplanting it verbatim would fight the rnov24 suite's own tone rules.
- Written for a human↔agent review relationship on GitHub PRs; it does not cover the orchestrator-specific case of adjudicating between two agents' conflicting findings (SDD's ruling mechanism covers that better).
- No record-keeping: what was accepted/rejected and why is not written to any artifact, so decisions made here evaporate unless another skill's ledger catches them.

## 14. using-superpowers (superpowers) — ADAPT

**Purpose:** Bootstrap skill routing: check for applicable skills before any response or action, process skills first, then implementation skills.

**Pros**
- The priority rule is the keepable core: process skills (brainstorming, systematic-debugging) set the approach before implementation skills run — a simple router an orchestrator can reuse to order its own workflow stages (spec before plan before dispatch).
- One genuinely important carve-out: `<SUBAGENT-STOP>` — a dispatched subagent executing a specific task ignores the bootstrap, preventing recursive skill-invocation inside workers. Any suite with subagent delegation needs this exact guard.
- Explicit precedence (user instructions > skills > default behaviour) is stated cleanly.

**Cons**
- The absolutist framing ("even a 1% chance a skill might apply → you ABSOLUTELY MUST invoke it, before clarifying questions, before checking files") is a compliance-maximal posture that would tax every small task in the rnov24 suite and directly conflicts with asking the user a clarifying question first when a request is ambiguous.
- It is a bootstrap for the superpowers ecosystem specifically (platform reference files, its own skill names); as a pattern it transfers, as a file it does not.
- Red-flag table pathologizes ordinary judgement calls ("this doesn't need a formal skill" is always rationalization), leaving no legitimate proportionality judgement — the orchestrator needs the opposite: a documented right to skip process for trivial work.

## 15. writing-skills (superpowers) — ADAPT

**Purpose:** Create and edit skills using TDD applied to process documentation — baseline pressure scenarios first, then a minimal skill, then loophole-closing refactors.

**Pros**
- **Skill Discovery Optimization** is directly load-bearing for building the rnov24 suite: the description field must state only triggering conditions ("Use when…"), never summarize the workflow — with tested evidence that a workflow-summarizing description made agents perform a shortcut version (one review instead of two) instead of reading the skill. Plus keyword coverage, verb-first naming, and frontmatter limits.
- "Match the form to the failure" is the most sophisticated guidance-engineering content in the batch: prohibition + rationalization tables for discipline failures, a **positive recipe/contract** for wrong-shaped output (with head-to-head wording-test evidence that prohibitions backfire there), required template slots for omissions, and conditionals keyed to observable predicates for conditional behaviour. This should govern how the rnov24 suite writes its own contracts.
- Micro-testing wording before full scenarios (fresh-context single samples, always a no-guidance control, 5+ reps, manually read flagged matches, variance-as-metric) is a cheap, concrete eval loop for tuning orchestrator prompts and report contracts before deploying them.

**Cons**
- The full iron-law regimen (pressure scenarios with combined pressures, baseline verbatim rationalization capture, bulletproofing until no loopholes) for **every** skill and **every edit** is expensive enough that a one-person suite will either skip it silently or stall; it needs tiering by skill criticality that the skill does not provide.
- Its token-efficiency targets (<200 words for frequently-loaded skills, <500 for others) are irreconcilable with the protocol-heavy skills in this very batch (SDD is ~4,500 words) — the guidance and the ecosystem's own practice contradict each other.
- Deployment checklist ends at "commit and push to your fork / consider a PR", with nothing on versioning, changelogs, or keeping a published repo (the user's actual goal) in sync with local copies.

## 16. diagnosing-superpowers (superpowers) — ADAPT

**Purpose:** Investigate why a superpowers session went wrong — from the transcripts on disk, with cited evidence — and produce a report (and optionally a scrubbed bundle or GitHub issue) for the maintainers.

**Pros**
- Evidence discipline worth stealing for any post-mortem/review tooling: every finding cites `path:line` or it is discarded, every number is computed from the transcript or a command, never from memory; "no citation, no finding" is enforced on its own subagents' output.
- Its triage step is a clean parallel-analysis pattern: the controller reads the problem region itself, then dispatches one analyst subagent per dimension in parallel (skill timeline, plan adherence, repeated work, stumbles, quality evidence, request conflicts, cost/time), each given the case file and an exact-path warning that a subagent's "current session" is its own — a real context-isolation gotcha, named.
- Privacy/consent handling is thorough: read-only on session files, redaction levels explained before bundling, scrub + scrub-audit loop until CLEAN, human approval of exact text before any issue or archive.

**Cons**
- Niche by design: it diagnoses one ecosystem's sessions for upstream bug reports, and its hardest rule — "you report, you do not diagnose; never name a defect or propose a change" — deliberately withholds the conclusion the user actually wants from a post-mortem. As an orchestrator component it supplies evidence gathering, not decisions.
- Heavy machinery (intake gating all analysis, seven mandatory analysts, case/report/bundle templates) for what is usually a five-minute question; nothing tiers the effort to the complaint's size.
- Intake absolutism ("nothing starts until your partner has answered; if they are away, write the questions and stop") conflicts with the autonomous-run posture used elsewhere in the same ecosystem.

## 17. brain-grade (original copy) — DROP

**Purpose:** Grade the user's intelligence (IQ, logic, EQ, creativity, street smarts) from their own past chat messages, using five isolated judge subagents and a coach, with quoted evidence for every claim.

**Pros**
- Its one transferable mechanism is genuinely good: **blind independent judges** — five subagents dispatched at once, each given only the evidence file and one rubric, none seeing the others' answers — followed by a synthesizer (coach) that works from the evidence plus all five verdicts. That is a reusable pattern for council-style review (design councils, multi-lens code review).
- Strict output contract per judge (fixed fields, <150 words, calibrated scale anchored at 50 = average, "≥70 needs three different quotes", "no quote, no claim") shows how to make subjective subagent verdicts comparable and auditable.
- Privacy handling in the collectors is careful: only the user's own words, token/email/phone masking, minimum-evidence threshold (stop below 30 messages), local-only storage.

**Cons**
- It is not a development, programming, design, or product skill at all — its subject is the user, not the work. Nothing in it helps plan, build, delegate, or review software.
- The fixed-form judge contract is domain-specific (score calibration, quote thresholds) and would need full redesign for engineering verdicts; what transfers is the pattern, not the file.
- Large embedded scripts (~200 lines × 2 collectors) make it one of the heaviest files in the library for zero workflow value to this suite.

**Verdict rationale:** DROP from the rnov24 development suite; mine the blind-judge + fixed-verdict-form pattern into the suite's review/council skill.

---

## Batch summary — the strongest orchestration protocol available here

Assembled from the ADOPT/ADAPT pieces above, the batch already contains most of a serious main-agent orchestrator:

1. **Dispatch as an artifact (SDD + agy-delegation).** A task is handed over as files, not prose: an extracted brief that is the single source of requirements (exact values live only there), a short dispatch frame (where the task fits, interfaces from earlier tasks, pre-resolved ambiguities), and a named report file. agy-delegation adds the packet shape for external workers — byte-identical stable header, one coherent change per packet, mandatory report footer — plus resume-instead-of-reanalyze and effort/model routing per task class.
2. **Dual-verdict task review with a diff package (SDD).** Every task is gated by a fresh reviewer who gets brief + report + a generated review package built from a BASE recorded before dispatch, and must return both a spec-compliance verdict and a quality verdict. The controller never pre-judges findings in the reviewer prompt; "cannot verify from diff" items are resolved by the controller personally.
3. **A bounded rework loop with adjudication (SDD + systematic-debugging).** Fix rounds are capped (5), early rounds resume the implementer, later rounds escalate to a fresh, stronger model; re-reviews are scoped to the fix diff with per-finding ADDRESSED / NOT ADDRESSED verdicts. At the cap, findings are adjudicated into ledgered rulings — never silently dropped. Debugging adds the complementary rule: 3 failed fixes means question the architecture and involve the human.
4. **Durable ledger + rulings (SDD / executing-plans).** A per-plan workspace and progress ledger that survives compaction, records completion lines only when the completion contract is evidenced (executing-plans' `task-done` runs the tests before it writes the line), and surfaces every `Ruling:` exhaustively to the human at the end.
5. **Evidence-before-claims as a universal gate (verification-before-completion + TDD).** No status claim without a fresh command and read output; a worker's "success" is checked against the VCS diff; a single-file green run is not a green suite, and an unreported red test falsifies the report.
6. **Isolation and safe landing (using-git-worktrees + finishing-a-development-branch).** Detect-or-create worktree isolation with ignore-checks and a clean baseline; finish with a verified suite, a human-chosen integration menu, merge-then-verify-then-clean sequencing, and provenance-based cleanup.

## What is still missing for a complete rnov24 orchestrator

- **Artifact chain beyond code.** The batch covers exactly two artifacts — a design spec (brainstorming) and an implementation plan (writing-plans). There is no PRD, DESIGN document, user persona, user story + acceptance criteria, ERD, userflow, or API documentation artifact: no templates, no quality gates between them, and no rule for which artifacts a given task class requires. SDD's machinery (brief, review package, dual verdict) is git-diff-based and must be re-based onto document artifacts (e.g. review package = artifact + the upstream artifacts it must agree with; verdict = consistency + completeness).
- **One canonical report schema and verdict vocabulary.** Three incompatible report styles coexist: SDD's short return contract (status / commits / one-line test summary / concerns) plus a free-form report file, agy's footer (branch, hash, files, checks, leftovers) or optional JSON schema, and requesting-code-review's free-form Strengths/Issues/Assessment. A suite needs one schema — machine-readable, with status enum, evidence fields (commands run + results), files/artifacts touched, and open concerns — that every worker type (native subagent, agy, reviewer) returns.
- **Acceptance verdicts tied to acceptance criteria.** Implementer statuses exist (DONE / DONE_WITH_CONCERNS / NEEDS_CONTEXT / BLOCKED), and reviewer verdicts exist per task, but nothing records an orchestrator-level ACCEPT / REWORK / ESCALATE verdict **against named acceptance criteria IDs**, so there is no traceable chain from user story → criterion → task → test evidence → verdict. writing-plans' Review Focus and Interfaces blocks are the nearest raw material.
- **A unified rework loop across worker types.** SDD's loop assumes resumable in-harness subagents and git commits; agy follow-ups are ad-hoc packets with no round cap, no escalation rule, and no loop log. One loop definition (rounds, resume-vs-fresh rule, model escalation, scoped re-review, cap adjudication) must cover both, and non-code artifacts too.
- **Escalation rules to the human, generalized.** The four stop conditions (irreversible/destructive, security-sensitive, outside-worktree side effects, plan-so-broken-every-path-is-a-guess) are a good spine, and debugging adds the 3-failed-fixes rule — but there are no cost/quota escalation thresholds for the orchestrator itself (agy-delegation checks quota for its worker only), no "reviewer and implementer disagree twice → human" rule, and no rule for surfacing parked findings before the very end.
- **Parallel write safety.** dispatching-parallel-agents parallelizes investigation, and SDD forbids parallel implementers outright. Nothing defines the middle ground the suite needs: one worktree per parallel writer, file-ownership partitioning in the plan, and a merge/conflict protocol at integration (finishing-a-development-branch handles one branch landing, not N workers converging).
- **Design and product review gates.** Every review mechanism in the batch reviews code. There is no reviewer role, rubric, or verdict for a PRD (problem validity, scope), a DESIGN (consistency, usability), an ERD (normalization, constraints), or API docs (contract completeness) — the blind-judge pattern in brain-grade and agy's read-only council-verdict routing are patterns to build these from, not ready skills.
- **Suite-level budgeting and routing policy.** Model selection is qualitative in SDD and quota-reactive in agy-delegation; no skill defines a per-plan budget, when to choose inline vs subagent-driven vs agy execution as one decision (writing-plans' handoff asks the human every time), or how verdict quality is sampled/audited over time (diagnosing-superpowers is the retrospective tool, but it is scoped to upstream bug reports and forbidden from concluding).

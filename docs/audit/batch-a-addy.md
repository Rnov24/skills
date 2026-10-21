# Batch A Audit — Addy Osmani `agent-skills` (25 skills)

- **Scope:** the 25 skills installed at `~/workspace/custom-skills/local-addy-*/` (addyosmani/agent-skills v0.6.13).
- **Method:** each `SKILL.md` read in full; reference files skimmed where present. Every skill gets a one-line purpose, concrete pros (mechanisms worth stealing), concrete cons (gaps, overlaps, rigidity), and a verdict: ADOPT as-is / ADAPT (with the change specified) / DROP (with reason).
- **Judging context:** these audits feed rnov24's own unified suite spanning development, programming, design, and product — built on (a) an artifact-based workflow (PRD, DESIGN brief, user personas, user stories + acceptance criteria, ERD, user flows, API documentation) and (b) a main-agent-as-orchestrator model (delegation packets, subagent review gates).

## Verdict summary

| Verdict | Count | Skills |
|---|---|---|
| ADOPT as-is | 4 | code-review-and-quality, constraint-driven-development, git-workflow-and-versioning, performance-optimization |
| ADAPT | 19 | api-and-interface-design, browser-testing-with-devtools, ci-cd-and-automation, context-engineering, debugging-and-error-recovery, documentation-and-adrs, doubt-driven-development, frontend-ui-engineering, idea-refine, incremental-implementation, interview-me, observability-and-instrumentation, planning-and-task-breakdown, security-and-hardening, shipping-and-launch, source-driven-development, spec-driven-development, test-driven-development, using-agent-skills |
| DROP (standalone) | 2 | code-simplification (fold into review), deprecation-and-migration (salvage 3 mechanisms into data/API skill) |

## Per-skill audits

### api-and-interface-design
**Purpose:** Design contract-first, backward-compatible APIs and module interfaces that are hard to misuse.
**Pros:**
- Contract-first workflow with typed input/output separation, branded IDs (`TaskId` vs `UserId`), and discriminated unions — directly reusable as the API documentation artifact's schema section, tying endpoints to ERD entities
- Exceptionally deep idempotency playbook rarely found elsewhere: derive key from intent (`charge:v1:${orderId}`), claim atomically via unique constraint (not check-then-insert TOCTOU), reject same-key/different-payload with 422, deliberate in-flight duplicate strategy (409 / wait / 202), and retention set from longest retry path including DLQ replay
- Concrete conventions and gates: single `APIError {code, message, details}` shape with status mapping (400/401/403/404/409/422/500), validate-only-at-boundaries list, plural-noun/camelCase/is-has-can naming table, mandatory pagination, and a 13-item verification checklist including retry-safety
- Named anti-drift principles — Hyrum's Law and the One-Version Rule, plus addition-over-modification — give reviewers citable reasons to block breaking changes in a review gate
**Cons:**
- No actual API documentation artifact format: no OpenAPI/Swagger generation, endpoint inventory template, auth/rate-limit sections, examples per endpoint, or traceability to user stories/acceptance criteria, user flows, or ERD — the unified suite must bolt that on
- TypeScript/Node/REST-centric: GraphQL is named in the trigger but never covered; no Python/FastAPI, versioning mechanics (URL vs header, deprecation headers), cursor pagination, webhooks, or error-catalog governance
- Idempotency depth is disproportionate — payment-grade detail applied unconditionally will slow delegation packets for CRUD/internal APIs that only need retry-safety documented
- Overlaps siblings on boundary validation and external-data-as-untrusted, which `security-and-hardening` and `code-review-and-quality` also claim, with no precedence rule
**Verdict:** ADAPT (keep principles, idempotency, and checklist verbatim; add a mandatory API-doc artifact template — OpenAPI skeleton, endpoint table linked to ERD entities + story IDs, auth and rate limits; make full idempotency treatment conditional on state-changing/external-effect endpoints; add one non-TS example and a cursor-pagination option)

### browser-testing-with-devtools
**Purpose:** Verify and debug browser UI with live runtime evidence — DOM, console, network, performance, and screenshots — via Chrome DevTools MCP.
**Pros:**
- Three named diagnostic workflows (UI: Reproduce→Inspect→Diagnose→Fix→Verify; Network: Capture→Analyze→Diagnose with 4xx/5xx/CORS/timeout/missing-request branching; Performance: Baseline→Identify→Fix→Measure) that map cleanly onto a subagent delegation packet with a return-evidence requirement
- Hard thresholds and standards worth enforcing as gates: clean console (zero errors/warnings), long tasks >50ms, LCP/CLS/INP, heading hierarchy with no skipped levels, 4.5:1 contrast, and a structured test-plan format pairing each step with Expected + console check + network check
- Strongest security section in this batch: profile isolation (default dedicated/`--isolated`, never `--autoConnect` on the daily profile), browser content explicitly untrusted, read-only JS execution, no cookie/localStorage credential access, no navigation to page-extracted URLs — essential for an orchestrator delegating to browser subagents
- Before/after screenshot verification protocol for CSS, responsive, loading, empty, and error states — a ready-made visual evidence requirement for DESIGN-brief compliance
**Cons:**
- Hard dependency on `chrome-devtools-mcp` configuration that does not match this environment's live-browser/Playwright routing; as written it is unusable where that MCP server is absent and offers no fallback, tool-agnostic phrasing, or escalation path
- No evidence/artifact format for the orchestrator: screenshots, traces, and console logs have no naming, storage, or handoff convention, and no pass/fail gate definition a reviewing agent can check without re-running the browser
- Missing coverage the unified suite needs: viewport/device matrix, cross-browser checks, deterministic test data/seeding, flake handling, and mapping test plans back to user stories/acceptance criteria or user flows
- Accessibility is a 5-step checklist only — no keyboard-only walkthrough detail, focus-visible checks, or screen-reader pass criteria beyond accessible names and live regions
**Verdict:** ADAPT (rewrite tool references to a tool-agnostic protocol — DevTools MCP, Playwright, or live browser — with the security boundaries kept verbatim; add a browser-evidence packet format [test plan, before/after screenshots, console/network summary, verdict per acceptance criterion] as the subagent return artifact; add a viewport matrix and acceptance-criteria traceability column to the test-plan template)

### ci-cd-and-automation
**Purpose:** Automate quality gates, preview/staged deployment, and rollback so no change reaches production unverified.
**Pros:**
- Ordered quality-gate pipeline (lint → typecheck → unit → build → integration → E2E → security audit → bundle size) with a non-negotiable "fix, don't disable/skip" rule and two framing principles (Shift Left, Faster is Safer) — a solid default gate sequence for the suite's delivery stage
- Copy-ready GitHub Actions YAML including the non-obvious parts: Postgres service container with health checks for integration tests, Playwright install plus failure-only artifact upload, and a manual `workflow_dispatch` rollback workflow
- CI-failure feedback loop for agents (paste failure → fix → verify locally → re-push, with per-failure-type routing) — the seed of an orchestrator retry protocol, even if primitive here
- Deployment discipline beyond CI: feature-flag lifecycle with mandatory cleanup date, staged rollout with a 15-minute error-monitoring window and rollback branch, preview-per-PR, Build Cop role, and env/secret separation (`.env.example` committed, CI never holds production secrets)
**Cons:**
- Entirely GitHub Actions + npm/Node 22 + Vercel-shaped: no stack-agnostic gate definition, nothing for Python/FastAPI, Modal, TiDB, or non-GitHub hosts that the target workflow actually uses, so most YAML is throwaway for this user
- Agent feedback loop is manual copy-paste of CI output — no structured failure packet, retry budget, stop condition, or subagent review gate before re-push, which the orchestrator model requires to avoid infinite fix loops
- Rigid and dated in places: "no gate can be skipped" with no documented waiver path, E2E labelled optional but included in the gate diagram, 10-minute pipeline target asserted without context, action versions pinned loosely (`@v4`), and no coverage thresholds, artifact/DESIGN-compliance checks, migration-safety, or preview-data seeding
- Overlaps `code-review-and-quality` on merge gates (required reviews/status checks) and Dependabot content duplicates the dependency-discipline section there, with no division of ownership
**Verdict:** ADAPT (extract a stack-agnostic gate contract — ordered stages, waiver process, <10 min budget, rollback + flag-cleanup requirements — and demote all YAML to per-stack examples, adding Python/Modal/Vercel variants; replace copy-paste feedback with a structured CI-failure packet with a max-retry and escalation rule; add artifact-conformance checks [PRD/DESIGN/API-doc presence] as an explicit early gate)

### code-review-and-quality
**Purpose:** Gate every change through a five-axis review — correctness, readability, architecture, security, performance — before merge.
**Pros:**
- Five-axis rubric with unusually sharp architecture tests: does the refactor reduce the concept count or merely relocate it, is feature logic leaking into a shared module, is a new conditional bolted onto an unrelated flow, are repeated conditionals signalling a missing dispatcher — plus a named Structural Remedies list (collapse branches, delete pass-through wrappers, make type boundaries explicit) so findings ship with a fix, not just a complaint
- Severity labelling scheme (Critical / required-no-prefix / Nit / Optional-Consider / FYI) with "lead with what matters" ordering — directly usable as the subagent review-gate output format in delegation packets
- Verifiable review process: tests-first reading, then a mutation check (invert one condition, run the suite, a green result is a missing-test finding), and Step 5 "verify the verification" — evidence-based gating, not LGTM rubber-stamping, reinforced by the honesty rules (quantify, don't soften, don't accept "fix later")
- Quantified sizing discipline: ~100 lines good, ~300 acceptable, ~1000 split it, plus a separate ~1000-total-line file-size signal, four splitting strategies (stack, file-group, horizontal, vertical), separate refactor from feature work, and a full dependency-upgrade protocol (changelog first, one package per change, review the lockfile diff)
**Cons:**
- Written for human PR culture — one-business-day response SLA, change descriptions for VCS history, multi-model pattern ending in "human makes the final call" — with no packet/review-artifact format, acceptance thresholds, or re-review loop for a main-agent orchestrator reviewing subagent diffs against PRD/DESIGN/API artifacts
- No traceability axis: nothing checks the change against user stories/acceptance criteria, user flows, ERD, or API documentation, which is the core of the target artifact-based workflow; "matches spec/task" is one bullet under Correctness
- Dead references and duplication: its See Also points to `../../references/security-checklist.md` and `performance-checklist.md` that do not exist in the installed folder, and the security/performance axes plus dead-code hygiene substantially duplicate `security-and-hardening`, `performance-optimization`, and `code-simplification` without a precedence rule
- The closing "presumptive blockers" nuance (surface-and-propose vs escalate-to-Required) partially contradicts the earlier severity table and will produce inconsistent gate verdicts between reviewer agents
**Verdict:** ADOPT as-is (the five axes, severity labels, mutation check, sizing thresholds, and dependency protocol become the suite's review gate unchanged; the missing artifact-traceability check and packet format belong in the orchestrator skill that invokes this review, not in a rewrite of it — only fix the two dead reference links at install time)

### code-simplification
**Purpose:** Reduce code complexity while preserving exact behavior, scoped to recently changed code.
**Pros:**
- A hard safety contract up front: preserve inputs, outputs, side effects, error behaviour, and ordering; four ask-before-every-change questions; and the red-flag rule that a simplification requiring test modification has probably changed behaviour — a clean pre/post gate for any refactor packet
- Chesterton's Fence as Step 1 with a concrete pre-flight list (responsibility, callers/callees, edge cases, tests, git blame) — prevents the most common subagent failure of deleting "useless" code that encodes a constraint
- Dense, scannable pattern tables with numeric signals (nesting 3+, functions 50+ lines, duplication 5+ lines, boolean-flag parameters) and TS/Python/React before-after pairs, plus the Rule of 500 (over 500 lines, use codemods/AST instead of hand edits) and incremental one-change → test → commit discipline
- Explicit over-simplification failure modes (inlining away a named concept, merging unrelated functions, deleting load-bearing abstraction, optimising for line count) and scope-to-what-changed — both rare and genuinely protective
**Cons:**
- Largest overlap in this batch: its readability, architecture, dead-code, and "separate refactor from feature work" content is already covered, often in stronger form, by `code-review-and-quality` (Readability axis, Structural Remedies, dead-code hygiene) — as a standalone skill it creates two competing authorities on the same diff
- No orchestrator fit: no before/after complexity evidence, no packet scope declaration, no reviewer sign-off format, and no link to acceptance criteria — verification is a self-reported checklist ending in the subjective "would a teammate approve"
- Guidance skews to worked micro-examples in three languages; nothing on simplifying the artifacts the unified suite produces (specs, prompts, pipelines), large generated-code cleanups, or when simplification should instead be a rewrite/escalation decision
- Thresholds are presented without calibration or exceptions beyond performance-critical code — 50-line functions and 3-level nesting will false-positive on legitimate parsers, state machines, and data pipelines if a subagent applies them mechanically
**Verdict:** DROP (as a standalone skill — its territory is already owned by the code-review skill, and two simplification authorities will conflict in review gates; salvage only the behaviour-preservation contract, the Chesterton's Fence pre-flight, the pattern tables, and the Rule of 500 into a single "refactor" section inside the review/implementation skill before dropping it)

### constraint-driven-development
**Purpose:** Turns a project's quality bar into a mechanically checked `CONSTRAINTS.md` contract instead of prose agents can quietly ignore.
**Pros:**
- Artifact is enforceable by construction: every dimension needs Rule + `Checked by` command + `Runs at` stage, plus a Floor, a Measured-not-yet-enforced ratchet table (record today's value, must not fall), and Exceptions with ID/owner/90-day expiry.
- Anti-cheating floor-guard in `references/floor-guard.md`: diff-scoped checks (exit 0/1/2, never read 2 as 0) for the 5 cheap-road-to-green moves — threshold moved, test skipped/deleted/assertion stripped, new `@ts-ignore`/`eslint-disable`/`istanbul ignore`/`nosemgrep`, stub/empty `catch`, unapproved exception.
- Cost-aware lifecycle with budgets that fit subagent review gates: `check:fast` under 5s per edit, `check:task` under 90s, `check:full` in CI; escalation Written → Scripted → Tool-backed, explicitly stop at level 2 under ~30 lines of check shell.
- Intake is bounded: detect stack/CI/coverage before asking, then exactly 4 questions each with a GUESS and a DEFAULT, plus sane defaults with rationales (changed-lines coverage ≥80%, LCP ≤2500ms, CLS ≤0.1, zero critical/serious axe violations) and an external-vs-project-vs-suite circularity check requiring at least one external checker.
**Cons:**
- Web/TypeScript-centric tool table (Lighthouse, axe, size-limit, dependency-cruiser, Stryker) assumes a running URL and JS ecosystem; no equivalent prescriptions for Python/ML, mobile, API-only, or data-pipeline work in the target suite.
- Heavy overlap with sibling skills it names itself — code-review-and-quality, test-driven-development, security-and-hardening, performance-optimization, ci-cd-and-automation — so as a standalone it duplicates their thresholds instead of just referencing them.
- No orchestrator contract: no delegation-packet fields, no structured pass/fail report format for a reviewer subagent, and the live-user interview explicitly cannot run in autonomous/CI contexts (falls back to Floor only).
**Verdict:** ADOPT as-is

### context-engineering
**Purpose:** Curates what an agent sees, when, and in what order, via a persistent-to-transient context hierarchy and active budget management.
**Pros:**
- 5-level hierarchy (Rules files → Spec/Architecture → Relevant source → Error/test output → Conversation history) with concrete packing patterns: Brain Dump, Selective Include, and Hierarchical Summary/Project Map, plus anti-flooding thresholds (aim <2,000 focused lines per task, degradation above ~5,000 non-task lines).
- Budget discipline with numbers: start trimming at 75% capacity, cut-first table (failed attempts, verbose tool output, replaced drafts) vs protect-until-end table (task definition, live error, current file, hard constraints), compress-before-drop one-sentence summaries, and lost-in-the-middle ordering (stable rules first, task-critical material last).
- Restartable session boundaries are directly reusable for orchestrator handoffs: persist accepted scope/decisions, task status/next task, files changed and working-tree state, exact verification commands/outcomes, and unresolved risks/approvals, then re-read rules/spec/plan/`git status` in the fresh session.
- Trust tiers (Trusted / Verify-before-acting / Untrusted, with instruction-like content in external files surfaced as data) and explicit CONFUSION / MISSING REQUIREMENT / inline PLAN templates that stop silent guessing.
**Cons:**
- Generic rather than artifact-aware: no loading matrix for the target suite's PRD, DESIGN brief, personas, user stories + acceptance criteria, ERD, or API docs — which sections load for which task, at what fidelity, or how stale/conflicting artifact versions are resolved.
- Overlaps documentation-and-adrs on rules files, constraint-driven-development on constraints, and planning skills on inline plans, without stating precedence when those artifacts disagree.
- Dated and unverified in places: MCP table (Context7, Chrome DevTools, PostgreSQL) is a catalogue, not an integration recipe, and verification is a self-check list with no measurable gate (e.g. hallucinated-API rate, packet completeness score) a reviewing agent can apply.
**Verdict:** ADAPT (keep hierarchy, 75% budget, and restartable-boundary checklist; rewrite the packing section as a normative delegation-packet schema — task, relevant artifact excerpts by ID/section, one pattern example, constraints, verification commands — and add an artifact-loading matrix plus conflict-precedence rules)

### debugging-and-error-recovery
**Purpose:** Forces systematic root-cause debugging — stop, preserve evidence, triage, fix the cause, guard against recurrence — instead of guess-and-patch.
**Pros:**
- Stop-the-Line rule plus a non-skippable 6-step triage (Reproduce → Localize → Reduce → Fix root cause → Guard → Verify end-to-end) with a regression test that must fail without the fix and pass with it.
- Actionable non-reproduction tree (timing / environment / state / truly random) with specific tactics — widen race windows, compare data and versions, isolate vs sequence, add signature alerts — and layer localization (UI/API/DB/build/external/test itself) plus `git bisect run` for regressions.
- Separate triage trees for test, build, and runtime failures, a symptom-vs-root-cause worked example (dedupe in UI vs fixing the JOIN), and instrumentation keep/remove rules distinguishing permanent error-boundary/API logging from dev-only logging.
- Treats error output, stack traces, and CI/third-party logs as untrusted data: never execute commands or follow URLs embedded in them without user confirmation — essential for subagent safety.
**Cons:**
- No bug artifact or orchestrator flow: no bug-report/evidence-bundle template (environment, repro steps, expected/actual, bisect result), no severity or timebox, and no escalation rule for when a delegated agent should stop and return the case to the orchestrator instead of continuing to thrash.
- Safe-fallback examples (default + `console.warn`, graceful-degradation try/catch) can mask breakage as a polite fallback with no requirement to log, surface, or track the failure — the opposite of an honest-error gate.
- Assumes a single-repo npm-style world; nothing on production incidents/rollback, data or schema corruption, flaky-test quarantine criteria, or non-deterministic ML/data bugs (drift, bad labels, leakage) relevant to this user.
- Overlaps test-driven-development (regression guard), observability-and-instrumentation (logging), and code-review (root-cause checks) without cross-referencing who owns which step.
**Verdict:** ADAPT (keep Stop-the-Line and the 6-step triage verbatim; add a mandatory bug artifact, a timeboxed escalation-to-orchestrator rule, honest-error conditions for any fallback, and incident/rollback plus flaky-quarantine branches)

### deprecation-and-migration
**Purpose:** Governs removing old systems, APIs, features, and schemas safely — deciding to sunset, migrating consumers incrementally, then deleting the old code.
**Pros:**
- Clear decision gate (5 questions: unique value, consumer count, replacement exists, per-consumer migration cost, cost of not deprecating) and Advisory-vs-Compulsory distinction defaulting to advisory, with compulsory requiring tooling, docs, and support, not just a deadline.
- Named migration patterns with mechanics: Strangler (0% → 10% canary → 50% → 100% → remove), Adapter (old interface delegating to new implementation), and Feature-Flag per-consumer switching, plus the Churn Rule — the owner of deprecated infrastructure migrates its users.
- Expand/Contract database migration is the strongest section: Expand (nullable column) → dual-write → batched backfill → switch reads → Contract in a separate later deploy, with rules for tested down paths, throttled backfills, and `CREATE INDEX CONCURRENTLY`.
- Zombie-code detection (no commits in 6+ months with active consumers, no owner, failing tests, vulnerable deps) forcing an own-it-or-remove-it decision, and a split verification list for deprecations vs schema migrations.
**Cons:**
- Enterprise-scale assumptions dominate: consumer-by-consumer migration, traffic percentages, and multi-team churn rarely apply to the solo/small-team, pre-1.0 projects the unified suite mainly serves, where a breaking change with a changelog is often proportionate.
- No artifact integration: the deprecation notice is a loose markdown snippet, with no deprecation plan linked to PRD/API docs/ERD, no consumer-inventory format, no API versioning/semver or endpoint-sunset conventions, and no defined metric or threshold for "zero active usage."
- Missing product-side migration entirely: end-user communication, data export/retention and deletion obligations, pricing/plan sunsets, and rollback criteria after removal has started.
- Overlaps documentation-and-adrs (notices, rationale), incremental-implementation (thin slices), and any future data/API design skill (expand/contract), so a standalone skill fragments those topics.
**Verdict:** DROP (as a standalone skill — salvage only Expand/Contract, Strangler, and the 5-question decision gate as a short migration chapter inside the unified data/API skill; the rest is low-frequency enterprise process the suite does not need to carry)

### documentation-and-adrs
**Purpose:** Records the *why* behind decisions and ships the surrounding docs — ADRs, API docs, README, and changelog — that humans and agents need to avoid re-deciding.
**Pros:**
- Match-existing-convention-first rule for ADRs (location/format, numbering/naming sequence, heading set; surface conflicts instead of starting a second scheme), then a complete ADR template with Status lifecycle Proposed → Accepted → Superseded/Deprecated, Alternatives Considered with explicit rejection reasons, and Consequences; never delete old ADRs, supersede them.
- Multi-format API documentation: JSDoc with `@param`/`@returns`/`@throws`/`@example` as the preferred TypeScript form, plus an OpenAPI example covering success (201) and validation error (422) responses.
- Concrete README skeleton (one-paragraph description, Quick Start, Commands table, Architecture linked to ADRs, Contributing) and Keep-a-Changelog-style changelog (Added/Fixed/Changed with issue refs), plus comment-the-why-not-the-what and document-known-gotchas rules with examples.
- Prose Review pass that protects factual fidelity: mark names/numbers/units/commands/paths/trade-offs/uncertainty that must survive editing, check them against source, restore lost qualifiers, and never replace an unsupported claim with an invented example or stronger guarantee.
**Cons:**
- Covers only ADRs, API snippets, README, and changelog — it has no templates or quality criteria for the target suite's core artifacts: PRD, DESIGN brief, user personas, user stories + acceptance criteria, or ERD (notation, keys, relationships), so it cannot serve as the suite's documentation backbone unmodified.
- No ownership, review gate, or freshness mechanism: "expensive to reverse" is the only ADR trigger threshold, there is no doc owner/status/review-date, no drift check against code or API surface, and no orchestrator checkpoint verifying artifacts are complete before implementation is delegated.
- Thin on modern API-doc completeness beyond one POST example: no auth, errors catalogue, pagination, versioning, or deprecation marking, and no diagram conventions for architecture/ERD.
- Overlaps context-engineering on CLAUDE.md/rules files and specs with no division of labour stated, and its examples are dated (2025) and task-app monocultural.
**Verdict:** ADAPT (keep the ADR template, convention-matching rule, and Prose Review intact as the decision-record core; extend the skill into the unified artifact system by adding templates and acceptance checklists for PRD, DESIGN brief, personas, stories + acceptance criteria, and ERD, a full API-doc checklist, and an artifact review gate with owner/status/supersession links that the orchestrator checks before delegation)

### doubt-driven-development
**Purpose:** Subjects every non-trivial decision to a fresh-context adversarial review before it is allowed to stand.
**Pros:**
- Precise non-trivial trigger with 5 tests (branching logic, cross-boundary, unverifiable property, invisible context, irreversible blast radius) plus an explicit When NOT to Use list, so it does not tax renames/formatting/one-liners
- Core anti-bias mechanism worth keeping verbatim: reviewer gets ARTIFACT + CONTRACT only, never the CLAIM or the author's reasoning, with an issues-only adversarial prompt that overrides balanced reviewer personas
- Bounded reconcile loop: findings classified in precedence order contract misread > valid+actionable > valid trade-off > noise, hard stop at 3 cycles / trivial findings / user override, and a checkable doubt-theater signal (0 actionable across 2+ substantive cycles = escalate)
- Cross-model safety detail: read-only sandbox, prompt via file/stdin never shell-interpolated, PATH + `--version` check and per-invocation user confirmation before any external CLI call
**Cons:**
- Mandatory cross-model offer in *every* interactive cycle is unaffordable friction for rnov24's orchestrator model — it would stall delegation packets and burn the agy/Gemini quota the suite is trying to preserve
- Heavy overlap with siblings: in-flight vs post-hoc split with `code-review-and-quality`, RED step with TDD, and fact-checking with source-driven-development is asserted but no single gate owns the verdict
- Not portable as written: hard references to Claude Code personas, `agents/`, and `../../references/orchestration-patterns.md`, plus a degraded self-review fallback when nested in a subagent that contradicts the fresh-context premise
- Produces no persistent artifact: no gate record, finding log, or sign-off format to attach to a PRD/DESIGN/story packet for later audit
**Verdict:** ADAPT — keep CLAIM → EXTRACT → DOUBT → RECONCILE → STOP and the ARTIFACT+CONTRACT-only rule as the suite's subagent review gate, but make cross-model escalation risk-triggered (auth, migration, public API, irreversible ops) instead of mandatory, replace persona/Claude-Code references with generic delegation packets, and require a short gate record (claim, findings by class, disposition) saved with the work artifact

### frontend-ui-engineering
**Purpose:** Builds production-quality, accessible, responsive UIs that follow a real design system instead of the generic AI aesthetic.
**Pros:**
- Reference-led quality workflow that maps directly onto a DESIGN brief: study 2-3 reference screens, record hierarchy/density/navigation/states, write a short design contract (job, primary action, required states, responsive rules, patterns to reject) before coding
- Concrete anti-AI table (purple/indigo everything, excessive gradients, rounded-2xl everywhere, stock card grids, oversized padding, shadow-heavy, lorem ipsum) paired with production replacements, plus semantic tokens, spacing-scale-only values, and 4.5:1 / 3:1 contrast thresholds
- Sound architecture defaults: composition over configuration, container/presentation split with explicit loading/error/empty handling, and a state ladder (local → lifted → Context → URL searchParams → server state → global store) with a prop-drilling limit of 3 levels
- Verifiable finish checklist: keyboard tab-through, screen reader, breakpoints 320/768/1024/1440px, skeleton over spinner, optimistic update with rollback, and loading/empty/error/success/permission states
**Cons:**
- Stack-locked to React + Tailwind + React Query/SWR + Storybook colocation; no guidance for non-React stacks, native, or the suite's other targets, and the 200-line component red flag is arbitrary without a split procedure
- Consumes no upstream artifacts: never takes personas, user stories/acceptance criteria, PRD, or an approved DESIGN brief as input, and produces no handoff artifact back to the orchestrator
- Overlaps heavily with rnov24's existing design stack (Atelier, impeccable, shadcn discovery/review, design-taste skills) on tokens, layout, and finish gates, with no precedence rule for conflicts
- Dangling dependency: detailed accessibility is deferred to `../../references/accessibility-checklist.md` which is not in the folder, leaving WCAG 2.1 AA coverage to inline snippets only
**Verdict:** ADAPT — keep the design-contract step, anti-AI table, state ladder, and breakpoint/state verification as the implementation layer, but require the DESIGN brief + story acceptance criteria as mandatory inputs, strip React/Tailwind specifics into stack adapters, inline the missing accessibility checklist, and defer all visual-direction decisions to the suite's design skills to remove duplication

### git-workflow-and-versioning
**Purpose:** Structures branching, atomic commits, and semantic versioning so agent-generated change stays reviewable, reversible, and releasable.
**Pros:**
- Quantified sizing and branching discipline: target ~100 lines per commit/PR, ~300 acceptable, split above ~1000; trunk-based with main always deployable, feature branches merged in 1-3 days, feature flags preferred over long branches
- Save Point Pattern built for agents — Implement → Test → Verify → Commit, revert to last known-good on failure — plus git worktrees for parallel agent streams without branch switching
- CHANGES MADE / THINGS I DIDN'T TOUCH / POTENTIAL CONCERNS summary format: the DIDN'T TOUCH section is a ready-made scope-discipline proof for subagent review gates
- Complete release contract: Conventional-Commits types with why-not-what bodies, SemVer with Hyrum's Law warning (assume breaking when unsure), tag as source of truth for version, and a human changelog grouped Added/Changed/Fixed/Deprecated/Removed/Security written with the change, not at release time
**Cons:**
- Much of it is standard practice restated; without the suite's ticket/story IDs in commit messages there is no traceability from commit → user story → PRD/ERD/API artifact
- Duplicates sibling skills: separate-concerns, atomic commits, and feature flags are repeated in incremental-implementation, and split strategies are deferred to code-review-and-quality, so the suite would carry two sources of truth
- Release/SemVer/changelog weight is disproportionate for solo, pre-consumer, and student projects that dominate rnov24's work; no lightweight mode is defined
- No handling for artifact versioning, monorepo/submodule repos, or generated-doc drift (ERD/API docs changing in the same commit as code)
**Verdict:** ADOPT as-is — use it unchanged as the suite's version-control backbone, including Save Point and CHANGES/DIDN'T TOUCH as the mandatory subagent return format; resolve the duplication by making this skill the sole owner of commit/branch/version rules and having other skills reference it

### idea-refine
**Purpose:** Refines a vague idea into a sharp, actionable concept through divergent expansion followed by convergent stress-testing.
**Pros:**
- Disciplined 3-phase flow (Understand & Expand → Evaluate & Converge → Sharpen & Ship) with hard caps that prevent brainstorm sprawl: 3-5 sharpening questions, 5-8 variations, 2-3 clustered directions
- Named divergent lenses (Inversion, Constraint Removal, Audience Shift, Combination, Simplification, 10x, Expert Lens) backed by a selective reference library (SCAMPER, How Might We, First Principles, JTBD, Constraint-Based, Pre-mortem in `frameworks.md`)
- Real evaluation rubric in `refinement-criteria.md`: User Value as painkiller vs vitamin, Feasibility including time-to-value and hardest part, Differentiation ranked from new capability down to cheaper, plus a Must-Be-True assumption audit
- Output one-pager makes trade-offs explicit — Problem Statement, Recommended Direction, Key Assumptions to Validate, MVP Scope, and a Not Doing (and Why) list, which the skill correctly calls its most valuable part
**Cons:**
- The one-pager is not a PRD and does not feed the artifact chain: no personas, no user stories with acceptance criteria, no success metrics or validation experiment owners, no ERD/API implications, and no defined handoff to spec-driven-development
- Overlaps rnov24's existing interview/grill and PRD skills (it itself defers unsure users to `interview-me` and decided directions to spec) with no routing rule for which discovery skill runs first
- Interactive-dialogue only, tied to named tools (`AskUserQuestion`, `Glob`/`Grep`); no async or delegation-packet mode for the orchestrator model, and the Steve Jobs philosophy section adds tone without mechanism
- Codebase grounding is optional and shallow (scan for prior art) with no check against existing product artifacts, roadmap commitments, or constraints already decided
**Verdict:** ADAPT — keep it only as the pre-PRD discovery stage, keep the caps, lenses, painkiller/vitamin rubric, and Not Doing list, but replace the one-pager template with a PRD seed containing HMW, JTBD job, primary persona, key assumptions with validation method, MVP scope, Not Doing, and open questions, and add an explicit exit rule handing off to the PRD/personas/stories workflow

### incremental-implementation
**Purpose:** Delivers multi-file changes in thin, verifiable vertical slices that each leave the system working, tested, and committed.
**Pros:**
- Three named slicing strategies that fit the artifact workflow directly: Vertical Slices (preferred, full DB+API+UI path per slice), Contract-First (Slice 0 = types/OpenAPI contract, then backend and frontend in parallel against mocks — ideal for ERD/API-doc driven delegation), and Risk-First (prove the riskiest piece before building on it)
- Tight Implement → Test → Verify → Commit cycle with Keep It Compilable and Rollback-Friendly rules (additive changes first, delete and replace in separate commits, migrations need rollback migrations, safe opt-in defaults, feature flag for incomplete work)
- Rule 0 Simplicity First and Rule 0.5 Scope Discipline with a NOTICED BUT NOT TOUCHING log — paired with red flags like >100 lines without tests, broken build between slices, and never re-running the same verification command on unchanged code
- Per-increment checklist anchored to the repo's own discovered test/build/typecheck/lint commands rather than hardcoded tooling
**Cons:**
- Substantial verbatim overlap with git-workflow-and-versioning (atomic commits, one thing at a time, separate concerns, feature flags) and with TDD/planning skills, so adopted together they contradict the single-source-of-truth principle
- No orchestrator mechanics despite an agent section limited to one prompt example: no delegation packet format per slice, no review gate or approval step between slices, and no rule for who may advance to the next slice
- No artifact maintenance step: slices never require updating user story acceptance status, API documentation, ERD, or DESIGN brief when implementation drifts from them, and Definition of Done is deferred to a missing `../../references/definition-of-done.md`
- Thresholds are soft and conflicting — ~100 lines before testing here vs ~100/300/1000 lines per commit/PR in the git skill — and the feature-flag example is an env-var toy with no lifecycle or removal rule
**Verdict:** ADAPT — keep it as the suite's execution core (especially Contract-First and Risk-First slicing), but delete all commit/branch/flag rules and reference git-workflow-and-versioning instead, inline a Definition of Done, and add a per-slice gate: delegation packet in, acceptance-criteria verification plus ERD/API/DESIGN artifact sync out, orchestrator approval before the next slice

### interview-me
**Purpose:** Extracts true user intent before any spec or code via a one-question-at-a-time interview until intent is predictable.
**Pros:**
- Hypothesis + confidence % protocol: forces an explicit one-sentence read with what's missing listed when <70%, making hidden assumptions auditable instead of silently baked into a PRD.
- One question + attached GUESS format, with rationale that reacting to a wrong guess is faster than generating from scratch and batches encourage skim answers.
- Checkable stop rule, not a vibe: done only when you can predict the user's reaction to the next 3 questions; plus the `want vs. should want` probe — "If you didn't have to justify this to anyone, what would you actually want?" — to puncture buzzword answers like "scalable/clean/modern".
- Tight restate template (Outcome / User / Why now / Success / Constraint / Out of scope, with Out of scope non-negotiable) and an explicit-yes gate that rejects "whatever you think", "sounds good", and silence as confirmation.
**Cons:**
- Output stops at a generic Statement of Intent saved to `docs/intent/[topic].md`; it does not map fields to the unified artifacts — no persona, user story + acceptance criteria, PRD, or DESIGN brief extraction.
- Terminal Turn rule (stop immediately on yes, do not invoke tools or start downstream work) breaks the main-agent-as-orchestrator flow, where confirmation should auto-generate the next delegation packet / spec draft behind a review gate.
- Explicitly unusable in non-interactive, CI, or autonomous contexts, and the 95% confidence target is unfalsifiable in practice and will stall small, low-risk asks that a unified suite should fast-track.
- Overlaps heavily with sibling Define-phase skills (`idea-refine`, `spec-driven-development`, `doubt-driven-development`) and with grill-style skills already in the local suite, with only prose handoff notes to separate them.
**Verdict:** ADAPT — keep the hypothesis/confidence header, one-question-with-guess loop, want-vs-should-want probe, and restate template, but replace the terminal-stop with a handoff that populates PRD/persona/story drafts, add a time/question cap and a low-risk fast path, and drop the 95% figure in favour of the predict-next-3 test alone.

### observability-and-instrumentation
**Purpose:** Instruments a feature as it is built so production behaviour is queryable via structured logs, metrics, traces, and symptom-based alerts.
**Pros:**
- Questions-first discipline: write 2–4 on-call questions before instrumenting, every signal must answer one — prevents log-everything noise and gives a concrete review-gate criterion.
- Sharp signal-selection model (metrics tell you *that*, traces tell you *where*, logs tell you *why*) plus RED (Rate/Errors/Duration) for endpoints/dependencies and USE (Utilization/Saturation/Errors) for resources.
- Concrete, stealable implementation rules: JSON logs with stable event names, mandatory correlation ID propagated across HTTP/queue boundaries, an `entryPoint` field (not ECS-reserved `source`) stamped at run start for multi-entry sinks, histogram percentiles over averages, and strict metric-cardinality bans (never user_id, raw URL, request_id, error text as labels).
- Alerting standard worth copying verbatim: symptom-only paging, actionable-only, threshold + duration justified by SLO/history, exactly two severities (page/ticket), a 3-line minimum runbook (means / first check / escalate to) in `docs/runbooks/`, and a verify step that induces a staging failure and test-fires each alert.
**Cons:**
- Stack- and scale-assumptive: TypeScript/Express, Prometheus `prom-client`, and OpenTelemetry examples, SLOs and on-call rotations — heavy for the solo/small-team products the unified suite targets, with no tiered lite version (e.g. structured logs + error tracking only).
- No artifact in the unified workflow: no telemetry-plan section for the API documentation or acceptance criteria, no mapping from user story to the question/signal that proves it works, and no dashboard/alert deliverable template.
- Blind spots for product/design work: no frontend RUM, product analytics, feature-flag exposure, or client error reporting, and retention, sampling cost, and vendor choice are mentioned only in passing.
- Duplicates neighbours: PII/secrets-in-logs is owned here and in `security-and-hardening`, regression guarding overlaps `performance-optimization`, and launch monitoring overlaps `shipping-and-launch`, with only one-line deferrals to separate them.
**Verdict:** ADAPT — keep RED/USE, correlation + entryPoint, cardinality, and symptom-alert/runbook rules as the review gate, but add a lite tier for pre-scale projects, a required Telemetry section in the API/PRD artifact (question → signal → alert → runbook per endpoint/story), and a frontend/RUM subsection; fix the dangling `../../references/observability-checklist.md` reference.

### performance-optimization
**Purpose:** Optimizes frontend, backend, and database performance only from measured bottlenecks, with a keep-or-revert decision on every fix.
**Pros:**
- Five-step loop MEASURE → IDENTIFY → FIX → VERIFY → GUARD paired with a symptom decision tree (first load vs. interaction vs. navigation vs. API, branching down to DNS/TLS/TTFB, long tasks >50ms, waterfalls) that tells you what to measure first.
- Hard thresholds and budgets: Core Web Vitals Good at LCP ≤2.5s, INP ≤200ms, CLS ≤0.1, plus enforceable budgets (JS <200KB gz, CSS <50KB gz, API p95 <200ms, Lighthouse ≥90) checkable in CI via Lighthouse CI / bundlesize.
- Best-in-set verification rigour: re-measure identically to baseline, one change at a time, delta must beat run-to-run variance, tests must stay green, and "neutral is a revert, not a keep" — backed by a ledger table (Idea / Baseline → Result / Verdict / Why, e.g. in `PERF.md`) so reverted ideas are not retried.
- Diagnostic depth, not folk remedies: for indexes require `EXPLAIN ANALYZE` and distinguish Seq Scan vs. stale `rows=` estimates (run `ANALYZE`) vs. Sort node, with cases an index cannot help (low selectivity, leading wildcard, function on column); likewise pool exhaustion signature (all endpoints slow, idle DB sessions, size `instances × max` under the DB ceiling, proxy for serverless) and cache rules (key must include tenant/locale/permissions, state staleness window, stampede protection, never cache balances/permissions).
**Cons:**
- Reference file (`references/optimization-patterns.md`, 250 lines) carries most worked fixes, so the core skill is a summary that delegates at the moment of need; the shared `../../references/performance-checklist.md` link is outside the skill folder and breaks in a repackaged unified suite.
- No intake contract with the artifact workflow: performance budgets are not pulled from the PRD/spec, there is no performance-requirement field for user stories, and no delegation packet or reviewer checklist for a subagent to execute the baseline/fix/re-measure cycle.
- Coverage is uneven and web-centric: deep on React re-renders, N+1, and image optimisation, thin on mobile, ML/inference latency, background jobs, and payload/serialization costs, despite the broad "frontend, backend, queries, databases" claim.
- Some budgets are asserted without context (200KB JS, 200ms p95) and will be wrong for data-heavy or AI products; the skill warns against guessing elsewhere but does not say to negotiate these per project.
**Verdict:** ADOPT as-is — the measure/verify/revert/ledger discipline transfers directly as the unified suite's performance review gate; only relink the two reference files into the new suite when packaging, without changing the content.

### planning-and-task-breakdown
**Purpose:** Decomposes a spec into small, ordered, vertically-sliced tasks with acceptance criteria, verification, and checkpoints.
**Pros:**
- Vertical slicing rule with a concrete contrast: not schema → all APIs → all UI, but "user can create an account (schema + API + UI)" per slice, so each task leaves a working, testable path.
- Complete per-task template: description, checkbox acceptance criteria, verification (focused test command, build command, manual check), dependencies, files likely touched, and estimated scope — directly usable as a subagent delegation packet skeleton.
- Quantified sizing: XS (1 file) to M (3–5 files, one feature slice), L (5–8) must be split, XL (8+) forbidden; split triggers are checkable — >1 focused session (~2h), >3 acceptance bullets, touches 2+ independent subsystems, or "and" in the title.
- Safety and ordering rules other planners omit: dependency graph built bottom-up, checkpoints every 2–3 tasks, high-risk tasks early, and never overwrite `tasks/plan.md`/`tasks/todo.md` with unchecked tasks for different work without asking; external trackers (GitHub/Jira/Linear/beads) mapped field-for-field instead of duplicating a markdown list.
**Cons:**
- Output model conflicts with the unified suite: it owns `tasks/plan.md` + `tasks/todo.md` as the source of truth, with no place for the PRD, DESIGN brief, personas, ERD, or API documentation to feed in, and no traceability from task back to story/acceptance criteria.
- Packet is incomplete for the orchestrator model: no context bundle, forbidden-files/do-not-touch list, ownership/conflict declaration for parallel agents, required evidence to return (diff, test output, screenshots), or subagent review gate — only a human checkpoint every few tasks.
- Assumes a single linear plan from a finished spec; no handling of design or research spikes, discovery tasks, or re-planning when ERD/API contracts change mid-build.
- Overlaps the local `to-tickets` / spec-driven family and the unified suite's own breakdown step; keeping it standalone duplicates task templates and risks two competing plan formats in one repo.
**Verdict:** ADAPT — keep vertical slicing, the sizing/split rules, dependency graph, and never-overwrite guard, but replace `tasks/todo.md` as primary output with delegation packets (add context, boundaries, return-evidence, and reviewer gate fields, plus source story/ERD/API links), and demote `plan.md` to an index of those packets or tracker items.

### security-and-hardening
**Purpose:** Hardens web applications threat-model-first against OWASP, supply-chain, privacy, and LLM-specific attacks.
**Pros:**
- Threat-model-first process that is fast and concrete: map trust boundaries (including LLM output, another process's command line/environment, filenames, and job payloads — "trust follows who *wrote* a value, not which channel delivered it"), name assets, run STRIDE per boundary, and write abuse cases next to use cases.
- Three-tier boundary system (Always Do / Ask First / Never Do) that is immediately gateable: parameterized queries, output encoding, HTTPS, bcrypt/scrypt/argon2, security headers, httpOnly/secure/sameSite cookies in Always; new auth flows, new PII categories, CORS changes, uploads, and rate-limit changes in Ask First; secrets in VCS, logging sensitive data, `eval()`/`innerHTML` on user data, tokens in localStorage in Never.
- Modern, specific controls rarely covered this well: SSRF defence resolving *all* DNS records and rejecting private/reserved IPv4+IPv6 with a named DNS-rebinding TOCTOU residual; destructive operations on derived paths requiring symlink-resolved target under an allowlisted root, at least one level below it, plus ownership evidence read before the operation; rate limiting on a shared store once >1 instance (~10 auth attempts/15 min); and secret rotation *before* history purge once pushed.
- Supply-chain and privacy sections with real procedure: find the lockfile-owning installation boundary, block install scripts before first execution and approve minimally, run the native audit against the committed lockfile, triage critical/high by reachability, never auto-apply `npm audit fix --force`, plus data classification, purpose-bound collection, retention + deletion across backups/caches/indexes, and OWASP LLM Top 10 (2025) mapping (output as untrusted input, system prompt is not a boundary, per-tenant RAG partitioning).
**Cons:**
- Scope sprawl in one skill: application hardening, dependency governance, GDPR/CCPA privacy, and LLM security together run to a long checklist plus a 324-line `references/hardening-patterns.md` and an external `../../references/security-checklist.md`; a subagent packet cannot carry it all, so teams will skim and miss the tier rules.
- No unified artifacts: threat model, data classification, and abuse cases are described in prose but given no template or home alongside the ERD (per-field classification) and API documentation (per-endpoint authz, rate limit, SSRF surface), so the work is not reviewable or traceable.
- Web/TypeScript-centric framing (helmet, cookies, CORS) with little for mobile, desktop, or ML/data pipelines, and Ask First gates assume a human approver with no escalation/severity or risk-acceptance record for the orchestrator to log.
- Overlaps neighbours without resolving ownership: PII in telemetry duplicates `observability-and-instrumentation`, incident/postmortem handling defers to `debugging-and-error-recovery`, and general input validation will duplicate API-design rules in the unified suite.
**Verdict:** ADAPT — keep the Always/Ask First/Never tiers and the SSRF, derived-path, and supply-chain procedures as the non-negotiable security gate, but split privacy and LLM sections into annexes, add fillable Threat Model and Data Classification artifacts tied to the ERD/API docs, and add a risk-acceptance entry (finding, reachability, deferral reason, review date) for the orchestrator's review log.

### shipping-and-launch
**Purpose:** Deploy to production safely via a pre-launch checklist, staged rollout, monitoring, and a reversible rollback plan.
**Pros:**
- Quantified rollout decision table worth copying verbatim: advance/hold/rollback thresholds for error rate (green within 10% of baseline, red >2x), P95 latency (green within 20%, red >50%), client JS errors (red >0.1% sessions), and business metrics (red decline >5%), applied at each canary step 5% → 25% → 50% → 100%.
- Complete feature-flag lifecycle with governance: deploy OFF → team/beta → gradual rollout → monitor → clean up, plus rules that every flag has an owner and expiration, cleanup within 2 weeks of full rollout, no nesting, and CI tests both states.
- Error-budget release gate as an objective ship/no-ship rule: >20% remaining ship normally, 0–20% slow rollouts only, exhausted freeze feature work; paired with a rollback-plan template specifying trigger conditions and time targets (<1 min flag, <5 min redeploy, <15 min DB rollback).
- Structured pre-launch checklist across Code Quality, Security, Performance, Accessibility (WCAG 2.1 AA 4.5:1, axe/Lighthouse clean), Infrastructure, and Documentation, plus a first-hour post-launch verification sequence (health 200, no new error types, latency, critical flow, logs flowing, rollback dry-run).
**Cons:**
- Assumes mature infrastructure (feature-flag service, canary infra, SLO/error-budget tracking, staged environments) with no tiered lightweight path for solo/free-tier stacks such as Vercel + Modal + managed DB, where most gates are inapplicable.
- No artifact handoff: does not consume PRD/spec acceptance criteria, DESIGN brief, or API docs as entry criteria, defines no release-notes/changelog artifact, and has no product/design sign-off gate.
- Heavy overlap with sibling skills and external references (`observability-and-instrumentation`, `security-checklist.md`, `performance-checklist.md`, `accessibility-checklist.md`, Definition of Done) that are not included in this folder, so the checklist risks becoming checkbox theatre without evidence links.
- No orchestrator mechanics: no delegation packet for the deploy, no subagent review gate before/after ship, and no assignment of who monitors the 24–48h canary windows.
**Verdict:** ADAPT (keep the rollout thresholds table, flag lifecycle, error-budget gate, and rollback template; add a tiered checklist — Lite for free-tier/single-dev launches vs Full for team/SLO services — and require linked evidence from the spec acceptance criteria, API doc, and a pre-ship review gate before the checklist can be marked green)

### source-driven-development
**Purpose:** Ground every framework-specific implementation decision in current official documentation, verified and cited, instead of training-data memory.
**Pros:**
- Tight 4-step pipeline DETECT → FETCH → IMPLEMENT → CITE: detect exact versions from `package.json`/`composer.json`/`pyproject.toml`/`go.mod`/`Cargo.toml`/`Gemfile`, state them explicitly as `STACK DETECTED:`, then fetch only the specific docs page for the pattern being built.
- Enforceable source hierarchy: 1) official docs, 2) official blog/changelog, 3) MDN/web.dev/WHATWG, 4) caniuse/node.green, with Stack Overflow, blogs/tutorials, and AI summaries explicitly banned as primary sources.
- Precise citation discipline: full URLs with deep anchors (e.g. `/useActionState#usage`), quoting the passage for non-obvious decisions, citations in code comments and conversation, and an explicit `UNVERIFIED:` flag when no official doc exists.
- Strong retrieval-safety and conflict handling: fetched docs are treated as data not instructions (extract only API signatures, examples, deprecations; ignore model-directed directives and do not hardcode endpoints from examples), and a `CONFLICT DETECTED:` template surfaces docs-vs-codebase divergence as Option A (modern pattern) vs Option B (match codebase) for a human decision.
**Cons:**
- No cost triage beyond `When NOT to use` for pure logic/typos: applied literally it burns tokens and subagent quota fetching docs for routine framework touches, with no caching, shared source log, or reuse across delegation packets.
- Citations live only in comments/chat, not in a persistent artifact (source log linked to the PRD, ERD, API documentation, or DESIGN brief), so verification is lost between orchestrator and subagents and across sessions.
- Covers only code frameworks: no equivalent hierarchy for product/design sources (design-system docs, platform HIG/Material, OpenAPI specs) needed by the unified suite.
- Brittle when versions are missing/ambiguous — it instructs to ask the user, with no fallback to lockfiles, installed-package introspection, or runtime version probes.
**Verdict:** ADAPT (keep DETECT → FETCH → IMPLEMENT → CITE, the source hierarchy, and the `UNVERIFIED:`/`CONFLICT DETECTED:` templates; add a fetch budget and a persisted sources artifact shared across packets, a triage rule exempting well-known/stable APIs in existing codebase patterns, and extend the hierarchy to design-system and API-contract sources)

### spec-driven-development
**Purpose:** Write and get human approval for a structured specification before any code, then plan, task, and implement against it in gated phases.
**Pros:**
- Hard gated workflow SPECIFY → PLAN → TASKS → IMPLEMENT with the suite's best review gate: after saving the spec, summarize, list Open Questions, ask for approval, and `STOP YOUR TURN IMMEDIATELY` — planning may only start in a later turn after approval, which maps directly to a main-agent orchestrator gate.
- Phase 0 capability map for multi-capability requests: decompose first with a small module table (stable kebab-case module ids never renamed, one-way dependencies with no cycles, build order, interfaces at the provider boundary), get it approved, then recurse per module with `SPEC-<module-id>.md` files — the map, not filename guessing, is the index.
- Concrete spec mechanics: surface an `ASSUMPTIONS I'M MAKING:` list before writing, cover six core areas (Objective, Commands with full flags, Project Structure, Code Style via a real snippet, Testing Strategy, Boundaries), use the three-tier Boundaries system (Always do / Ask first / Never do), and reframe vague requirements into testable success criteria (e.g. "faster" → LCP <2.5s on 4G, load <500ms, CLS <0.1).
- Living-spec discipline: update the spec before changing code when decisions/scope change, commit it with the code, reference it in PRs, and stay format-agnostic if the project already uses OpenSpec or another spec system.
**Cons:**
- Template is code-centric and underserves the unified artifact workflow: personas, user stories + acceptance criteria, ERD, API documentation, and DESIGN brief have no dedicated sections or linked sub-artifacts and would be squeezed into Objective/Tech Stack.
- Significant overlap with `planning-and-task-breakdown`, which it defers to as canonical for both Plan and Tasks phases, making Phases 2–3 largely a summary; the ~5-files-per-task sizing rule is stated without rationale.
- Rigid for the orchestrator model: human approval at every phase and a vague `>30 minutes` trigger, with no fast-track or subagent-internal mini-spec for small bounded delegation packets, risks bottlenecking parallel work.
- No traceability or quality rubric linking story → acceptance criterion → task → test, and no check that success criteria are complete beyond being "specific and testable."
**Verdict:** ADAPT (adopt the gated workflow, Phase 0 capability map, assumption-surfacing, reframing, and hard stop-after-spec rule as-is; expand Phase 1 to require/link the unified artifacts — PRD objective, personas, user stories + acceptance criteria, ERD, API doc, and DESIGN brief — as named spec sections, and add a traceability table and a lightweight packet-spec variant for subagent tasks)

### test-driven-development
**Purpose:** Drive implementation and bug fixes with a failing-test-first red-green-refactor loop so behavior is proven, not assumed.
**Pros:**
- Stack-discovery first step that prevents false defaults: read `package.json`/`pom.xml`/`pyproject.toml`/`go.mod`/`Cargo.toml`, prefer checked-in wrappers (`./gradlew`, `./mvnw`, `make test`) and README/CI commands, learn focused-test vs full-suite commands and local test conventions before writing the first test.
- Named, reusable patterns: RED (test must fail) → GREEN (minimal code) → REFACTOR (tests still pass), and the Prove-It Pattern for bugs (reproduction test fails → fix → passes → full suite), plus a test pyramid (unit ~80% / integration ~15% / E2E ~5%) with a resource size model (Small: single process, no I/O, ms; Medium: localhost only, seconds; Large: external services, minutes) and a decision guide (pure logic → unit, boundary-crossing → integration, critical flow → E2E).
- Specific test-quality rules: test state not interactions, DAMP over DRY (each test reads as a self-contained specification), real implementations > fakes > stubs > mocks with mocks only for slow/non-deterministic/side-effectful boundaries, Arrange-Act-Assert, one assertion per concept, and descriptive specification-style names.
- Orchestrator-ready elements: spawn a subagent blind to the fix to write the reproduction test for complex bugs, a browser DevTools verification loop REPRODUCE → INSPECT → DIAGNOSE → FIX → VERIFY (console/network/DOM/styles/performance/screenshots), an anti-pattern table, and the rule never to re-run the same test command on unchanged code.
**Cons:**
- Rigidity: test-first for "any logic, any bug, any behavior change" with no exemption path for prototypes, exploratory UI/design work, or glue code makes it hostile to the design and product phases of the unified suite.
- No linkage to the artifact workflow: tests are not traced to user-story acceptance criteria, API contracts, or DESIGN states; no contract testing, visual-regression, or accessibility test guidance despite those artifacts being first-class in the target suite.
- Examples are uniformly TypeScript/TaskService despite the language-agnostic framing, and there is no guidance for non-deterministic ML/data work, notebooks, or snapshot/golden-file testing relevant to AI projects.
- Overlaps `debugging-and-error-recovery`, `browser-testing-with-devtools`, and the shared Definition of Done in verification, with coverage mentioned only as "hasn't decreased (if tracked)" and no thresholds or flakiness quarantine process.
**Verdict:** ADAPT (keep stack discovery, Prove-It, pyramid/size model, DAMP, real-over-mock preference, and the blind-subagent reproduction pattern; relax strict test-first to test-first for logic/bug fixes and test-alongside for UI/prototype slices, and add acceptance-criteria-to-test traceability plus contract and visual/accessibility test types tied to the API doc and DESIGN brief)

### using-agent-skills
**Purpose:** Meta-skill that routes any incoming task to the right workflow skill by development phase and enforces core operating behaviors across all skills.
**Pros:**
- Complete routing decision tree and taxonomy reusable as an orchestrator routing table: task signals map to 22 skills across Define / Plan / Build / Verify / Review / Ship (e.g. unknown wants → `interview-me`, rough concept → `idea-refine`, new feature → `spec-driven-development`, UI → `frontend-ui-engineering`, doc-verified code → `source-driven-development`), plus a Quick Reference table with one-line summaries per skill.
- Canonical 16-step lifecycle sequence from `interview-me` through `shipping-and-launch`, with explicit notes that observability runs parallel with implementation (steps 7–9, not after) and that partial sequences are valid (bug fix = debugging → TDD → code review), preventing all-or-nothing application.
- Six portable Core Operating Behaviors with concrete formats: Surface Assumptions (`ASSUMPTIONS I'M MAKING:` block), Manage Confusion Actively (STOP, name it, present tradeoff, wait), Push Back When Warranted (state issue, quantify downside, propose alternative, accept override), Enforce Simplicity, Maintain Scope Discipline (do not clean up orthogonal code, remove comments, or add unspec'd features), and Verify, Don't Assume (evidence required, backed by a project-wide Definition of Done).
- Checkable failure-mode list (10 items: unchecked assumptions, plowing ahead when lost, sycophancy, overcomplication, orthogonal edits, building without a spec, skipping verification, etc.) and skill rules (check for a skill before starting, skills are workflows not suggestions, multiple skills chain, when in doubt start with a spec).
**Cons:**
- Routing is verb/phase-based and locked to the Addy skill names: it routes by what the task sounds like, not by artifact state (which of PRD, personas/stories, ERD, API doc, DESIGN brief exist or are approved), and it has no product/design discovery phases beyond a single UI skill.
- No orchestrator mechanics at all despite being the meta-skill: no delegation packet format, subagent spawning/review gates, handoff artifacts, context/quota management, or parallel-vs-sequential dispatch rules — it assumes one agent invoking skills in sequence.
- Duplicates sibling content (assumption block repeats `spec-driven-development`, simplicity/scope repeat code-review/simplification), creating drift risk if kept as a separate skill in the unified suite.
- No conflict or priority resolution when several skills trigger at once, and no entry/exit criteria per transition, so two agents can legitimately route the same task differently.
**Verdict:** ADAPT (keep the phase taxonomy, routing tree, lifecycle sequence, and the six Core Operating Behaviors as the unified suite's orchestrator core; rewrite routing to be artifact-state-driven for the PRD/DESIGN/personas/stories/ERD/API workflow, add delegation-packet and subagent review-gate stages, define tie-breaking and entry/exit criteria per handoff, and deduplicate behaviors so this is the single source other skills reference)

## Batch summary

### Internal overlaps (must be resolved to a single owner in the unified suite)

- **Commit/branch/flag rules** are claimed by three skills: `git-workflow-and-versioning`, `incremental-implementation`, and `ci-cd-and-automation` (plus flag lifecycle again in `shipping-and-launch`). Owner: git-workflow.
- **Simplification/readability/dead code:** `code-simplification` is almost fully subsumed by `code-review-and-quality`'s Readability axis + Structural Remedies — the reason code-simplification is a DROP.
- **Security & performance axes:** `code-review-and-quality` duplicates the cores of `security-and-hardening`, `performance-optimization`, `observability-and-instrumentation` (PII in logs claimed by both observability and security), and several skills point at shared `../../references/security-checklist.md` / `performance-checklist.md` / `accessibility-checklist.md` / `observability-checklist.md` files that are **not present in the installed folders** — dead links that break on repackaging. The same applies to the shared Definition of Done referenced by TDD, incremental-implementation, using-agent-skills, and shipping-and-launch.
- **Thresholds are re-stated, not referenced:** `constraint-driven-development` re-declares thresholds owned by TDD, security, performance, and CI instead of pointing at them; sizing numbers conflict slightly across skills (~100 lines before testing vs ~100/300/1000 per commit/PR vs XS–XL file counts in planning).
- **Define-phase trio:** `interview-me`, `idea-refine`, and `spec-driven-development` overlap on intent extraction and assumption-surfacing (the `ASSUMPTIONS I'M MAKING:` block appears in both spec-driven and using-agent-skills); no routing rule decides which discovery skill runs first.
- **Verification loops:** debugging's regression guard, TDD's Prove-It, browser-testing's REPRODUCE→VERIFY, and code-review's mutation check are four versions of the same evidence idea with no shared vocabulary.

### What the batch does well as a lifecycle

- **A complete, correctly ordered spine exists.** `using-agent-skills` supplies a Define → Plan → Build → Verify → Review → Ship taxonomy and a canonical 16-step sequence, and correctly notes that partial sequences are valid (a bug fix is debugging → TDD → review, not the whole chain) and that observability runs parallel to implementation rather than after it.
- **Gates are quantified, not vibes.** Nearly every stage has numbers a reviewer can check: ~100/300/1000-line sizing (git, review), XS–XL task sizing with split triggers (planning), coverage ≥80% on changed lines and check-time budgets of 5s/90s/CI (constraints), Core Web Vitals and bundle budgets (performance, frontend), canary advance/hold/rollback thresholds and an error-budget ship gate (shipping).
- **Anti-self-deception machinery is the batch's signature strength.** Doubt-driven's ARTIFACT+CONTRACT-only blind review, code-review's mutation check and "verify the verification," performance's "neutral is a revert" plus a reverted-ideas ledger, constraint's floor-guard against test-weakening diffs, TDD's blind-subagent reproduction test, and source-driven's `UNVERIFIED:` flag all attack the same failure — an agent grading its own homework — from different angles.
- **Safety and honesty are treated as defaults:** browser content, error output, fetched docs, and LLM output are all explicitly untrusted data; security's Always/Ask First/Never tiers are gateable as written; fallbacks and scope discipline (CHANGES MADE / DIDN'T TOUCH, NOTICED BUT NOT TOUCHING) make silent drift visible.

### What it lacks for (a) an artifact-based workflow

- **No product artifacts exist at all.** There is no PRD template, no user persona format, no user-story + acceptance-criteria format, no ERD notation or conventions, and no user-flow artifact. `interview-me` stops at a generic Statement of Intent; `idea-refine`'s one-pager is explicitly not a PRD; `documentation-and-adrs` covers only ADRs, README, changelog, and API snippets.
- **API documentation is guidance, not an artifact.** `api-and-interface-design` has excellent design rules and an idempotency playbook but no OpenAPI/endpoint-inventory artifact, no auth/rate-limit sections, and no link from endpoints to ERD entities or story IDs.
- **Traceability is missing end-to-end.** Nothing links story → acceptance criterion → task → test → commit. Planning's task template, TDD, and code review each say "matches spec" in passing, but there is no ID scheme, no traceability table, and no artifact-sync step when implementation drifts from the ERD/API doc/DESIGN brief mid-slice.
- **Design is one implementation skill, not an artifact stage.** `frontend-ui-engineering` has a good design-contract step but consumes no approved DESIGN brief, personas, or stories, and produces no handoff artifact; there is no design-review gate anywhere in the batch.
- **Artifacts have no lifecycle governance.** No owner/status/review-date fields, no supersession links (outside ADRs), no drift checks between docs and code, and no gate where an orchestrator verifies artifact completeness before implementation starts.

### What it lacks for (b) a main-agent-as-orchestrator model

- **No delegation packet format.** The pieces exist scattered — planning's per-task template, context-engineering's packing patterns and restartable-session checklist, incremental's per-slice cycle — but no skill defines a packet with context bundle, boundaries/do-not-touch list, ownership declaration for parallel agents, required return evidence, and a review gate. `using-agent-skills`, the meta-skill, assumes a single agent invoking skills in sequence.
- **Review gates are human-PR-shaped, not agent-shaped.** Code review assumes a one-business-day human SLA and ends at "human makes the final call"; doubt-driven demands a cross-model offer every cycle (unaffordable on a delegated-quota model) and produces no gate record; no skill defines pass/fail verdict formats, re-review loops, retry budgets, or escalation rules (CI feedback is manual copy-paste; debugging has no timebox or hand-back rule).
- **Routing is by verb, not by state.** `using-agent-skills` routes on what a task sounds like, not on which artifacts exist/are approved; there are no entry/exit criteria per phase transition and no tie-breaking when several skills trigger at once.
- **No resource economics.** Nothing budgets context per packet beyond context-engineering's trimming rules, no quota awareness for delegated workers, no parallel-vs-sequential dispatch rules (git worktrees are mentioned, but no ownership/conflict protocol), and source-driven has no fetch budget or shared source cache across packets.
- **Environment mismatch to fix during adaptation:** hard dependencies on `chrome-devtools-mcp`, GitHub Actions/npm/Vercel, React/Tailwind, and Claude Code personas recur across the batch; the unified suite needs tool-agnostic protocols and stack adapters (Python/FastAPI, Modal, TiDB, Playwright/live browser) instead.

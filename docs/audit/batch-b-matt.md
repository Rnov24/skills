# Audit Batch B — Matt Pocock Skills & Their Local Counterparts

Scope: all 38 `local-mp-*` skills plus the evolved/recovered local versions (`local-to-spec`, `local-to-tickets`, `local-grilling`, `local-grill-with-docs`, `local-research`, `local-prototype`, `local-domain-modeling`, `local-implement-spec`, `local-to-questionnaire`, `local-writing-for-agents`, `local-setup-matt-pocock-skills`, `local_engineering_workflow`). Every `SKILL.md` was read in full. Duplicates are audited once.

**Verdict tally: ADOPT 15 · ADAPT 15 · DROP 9** (39 distinct skills).

## Duplicate-pair ruling (read this first)

11 skills exist in both `local-mp-*` and plain `local-*` form. Diffing them shows the plain `local-*` copies are **recovered copies, not evolutions**: the body text is verbatim identical to the mp copy, but the YAML frontmatter (`name`, `description`, `disable-model-invocation`) has been stripped out (the description survives only in a sidecar `skill.yaml`), and a generic "Available connectors — use `muse.connector_search`…" boilerplate tail has been appended. Consequences:

- **Winner in 10 of 11 pairs: the `local-mp-*` copy.** It keeps invocation metadata (several of these skills are deliberately user-invoked only; losing `disable-model-invocation` changes when they fire), and its body is equal or fuller. `local-implement-spec` is missing the whole goal / task-graph / context-pointer preamble the mp copy has; `local-setup-matt-pocock-skills` drops the step that creates the configured triage labels on GitHub/GitLab; `local-to-tickets` drops the "omit Blocked-by when native edges were set" rule.
- **The one real exception is `grilling`** (below): the local copy was genuinely rewritten — it merges in the write-docs-as-you-go discipline and adds alternatives pointers — but loses the mp copy's frontmatter and its ❓/➡️ round formatting. Correct move: merge, taking mp packaging + local content additions.
- **`local_engineering_workflow` has no mp counterpart** — it is a genuine local creation (a Muse-native composite of setup + to-spec + to-tickets + implement-spec) and is audited on its own at the end.

---

## The skills

### ask-matt
Router over the whole suite: maps a situation to the main flow (idea → ship), the two on-ramps (triage, diagnosing-bugs), wayfinder, and the standalone skills, plus phase-boundary and context-hygiene rules.
- Pros: The only place the whole system is drawn as one map, including branch conditions ("can every question be settled in conversation?", "is this a multi-session build?"). Phase-boundary decision tree (Continue / clear / handoff / subagent / compact, in cost order) is genuinely useful orchestration knowledge. Insists the router read a skill's SKILL.md before summarising or skipping it.
- Cons: Hard-wired to Claude Code idioms (`/clear`, `/compact`, a "~150k smart zone") that don't transfer to other harnesses. User-invoked only, so the agent never routes proactively. The map covers engineering only — no product-discovery or design phases exist for it to route to.
- **Verdict: ADAPT** — keep the map-and-branches structure as the rnov24 suite router, rewrite the phase-boundary rules in harness-neutral terms, and extend the main flow backwards into product/design phases.

### chief-of-staff
Long-running single-session coordinator: all work done by subagents, sparse communication via context pointers, constant pressure to improve the agent's environment ("pit of success").
- Pros: Names the orchestrator stance explicitly — tactical track plus strategic track (improve the environment for the *next* task). "All work in subagents, protect your context window" and pointer-based communication are exactly the delegation hygiene the rnov24 suite wants. The pit-of-success checklist (constrained APIs, lint rules, CODING_STANDARDS.md, log/data access) is a concrete environment audit.
- Cons: Almost no mechanics: no packet format, no report format, no completion criteria, no review step, no failure handling — it is a posture, not a workflow. Assumes one immortal session accruing "tribal knowledge," which is the opposite of the suite's artifact-based, fresh-context-per-ticket model. "Be relentless… use every user message as an excuse" invites scope creep.
- **Verdict: ADAPT** — keep it as a short orchestrator charter, but bolt on the concrete contracts it lacks (bounded packets, structured worker reports, independent review) from implement-spec and the local agy-delegation practice.

### claude-handoff
Writes a handoff summary and immediately launches a fresh background agent with it via `claude --bg`.
- Pros: The handoff content rules (suggested-skills section, reference don't duplicate, redact secrets) are sound and shared with `handoff`. Auto-launching the successor removes a manual step.
- Cons: Entirely dependent on the Claude Code CLI's background-agent feature — dead weight in any other harness. Passing a summary as a shell argument is fragile despite the `$(cat …)` workaround. Strictly worse than `handoff` + native subagent spawning, which the parent system already has.
- **Verdict: DROP** — keep `handoff` for the document; launching is the orchestrator's job, not a skill's.

### code-review
Two-axis review of a diff against a fixed point: Standards (repo's documented standards + a Fowler smell baseline) and Spec (the originating issue/spec), run as parallel sub-agents and reported side by side, never merged.
- Pros: The two-axis separation is the single best review idea in the batch — code can pass one axis and fail the other, and aggregating would let one mask the other. Fixed point is pinned and validated (`git rev-parse`, non-empty diff) before any subagent runs. Spec-source lookup order and standards-source discovery are concrete; the smell baseline is explicitly subordinate to documented repo standards and always labelled a judgement call. Sub-agent briefs are tight, with word caps and per-axis report formats.
- Cons: Useless on the Spec axis when no spec/ticket exists (it degrades gracefully, but the suite must guarantee a spec artifact upstream). 400-word caps can truncate a large diff's findings. No severity ranking *within* an axis and no defined fix-and-re-review loop (that lives, thinly, in implement/implement-spec).
- **Verdict: ADOPT** — this becomes the suite's review core unchanged; the rnov24 additions belong around it (per-ticket review, a fix loop, a design axis), not inside it.

### codebase-design
Vocabulary reference for deep modules: module, interface, depth, seam, adapter, leverage, locality; the deletion test; "the interface is the test surface"; one adapter = hypothetical seam, two = real.
- Pros: A small, exact, enforceable vocabulary that tdd, improve-codebase-architecture, and setup-ts-deep-modules all speak — shared language is what makes their outputs comparable. The principles are falsifiable in practice (deletion test, test-past-the-interface smell). Explicitly rejects the Ousterhout lines-ratio framing and says why.
- Cons: Pure vocabulary — no process, no artifact, no completion criteria; value only shows up through the skills that consume it. Examples and mindset are backend/TS-flavoured; nothing about UI component depth. The "use these terms exactly, never say component/service/API" policing can become pedantry if applied to user-facing prose.
- **Verdict: ADOPT** — keep as the architecture vocabulary layer under the suite.

### diagnosing-bugs
Six-phase diagnosis discipline whose centre of gravity is Phase 1: build a tight, red-capable feedback loop before any theorising; then reproduce + minimise, 3–5 falsifiable hypotheses, tagged instrumentation, fix + regression test, cleanup checklist.
- Pros: The red-capable completion criterion is exemplary — one named command, already run, deterministic, fast, agent-runnable, asserting the user's exact symptom. "No red-capable command, no Phase 2" is a hard gate that kills the most common debugging failure (hypothesising from code-reading). Minimisation, hypothesis format ("If X, then changing Y…"), `[DEBUG-xxxx]` log tagging, and the Phase 6 cleanup checklist are all concrete and portable. Perf regressions get a separate measure-first branch.
- Cons: Heavy ceremony for a trivial bug; it says "skip phases only when explicitly justified" but gives no fast path. Phase 5 honestly flags "no correct seam" as an architecture finding, but then the skill just ends — the hand-off to improve-codebase-architecture is only implied here (ask-matt states it). Assumes an environment the agent can run loops in unattended.
- **Verdict: ADOPT** — adopt whole; add one line routing the no-seam finding to the architecture skill.

### domain-modeling *(mp copy wins over local)*
Active discipline for sharpening the domain model: challenge terms against `GLOSSARY.md`, propose canonical terms, stress-test with concrete scenarios, cross-check claims against code, update the glossary inline, offer ADRs only when hard-to-reverse + surprising + a real trade-off.
- Pros: The inline-update rule (write the term the moment it resolves, never batched) is what keeps a glossary alive instead of aspirational. The three-gate ADR test is a sharp, memorable filter against ADR spam. Lazy file creation and the single- vs multi-context (`GLOSSARY-MAP.md`) layout scale from solo repos to monorepos. "Glossary is totally devoid of implementation details" keeps the artifact clean.
- Cons: Vocabulary-only modelling — it sharpens *words*, but produces no entity/relationship model, so there is no bridge from glossary to ERD or data schema (a real gap for the rnov24 suite's artifact set). Depends on companion format files (GLOSSARY-FORMAT.md, ADR-FORMAT.md) being present.
- **Verdict: ADOPT** — adopt the mp copy; the rnov24 suite should add a data-modelling companion that turns glossary terms into entities/ERD rather than stretching this skill.

### git-guardrails-claude-code
Installs a Claude Code PreToolUse hook that blocks `git push`, `reset --hard`, `clean -f`, `branch -D`, `checkout .`/`restore .`.
- Pros: Concrete, verifiable (ships a test invocation with expected exit code 2), asks scope (project vs global) and merge-don't-overwrite for settings. Blocking at the tool layer beats instructing the model not to.
- Cons: Entirely Claude-Code-specific (`.claude/settings.json`, hook protocol). On this stack, destructive-action control already belongs to the platform permission system, so the skill duplicates a platform feature. The blocked list is all-or-nothing — blocking *every* push also blocks the legitimate push at the end of implement.
- **Verdict: DROP** — the *idea* (a destructive-git denylist) survives as one checklist line in the suite's setup skill; the harness-specific installer does not.

### grill-me
Seven-line stub: "Call the Skill tool with grilling." The stateless entry point to the interview — no working directory, nothing saved.
- Pros: Correctly recognises that the same interview primitive needs a no-paper-trail mode for plans/designs/writing with no repo underneath.
- Cons: It is an alias, not a skill — a whole discoverable slot spent on one line. Keeping grill-me, grill-with-docs, and grilling as three separate skills is exactly the cognitive load writing-for-agents warns about.
- **Verdict: ADAPT** — fold into `grilling` as an invocation mode (stateless), don't ship as a separate skill.

### grill-with-docs *(mp copy wins over local)*
Seven-line stub composing `grilling` + `domain-modeling`: interview that also writes glossary terms and ADRs as it goes.
- Pros: The composition itself is the insight — the interview is where domain language gets decided, so capturing it inline (not in a later docs pass) is the right default whenever a repo exists; ask-matt rightly makes it the main flow's step 1.
- Cons: Same alias-not-a-skill problem as grill-me. The stub carries zero guidance about when docs capture should *not* happen (e.g. exploratory grilling the user doesn't want persisted).
- **Verdict: ADAPT** — fold into `grilling` as the default with-docs mode when a working directory exists.

### grilling *(merge: mp packaging + local content)*
The interview primitive: map the plan as a decision tree, work it in rounds along the **frontier** (decisions whose prerequisites are settled), give a recommended answer per question, dispatch subagents for facts, never act until the frontier is empty and the user confirms shared understanding.
- Pros: Frontier/rounds is a real algorithm, not a vibe — it prevents asking questions whose answers depend on still-open questions, and each round visibly reshapes the tree. "Facts are the agent's job, decisions are the user's" plus non-blocking subagent fact-finding is excellent delegation hygiene. The recommended-answer-per-question format makes "yes" cheap for the user.
- Cons: Asking the *whole frontier at once* produces long multi-question rounds that can overwhelm — for this user specifically, one sharp question per turn has proven to land better than a numbered deck, so the round size needs a cap or a one-at-a-time variant. No artifact of its own: without the docs mode, a long grilling leaves nothing behind. The mp copy's ❓/➡️ formatting is nicer than the local copy's bullets.
- Local vs mp: the **local copy is the one genuine evolution in this batch** — it adds a "write docs as you go" section (glossary inline, ADR three-gate, pointing to local-domain-modeling for formats) and an alternatives footer (questionnaire when the knowledge is someone else's; engineering workflow when the interview ends). But it loses the frontmatter and the round format block.
- **Verdict: ADOPT (merged)** — mp copy as the base (frontmatter, round format), graft the local copy's docs-as-you-go section and alternatives pointers, and add a round-size dial (full frontier vs one-question turns).

### handoff
Compacts the current conversation into a handoff document in the OS temp dir: suggested-skills section, reference artifacts instead of duplicating them, redact secrets, tailor to the stated purpose of the next session.
- Pros: Short, complete, and correct about the failure modes (duplication, secret leakage). "Reference by path or URL" keeps handoffs small and single-sourced.
- Cons: Temp-dir storage is the wrong default on this stack — ephemeral, undiscoverable later, and exactly where artifacts go to die; an artifact-based suite should file handoffs in the project. No structure/template for the document body itself, so quality varies by run.
- **Verdict: ADAPT** — keep the rules, change the destination to a project artifacts location (e.g. `docs/handoffs/` or the feature's `.scratch/` folder) and add a minimal body template.

### implement
Seventeen-line per-ticket driver: fetch the ticket, build it via tdd at pre-agreed seams, typecheck/test regularly, full suite at the end, code-review, commit.
- Pros: Deliberately thin — it composes tdd + code-review rather than restating them, which is the suite's best structural habit. The cadence (single test files regularly, full suite once at the end) is a sensible cost rule.
- Cons: Too thin to be safe: no check that the ticket's acceptance criteria are actually met, no structured report back (what was built, what was verified, what's left), commits unconditionally with no branch hygiene, no behaviour specified for a blocked or ambiguous ticket beyond asking. As an orchestrator contract it trusts the implementer completely.
- **Verdict: ADAPT** — keep the composition, add an acceptance-criteria check against the ticket, a fixed completion report, and a no-commit-until-review-passes rule.

### implement-spec *(mp copy clearly wins)*
The orchestrator: read spec + tickets as a task graph, optional exploration subagent, create an integration branch, run implementer subagents per frontier ticket in their own worktrees, merge via a merger subagent, unblock and dispatch more, one code-review over the integration branch at the end, draft PR, clean up worktrees.
- Pros: The most complete delegation design in the batch — frontier-driven parallelism, worktree isolation per implementer, a dedicated merger role, exploration separated from implementation, sparse pointer-based communication, and a single integration branch as the merge artifact. The mp copy's preamble (goal, "tickets are a task graph, not a list of steps," background subagents for maximum concurrency) is load-bearing and the local copy lacks all of it.
- Cons: Review happens only once, at the very end, over the whole integration branch — a bad ticket can contaminate merges before anyone looks; there is no per-ticket review or acceptance gate. The end-of-run review fixes are funnelled into a *single* implementer subagent (a bottleneck and a context risk). No worker report schema, no verification that a subagent's "done" is true, no retry/escalation path for a failed or stuck subagent, no merge-conflict protocol beyond the merger role. Assumes git worktrees and a configured tracker throughout.
- **Verdict: ADOPT** — adopt the mp copy as the suite's orchestration core; its gaps (per-ticket gates, report schema, escalation) are the rnov24 layer to add on top, listed in the summary.

### improve-codebase-architecture
Scans for deepening opportunities (hotspot-first via commit history), presents candidates as a visual HTML report with before/after diagrams and recommendation-strength badges, then grills the chosen candidate with domain-modeling side effects.
- Pros: Scoping by recent-change hotspots (YAGNI) instead of scanning everything is the right economics. Refusing to propose interfaces before the user picks a candidate keeps the report honest. ADR-conflict handling (surface only when friction warrants reopening, with a warning callout) respects recorded decisions. The post-pick loop correctly reuses grilling + domain-modeling + codebase-design's design-it-twice.
- Cons: The HTML report is written to the temp dir and built on Tailwind/Mermaid CDNs — it evaporates and can fail to load in restricted-network environments; an artifact-based suite wants this as a durable repo document. Scope is narrow by design (only deepening; no other architecture smells get a look-in).
- **Verdict: ADAPT** — keep the process, emit the report as a persistent Markdown artifact in the repo (diagrams as Mermaid source), keep HTML only as an optional render.

### loop-me
Stateful grilling whose only output is workflow specs (`workflows/*.md`): views life as loops within loops, with a small vocabulary (trigger, checkpoint, push right, brief).
- Pros: "Push right" (defer the human checkpoint as far as possible) and the **brief** (a decision-ready summary, never raw output) are excellent checkpoint-design ideas. Definition of done — "an implementer agent could build it without asking a single question" — is a properly demanding completion criterion.
- Cons: It is a personal-life workflow tool that happens to live in the repo; it contributes nothing to building software. Its workspace conventions (`NOTES.md`, `workflows/`) are a second, incompatible artifact system next to the engineering suite's.
- **Verdict: DROP** from the rnov24 dev/product/design suite — but salvage *push right* and *brief* into the orchestrator's human-checkpoint design before dropping.

### migrate-to-shoehorn
Mechanical migration of test files from `as` assertions to `@total-typescript/shoehorn` (`fromPartial` / `fromAny` / `fromExact`), with grep-driven workflow.
- Pros: Well-scoped and honest about its limits (test code only), with a clear pattern table.
- Cons: A single-library, single-language migration recipe. It is a runbook for one author's course ecosystem, not a reusable capability; the chance it ever fires again in this suite is negligible.
- **Verdict: DROP**.

### pr
PR-body template (credited to Dex Horthy's show-me skill): Summary as the smallest visual that shows the change (pseudocode, call tree, component tree, file tree, Mermaid, or shaped diff), before/after Evidence, and Merge Danger (one-way/two-way door + blast radius).
- Pros: "Smallest visual that makes the point" plus a menu of visual forms matched to change type is genuinely good communication design. Before/after evidence as a required section turns PRs into verification artifacts. The door/blast-radius framing forces an explicit reversibility judgement on every merge.
- Cons: Template only — no process for producing the evidence (screenshots assumed "when the environment is set up for it"). No link back to spec/tickets, so the PR doesn't close the artifact chain. Third-party credit line needs carrying if republished.
- **Verdict: ADOPT** — add a "Spec / tickets" link line when the rnov24 suite adopts it; keep the credit.

### prototype *(mp copy wins; bodies identical)*
Throwaway code that answers one question, with two branches: logic/state-model (single shareable HTML file with guided walkthroughs) or UI (several radically different variants on one route behind a URL param). Rules: marked throwaway, trivial to run, no persistence, surface the state, capture the verdict and keep the prototype as a primary source on a throwaway branch.
- Pros: "The question decides the shape" and the explicit warning that picking the wrong branch wastes the whole prototype. The capture rule is the artifact discipline the suite wants: validated decision folds into real code/spec, prototype itself preserved as a primary source with a context pointer from the issue. Surface-the-state makes prototypes readable by non-developers.
- Cons: The UI branch is a *variation generator*, not a design process — no personas, no user flow, no design rationale, no DESIGN artifact comes out of it, and "several radically different variants" can produce breadth without a decision method. No criteria for what counts as the question being answered.
- **Verdict: ADOPT** — adopt as the suite's prototyping skill; the design-phase extension (verdict + rationale recorded as a design artifact) belongs in the new design skills, not here.

### research *(mp copy wins; bodies identical)*
Delegates a question to a background agent that investigates primary sources only and leaves a single cited Markdown file in the repo.
- Pros: Primary-sources-only is the right bar, stated in one line ("follow every claim back to the source that owns it"). Background-agent framing keeps the main context free. Output is a durable, cited file — a proper artifact other skills can point at.
- Cons: Twelve lines is under-specified: no findings template, no claim/source table format, no handling of conflicting sources or confidence, no naming/location convention beyond "somewhere sensible." Quality will vary wildly run to run.
- **Verdict: ADAPT** — keep the bar and the delegation model, add a findings template (question, claims with citations, conflicts, open questions) and a default save location.

### retro
Retrospective on a coding session that improves the agent's *environment*, not the code: navigation pointers, automated checks, coding standards, AGENTS.md hygiene, tool economy, no-op instructions, information access. Mechanical mistakes become deterministic checks; judgement calls become standards.
- Pros: The mechanical → check / judgement → standard classification is a sharp rule that prevents both lint-bloat and standards-bloat. Noticing "a repo with no guardrail at all is itself a finding" and "check that already exists but is unwired" shows real diagnostic taste. The implementation-vs-review context-pressure note (review agent should carry standards enforcement) is a sophisticated orchestration insight. It closes the main flow's loop: this session's mistakes become next session's environment.
- Cons: Depends on access to session logs, which is harness-specific. No output artifact or template — candidates are "presented to the user" and can evaporate. Calls writing-for-agents first, a dependency a reader can't see from the description.
- **Verdict: ADOPT** — adopt; file the accepted changes as a short retro artifact when the suite wraps it.

### scaffold-exercises
Scaffolds course-exercise directory trees (sections, problem/solution/explainer variants, stub readmes) that pass `pnpm ai-hero-cli internal lint`, using `git mv` for renumbering.
- Pros: Internally consistent and lint-verified; the git-mv-for-history point is good practice.
- Cons: Hard-bound to one author's course platform and its private lint rules. Nothing in it generalises to developing, designing, or shipping product.
- **Verdict: DROP**.

### setup-matt-pocock-skills *(mp copy wins)*
One-time per-repo bootstrap: explore the repo, then configure the three things every other skill assumes — issue tracker (GitHub/GitLab/local markdown/other), the five canonical triage labels, and the domain-doc layout — writing `docs/agents/*.md` and an `## Agent skills` block into the existing CLAUDE.md/AGENTS.md.
- Pros: This is what makes the rest of the suite *portable*: skills read configuration from `docs/agents/` instead of hard-coding a tracker. Explore → present → confirm → write, one section one answer, with recommended defaults the user can accept in a word. Careful file etiquette (never create AGENTS.md when CLAUDE.md exists, update an existing block in place, skip sections exploration already settled). The local-markdown tracker option makes the whole suite work with no external service.
- Cons: Branded and framed around Matt's suite specifically. The configuration surface covers tracker/labels/domain docs only — nothing for product or design artifacts (where PRDs, personas, design docs live), because the suite has none. Label creation on the tracker (present in mp, dropped in local) makes setup partially a write operation users may not expect.
- **Verdict: ADAPT** — adopt the pattern wholesale as the rnov24 suite's setup skill, rebranded, and extend the config with artifact locations for product/design docs and the delegation engine choice.

### setup-pre-commit
Installs Husky + lint-staged + Prettier, wires typecheck and tests into the pre-commit hook, verifies, and commits through the new hooks as a smoke test.
- Pros: End-to-end concrete with a verification checklist and the nice touch of letting the setup commit itself exercise the hooks. Package-manager detection and "omit lines for scripts the repo lacks" show restraint.
- Cons: JavaScript-only and opinionated (imposes Prettier defaults on repos that may have chosen otherwise). Running the *full* test suite on every commit is a slow-hook anti-pattern for larger repos. Overlaps retro's guardrail thinking without referencing it.
- **Verdict: ADAPT** — generalise into a stack-detecting guardrail setup (fast staged checks by default, full suite in CI), aligned with retro's "no guardrail is a finding" rule.

### setup-ts-deep-modules
Wires dependency-cruiser into a TypeScript repo so every package is a deep module: root files are entry points, subfolders are private, tests go through entry points, no cycles — then *proves the rules bite* with a pass → fail → pass demonstration.
- Pros: The prove-it-bites completion criterion (temporarily add a forbidden deep import and watch it fail) is the best verification pattern in the batch — a guardrail that has never failed is not a guardrail. "Entry points, not a barrel" and depth-decided privacy (any subfolder is private, so config never grows) are elegant, low-maintenance rules. Ships an example package as a copy-me template.
- Cons: TypeScript-only, and the prescribed layout (`src/packages/<name>/{lib,tests}`) is a strong structural opinion that fits monorepos far better than the small apps this user usually builds. Installing an enforcement tool is a bigger commitment than a skill usually makes.
- **Verdict: ADAPT** — keep as an optional architecture-guardrail module for larger TS repos, not a default suite step; keep prove-it-bites as a pattern other setup skills copy.

### tdd
The red → green reference: tests verify behaviour through public interfaces; test only at pre-agreed seams; anti-patterns (implementation-coupled, tautological, horizontal slicing); vertical tracer slices; refactoring is *not* part of the loop.
- Pros: The anti-pattern catalogue is the valuable part — "tautological" (assertion recomputes expected value the way the code does) names a failure most TDD guides never mention. Pre-agreed seams, confirmed with the user with a what-it-catches/what-it-misses note per seam, stops both under- and over-testing. Clean separation of concerns: design questions route to codebase-design, refactoring routes to review.
- Cons: Seam confirmation is a human checkpoint that can stall fully-AFK ticket work (implement-spec's implementers call tdd without a user present; the suite never resolves that tension). No reporting artifact — nothing records which seams were agreed, so review can't check them later unless the spec did (to-spec's seam sketch partially covers this).
- **Verdict: ADOPT**.

### teach
Stateful multi-session teaching workspace: `MISSION.md`, lessons as self-contained HTML files, learning records (ADR-analogues), reference docs, assets library; grounded in fluency-vs-storage-strength, retrieval practice, spacing, zone of proximal development.
- Pros: As pedagogy it is excellent, and its artifact discipline (mission, numbered learning records, reusable assets, compressed reference docs) is the same single-source pattern the engineering suite uses. "Never trust your parametric knowledge; populate RESOURCES.md first" is a good epistemic rule.
- Cons: It teaches *the user*, it does not build product — outside the developing/programming/design/product scope of the rnov24 suite. HTML lesson production is heavy machinery for a skill the suite would never invoke mid-flow.
- **Verdict: DROP** from this suite (keep in the personal library; it was never part of the engineering flow — ask-matt lists it as standalone).

### to-questionnaire *(mp copy wins; bodies identical)*
Turns a decision the user can't answer alone into a questionnaire for the person who holds the knowledge: grill the *send* (who, what we need back), never the subject; questions target the knowledge gap, ordered most-important-first, one idea each, with answer stubs and "why this matters" lines.
- Pros: "Grill the send, not the subject" is a genuinely clever inversion that keeps the interview within what the user can actually answer. The document template is complete (purpose, context, how-to-answer with effort/deadline, catch-all) and async-aware ("you may only get one pass"). Each step has an explicit done-when.
- Cons: Assumes a single recipient and a single round trip; no step for integrating the returned answers back into the spec/grilling. No guidance for sensitive topics where the questionnaire itself needs review before sending.
- **Verdict: ADOPT** — this is the suite's bridge to stakeholder knowledge and will matter even more in the rnov24 product phase (client/lecturer/user discovery).

### to-spec *(mp copy wins; bodies identical)*
Synthesis, not interview: turns the current conversation into a spec and publishes it to the tracker with `ready-for-agent`. Template: Problem Statement, Solution, User Stories (long numbered list), Implementation Decisions, Testing Decisions (with test seams sketched and user-checked *before* writing), Out of Scope, Further Notes. No file paths or code snippets, except prototype snippets that encode a decision.
- Pros: The no-interview rule keeps a clean division of labour with grilling (decisions happen there; this only writes them down). Sketching test seams *before* writing, preferring existing and highest seams, wires testability into the spec instead of bolting it on. The no-file-paths rule (they go stale) with the prototype-snippet exception shows real judgement about what a spec is for. User-perspective problem/solution sections keep it readable by non-implementers.
- Cons: For an artifact-based suite the template is thin in exactly the places the rnov24 suite cares about: user stories carry **no acceptance criteria** (those only appear later, per ticket), there are no personas, no non-functional requirements, no user-flow, and API contracts / schema changes are merely *listed as possible contents* of Implementation Decisions rather than being first-class sections (no ERD, no API documentation artifact). "Extremely extensive" user stories with no prioritisation (no must/should/could) invites bloated specs.
- **Verdict: ADOPT as the core spec skill, extended** — the rnov24 version keeps this template's spine and adds acceptance criteria per story, a persona reference, and dedicated data/API sections (see summary gaps).

### to-tickets *(mp copy marginally wins)*
Breaks a spec/plan/conversation into tracer-bullet vertical slices, each declaring its blocking edges; wide refactors are sequenced expand → migrate-in-batches → contract instead; the breakdown is quizzed with the user before publishing, one file per ticket locally (`.scratch/<feature>/issues/`) or native blocking links on a real tracker.
- Pros: The ticket template (what-to-build from the user's perspective, blocked-by, status, acceptance-criteria checkboxes) makes every ticket self-contained enough for a fresh context window — the property the whole orchestration model depends on. Blocking edges as first-class data (native where the tracker supports it) is what turns a list into a schedulable graph with a frontier. The wide-refactor exception is hard-won knowledge most slicing guides omit.
- Cons: Acceptance criteria are bare checkboxes — no Given/When/Then or source link back to the spec's user stories, so "done" can be gamed. No size/estimate or risk field. The quiz step is a full stop for user approval every time, which is right for planning but makes the skill unusable AFK.
- **Verdict: ADOPT** — adopt whole; the acceptance-criteria strengthening belongs to the rnov24 ticket template.

### triage
Moves incoming issues (and optionally external PRs — "a PR is an issue with attached code") through a state machine: two category roles × five state roles, with redundancy and prior-rejection checks, claim verification (reproduce the bug / run the PR's tests) *before* grilling, and outcomes that include a durable agent brief, an `.out-of-scope/` knowledge base entry, or templated needs-info notes.
- Pros: Verifying the claim before investing in grilling is excellent sequencing. The out-of-scope KB turns rejections into institutional memory instead of repeated arguments. Agent-brief as the `ready-for-agent` output makes triage produce exactly the artifact implement consumes. Resumability (read prior triage notes, don't re-ask) respects everyone's time.
- Cons: Heavy process for a solo developer whose "incoming issues" are mostly his own — the full state machine earns its keep on a multi-reporter project, not a one-person repo. Every posted comment must open with an AI-generated disclaimer, which is tracker noise. Strongly tracker-dependent; the local-markdown mode is the least developed path.
- **Verdict: ADAPT** — keep the state machine, verification step, agent brief, and out-of-scope KB; add a slim solo mode (fewer states, brief optional) for single-maintainer repos.

### wait-what
One-paragraph corrective: when a message didn't land, re-pitch it with context, in ASD-STE100 Simplified Technical English, using the glossary's ubiquitous language.
- Pros: Names a real, frequent failure (agent explains past the user) and gives it a one-word invocation. Tying the re-pitch to GLOSSARY.md vocabulary reinforces the shared-language investment. Nearly zero cost.
- Cons: One paragraph is a norm, not a workflow — there is nothing to execute. STE100 is an aerospace standard whose full rule set nobody will actually apply; "plain English" would do.
- **Verdict: ADAPT** — fold into the suite's communication/brief standard (alongside loop-me's *brief* idea) rather than shipping as a standalone skill.

### wayfinder
Plans an effort too big and foggy for one session as a shared map on the issue tracker: one map issue (destination, notes, decisions-so-far index, not-yet-specified fog, out of scope) plus child **decision tickets** typed research / prototype / grilling / task, HITL or AFK, claimed by assignment, resolved one per session, producing decisions — not deliverables — until the route is clear and it hands off to to-spec.
- Pros: The fog-of-war discipline is the best planning idea in the batch: ticket only what you can state precisely, park the dimmer stuff in Not-yet-specified, and let resolutions graduate fog into tickets — it refuses both under-planning and fake precision. Map-as-index-not-store (a decision lives in exactly one place, its ticket) is rigorous single-sourcing. Claim-by-assignment makes parallel sessions safe; refer-by-name keeps human-facing text readable; "plan, don't do" with a Notes override is a well-judged default. This is the only skill that handles genuinely multi-session, multi-agent *thinking* work.
- Cons: The most cognitively demanding flow in the suite (ask-matt says so itself) — heavy for anything that isn't truly huge. Depends on tracker features (child issues, native blocking, labels) and degrades on local markdown. Its ticket types have no design or product-discovery type beyond a generic prototype/grilling, and it hands off at to-spec, inheriting that template's gaps.
- **Verdict: ADOPT** — adopt as the suite's large-effort planning layer, above the main flow.

### wizard
Generates an interactive bash wizard (from a fixed, never-edited template library) that walks a human through steps only they can do — provisioning, credentials, dashboard clicks, migrations — opening URLs, capturing values with hidden entry for secrets, writing `.env` / GitHub secrets, confirming before irreversible actions.
- Pros: Correctly scoped by a negative rule: never invoke it for steps the agent can do itself. Scoping discipline is strong (read the repo's env/CI first, enumerate every captured value with source, destination, and secrecy before authoring). "Never invent steps that may not exist" for third-party UIs is the right honesty bar. Static verification (trace every value to its destination; match every `set_secret` name to a CI reference) instead of running it is the correct test strategy.
- Cons: The template is bash-specific and the wizards are ephemeral by default, so the knowledge can still walk away. Dashboard click-paths rot quickly. Value is real but occasional — this is an ops utility, not a flow step.
- **Verdict: ADAPT** — keep for infra/credential setup in the rnov24 suite, with the template vendored and a rule to commit wizards for repeatable setups.

### writing-beats
Article writing, exploit mode: assemble a fixed pile of raw material into a journey of beats, where every concept must be **grounded** (prerequisite or introduced by an earlier beat) before a later beat may lean on it; user picks each next beat from 2–3 candidates.
- Pros: The grounding model (requires/grounds per beat, reachability of candidates) is a dependency graph for prose — the same frontier thinking as to-tickets, applied to explanation. One beat at a time, re-read from disk, preserve user edits: good file discipline.
- Cons: It writes articles. It is not part of developing, programming, designing, or shipping product, and the suite already has documentation pressure from specs/ADRs/briefs without adding a literary workflow.
- **Verdict: DROP** from this suite — salvage the *grounding* idea for sequencing spec/design documents (don't let a doc lean on an undefined term) into writing-for-agents' rnov24 notes.

### writing-fragments
Article writing, explore mode: a grilling session that mines raw fragments (sharp sentences, vignettes, half-thoughts, a **leading word**) into one append-only Markdown file with no structure imposed.
- Pros: The leading-word concept (one coinage the whole piece hangs on) is valuable and already echoed in writing-for-agents. Append-silently, re-read-before-write file discipline is good.
- Cons: Pure explore with an explicit ban on structure — the opposite of what an artifact-based delivery suite needs mid-flow. Content-writing scope, not product scope.
- **Verdict: DROP** from this suite (the leading-word idea survives via writing-for-agents).

### writing-shape
Article writing, exploit mode variant: shape a raw pile into an article paragraph by paragraph, arguing form (prose vs list vs table vs callout) for each block, with the same grounding model as writing-beats.
- Pros: The format-argument table (when a table beats repeated prose, when a quote beats a paraphrase) is a usable checklist for technical documents too. Naming gaps in the pile explicitly ("we need an example and the pile doesn't have one") is honest drafting.
- Cons: Same scope problem as the other two writing skills, and it substantially overlaps writing-beats (two exploit-mode article assemblers is one too many even for a writing suite).
- **Verdict: DROP** from this suite; optionally keep the format-argument checklist as a reference inside the suite's docs-writing guidance.

### writing-for-agents *(mp copy wins; bodies identical)*
Reference for writing anything an agent consumes (skills, AGENTS.md, pointed-at docs): context pointers and their wording as the trigger mechanism; the two loads (context load, cognitive load); the information hierarchy and progressive disclosure; completion criteria (clarity + demand, premature completion); leading words; negation as a failure mode; pruning (single source of truth, environment-as-source, no-ops, sediment).
- Pros: This is the batch's meta-skill — the rnov24 suite's own skills should be written to it. Completion-criteria theory (sharpen the bound first; hiding post-completion steps only works across a real context boundary) directly explains why implement-spec's subagent structure works. The no-op test ("does this sentence change behaviour versus the default?") and cache test ("could the agent just look this up?") are immediately applicable editing tools.
- Cons: Dense and abstract — all reference, no steps, no checklist or worked example, so applying it requires already understanding it. Its companion SKILL-MECHANICS.md carries the skill-specific half, so the file alone is incomplete.
- **Verdict: ADOPT** — adopt as the authoring standard for the rnov24 suite itself; consider adding a one-page checklist distillation when the suite is written.

### local_engineering_workflow *(local-only composite)*
A single Muse-native file that compresses setup-matt-pocock-skills + to-spec + to-tickets + implement-spec into one workflow: configure the repo once, synthesise a spec from the conversation, break it into tracer-bullet tickets with blocking edges, then implement the frontier with background workers on an integration branch — delegating implementation through the local agy-delegation skill with bounded packets — and closes with alternatives pointers (local-grilling when the plan is uncertain, local-prototype for an open question, local-prd for a formal product document).
- Pros: It is the only artifact in the batch already adapted to this user's real stack: harness-neutral wording, `muse.skill_search` instead of a Skill tool, and implementation delegated to agy on a separate quota — which is precisely the orchestration model the rnov24 suite wants. Having setup + spec + tickets + implement in one entry point proves the flow composes. The alternatives footer is good router behaviour in miniature.
- Cons: Compression cost real detail: its review step is one generic sentence ("review the integration branch") where the mp originals specify the two-axis review; TDD is reduced to "builds the ticket with tests" with no seams or anti-patterns; there is no retro, no handoff, no per-ticket acceptance check, and no worker report format. As a monolith it can't be invoked in pieces (no standalone spec or tickets step). No frontmatter, so invocation relies on its sidecar metadata.
- **Verdict: ADAPT** — use it as the *skeleton/blueprint* for the rnov24 orchestrator skill, but rebuild it by composing the fuller adopted primitives (two-axis code-review, tdd, implement-spec's graph mechanics) rather than inheriting its compressions.

---

## Batch summary

### How Matt's flow works as a system

The suite is a pipeline with one precondition and a closing loop:

**setup → grill → (prototype detour) → spec → tickets → implement → review → retro**, with two on-ramps (triage for incoming work, diagnosing-bugs for broken work) and one escape hatch for oversized efforts (wayfinder, which produces decisions and hands off at to-spec).

- **Setup** (`setup-matt-pocock-skills`) runs once per repo and writes the configuration every other skill reads: tracker choice, the five triage labels, domain-doc layout, all recorded in `docs/agents/*.md` and pointed at from CLAUDE.md/AGENTS.md. Skills never hard-code where issues live.
- **Grill** (`grill-with-docs` = `grilling` + `domain-modeling`) settles decisions before anything is written down as a plan. The decision-tree frontier guarantees questions are only asked when their prerequisites are settled; facts are delegated to subagents, decisions stay with the user.
- **Spec** (`to-spec`) is pure synthesis of the grilled conversation — deliberately no interview — and sketches test seams before writing.
- **Tickets** (`to-tickets`) convert the spec into a task graph of tracer-bullet vertical slices with explicit blocking edges; the user approves granularity and edges before anything is published.
- **Implement** runs two ways: `implement` per ticket in a fresh context, or `implement-spec` orchestrating implementer subagents across the graph's frontier onto one integration branch. Both drive `tdd` and close with `code-review`.
- **Review** (`code-review`) is two-axis (Standards / Spec) and deliberately never collapses the axes. `pr` then packages the result with evidence and a reversibility judgement.
- **Retro** feeds the loop: the session's mistakes are converted into environment improvements (deterministic checks for mechanical errors, standards for judgement calls), so the next run starts from a better setup.

Context management is treated as a first-class design constraint throughout: steps 1–3 stay in one unbroken window, each implementation starts fresh from its ticket, and phase boundaries have an explicit decision procedure (ask-matt / PHASE-BOUNDARIES.md).

### Artifact discipline

The system's real strength is that every phase emits a durable, single-sourced artifact and consumes pointers to the previous ones:

- **`GLOSSARY.md` + ADRs** — written *inline during grilling*, gated by the three-part ADR test, lazily created, implementation-free. ADRs are treated as settled law by diagnosing-bugs, tdd, improve-codebase-architecture, and to-spec.
- **The spec** — a fixed template published to the tracker with a `ready-for-agent` label; user-perspective problem/solution, an extensive user-story list, implementation and testing decisions, explicit out-of-scope. It is the contract the Spec axis of code-review later checks against.
- **Tickets with blocking edges** — one file per ticket (`.scratch/<feature>/issues/NN-slug.md`) or native tracker issues with native blocking links; each carries what-to-build, blocked-by, status, and acceptance criteria. The edges are data, not prose, which is what makes the frontier computable and parallel implementation safe.
- **Supporting artifacts** — agent briefs from triage, the `.out-of-scope/` rejection KB, research notes as cited Markdown, prototypes preserved on throwaway branches with context pointers from issues, handoff documents that reference rather than duplicate, and the wayfinder map as an index that never restates its tickets.

The recurring mechanisms: communicate by **context pointer**, never by copying content; keep each meaning in **one place**; label work with a small state vocabulary (`ready-for-agent` etc.) so any agent can pick it up cold.

### Gaps for product and design phases

Matt's flow starts at "you have an idea." Everything upstream of the idea — and everything about the humans the software is for — is missing or thin:

- **No product discovery.** No PRD skill, no problem validation, no market/user research synthesis (research exists but is framed as technical reading), no prioritisation. `to-questionnaire` is the only stakeholder-knowledge tool, and it's generic.
- **No personas or user stories with teeth.** The spec template asks for user stories but provides no persona artifact for the `<actor>` to refer to, and — critically — **no acceptance criteria at story level**; acceptance only appears later as bare checkboxes on tickets, disconnected from the stories they verify.
- **No design phase or design artifacts.** There is no DESIGN artifact, no userflow/journey artifact, no wireframe-to-spec path. `prototype`'s UI branch generates variations but produces no design rationale, no decision record, and no reviewable design output; there is no design equivalent of the Standards axis in code-review.
- **Data and API modelling are second-class.** Schema changes and API contracts are named as *possible contents* of the spec's Implementation Decisions list — there is no ERD/data-model artifact, no API documentation artifact, and domain-modeling sharpens vocabulary without ever modelling entities or relationships.
- **No non-functional requirements** anywhere in the spec template (performance, security, accessibility, i18n), and no brief artifact formalising goals/constraints before grilling starts.

### Gaps for orchestrator-style delegation

`implement-spec` + `chief-of-staff` gesture at orchestration but leave the contract layer unspecified:

- **No worker packet or report schema.** Nothing defines what an implementer subagent receives beyond pointers, nor what it must return (files changed, tests run, acceptance evidence, blockers). "Done" is self-reported and never independently verified except by the single end-of-run review.
- **No per-ticket quality gate.** Review happens once, over the whole integration branch, after all merges — contamination is discovered at the most expensive moment, and fixes are funnelled through one implementer.
- **No failure semantics.** No retry, escalation, stuck-agent, or merge-conflict protocol; no rule for a ticket that turns out to be mis-specified mid-flight (route back to grilling? to triage?).
- **No resource awareness.** Nothing tracks cost/quota per worker or bounds parallelism by anything except the frontier — on this user's stack, where implementation runs on a separate metered engine (agy), the packet discipline in `local_engineering_workflow` (bounded packets via agy-delegation) is an addition Matt's suite doesn't have.
- **chief-of-staff is a posture without mechanics** — it mandates subagents and pointers but defines no artifacts, criteria, or review, so two runs of it would orchestrate completely differently.

These gaps are the rnov24 suite's design space: keep Matt's spine (setup → grill → spec → tickets → frontier implementation → two-axis review → retro) and its artifact discipline, and add (1) a product front-end (brief, PRD, personas, user stories with acceptance criteria), (2) a design phase with its own artifacts (DESIGN, userflow) and review axis, (3) first-class data/API artifacts (ERD, API docs), and (4) a real delegation contract (packet schema, structured worker report, per-ticket acceptance + review gates, escalation path).

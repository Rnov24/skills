# Audit Batch E — Product, Content, and Everything Else

Scope: the skills in `~/workspace/custom-skills/` not covered by the development, design,
research, and orchestration batches — `local-prd`, `local-brag`, `local-brag-slim`,
`local-live-carousel`, `local-kaggi`, `local-humanizer`, `local-slopmonster`,
`local-skill-creator`, `local-full-output-enforcement`, and `recovered-skill-notes` —
plus a sweep verdict on the `papercut-*` family in `~/workspace/skills/`.

Verdicts are given against one target: a unified rnov24 suite for development + design +
product, in the style of addyosmani/agent-skills and mattpocock/skills, with an
artifact-based workflow (PRD, DESIGN, brief, personas, user stories with acceptance
criteria, ERD, userflow, API documentation) and a main agent that orchestrates
subagents, delegates clearly, and reviews results.

- **ADOPT** — take into the suite substantially as-is.
- **ADAPT** — take the mechanism or a reworked subset; do not take it whole.
- **DROP** — do not take it; salvage at most a named idea.
- **OUT-OF-SCOPE** — legitimate skill, wrong suite; it belongs to a different product
  surface (marketing content, competitions) and should stay a separate install.

---

## 1. local-prd — the only real product skill, and only half of one

**Purpose.** Generate a PRD for a software system or AI feature through a three-phase
flow: discovery interview, analysis/scoping, then drafting against a fixed
five-section schema.

**Pros**

- **A real discovery gate.** Phase 1 forbids drafting before interrogating the user on
  the core problem, success metrics, and constraints, and the DON'T list hardens it:
  never write without at least two clarifying questions, never hallucinate constraints —
  label them `TBD`. This is the correct posture for a product phase's entry gate.
- **A measurable-criteria standard with a worked contrast.** The vague-vs-concrete
  diff ("search should be fast" → "results within 200 ms for a 10k-record dataset,
  ≥85% Precision@10, 100% Lighthouse Accessibility") is a reusable quality rule for
  every artifact in a suite, not just PRDs.
- **The schema names the right headline artifacts.** Executive summary with 3–5
  measurable success criteria, personas, user stories in
  `As a [user], I want to [action] so that [benefit]` form, acceptance criteria as a
  "Done" definition per story, and explicit non-goals to protect the timeline.
- **AI-feature awareness.** A dedicated section for tool/API requirements and an
  evaluation strategy (benchmark set, pass rate, citation accuracy in the worked
  example) — most generic PRD templates have nothing like this, and it fits this
  user's actual projects.

**Cons**

- **It produces one monolithic document, not an artifact set.** Brief, personas,
  stories, and technical specification are all sections of a single file. There is no
  file layout, no per-artifact status, no owner, no links between artifacts, and no
  handoff contract to a design or engineering phase. This is the exact opposite of the
  artifact-based workflow the suite is supposed to run.
- **No YAML frontmatter and no trigger description in the SKILL.md itself** (it opens
  with a bare title; triggering metadata lives in a separate `skill.yaml`). In a
  standard skills layout this skill under-triggers or fails to load — compare
  `local-brag` and `local-skill-creator`, which carry proper `name`/`description`
  frontmatter.
- **Single-pass, gate-free process.** Discovery → analysis → draft is linear. There is
  no approval gate between the draft and downstream work, no review checklist against
  the schema, no iteration loop beyond "present a draft and ask for feedback," and no
  verification step that the finished PRD actually contains every schema section.
- **143 lines with no bundled templates, references, or examples directory.** The one
  worked example (intelligent search) is truncated and mixes schema levels — its
  sections 3 and 4 do not match the Strict PRD Schema's sections 3 and 4 — so a model
  following the example and a model following the schema produce different documents.

**PRD structure audit — what a real product phase needs vs. what the schema has**

Present and adequate: problem statement, proposed solution, headline success criteria,
non-goals, a phased rollout sketch (MVP → v1.1 → v2.0), technical risks, and a security
& privacy line.

Missing, exactly:

1. **Brief as its own artifact.** No one-page brief distinct from the PRD: no context
   or background, no target segment, no "why now," no decision the brief is asking
   for. Discovery asks "why are we building this now?" and then gives the answer
   nowhere to live.
2. **Persona depth.** "User Personas: Who is this for?" is the entire specification.
   No persona template (goals, pain points, current workaround, behaviour, technical
   context), no primary/secondary distinction, no anti-persona, and no traceability
   from a persona to the stories written for it.
3. **Story quality machinery.** No prioritisation (MoSCoW, RICE, or even must/should),
   no epic grouping, no sizing, no negative/edge-case stories, and acceptance criteria
   are free-form bullets rather than a checkable format (Given/When/Then or an
   equivalent). The worked example's AC ("supports multi-turn clarification") would
   fail the skill's own measurable-criteria standard.
4. **Measurable success, operationalised.** KPIs are requested as a list, with no
   baseline, no target value per metric, no measurement method, no time window, no
   North Star vs. input vs. guardrail distinction, and no instrumentation or event
   tracking specification — so the metrics can never be checked after launch.
5. **Scope as a positive statement.** Non-goals exist; an explicit in-scope list,
   MVP entry/exit criteria, an assumptions log, an open-questions log, and a
   dependencies list do not. (Phase 2 prose mentions identifying dependencies; the
   schema then drops them.)
6. **Stakeholders and decision rights.** No owner, no approvers, no RACI, no sign-off
   step, no document status or version history. A PRD nobody has approved is a draft
   forever.
7. **The design artifacts.** Phase 2 says "map out the user flow," but the schema has
   no userflow artifact, no reference to a DESIGN document, and nothing on states a
   design phase needs — empty, error, loading, permission-denied. The flow is
   mentioned and then lost.
8. **The data and API artifacts.** Technical specifications stop at "architecture
   overview" prose plus "APIs, DBs, and Auth" as integration points. There is no ERD
   or data model, no data dictionary, no API documentation or contract section — two
   of the artifact types the unified suite is explicitly built around have no home
   in its only product skill.
9. **Non-functional requirements.** Performance appears only inside the example.
   Reliability, scalability, accessibility (beyond the example), localisation, and
   compliance have no schema slots.
10. **Release mechanics.** Rollout is three version labels. No milestones with owners
    or dates, no migration plan, no feature-flag or rollback plan.
11. **Risk beyond the technical.** Only latency/cost/dependency risks; no product,
    market, or adoption risks, and no mitigation or owner per risk.

**Verdict: ADAPT.** This is the seed of the suite's product phase — the discovery gate,
the measurability standard, and the TBD-honesty rule should be adopted verbatim — but
the output must be rebuilt from a single document into the artifact chain (brief →
personas → stories + acceptance criteria → metrics plan → scope/non-goals) with the
eleven gaps above closed and explicit handoffs to the userflow/DESIGN, ERD, and API
artifacts owned by later phases.

---

## 2. local-brag

**Purpose.** Turn the current project into a 15–25 s launch video with Hyperframes,
through inspect → plan/storyboard → compose → validate/render/deliver steps.

**Pros**

- **A genuinely gated artifact pipeline.** Each step ends in a checkable gate:
  a 9-question planning rubric before planning, `brag-plan.md` existing with scene
  durations summing to 15–25 s before composing, `npx hyperframes check` passing with
  zero errors before rendering, and the mp4 + chosen poster + share copy existing
  before delivery. Gates are file- and command-based, not vibes.
- **Clear ownership split at the handoff.** "/brag owns the product angle, source
  material, storyboard, tone, format, audio selection; Hyperframes owns composition
  structure, timing, mechanics, render" — a clean delegation contract between an
  orchestrating skill and an executing tool, written down in one paragraph.
- **Anti-fabrication laws with teeth.** "Show the thing" (at least one scene of real
  UI/copy), generic SaaS language banned by name, and claims must come from the
  project's own copy. Share copy is a named deliverable, not an afterthought.
- **Run hygiene.** Timestamped output directories so runs never overwrite each other,
  and a model-check dispatch at the top that routes to brag-slim under a stated
  condition instead of silently doing the wrong workflow.

**Cons**

- **It is a marketing deliverable, not a development, design, or product artifact.**
  Nothing it produces feeds a build: the plan, storyboard, and video are terminal
  launch assets.
- **Heavy, brittle coupling.** It depends on five external Hyperframes domain skills
  plus bundled music/SFX assets (~17 MB in this folder alone); the dispatch rule is
  pinned to one model name ("Claude Opus 5.5") and will age badly.
- **Duplicate implementation.** This skill and `local-brag-slim` trigger on nearly the
  same phrases and implement the same job two ways; keeping both in one suite invites
  routing errors.
- **Creative laws are over-fit to one format.** The hook→reveal→highlights→punchline
  pattern, seven tone presets, and second-level readability timings are video craft;
  none of it transfers to product or engineering artifacts.

**Verdict: OUT-OF-SCOPE.** Keep it installed as a standalone launch tool. Do not fold
it into the suite — but steal its gate discipline (rubric gate → plan-file gate →
machine-check gate → deliverable gate) and its one-paragraph ownership split as
patterns for the suite's own phases.

---

## 3. local-brag-slim

**Purpose.** The same launch-video job as brag, in one self-contained file with no
bundled assets: inspect a project or a live website, plan, build, check stills, render,
deliver poster and share copy.

**Pros**

- **Best source-handling rules in the batch.** For projects it reads the real
  components, styles, fonts, and images instead of rebuilding them; for websites it
  anticipates the empty-JS-shell failure and prescribes headless rendering, overlay
  dismissal, and section-by-section scrolling.
- **An explicit do-not-read list** — build output, lock files, `.env`, keys,
  credentials, anything `.gitignore` excludes — and a matching rule that no secrets,
  internal hostnames, real user names, or personal data may reach the plan, the video,
  or the share copy, with fictional stand-ins substituted and disclosed. This is a
  reusable safety pattern for any skill that inspects a repo.
- **A visual QA step that actually looks.** Inspect stills from every scene *and*
  mid-transition before the full render; named failure modes (overflow, collisions,
  low contrast, muddy crossfades) with named fixes.
- **Poster-frame correctness.** Replace frame 0 with the strongest settled frame
  rather than adding a frame, so duration and audio sync survive — a small, precise,
  verifiable delivery rule.

**Cons**

- **Same scope problem as brag, plus redundancy.** It exists only because the full
  brag routes to it on one model; as suite content it is a second implementation of
  an out-of-scope job.
- **"Build it with whatever works on this machine"** is the opposite of a workflow:
  no pinned tool, no check command, no reproducible render path.
- **No gates.** Unlike full brag there are no rubric questions, no plan-file
  requirement with a duration sum, and no machine check — quality rests entirely on
  the model remembering the creative laws.

**Verdict: OUT-OF-SCOPE.** If one brag survives anywhere, this is the better one to
keep (self-contained, safer source handling). For the suite, only its do-not-read
list and its stills-before-render QA habit are worth extracting.

---

## 4. local-live-carousel

**Purpose.** Turn a topic, product, or story into an animated social carousel — one
8-second looping mp4 per slide plus full-deck videos, a cover image, and a swipeable
PDF — from a declarative `deck.json` rendered by a bundled Python/FFmpeg engine.

**Pros**

- **A clean artifact contract.** The agent writes only `deck.json` against a written
  spec (`references/deck-spec.md`); the engine does all drawing, timing, animation,
  and music. "You never write drawing code" is exactly the separation a suite wants
  between an authoring artifact and a deterministic renderer.
- **Tooling that verifies before it renders.** `doctor` checks the environment,
  `check` splits findings into errors (must fix) and warnings (should fix), and
  `preview` renders a contact sheet the agent must actually inspect and iterate on
  before the expensive render. Incremental re-render via a cache makes the loop cheap.
- **A bounded interview with defaults.** One short message, seven questions, each
  with a sensible default, and an explicit escape hatch ("just make it" → pick
  defaults, state them in one line, continue). A good model for intake UX in the
  suite's own phases.
- **Hard honesty rules.** Real facts only — never invent statistics, prices, reviews,
  testimonials, or star ratings; if a number is missing, ask or choose a graphic that
  needs none. Example decks are labelled placeholders whose facts must all be
  replaced.

**Cons**

- **Pure content production.** Instagram/TikTok/LinkedIn carousels are distribution
  assets; no output informs a product, design, or engineering decision.
- **Domain-locked vocabulary.** 14 graphic types, two house looks, hook/CTA slide
  grammar — none of it generalises beyond this one format.
- **Platform and toolchain assumptions baked in** (Pillow/numpy/imageio-ffmpeg,
  per-platform posting instructions) that a development suite should not carry.

**Verdict: OUT-OF-SCOPE.** Keep as a standalone content tool. Its transferable assets
are the spec'd-artifact-plus-deterministic-engine split and the
doctor → check → preview → render verification ladder, both of which the suite's
artifact pipeline should imitate.

---

## 5. local-kaggi

**Purpose.** A mascot sidekick for data-science competitions: intake brief, phased
battle plan, experiment loop with a journal, pre-submit checklist, and post-mortem,
across learn / normal / brutal autonomy modes.

**Pros**

- **The best gate design in the batch.** Five phases, each ending in a user-owned
  decision gate, with an explicit anti-skip rule: if the user says "just submit it,"
  Kaggi runs the check first, briefly, then proceeds. Autonomy is a mode the user
  selects, not a default the agent drifts into.
- **Delegation of irreversible actions is explicit and bounded.** In brutal mode the
  agent may submit only under a one-time grant that names the allowance ("up to 2
  times per day for this competition"); without it, the agent prepares everything
  and the human presses the button. Every grant-driven action is logged. This is
  precisely the rule a suite orchestrator needs for deploys, merges, and publishes.
- **A real working artifact: the experiment journal.** Fixed entry format (date,
  hypothesis, change, CV score with the validation scheme named, public score,
  verdict keep/drop/investigate), read before every turn, and numbers are mandatory —
  "it felt better" is not a result. The journal, README brief, SUBMISSIONS.md log,
  and lessons.md are scaffolded by a script into a fixed workspace layout.
- **Evidence discipline stated as operating rules.** Observed vs. inferred labelled
  every time; never report a metric that wasn't produced or read from a real source;
  actively try to break your own validation. Plus a trap catalog that names a
  failure, explains its mechanism in one or two sentences, and states the alternative.

**Cons**

- **The domain content is unusable for the suite.** Metric-invariance analysis,
  modality routing for tabular/vision/NLP/recommender, the leakage trap catalog, and
  the Kaggle MCP/API setup are competition-specific; roughly two-thirds of the file
  would be dead weight.
- **Persona overhead.** The mascot voice, mode-switching banter, and per-phase
  Socratic question banks cost tokens on every load and fight the tone a professional
  dev/design/product suite needs.
- **Token handling is described in the skill text itself** (bearer token location,
  config file path and format), normalising the idea that a skill should document
  where a live credential sits — a habit the suite should not import.

**Verdict: ADAPT.** Strip the competition domain and the mascot; adopt the skeleton —
phased flow with user-owned gates, a scaffolded workspace of named artifacts, a
mandatory structured journal the orchestrator reads before acting, a pre-submit
checklist, and the explicit one-time grant rule for irreversible actions. Those five
mechanisms are the strongest orchestration material in this batch.

---

## 6. local-humanizer

**Purpose.** Rewrite AI-sounding text so it reads like its author, using a catalog of
26 patterns (staging, rhythm-by-rule, inflation, formatting-by-rule, chat leftovers,
wrong-reader) ordered by strength, without changing what the text says.

**Pros**

- **A principled, ranked catalog instead of a word blacklist.** Patterns are ordered
  strongest first, graded ("act on one sighting" vs. "*weak alone*, needs company"),
  each with a mechanism, before/after pairs, and a "when not to act" section covering
  quotations, deliberate style, and pre-2022 text. That calibration is rare and keeps
  the edit from becoming vandalism.
- **Fact-preservation as a checkable step.** Step 3 of its process audits the rewrite
  for added or dropped facts, names, numbers, dates, quotes, and claims — and names
  which pattern edits (§6, §9, §19) most often cause losses. An unsupported addition
  and a lost claim are both defined as errors.
- **Voice matching with an override rule.** A user sample overrides the pattern rules
  (including the dash ban); without one, voice is inferred from text type, and
  reference/technical text stays neutral. File mode protects code blocks, commands,
  paths, YAML, and link targets from prose edits.
- **Package discipline around it.** Its `AGENTS.md` holds the skill to a word cap
  (every word is read on each use), requires SKILL.md/README sync, and names validator
  commands — good hygiene for a suite that will ship many skills.

**Cons**

- **391 lines / ~5,200 words loaded on every invocation.** For a prose-polish utility
  that is an enormous context tax; most invocations need three or four patterns, not
  twenty-six.
- **English-centric and prose-only.** It polishes how artifacts read; it says nothing
  about whether a PRD, spec, or README is complete, correct, or structured — and this
  user's working language is mixed Indonesian/English, which the catalog only touches
  via the not-X-but-Y construction.
- **Hard rules that can misfire in technical writing.** The total em-dash ban and
  triad suspicion will fight legitimate technical prose (three-item architectures,
  conventional dash use) unless the sample-override is exercised every time.

**Verdict: ADAPT.** Include a trimmed version as the suite's final prose pass over
user-facing artifacts (PRD, README, API docs, release notes): keep the ranked
top patterns, the fact-preservation audit, and the sample-override rule; cut the rest
to a reference file loaded on demand.

---

## 7. local-slopmonster

**Purpose.** Edit a draft (README, landing page, email, script) for its audience:
run a deterministic pattern checker, rewrite in a fixed order, get a second pass from
a different model family, diff against the source, and re-check.

**Pros**

- **A deterministic checker with honest limits.** `deslop.py` scores five categories
  and the skill states plainly that 5/5 means "no scored patterns matched," not that
  the copy is clear or true — and that the final editorial review is required even at
  5/5. Tools that confess their limits get used correctly.
- **Cross-model second pass, with failure modes documented.** The rival-CLI pass
  specifies exit-code semantics (124 timeout, 127 missing CLI whose stdout is *not* an
  edited draft), a notes separator to watch for, and an instruction to report when the
  pass could not be completed instead of pretending it happened. That is a review
  protocol, not a hope.
- **Diff-before-done.** Step 4 compares the edit against the source for changed facts
  and commands, surviving links and placeholders, and deletions that removed necessary
  information — then re-runs the checker.
- **Anti-fabrication rule for copy.** Never invent customer counts, testimonials, or
  results; mark gaps `[needs number]`; `--allow-proof` may be used only after the
  evidence has actually been checked.

**Cons**

- **Functionally redundant with local-humanizer.** Same job (de-slop prose), weaker
  pattern theory, heavier machinery. A suite carrying both will route inconsistently;
  one must win.
- **External-CLI fragility.** The second pass depends on a rival CLI being installed
  and authenticated; in many environments it degrades to "use the other model's chat,"
  which is unauditable.
- **English-only rules that do not detect input language**, stated in the skill itself —
  a poor fit for this user's bilingual documents.

**Verdict: DROP** as a standalone skill in the suite. Salvage two mechanisms into the
adapted humanizer pass: the deterministic pre-checker with confessed limits, and the
cross-model-family second review with explicit failure reporting. Humanizer's catalog
and fact-preservation audit are the stronger base.

---

## 8. local-skill-creator

**Purpose.** Create new skills and iteratively improve them: capture intent, draft,
run test prompts with and without the skill in parallel subagents, grade against
assertions, show results in a review viewer, revise, and optimise the trigger
description against should/should-not-trigger eval queries.

**Pros**

- **A real eval loop, not "try it and see."** Every test case runs twice in the same
  turn — with-skill and baseline (no skill, or a snapshot of the old version) — so the
  skill's value is measured against a control. Assertions are drafted while runs are
  in flight, grading uses fixed field names the viewer depends on, timing/token data
  is captured from completion notifications because that is the only chance to get it,
  and an analyst pass hunts for non-discriminating assertions and flaky evals.
- **Trigger engineering treated as a first-class problem.** Twenty realistic eval
  queries with near-miss negatives, a user review step before running, a train/test
  split with the winner selected on held-out score, and a plain explanation of why
  trivial queries never trigger skills regardless of description quality.
- **Sound authoring doctrine.** Progressive disclosure (metadata → SKILL.md body →
  bundled resources), keep SKILL.md under ~500 lines, explain the *why* instead of
  stacking MUSTs, generalise from feedback instead of overfitting to the test cases,
  and bundle a script when every test run independently reinvented the same helper.
- **It is the meta-tool the suite itself needs.** A unified suite of a dozen-plus
  skills cannot be validated by hand; this loop is how each rnov24 skill gets tested
  before it ships and regression-tested after edits.

**Cons**

- **Long and environment-specific.** 486 lines covering Claude.ai, Cowork, and
  headless variants inline; the viewer, packaging, and description-optimisation steps
  assume specific CLIs and a browser/display that this VM does not reliably have, and
  the skill itself has to keep carving out exceptions for that.
- **Heavyweight for small skills.** Spawning paired subagents, grading, and a viewer
  round-trip is proportionate for a flagship skill and absurd for a 40-line utility;
  the skill offers a "just vibe with me" escape but no lightweight middle tier.
- **Human-in-the-loop bottleneck.** The loop's centre is the user reviewing outputs
  in a viewer and returning feedback.json; unattended or overnight suite-building
  runs stall at exactly that step.

**Verdict: ADOPT.** Take it as the suite's own development and QA infrastructure —
the thing that builds and grades the other skills — with two local amendments: a
defined lightweight tier (draft + 2 prompts + inline review) for small skills, and
static-file review output as the default instead of a served viewer.

---

## 9. local-full-output-enforcement

**Purpose.** Override default truncation behaviour: ban placeholder patterns
(`// rest of code`, "for brevity," skeleton-instead-of-implementation), lock the
deliverable count up front, and pause/resume cleanly at token limits.

**Pros**

- **The scope-lock is a genuinely good mechanism.** Step 1 counts the distinct
  deliverables the request implies and locks the number; step 3 re-reads the original
  request and compares the output count against it before responding. That is an
  artifact-completeness check in miniature.
- **The banned-pattern list is concrete and greppable.** Named code and prose
  patterns, plus structural shortcuts (first-and-last-section-only, one example
  standing in for repeated logic) — a reviewer, human or agent, can actually check
  for these.
- **A clean breakpoint protocol.** Stop at a section boundary, emit a
  `[PAUSED — X of Y complete…]` marker naming the resume point, and continue without
  recap or repetition. Multi-part artifact generation needs exactly this contract.

**Cons**

- **It is a behaviour patch, not a workflow.** 49 lines of insistence with no
  artifacts, no gates, no domain content — there is nothing to adopt as a suite
  *skill*; its value is three rules.
- **Its absolutism fights other suite values.** "Do not optimise for brevity —
  optimise for completeness" and "no exceptions" collide with progressive disclosure,
  with concise user-facing summaries, and with any cost/latency judgement; applied
  globally it inflates every output.
- **Self-check only.** The cross-check is the same model re-reading its own work in
  the same response; there is no external verification (file exists, sections present,
  tests pass) of the kind brag's and skill-creator's gates provide.

**Verdict: ADAPT.** Dissolve it into the suite's artifact standard: the scope-lock
count becomes the artifact manifest check (every artifact the phase promises exists
and is complete), the banned-pattern list becomes review-checklist items, and the
pause marker becomes the long-generation protocol. Do not ship it as a standalone
skill and do not adopt its global anti-brevity stance.

---

## 10. recovered-skill-notes

**Purpose.** A placeholder note explaining that the folder preserves earlier local
learning, that some of it may be unverified or out of date, and that useful methods
should be moved into real skills.

**Pros**

- **Honest provenance labelling.** It warns, in its own text, that the contents are
  unverified and may be stale, and prescribes comparing them against current skills
  before use — the right default suspicion for recovered material.
- **It states a retirement rule:** once useful content is incorporated into a real
  skill, retire the recovery entry, and keep corrections to system skills as separate
  amendments tied to a reviewed revision.

**Cons**

- **There is no skill here.** The SKILL.md is eight lines of meta-guidance; it teaches
  no task, has no workflow, no triggers, and no checks. Anything of value lives in its
  `references/` folder, unaudited and unindexed.
- **As an installed "skill" it is pure routing noise** — a description-less entry that
  can only confuse triggering and suite inventories.

**Verdict: DROP.** Not suite material in any form. Mine the `references/` folder once,
by hand, during suite construction; promote anything real into a named skill and
delete the recovery shell from the suite's inventory.

---

## Sweep verdict: the papercut-* family as a worked example of artifact-based workflow

The nine papercut skills (`papercut-explainer` as orchestrator; `-strategy`, `-hook`,
`-script`, `-storyboard`, `-setup`, `-voice`, `-build`, `-qa`) are the most complete
artifact-based pipeline in either skills directory, and the decomposition gets the
fundamental thing right: **the pipeline lives in files, not in chat.** Each stage has a
declared reads/writes contract (strategy writes the BRIEF block into
`research/facts.md`; hook writes the HOOK block into `STORYBOARD.md`; script writes
`narration/script.json` plus a staging table; storyboard adds the Camera/Cut table and
frame-level scene blocks; voice produces per-line WAVs and word timings that become
`src/plan.json`; build turns all of it into `episode.json`, scenes, and the mp4; QA
checks rendered stills against the storyboard and the style DNA), every stage ends in
a checkbox gate, every stage names its successor and can be entered directly ("fix or
rebuild one scene" routes to build then QA), and a fresh session can resume from any
stage because the state is on disk — with two further refinements a dev suite should
copy: a persistent series-level context file (`SERIES.md`: audience, voice, palette,
keyword log, what has worked) that every stage reads first, which is exactly a
project-level PRODUCT/context artifact; and a post-delivery autopsy stage that feeds
measured results back into that context file, closing a loop most workflows leave
open. Where it does badly is equally instructive. The contracts are enforced by prose
and checklists alone — nothing validates that `script.json` matches the staging table
or that `episode.json` matches the storyboard, so drift between artifacts is caught,
if at all, by a human reading stills. The phase count is bought with duplication:
preflight, library-path resolution, and install-mode probing are restated in nearly
every skill, so a fix must be made in five places; shared rules live in cross-referenced
reference files (`../papercut-explainer/references/…`) whose relative paths break if
skills are installed separately, as this very install shows — the family sits in
`~/workspace/skills/` while its library, config, and scene-agent infrastructure live
elsewhere, and several stages degrade to "hand over to papercut-setup" when the
environment doesn't match. The gates are also asymmetric: creative stages get scored
rubrics (the six-question hook check, five scored variants, drop any variant failing
the truth question) while build and QA gates are judgement calls ("looks like paper")
with a two-fix-round cap and no escalation path. Net lesson for the rnov24 suite:
copy the shape — orchestrator, stage skills, named artifacts with reads/writes
contracts, per-stage gates, a persistent project context file, and a feedback stage —
but generate the shared preflight/rules from one source instead of restating them,
and add machine validation between artifacts (schema checks on the JSON, cross-checks
that downstream files match upstream ones) where papercut relies on eyes.

---

## Batch summary — what the product phase still needs

None of these ten skills, alone or combined, provides a complete product phase.
`local-prd` is the only one even attempting it, and the gaps below survive adopting
everything in this batch:

1. **An artifact chain with traceability.** Separate, named artifacts — brief,
   personas, user stories with acceptance criteria, metrics plan, scope/non-goals —
   each with an owner, a status, and links forward and back (story → persona,
   criterion → metric, story → userflow frame → API endpoint), so a change in one
   place shows what it invalidates in the others. PRD gives one document; kaggi and
   papercut show the file-based shape but for other domains.
2. **Prioritisation and sequencing as artifacts.** A stated method (MoSCoW or RICE),
   a ranked backlog, and a roadmap with milestones, owners, and dates. PRD's rollout
   is three version labels; nothing in the batch ranks anything.
3. **A research input stage.** Interview or survey synthesis, support/feedback mining,
   and competitive analysis written into the brief as evidence. Kaggi's intake brief
   and papercut-strategy's competitor study prove the pattern, but both are welded to
   their domains; the product phase needs its own version whose output is the brief.
4. **Approval and decision records.** A sign-off gate on the brief and on the PRD
   (who approved, when, what changed since), plus a lightweight decision log for
   product choices — the product analogue of an ADR. Kaggi's gates are the model;
   no product skill here has them.
5. **Handoff contracts to the neighbouring phases.** The product phase must emit what
   design and engineering consume: userflow requirements and state inventories for
   the DESIGN artifact, and entity/operation inventories that become the ERD and the
   API documentation. PRD mentions a user flow and "APIs, DBs" and hands over
   neither.
6. **A metrics plan that can be checked after launch.** Baselines, targets,
   instrumentation events, and a scheduled post-launch review that compares results
   against the PRD's success criteria and writes back what was learned — papercut's
   autopsy loop, generalised. Every skill in this batch stops at delivery.
7. **Templates and a completeness check.** Fill-in templates for each product
   artifact and a mechanical check (full-output-enforcement's scope-lock, hardened
   into a script) that fails a phase whose manifest lists an artifact that is
   missing, empty, or still carrying `TBD`s nobody has signed off.

**Verdict counts for this batch:** ADOPT 1 (local-skill-creator), ADAPT 4 (local-prd,
local-kaggi, local-humanizer, local-full-output-enforcement), DROP 2
(local-slopmonster, recovered-skill-notes), OUT-OF-SCOPE 3 (local-brag,
local-brag-slim, local-live-carousel).

**The five most valuable mechanisms to carry into the unified suite:** (1) kaggi's
user-owned phase gates combined with the explicit one-time grant for irreversible
actions and the mandatory structured journal; (2) skill-creator's paired
with-skill/baseline eval loop with assertions, grading, and held-out trigger
optimisation — the suite's own QA; (3) PRD's discovery-before-drafting gate, its
measurable-criteria standard, and its label-it-`TBD` ban on invented constraints;
(4) brag's gate ladder — rubric gate, plan-file gate, machine-check gate (`hyperframes
check` at zero errors), deliverable gate — with its one-paragraph ownership split
between orchestrator and executor; (5) the prose-QA pair: humanizer's
fact-preservation audit (added or dropped fact, name, number, or claim is an error)
reinforced by slopmonster's deterministic checker that confesses its own limits and
its cross-model-family second pass with explicit failure reporting.

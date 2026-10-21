# Audit Batch C — Design / Frontend Skill Cluster

Scope: 33 skills in `~/workspace/custom-skills/` covering design taste, frontend build, Stitch, shadcn, brand/logo, and the ui-ux-pro-max (uupm) family.
Method: every SKILL.md read (short ones in full; the 800–1,500-line prompt-style ones skimmed structurally and judged as artifacts — heading skeleton, rule repetition, tooling). Line/file counts are from the actual folders.
Verdicts are relative to one unified rnov24 system (artifact-based, orchestrator-led, in the style of addyosmani/agent-skills and mattpocock/skills): **ADOPT** = survives as-is, **ADAPT** = survives after surgery, **DROP** = remove, **MERGE-INTO** = standalone dies, best parts move into the named target.

---

## 1. local-atelier (82 lines + 10 reference files, 64K)

**Purpose:** Jal's own design crew in one skill — PRD ingest → brief → 11-part DESIGN.md → mandatory Stitch keyframe loop per page → build → five-persona council review → QA → ship.

**Pros:**
- The only skill in the batch built around *artifacts and delegation*: DESIGN.md is the constitution, the Builder implements and "never writes the taste," reviewers are separate subagents. This is exactly the orchestrator pattern the unified system wants.
- Bounded verification is written down: build → one batched review round → one batch fix → at most one more round → stop. Anti-loop discipline almost no other skill has.
- Quantified taste: Density / Motion / Boldness / Strangeness levels 1–5 set in the brief, so later decisions are checkable against numbers instead of vibes.
- Three honest entry modes (blank-canvas / phoenix redesign / tune-up) and "the brief wins over taste" as an explicit rule.

**Cons:**
- Hard Stitch lock-in: the keyframe loop is *mandatory* and Stitch-specific, so the whole workflow dies or stalls when Stitch is unavailable, slow, or the wrong tool (native app, design-system work).
- Council of five named personas (Wren, Magpie, Tortoise, Fox, Lark) is charming but expensive — five reviewer subagents per page is a lot of tokens for small pages, and persona debate can produce theatre instead of findings.
- Taste still lives in prose (`niche-moves.md`, "at least two niche moves") — distinctive, but not verifiable; a builder can claim any two moves.

**Verdict: ADOPT** — this is the backbone of the unified design workflow. (Surgery happens inside it: keyframe loop becomes tool-agnostic, council becomes scalable.)

## 2. local-design-taste-frontend / tasteskill v2 (415 lines, 1.8M, library + scripts + evals)

**Purpose:** Anti-slop art direction: deal a researched design direction from a library built from 247 curated gallery sites, build to it, then run a real-browser inspect → screenshot → look-and-fix loop.

**Pros:**
- Real mechanisms, not just prose: `scripts/draw.mjs` deals directions (sector/roles/tone/assets), `inspect.mjs` and `lint.mjs` check the built page, there is an `evals/` folder — one of only two skills in the batch with evals.
- The "subject inventory" step (8–12 things true of this client and no competitor) and "write the argument" step (page as claims with proof; delete sections with no claim) are genuinely strong brief discipline that Atelier lacks.
- Asset honesty: directions are constrained by `--have` (only plan around imagery that actually exists), with open-archive sourcing as the fallback. Prevents the classic fake-product-shot failure.
- Redraw discipline: a dealt slot may be redrawn only for a statable reason, and every redraw is recorded in the report — auditable randomness instead of silent drift.

**Cons:**
- The dealt-direction model fights the brief model: "adopt it, do not blend" plus redraw guilt is a strong ideology that will clash with client-pinned directions and with Atelier's DESIGN.md-first flow if both run.
- Heavy: 1.8M of library JSON, its own base.css/base.js, sector/role taxonomy to learn. Running it *and* Atelier means two competing art-direction authorities.
- House style is one aesthetic (gallery/editorial) presented as universal law; weak fit for Operate-mode product UI, dashboards, dense tools.

**Verdict: ADAPT** — keep the library, draw, inspector and evals as the *direction + visual-QA engine* inside the unified workflow; strip its claim to be the top-level workflow.

## 3. local-gpt-taste (76 lines, single file)

**Purpose:** "Awwwards-level" manifesto: Python-randomized layout choices, AIDA page structure, 2-line hero rule, gapless bento grids, GSAP ScrollTrigger physics, pre-flight `<design_plan>`.

**Pros:**
- A few concrete, checkable rules: hero headline max 2 lines, gapless bento (`grid-flow-dense`), mandatory pre-flight design plan before code.
- The randomization idea (break the model's layout rut by external dice) is a real mechanism, even if crude.

**Cons:**
- Pure prompt-bloat manifesto: ALL-CAPS directives, no artifacts, no verification, no references — nothing to check output against except the same prose.
- AIDA + bento + GSAP pinning is one narrow landing-page recipe universalized to all frontend work; actively harmful for product UI.
- Almost total overlap with high-end-visual-design and stitch-craft (which literally imports its rules in Phase 0).

**Verdict: MERGE-INTO local-atelier** — salvage the 2-line hero rule, bento discipline and pre-flight plan into Atelier's motion/layout references; delete the standalone.

## 4. local-high-end-visual-design (99 lines, single file)

**Purpose:** Agency-feel visual design: anti-pattern bans, vibe/layout archetype picker, "double-bezel" nested cards, island buttons/nav, magnetic hovers, motion choreography, pre-output checklist.

**Pros:**
- Named, reusable component moves (Double-Bezel/Doppelrand, Island CTA, Fluid Island nav) — more transferable than generic "make it premium" prose.
- Has a performance guardrails section and a pre-output checklist, which most manifestos skip.

**Cons:**
- Same genre as gpt-taste: unverifiable superlatives ("expensive feel"), archetype roulette, no tooling, no artifacts.
- Its signature moves are fashion, not system: double-bezel everything becomes the next template tell, exactly what it claims to fight.
- Overlaps minimalist-ui / industrial-brutalist-ui in structure (archetypes + bans + type + motion) with opposite conclusions, proving these are presets, not principles.

**Verdict: MERGE-INTO local-atelier** — keep the named component moves as optional entries in Atelier's niche-moves library.

## 5. local-minimalist-ui (87 lines, single file)

**Purpose:** One fixed aesthetic preset: warm monochrome editorial minimalism, flat bento, muted pastels, no gradients, no heavy shadows.

**Pros:**
- Honestly scoped: it is a *preset*, with concrete palette, type architecture, component specs and banned elements — internally consistent and immediately usable.
- Short and cheap to load; the bans are mostly checkable (gradient present? shadow weight?).

**Cons:**
- A preset sold as a skill: zero workflow, zero adaptation logic — if the brief isn't warm-monochrome editorial, the skill has nothing to say.
- Hard bans (no gradients, ever) conflict with briefs and with sibling presets; loading two presets at once guarantees contradiction.

**Verdict: MERGE-INTO local-atelier** — as a style-preset card in the direction library (alongside the dealt directions of tasteskill), not a standalone skill.

## 6. local-industrial-brutalist-ui (93 lines, single file)

**Purpose:** One fixed aesthetic preset: Swiss industrial print × military/CRT telemetry — rigid grids, extreme type-scale contrast, analog degradation, for data-heavy dashboards and editorial sites.

**Pros:**
- The most *specific* preset in the batch: two named archetypes with separate light/dark color systems, macro/micro typography split (structural headers vs telemetry data) — the micro-typography idea is genuinely useful for dashboards.
- Clear applicability statement (data-heavy, blueprint feel) instead of claiming universality.

**Cons:**
- Same structural problem as minimalist-ui: preset-as-skill, no workflow, no QA, bans by vibe.
- Texture/degradation effects (CRT, analog noise) are performance and accessibility risks with no guardrails mentioned.

**Verdict: MERGE-INTO local-atelier** — as a style-preset card; keep its macro/micro type split as a general dashboard pattern.

## 7. local-frontend-design (72 lines, single file, Anthropic)

**Purpose:** Principles for distinctive, non-templated design: ground in the subject matter, plan tokens in two passes, review the plan against the brief for default-ness, then build with restraint.

**Pros:**
- The best *principles* text in the batch: a concrete calibration list of current AI design defaults (cream+serif+terracotta, near-black+acid accent, broadsheet, SaaS-card kit, eyebrow/→ tells) — specific enough to actually steer away from.
- The two-pass process (plan as tokens + ASCII wireframes → self-review "would I produce this for any similar prompt?" → revise → build) is a cheap, powerful anti-generic gate that needs no tooling.
- Writing-in-design section (active voice, consistent action names, errors that explain, empty states as invitations) covers UX copy better than skills ten times its size.

**Cons:**
- No artifacts, no checklists, no verification step beyond "take screenshots if you can" — it improves judgement, it doesn't enforce anything.
- Web/hero-centric; little to say about dense product UI, forms, or design systems.

**Verdict: ADOPT** — as the principles layer of the unified system (the "constitution preamble" every design skill defers to).

## 8. local-emil-anim (wrapper 15 lines; 4 sub-skills, ~1,300 lines incl. STANDARDS.md)

**Purpose:** Emil Kowalski's animation craft: find animation opportunities, improve/audit motion, and review animation code against a written standards reference.

**Pros:**
- The most *verifiable* taste in the batch: STANDARDS.md gives numbers and rules a reviewer can literally check — easing by intent (enter = ease-out), never `scale(0)` (start 0.9–0.97), press feedback `scale(0.97)`/160ms, animate only transform/opacity, momentum dismissal velocity threshold, damping at drag boundaries.
- Proper skill architecture: small wrapper, sub-skills per job (find / improve / review), AUDIT.md + PLAN-TEMPLATE.md artifacts for the improve loop.
- Debugging guidance is real-world: slow-motion passes, DevTools Animations panel, test gestures on a real device, fresh-eyes-next-day.

**Cons:**
- Web/CSS/Framer-Motion centric; the Framer shorthand warning and WAAPI advice don't transfer to native or canvas work.
- The 674-line `emil-design-eng` sub-skill is broader than animation and will drift out of sync with the tighter review standards.

**Verdict: ADOPT** — the motion chapter of the unified system, unchanged in substance.

## 9. local-impeccable (86-line router + ~40 reference files, scripts, hooks; 2.3M)

**Purpose:** Full frontend design OS: PRODUCT.md/DESIGN.md project context, four surface modes (Persuade / Operate / Read / Experience), and ~25 commands — shape, init, document, extract, critique, audit, polish, bolder, quieter, harden, onboard, animate, colorize, typeset, layout, live variant iteration, plus a design-detector hook and a `doctor` drift checker.

**Pros:**
- Artifact-based like the target system: durable PRODUCT.md + DESIGN.md per project, surface briefs, and a doctor that detects drift between artifacts and reality — the only skill that maintains its own artifacts over time.
- The mode taxonomy is the best scoping device in the batch: it stops landing-page taste being applied to dashboards (the failure mode of gpt-taste et al.) by naming what visitor success means per surface.
- Command granularity maps cleanly onto an orchestrator's delegation menu (audit vs critique vs polish vs harden are different jobs with different references), and the hook (auto-detector after UI edits) is a real enforcement mechanism, not prose.

**Cons:**
- Directly competes with Atelier as top-level orchestrator — two directors, two DESIGN.md formats, two review loops. Running both is incoherent; one must subordinate.
- Big surface: ~40 reference files, native variants, pin/unpin shortcuts, live-browser tooling. High maintenance and load cost; many commands (delight, overdrive, bolder) are taste dials with soft criteria.
- Its DESIGN.md/PRODUCT.md conventions would need reconciling with Atelier's 11-part DESIGN.md — a real migration cost, not a merge by copy-paste.

**Verdict: ADAPT** — adopt its mode taxonomy, command menu, hook and doctor into the unified system; demote it from co-director to the execution/QA arm under one workflow.

## 10. local-image-to-code (1,229 lines, single file)

**Purpose:** Image-first web building: generate section design images yourself, analyze them deeply, then implement to match — never crop old images, regenerate fresh, generate "enough" images.

**Pros:**
- The core discipline is right and matches how Jal actually works (rendered keyframe → user verdict → code): image first, code second, fidelity to the keyframe is the acceptance test.
- Combinatorial variation engine (theme × background × type × hero × section system) is a usable prompt-construction checklist for keyframes.

**Cons:**
- Extreme prompt-bloat: 1,229 lines / ~5,800 words to say a 100-line idea, with numbered "RULE"s repeating the same injunctions (no cropping is stated at least four ways). Token-expensive every load, and repetition dilutes the load-bearing rules.
- Written for "Codex" by name and assumes its image tool; the workflow half (analysis standard, fidelity loop) is buried inside tool-specific generation nagging.
- No stopping rule: "generate enough / never under-generate" pushes toward image spam and quota burn with no budget or acceptance gate.

**Verdict: MERGE-INTO local-atelier** — compress to a one-page keyframe-fidelity protocol inside Atelier's keyframe loop; delete the standalone.

## 11. local-imagegen-frontend-web (988 lines, single file)

**Purpose:** Generate premium website design *reference images* — one separate horizontal image per section, with composition/CTA/hero-scale variety rules.

**Pros:**
- The one-image-per-section rule is concrete and produces legible, implementable keyframes instead of unreadable mood boards.
- Per-section variation axes (composition anchor, background mode, CTA variation, hero scale) are a practical checklist against the all-sections-look-alike failure.

**Cons:**
- Same bloat pattern as image-to-code (~5,800 words, "HARD OUTPUT RULE — READ FIRST" shouting, combinatorial engine duplicated almost verbatim between the two skills — they share whole sections).
- Pure generation-side: no analysis, no implementation, no fidelity check — it makes pictures and stops, so it cannot stand alone as a workflow.
- Hard rules (always horizontal, always separate) are format dogma that breaks for tall/hero or continuous-scroll designs.

**Verdict: MERGE-INTO local-atelier** — its per-section keyframe checklist becomes the prompt recipe in Atelier's keyframe loop; the file itself goes.

## 12. local-imagegen-frontend-mobile (1,466 lines, single file)

**Purpose:** The mobile twin of the above: premium app screen concepts — screen-first, multi-screen consistency via an "App Design Bible," platform modes (iOS / Android / cross-platform), mockup framing, onboarding and navigation rules.

**Pros:**
- The App Design Bible + multi-screen consistency rules address the real mobile failure (every generated screen invents a new app) better than anything else in the batch.
- Platform-mode distinction (iOS-native vs Android-native vs neutral) and safe-area/navigation rules show actual mobile literacy, not just shrunk web thinking.

**Cons:**
- The longest file in the batch (1,466 lines / ~6,500 words) with the same duplicated combinatorial engine and rule-shouting as its web siblings — three near-identical engines in three files.
- Mockup-frame default (screens inside phone frames) is presentation chrome that can fight fidelity when the image is meant as an implementation reference.
- Generation-only again: no build, no QA, no handoff format for the developer.

**Verdict: MERGE-INTO local-atelier** — keep the Design Bible + consistency + platform-mode rules as Atelier's mobile keyframe annex; delete the standalone.

## 13. local-brandkit (844 lines, single file)

**Purpose:** Brand-kit *image generation*: strategy-first identity boards — logo concept methods, 3×3 panel board system (cover, construction, applications…), boards/decks in minimalist, cinematic, luxury, dark-tech etc. worlds.

**Pros:**
- Strategy before visuals: brand intake + strategy step precedes generation, and the five logo concept methods (monogram+meaning, product action, metaphor fusion, negative space, construction geometry) are a real ideation checklist.
- A defined deliverable format (the 3×3 board) makes output comparable across runs and presentable to a client/user for a verdict.

**Cons:**
- 844 lines to drive an image model; the board format is the product, so quality is capped by image-gen logo rendering (garbled wordmarks, unusable vectors) — it produces *presentations of* identity, not production identity files.
- Overlaps logo-design-skill (which does real SVG + testing) and uupm-design's CIP boards, with weaker deliverables than both.

**Verdict: ADAPT** — keep as the optional *brand-board presentation* module downstream of a real mark; never as the logo source of truth.

## 14. local-logo-design-skill (nested SKILL.md 223 lines; 1,589 files, 24M — mostly a 1,400+ SVG library + .git)

**Purpose:** Professional logo design end-to-end: discovery brief → category research against a searchable library of 1,400+ real SVG logos → geometric SVG concepts → testing → presentation → production variants and guidelines, with dependency-free Python scripts.

**Pros:**
- The strongest tooling in the batch: `svg_audit.py` (live text, rasters, color count, near-miss angles), `preview_sheet.py` (size ladder down to 16px, one-colour, reversed, squint, shelf test vs competitors), `concept_sheet.py`, `presentation_board.py`, `export_variants.py` (favicon/app-icon/webmanifest sets). Verification is executable, not vibes.
- Process discipline that respects the user: a hard concept checkpoint — show concepts and recommendation, build the full kit only after the user picks a direction.
- Anti-cliché research step (list the category's clichés, treat as off-limits) and "identifier, not explanation" philosophy keep concepts honest.

**Cons:**
- 24M footprint, ships its own `.git` and a tech-skewed library (the skill itself admits the skew); library searches for non-tech sectors are thin.
- SVG-by-code is drawing blind — the skill mitigates with render-and-look, but concept quality still hinges on the model's geometry discipline.
- Claude-Code path assumptions (`${CLAUDE_SKILL_DIR}`) need adaptation per runtime.

**Verdict: ADOPT** — the identity specialist of the unified system; brandkit and uupm logo features defer to it.

## 15. local-redesign-existing-projects (182 lines, single file)

**Purpose:** Upgrade an existing site/app in place: audit across typography, color, layout, states, content, components, iconography, code quality and "strategic omissions," then apply upgrade techniques by fix-priority ladder.

**Pros:**
- The audit taxonomy is genuinely useful, especially "Strategic Omissions (What AI Typically Forgets)" and the explicit fix-priority ordering — it triages instead of rewriting everything.
- Framework-agnostic and functionality-preserving by charter ("without breaking functionality"), which most redesign advice ignores.

**Cons:**
- It is Atelier's tune-up mode plus impeccable's audit/polish, written as a third standalone: same audit categories, same premium-upgrade moves (type upgrades, surface upgrades, motion upgrades) found in high-end-visual-design.
- Checklist without tooling: no scripts, no before/after capture requirement, no regression check — the "don't break functionality" promise has no mechanism behind it.

**Verdict: MERGE-INTO local-atelier** — its audit taxonomy + fix-priority ladder become the tune-up mode's checklist, with screenshot before/after made mandatory there.

## 16. local-design-loop (528 lines, single file)

**Purpose:** Autonomous multi-page site builder via baton passing: each run reads `.design/next-prompt.md`, generates a page, integrates it, verifies visually, and writes the next baton — backends: direct generation or Stitch SDK.

**Pros:**
- The baton is the best *orchestration* mechanism in the batch: a durable, file-based handoff (state, next task, context pointers) that makes multi-session, multi-agent work resumable — directly reusable by the unified system's subagent delegation.
- Integration discipline: new pages must reuse the exact shared header/footer extracted from the most recent page; visual verification step before writing the next baton.
- Backend-agnostic in principle (Claude default, Stitch optional) — one of the few Stitch-adjacent skills not hard-locked to Stitch.

**Cons:**
- Output lock-in: self-contained single-file HTML + Tailwind CDN, no build step — fine for throwaway marketing sites, wrong default for real projects in a component stack.
- Autonomy without a budget: "keep the loop alive" has no page cap, cost cap, or user checkpoint; combined with permissive triggering ("just keep going") it can burn quota building unreviewed pages.
- Duplicates stitch-loop's baton system almost exactly — two baton schemas to maintain.

**Verdict: ADAPT** — adopt the baton as the unified system's standard handoff artifact; drop the Tailwind-CDN output lock and add checkpoints/caps.

## 17. local-scrollytelling (345 lines, single file + real CLI)

**Purpose:** Turn a video or image folder into a scroll-scrubbed landing page (Next/Nuxt/Astro/plain HTML) via the `@danhnm1203/scrollytelling` CLI: frame extraction, scroll-driven scrub, copy beats, snapping layout, reduced-motion support.

**Pros:**
- Narrow, real, and verifiable: an actual installed tool with scaffold/frames commands, a measurement checkpoint, and a verification section — claims can be checked (frame counts, scrub behavior).
- Correct technical reasoning documented (why a frame sequence beats `<video>` seeking), plus reduced-motion and mobile fallbacks treated as first-class, not afterthoughts.
- Includes this VM's environment adaptations — it has survived contact with reality here (also: Jal's explicit redirect that personal-site work uses this + DESIGN.md, not Stitch).

**Cons:**
- One-trick scope by design: it is a hero technique, not a design workflow; it will be over-applied if it ranks beside general skills.
- Asset prerequisite is heavy (needs footage or frame sequences), and scroll-scrub pages are a performance/a11y liability when used as decoration.

**Verdict: ADOPT** — as a specialist technique module the workflow can call, not a peer workflow.

## 18. local-shadcn-component-discovery (275 lines + registries reference)

**Purpose:** Search-before-you-build for shadcn-compatible components across the whole registry ecosystem (official MCP, CLI, or web when no project), present options, then install.

**Pros:**
- Attacks a real cost: agents hand-rolling tables/modals that already exist as maintained components. The three access paths (MCP preferred → CLI → no-project research) degrade gracefully.
- Proactive trigger design: it is meant to fire *during* build planning, not only when asked — the right shape for a discovery step in an orchestrated build phase.
- Presentation format is decision-ready (registry, name, what it is) rather than a link dump.

**Cons:**
- Registry quality is uneven and unvetted by the skill — discovery without a quality/security bar can import slop faster than writing it.
- shadcn/React/Tailwind lock-in; useless outside that stack, and it assumes the official shadcn skill/MCP context that may not be configured.

**Verdict: ADOPT** — becomes the component-discovery step of the unified build phase (with a vetting note added).

## 19. local-shadcn-component-review (243 lines + checklist/animation/theme references)

**Purpose:** Review custom shadcn-style components and layouts against design-pattern conventions: composition, spacing audit, design-token usage, CVA variants, `cn()`, theme-aware styling, responsive/a11y, across the Vega/Nova/Maia/Lyra/Mira style variants.

**Pros:**
- Concrete, diff-able criteria: hardcoded colors, spacing drift, missing `data-slot`, token misuse — a reviewer (human or subagent) can point at lines, unlike taste prose.
- Honest scoping section ("What This Skill Does NOT Enforce") — rare humility that prevents checklist imperialism.
- Pairs naturally with discovery: one finds components, this one keeps custom ones idiomatic; together they form the component QA gate.

**Cons:**
- Same stack lock-in (shadcn/Radix/Tailwind/CVA); the five style-variant references will rot as upstream styles evolve.
- Review-only: no autofix, no script/linter — enforcement depends on reviewer diligence.

**Verdict: ADOPT** — the component-review gate of the unified build phase.

## 20. local-web-design-guidelines (40 lines, single file, Vercel)

**Purpose:** Review UI code against Vercel's Web Interface Guidelines: fetch the current guidelines from a source URL, read the specified files, output findings in the specified format.

**Pros:**
- Tiny, honest wrapper; because rules are fetched live, they stay current instead of fossilizing in a prompt.
- Clear trigger phrases and a defined findings format — good reviewer ergonomics.

**Cons:**
- The entire value lives at a remote URL: if it moves, changes tone, or is unreachable (this VM's egress proxy blocks plenty), the skill is an empty envelope. Unversioned external truth is unverifiable in review.
- 40 lines means zero local substance — no prioritization, no severity model, no overlap control with impeccable audit / shadcn review.

**Verdict: ADAPT** — vendor a pinned, dated copy of the guidelines into the unified QA references (update deliberately, like a dependency), keep the fetch as an update path only.

## 21. local-ux-skill (35-line authored wrapper; engine + 25 commands + 5 agents + 12 JSON manifests; 591 files, 7.5M)

**Purpose:** Design-intelligence engine (ux-skill v3.2.1, MIT): 25 `/ux-*` commands, 5 sub-agents, a deterministic anti-pattern linter, queryable data manifests (styles, palettes, type pairings, components, industries) and a Python engine (generator/evaluator/decisions ledger/brand fidelity).

**Pros:**
- Deterministic parts exist: an anti-pattern linter and an evaluator that don't depend on model mood, plus a decisions ledger — artifacts and checks an orchestrator can actually gate on.
- Data-over-prose design: manifests are queryable JSON, so "which palette for fintech" is a lookup with provenance, not a manifesto recital.
- Command set covers the full arc (discover → design → component → dashboard → audit → critique → fix → evolve), showing the shape of a complete UX workflow.

**Cons:**
- Massive and sprawling: 7.5M, 591 files, 25 commands and 5 agents that overlap impeccable's command menu and uupm-pro-max's data pitch — three design-intelligence engines is two too many.
- The authored local SKILL.md is only 35 lines of wrapper; the real behavior lives in commands/engine a reader must excavate, so trigger discipline and quality vary by sub-part.
- Engine is Python with `__pycache__` shipped and a PHASE-PLAN of its own — it is a product, not a skill, with a product's maintenance bill.

**Verdict: ADAPT** — harvest the linter, the manifests and the decisions-ledger idea into the unified QA layer; retire the command sprawl and engine as a standalone system.

## 22. local-uupm-design (334 lines + 12 references, 376K)

**Purpose:** Kitchen-sink design router: logo generation (55 styles, via Gemini/Atlas Cloud/MuAPI), corporate identity program (50 deliverables + mockups), icon design, banners, slides, social photos — mostly by calling external AI image APIs through bundled scripts.

**Pros:**
- The CIP (corporate identity program) deliverable taxonomy — 50 named deliverables with a guide — is a genuinely useful completeness checklist for identity work.
- Routing table up front at least admits these are different jobs (logo ≠ banner ≠ slides).

**Cons:**
- Breadth as a substitute for depth: six products in one skill, each done better by a specialist already installed (logo-design-skill, brandkit, uupm-slides, uupm-banner-design — the last two are *also in this batch*, so it even duplicates its own family).
- Hard dependency on third-party image APIs (Atlas Cloud, MuAPI) with keys/pricing/availability outside our control; outputs are mockups, not production assets.
- Script-path sprawl and prompt-engineering references per sub-feature make it the highest-maintenance way to get the worst version of each deliverable.

**Verdict: DROP** — salvage only the CIP deliverable checklist into local-brandkit; the router and API plumbing go.

## 23. local-uupm-design-system (249 lines + token references + slide CSVs, 248K)

**Purpose:** Design-token architecture and component specs: three-layer tokens (primitive → semantic → component), CSS variables, spacing/typography scales, component spec pattern — plus a slide-generation system fed by decision CSVs.

**Pros:**
- The three-layer token model is the canonical, correct architecture and the only rigorous token treatment in the batch: primitive → semantic → component, with per-layer references. This is exactly what a DESIGN.md needs underneath it to become executable.
- Component spec pattern gives tokens a contract components can be reviewed against (pairs with shadcn-component-review).

**Cons:**
- Two skills stapled together: half the payload is a slide system (layout/copy/chart CSVs, BM25 slide search) that has nothing to do with tokens and belongs with slides tooling.
- Reference-heavy but enforcement-light: no validator script that checks a codebase against the token layers.

**Verdict: ADAPT** — adopt the token architecture + component spec pattern as the unified system's design-system chapter; amputate the slide half.

## 24. local-uupm-ui-styling (337 lines + ~90 font files, 5.8M)

**Purpose:** How-to for building UIs with shadcn/ui + Tailwind + a canvas visual-design layer: setup, component guide, theming/dark mode, accessibility patterns, Tailwind customization, bundled canvas fonts.

**Pros:**
- Competent, conventional stack guidance: Radix-based accessibility patterns, theme customization, responsive utilities — the "boring correct" baseline for shadcn projects.
- Bundled OFL fonts make the canvas/poster features reproducible offline.

**Cons:**
- Mostly documentation the model already knows, frozen at install time: shadcn/Tailwind docs in prose form rot quickly and add load cost without adding judgement, artifacts, or checks.
- 5.8M of the 5.8M is font binaries for a niche canvas feature; the skill's center of gravity (UI styling) is the part with the least unique content. Overlaps shadcn-component-review (patterns) and uupm-design-system (theming) without their review/token rigor.

**Verdict: MERGE-INTO local-uupm-design-system** — keep the theme/accessibility pattern notes in the unified design-system chapter; drop the doc-recital and ship fonts separately or not at all.

## 25. local-uupm-ui-ux-pro-max (215 lines + searchable CSV data + Python search, 3.8M)

**Purpose:** Design intelligence by database: Python BM25-style search over styles, 192 product palettes/reasoning profiles, font pairings, UX guidelines, icons, GSAP presets and stack guides; `--design-system` generates a project design system and can persist it as Master + Overrides files.

**Pros:**
- Data-backed instead of manifesto-backed: answers come from queryable datasets with a provenance file, and the search tool is plain Python with no external dependencies — runnable and testable here.
- The persist pattern (Master design-system file + per-page Overrides) is a real artifact architecture an orchestrator can version, diff and hand to subagents — one of the few concrete artifact schemes outside Atelier/Impeccable.
- Priority-ordered rule categories (accessibility > interaction > layout…) give reviews a triage order instead of a flat rule pile.

**Cons:**
- Dataset curation is opaque at the edges: headline counts (79 styles "50 active", 192 palettes) invite trust the data may not earn; a plausible-but-wrong palette lookup is worse than admitted taste.
- Overlaps ux-skill's manifests and impeccable's design-system generation — third engine for the same job.
- Windows of rot: fonts/icons/GSAP preset data ages, and there's no update cadence defined.

**Verdict: ADAPT** — keep the search tool + Master/Overrides persistence as the unified system's *design-system generator*; consolidate its data with ux-skill's manifests instead of running two databases.

## 26. local-uupm-brand (109 lines + 11 references + extract-colors script, 144K)

**Purpose:** Brand governance: voice framework, visual identity, messaging framework, logo usage, consistency/approval checklists, and a sync workflow from `brand-guidelines.md` → design tokens → verify.

**Pros:**
- The brand→tokens sync workflow is the missing link between brand documents and code in most of this batch: guidelines as source, tokens as compiled output, verification as a step.
- Governance artifacts (consistency checklist, approval checklist, asset organization) suit an orchestrator handing brand work to subagents.

**Cons:**
- Thin: 489 words of SKILL.md leaning on generic references (voice framework, messaging framework) that read as templates awaiting content.
- Overlaps brandkit (identity creation) and logo-design-skill's guidelines phase; as a standalone it is the paperwork layer of jobs owned elsewhere.

**Verdict: MERGE-INTO local-brandkit** — its guidelines artifact + sync-to-tokens workflow becomes brandkit's governance chapter (with logo-design-skill remaining the mark's source of truth).

## 27. local-uupm-banner-design (146 lines + size/style reference)

**Purpose:** Banner design across social/ads/hero/print: requirements interview, art-direction options (10 named styles), generation, export to exact platform sizes, present-and-iterate.

**Pros:**
- The platform size reference (Facebook/X/LinkedIn/YouTube/Instagram/Google Display/print) is factual, reusable data — the kind of table an agent should look up, not improvise.
- Present-multiple-options-then-iterate matches how banner work is actually approved.

**Cons:**
- A single deliverable type wearing a whole skill: the workflow is "ask, generate options, export, iterate," which is every image skill's workflow with a size table attached.
- Duplicated inside uupm-design (banner is one of its six routes) and adjacent to brandkit boards; three homes for banner logic.

**Verdict: MERGE-INTO local-brandkit** — the size/style tables become a reference file in the brand/asset module; the standalone dies.

## 28. local-uupm-slides (45 lines + 5 references, 32K)

**Purpose:** Strategic HTML presentations: Chart.js charts, design tokens, copywriting formulas, slide strategies, routed subcommands for create etc.

**Pros:**
- Treats slides as designed artifacts (tokens, layout patterns, strategy per slide) rather than bullet dumps; copywriting formulas give decks a narrative spine.

**Cons:**
- Out of this cluster's scope: presentations are a separate product line (and the repo has dedicated deck tooling); including it in a *frontend design* system dilutes both.
- It is a thin router (222 words) whose substance lives in references shared with uupm-design and uupm-design-system's slide half — the same slide system appears three times in one family.

**Verdict: DROP** (from the design system) — if deck work is wanted later, resurrect it as its own standalone, fed by the unified token chapter.

## 29. local-stitch (43 lines, single doc + client)

**Purpose:** Infrastructure doc for Jal's direct Stitch MCP integration: the `~/workspace/stitch/stitch_mcp.py` client, its 15 tools (projects, screens, design systems), API-key location, and operational quirks.

**Pros:**
- Short, factual, and earned: endpoint/transport facts (Streamable HTTP, SSE GET = 405), the "results are huge, pipe through head" warning, and Jal's explicit no-opencode decision are recorded where the next agent will find them.
- Correct separation of concerns: this is plumbing documentation, not a workflow manifesto — other skills should reference it, not restate it.

**Cons:**
- Not a portable skill: hardcodes this machine's paths and key location, so it can't be published or shared as-is (fine for a local system, must be quarantined from any public repo).
- No error-recovery guidance beyond size warnings; timeouts (a known local pain: generation calls run 77–90s+) are only in AGENTS.md, not here.

**Verdict: ADOPT** — as the local Stitch plumbing layer under the unified workflow (kept private/local, referenced not copied).

## 30. local-stitch-design (router doc; official Google Labs plugin, 6 sub-skills, 252K)

**Purpose:** The official Stitch plugin suite: generate-design, code-to-design, extract-design-md, extract-static-html, manage-design-system, upload-to-stitch — with per-framework references (React/Tailwind, Vue, Svelte, Angular, plain CSS).

**Pros:**
- Bidirectional, which no local skill matches: code → Stitch design and Stitch → static HTML extraction, plus DESIGN.md *extraction from an existing codebase* (the fastest way to bootstrap the artifact the whole system runs on).
- Official and maintained upstream; framework-specific extraction references keep DESIGN.md output idiomatic per stack.
- Composes cleanly: these are tools with inputs/outputs, not opinions — an orchestrator can call them without adopting a foreign workflow.

**Cons:**
- Plugin-format assumptions (Codex/Claude plugin layout) and Stitch availability still gate everything; extraction quality varies and its DESIGN.md schema must be reconciled with Atelier's 11-part template.
- The local router doc is thin (37 lines) — real behavior lives in six sub-skills that must be read individually at use time.

**Verdict: ADOPT** — the Stitch tool arm of the unified workflow; its extract-design-md becomes the standard bootstrap for existing projects.

## 31. local-stitch-design-taste (186 lines + sample DESIGN.md)

**Purpose:** Author a *semantic* DESIGN.md for Stitch: atmosphere, palette as descriptive color, typography rules, hero, components, layout, responsive, motion philosophy, and an explicit anti-patterns ("AI tells") list — prose a design model can interpret, not tokens.

**Pros:**
- Understands its medium: Stitch consumes descriptive language ("warm off-white like sun-bleached paper"), so the skill teaches writing *interpretable* design language with reasoning attached to each color/type choice.
- The anti-pattern list as a named DESIGN.md section is a clean idea — negative space in the spec, portable to any DESIGN.md template.

**Cons:**
- It is a DESIGN.md *format*, and the system already has two: Atelier's 11-part template and Impeccable's DESIGN.md. A third format guarantees conversion friction every time artifacts move between skills.
- Single-purpose and Stitch-shaped: hero-section centrality and atmosphere-first ordering fit marketing pages, not product UI; no tokens, no component specs, nothing executable.

**Verdict: MERGE-INTO local-atelier** — fold its semantic-writing guidance and anti-patterns section into Atelier's DESIGN.md template; one format survives.

## 32. local-stitch-craft (165 lines + 6 references + 3 scripts, 52K)

**Purpose:** A meta-orchestrator (Jal's own): Phase 0 "machine skill amalgamation" (discover installed design skills and merge their directives), brief interview → brief.md, up to 8 Stitch design passes, code translation, multi-viewport Stitch review, scrollytelling/motion phase, and an "Awwwards jury" story review.

**Pros:**
- Real utilities under the prose: `brief_scaffold.py` (standardized brief.md), `verify_responsive.py` (linter for viewport breakage, font issues, AI clichés), multi-viewport snapshot capture — verification as code.
- The brief.md constitution idea and the responsive-parity review are the right instincts, and the phase structure shows the shape of the unified workflow Jal wants.

**Cons:**
- Architecturally the wrong shape for a unified system: it *amalgamates other skills' directives at runtime* (gpt-taste's bento rules + stitch-design-taste's palette rules + …), which imports every contradiction between them and makes runs non-reproducible — the same project can get a different merged doctrine each time the installed-skill set changes.
- Directly duplicates Atelier's director role with a different brief format, different review (jury vs council) and an 8-pass Stitch loop with no cost bound; two orchestrators cannot both own a project.
- Stitch-CLI lock-in is total: phases 2–4 assume the CLI, its auth, and its viewport model.

**Verdict: DROP** — as an orchestrator. Salvage `verify_responsive.py`, the brief scaffold and the story-review rubric into Atelier's QA stage before deleting.

## 33. local-stitch-loop (83 lines + baton schema/SITE.md examples)

**Purpose:** Multi-page site building on Stitch via the same baton system as design-loop: read `.design/next-prompt.md`, consult SITE.md/DESIGN.md context, generate with Stitch, integrate, update site docs, write the next baton.

**Pros:**
- The baton schema + SITE.md example are the cleanest *specification* of the handoff format in the batch (fields, pitfalls, troubleshooting) — good source material for standardizing the artifact.
- Context-file discipline (SITE.md as living site documentation updated every iteration) is a genuinely good maintenance habit.

**Cons:**
- Functionally a fork of design-loop with the generator swapped: same baton, same steps, same pitfalls — maintaining both guarantees schema drift between the two baton files.
- Stitch-only generation path inherits all Stitch availability/timeout risks, with none of design-loop's backend choice.

**Verdict: MERGE-INTO local-design-loop** — one baton schema survives; Stitch stays as one of its backends, and this file's schema/examples become the canonical baton spec.

---

# Batch Summary

## Verdict counts (33 skills)

| Verdict | Count | Skills |
|---|---|---|
| ADOPT | 9 | atelier, frontend-design, emil-anim, logo-design-skill, scrollytelling, shadcn-component-discovery, shadcn-component-review, stitch (infra), stitch-design |
| ADAPT | 8 | design-taste-frontend, impeccable, brandkit, design-loop, web-design-guidelines, ux-skill, uupm-design-system, uupm-ui-ux-pro-max |
| MERGE-INTO | 13 | gpt-taste, high-end-visual-design, minimalist-ui, industrial-brutalist-ui, image-to-code, imagegen-frontend-web, imagegen-frontend-mobile, redesign-existing-projects, uupm-ui-styling, uupm-brand, uupm-banner-design, stitch-design-taste, stitch-loop |
| DROP | 3 | uupm-design, uupm-slides, stitch-craft (orchestrator; scripts salvaged) |

## How many of these are the same "taste" skill in different clothes?

**At least 14 of the 33 carry the same core taste manifesto**, and **7 are essentially *only* that manifesto**:

- Pure taste-in-different-clothes (7): gpt-taste, high-end-visual-design, minimalist-ui, industrial-brutalist-ui, frontend-design (the principled exception), stitch-design-taste, and the taste layer of design-taste-frontend. Swap the signature bans (no purple gradients / no cream+terracotta / no gradients at all / no soft shadows) and the signature moves (bento / double-bezel / flat bento / Swiss grid) and the skeletons are identical: archetype picker → typography rules → palette rules → component moves → motion rules → bans → pre-output checklist.
- Same manifesto embedded in a larger machine (7 more): atelier, impeccable, redesign-existing-projects, image-to-code, imagegen-frontend-web, imagegen-frontend-mobile, stitch-craft — plus data-flavored restatements in ux-skill and uupm-ui-ux-pro-max.

The tell: whole engines are duplicated verbatim (image-to-code and both imagegen skills share a "combinatorial variation engine"; stitch-craft Phase 0 literally imports gpt-taste's and stitch-design-taste's rules). The batch doesn't have 33 opinions — it has roughly **one anti-slop opinion, two real workflows (Atelier, Impeccable), three databases (tasteskill library, ux-skill manifests, pro-max CSVs), and a set of genuine tools** (logo scripts, shadcn pair, Stitch suites, scrollytelling CLI, baton loops). The unified system should keep the tools, pick one workflow, pick one database, and demote the manifesto to a single principles document (frontend-design + the best bans) referenced by everything else.

## What a single design workflow actually needs

Six stages, each with one artifact in and one artifact out — everything in this batch that matters serves one of these, and nothing needs a seventh:

1. **Brief** — short human-decision interview + stated assumptions (Atelier's brief; stitch-craft's brief.md scaffold; logo skill's discovery brief). Artifact: `brief.md`, including quantified levels (density/motion/boldness/strangeness) and the surface mode (Persuade/Operate/Read/Experience, from Impeccable).
2. **DESIGN.md** — one format only: Atelier's 11-part constitution, written semantically (stitch-design-taste's descriptive language + anti-patterns section), underpinned by uupm-design-system's three-layer tokens, bootstrapped for existing codebases by stitch-design's extract-design-md.
3. **Keyframe / reference** — per page/section images before code (imagegen checklists compressed into prompt recipes; logo concepts via logo-design-skill when identity is in scope). Artifact: keyframe PNGs the user approves — generation tool (Stitch via local-stitch/stitch-design, or image models) is a swappable backend, never a workflow dependency.
4. **Component discovery** — search before building (shadcn-component-discovery; design-system generator lookups from uupm-ui-ux-pro-max / ux-skill data). Artifact: a component plan naming what is reused vs built.
5. **Build** — a builder subagent implements keyframes in the project stack, in baton-sized units (design-loop's `.design/next-prompt.md` handoff), following the dealt/chosen direction (tasteskill's draw) and Emil's motion standards.
6. **Visual QA** — screenshot the real build and compare against keyframes (tasteskill's inspect/look-and-fix loop), deterministic linters where they exist (ux-skill anti-pattern linter, stitch-craft's verify_responsive.py, logo svg_audit), shadcn-component-review for component idioms, Impeccable's audit/harden for a11y/performance/edge cases, council review (Atelier) scaled to page importance — with Atelier's bounded-pass rule as the stopping condition.

## Mechanisms worth keeping (the short list)

1. **Artifact constitution chain** — brief.md → DESIGN.md → keyframes as versioned files every subagent reads/writes (Atelier + Impeccable's PRODUCT.md + doctor drift-check).
2. **Council review with bounded passes** — multi-persona/multi-lens review, dissent recorded, batched fixes, hard stop after two rounds (Atelier).
3. **Dealt direction + screenshot look-and-fix loop** — externalized art direction from a researched library, then real-browser inspection against screenshots (design-taste-frontend), the batch's only closed visual feedback loop with evals.
4. **Baton handoff file** — `.design/next-prompt.md` as the standard resumable delegation artifact for multi-page/multi-agent work (design-loop / stitch-loop).
5. **Executable verification & searchable data over prose** — logo skill's test scripts (16px/one-colour/shelf test), ux-skill's deterministic linter, pro-max's Master+Overrides design-system persistence, shadcn search-before-build: checks an orchestrator can gate on instead of trusting taste claims.

# Absorb report: anthropics/skills (target: frontend-design)

- Source: https://github.com/anthropics/skills/tree/main/skills/frontend-design · Commit: dbd4588f9e1033efb41dad4bef2f7947c8993d44 · Licence: Apache-2.0 (© Anthropic) — text and mechanisms may be adapted with credit
- Date: 2026-10-23 · Run by: orchestrator (single-skill scope targeting frontend-design)

## Licence ruling (decided before any adaptation)

The target unit carries an Apache-2.0 `LICENSE.txt`. Text and mechanisms may be adapted into the suite's conventions with appropriate credit. Upstream prose is adapted and rewritten into the suite's checkable rulebook and preview gates.

## Scope ruling

The invocation named the `skills/frontend-design` subdirectory of `anthropics/skills`. This run audits and absorbs that skill specifically. The remainder of the repository (17 other skill directories) was inventoried at survey depth below; absorbing any of them is a separate run requiring its own invocation.

## Inventory (target and survey)

| Unit | Purpose (theirs, one line) | Ships besides prose | Size |
|---|---|---|---|
| frontend-design (TARGET) | Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one | None — SKILL.md + LICENSE.txt | 71 lines |
| academy-guide | Interactive tutorial guidance | — | Niche / tutorial-specific |
| algorithmic-art | Algorithmic canvas art generation | code | Out of scope for dev/product workflow |
| brand-guidelines | Brand identity enforcement | — | Overlap: suite `design` (DESIGN.md) |
| canvas-design | HTML5 canvas visual design | code | Niche / canvas-specific |
| claude-api | Anthropic API integration patterns | code/docs | Harness/API-specific |
| discernment-nudge | Nudge to evaluate responses critically | — | Persona/behaviour; out of scope |
| doc-coauthoring | Document co-authoring patterns | — | Overlap: suite `spec`, `brief` |
| docx, pdf, pptx, xlsx | Document generation & editing skills | code/binaries | Source-available (not Apache); out of scope |
| internal-comms | Corporate communications drafts | — | Out of scope for dev/product suite |
| mcp-builder | Guide to building MCP servers | code | Tooling candidate (future) |
| skill-creator | Creating new agent skills | templates/scripts | Overlap: suite `gluttony`, `adapt` |
| slack-gif-creator | Animated GIF generation for Slack | scripts | Out of scope |
| theme-factory | Theme generation | code | Overlap: suite `design` token exports |
| web-artifacts-builder | Web app artifact creation | code | Overlap: suite `implement` |
| webapp-testing | Playwright testing for web applications | code/tests | Overlap: suite `verify`, playwright-cli |

Vetting: `skills/frontend-design` contains only `SKILL.md` and `LICENSE.txt`. It contains no scripts, no hooks, no network calls, and no executable code.

## Audit and verdicts

| Unit | Pros (mechanisms the suite lacks) | Cons / overlap ruling | Verdict |
|---|---|---|---|
| frontend-design | (1) Concrete calibration list of 5 AI design default clusters (cream+serif+terracotta #D97757; near-black+acid; broadsheet hairline; SaaS-card kit; template chrome with middle dots 'A · B · C', spaced em dashes 'WORD — fragment', and button '→'). (2) Two-pass default-ness review gate before code: draft token plan and ASCII layout, then self-review against brief "would I produce this for any similar prompt?" before writing code. (3) Chanel restraint law: spend boldness in one memorable moment, keep everything else quiet and disciplined. (4) Concise writing-in-design rules (active voice, user perspective, errors explain without apology, empty state as invitation). | Pure guidance prompt with no checkable artifacts, no verification step, and no tooling. As a standalone skill, it violates the suite's "one taste core" law and duplicates existing coverage in `skills/design`, `templates/design.md`, `taste-core.md`, and `copy.md`. | MERGE-INTO design — extract the 5 AI-tell calibrations, the two-pass uniqueness check into the preview block, and the Chanel restraint rule into `skills/design/SKILL.md`, `templates/design.md`, and `taste-core.md`. Upstream prose discarded; no standalone skill created. |

## Integration performed

Prepared as a staged diff on 2026-10-23, pending the human gate:
- `skills/design/SKILL.md`: reinforced preview block with the two-pass uniqueness check; added the Chanel restraint principle to the build discipline; added Apache-2.0 credit to Anthropic in the references/footer.
- `skills/design/references/taste-core.md`: added the 5 AI design default clusters under Structure and Chrome and Pre-ship slop gates (middle dots, spaced em-dash labels, button '→', cream+terracotta / acid-on-black defaults unless explicitly requested by brief).
- `templates/design.md`: added the 5 signature AI default traps as explicit bans in the design constitution template.
- `docs/ADAPTATIONS.md`: recorded entry A-007 at EXPOSED.
- `docs/SYNTHESIS.md`: added attribution credit for Anthropic `frontend-design`.

## Review

- Fidelity axis: PASS on mechanisms. The 5 specific calibration traps, the two-pass uniqueness check, and the Chanel single-boldness rule survive in substance as checkable rules and gates. Upstream prompt prose is discarded.
- Fit axis: PASS. No orphan skill, no second taste manifesto, no new un-triggered artifact. Merges cleanly into the existing design phase and `DESIGN.md` constitution chain.
- Human gate: approved on 2026-10-23

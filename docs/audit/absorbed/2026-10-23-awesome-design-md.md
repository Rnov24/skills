# Absorb report: VoltAgent/awesome-design-md

- Source: https://github.com/voltagent/awesome-design-md · Commit: 3b605329240ce735b510037cca322f1831fdd7f8 (2026-10-14) · Licence: MIT (© VoltAgent) — text may be adapted with credit; in the event, all absorbed material was rewritten in the suite's own words anyway
- Date: 2026-10-23 · Run by: Ronald (gluttony run 4; audit by four parallel family auditors plus orchestrator format checks)
- Verdict tally: ABSORB-NEW ×0 · ADAPT-EXISTING ×1 unit (cohere) · MERGE-INTO design ×14 units + 7 format mechanisms (several merges are family patterns carried by more than one unit) · REJECT ×69 units outright, plus the surviving units' token sets (every brand's tokens rejected, including the merged units')

Intake notes. Shallow clone at `.work/gluttony/awesome-design-md`. Vetting:
the repo contains no executable code at all — 169 markdown files, 2 GitHub
YAML configs (funding, an issue template), a licence, a gitignore. Nothing
to run, nothing reaching for credentials or the network. The README's
preview.html files are not in the repository (previews live on the
commercial getdesign.md site); each brand folder ships DESIGN.md plus a
README stub pointing there. One anomaly: `slack/` has no README stub, is
absent from the README collection list, and its frontmatter misspells the
brand ("Slacc-Inspired").

What this repo is: not a skill suite. It is 84 instances of one artifact —
DESIGN.md — extracted from real brand sites. The audit therefore ran on two
levels: the format (one shared unit) and the 84 brand contents (one unit
each). The format was the feast; the brands were almost entirely restyle.

## Inventory

| Unit family | Units | Size (DESIGN.md lines) | Ships besides prose |
|---|---|---|---|
| AI & LLM Platforms | 13 (claude, cohere, elevenlabs, jobright, minimax, mistral.ai, ollama, opencode.ai, replicate, runwayml, together.ai, voltagent, x.ai) | 7,127 | YAML frontmatter token registry (11 of 13) |
| Developer Tools | 7 (cursor, expo, lovable, raycast, superhuman, vercel, warp) | 3,740 | YAML frontmatter (6 of 7) |
| Backend, Database & DevOps | 9 (clickhouse, composio, hashicorp, mongodb, oracle, posthog, sanity, sentry, supabase) | 5,230 | YAML frontmatter (8 of 9) |
| Productivity & SaaS | 8 (cal, intercom, linear.app, mintlify, notion, resend, sap, zapier) | 5,070 | YAML frontmatter (8 of 8) |
| Design & Creative Tools | 6 (airtable, clay, figma, framer, miro, webflow) | 3,630 | YAML frontmatter (6 of 6) |
| Fintech & Crypto | 9 (binance, coinbase, kraken, mastercard, mercury, nerdwallet, revolut, stripe, wise) | 4,651 | YAML frontmatter (7 of 9) |
| E-commerce & Retail | 6 (airbnb, meta, mydealz, nike, shopify, starbucks) | 3,450 | YAML frontmatter (6 of 6) |
| Media & Consumer Tech | 16 (1win, aljazeera, apple, dji, hp, ibm, nvidia, oura, pinterest, playstation, spacex, spotify, theverge, uber, vodafone, wired) | 8,854 | YAML frontmatter (14 of 16) |
| Automotive | 7 (bmw, bmw-m, bugatti, ferrari, lamborghini, renault, tesla) | 3,195 | YAML frontmatter (5 of 7) |
| Retro Web | 2 (dell-1996, nintendo-2001) | 1,281 | YAML frontmatter (2 of 2) plus an auto-generated `ex-*` examples block |
| Unlisted | 1 (slack) | 482 | YAML frontmatter |
| **Total** | **84** | **46,710** | 74 Stitch-format files, 10 legacy-format files |

Two formats coexist. The Stitch format (74 files): YAML frontmatter with
`version, name, description, colors, typography, rounded, spacing,
components`, component values bound by `{colors.x}`-style references, then
body sections Overview / Colors / Typography / Layout / Elevation & Depth /
Shapes / Components / Do's and Don'ts, and in most files Responsive
Behavior (51), Iteration Guide (50), Known Gaps (43). The legacy format
(10 files: kraken, lamborghini, lovable, mastercard, runwayml, sanity,
spotify, starbucks, tesla, theverge): numbered sections 1–9 ending in an
Agent Prompt Guide, hex in prose, no token references.

Orchestrator's mechanical checks on the Stitch files: 7,923 token
references inside `components:` blocks, 0 unresolved among parseable files;
3 files have frontmatter that does not parse as YAML at all (elevenlabs,
raycast, supabase — an unquoted colon in the description), which is itself
evidence for the lint gate absorbed below. 24 files carry auto-derived
`ex-*` example surfaces, 13 of them with unresolved `TO_FILL` markers.

## Format audit and verdicts

| Mechanism | Evidence | Suite equivalent before | Verdict |
|---|---|---|---|
| Frontmatter token registry (`colors/typography/rounded/spacing` as structured maps) | 74/84 | Prose bullets in templates/design.md | MERGE-INTO templates/design.md — the registry becomes the single source; prose states roles and never restates values (upstream repeats hex in prose throughout; that duplication is rejected, see below) |
| `components:` token bindings (`backgroundColor: "{colors.accent}"`, typography/rounded/spacing refs) | 74/84 | Component rules as prose only | MERGE-INTO templates/design.md — bindings make orphaned and invented tokens mechanically checkable |
| Variant-as-separate-entry (`button-primary-disabled` as its own registry entry) | 57/84 | States implied in prose | MERGE-INTO templates/design.md — state coverage becomes enumerable |
| Lint gate (`npx @google/design.md lint DESIGN.md`: broken-ref, contrast-ratio, orphaned-tokens) | named in 34/84 | Exports section stated precedence, no validation step | MERGE-INTO templates/design.md (Exports) + docs/ARTIFACTS.md DESIGN.md gate |
| Known Gaps section (unobserved states, sampled values, out-of-scope surfaces) | 43/84 | None in the constitution (study artifacts have honesty fields; DESIGN.md did not) | MERGE-INTO templates/design.md — required when the system derives from a study or extraction |
| Note on Font Substitutes (licensed face → named open substitute + adjustment) | 69–73/84 | Font-pairing guidance, no per-project substitute record | MERGE-INTO templates/design.md (Tokens) |
| Responsive Behavior as a named section (breakpoint table, collapsing strategy, image reframing) | content in 84/84, top-level in 51 | Breakpoints mentioned inside Layout rules only | MERGE-INTO templates/design.md — new Responsive section |
| `version: alpha` key | 74/84, identical value in all | none | REJECT — a constant carries no information; the adapted template carries `version: "1"` as a real format version instead |
| Iteration Guide as a constitution section | 50/84 | process lives in skills | REJECT as a section — process does not belong in a constitution; its one load-bearing step (the lint) was extracted above |
| Agent Prompt Guide (legacy §9: quick colour reference + prose component prompts) | 10/84 | none | REJECT — prose prompts duplicate the token list in a form no reviewer can check; upstream itself superseded it. The legacy variant explicitly instructs feel-words over CSS values, against the suite's checkable-rule standard |
| `ex-*` kit-mirror example blocks (auto-derived generic surfaces re-skinned per brand) | 24/84, 13 with `TO_FILL` | none | REJECT — generated filler; a cart drawer for Dell 1996 proves volume, not token fitness |
| Hex values repeated in body prose beside every reference | pervasive in 74 | Exports: "this file wins" | REJECT — duplication defeats single-source; values live once, in the registry |
| `{component.x}` references in body prose | 40/84 singular vs 7/84 plural forms | none | REJECT — upstream is internally inconsistent, and prose refs duplicate the binding block; references live in the registry only |
| Motion and accessibility sections | 0/84 motion sections; a11y limited to touch targets in 9/84 | Motion rules + Accessibility floor | Already covered — the suite is ahead of upstream here; nothing to take |
| Provenance / attestation for studied sources | 0/84 (the retro files present invented responsive rules as system fact, unmarked) | study skill: attestation gate, safety record | Already covered — suite ahead; the retro files are the cautionary example for why Known Gaps was merged |

## Audit and verdicts — brand units

Every unit below is an instance of an artifact the suite already owns
(DESIGN.md via `design`/`study`). A unit earns a merge only for a checkable
mechanism the suite lacks; its token set is rejected in every case,
including merged units. "Restyle" means: competent brand tokens and prose,
no transferable mechanism.

| Unit | Mechanism found | Verdict |
|---|---|---|
| cohere | Gradient rule finer than the suite's blanket ban: gradients are media (hero imagery, posters, image bands), never UI fill | ADAPT-EXISTING taste-core.md — media-vs-fill distinction added to the gradient rule |
| cursor | Agent-activity state tokens: named semantic colours per process verb (thinking / search / read / edit / done), done distinct | MERGE-INTO style-directions.md — agent and process state token roles |
| binance | Directional colour reservation (green/red only for buy/sell direction) + canvas mode by surface intent (dark showcase, light transaction, same CTA token) | MERGE-INTO taste-core.md (reserved-hue contract) + taste-core.md light/dark rule (mode-by-intent clarification); also the strongest instance of the family reservation pattern (aljazeera live-red, starbucks Rewards gold, coinbase price cells) |
| clickhouse | Band-sequencing rule: never repeat the same surface mode in consecutive bands | MERGE-INTO style-directions.md — band alternation discipline (clay's card-colour sequencing is the same rule in colour form) |
| hashicorp | Per-product identity-token governance: a product's colour is scoped to its own sections and is drift anywhere else | MERGE-INTO style-directions.md — multi-product identity tokens (intercom's sub-brand reservation is a duplicate instance) |
| oracle | Tonal-ladder-as-structure: sections separated by ladder rung alone, uniform band rhythm, no cards/rules/shadows | MERGE-INTO style-directions.md — ladder-only sectioning as a named option |
| mintlify | Documentation component vocabulary the shelf lacks: property-row (code name + type badge + required badge + description) | MERGE-INTO components — new archetype X1 |
| sap | Two-storey persistent app-frame chrome for mega-catalogues | MERGE-INTO components — new archetype X2 |
| nerdwallet | Comparison-trust labelling: one award badge per set, pinned to the winner only, contrast tier engineered for saturated bands | MERGE-INTO components — new archetype X3 |
| airbnb | Segmented search pill (caption-over-value segments, hairline dividers, orb action) + the scrim as a named palette role | MERGE-INTO components — new archetype X4; scrim role into style-directions.md palette construction |
| meta | Composed PDP archetype: gallery rail + sticky purchase rail + variant picker as one unit | MERGE-INTO components — new archetype X5 (dji and starbucks repeat slices of it) |
| mydealz | Vote/heat pill: bidirectional community-temperature signal with a reserved hue pair | MERGE-INTO components — new archetype X6 |
| theverge | StoryStream feed archetype: rail line + mono timestamp + compact card, rhythm broken by accent tiles | MERGE-INTO components — new archetype X7, structure only; its palette is signature and stays behind |
| wise | Utility-as-hero: the hero is the product's core utility, operable (currency converter), not a headline about it | MERGE-INTO style-directions.md — seventh composition pattern (uber's request-form hero is a duplicate instance) |
| pinterest | Masonry discipline: preserve intrinsic aspect ratios, column-flow order, no uniform cropping | MERGE-INTO taste-core.md — masonry checkbox in Layout |
| claude | none (product-evidence rule already the imagery gate; editorial direction already a style-directions row) | REJECT — restyle |
| elevenlabs | none (restricted-use gradient orbs are a weaker duplicate of cohere) | REJECT — duplicate + restyle; frontmatter also fails YAML parsing |
| jobright | none | REJECT — token set + archetype instances |
| minimax | none (per-model gradient cards are token assignment, not a rule) | REJECT — restyle |
| mistral.ai | none (sunset stripe is a signature token) | REJECT — restyle |
| ollama | none (README-as-homepage is a macrostructure the suite already vendors) | REJECT — direction already expressible |
| opencode.ai | none (all-mono type contradicts the suite's font discipline) | REJECT — restyle against suite rules |
| replicate | none (status badges on model cards are component data) | REJECT — component instances, no mechanism |
| runwayml | none (legacy format; per-component prose prompts are the form the suite rejects) | REJECT — anti-pattern format + restyle |
| together.ai | none (band alternation is a macrostructure instance) | REJECT — restyle, incomplete format |
| voltagent | none (one accent on black restates the developer-tool row) | REJECT — restyle of an existing row; noted, not absorbed, despite being the source repo's own brand |
| x.ai | none | REJECT — restyle, incomplete format |
| expo | none | REJECT — restyle |
| lovable | none (opacity-derived greys are a weaker version of the suite's OKLCH neutral construction; legacy prose-prompt format) | REJECT — weaker duplicate |
| raycast | none (product-chrome-as-marketing already the imagery gate; category accents already data-colour rules) | REJECT — principle already owned; frontmatter also fails YAML parsing |
| superhuman | none (three-canvas rhythm is a macrostructure instance) | REJECT — restyle |
| vercel | none (its signature mesh gradient is affirmatively banned by taste-core as fill; as media it is now covered by the cohere distinction, which needed no Vercel tokens) | REJECT — restyle whose signature contradicts suite rules |
| warp | none (serif-italic accent already described by the 2+1 font rule) | REJECT — restyle |
| composio | none (terminal-grid hero is H8/F5 territory) | REJECT — restyle of an existing archetype |
| mongodb | none distinct from mintlify's docs slice | REJECT — duplicate + restyle |
| posthog | none (mascot marginalia is a commissioned brand asset) | REJECT — virtue is illustration + length (690 lines) |
| sanity | display-p3 accent tokens noted, but the file offers no gate for them; sole unit in its family with no frontmatter; −4.48px tracking violates taste-core's floor | REJECT — format non-conforming; p3 noted as future evidence only |
| sentry | none (sticker overlap is a signature decoration move) | REJECT — contradicts the anti-slop core |
| supabase | none | REJECT — clean restyle; frontmatter also fails YAML parsing |
| cal | card-semantics labelling is one project's convention, already implied by the imagery gate | REJECT — narrow convention |
| intercom | sub-brand accent reservation duplicates hashicorp's scoping | REJECT — duplicate instance |
| linear.app | none (4-step dark ladder and screenshot-as-protagonist already codified) | REJECT — best-written restyle in the set, still a restyle |
| notion | none (pastel property tints collide with the one-accent rule; 821 lines, longest in family) | REJECT — length as virtue |
| resend | none (editorial serif for a dev tool is a permitted direction departure, not a mechanism; four type lanes violate the suite cap) | REJECT — direction example |
| zapier | none | REJECT — warm-neutral restyle |
| airtable | pricing sub-system namespace + featured-by-tone are refinements a project writes in its own component rules | REJECT — no new artifact or gate |
| clay | card-colour sequencing duplicates clickhouse's alternation rule | REJECT — duplicate |
| figma | discrete weight whitelist is a token constraint, not a workflow mechanism | REJECT — a DESIGN.md line, not an absorption |
| framer | none (gradient spotlight cards are the canonical taste-core failure; −5.5px tracking breaches the floor) | REJECT — signature mechanism is one the suite bans |
| miro | none distinct from notion/mongodb duplicates | REJECT — duplicate + restyle (825 lines) |
| webflow | accent-as-full-fill-category is the airtable/clay signature-card rule a third time | REJECT — third instance, no new ground |
| coinbase | price cells duplicate binance's reservation, weaker; its own Known Gaps admits trading surfaces were never captured | REJECT — incomplete evidence + duplicate |
| kraken | none (spacing enumerated as raw px, against token discipline; 125 lines) | REJECT — unfinished stub |
| mastercard | none usable — the distinctive material is the interlocking-circles motif itself | REJECT — ⚠️ signature-copy flag: trademark motif; study rules bar carrying it over |
| mercury | mode flips by page, weaker than binance's by-intent rule | REJECT — duplicate mechanism |
| revolut | band polarity duplicates the family mechanism, less precisely | REJECT — duplicate + tokens |
| stripe | its one real rule (tnum on money cells) is already a taste-core checkbox | REJECT — ⚠️ signature-copy flag: gradient mesh is the brand signature and a taste-core ban as fill; composited faux-UI mockups collide with the chrome ban |
| 1win | odds-chip + betslip panel are genuinely absent from the suite | REJECT — a real mechanism with no home: a gambling vertical with no consumer, artifact, or gate in this suite; absorbing it would create exactly the orphan the suite forbids |
| aljazeera | live-red reservation is an instance of the binance family pattern | REJECT as a unit — its mechanism landed via the reserved-hue contract; newsroom tokens are restyle |
| apple | none (the source half the others imitate; already owned via photographic macrostructure + imagery gate) | REJECT — canonical, absorbed in principle long ago |
| dji | PDP slices duplicate meta's archetype | REJECT — duplicate |
| hp | none (chevron ornament has no semantic anchor) | REJECT — fails the decoration gate on arrival |
| ibm | none (a marketing extract of Carbon; its own gaps point at Carbon's docs as the real system) | REJECT — derivative extract; a project adopting Carbon cites Carbon under the locked-system rule |
| nvidia | none (corner-square ornament fails the decoration gate) | REJECT — tokens + banned ornament |
| oura | circular stat readout is the stat-led archetype in a ring | REJECT — restyle of an existing archetype |
| playstation | band chapters duplicate the family polarity mechanism | REJECT — duplicates on every axis |
| spacex | autoplay full-viewport hero video conflicts with hero-media discipline | REJECT — signature move is one the suite gates |
| spotify | stepped dark ladder restates style-directions' dark-palette construction | REJECT — well-executed restatement (legacy format) |
| starbucks | customisation cluster duplicates meta's PDP slice; Rewards-gold is the reservation pattern again | REJECT — duplicate mechanisms (legacy format) |
| nike | filter sidebar is standard PLP practice under ux-heuristics | REJECT — ⚠️ mild signature flag: burned-in uppercase Futura lockups are the brand treatment; principle (photo speaks, chrome silent) already owned |
| shopify | stacked-shadow depth trick contradicts "border or shadow, never both" | REJECT — signature technique loses to a stricter existing rule |
| bmw | none (near-duplicate of bmw-m with inverted surfaces) | REJECT — restyle of its sibling |
| bmw-m | none ("stripe never a CTA fill" is Bans material the suite already has) | REJECT — restyle |
| bugatti | type role-lock is expressible in existing Tokens + Component rules slots | REJECT — disciplined restyle; all faces licensed |
| ferrari | paired on-dark/on-light variants are the Variants section's job; file contradicts its own no-gradient claim | REJECT — restyle, internally inconsistent extraction |
| lamborghini | legacy prose format; palette contradicts its own gold-only rule (three extra accent tokens shipped) | REJECT — legacy restyle, self-violating |
| renault | scarcity cap is Tokens/Bans material; `link: #0000ee` enshrines a browser default its own prose disowns | REJECT — restyle with extraction noise promoted to system |
| tesla | 0.33s transition token already has a home in Motion rules | REJECT — legacy restyle |
| dell-1996 | brand-level variant explosion (7 ribbon cards differing only in fill); its Responsive section is an invented modern retrofit presented as fact | REJECT — period restyle; the invented sections are the cautionary case for Known Gaps |
| nintendo-2001 | per-page hero tints are Variants material; Responsive section is admittedly hypothetical | REJECT — restyle with speculative sections |
| slack | token scale tops out at 28px while its own prose specifies 64–96px section padding — the scale does not cover its own system | REJECT — weakest extraction quality in the repo; unlisted anomaly |
| uber | request-form hero duplicates wise's utility-led pattern, less precisely specified | REJECT — duplicate pattern, monochrome tokens |
| vodafone | colossal-headline campaign treatment is covered by the photographic macrostructure; display face is proprietary signature-adjacent material | REJECT — a campaign treatment, not a transferable system |
| wired | three-faces-three-roles contradicts taste-core's two-face ceiling; the file itself states the serif is the signature and must not be substituted | REJECT — untransferable by its own terms, and in conflict with an existing gate |

Signature-copy flags kept on record for any future study of these sources:
mastercard (motif), stripe (gradient mesh), theverge (palette — structure
absorbed, palette not), nike (typographic treatment), wired (its own file
states the serif is the signature and must not be substituted; also three
faces against the suite's two-face ceiling — REJECT, untransferable by its
own terms).

## Integration performed

First staged as a full digestion diff (registry template, taste-core and
style-directions rule merges, X1–X7 component annex). At the human gate
the owner ruled instead: "ambil aja sebagai referensi design md" — take
it as a DESIGN.md reference. The landing was revised to that ruling
before any commit; the rule merges and the annex were withdrawn, and the
audit above is their record for future adapt cycles. What landed, as
v1.10.0:

- `skills/design/references/brand-systems/` — all 84 upstream DESIGN.md
  files vendored verbatim, plus `INDEX.md` (load discipline: index
  first, at most one or two files; provenance; quality caveats — the 3
  broken-YAML files, the 10 legacy files, `ex-*` filler, retro
  speculation, signature cautions) and `UPSTREAM-LICENSE.txt` (MIT).
- `templates/design.md` — adopts the corpus format: frontmatter token
  registry (colors/typography/rounded/spacing/components with
  `{token.ref}` bindings, state variants as separate entries), Tokens
  prose reduced to roles + font substitutes, new Responsive and Known
  Gaps sections, lint validation in Exports. The registry is the single
  source; prose never restates values. Existing projects' DESIGN.md
  files are not migrated. Kept from the original staging because the
  reference shelf and the suite's own constitutions must speak the same
  format to be usable side by side.
- `skills/design/SKILL.md` — constitution step 2 states the registry,
  lint, and known-gaps rules; references list gains the brand-systems
  shelf with its load discipline and the study-attestation boundary.
- `docs/ARTIFACTS.md` — DESIGN.md gate gains the parse/resolve/lint
  checks and the Known Gaps requirement for derived systems.
- `docs/ADAPTATIONS.md` — A-005 filed at EXPOSED, recording the ruling.
- `docs/SYNTHESIS.md` — v1.10.0 note with credit.
- Withdrawn before commit (recorded in this report, not in force):
  taste-core additions (reserved-hue contract, media-vs-fill gradient
  distinction, mode-by-intent, masonry), style-directions additions
  (scrim role, agent-state tokens, multi-product scoping, utility-led
  pattern, band disciplines), and component archetypes X1–X7.

Validation run on the final diff: all 21 SKILL.md frontmatters valid
(name matches directory, description present); every `templates/`
reference in the skills resolves; the new template's frontmatter parses
as YAML and every component binding reference in it resolves; the shelf
holds exactly 84 DESIGN.md files matching the upstream clone at the
recorded commit (byte-compared at vendoring); skills index regenerated
with no changes (no skill frontmatter changed).

## Review

- Fidelity axis: PASS. Each merged mechanism was re-checked against its
  upstream instance — the registry schema and reference syntax are the
  upstream format's load-bearing parts (7,923 references, zero unresolved
  upstream is the discipline being imported, not its prose); the one-line
  rules (reservation, alternation, scoping) are stated upstream in brand
  vocabulary and are rewritten here as brand-free checkable rules;
  archetypes X1–X7 keep the source composition and drop the source tokens,
  with X7's palette explicitly refused.
- Fit axis: PASS with one recorded tension. Two auditors disagreed on the
  registry: one recommended adopting the frontmatter wholesale, one
  warned it would create a second source of truth beside the template's
  prose Tokens. The landed design resolves it by demoting the prose:
  values live once, in the registry; prose carries roles and rules only,
  and the template says so in its own header comment. No new skill, no
  new rule in force: the landing adds reference data behind an index, a
  template format, and a gate check — the smallest change consistent
  with the owner's ruling.
- Human gate: ruled by the owner 2026-10-23 — taken as a DESIGN.md
  reference shelf, not digested (see Integration performed). Released as
  v1.10.0 under that ruling. Promotion of A-005 from EXPOSED requires a
  proving run: a real project's DESIGN.md drafted with the shelf
  consulted, written in the new format, and linted clean.

# Style directions

This file is the condensed direction reference for the design phase: how
to pick a visual direction from the product and its personas, how to build
a palette that survives contact with real screens, which font pairings are
proven for which character, and which motion patterns exist with their
timing budgets. Load it when a new direction is being chosen or when
DESIGN.md tokens are first written. It is guidance for the decision, not a
catalogue; the catalogue lives upstream and the closing note says when to
go there.

## Choosing a direction

A direction is three decisions that must agree: composition traits,
palette character, and type character. Pick them from the product type and
the persona's situation, never from what is fashionable this quarter. The
table gives starting points; DESIGN.md records what was actually chosen
and the reason, and a deliberate departure from the table with a written
reason beats a faithful row with none.

| Product type | Direction traits | Palette character | Type character |
|---|---|---|---|
| General SaaS / B2B tool | Restrained, grid-true, density earned by the task | Trust primary (blue family), neutral surfaces, one contrasting action accent | Neutral grotesque, single family, many weights |
| Micro SaaS / indie product | Flat, direct, product visible in the first screen | Vibrant primary on generous white space | Friendly geometric sans, confident display weight |
| E-commerce | Hierarchy that sells: product first, price and action unmissable | Brand primary, success green kept distinct from the accent | Clean sans; display only in campaign heroes |
| Luxury e-commerce / premium brand | Sparse, slow, material; whitespace as a price signal | Near-black neutrals, one metallic or deep jewel accent | High-contrast serif display, quiet sans text |
| Financial / analytics dashboard | Data-dense, calm under load, dark surfaces where screens run all day | Dark ground, restrained cool range, red/green reserved strictly for movement | Tabular figures, compact grotesque, mono for raw values |
| Healthcare | Calm, legible, forgiving; accessibility is the aesthetic | Soft cyan/blue family, health green as secondary, nothing alarming except alarms | Humanist sans, large default sizes |
| Education | Warm, structured play; progress always visible | Playful but limited set (three hues, not a rainbow) | Rounded or friendly sans, generous line-height |
| Creative agency / portfolio | The work is the layout; editorial grid, motion as signature | Bold primaries or strict monochrome plus one accent | Statement display face, deliberately chosen |
| Government / public service | Accessible and ethical first; decoration is a liability | Professional blue, very high contrast, no tricks | Plain grotesque, maximum legibility |
| Developer tool | Precision as beauty; density respected, keyboard-first | Dark ground, syntax-aware accent set | Mono for code and data, technical sans for UI |

## Palette construction

A palette is a set of roles before it is a set of colours. Build it in this
order and stop as soon as every role is filled.

1. **Roles first.** Surface, raised surface, ink, muted ink, border,
   primary, on-primary, accent, on-accent, danger, on-danger, and the focus
   ring. A colour with no role does not enter the system.
2. **Ratios.** Roughly 60% neutral surfaces, 30% secondary tones (muted
   surfaces, borders, secondary text), 10% accent and primary action. When
   everything is saturated, nothing is; a screen that reads as mostly
   accent has failed its own hierarchy.
3. **One accent.** The accent means action or selection everywhere. Danger
   is its own role and never borrows the accent's hue.
4. **Contrast is computed per pair.** Every text role is checked against
   every surface it can sit on (4.5:1 body, 3:1 large), including the
   accent button's label against its fill. A palette that only works on
   its hero surface is unfinished.
5. **Dark surfaces.** Build dark as its own palette, not an inversion:
   grounds step up through two or three near-black levels rather than one
   black, text drops to an off-white (pure white on pure black vibrates),
   accents are lightened a step to hold contrast, and elevation reads
   through lighter surfaces more than through shadows, which disappear on
   dark grounds.
6. **Data colours.** Chart palettes are a separate, smaller system:
   categories distinguishable by a colour-blind reader (hue plus lightness
   steps, never red/green alone), and a sequential scale for magnitude.
   Brand colours do not automatically become chart colours.

## Page composition patterns

For marketing and landing surfaces, composition follows a small set of
proven orders. Pick by the product's proof situation, not by taste: a
product with users to quote argues differently from one with only a demo
to show. Whichever pattern is chosen, the primary call to action appears
in the first screen and again at the end, and its label passes the same
4.5:1 check against its fill as any other text.

| Pattern | Section order | Fits when |
|---|---|---|
| Hero + features + CTA | Headline and image, value proposition, 3–5 features, closing CTA | The default for SaaS and tools with a clear feature story |
| Hero + social proof + CTA | Headline, problem, solution, verified testimonials with name and role, CTA | Trust is the bottleneck; real quotes exist and may be used |
| Demo-led | Headline, interactive demo or product video at the centre, per-feature breakdown, CTA | The product explains itself better in motion than in words; a static, captioned fallback is mandatory |
| Pricing-led | Headline, plan comparison, feature table, FAQ, CTA | The buyer's first question is price; the recommended plan is marked honestly, with real savings shown |
| Minimal single column | Headline, short description, at most three benefit bullets, one large CTA | One action matters and everything else is distraction; micro products and waitlists |
| Three-step funnel | Problem, solution, action, each with a small step CTA | Onboarding-shaped offers where progressive disclosure carries the argument |

Two failure shapes recur across all six. A hero whose media is decoration
rather than evidence (a video that shows nothing the words do not, an
image no persona recognises) wastes the strongest position on the page.
And any pattern collapses when the sections between hero and closing CTA
stop adding reasons and start adding length; each section must earn its
place with a new argument, a new proof, or a removed objection.

## A worked palette skeleton

The role order above, applied to a general SaaS product, produces a
skeleton like this before any brand colour is debated. The hues are
illustrative; the structure (every role filled, muted tones derived from
the surface family rather than borrowed greys, the accent kept out of the
neutrals' way) is the part worth copying.

| Role | Light ground | Dark ground |
|---|---|---|
| Surface | near-white, faintly warm or cool to match the primary | near-black step 1 |
| Raised surface | pure white or one step up | near-black step 2 (lighter, not shadowed) |
| Ink | near-black tinted toward the primary | off-white, never pure white |
| Muted ink | the ink mixed 60% toward the surface | the ink mixed 55% toward the ground |
| Border | the ink at 10–14% over the surface | the ink at 14–18% over the ground |
| Primary | the brand hue at full strength | the brand hue lightened one step |
| Accent | one contrasting hue, action only | same accent, contrast re-measured |
| Danger | a red that shares the palette's temperature | the same red, lightened to hold 4.5:1 |

## Font pairing

Pairing rules come before pairings. The display face carries the product's
character and appears at large sizes only; the text face carries the
reading and must disappear. Pair on contrast of kind (serif against sans,
geometric against humanist) with agreement of proportion (similar x-height
ambitions, compatible weights). One family in many weights beats two
families that fight, and a pairing is not done until real product copy (the
longest heading, the ugliest data label, an Indonesian and English string
side by side where the product is bilingual) has been set in it.

| Character | Display / heading | Text / UI | Notes |
|---|---|---|---|
| Editorial | High-contrast serif (Playfair class) | Clean sans (Inter class) | Serif speaks at display sizes; keep it out of UI chrome |
| Editorial, bookish | Text serif (Libre Baskerville class) | Same serif family | All-serif works for reading products, fails for dashboards |
| Technical | Grotesque with character (Space Grotesk class) | Neutral sans (DM Sans class) | Display face has quirks; body face must have none |
| Developer | Mono (JetBrains Mono class) for code and data | Technical sans (IBM Plex Sans class) | Mono is scoped to code/data, per taste-core.md |
| Friendly SaaS | Geometric sans, semibold (Poppins class) | Humanist sans (Open Sans class) | Warm without going rounded; safe for broad audiences |
| Neutral system | Single grotesque (Inter class) | Same family | The dashboard default; hierarchy comes from weight and size |
| Luxury | Didone or elegant serif (Playfair, Abril class) | Light sans, wide tracking on labels only | Display face at hero sizes only; small serif display is illegible |
| Playful | Rounded display (Fredoka class) | Rounded text sans (Nunito class) | Both faces rounded reads young; use where the persona is, not where it is not |

## Motion patterns

Motion is budgeted like colour: a pattern is chosen for a purpose, given a
duration range, and anything outside the table needs a written reason in
DESIGN.md. All patterns animate transform and opacity (plus the richer
properties taste-core.md allows when they stay smooth), never layout
properties, and all resolve to their final state under reduced motion.

| Purpose | Pattern | Duration |
|---|---|---|
| Hover / press feedback | Small lift (≤2px) or colour settle, ease-out | 150–200ms |
| Card or tile hover | Lift 4px with soft shadow growth, ease-out | 200–300ms |
| Scroll reveal, subtle | Fade with 8–16px rise, ease-out | 300–400ms |
| Section reveal with stagger | Children rise 24px, stagger ≤0.08s, capped near 8 items | 400–600ms |
| Page transition, quiet | Crossfade, exit faster than entrance | 200–300ms |
| Page transition, spatial | Overlay wipe or shared-element move, ease-in-out | 400–800ms |
| Parallax | Background layers at 5–15% travel, scrubbed to scroll | tied to scroll |
| Skeleton loading | Single shimmer sweep, one loop per group, killed on mount | 1200–1600ms loop |
| Progress and spinners | Linear, constant rate; linear easing is correct here | 800–1200ms loop |
| Carousel rotation | No default rotation; if used, pauses on hover, focus, and off-screen | user-controlled |

Two disciplines apply to every row. Feedback never waits for animation:
navigation and state changes are capped so the interface answers within
roughly 250ms even when an exit animation is still finishing. And no
pattern ships without its cleanup (listeners removed, looping tweens
killed on unmount, off-screen animation paused), because leaked motion is
a defect that only appears in long sessions.

## Sources and the upstream databases

This file distils the design data carried by the ui-ux-pro-max skill
(product-type recommendations, colour, typography, UX-guideline, and
motion datasets) and the craft judgement of the impeccable skill family.
The full searchable upstream databases (dozens of styles, nearly two
hundred product palettes, seventy-plus font pairings, the complete UX
guideline set, icon and chart data) remain in that skill's data files.
Stay in this file for direction decisions and DESIGN.md tokens. Go
upstream when a project needs a specific palette, pairing, or style
profile beyond these tables, when a niche product type is missing here,
or when a review finding must be checked against the full guideline text
rather than its condensed form.

# Taste core

This is the suite's single anti-slop rulebook. Load it when writing or
amending DESIGN.md, when producing keyframes, and when a review needs the
craft axis judged against something written down instead of someone's mood.
Every rule here is a check: a reviewer looking at the rendered screen can
say whether it holds. Where a project's DESIGN.md consciously overrides a
rule, the override is written in DESIGN.md and the rule is judged there;
an unwritten exception is a violation.

## How to read these rules

A rule names the failure it prevents. Most failures below are not ugliness;
they are the defaults a model or a rushed human reaches for when no decision
was made. The test is never "could this look fine somewhere" but "was this
chosen for this product, and can the choice be pointed at".

## Typography

- [ ] Every screen uses at most two typefaces: one voice for display and
  headings, one for text and UI. A third face appears only for code, data,
  or measurement, where monospace is a tool rather than a costume.
- [ ] The display face was sourced for this project's character. A platform
  default (the system sans, Arial, Impact-class faces) doing display duty
  on a branded surface fails.
- [ ] Type sizes come from a named scale in DESIGN.md. No size exists on
  screen that is not in the scale, and adjacent steps differ enough to read
  as different ranks, not as accidents.
- [ ] Body text measures 65–75 characters per line at reading sizes.
  Full-viewport-width paragraphs fail.
- [ ] Body text is at least 16px on web surfaces, line-height is unitless
  and at least 1.4, and text never sits below 12px for content a user must
  read.
- [ ] Headings balance their lines and never overflow their container at
  any supported breakpoint. One-word orphan lines in display headings fail.
- [ ] Letter tracking never goes tighter than -0.04em. Display type usually
  reads better between -0.02em and -0.03em; anything tighter is a defect,
  not a style.
- [ ] Emphasis is carried by weight, size, or position. Gradient-filled
  text fails. All-caps is reserved for short labels and display faces built
  for it, never for body copy or long headings.
- [ ] Numbers in tables and dashboards are tabular. Columns of figures that
  jitter because digits have different widths fail.

## Colour

- [ ] Every colour on screen resolves to a named token with a role
  (surface, ink, muted, accent, danger, and their on-colours). A raw hex in
  a component that no token explains fails.
- [ ] Body and placeholder text reach 4.5:1 against their background;
  large text reaches 3:1. This is measured, not eyeballed.
- [ ] Secondary text on a coloured surface is tinted from that surface's
  hue or from the foreground. Neutral grey text dropped onto a coloured
  background fails; it reads as dirt, not hierarchy.
- [ ] The palette has one accent that means something (action, selection,
  or state). A second saturated colour fighting for the same job fails.
- [ ] Colour is never the only carrier of meaning. Status, errors, and
  chart categories also differ by icon, label, position, or pattern.
- [ ] Light or dark is chosen from the use scene (who, where, ambient
  light), written in DESIGN.md, and applied whole. A dark theme that is a
  light theme with inverted backgrounds fails on its own contrast checks.
- [ ] Decorative gradients are absent unless the direction in DESIGN.md
  names the gradient as part of the world. The default purple-to-blue
  linear gradient on heroes, buttons, or text is the canonical failure:
  it is the colour scheme of no decision having been taken.

## Layout

- [ ] The page has a composition before it has components: a grid or an
  intentional asymmetry that a reviewer can describe in one sentence.
  Content poured into equal columns until it stops fails.
- [ ] A grid of same-size cards (icon, heading, paragraph, repeated) is
  never the page structure. Cards group genuinely parallel items; nested
  cards always fail.
- [ ] The hero-metric scaffold (one giant number, a small label, a row of
  supporting stats, an accent colour) appears only when the product's
  actual job is that metric. As a generic landing shape it fails.
- [ ] Spacing comes from the named scale. Related items sit closer than
  unrelated ones, and the space above a heading exceeds the space below
  it, so the heading binds to what follows.
- [ ] Elevation is declared once per element: a border or a shadow, never
  both. A 1px border under a wide soft shadow is the ghost card and fails.
- [ ] Shadows carry an offset and a soft blur. A zero-offset coloured halo
  is not depth; a hard offset shadow (the 4px 4px 0 block) appears only in
  a world that is deliberately neobrutalist.
- [ ] Card radii stay in the 12–16px band unless DESIGN.md says otherwise;
  pill shapes are for small controls, not containers.
- [ ] Section numbers (01 / 02 / 03) appear only when the sequence itself
  carries information. As decoration they fail.
- [ ] There is no kicker or eyebrow label above a heading. The heading
  carries its own weight; if it cannot, rewrite the heading.

## Components

- [ ] Every interactive element exists in all its states on the judged
  screen or in the component's own review: default, hover, focus,
  active, disabled, loading, and where relevant error and empty.
- [ ] Every interactive element on a judged screen does something real
  when used, or is removed, or carries a visible coming-soon label.
  Dead buttons, dead links, and navigation entries that lead nowhere
  fail — a control that performs nothing teaches the user that every
  control might perform nothing.
- [ ] A modal is used only for a task that needs interruption or protected
  focus. A modal holding ordinary content that could live on the page
  fails.
- [ ] Icons come from one library or one authored set, in one stroke and
  weight. Unicode glyphs and emoji standing in for icons fail.
- [ ] Sparklines, progress rings, and soft-shadowed rounded rectangles
  never stand in for content. Decoration that pretends to be data fails.
- [ ] Glass and blur are effects with a job (separating a layer the user
  must read through), never a surface treatment applied because it was
  available.
- [ ] A coloured side border above 1px on cards, list items, callouts, or
  alerts fails. It is the most reliable single tell of assembled,
  un-designed UI.
- [ ] Controls name their action in the product's own words. "Submit",
  "OK", and "Click here" fail where the action has a name.

## Motion

Governed in detail by the motion table in style-directions.md; the taste
rules are these.

- [ ] Each view has at most one authored motion moment. Scattered effects,
  and the identical entrance animation repeated on every section, fail.
- [ ] Motion explains a state change (where something came from, where it
  went, what is now true) or it is removed. Motion that only decorates
  fails.
- [ ] Entrances ease out exponentially from an already-visible default
  state. Content that is invisible until an animation fires fails, because
  it breaks without the animation.
- [ ] Continuous animation is reserved for loading indication. Decorative
  infinite loops (bouncing icons, pulsing badges seeking attention) fail.
- [ ] Under prefers-reduced-motion, every animation resolves immediately
  to its final, readable state. A global 0.01ms kill that also destroys
  state feedback fails in the other direction.

## Imagery

- [ ] Imagery is real photography, real product shots, or honest geometry.
  SVG imitating a picture (sketch-style scenes, doodle figures, grain
  filters standing in for texture) fails. Crisp vector shapes, diagrams,
  and animated linework are geometry and pass.
- [ ] A subject's edge is never faked with a circle, polygon, or radial
  mask approximating its contour. Either derive the cut-out from the actual
  image or present the image whole.
- [ ] Backgrounds are surfaces. Texture comes from the subject's world (a
  real canvas, map, blueprint, or measuring surface). Repeating gradient
  stripes and two-axis grid overlays over generic content fail.
- [ ] Placeholder content never appears in a judged artifact: no lorem
  ipsum, no grey-box images, no invented statistics presented as real.
  Illustrative values are labelled illustrative.
- [ ] The undrawn surfaces still carry the design: text selection colour,
  caret, scrollbars, focus rings, and link underlines are themed from the
  palette. Browser defaults left untouched on a branded page fail.

## Pre-ship slop gates

The sections above state the craft rules. This section is the mechanical
sweep that runs after them, before any design output ships: checks a
reviewer can settle from the code and the rendered page without arguing
taste. Several are stricter restatements of failures named upstream in
Hallmark's slop test; where a rule above already covers a failure, the
gate is not repeated here. Run the six-axis self-critique first (the
review rubric carries it): any axis under 3 sends the output back for a
revision pass before the gate sweep begins.

### Motion mechanics

- [ ] No `transition-all` or `transition: all` anywhere; every transition
  names its properties.
- [ ] No uniform hover scale (`hover:scale-105` and kin) applied across
  unrelated elements, and no element carries more than one hover effect
  at a time (translate, scale, shadow, colour, rotate — pick one).
- [ ] No animation runs on layout properties (`width`, `height`, `top`,
  `left`, `margin`, `padding`); movement uses transform, opacity, or a
  `grid-template-rows` fraction.
- [ ] The focus ring never transitions into existence. It appears
  instantly, in full, the moment focus lands.
- [ ] No celebratory success toast for an action whose effect the user
  can already see. Toasts are for failures and invisible effects.
- [ ] Tooltip timing separates intent: hover delay 800–1000ms, focus
  delay 0ms. Equal delays fail.
- [ ] Auto-rotating content pauses on hover and on focus, without
  exception.

### Colour mechanics

- [ ] No neutral is zero-chroma (`oklch(... 0 ...)`). Neutrals are tinted
  toward the anchor hue at 0.005 chroma or more. A direction whose
  DESIGN.md declares a strict monochrome system is the one exception.
- [ ] The accent covers at most ~5% of any single viewport by area.
  A declared atmospheric direction may run accent-tinted blooms to ~20%.
- [ ] No pure `#000` or `#fff` serves as a base surface. A modern-minimal
  direction may declare a pure-white paper explicitly in DESIGN.md.
- [ ] Contrast is computed per rendered pair, not assumed: where the
  OKLCH lightness gap between text and background is under 50 points,
  the pair is flagged and confirmed with a full APCA or WCAG
  calculation before shipping. `scripts/contrast-check.py` computes a
  WCAG pair from two hex values; verdicts read the unrounded ratio.
- [ ] Every accent fill that carries text has its paired on-accent token
  defined and applied. Text within ~5 lightness points and ~0.05 chroma
  of its own fill fails outright — that is the black-on-black bug.

### Layout safety

- [ ] `overflow-x: clip` is set on both `html` and `body` — `clip`, not
  `hidden`, because `clip` preserves sticky and fixed descendants.
- [ ] Image-bearing grid tracks use `minmax(0, 1fr)`, never a bare `1fr`;
  a bare track sizes to the image's intrinsic width and pushes the page
  past the viewport.
- [ ] Display headings carry `overflow-wrap: anywhere` and `min-width: 0`,
  so a long compound word wraps inside the word instead of off screen.
- [ ] All-caps display type keeps `line-height` at 1.0 or above
  (1.02–1.08 reads best); below 1.0 the cap-tops of one line collide
  with the baseline of the line above when the heading wraps.
- [ ] Any rule that sets a dark background sets the text colour in the
  same rule. A flipped surface whose children inherit the old ink fails.
- [ ] A decorative band on text (highlighter, underline, stroke) is
  positioned on purpose: a highlighter sits behind the x-height, an
  underline is 1–2px and offset 1–2px from the baseline, never a 5px bar.
- [ ] Flex bars mixing elements of different intrinsic heights (nav,
  toolbar, CTA row) declare `align-items: center` and `line-height: 1`
  on the sized items; inherited stretch makes siblings uneven.
- [ ] Only one element sticks at `top: 0`. A second sticky element
  offsets by the banner-height token and carries a lower z-index than
  the page nav, or the two collide on scroll.
- [ ] Decorative SVG, canvas, and CSS art carry `aria-hidden="true"` or
  an accessible name. Unlabelled decoration is an accessibility finding.
- [ ] The hero fits the fold: bottom padding is at least 1.3× the top
  padding, and at 1280×800 the eyebrow, headline, lede, and primary CTA
  are all visible without scrolling.

### Structure and chrome

- [ ] The eyebrow-and-heading wrapper resolves to a single column,
  always. A label sitting in a side column beside its heading (the
  tag-left, header-right head) is banned at every width, including when
  a reference build being matched ships it; the rules win over parity.
- [ ] The nav is a routed pick, not the default bar (wordmark left, four
  or five inline links, button right, hairline under, full width). The
  default bar ships only when the page genuinely has two destinations.
- [ ] The footer is a routed pick, not the default index (four link
  columns, social-icon row, small copyright line). The default index is
  reserved for a genuine docs root or hub.
- [ ] No decoration without a semantic anchor: every ornament in the
  hero names something (an edition, a year, a command the user would
  type, a state that responds to interaction). A floating cursor, a
  stray numeral, a chip with no rationale fails.
- [ ] No re-drawn UI chrome: no hand-built browser bars, phone frames,
  code-window frames, or IDE chrome in HTML, CSS, or SVG. Show a real
  screenshot in a figure, or let the content stand without a frame.
- [ ] The same component archetype never repeats in a project with the
  same variation-knob values. A repeat records at least one knob delta.
- [ ] Hero media discipline holds: no sound-on autoplay, a poster on
  every hero video, no lazy loading on the largest-contentful element,
  and no Lottie where hand-built SVG or CSS reaches the same motion.

### Type and token discipline

- [ ] Italic display type (headings, wordmarks, stat figures, an italic
  emphasis word inside an upright headline) is absent by default. The
  one exception is a direction whose genre is editorial and whose
  DESIGN.md explicitly chooses italic display as the project's voice;
  there it is a recorded decision, not a drift. Body-copy emphasis in
  running paragraphs is always allowed.
- [ ] An outlier face (the third family, where one exists) appears in at
  most two slots on the page — wordmark plus hero stat is the canonical
  pair. A third slot means the outlier has become a body face; collapse
  it back.
- [ ] No colour or font value appears in a component that does not come
  from the token block. A value the design needs is lifted into the
  tokens as a named variable first, then referenced; inline values are
  mid-render improvisation and fail.
- [ ] Placeholder names and product clichés (Jane Doe, John Smith, Acme,
  Nexus, Seamless, Unleash) appear nowhere in judged output; use names
  plausible for the product's actual audience.

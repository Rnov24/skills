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

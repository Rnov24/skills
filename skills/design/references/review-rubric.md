# Design review rubric

This rubric governs the council review in the design skill. Load it when a
keyframe, a built screen, or a DESIGN.md amendment is being reviewed. Each
council lens works from one axis below, checks it against the reference
file named for that axis, and records findings with the severity
vocabulary at the end of this file. Dissent between axes is recorded, not
averaged; the deterministic checks at the end run first, because a screen
that fails measurement does not earn a taste discussion.

## Axis 1: Product fit

Checked against the PRD, PERSONAS.md, and USERFLOW.md.

- The screen serves the story and acceptance criteria it claims; nothing
  on it exists for a persona or goal the product does not have.
- The primary action of the flow is the visually primary element; the
  thing the persona came to do is findable within seconds.
- Every state the flow names (empty, loading, error, success) is present
  in the design, not promised for later.
- Copy is the product's own language; controls name their actions, errors
  name the problem and the recovery.

## Axis 2: Typography and layout

Checked against taste-core.md (Typography, Layout).

- The composition can be described in one sentence and the grid or
  asymmetry is intentional, with no card grid substituting for it.
- Type sizes all come from the DESIGN.md scale, body measure and sizes
  pass, headings neither overflow nor orphan at any breakpoint.
- Spacing follows the scale with grouping that matches meaning, and
  elevation is declared once per element.

## Axis 3: Colour and tokens

Checked against taste-core.md (Colour) and style-directions.md (Palette
construction).

- Every colour resolves to a named token with a role; the accent means one
  thing; danger is distinct; data colours follow their own rules.
- Contrast ratios pass by measurement on every text/surface pair actually
  rendered, including over imagery and in the dark palette if one exists.
- The direction (traits, palette character, type character) matches the
  product-type decision recorded in DESIGN.md, or the departure is written
  there with its reason.

## Axis 4: Interaction and states

Checked against ux-heuristics.md (Forms, Feedback, Lists, Touch).

- Every interactive element shows all its states; every asynchronous
  action feeds back; every empty and error state offers the next action.
- Forms follow the label, error-placement, and validation-timing rules;
  no task depends on hover; gestures never fight the platform.
- The flow can be completed by keyboard alone, in visual order.

## Axis 5: Accessibility

Checked against ux-heuristics.md (Accessibility floor) and taste-core.md.

- Focus is visible everywhere it can land and never obscured by sticky
  elements; heading structure and landmarks are sound.
- Meaning is never carried by colour alone; meaningful images have alt
  text; icon-only controls have accessible names.
- Reduced motion resolves every animation to a readable final state, and
  the layout survives 200% text scaling and 400% zoom without loss.

## Axis 6: Craft and anti-slop

Checked against taste-core.md as a whole.

- None of the signature defaults appear unearned: no default gradient, no
  kicker above a heading, no ghost cards, no side-border accents, no emoji
  icons, no sketch-SVG imitation imagery, no lorem ipsum or invented
  statistics in a judged artifact.
- The undrawn surfaces (selection, caret, scrollbars, focus rings) carry
  the palette.
- The specificity test: the composition could not be lifted onto an
  unrelated product unchanged. If it could, the design has not yet become
  this product's design, whatever its polish.

## Severity vocabulary

Findings use the suite's scale, and the scale decides what happens next.

- **Critical** blocks acceptance: a flow cannot be completed, a contrast
  or target-size floor fails, content is lost at a supported size, or a
  judged artifact ships placeholder content.
- **Required** must be fixed before acceptance but does not block use: a
  missing state, an untokenised colour, a rule in DESIGN.md broken in one
  place.
- **Nit** is a real but cosmetic deviation: a spacing step off scale, an
  orphan word in a heading, a shadow softer than the system.
- **Optional** is a defensible improvement the author may decline with a
  sentence of reasoning recorded.
- **FYI** is an observation with no action requested, recorded so the next
  review does not rediscover it.

A review with Critical findings open cannot pass, whatever the other axes
say. Two rounds maximum, per the design skill; after round two, unresolved
Required findings and any axis disagreement go to the human with each
position stated in a paragraph.

## Deterministic checks

Run these before any axis discussion. Each is verifiable by screenshot or
measurement, and its result is a fact in the review record, not an
opinion.

- [ ] Screenshots of the judged screens at the smallest and largest
  supported widths, plus the keyframe they are judged against.
- [ ] Contrast ratios measured for every text/surface pair on those
  screenshots (tool output recorded, not estimated).
- [ ] No horizontal scrollbar and no clipped or overflowing text at any
  judged width; headings checked line by line.
- [ ] Touch targets measured: smallest interactive element meets the
  ux-heuristics.md minimums with spacing intact.
- [ ] Every colour and type size on screen traced to a DESIGN.md token or
  scale step (computed styles sampled, unexplained values listed).
- [ ] All states captured as screenshots: default, hover, focus, disabled,
  loading, empty, error for each interactive region.
- [ ] Keyboard walk recorded: tab order through the screen, focus visible
  in every stop, no trap, modal focus contained.
- [ ] Reduced-motion pass: animations resolve to final states, no content
  exists only inside motion or auto-rotation.
- [ ] Layout shift on load and on async updates observed (content does
  not jump when images, badges, or data arrive).
- [ ] Placeholder scan: no lorem ipsum, no grey-box imagery, no invented
  numbers presented as real anywhere in the judged artifact.
- [ ] Stamp-lies check: every claim the output makes about itself — header
  stamps naming the macrostructure, theme, or gate scores; metadata;
  stated token usage; a preview block's declared sections — is compared
  against the artifact itself. A claim that disagrees with what was
  actually built is a Critical finding, because every later reader trusts
  the stamp instead of re-checking the work.
- [ ] DESIGN.md drift check: the artifact's rendered tokens and treatments
  are diffed against DESIGN.md as it currently stands, value by value.
  Drift is listed explicitly; unrecorded drift is a Required finding, and
  deliberate drift without a Variants amendment is treated as drift, not
  initiative.

## Named-tell findings

Craft findings name the tell, not the reviewer's mood. The named tells
live in taste-core.md (the pre-ship gates) and ux-heuristics.md (the
microinteraction tells); a finding cites the tell by its name so the
author can find the rule, the fix, and the reason without a second
conversation. The format is one line per finding:

```
[severity] Tell name — file:line or screen region. Why it fails here. → The fix.
```

Example: `[Required] transition-all — styles.css:142. The card's focus
ring animates in with everything else. → Name the two properties that
change on hover; focus stays instant.` A finding that cannot name its
tell, point at its evidence, and state its fix is an opinion, and it is
recorded as FYI at most.

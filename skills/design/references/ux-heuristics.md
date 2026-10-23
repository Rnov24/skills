# UX heuristics

This is the usability checklist for the design phase and for the
interaction axis of design review. Load it when writing USERFLOW.md, when
building screens with forms, lists, or state changes, and whenever a review
needs usability judged as checkable statements rather than impressions.
Rules are grouped by the surface they govern; an item that does not apply
to the screen under review is marked n/a with the reason, never silently
skipped.

## Choice, grouping, and convention

The point of every screen is the user's goal: design the shortest clear
path to it, make the next action obvious, and remove anything that does
not serve that path.

- [ ] **One purpose per screen (Hick).** Each screen has one clear
  purpose and one dominant decision. Options that are irrelevant or
  low-priority are removed, deferred, or grouped behind it — the choice
  count on screen is a design decision, not an accident of the data.
- [ ] **Recommend, don't dump (Hick).** Where a user may struggle to
  choose, the interface recommends an option (a default, a "most common"
  marker, a sensible ordering) instead of presenting an undifferentiated
  list and leaving the work to them.
- [ ] **Familiar before novel (Jakob).** Navigation, search, settings,
  and account controls sit where comparable products put them, and icons
  and gestures mean what they mean elsewhere. A novel pattern is used
  only when its advantage over the familiar one can be named in a
  sentence; novelty without a named advantage fails.
- [ ] **Spacing signals grouping (Proximity).** Related labels,
  controls, and information sit closer to each other than to anything
  unrelated. Relationships are established by spacing first; a border or
  box is added only when spacing alone cannot carry the grouping.
- [ ] **Chunk, and carry it forward (Miller).** Long content and long
  tasks are divided into small, meaningful groups with headings. The
  user never has to remember information from an earlier screen to
  complete a later one — the system carries it, prefills it, or repeats
  it where it is needed.
- [ ] **Same look, same purpose (Similarity).** Elements with the same
  appearance do the same kind of thing, everywhere: colour, label, icon,
  spacing, and state behaviour are consistent per component. The same
  visual treatment is never reused for a different action, and an
  established component is reused before a new one is created.
- [ ] **Connect what belongs together (Uniform Connectedness).**
  A control is visually connected to the content it affects — shared
  container, background, line, or state — and unrelated elements are
  kept visually separate. Connection is deliberate, never decoration.
- [ ] **Essentials first and last (Serial Position).** In any sequence
  — navigation, a list, a screen, a flow — the most important item comes
  first and the final action or takeaway comes last. Low-priority items
  sit in the middle, never in the two positions people remember.

## Navigation and wayfinding

- [ ] The user can always tell where they are: the current location is
  visually indicated in navigation, and page titles match the label that
  led there.
- [ ] Back behaves the way the platform promises. In-app back returns to
  the previous in-app state with scroll and input intact; nothing replaces
  history so the browser or system back button breaks.
- [ ] Any state worth sharing or returning to has a URL or deep link that
  restores it. One static address for every state of a dynamic view fails.
- [ ] Breadcrumbs appear only where the hierarchy is three or more levels
  deep; on flat structures they are noise and are omitted.
- [ ] Primary navigation holds at most five destinations on mobile bottom
  bars and stays reachable without scrolling on desktop.
- [ ] Fixed or sticky navigation never covers content: the layout reserves
  its height, and anchored jumps land below it (scroll padding set).
- [ ] Search exists where the content volume makes browsing unreasonable,
  offers suggestions as the user types, and its empty result offers the
  nearest useful alternatives rather than a dead end.

## Forms and input

- [ ] Every input has a visible label, bound to the field, that survives
  typing. A placeholder is never the only label.
- [ ] Required fields are marked, and the marker is explained once per
  form. Optional fields are the minority or are marked instead,
  consistently.
- [ ] Errors appear below the field they belong to, name the problem and
  the fix in plain words, and are announced to assistive technology
  (aria-describedby, role=alert, or a live region). A summary at the top
  alone fails.
- [ ] Validation runs on blur for most fields, on submit for the whole
  form, and never punishes typing in progress with errors for a field the
  user has not left.
- [ ] Fields use the input type and inputmode that summon the right
  keyboard and validation (email, tel, numeric, url), and autocomplete
  attributes let the browser fill what it already knows.
- [ ] The user never re-enters information the system already holds; prior
  values are prefilled or offered for selection.
- [ ] **Defaults are safe (Hick).** A preselected value is the safest and
  most common option, derived from context where context exists. A
  default never creates a commitment the user did not intend (a paid
  tier, a public post, a recurring charge), and every default is easy
  to change at the point where it is shown.
- [ ] **Input is tolerated (Postel).** Fields accept the reasonable
  formats a person would type — spaces and dashes in numbers, either
  date order the locale allows, case-insensitive codes — and normalise
  them instead of rejecting them. Format requirements that cannot be
  tolerated are stated before submission, not discovered from an error.
- [ ] **Impossible actions are unavailable, risky ones are warned
  (Postel).** An action that cannot succeed in the current state is
  disabled with its reason reachable, not left clickable to fail.
  Before a destructive or irreversible action, the interface names what
  will be lost and requires a deliberate confirmation; reversible
  actions never get that dialog (see the confirmation-dialog tell).
- [ ] Password fields offer a show/hide toggle, and long forms disclose
  progressively: the full field list of a complex task is never the first
  screen.
- [ ] Submitting shows progress on the control itself, disables duplicate
  submission, and ends in a visible success or error state. A button that
  does nothing visible on click fails.

## Feedback and system states

- [ ] Every asynchronous action produces feedback within the interaction:
  a skeleton, spinner, or progress indicator that preserves the layout and
  keeps focus where it was. A frozen screen during a wait fails.
- [ ] Loading placeholders reserve the space of what replaces them, so
  content arriving does not shove the page around (layout shift visible to
  the eye fails).
- [ ] Every list, page, and panel that can be empty has a designed empty
  state: what is missing, why, and the action that fills it.
- [ ] Every error state offers recovery: what happened, what the user can
  do next, and a working retry or escape. An error message that only
  apologises fails.
- [ ] Success is confirmed briefly and in place (message, state change, or
  toast dismissing itself in 3–5 seconds). Toasts never carry an action
  the user cannot afford to miss.
- [ ] Multi-step work shows its progress (step indicator or bar) and lets
  the user move back without losing entered data.
- [ ] **Feedback lands within ~400ms (Doherty).** Every action is
  acknowledged immediately (state change on the control itself), and a
  result or a visible progress state follows within roughly 400ms.
  Where the outcome is predictable and reversible, an optimistic update
  is applied at once and rolled back on failure. A user left wondering
  whether an action registered fails, whatever the backend's excuse.
- [ ] **Errors preserve the work (Postel).** After any error the user's
  entered data, selections, and scroll position are still there. The
  message names what went wrong in plain words and exactly how to fix
  it, and offers retry, undo, restore, or cancel where the action
  allows one. Making the user re-enter work because the system failed
  is itself a failure.
- [ ] **Flows end memorably (Peak-End).** A completed flow ends on a
  designed completion state: what was accomplished, in the user's
  terms, and what happens next. No flow ends on an empty screen, a
  bare spinner that stops, or a state the user must interpret.
- [ ] **Progress feels like progress (Goal-Gradient, Zeigarnik).**
  Multi-step work is divided into named milestones, progress already
  made is emphasised over the total, and remaining work is stated
  specifically ("2 steps left: address, confirm") rather than as a
  bare percentage. Interrupted work can be resumed where it stopped.
- [ ] Status is never carried by a bare live count alone; where counts
  update dynamically, one atomic, readable status message serves assistive
  technology.

## Lists and data density

- [ ] Long lists offer the controls their size demands: sort, filter, or
  search, with the active state of each visible.
- [ ] Rows keep one primary action obvious; secondary actions are grouped,
  not sprayed across the row as competing buttons.
- [ ] **One dominant action per section (Von Restorff).** Every section
  and screen has at most one visually dominant call to action; secondary
  actions are visibly quieter. When everything is emphasised, nothing
  is — a screen where three buttons compete at the same weight fails.
- [ ] **Actions sit beside their content (Fitts).** A control is placed
  next to the content it affects, a form's submit sits near its final
  input, and frequent actions sit within easy reach of where the user's
  attention already is. Sending the eye or the pointer across the screen
  to act on what it is looking at fails.
- [ ] **The path stays short (Parkinson).** The number of steps, screens,
  and confirmations between intent and completion is counted in the
  flow and justified step by step; a step that only confirms a
  reversible action, or asks again for information already given, is
  removed. Frequent and repeat actions offer a shortcut (a default, a
  repeat-last, a saved choice) instead of the full path every time.
- [ ] Tables align text left, numbers right with tabular figures, and keep
  the header identifiable when the table scrolls.
- [ ] Dense data earns its density: every column answers a question a
  persona in PERSONAS.md actually asks, and the rest is one click deeper,
  not on the first screen.
- [ ] Pagination or infinite loading states the total or the position;
  a list that silently ends fails.

## Touch and mobile

- [ ] Touch targets are at least 44pt on iOS, 48dp on Android, and never
  below 24 CSS px on web, with at least 8px of space between adjacent
  targets.
- [ ] No primary action depends on hover. Hover may decorate; tap and
  click must complete every task.
- [ ] Custom gestures never fight the platform: vertical scroll on main
  content is sacred, horizontal swipes belong to contained carousels, and
  drag interactions have a button or tap alternative.
- [ ] Full-height layouts use dynamic viewport units (dvh) or equivalent,
  so mobile browser chrome does not clip content designed against 100vh.
- [ ] Nothing requires horizontal scrolling at the smallest supported
  width, and layouts survive 200% text scaling without clipped content.
- [ ] Tap feedback is immediate (state change within the frame budget);
  the 300ms-feeling lag of unmanaged tap handling fails.
- [ ] A focused input scrolls into view above the on-screen keyboard;
  a form field the keyboard covers while it is being filled fails, at
  whichever height the keyboard takes on that device.

## Accessibility floor

- [ ] Contrast passes the numbers in taste-core.md, including placeholder
  text, disabled states that still carry information, and text over
  imagery (measured against the image, not the average of it). Verdicts
  read the unrounded ratio: 4.498:1 displays as 4.50 and still fails.
  Compute a pair with `scripts/contrast-check.py <hex1> <hex2>` rather
  than estimating it; `--selftest` recomputes the reference table below
  so the table and the formula cannot drift apart.
- [ ] Non-text contrast holds at 3:1 for the parts of a component a user
  must perceive to use it: control boundaries, status indicators, input
  borders against their field, chart segments against their neighbours.
  A button identifiable only by its label text, on a boundary that
  vanishes against the surface, fails.
- [ ] Every interactive element is reachable and operable by keyboard
  alone, in an order that matches the visual order, with no traps.
  Escape closes dialogs, menus, and popovers; a layer that only a
  pointer can dismiss fails.
- [ ] Focus is visible on every control, including inside modals: an
  indicator of at least 2 CSS px perimeter at 3:1 contrast against
  adjacent colours, never removed without a replacement, and never hidden
  under sticky bars or overlays.
- [ ] Meaningful images carry descriptive alt text; decorative ones are
  marked decorative. Icon-only controls carry an accessible name.
- [ ] Heading levels are sequential and landmarks exist (header, nav,
  main), so the page can be navigated by structure, not only by sight.
- [ ] Reduced motion is honoured as taste-core.md states, and no
  information exists only inside an animation, parallax layer, or
  auto-rotating carousel; carousels pause on hover and focus and expose
  every slide to keyboard controls.
- [ ] The page works at 400% zoom and with text spacing increased, without
  loss of content or function (reflow, no two-dimensional scrolling for
  reading content).

Contrast reference pairs, recomputed by `scripts/contrast-check.py
--selftest` — this table is the script's source of truth, so edit the
table and the script's verdicts follow:

| Pairing (text on background) | Ratio | Normal text (4.5) | Large text (3.0) |
|------------------------------|-------|-------------------|------------------|
| Black on white | 21.00 | Pass | Pass |
| White on black | 21.00 | Pass | Pass |
| White on #333333 | 12.63 | Pass | Pass |
| White on #666666 | 5.74 | Pass | Pass |
| #777777 on white | 4.48 | Fail | Pass |
| #777777 on #070707 | 4.50 | Fail | Pass |
| White on #888888 | 3.54 | Fail | Pass |
| White on #999999 | 2.85 | Fail | Fail |
| #555555 on black | 2.82 | Fail | Fail |

The `#777777 on #070707` row is the near-threshold case: 4.4983:1 rounds
to 4.50 for display and still fails 4.5:1. Read the table as a sanity
check, not a substitute; any pairing not listed, or near a threshold,
goes through the script.

## The eight-state contract

Every interactive element has eight states. Styling two of them (default
and hover) is where generated interfaces break, and in component-scope
work this contract is mandatory rather than advisory. An element missing
any state is unfinished.

| State | When | Treatment |
|---|---|---|
| Default | At rest | Base styling |
| Hover | Pointer over, inside `@media (hover: hover)` only | One small shift: colour, 1px translate, or border |
| Focus | Keyboard or programmatic focus | Visible ring via `:focus-visible`, never animated in |
| Active | During the press | Pressed in: darker, or `translateY(1px)` |
| Disabled | Not interactive | Three channels at once (below) |
| Loading | Processing | Inline spinner or progress; the label stays readable |
| Error | Failed validation or action | Colour plus glyph plus message, `aria-invalid="true"` |
| Success | Completed | Quiet confirmation; auto-clears when the user edits again |

- [ ] Disabled is signalled on three channels, never opacity alone:
  reduced opacity (~0.55), `cursor: not-allowed`, and the native
  `disabled` attribute or `aria-disabled="true"`.
- [ ] State is never carried by colour alone; error and success pair
  their colour with a glyph, a label, or a pattern.
- [ ] Hover styles live inside `@media (hover: hover)` so touch users
  never inherit stuck hover states.

## Input geometry

Inputs are where almost-right interfaces lose. These rules are
mechanical: each one either holds in the CSS or it does not.

- [ ] **Border width is constant across every state.** Default, hover,
  focus, error, and disabled all keep the same `border-width`. State
  changes go to `border-color`, `background-color`, `outline`, or
  `box-shadow` — never to width, because a width change shifts layout on
  focus and the eye reads it as the page being untuned.
- [ ] **The focus outline slot is reserved at rest.** Inputs carry
  `outline: 2px solid transparent` with `outline-offset: 1px` from the
  start, so the focus ring appears inside geometry that already exists.
  The ring itself is built from `outline`, never from `border`.
- [ ] **The right-edge glyph slot is reserved.** Every input holds ~24px
  at its right edge for a clear button, an error or success glyph, or a
  loading spinner. An unused slot sits empty; content never reflows when
  a glyph appears.
- [ ] **Input height equals button height** on the same form. One base
  height, with 44px as the floor. A 38px input beside a 44px button is
  the most common form-tuning failure there is.
- [ ] **The helper-text slot has a stable height** (`min-height: 1lh`)
  even when empty, and the error message replaces the helper text in the
  same slot at the same size. An error appearing must not push the page
  down, and helper and error never show at once.
- [ ] Vertical padding is derived, not magic: `(height − line-height) / 2`
  for the input's base height.
- [ ] Never transition `border-width`, `padding`, or `height` between
  states, and never fade or scale the focus ring in.
- [ ] Textarea keeps the same geometry, plus `resize: vertical` and a
  `min-height` around 6rem. A custom select is built only when native
  keyboard and screen-reader behaviour can be fully replicated;
  otherwise the native control is styled at the wrapper.
- [ ] During async validation the field stays editable with its spinner
  in the glyph slot; the submit control carries the disabled state, not
  the field.

## Timing and easing canon

Microinteraction timing is a token decision, not a per-screen invention.
Pick durations from these buckets and do not invent new ones.

| Bucket | Use for |
|---|---|
| 80–120ms | Instant feedback: press ticks, checkbox state, keystroke echo |
| 150–200ms | Hover transitions, single-property fades, tooltip appearance after its delay |
| 250–300ms | Modal, dropdown, and sheet opening; tab content crossfade; validation glyph |
| 400–500ms | Toast entry, page-load reveal, accordion, multi-property transitions |
| 0ms | Focus appearance, keyboard navigation, error appearance — many things should not animate at all |

- Exit durations run at 60–75% of the matching entrance (a 300ms enter
  pairs with a ~200ms exit), never the reverse.
- Three easing tokens cover nearly all UI motion: `--ease-out`
  `cubic-bezier(0.16, 1, 0.3, 1)` for entering elements, `--ease-in`
  `cubic-bezier(0.7, 0, 0.84, 0)` for exiting elements, `--ease-in-out`
  `cubic-bezier(0.65, 0, 0.35, 1)` for state toggles. A standard
  alternative, `cubic-bezier(0.4, 0, 0.2, 1)`, may replace the set where
  a platform's own motion language already uses it.
- Banned curves: the browser-default `ease` (flat, uncrafted), `linear`
  except for progress bars and continuous loaders, and any overshoot
  above ~110% on UI state changes. Spring physics and overshoot belong
  to physical interactions only: drag release, swipe dismiss, picker
  snap.
- At most three distinct animation primitives run on one page. When in
  doubt, cut: ask what breaks if the animation were instant, and keep
  only the ones where the answer is information.

## Named microinteraction tells

Review vocabulary for the motion failures generated code repeats. Any one
of these in a judged screen is a finding; name it in the review rather
than describing it vaguely.

- **transition-all** — every property animates, including ones that must
  be instant; properties are never specified.
- **Universal hover scale** — every card lifts the same way on hover,
  with no shadow change, no easing, and no purpose.
- **Bouncy overshoot on UI** — springy easings on buttons, modals, and
  tooltips; a 2018 throwback reserved for physical drag release only.
- **Stacked hover effects** — one element translating, scaling,
  shadowing, colour-shifting, and rotating in the same hover.
- **Animated hover gradients** — the background slides through colour
  space on hover; expensive and communicates nothing.
- **Cursor-follower dots** — a trailing dot lagging behind the pointer.
- **Parallax on scroll** — layers drifting at different speeds; a
  vestibular trigger that rarely serves the content.
- **Layout-property transitions** — `width`, `height`, `margin`, or
  `padding` animated frame by frame through reflow.
- **Celebratory success toasts** — "Done!" announced for an effect the
  user is already looking at; success should be silent.
- **Confirmation dialogs for reversible actions** — a modal asking
  permission to do what an Undo toast would cover better.
- **Spinner flash** — a spinner shown for under a frame's notice; delay
  showing it ~150ms, or keep it visible at least ~300ms once shown.
- **Equal tooltip delays** — hover and focus sharing one delay; hover
  waits 800–1000ms, focus is instant, because the intents differ.
- **Toasts that shift layout** — a new toast pushing content down and
  the dismissed one letting it spring back; toasts stack at a corner.
- **Universal scroll fade-up** — every section fading in on intersection
  until the page never settles; one orchestrated entrance is the limit.

---

Absorption note (A-006, 2026-10-23): the non-text contrast rule, the
keyboard-occlusion rule, the Escape rule, the unrounded-threshold
discipline, and the contrast reference table were extracted from
miqdadbadjuber/anti-slop (MIT, commit c93d08c7), its human unit; the
checker script is adapted at `scripts/contrast-check.py` with credit in
its header. Full audit: `docs/audit/absorbed/2026-10-23-anti-slop.md`.

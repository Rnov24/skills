# UX heuristics

This is the usability checklist for the design phase and for the
interaction axis of design review. Load it when writing USERFLOW.md, when
building screens with forms, lists, or state changes, and whenever a review
needs usability judged as checkable statements rather than impressions.
Rules are grouped by the surface they govern; an item that does not apply
to the screen under review is marked n/a with the reason, never silently
skipped.

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
- [ ] Status is never carried by a bare live count alone; where counts
  update dynamically, one atomic, readable status message serves assistive
  technology.

## Lists and data density

- [ ] Long lists offer the controls their size demands: sort, filter, or
  search, with the active state of each visible.
- [ ] Rows keep one primary action obvious; secondary actions are grouped,
  not sprayed across the row as competing buttons.
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

## Accessibility floor

- [ ] Contrast passes the numbers in taste-core.md, including placeholder
  text, disabled states that still carry information, and text over
  imagery (measured against the image, not the average of it).
- [ ] Every interactive element is reachable and operable by keyboard
  alone, in an order that matches the visual order, with no traps.
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

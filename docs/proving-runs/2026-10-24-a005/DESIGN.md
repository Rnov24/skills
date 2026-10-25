---
version: "1"
name: "linkstash-design"
description: "A quiet, light workbench for one person's saved links. Warm paper canvas, white surfaces separated by hairlines instead of shadows, near-black blue-grey ink, and one deep-teal accent that means exactly one thing: the action that saves or confirms. System type only, mono for URLs and tags, no decorative system at all. The design language in concrete terms: paper #faf8f4, accent #007b82, system sans at 700/500/400, radius 10px surfaces and 8px controls, one soft shadow on the form surface and nowhere else."
colors:
  surface: "#ffffff"
  ink: "#182029"
  ink-muted: "#575e66"
  border: "#dadee3"
  accent: "#007b82"
  primary: "#007b82"
  on-accent: "#f8fdfd"
  danger: "#b02a2d"
  on-danger: "#ffffff"
  paper: "#faf8f4"
typography:
  display:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', sans-serif"
    fontSize: "24px"
    fontWeight: 700
    lineHeight: "1.25"
    letterSpacing: "0px"
  body:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: "1.5"
    letterSpacing: "0px"
  label:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', sans-serif"
    fontSize: "14px"
    fontWeight: 500
    lineHeight: "1.4"
    letterSpacing: "0px"
  data:
    fontFamily: "ui-monospace, 'SF Mono', Menlo, Consolas, monospace"
    fontSize: "13.6px"
    fontWeight: 400
    lineHeight: "1.45"
    letterSpacing: "0px"
rounded:
  sm: "6px"
  md: "8px"
  lg: "10px"
  full: "9999px"
spacing:
  xs: "4px"
  sm: "8px"
  md: "16px"
  lg: "24px"
  xl: "40px"
  section: "24px"
components:
  button-primary:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.md}"
  button-primary-disabled:
    backgroundColor: "{colors.border}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.md}"
  chip:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    typography: "{typography.data}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.sm}"
  chip-selected:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.data}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.sm}"
  button-danger:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.on-danger}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.md}"
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.md}"
---

# Design constitution: Linkstash

## Character

A quiet workbench for one person's links. Light, calm, and fast to
scan; the page is a tool, not a poster. Every rule below is checkable
against a screenshot or the CSS. (This constitution re-expresses the
project's original prose DESIGN.md in the suite's registry format;
where the two disagree, this registry is the draft under review, not
yet the project's live file.)

## Tokens

- Colour roles: paper is the page canvas; surface carries the form and
  rows; ink is primary text; ink-muted is secondary text and metadata;
  border is every hairline and resting input border; accent is the one
  chromatic meaning in the system, contracted to save/confirm actions,
  the active tag chip, focus rings, and links; danger appears only
  inside the delete confirmation. Light mode only; there is no dark
  surface intent.
- Type roles: display carries the page title only; body carries notes
  and form text; label carries field labels and buttons; data (mono)
  carries URLs, tags, and the link count. Data type is forbidden in
  headings; display type is forbidden inside list rows.
- Font substitutes: none needed. The system is system stacks by
  decision, so every named face loads everywhere with no substitute.
- Spacing and radius: a 4px-based scale; sections use lg or section
  steps only. Radius is contracted by altitude: surfaces lg, controls
  md, chips sm, nothing else.

## Layout rules

- One column, max-width 880px, centred, 20px page padding.
- Page order never changes between states: header (wordmark + count),
  add form, toolbar (search, tag chips, Active/Archived switch), link
  list, footer line.
- The add form is one surface: URL full width, then title + tags in a
  row, then note, then the submit button at the form's bottom-right.
- List rows: title (link, ink, 600) with host and date quiet at the
  right; note in ink-muted on line two when present; tag chips and row
  actions on line three. Rows are separated by hairlines, never
  shadows; the form surface carries the system's only shadow.

## Responsive

| Breakpoint | Behaviour |
| --- | --- |
| ≤640px | Single column already; title + tags row stacks vertically; row actions stay on line three, left-aligned; page padding drops to 16px |
| 641–1024px | As designed; max-width still binds |
| >1024px | As designed; the column does not widen past 880px |

No imagery exists to reframe at any breakpoint.

## Component rules

- One visually dominant action per view: the add form's submit. Every
  other action is a quiet text button or chip.
- Tag chips toggle a single tag filter; the selected chip is the only
  accent-filled chip on the page.
- Inputs are 44px tall with a 1px border in every state; state changes
  colour only. The focus ring is a 2px accent outline whose slot is
  reserved at rest, so focus never shifts layout. Labels are always
  visible above fields.
- The delete confirmation appears inline in its row ("Hapus tautan
  ini? [title] — Hapus / Batal"), never a modal, never a browser
  confirm().

## Motion rules

At most one primitive: control colour settling on hover (150ms, colour
only, inside `@media (hover: hover)`). No entrance animations, no
scroll effects. Reduced motion removes the hover transition.

## Imagery and iconography

None. No photos, no illustrations, no icon set. The wordmark is type.
This is a decision, not an omission: a link workbench earns no imagery.

## Bans

- No default AI aesthetic clusters (cream+terracotta, near-black+acid,
  unprompted broadsheet, generic SaaS card kit). The warm paper here is
  a near-white neutral at 98% lightness with a teal accent, not the
  cream+terracotta cluster; the distinction is recorded so a reviewer
  checks values, not vibes.
- No template chrome: middle dots ('A · B · C'), spaced em-dash
  labels, button '→'.
- No single-word colored or styled accents in headlines.
- No gradient text or background gradients anywhere.
- No decorative numbered markers (01/02/03) on non-sequential content.
- No shadows except the form surface's one soft shadow.
- No external font or asset requests; system stacks only.

## Accessibility floor

Body text ink on paper measures 15.5:1; ink-muted on paper 6.2:1;
on-accent on accent 4.9:1 (AA for the label size it carries); danger
on surface 6.5:1. All pairs verified with the suite's
`scripts/contrast-check.py` in this proving run's report. Interactive
targets are 44px tall; every action is keyboard reachable with a
visible focus ring; reduced motion is honoured above.

## Exports

The registry is the single source of truth. This project ships one
translation: CSS custom properties on `:root` in the app stylesheet,
using the OKLCH values of the original prose constitution. The hex
values in this registry are sRGB conversions of those OKLCH tokens
(computed, not re-picked); if the two ever disagree, the project's
live CSS wins until this draft is adopted, and the disagreement is a
finding, not a detail.

Validation: after any edit to this file, run
`npx @google/design.md lint DESIGN.md` and clear what it flags
(broken token references, contrast failures, orphaned tokens). A
registry edit that has not been linted has not been checked; the
review gate treats a lint failure like a failing test.

## Variants

None. One surface, one system.

## Known gaps

- The original constitution is prose with OKLCH values; this registry
  draft converts them to hex. The conversion is mathematical, but the
  project's canonical values remain OKLCH until the owner adopts this
  format in the project repo.
- Component registry entries cover the components the constitution
  names (button, chip, input). Row actions and the switch are governed
  in prose above but have no registry entries yet; adding them is
  follow-up work, recorded here rather than silently absent.
- Elevation has no registry token; the one permitted shadow is
  described in Layout rules. The format has no elevation registry
  section in the suite template, which is itself a gap worth an
  adapt-cycle note.
- The linter expects a `primary` colour where the suite template's
  registry names the role `accent`. This draft defines both with the
  same value (accent is the role name the prose uses; primary is the
  linter's alias). The template should rule on this once, for every
  project, instead of each draft improvising.

---
version: "1"
name: "<project-slug>-design"
description: "<One paragraph: the design language in concrete terms — canvas, accent, type pairing, the one decorative system if any. This is the frontmatter rendering of Character below; keep the two in agreement.>"
colors:
  surface: "<hex>"
  surface-raised: "<hex>"
  ink: "<hex>"
  ink-muted: "<hex>"
  border: "<hex>"
  accent: "<hex>"
  on-accent: "<hex>"
  danger: "<hex>"
  on-danger: "<hex>"
  scrim: "<hex at an opacity, for text over photography; delete if no text ever sits on imagery>"
typography:
  display:
    fontFamily: "<family, fallbacks>"
    fontSize: "<px>"
    fontWeight: <weight>
    lineHeight: "<px or ratio>"
    letterSpacing: "<px or em>"
  body:
    fontFamily: "<family, fallbacks>"
    fontSize: "<px>"
    fontWeight: <weight>
    lineHeight: "<px or ratio>"
  label:
    fontFamily: "<family, fallbacks>"
    fontSize: "<px>"
    fontWeight: <weight>
    lineHeight: "<px or ratio>"
rounded:
  sm: "<px>"
  md: "<px>"
  lg: "<px>"
  full: "9999px"
spacing:
  xs: "<px>"
  sm: "<px>"
  md: "<px>"
  lg: "<px>"
  xl: "<px>"
  section: "<px>"
components:
  button-primary:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: "{spacing.xs} {spacing.md}"
  button-primary-disabled:
    backgroundColor: "{colors.border}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: "{spacing.xs} {spacing.md}"
---

# Design constitution: <project>

< The frontmatter above is the token registry: the single machine-readable
  source for every colour, type, radius, and spacing value in this system,
  and for each component's token bindings. Prose below states roles, usage,
  and rules; it never restates values. If prose and registry disagree, the
  registry is wrong or the prose is stale — fix one, never ship both.
  Component states are separate registry entries with a state suffix
  (-active, -pressed, -selected, -disabled, -on-dark), so state coverage
  is enumerable by reading the registry. New variants are new entries,
  never inline overrides inside a component. >

## Character
< One paragraph. The personality every screen must be consistent with,
  stated concretely enough to argue from. >

## Tokens
< Roles and usage only — values live in the registry. >
- Colour roles: <which role does what; the accent's one meaning; any
  reserved hue and the single meaning it is contracted to; which mode
  (light/dark) serves which surface intent if the system splits modes>
- Type roles: <which registry entry carries display, body, labels, data;
  where each is used and where it is forbidden>
- Font substitutes: <for every licensed or unavailable family: the named
  open substitute and the adjustment it needs (weight, line-height,
  letter-spacing). A system that names a face nobody can load is unfinished.>
- Spacing and radius: <the scale's logic; which steps sections may use>

## Layout rules
< Grid, density. Rules a reviewer can check, not adjectives. >

## Responsive
< Breakpoint table: each breakpoint, what collapses or reflows and how,
  and how imagery is reframed (crop, art direction, or removal) at each.
  Touch targets are governed by the accessibility floor, not restated here. >

## Component rules
< Per component family: when it is used, when it is not, its states. The
  token bindings for each component live in the registry; this section is
  the usage law the bindings cannot express. >

## Motion rules
< What motion is for here, durations, what never animates. >

## Imagery and iconography
< Sources, style, treatment. >

## Bans
< The explicit never list for this project. Each ban is checkable.
  Default anti-slop bans to enforce unless consciously overridden:
  - No default AI aesthetic clusters (cream+terracotta, near-black+acid, unprompted broadsheet, generic SaaS card kit)
  - No template chrome: middle dots ('A · B · C'), spaced em-dash labels, button '→'
  - No single-word colored/styled accents in headlines
  - No gradient text or unmotivated background gradients
  - No decorative numbered markers (01/02/03) on non-sequential content >

## Accessibility floor
< Contrast, target sizes, keyboard, reduced motion. >

## Exports
The registry is the single source of truth. Tooling consumes translations
of it, never parallel definitions: keep one tokens file (CSS custom
properties on `:root`, with dark variants redefined under a `.dark` or
`[data-theme="dark"]` block), and generate from the registry a Tailwind
v4 `@theme` block, a DTCG `tokens.json`, and shadcn CSS variables.
< Which translations this project actually ships, and where each lives. >
When an export is generated into the project, it merges into the existing
entry stylesheet rather than overwriting it. If a generated translation
and this file disagree, this file wins and the translation is regenerated.
A design refresh updates the registry and nothing else.

Validation: after any edit to this file, run
`npx @google/design.md lint DESIGN.md` and clear what it flags
(broken token references, contrast failures, orphaned tokens). A registry
edit that has not been linted has not been checked; the review gate treats
a lint failure like a failing test.

## Variants
< A page or component whose treatment should differ from the system
  above is recorded here as an amendment, naming the variant, where it
  applies, and which tokens or treatments change — never as per-page
  token overrides inside the component itself. A variant that becomes
  the default is promoted into the sections above and closed here. >

## Known gaps
< What this constitution does not establish: states never observed,
  surfaces out of scope, values sampled rather than canonical, faces
  whose substitutes are approximations, timings never measured. Required
  when the system derives from a study or an extraction; write "none
  known" only when the system was authored first-hand and fully
  specified. A gap recorded here is a finding already answered; a gap
  left out is a false claim of completeness. >

# Design constitution: <project>

## Character
< One paragraph. The personality every screen must be consistent with,
  stated concretely enough to argue from. >

## Tokens
- Colour: <palette with roles: surface, ink, accent, danger; hex values>
- Type: <families, scale, weights; where each size is used>
- Spacing: <base unit and allowed steps>
- Radius / elevation: <named values only>

## Layout rules
< Grid, breakpoints, density. Rules a reviewer can check, not adjectives. >

## Component rules
< Per component family: when it is used, when it is not, its states. >

## Motion rules
< What motion is for here, durations, what never animates. >

## Imagery and iconography
< Sources, style, treatment. >

## Bans
< The explicit never list for this project. Each ban is checkable. >

## Accessibility floor
< Contrast, target sizes, keyboard, reduced motion. >

## Exports
The tokens above are the single source of truth. Tooling consumes
translations of them, never parallel definitions: keep one tokens file
(CSS custom properties on `:root`, with dark variants redefined under a
`.dark` or `[data-theme="dark"]` block), and generate from it a Tailwind
v4 `@theme` block, a DTCG `tokens.json`, and shadcn CSS variables.
< Which translations this project actually ships, and where each lives. >
When an export is generated into the project, it merges into the
existing entry stylesheet rather than overwriting it. If a generated
translation and this file disagree, this file wins and the translation
is regenerated. A design refresh updates this section and nothing else.

## Variants
< A page or component whose treatment should differ from the system
  above is recorded here as an amendment, naming the variant, where it
  applies, and which tokens or treatments change — never as per-page
  token overrides inside the component itself. A variant that becomes
  the default is promoted into the sections above and closed here. >

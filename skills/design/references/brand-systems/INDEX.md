# Brand systems — the DESIGN.md reference shelf

Eighty-four worked DESIGN.md files, each an extraction of one real
brand's design system, vendored from VoltAgent/awesome-design-md (MIT,
commit 3b605329240ce735b510037cca322f1831fdd7f8, absorbed 2026-10-23,
A-005). They are here as references: examples of the DESIGN.md format at
full depth, and worked systems to consult when a brief names a brand
direction or a project needs a starting system to react against.

## Load discipline

Read this index, pick at most one or two brands, and read only those
files. A typical use is one brand file beside the brief while a project's
own DESIGN.md is drafted. Reading the shelf to "get a feel for it" is
the single biggest token waste available in this suite; the shelf is
2.6 MB and exists so nobody has to hold it all.

## What these files are, and are not

They are inspired interpretations extracted from public websites, not
the brands' official internal systems, and the suite treats them the
way the study skill treats any public reference: principles and format
may be learned from them; a brand's signature moves and token identity
are not carried into a project's own system wholesale. A project that
wants to be "like Linear" drafts its own DESIGN.md informed by the
reference, under the brief and the attestation rules, in its own tokens.

Quality caveats, recorded so nobody has to rediscover them:

- Three files have frontmatter that does not parse as YAML (elevenlabs,
  raycast, supabase — an unquoted colon in the description). Read them as
  prose; do not feed them to tooling until fixed.
- Ten files use the older prose format with an Agent Prompt Guide
  (kraken, lamborghini, lovable, mastercard, runwayml, sanity, spotify,
  starbucks, tesla, theverge). Their token values live in prose tables.
- Twenty-four files carry auto-generated `ex-*` example blocks, thirteen
  with unresolved `TO_FILL` markers. Skip those sections; they are
  generator filler, not extracted system.
- The retro files (dell-1996, nintendo-2001) contain admittedly
  speculative modern-responsive sections. Enjoy them as period studies;
  do not cite them as extracted fact.
- Signature caution: mastercard (motif), stripe (gradient mesh),
  theverge (palette), nike (typographic treatment), and wired (type
  system) carry brand signatures. Reference for analysis and format;
  the signature itself never transfers.

## The shelf

### AI & LLM platforms
claude (warm terracotta, editorial) · cohere (enterprise white, gradient
media) · elevenlabs (dark cinematic, waveform) · jobright (mint, black
pills, condensed type) · minimax (bold dark, neon) · mistral.ai
(minimal, purple-toned) · ollama (terminal-first monochrome) ·
opencode.ai (developer dark) · replicate (clean white, code-forward) ·
runwayml (cinematic dark heroes, paper bands) · together.ai (blueprint
technical) · voltagent (void black, emerald, terminal) · x.ai (stark
monochrome)

### Developer tools
cursor (warm cream editorial, IDE chrome) · expo (dark, code-centric) ·
lovable (playful gradients) · raycast (dark chrome, gradient accents) ·
superhuman (premium dark, keyboard-first) · vercel (black-and-white
precision, Geist) · warp (dark terminal, block UI)

### Backend, database & DevOps
clickhouse (yellow accent, technical docs) · composio (dark, colourful
integration icons) · hashicorp (enterprise black-and-white) · mongodb
(green, documentation-led) · oracle (warm neutral ladder, charcoal
actions) · posthog (playful, developer dark) · sanity (dark-first
editorial, coral accent) · sentry (dark, data-dense, pink-purple) ·
supabase (dark emerald, code-first)

### Productivity & SaaS
cal (clean neutral) · intercom (friendly blue) · linear.app
(ultra-minimal, purple accent) · mintlify (clean, green, reading-first)
· notion (warm minimalism, serif headings) · resend (minimal dark, mono
accents) · sap (white canvas, flat blue bands) · zapier (warm orange,
illustration-led)

### Design & creative tools
airtable (colourful, structured) · clay (organic shapes, soft
gradients) · figma (vibrant multi-colour) · framer (bold black and
blue, motion-first) · miro (yellow accent, infinite canvas) · webflow
(blue, polished marketing)

### Fintech & crypto
binance (yellow on monochrome) · coinbase (clean blue, institutional) ·
kraken (purple, data-dense) · mastercard (warm cream, orbital pills) ·
mercury (ink-violet, indigo action) · nerdwallet (deep spruce, mint
washes) · revolut (dark, gradient cards) · stripe (purple gradients,
light display type) · wise (bright green, friendly)

### E-commerce & retail
airbnb (coral, photography-led, rounded) · meta (photography-first,
light/dark surfaces) · mydealz (dense card feed, voting pill) · nike
(monochrome, massive uppercase type) · shopify (dark cinematic, neon
green) · starbucks (four-tier greens, warm cream)

### Media & consumer tech
1win (near-black, vivid green — gambling; reference only) · aljazeera
(flat paper, dense headlines, orange) · apple (premium whitespace,
cinematic imagery) · dji (studio tiles, engineering blue) · hp (white
canvas, electric blue) · ibm (Carbon system, structured blue) · nvidia
(green-black, technical) · oura (warm paper, editorial serif) ·
pinterest (red accent, masonry) · playstation (three-surface channel
layout) · spacex (black-and-white, full-bleed) · spotify (green on dark,
album-art-led) · theverge (acid-mint and ultraviolet) · uber (bold
black-and-white) · vodafone (monumental uppercase, red bands) · wired
(paper-white broadsheet, custom serif)

### Automotive
bmw (dark premium, precise) · bmw-m (motorsport contrast) · bugatti
(cinema black, monumental type) · ferrari (chiaroscuro editorial, red
used sparingly) · lamborghini (true black, gold accent) · renault
(aurora gradients, zero-radius buttons) · tesla (radical subtraction,
full-viewport photography)

### Retro web
dell-1996 (catalog-era 1996 web) · nintendo-2001 (Y2K console chrome)

### Unlisted upstream
slack (aubergine, pill CTAs — absent from the upstream README list;
weakest extraction in the set, token scale incomplete)

## Provenance

Source: https://github.com/voltagent/awesome-design-md at commit
3b605329240ce735b510037cca322f1831fdd7f8, MIT licence (full text in
UPSTREAM-LICENSE.txt beside this index). Vendored verbatim as
reference data under the owner's ruling at the A-005 human gate
(2026-10-23): taken as a DESIGN.md reference shelf, not digested into
suite rules. The full gluttony audit — including the mechanism merges
that were prepared, then withdrawn under that ruling, and kept on
record for future adapt cycles — is
`docs/audit/absorbed/2026-10-23-awesome-design-md.md`.

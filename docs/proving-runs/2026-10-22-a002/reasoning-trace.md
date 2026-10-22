# Reasoning trace — proving run A-002 (hallmark absorption)

Run: 2026-10-22. Worker deliverables in this folder: `index.html` +
`style.css` (brief 1, full page) and `form-states.html` + `form.css`
(brief 2, component scope). Static HTML/CSS only, no JavaScript, no
external requests of any kind.

## Pre-flight findings (design skill, existing-project scan)

This is a fresh standalone proving project. There is no existing
DESIGN.md, no font stack, no palette, and no framework to preserve:
this folder contained only the two brief files before the run started.
The pre-flight result is therefore "nothing to preserve", stated
plainly: the conflicts the scan exists to catch (a locked DESIGN.md
overriding suite defaults, an inherited palette fighting a new accent,
a motion library already in the manifest) cannot arise here, because
none of those things exist yet. Every token, pairing, and rule in the
deliverables is introduced by this run and recorded below, so a later
run can treat this trace as the thing to preserve or amend.

One constraint does bind like a locked system would: the brief fixes
the budget at zero and the build at static HTML/CSS, and the task
fixes "system font stacks only, no external requests". That collides
with two taste-core defaults — a platform default doing display duty
fails, and the bare system stack is a banned default. The collision is
resolved in favour of the brief, and the reason is recorded here as
the rules require: with webfonts forbidden, the display voice is a
deliberately chosen serif system stack (Georgia-led) picked for the
editorial genre below, paired against a neutral system sans for body,
with a weight contrast of 700 against 400. It is a decision with a
stated reason, not a reach for the first stack that came to mind.

## Diversification / rotation statement

Fresh project, no prior runs in a design log, so there is no last
three to differ from. The rotation is argued from the brief's proof
situation, in plain words, below.

## Preview block — the page (brief 1)

- Macrostructure: 11 Catalogue.
- Genre / direction: editorial (the silent default; no other genre
  fires — not a SaaS or developer tool, not atmospheric, not playful).
  Direction within it: broadsheet catalogue — warm tinted paper,
  serif display, hairline rules, inventory first.
- Enrichment tier: tier 0, typography only, plus the imagery gate's
  honest placeholders for product media (see below). No CSS art, no
  SVG illustration, no generated imagery.
- Sections in order: masthead/nav → hero (the Catalogue heading:
  brand tagline and a short lede, no big display, no global CTA) →
  Katalog (6 products) → Kelas (schedule for 3 classes, then how to
  register in steps) → Testimoni (honest empty state) → footer with
  contact (colophon).
- Nav archetype: N6 Newspaper Masthead. Footer archetype: Ft4 Dense
  Typographic.
- Motion primitives (maximum three; two used, both small): (1) link
  colour settle on hover, 150ms, ease-out, colour property only,
  inside `@media (hover: hover)`; (2) the card micro-action's
  underline thickening on hover is deliberately NOT added — one
  primitive total on links, plus nothing else. Catalogue prescribes
  "reveal: none", so there are no entrance animations, no scroll
  effects, and under `prefers-reduced-motion` the single transition
  resolves to none.
- Accent: exactly one, a roasted terracotta in OKLCH (hue 40),
  defined once as `--accent` in `:root` and used only through the
  token: links' hover/active colour, the focus ring, text selection,
  and the step markers' numerals are kept in muted ink instead, so
  the accent stays under roughly 5% of any viewport. Neutrals are
  tinted toward a warm anchor hue (70) at low chroma — no zero-chroma
  grey, no pure black, no pure white. All other colours are OKLCH
  tokens in the same `:root` block; there are no hex or rgb values
  anywhere in the CSS, and no gradients of any kind.

## The rotation pick, with reasons

Pick: **11 Catalogue.** The page's job is inventory: six bean SKUs of
equal standing, each with a process, an origin, a weight, and a price,
plus a schedule of three classes. Catalogue is the shape whose body
is a uniform grid of variations of the same thing, whose divider is
the hairline rule, whose button is a card-internal link, and whose
opening is an inventory header with a count. The composition can be
said in one sentence: a broadsheet masthead over a uniform inventory
grid, separated by hairlines.

Rejected, with the reason stated:

- **04 Stat-Led — rejected.** Its own index line says it is for when
  a real metric is the narrative, never with invented numbers. This
  brief has no metric: no sales figures, no ratings, no counts of
  happy customers exist, and inventing them is explicitly forbidden.
  A Stat-Led page here could only be built on fabricated proof.
- **09 Quote-Led — rejected.** It opens with borrowed credibility —
  a real quote. No testimonial exists to quote; the brief says so
  outright. Leading with a quote would mean writing one and
  attributing it to someone, which is the exact honesty failure this
  run exists to catch.
- **08 Photographic — rejected.** One strong image per fold is
  impossible: the team has no product photos, stock is banned, and
  generated images masquerading as photos are banned. The imagery
  gate fires instead (below).
- **01 Bento Grid — rejected.** Bento sells features in mixed-weight
  blocks; these are products of equal standing, and F6's own
  anti-pattern list warns against borrowing Bento's irregular spans
  for a product grid. Hierarchy the products do not have would be
  invented by the layout.
- **07 Manifesto / 02 Long Document — not picked.** The brand has a
  point of view, but the brief asks a shop page to do shop work —
  show the beans, show the classes, take the reader to contact.
  A belief-first or prose-first shape would bury the inventory the
  audience came for.

## Imagery gate decision

Kopi Pesisir is a shop, so the gate's shop branch fires: real
photography is what this page needs, and none exists. The build
therefore ships honest placeholders and waits for the owner's assets.
Each product's media slot is a labelled block in one placeholder
token that names the intended subject and the target size (for
example "Foto belum tersedia — Biji Robusta Pesisir utuh, latar
karung goni · target 800 × 600 px"). A placeholder looks like a
placeholder: dashed hairline, flat tinted surface, small label text.
There is no `<img>`, no stock, no generated image, and no CSS or SVG
imitation of a photograph anywhere in the build.

## The testimonial decision

The brief requires a testimonial section and simultaneously states
that no real testimonial exists. The section is therefore built as a
designed empty state, not filled and not silently dropped. It names
what is empty ("Belum ada testimoni yang dapat ditampilkan"), says
why in plain words (the roastery has not yet collected written
testimonials from buyers or class participants, so the section stays
empty rather than being filled with invented quotes), and offers
exactly one action, a typographic link to the catalogue — the
empty-state shape copy.md prescribes. No T-archetype is used: T1, T3
and T4 all render a real quote or a real stat strip, and using their
shapes with fabricated content would launder the invention through
a respectable layout. This choice, and its reason, are recorded here
so the reviewer judges the decision, not just the rendering.

## Component archetype picks, with knob values

Seven archetype files were read and used. No archetype repeats on
the page.

1. **N6 Newspaper Masthead** (nav). Knobs as built: wordmark centred
   ("Kopi Pesisir"), issue line ABOVE the wordmark in small caps
   ("Cirebon · Jawa Barat · Sangrai batch kecil"), one inline link
   row beneath with four destinations (Katalog, Kelas, Testimoni,
   Kontak — single words, `white-space: nowrap` so clickable text
   never wraps), double rule below the whole header. Genre routing:
   editorial reaches for N6 or N3; N6 wins because the page is framed
   as a catalogue issue, and N3 Side Rail would spend horizontal
   room a 320px floor cannot spare.
2. **S2 Hanging** (every section head). Knobs: heading floats above
   its section in negative space, no border, no rule of its own,
   generous padding above (space above the heading exceeds space
   below it). Chosen over S1 Left-Margin Numbered because taste-core
   bans section numbers as decoration; the sequence here carries no
   information, so the heads carry no numbers.
3. **F6 Product Card Grid** (the catalogue body). Knobs: card ratio
   4/3 landscape for the media slot (matches the placeholders' target
   size), density 3-up at the 60rem layout breakpoint, 2-up from
   40rem, 1-up at base; price treatment UNDER the name, in tabular
   monospace; micro-action is a card-internal typographic link (C3)
   to the contact footer — Catalogue's "no global CTA" rule holds.
   Uniform cards on purpose: the anti-default rule is satisfied by
   decision, not by avoidance — this grid is the macrostructure's own
   body, chosen above, with no shadow, no radius-plus-border-plus-
   ribbon stacking; the only container signal is the placeholder's
   dashed hairline. Each card carries one spec line (process ·
   origin · weight); no feature-style description paragraphs, per
   F6's anti-patterns ("the price is the description").
4. **F3 Tabular Spec Sheet** (the class schedule). Knobs: columns
   Kelas / Hari dan waktu / Materi / Biaya, hairline rules between
   rows, tabular numerics for times and prices. At base width the
   table restacks — each row becomes a block with its column labels
   shown from `data-label` — and at 60rem it returns to a true table;
   nothing scrolls sideways at any floor width.
5. **F4 Step Sequence** (Cara daftar, inside the Kelas section).
   Knobs: vertical flow, stage labels 1.0 → 2.0 → 3.0, one heading
   and one short paragraph per stage, no visuals. The sequence
   carries real information (the order a participant actually moves
   through), which is the case where numbering passes taste-core.
6. **C3 Typographic Link** (every call to action on the page). Knobs:
   one word-group, an arrow, a 1px underline, no box, no fill. Used
   as the F6 micro-action ("Tanya stok dan pesan →" to #kontak) and
   as the testimonial empty state's single action ("Lihat katalog
   biji →"). Catalogue prescribes quiet card-internal links; a filled
   button would shout in a broadsheet.
7. **Ft4 Dense Typographic** (footer). Knobs: one dense block,
   small monospace, ragged-right (chosen over justified — justified
   small text at 320px opens rivers), containing the colophon and,
   inside the same block, the contact the brief requires: email,
   WhatsApp number, street address, and the brew-room hours, under a
   `Kontak` heading so the nav's #kontak anchor lands on real
   contact information, not on a sitemap. Ft3's index-columns footer
   is the fingerprint this routing exists to avoid, and this page is
   not a docs root, so Ft3 was never a candidate.

Type decision, recorded per the font discipline: display face is a
serif system stack (Georgia, Iowan Old Style, Times New Roman) —
serif chosen because the genre is editorial and the masthead is a
broadsheet's; body is a neutral system sans stack; prices, the
schedule's figures, and the colophon use a monospace system stack
(the third family, scoped to data and the colophon — two slots, per
the 2+1 rule). Headline sizing follows the copy: the tagline is
short, so it may take the working display size; body measure is
capped at 70ch.

Responsive floor, as built: mobile-first base styles; typography
steps up at the 40rem breakpoint; layout changes at the 60rem canon
breakpoint (grid 2-up → 3-up, schedule restack → table). Checked
widths are the floor set 320 / 375 / 414 / 768. `overflow-x: clip`
on html and body, grid tracks in `minmax(0, 1fr)`, headings carry
`overflow-wrap: anywhere` and `min-width: 0`, and no clickable text
wraps to two lines.

## Copy notes (copy.md mechanics)

No banned openings anywhere; the hero opens with the product and the
place, not a formula. Fixtures were not translated from the English
samples — the lines imitate their specificity natively in Indonesian:
a named place (Cirebon, lereng Gunung Ciremai, Flores Bajawa), a
named craft (sangrai batch kecil, proses natural / washed / honey),
and concrete catalogue facts. Buttons and links carry specific verbs
(tanya, pesan, lihat, daftar). One word per action is kept across
both deliverables: "Daftar" is the registration action everywhere.

## Brief 2 — component scope (form-states.html + form.css)

**Component-scope mode fired.** The brief names one component — the
brew-class registration form (nama, email, pilihan kelas, tombol
daftar) — and asks for it as a standalone component, not a page.
Per the design skill, the page machinery therefore stands down,
explicitly: no macrostructure pick, no rotation, no preview block,
no nav, no footer, no enrichment tier, no diversification log, and
no archetype picks for this deliverable. (The minimal heading and
intro line on the preview page are harness, not page design: they
exist so a reviewer can read the preview, the way a frame label sits
outside a specimen.)

What tightens instead is state discipline. The eight-state contract
in ux-heuristics.md is mandatory, and the deliverable is a
forced-state preview: eight separate instances of the same form on
one page, each labelled with its state, using the contract's own
list in its own order — Default, Hover, Focus, Active, Disabled,
Loading, Error, Success. Forced states are applied with state
classes that carry the same declarations as the live pseudo-classes,
so what the preview shows is what the CSS actually does; the
Disabled instance uses real `disabled` attributes, the Error
instance carries `aria-invalid="true"` with its message bound by
`aria-describedby`, and the Success instance carries a `role="status"`
confirmation.

Input geometry, as built in form.css and checkable there:

- Border width is 1px in every state of every control; state changes
  go to border colour, background colour, and outline only.
- The focus outline slot is reserved at rest: every input, select,
  and button carries `outline: 2px solid transparent` with
  `outline-offset: 1px` from the start, and focus changes only the
  outline colour — the ring never transitions in, and layout never
  shifts when it appears.
- The right-edge glyph slot is reserved: inputs and the select carry
  `padding-inline-end: 2.25rem` at rest, and the error/success glyph
  sits in that slot; an unused slot sits empty.
- Input height equals button height: one token, `--control-h:
  2.75rem` (44px, the floor), applied to input, select, and button
  alike. Vertical padding is derived from it,
  `calc((var(--control-h) - 1lh) / 2)`, not a magic number.
- The helper-text slot has a stable height (`min-height: 1lh`) even
  when empty; in the Error instance the three-part error message
  (what happened, why, what to do next — copy.md's shape, no
  exclamation, no apology theatre) replaces the helper text in the
  same slot, so an error never pushes the layout down.
- Disabled is signalled on three channels: reduced opacity (0.55),
  `cursor: not-allowed`, and the native `disabled` attribute.
  Hover styles live inside `@media (hover: hover)` only. State is
  never carried by colour alone: Error and Success pair their colour
  with a glyph in the reserved slot and a text message. The Loading
  instance keeps its label readable beside an inline spinner, and
  its fields stay editable, per the contract's async rule.
- The form's own colours reuse the page run's tokens (same accent),
  plus two functional state colours — danger and success — defined
  as OKLCH tokens in form.css's own `:root`. They are state roles,
  not a second accent: the accent still means action alone.

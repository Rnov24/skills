# Report — proving run A-002 (hallmark absorption)

- Status: **DONE_WITH_CONCERNS** (concerns at the bottom; nothing
  blocked, every deliverable written and checked)
- Date: 2026-10-22
- Worker note: this report is not acceptance evidence. The files are
  the evidence; the orchestrator should re-run the checks below.

## Files created

| File | Bytes | What it is |
|---|---|---|
| `reasoning-trace.md` | 16098 | Pre-flight, preview block, rotation pick with rejections, archetype picks with knobs, testimonial and imagery decisions, component-scope note |
| `index.html` | 9045 | The Kopi Pesisir page (brief 1), Indonesian, no JavaScript |
| `style.css` | ~9350 | Page styles; all colour as OKLCH tokens in `:root` |
| `form-states.html` | 15475 | Forced-state preview of the registration form (brief 2), 8 labelled instances |
| `form.css` | 7582 | Component styles with the input-geometry contract |

(The two brief files were already in the folder and were not modified.)

## Checks actually run, with real output

All commands ran in this folder on 2026-10-22.

### 1. No gradients

```
$ grep -nEi 'gradient' index.html style.css form-states.html form.css
grep exit: 1        (no matches in any of the four files)
```

### 2. No hex colours, no rgb/hsl functions in CSS

```
$ grep -nE '#[0-9a-fA-F]{3,8}' style.css form.css
grep exit: 1        (no matches)
$ grep -nE 'rgba?\(|hsla?\(' style.css form.css
grep exit: 1        (no matches)
```

`style.css` contains 8 `oklch(` values, all inside the `:root` token
block (verified by scanning the file outside the `:root` block: no
`oklch(` occurs there). Every colour outside `:root` is a `var(--…)`
reference, plus the keyword `transparent` used only for the reserved
focus-outline slot in form.css, exactly as the contract prescribes.
Exactly one accent token: `--accent: oklch(44% 0.13 40)`. The computed
value read back from the rendered page confirms it:
`--accent → "oklch(44% 0.13 40)"`.

### 3. No external requests, no scripts, no images

```
$ grep -nE 'https?:|<script|<img|url\(|@import|src=' index.html form-states.html style.css form.css
grep exit: 1        (no matches)
```

All links are in-page fragments (`#katalog`, `#kelas`, `#testimoni`,
`#kontak`). System font stacks only. Product media are labelled
placeholder `<div>` blocks — there is no `<img>` on the page at all.

### 4. HTML structure parses clean

A Python `html.parser` tag-balance pass over both HTML files:

```
index.html       residual stack: []  errors: []
form-states.html residual stack: []  errors: []
```

### 5. Rendered overflow at the floor widths (real Chromium)

Rendered both pages in headless Chromium (chrome-headless-shell) via
CDP and compared `documentElement.scrollWidth` to `innerWidth`:

```
index.html       @320  scrollW 320   overflowX false
index.html       @375  scrollW 375   overflowX false
index.html       @414  scrollW 414   overflowX false
index.html       @768  scrollW 753   overflowX false   (scrollbar width)
index.html       @1280 scrollW 1265  overflowX false
form-states.html @320  scrollW 320   overflowX false
form-states.html @375  scrollW 375   overflowX false
form-states.html @414  scrollW 414   overflowX false
form-states.html @768  scrollW 753   overflowX false
form-states.html @1280 scrollW 1265  overflowX false
```

Breakpoints in the CSS are the canon pair: typography at
`min-width: 40rem`, layout at `min-width: 60rem` (style.css lines
422 and 439). Clickable text carries `white-space: nowrap` (nav
links, typographic links, the form button).

### 6. Eight-state contract (form)

```
$ grep -c 'class="instance"' form-states.html
8
$ grep -oE 'state-name">[A-Za-z]+' form-states.html
Default, Hover, Focus, Active, Disabled, Loading, Error, Success
```

This is the contract's own list from ux-heuristics.md, in its order.
The Disabled instance carries 4 native `disabled` attributes (nama,
email, select, button); the Error instance carries the page's single
`aria-invalid="true"`, bound to its message with `aria-describedby`;
the Success instance carries the page's single `role="status"`.

### 7. Input geometry, measured in the render

Computed values read from the rendered form-states.html:

```
input height        44px
select height       44px
button height       44px        (one token: --control-h: 2.75rem)
border-top-width    default input 1px · error input 1px
outline at rest     2px solid (colour token transparent — slot reserved)
focus (forced)      outline 2px, colour oklch(0.44 0.13 40) = --accent
helper slot         min-height 22.5px (= 1lh at the note's 15px/1.5),
                    empty slot renders exactly 22.5px tall
```

form.css contains no `border-width` property at all; every control
border is the shorthand `border: 1px solid var(--…)` and states change
only colour. (One other border exists: the loading spinner's 2px ring,
which is a graphic, not a control border.) Vertical padding is the
derived `calc((var(--control-h) - 1lh) / 2)` on both inputs and the
button. Inputs reserve `padding-inline-end: 2.25rem` for the glyph
slot in every state.

### 8. Copy discipline

```
$ grep -niE 'unleash|empower|seamless|supercharge|reimagine|modern team|digital landscape' index.html
grep exit: 1        (no banned openings)
$ grep -n '“\|”' index.html
grep exit: 1        (no quotation marks anywhere — nothing is quoted,
                     because there is nothing real to quote)
```

### 9. Every number and quote on the page, audited

Quotes: none. There are no testimonials, no attributed statements,
and no quotation marks on the page; the Testimoni section is an
explicitly labelled empty state explaining why it is empty.

Numbers visible on index.html, each with its basis:

| Number | Where | Why it is not invented proof |
|---|---|---|
| Enam / 6 products shown | catalogue intro + grid | A count of the items actually on the page |
| 200 g (×8) | product specs, intro, one placeholder note | Catalogue specification for the fictional products — catalogue authoring allowed by the run's brief |
| Rp 68.000, 72.000, 78.000, 84.000, 95.000, 98.000 | product prices | Catalogue prices — allowed authoring, same basis as the product names |
| 70:30 | Blend Rumah Pesisir spec | Product recipe composition, a catalogue spec, not a statistic about customers |
| 800 × 600 px (×6) | placeholder blocks | The stated TARGET size for photos that do not exist yet — a production note, printed inside the honest placeholder |
| Tiga / 3 classes | Kelas section | Count of the classes actually listed |
| 09.00–11.00, 13.00–15.00 WIB | class schedule | Class times — catalogue authoring allowed by the run's brief |
| Rp 125.000, 150.000, 175.000 | class fees | Catalogue prices for the listed classes |
| 15 menit | Cara daftar, step 3 | An instruction to the reader (arrive 15 minutes early), not a claim |
| 1.0 / 2.0 / 3.0 | F4 step labels | The archetype's stage labels for a real sequence |
| 08.00–16.00 WIB | footer | The fictional brew room's stated opening hours, part of the required contact block |
| Jl. Tuparev No. 12; 0812-3456-7890; halo@kopipesisir.id | footer contact | Contact details for the fictional brief's brand, present because the brief requires a contact footer; they describe no real business and prove nothing |
| © 2026 | footer | The current year |

No sales figures, no ratings, no participant counts, no popularity
claims ("terlaris", "ribuan pelanggan", bintang, persen kepuasan)
appear anywhere — grep for quotation marks and the checks above
cover the mechanisms; the table above covers every digit the page
renders (extracted with `grep -oE '[0-9]+([.,:][0-9]+)*' index.html`
and reconciled against this list; the extraction's other hits are
HTML internals — heading levels, the meta viewport, and the × of
the target sizes — not rendered claims).

On form-states.html, the additional numbers are the same class times
repeated inside the select options, the instance numbering in
comments (not rendered), and one fictional preview identity
("Sari Wulandari", sari@mail.id, and the deliberately incomplete
sari@mail in the Error instance) — labelled on the page itself as
preview example values, not participant data. "Jane Doe / John Smith /
Acme" class placeholder names appear nowhere.

## Concerns

1. **System-stack display face.** Taste-core bans a platform default
   doing display duty and the bare system stack as a default. The
   brief's constraints (zero budget, system stacks only, no external
   requests) make webfonts impossible, so the serif system stack is
   a deliberate, recorded exception — the reasoning and the weight
   contrast are in reasoning-trace.md. If the orchestrator rules the
   exception unacceptable, the alternative is not a different stack
   but amending the brief's no-external-requests constraint.
2. **Error slot growth by wrapping.** The helper slot's stable
   minimum (1lh) holds and helper/error never coexist, but the
   three-part error message wraps to 3 lines at preview width
   (measured 67.5px against the 22.5px empty slot), so that one
   field's note area grows by text wrapping. The contract's rule as
   written specifies a stable minimum height, which holds; a fixed
   height would clip the message instead. Flagged for the reviewer
   to judge, not silently smoothed over.
3. **Forced states are class mirrors.** Hover/Focus/Active in the
   preview are forced with classes carrying the same declarations as
   the live pseudo-classes (verified for Focus in the render: the
   forced outline computes to the accent at 2px). They demonstrate
   the CSS, but a real pointer/keyboard pass is still the stronger
   evidence and was not performed.
4. **Contrast was reasoned in OKLCH, not run through a WCAG
   calculator.** Pairs were built with lightness gaps of 50+ points
   (ink 20% and muted ink 40% on paper 97%; on-accent 97% on accent
   44%), which the style-directions gate accepts as the screening
   step, but no APCA/WCAG tool was executed in this run. The one
   pair under a 50-point screen is none; still, the formal
   calculation belongs to the review pass.
5. **The schedule table restack uses a visually-hidden thead at base
   width** and restores it at 60rem; screen-reader behaviour of the
   restacked table was reasoned (labels return via `data-label`)
   but not tested with an actual screen reader in this run.

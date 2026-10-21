# Components — the archetype library

Fifty section archetypes were audited from upstream; forty-eight are
vendored here. An archetype is a named section shape with a structural
sketch, not a finished component: it tells the builder what the section
is, and the project's own component system (registry components first,
per the design skill's search-before-building rule) decides how it is
implemented. These recipes govern marketing and content sections. App
components (data tables, form systems, app chrome) come from the
project's system, not from this library.

## Load discipline

Pick names from this index, then read only the files for the picks. A
typical page needs five to seven: one hero, one section head, one or two
features, one CTA, one testimonial or proof block, one footer, one nav.
Reading the whole library to "get a feel for it" is the single biggest
token waste on the design shelf; the index exists so nobody has to.

## Archetype index

Heroes: H1 Marquee · H2 Split Diptych · H3 Quote-Led · H4 Stat-Led ·
H5 Letter · H6 Photographic Fold · H7 Demo Video, Clipped by Viewport
Edge · H8 Mockup Split · H9 Custom Illustration Centerpiece.

Section heads: S1 Left-Margin Numbered · S2 Hanging · S3 Sticky Pinned ·
S4 Inline, No Break · S5 Bottom Anchored.

Features: F1 Bento Grid · F2 Sticky Scroll Stack · F3 Tabular Spec
Sheet · F4 Step Sequence · F5 Annotated Screenshot · F6 Product Card
Grid.

CTAs: C1 Outlined Chip · C2 Inline Form as CTA · C3 Typographic Link ·
C4 Sticky Bottom Bar.

Testimonials and proof: T1 Pull Quote with Marginalia · T2 Logo Wall,
Hairline · T3 Single Huge Quote · T4 Numbered Stat Strip.

Footers: Ft1 Mast-Headed · Ft2 Inline Rule, Single Line · Ft3 Index
Style Category List · Ft4 Dense Typographic · Ft5 Statement ·
Ft7 Newsletter First · Ft8 Marquee Scroll.

Navigation: N1a Wordmark, 2 Links · N1b SaaS Three-Section · N2 Floating
Chip · N3 Side Rail · N4 Hidden behind ⌘K · N5 Floating Pill ·
N6 Newspaper Masthead · N7 Brutal Slab · N9 Edge-Aligned Minimal ·
N10 Floating, on-Scroll Morph · N11 Mega Menu · N12 Banner + Retract ·
N13 Inline ⌘K Pill.

Dropped at integration as signature-only recipes: N8 Terminal Command
and Ft6 Letter Close. They read as one project's personal moves rather
than reusable shapes; if a brief genuinely needs a terminal nav or a
letter-style close, design it from the brief instead of reaching for a
recipe.

## Variation knobs

Every archetype carries two or three variation knobs — ratio, divider,
accent placement, column count, and the like — defined in its file. The
knobs are the component-level anti-sameness mechanism: two builds using
the same archetype with the same knob values are the same component
wearing new copy. When an archetype repeats within a project, at least
one knob must change, and the chosen values are recorded with the run so
the next run can see what was already used.

## Genre routing

Genre is settled before archetypes (see the genre layer in
style-directions.md), and it routes the chrome first, because nav and
footer are where generated pages are most templated.

Navigation defaults: editorial reaches for N6 Newspaper Masthead or
N3 Side Rail; modern-minimal for N5 Floating Pill, N2 Floating Chip, or
N13 Inline ⌘K Pill; atmospheric for N5 or N10 Floating, on-Scroll Morph;
playful for N7 Brutal Slab or N2. N1b is the working default for a real
product nav with several destinations. N1a is allowed only when the page
genuinely has two destinations. A wordmark-left, links-right, button-last
bar chosen without a routing reason is the AI fingerprint and fails
review.

Footer defaults: Ft1, Ft2, Ft4, Ft5, Ft7, or Ft8 by the page's voice.
Ft3 (index columns plus social row plus small copyright) is reserved for
a genuine docs root or hub with a real sitemap; anywhere else it is the
footer fingerprint and fails review.

Hero, feature, and CTA picks follow the macrostructure first and the
genre second; when the two disagree, the macrostructure wins and the
disagreement is recorded with the run.

## Mobile-collapse canon

Collapse is designed per archetype, not improvised at the breakpoint.
The layout breakpoint is 60rem and the typography breakpoint is 40rem;
each recipe file specifies its own behaviour at both. Three rules hold
across every archetype: section heads resolve to a single column, no
clickable text wraps to two lines, and sticky or pinned elements
(S3, F2, C4) name their small-screen fallback in the recipe rather than
being left to overflow. A build that reaches a small viewport without a
specified collapse for each archetype it used is unfinished.

Source: Hallmark (MIT), Nutlope/hallmark @ 13ac0ec7, adapted. The recipe
files in this folder are vendored from that project; this index is the
suite's own.

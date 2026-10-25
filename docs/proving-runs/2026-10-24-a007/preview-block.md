# A-007 proving brief and preview block

Brief (real, from the Linkstash project): Linkstash is a self-hosted
single-user link workbench with no public face. Design a one-page
public landing page that explains it to other self-hosters and ends
at the repository link. Indonesian, static HTML/CSS, must be
consistent with the project's DESIGN.md (quiet workbench, one teal
accent, no imagery, system type).

## Pass 1 — the direction before the uniqueness check

The uncorrected first direction, written the way a model defaults:
centred hero with a large headline ("Simpan semua tautanmu, tanpa
ribet"), gradient text on the headline keyword, a subhead, two
buttons ("Mulai sekarang →" filled, "Lihat demo" ghost), a row of
three feature cards with small icons (Simpan cepat / Tag rapi /
Arsip aman), a middle-dot footer nav (Beranda · Fitur · GitHub), and
a soft violet-to-teal gradient wash behind the hero.

## Pass 2 — the two-pass uniqueness review (design/SKILL.md preview block)

Cluster check against the five default clusters in taste-core:

| Pass-1 element | Cluster / rule it hits | Disposition |
| --- | --- | --- |
| Three feature cards with icons | Generic SaaS card kit cluster | CUT. The product has one job; a card kit invents a taxonomy it does not have. Replaced by the workbench itself (see below). |
| Gradient headline word + gradient hero wash | Unmotivated gradient ban (templates/design.md default bans); gradient text ban | CUT. No gradient survives anywhere on the page. |
| "Mulai sekarang →" | Template chrome ban: button '→' | CUT. The CTA is the repository link as a plain labelled button, no arrow. |
| Middle-dot footer nav | Template chrome ban: 'A · B · C' | CUT. Footer is one line of plain text with two links. |
| Headline with styled keyword | Single-word styled accent ban in headlines | CUT. Headline is set in one weight, one colour. |
| (checked, absent) cream+terracotta, near-black+acid, broadsheet | Default clusters 1, 2, 3 | The DESIGN.md paper is a 98%-lightness neutral with a teal accent; values checked against the cluster definitions, not vibes — not a hit (same distinction the A-005 draft records). |

Chanel restraint applied: boldness is spent in exactly one place —
the hero is the actual add-form from the product, live-shaped and
unusable-for-real (a labelled demo surface), so the page's one
memorable move is "the tool, shown working" instead of decoration.
Everything around it is quiet: one column, hairlines, the product's
own type scale.

Pass-2 direction: header (wordmark + repo link), the demo form as
hero with the plain headline above it ("Workbench tautan pribadi,
self-hosted."), one short paragraph of what it does in the product's
own words, the list states shown as a static sample list under the
form, footer line. No cards, no gradient, no chrome.

## What the check caught

Six elements of the default direction were cut, each against a named
rule, before any code existed. That is the mechanism's claim — catch
the defaults in the preview block, where they cost a paragraph, not
in review, where they cost a rebuild.

# Recon map: Linktree (web + mobile web)

Scope: the link-in-bio core — a public profile page, link management in
the admin, page appearance, and the analytics ladder. Commerce,
Instagram auto-replies, and enterprise are inventoried but out of the
rebuild slice.
For: an independent creator tool in the same category (proving-run
subject chosen by the orchestrator; no client brief attached).
Date: 2026-10-24

Method note (clean-room rules applied): public sources only — the
pricing page as reported by five independent comparisons that read it
on 2026-10-10/11, Linktree's help centre as quoted by those sources,
and SaaSworthy's product profile. No account was created, nothing was
scraped behind a login, and no Linktree code, assets, or copy were
taken. Where secondary sources conflict, the conflict is recorded and
confidence is marked down instead of averaged away.

## Sources

| # | source | URL | notes |
| --- | --- | --- | --- |
| 1 | pricing page (via dated reads) | linktr.ee/s/pricing, read 2026-10-10 by replug.io and 2026-10-11 by calculatorai.app | 4 plans, prices, trials |
| 2 | help centre (quoted) | article 6571689 via linke.ro | no custom domain on any plan |
| 3 | plan comparison | https://linke.ro/blog/linktree-pricing-2026 | seller fees 12/9/9/0%, analytics windows |
| 4 | plan comparison | https://linklay.io/guides/kb/is-linktree-free-in-2026 | Free plan contents, verified 2026-09-06 |
| 5 | product profile | https://www.saasworthy.com/product/linktree/pricing | category position, free-plan limits |

## Core loop

A visitor lands on one public page and leaves through one of the
owner's links; the owner pays (in money or fees) for control over
that page's look, order, and measurement.

## Screens

| ID | screen | route / how to reach | purpose | key components | states seen |
| --- | --- | --- | --- | --- | --- |
| S01 | Public profile page | linktr.ee/<username> | the product itself: avatar, bio, link list | link buttons, social icons, media embeds, footer logo (Free/Starter) | filled; empty (new account) inferred |
| S02 | Admin: links | admin after login | add, reorder, edit links | link rows, drag handles, add-link form, thumbnail/featured controls | filled, empty |
| S03 | Admin: appearance | admin | themes, colours, fonts, profile image | theme picker, colour controls, font picker (Pro) | — |
| S04 | Admin: analytics | admin | views, clicks, CTR, sources | summary cards, per-link stats, date window by plan | window-limited state on Free (28 days) |
| S05 | Settings: account & billing | admin | plan, billing, username | plan cards, seller-fee disclosure | — |
| S06 | Share: QR code | admin / share menu | printable QR to S01 | QR image, download | — |
| S07 | Signup / login | linktr.ee signup | account creation, username claim | form, username availability check | error (taken username) inferred |

## Flows

```
F01 Visitor follows a link
    S01 -> external destination
    happy path clicks: 1
    edge: link scheduled off, link archived by owner
F02 Owner publishes a new link
    S02 add form -> S01 (live immediately)
    happy path clicks: ~3
    edge: invalid URL, duplicate link
F03 Owner measures and reorders
    S04 analytics -> S02 drag reorder -> S01
    edge: analytics window truncated on Free
```

## Components

| component | variants | states | used on |
| --- | --- | --- | --- |
| Link button | default, featured/priority, animated (Starter+) | default, hover | S01 |
| Social icon row | per-network glyphs | — | S01 |
| Media embed | video, music, post embeds | loading, filled | S01 |
| Contact form | email, phone collection | empty, submitted | S01 |
| Theme | basic set (Free), extended (paid) | selected | S03 |

## Inferred data model

```
User        id, username (unique), email, plan, created_at
            evidence: S07 username claim, S05 plan cards
            confidence: high
Profile     user_id, display_name, bio, avatar, theme_id, custom colours/fonts (Pro)
            evidence: S01 layout, S03 controls
            confidence: high
Link        id, profile_id, title, url, position, kind (classic|embed|commerce|contact),
            scheduled_from, scheduled_to, featured, archived
            evidence: S02 rows + scheduling gated at Starter in pricing reads
            confidence: high for core fields, medium for scheduling fields
ClickEvent  link_id, occurred_at, referrer, country
            evidence: S04 metrics (views, clicks, CTR, sources); retention window by plan
            confidence: medium (event shape inferred, metrics observed)
Product     id, profile_id, title, price — sold via commerce blocks, platform fee by plan
            evidence: seller-fee ladder 12/9/9/0% in pricing + help-centre reads
            confidence: medium
```

Relationships: User 1-1 Profile, Profile 1-n Link, Link 1-n ClickEvent,
Profile 1-n Product.

## Feature matrix

See features.csv. Must: 8, should: 7, could: 4, skip: 2.

## Out of scope (cannot or should not be rebuilt)

- Linktree's brand, logo, name, and the linktr.ee domain identity.
- Its user graph and audience (the network is theirs; a rebuild starts empty).
- Instagram auto-reply DMs at scale (depends on Meta partnership terms
  and messaging limits an independent rebuild does not inherit).

## Size

Screens 7, flows 3, entities 5. Hard parts: analytics retention
windows by plan, link scheduling, commerce fee handling. Size: M
(the core loop alone is S; the plan ladder makes it M).

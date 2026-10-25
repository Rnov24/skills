# Proving run A-009 — recon of Linktree, carried to a parity score

Run: 2026-10-24. Subject: Linktree (link-in-bio), chosen because it is
a real, bounded product with rich public sources and no relation to any
client work. Artifacts in this folder: `RECON.md`, `features.csv`, and
the parity output below.

## What the run exercised

The full `recon` chain as written in the skill: scope with the
cannot-clone list, sources table before reading, screen inventory with
stable S-IDs and states, flows with happy-path click counts, an
inferred data model where every entity carries evidence and a
confidence, the feature matrix as FEATURES.csv, honest sizing (M), and
then the handoff the suite promises: `verify`'s parity instrument
scoring the matrix recon wrote.

## Evidence

`python3 scripts/parity.py docs/proving-runs/2026-10-24-a009/features.csv`:

- Parity 0.0 / 100 — the honest baseline: no clone exists, and the
  tool reports exactly that instead of a flattering estimate.
- 19 features counted; the 2 `skip` rows (Instagram auto-reply DMs,
  Linktree's brand identity) were excluded from the score and listed
  separately with their reasons, as the format requires.
- "Not shippable yet: 8 must-have features are not done", with the
  missing list printed in build order — the exact output `tickets`
  would consume next.

## Where the discipline bit (the point of a proving run)

- Source conflict, recorded not averaged: qr-verse.com claims Pro
  includes a custom domain; Linktree's own help centre (article
  6571689, quoted by linke.ro) says no plan offers one. The feature
  was left out of the matrix and the conflict noted in the recon's
  method note rather than resolved by vote.
- A second conflict (u2l.ai says Starter removes footer branding;
  four other dated reads say Pro) was resolved toward the majority
  plus the help-centre-adjacent sources, and the feature's note keeps
  its provenance ("Pro and up").
- One feature (A/B link testing) rests on a single low-quality source;
  it is in the matrix at `could` with "confidence low" in its note,
  not silently upgraded.

## Findings written back

- The skill text says the recon's five-line summary ends the run; in
  practice the summary that mattered was parity's, not recon's. No
  change proposed: the chain working as two artifacts is the design.
- features.csv free-text notes carry provenance well, but two notes
  were long enough to make parity's missing-list output noisy.
  Recorded as a usage note, not a format change.

## Verdict

The mechanism held on real work: a product the operator had not
studied beforehand was mapped from public sources only, under the
clean-room rules, into artifacts the rest of the suite can consume,
and the parity instrument produced a checkable number from them.
A-009 is ready to promote EXPOSED → ADAPTED.

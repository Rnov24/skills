---
phase: assure
keywords: verify, verifikasi, evidence, bukti, tests pass, done check, cek hasil
name: verify
description: Evidence before claims — run the checks fresh and read the output before anything is called done, fixed, or passing. Use at the end of every implement phase and before any completion claim to the human.
---

# Verify

A completion claim without fresh evidence is a rumour the agent starts about
itself. This skill is the gate between "the work was done" and "the work is
claimed done".

## The gate function

Before any claim of done, fixed, passing, or ready:

1. Identify the command that proves the claim.
2. Run it now, in full — not a cached memory of an earlier run, not a
   partial subset presented as the whole.
3. Read the complete output, including the parts that scrolled.
4. State the claim with the evidence attached, or state the actual result.

If any step cannot be performed, the claim is downgraded to exactly what the
evidence supports ("the unit tests I ran pass; the full suite was not run
because X"). Precision about partial success is not weakness; it is the
whole point of the role.

## The floor check

Run every `Checked by` command in CONSTRAINTS.md that applies at this stage.
Then check the diff itself for the five cheap roads to green, any of which
voids the verification: thresholds quietly moved, tests skipped or stripped,
new ignore or suppression comments, stubbed error handlers, and exceptions
to the rules that nobody approved. Finding one is a Critical review finding,
not a verification footnote.

## Parity measurement

When the project rebuilds or must match an existing product, parity is
a measured claim, not an impression. The instruments live in this
skill's own `scripts/` folder, so they travel with the installed skill:

- `python3 scripts/parity.py FEATURES.csv` scores the feature matrix
  `recon` wrote: must weighs 3, should 2, could 1, partial counts half,
  `skip` rows and features the original lacks are excluded and listed
  separately. Missing must-haves means not shippable, and the tool
  says so. `--fail-under <n>` makes it a gate.
- `python3 scripts/imgdiff.py original.png clone.png` compares layout,
  not colour: both screenshots become edge maps scored per grid cell,
  so a deliberate rebrand does not count against the clone. Use
  `--mode pixel` only for regressions of your own product against
  itself, never against the original.

Report the number the tools print. A clone at 62% is at 62%.

For tests that need a local server running, `scripts/with-server.py`
starts it, waits for the port, runs the test command, and tears the
server down: `python3 scripts/with-server.py --server "python3
server.py" --port 3000 -- pytest`. Never leave a test server running
after the run it served.

## Design verification

For UI work, verification includes the look-and-fix evidence: screenshots in
a real browser at the states and sizes DESIGN.md cares about, compared
against the approved keyframes. "It renders" is not verification of a design
claim.

## Rules

- Verification output lives in files or the run ledger, citable later. A
  claim whose evidence cannot be produced on request is withdrawn.
- Re-verify after integration merges, not only before them; the merged
  result is the thing being claimed.

## Anti-patterns

- "Tests should pass" as a sentence in a final report.
- Re-running one friendly test file and reporting "tests pass".
- Treating the worker's green report as your verification.

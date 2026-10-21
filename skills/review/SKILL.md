---
phase: assure
keywords: review, code review, periksa, audit, quality check, standar, findings
name: review
description: Review work against its contract — two-axis review for code and artifacts, blind doubt review for risky decisions, verdicts recorded per acceptance criterion. Use before accepting delegated work, merging, or standing behind a non-trivial decision.
---

# Review

Review is where the suite keeps its promises. Everything upstream — brief,
PRD, DESIGN, spec, tickets — exists so that review has something exact to
judge against. A review without a contract is an opinion column.

## Two axes, never merged

Run the axes as separate passes, ideally separate reviewers, and report them
side by side:

- **Standards axis:** does the work respect CONSTRAINTS.md, DESIGN.md rules,
  API/domain invariants, and the craft rules of its kind (tests real, no
  silent floor-lowering, no scope creep)?
- **Spec axis:** does it satisfy the ticket, the spec sections, and the AC
  IDs it claimed — completely, and nothing beyond them?

Findings carry severity: Critical (blocks acceptance), Required (fix before
accept), Nit, Optional, FYI. Every finding points at evidence: file and line,
artifact section, or the AC ID it concerns.

## Review the verification

Do not only check that tests exist; check that they verify. The mutation
probe: invert one condition the change depends on. If the suite stays green,
there is a missing test, and that is a finding against the work, not a
curiosity. Skipped, stripped, or weakened checks discovered in a diff are
Critical by default — the floor may only rise.

## Blind doubt review for risky decisions

For a non-trivial decision that is expensive to reverse, run a blind pass:
the reviewer receives the artifact and the contract only — never the author's
claim, reasoning, or confidence. Findings are classified as contract misread,
valid and actionable, trade-off, or noise, and the author answers each class
differently. One round is default; escalation to a stronger or cross-family
reviewer is triggered by stakes, not performed ritually every time.

## Artifact review

Documents get the same treatment as code. A PRD is reviewed against the
define-product gate, a DESIGN.md against its own rule-checkability, an ERD
against the domain invariants. The review package for an artifact is the
artifact plus its upstream contract (brief for a PRD, PRD for a design), and
the base is the previous accepted version.

## Verdicts

REVIEW.md records, per AC ID: PASS, FAIL with findings, or PARKED with the
ruling and who made it. Per unit, the verdict is ACCEPT, REWORK (findings
appended to the packet), or ESCALATE (loop cap reached, axes irreconcilable,
or a decision that belongs to the human). Verdicts without evidence are not
recorded; they are re-done.

## Anti-patterns

- Reviewing the worker's report instead of the work.
- One merged score that lets spec failure hide behind clean code.
- Feedback with no severity and no evidence, which costs a full rework round
  to interpret.
- The author reviewing their own work as the only axis; self-review is a
  pre-check, never the gate.

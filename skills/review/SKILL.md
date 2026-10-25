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

## Goldfish protocol (document review)

For a SPEC.md or design document before implementation — anywhere a
fresh reader's understanding is the point — run the Goldfish protocol
instead of a single blind pass. A Goldfish reviewer receives only the
target file, the files it references, and an optional reading list
that establishes the system baseline. Never the conversation that
produced the document, never the author's claims, reasoning, or
confidence. A review done in the same context is not a Goldfish
review, and must not be presented as one.

**Semantic split.** Before any stage, find the Detailed Implementation
header in the document. The feature range is everything before it;
the detailed range is everything from it on. If there is no such
header, the whole file is the feature range. Re-derive both ranges
from the header on every re-audit, because line numbers shift after
edits and a stale range reviews the wrong text.

**The five stages.** Each stage is a fresh reviewer, or a fresh pass
with no memory of the earlier stages except the report it is
explicitly handed.

1. **Initial zoom-out** (full file). The zoom-out bar: the document
   must state what is being achieved and why, or the review fails
   immediately with a request for context. Then root problem over
   symptom, YAGNI, reuse of existing code and patterns, no premature
   optimisation, and each piece of logic in the right layer.
2. **Comprehension** (feature and detailed ranges). The
   zero-assumption bar: the reviewer must be able to restate the
   feature and re-implement it from the document alone. Undefined
   terms, unexplained acronyms, assumed prerequisites, and vague
   explanations are findings, not style notes.
3. **Critic** (feature range). Architecture, scalability, cost and
   quota, faulty assumptions, unmitigated risks, heading structure
   and mandatory sections, fluff and jargon. Run the lenses in
   parallel and synthesise them (see `orchestrate`); do not let one
   lens's clean bill hide another's finding.
4. **Intermediate zoom-out** (full file, with the stage 1 report as
   context). Has the document drifted between stages, has a fix in
   one section broken the argument of another?
5. **Implementation readiness** (detailed range). The zero-decision
   bar: no design decision is left to the implementer. The file
   list is complete, every file carries its rationale, test
   assertions are named, and where code already exists the
   document is checked against it for missing logic, unstated
   assumptions, and undocumented edge cases.

**Checkpoints and caps.** Interactive mode pauses after each stage:
proceed, update the document first and pause, or pause the review.
Consolidated mode runs all five stages, then consolidates. Either
way, each stage gets at most one re-audit; after that cap, residual
findings are documented as accepted trade-offs with a written ruling
naming who ruled and why. They never advance silently.

**Exit.** The stages feed the verdicts below; they do not replace
them. Per-stage reports live in the run folder (`.work/` or the run
folder, not committed); the consolidated findings land in REVIEW.md
with a traceability line from each raw finding to its consolidated
action, severities mapped to the suite's scale (Blocker to Critical,
Major to Required, Nit to Nit). A document that fails context
sufficiency at stage 1 does not proceed to stages 2 to 5 until it
is fixed.

## Finding triage (CONTEST vs PROPOSE FIX)

Every finding that reaches the author is triaged, by the author,
into one of two bins before anything is fixed.

- **CONTEST** — the critique is inaccurate or rests on a
  misunderstanding of the codebase. A contest must carry exact
  evidence defending the current text (code, or a design-doc
  section), and it is answered with the blind-doubt classes above:
  contract misread, valid and actionable, trade-off, or noise.
  A contest with no evidence is not a contest; it is a shrug.
- **PROPOSE FIX** — the critique is valid, with a precise textual
  replacement or structural adjustment. PROPOSE FIX items may be
  accepted as one batch. CONTEST items are never auto-accepted.

Walk the findings one by one with the human when the stakes
warrant it, and defer all edits until every item is decided.
Decisions land in REVIEW.md and the run ledger, never in memory.
A finding nobody decided on is an open finding.

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
- Presenting a same-context review as a Goldfish review; the isolation is
  the mechanism, and without it the protocol is theatre.
- Recording triage decisions in memory or chat instead of REVIEW.md and
  the ledger; a decision that cannot be produced on request was never made.
- Looping until zero findings with no cap; the suite's rework cap governs,
  and residual findings advance only by written ruling.

<!-- Credit: Goldfish protocol (five stages, semantic split, fresh-context
reviewers, one re-audit per stage), CONTEST vs PROPOSE FIX triage, and the
zoom-out / zero-assumption / zero-decision bars adapted from
google/elephant-goldfish-model (Apache-2.0, commit
3d0b34821ce88ad328b0c9bf0e06d7eb5f1cd669), skills egm-review,
egm-review-loop, egm-resolve and resources/document_standards/
zoom-out-standard.md, implementation-readiness-standard.md,
re-implementation-standard.md. Mechanisms rewritten into suite
conventions; see docs/audit/absorbed/2026-10-26-elephant-goldfish-model.md
(A-011). -->

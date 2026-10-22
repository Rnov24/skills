# Proving run A-004 — auditor report

- **Status:** DONE_WITH_CONCERNS (the audit is complete — all 18 rules
  judged on both targets, no skips — and the concerns below are about
  the ruleset's wording, which is evidence this run exists to collect)
- **Date:** 2026-10-22
- **Auditor note:** this report is not the verdict on A-004. The
  verdicts in audit.md are claims with cited evidence; the orchestrator
  re-verifies them.

## Files created (both in this folder)

| File | What it is |
|---|---|
| `audit.md` | The audit: 18 rule entries per target in ux-heuristics.md order, evidence labelled RENDER / DOM-HTML / SOURCE with file:line, FAILs quoting the rule's operative words and naming the exact element, per-target tallies, overall tally, and an out-of-scope observations section |
| `report.md` | This file |

Nothing in either target repository was modified.

## Method summary

- Read the brief, then the 18 rules in
  skills/design/references/ux-heuristics.md (the 8 in "Choice,
  grouping, and convention"; the bolded Defaults-are-safe,
  Input-is-tolerated, and Impossible-actions rules in "Forms and
  input"; the bolded Doherty, Errors-preserve, Peak-End, and
  Goal-Gradient rules in "Feedback and system states"; the bolded
  Von Restorff, Fitts, and Parkinson rules in "Lists and data
  density"). No other rules were applied as verdicts.
- Target A judged from the orchestrator's 420px render plus
  popup.html and popup.js in full, with scraper.js and content.js
  read at the exact points the popup's messages land (pause/stop
  state machine, already-running guards, getStatus response,
  processPage response timing). The empty model dropdown in the
  render was judged from source, per the brief, and recorded as an
  out-of-scope observation rather than a defect.
- Target B judged from the three orchestrator renders plus the full
  login and register page sources. The served build at
  localhost:3100 was dumped with the headless Chromium shell
  (--dump-dom) for both routes as a cross-check: the served DOM
  matched the source on every fact used (submit labels, role default
  visible in the served submit label "Daftar sebagai Siswa", the
  code section and its quick-fill chips present in the served build).
  No form was submitted and no credentials were used anywhere; both
  routes returned HTTP 200.
- Dynamic rules (Doherty, Errors preserve, Peak-End, Goal-Gradient)
  were judged from the submit/flow handlers in source, and every
  such entry in audit.md says so.

## Tally

| Target | PASS | FAIL | NA |
|---|---|---|---|
| A — NetAcad popup | 14 | 4 | 0 |
| B — EXAMIND auth | 17 | 1 | 0 |
| Both | 31 | 5 | 0 |

Target A FAILs: Serial Position; Impossible actions unavailable /
risky ones warned; Flows end memorably (Peak-End); Progress feels
like progress (Goal-Gradient).
Target B FAIL: Progress feels like progress (Goal-Gradient).

The pattern is itself a finding about the ruleset: the five FAILs are
not scattered. Four of the five sit in state communication over time
(what the interface says while work runs and when it ends, and what
may be pressed meanwhile), and the same Goal-Gradient rule failed on
both products independently — long-running or multi-step work exists
in both, and in both the interface declines to show where the user
stands in it.

## Concerns — where the rules were ambiguous to apply

These are reported as evidence about the ruleset, per the brief.
Each was resolved as stated, but a second competent auditor could
resolve some of them the other way, and the orchestrator should know
exactly which verdicts rest on an interpretation.

1. **Serial Position — "last" is not scoped.** The rule says
   low-priority items must never sit in "the two positions people
   remember", but does not say whether the sequence is the screen,
   the section, or the action stack. On Target A the FAIL rests on
   reading the sequence as the popup's action stack, whose final row
   is the export ghost buttons; a reader who scopes the sequence per
   section (the run area leads with its primary action, and settings
   sections end on their own content) could pass it. The rule needs a
   scope sentence more than this surface needs a redesign.
2. **Doherty — "state change on the control itself" vs adjacent
   status.** Target A's run buttons acknowledge through the #status
   line directly beneath them, set synchronously in the handler; only
   the Save button changes its own appearance. The auditor passed
   Target A because the acknowledgement is immediate and inseparable
   from the press, but the rule's parenthetical, read literally,
   demands the change be on the control. Target B's buttons do
   change themselves (spinner + label + disabled), so the ambiguity
   only affects A's verdict.
3. **Defaults are safe — where "commitment" begins.** Target A ships
   three behaviour defaults ON (auto-select answers, show answer
   cards, solve new pages). The rule's examples of forbidden defaults
   are commitments (paid tier, public post, recurring charge), and
   nothing executes until an explicit run press, with auto-submit —
   the genuinely committing default — shipped off. The auditor passed
   it on that reading. A stricter reader who treats "auto-solve new
   pages" as itself a commitment could fail it. The rule would be
   sharper if it defined commitment as an effect that occurs without
   a further deliberate action.
4. **Peak-End — what counts as "a flow" on a remote-control
   surface.** The Target A FAIL applies the rule to the popup even
   though the run executes in the page. The application is defensible
   because the popup initiates the run, receives the completion
   response, and is where the ending state renders (a present-tense
   "running" message that then auto-clears to blank) — but the rule
   does not scope "flow" by surface, and the entry in audit.md shows
   the whole evidence chain so the orchestrator can overturn the
   scoping if it disagrees.
5. **Goal-Gradient — conditional steps.** On Target B the OTP step
   only exists when the backend requires verification, so some users
   never see a second step. The FAIL stands because users who do hit
   step 2 get no step position, milestone, or remaining-work
   statement — but the rule does not say whether a conditional or
   rare step owes the same indicator as a fixed wizard step.
6. **Miller — "screen" mapped to "session" on Target A.** The
   carry-forward half of the rule speaks of earlier and later
   screens; a popup has one screen, so the auditor judged the
   carry-forward by persistence across popup openings (settings
   reloaded and re-presented from storage). The mapping is natural,
   but it is a mapping, and it is the reason Target A's Miller entry
   is a PASS rather than an NA. Target B needed no such mapping (its
   verify-link prefill is the rule's textbook case).
7. **A note on NA:** no rule returned NA on either target, which the
   auditor double-checked rather than celebrated. The two nearest
   candidates were Miller on Target A (resolved by the session
   mapping above) and Peak-End on a surface with no purchase-like
   flow (Target A does complete flows — runs and saves — so the rule
   applies). If the orchestrator prefers stricter NA discipline,
   those are the two entries to re-examine first.

# Orchestrator review — proving run A-004 (UX-law rules)

Reviewer: the orchestrator, 2026-10-22. The auditor's verdicts were
treated as claims. Every FAIL was re-derived from the cited evidence
in the target source code, and three PASSes were spot-checked the
same way. Neither target repository was modified (verified by git
status after the run).

## Re-verification of the five FAILs — all five reproduce

1. **Target A, Impossible actions / risky warned.** popup.html renders
   Pause and Stop as ordinary buttons; a grep of popup.js shows the
   two are never assigned `disabled` in any state, so both are
   clickable while idle. The pause handler flips the button to
   "Resume" and shows "Paused" on the response, and
   `pauseAutonomousLoop` (scraper.js) sets `isAutonomousPaused = true`
   unconditionally, with no is-running check — an idle Pause press
   manufactures a paused state for a loop that does not exist. A grep
   for `confirm(` across popup.html, popup.js, ui.js, scraper.js and
   content.js returns zero matches, while Auto-Solve combined with
   Auto-Submit hands answers to a real quiz. Both halves of the rule
   fail on primary evidence.
2. **Target A, Peak-End.** content.js answers the processPage message
   only inside `fn().then(...)` — the response genuinely means the
   loop has finished. popup.js answers that completion with the
   present-tense text "Quiz Auto-Pilot running", through a status
   helper whose default duration auto-clears the text after 3500ms,
   leaving a blank status and a "Ready" badge. Completion itself is
   recorded only in console.log calls in scraper.js. No surface
   anywhere states what was accomplished. The FAIL is, if anything,
   understated.
3. **Target A, Goal-Gradient.** scraper.js tracks
   `scrollerCurrentSection` and content.js's getStatus response
   carries `scrollCurrent` and `scrollTotal`. The popup's poll
   handler reads only the running/paused flags and renders one of
   three status words; the two counters are never read. The data to
   show progress exists end-to-end and the last hop declines it.
4. **Target A, Serial Position.** The HTML order is as claimed: the
   action stack ends with the Export Markdown / Export JSON ghost
   pair, the lowest-priority actions on the surface sitting in the
   final position. Upheld under the rule's own wording, which names
   "a screen" as one of its sequence scopes and this popup is a
   single screen. The auditor's disclosed scope ambiguity is recorded
   below as a clarity finding, not grounds to overturn.
5. **Target B, Goal-Gradient.** register/page.tsx holds an explicit
   two-step state (its own comment: "1: Registration Form,
   2: OTP Verification Panel"), but a search of the file finds no
   step indicator, milestone name, or remaining-work text rendered
   anywhere — the step structure exists in code and is invisible to
   the user standing in it. FAIL stands.

## Spot-checked PASSes — all three reproduce

- **Target B, Doherty.** `setLoading(true)` is literally the first
  statement of the login submit handler, before validation or any
  request.
- **Target B, Impossible actions.** The OTP verify button is disabled
  until the code is exactly 6 digits, and the resend control is
  disabled through its cooldown with the reason printed on the
  control itself ("Kirim ulang dalam {cooldown} dtk").
- **Target A, Defaults are safe.** popup.js loads autoSubmit with
  `=== true` (the committing behaviour ships OFF and must be opted
  into) while the non-committing defaults load with `!== false`,
  and the Mercury decision toggle is also opt-in. The auditor's
  disclosed interpretation is the natural one, and it is confirmed
  in code.

## False positives

None. Five FAILs claimed, five reproduced from primary evidence,
zero overturned. The auditor also refused free findings: the
production quick-fill registration-code chips on Target B's register
screen and the missing password-visibility toggle on login were
correctly parked as out-of-scope observations instead of being
stretched into verdicts.

## Ruleset clarity findings (recorded, not silently resolved)

The auditor reported six wording ambiguities, each tied to a verdict
that rests on the disclosed interpretation: Serial Position's
unscoped "last", Doherty's "on the control itself" against an
adjacent status line, Defaults' undefined start of "commitment",
Peak-End's unscoped "flow", Goal-Gradient's silence on conditional
steps, and Miller's screen-to-session mapping on a single-screen
surface. None of them blocked a verdict in this run, and one exposure
is not enough to rewrite a rule on — per the adapt discipline these
stay recorded here as watched items. A second run that trips on the
same wording is the signal that earns a clarification candidate.

## Verdicts on the proving run

- Discrimination: the ruleset separates the two surfaces cleanly —
  4 FAILs on the dense settings-and-actions popup against 1 on the
  focused auth flow — and the one rule that failed both, Goal-Gradient,
  failed for the same underlying reason in each (the interface holds
  progress information it never shows), which is a pattern, not noise.
- Spec verdict: **PASS.** All 36 rule-target pairs judged with
  labelled evidence, FAILs quoting the rule and naming the element,
  NA discipline checked rather than assumed.
- Quality verdict: **PASS.** Zero false positives under independent
  re-verification, PASSes spot-checked in source, out-of-scope
  observations kept out of the tally.

A-004 is promoted to ADAPTED on this evidence.

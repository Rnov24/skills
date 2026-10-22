# Proving brief A-004 (orchestrator)

Audit two real UIs against exactly the 18 rules that gluttony run 3
(A-004) merged into `skills/design/references/ux-heuristics.md` — the
8 rules in "Choice, grouping, and convention", the 3 bolded rules in
"Forms and input" (Defaults are safe; Input is tolerated; Impossible
actions are unavailable, risky ones are warned), the 4 bolded rules in
"Feedback and system states" (Feedback lands within ~400ms; Errors
preserve the work; Flows end memorably; Progress feels like progress),
and the 3 bolded rules in "Lists and data density" (One dominant
action per section; Actions sit beside their content; The path stays
short). No other rules are in scope; other observations are recorded
separately and never counted as verdicts.

## Targets (a contrast pair, both the owner's real products)

- Target A — the NetAcad AI Assistant extension popup, a dense
  settings-and-actions surface. Source: ~/workspace/netacad-autoanswer/
  (popup.html, popup.js, ui.js). Render captured by the orchestrator:
  target-a-netacad-popup-420.png in this folder (file:// render; the
  model dropdown is unpopulated there because extension storage APIs
  are absent outside the extension host — judge that element from
  source, and say so).
- Target B — the EXAMIND auth screens (login + register), a focused
  flow surface, served from the owner's local build at
  http://localhost:3100/login and /register (the server is already
  running; source in ~/workspace/examind-fe/src/app/(auth)/). Renders
  captured by the orchestrator: target-b-examind-login-1280.png,
  target-b-examind-login-390.png, target-b-examind-register-1280.png.

## Method

- One verdict per rule per target: PASS, FAIL, or NA. NA requires the
  reason (the surface genuinely lacks the situation the rule governs).
  A rule silently skipped is a failed audit, not a passed one.
- Every verdict carries evidence, labelled by type: RENDER (what the
  screenshot shows, described precisely), DOM/HTML (an element fact),
  or SOURCE (file:line in the target's code, quoted behaviour). Dynamic
  rules (Doherty, Peak-End, Errors preserve work, Goal-Gradient) are
  judged from the submit/flow handlers in source when the render
  cannot show them, and the evidence type must say so.
- FAIL verdicts must quote the rule's own words and name the exact
  element that breaks them. A FAIL the orchestrator cannot reproduce
  from the cited evidence will be overturned as a false positive in
  review, and false positives count against the ruleset's clarity,
  not just the auditor — so do not stretch a rule to catch something
  it does not say.
- This is an audit only. Do not modify either target repository.

---
phase: discover
keywords: brief, problem, masalah, kebutuhan, request, idea, ide, mau bikin, unclear requirement
name: brief
description: Turn a raw request into an approved problem brief. Use when a request is bigger than a one-line fix or its real problem is unstated — before research, PRD, or any design work.
---

# Brief

A brief is the cheapest artifact in the suite and the one whose absence costs
the most. It states the problem before anyone falls in love with a solution.

## Process

1. **Interview for the real want.** Ask what outcome the requester actually
   wants, not what they think they should want. One question at a time, each
   building on the last answer. Stop when the problem can be stated in two
   sentences that the requester recognises as their own.
2. **Separate problem from proposed solution.** Most requests arrive as
   solutions ("add a dashboard"). The brief records the problem ("nobody can
   see which exams are currently running") and lists the proposed solution as
   one candidate, not as the scope.
3. **Name the evidence.** What is known, what is assumed, what is unknown.
   Unknowns that a decision depends on become research tasks, not footnotes.
4. **Draw the boundary.** Scope and explicit non-goals. A brief without
   non-goals is a scope leak waiting for a date.
5. **Write BRIEF.md** from `templates/brief.md` and get the human's approval.
   Approval of the brief is approval of the problem, not of any solution.

## Rules

- Short is a feature: one page. If the brief needs a second page, the problem
  is probably two problems.
- Divergence before convergence: when the direction is genuinely open, sketch
  two or three framings of the problem and let the human kill the wrong ones
  before any convergence work starts.
- The brief is allowed to conclude "do not build this". That is a success,
  recorded like any other outcome.

## Anti-patterns

- Writing the brief as a feature list; features belong to the PRD.
- Interviewing in bulk (a questionnaire of twenty questions) instead of one
  question at a time; the second question depends on the first answer.
- Starting design or spec work on an unapproved brief because the direction
  "seemed obvious".

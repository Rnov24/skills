---
name: adapt
description: The suite's adaptation loop — turn observed failures and repeated friction from real runs into permanent, evidence-backed changes to the suite itself. Use after retros, when review findings escape a gate, when the finder misses, or when absorbed skills need promotion.
phase: meta
keywords: adapt, adaptation, adaptasi, evolve, self-improvement, improve suite, belajar dari run, routing miss, wheel, mahoraga
---

# Adapt

A suite that cannot change itself decays into ritual. Adapt is the wheel:
every phenomenon the suite survives — an escaped defect, a repeated rework
finding, a finder miss, a human correction given twice — turns the wheel
once, and the suite comes out different in exactly the place that failed.

Adaptation is earned by exposure. Nothing in this skill changes the suite
on a hunch, a benchmark from someone else's workflow, or a good argument.
A change becomes an adaptation only after the phenomenon it counters has
been observed in a real run, with evidence that can be pointed at.

## Signals

Harvest candidates from these sources, in this order of trust:

1. **Escapes.** Findings discovered after the gate that should have caught
   them, recorded in RETRO.md. An escape indicts a specific gate; the
   candidate names it.
2. **Rework hot spots.** The same finding class appearing in two or more
   review rounds or two or more runs. Repetition means the contract, the
   packet, or the template is unclear — not that workers are careless.
3. **Finder misses.** The routing-miss log (`.work/routing-misses.log`,
   appended automatically by `find_skill.py` on NO_CONFIDENT_MATCH) and any
   run where the orchestrator routed by hand because the index failed.
4. **Repeated human corrections.** The same correction given in two runs is
   a rule the suite failed to carry. One correction is conversation; two is
   a specification.
5. **Parked findings with rulings.** A ruling that keeps recurring is a
   policy pretending to be an exception.
6. **Unaudited arrivals.** New skills installed in the environment that
   gluttony has not processed, and gluttony absorptions still at EXPOSED.

## The candidate

Each candidate is filed in `docs/ADAPTATIONS.md` from
`templates/adaptation.md` with five fields, no fewer:

- **Phenomenon:** what was observed, with links to the run, review, or log
  line that proves it happened.
- **Counter:** the exact suite change — which skill, template, keyword set,
  or gate, edited how.
- **Expected effect:** the observable that should move, stated so a later
  run can confirm or refute it.
- **Blast radius:** what the change could break, and which existing rule it
  might contradict.
- **Status:** PROPOSED, TRIAL, ADAPTED, or REJECTED, always with a date.

## The loop

1. **File** the candidate when the signal is harvested (retro is the usual
   harvest point; adapt may be run on its own whenever signals accumulate).
2. **Verify the phenomenon.** Re-read the evidence. If the evidence is one
   ambiguous incident, the candidate waits for a second exposure instead of
   being argued into existence.
3. **Trial when the blast radius is wide.** Process changes that touch many
   skills run as TRIAL on one project or one run first, with the expected
   effect checked at that run's retro. Narrow changes (a keyword, a template
   field, a clarified gate) skip trial.
4. **Human gate.** Applying a candidate is a grant decision: the human sees
   phenomenon, counter, and expected effect, and approves or rejects.
   Rejected candidates stay in the log with the reason. The wheel remembers
   what did not work so the same proposal is not re-litigated every month.
5. **Apply completely or not at all.** An approved adaptation edits the
   skill or template, regenerates the index when frontmatter changed, bumps
   the suite version, notes the reinstall command, and flips its log entry
   to ADAPTED with the commit that carried it. A half-applied adaptation is
   worse than a rejected one because the log then lies about what the suite
   is.
6. **Confirm or revert.** If three runs pass without the expected effect
   moving, the adaptation is reverted by counter-entry in the log, not
   quietly edited away. Adaptations are hypotheses with a memory, not
   decorations.

## Absorption staging

Gluttony delivers mechanisms at **EXPOSED**: audited, adapted in form,
present in the suite, but not yet proven in this suite's own work. Adapt
promotes a mechanism to **ADAPTED** when a real run has used it and the
retro records that it held, or when the human promotes it by written
ruling. A mechanism that sits at EXPOSED through five runs without being
used is a candidate for removal — the suite absorbed it for a need that
turned out not to exist, and carrying it is not free.

## Proving runs for design mechanisms

Design mechanisms are hard to promote on testimony: a run "felt" better
proves nothing. A design adaptation, and any EXPOSED design absorption
seeking promotion, is proven by a **brief-to-output pair** filed with the
candidate in `docs/ADAPTATIONS.md`:

- **The brief, verbatim**, with the reasoning trace preserved beside it —
  pre-flight findings, the rotation pick and its stated reason, the
  preview block — so a reviewer can see what the mechanism was responding
  to, not just what it produced.
- **The output**: the artifact itself or a durable link to it, not a
  description of it.
- **The findings writeback**: what failed, which rule the failure became
  (or which existing rule it confirmed), and the review verdict the pair
  received. A pair with no findings is suspicious, not clean.

Choose the proving briefs as a contrast set: they should stress the
mechanism's failure modes, not flatter it. And pairs rot — a brief-to-
output pair proves the mechanism as the suite stood when it ran; after
the relevant skill changes materially, the pair is retired and a fresh
run proves the mechanism again, or the promotion lapses back to EXPOSED.

## Anti-patterns

- Adapting to a single loud incident with no second exposure.
- Absorbing a famous workflow wholesale because it is famous; the wheel
  turns for observed phenomena, not for reputations.
- Editing a skill in place without a log entry; an unlogged change is an
  adaptation the next maintainer cannot reason about.
- Letting candidates accumulate unreviewed; a backlog of fifty proposals is
  a signal to hold an adapt session, not a trophy.

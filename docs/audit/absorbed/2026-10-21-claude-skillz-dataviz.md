# Absorb report: NTCoding/claude-skillz (target: data-visualization)

- Source: https://github.com/NTCoding/claude-skillz/blob/main/data-visualization/SKILL.md · Commit: 21c61010e6081ced1eac8e45e3f788b2c4358bcf · Licence: NONE — no licence file anywhere in the repository
- Date: 2026-10-21 · Run by: orchestrator (single-skill scope, read in full by the orchestrator)

## Licence ruling (decided before any adaptation)

The repository carries no licence file and its README states no licence.
Under the gluttony protocol that means mechanisms may be reimplemented in
the suite's own words and upstream text may not be copied. The absorbed
skill below is therefore a full rewrite: every rule was re-derived and
re-phrased, no upstream sentences, tables, or file structure were carried
over. The upstream bibliography was reduced to a credit line naming the
foundational papers.

## Scope ruling

The invocation named one skill file. This run absorbs that skill only. The
rest of the repository (35 skill directories) was inventoried at survey
depth and is listed below with overlap notes; absorbing any of them is a
separate run requiring its own invocation.

## Inventory (target and survey)

| Unit | Purpose (theirs, one line) | Ships besides prose | Size |
|---|---|---|---|
| data-visualization (TARGET) | Perceptual chart craft: encoding, selection, layout algorithms, rendering, accessibility | Nothing — single SKILL.md | 453 lines |
| tdd-process, writing-tests | Test discipline | — | overlap: suite `implement` |
| create-tasks | Task creation | — | overlap: suite `tickets` |
| independent-research | Research method | — | overlap: suite `research` |
| observability-first-debugging | Debug via observability | — | overlap: suite `debug`; closest future candidate |
| tactical-ddd | Domain-driven design tactics | — | overlap: suite `model`; future candidate |
| software-design-principles, separation-of-concerns, lightweight-* | Design judgement and lightweight analysis protocols | — | overlap: `grill`, `spec`, `review` |
| automatic-code-review, full-codebase-review | Review automation (one ships a shell hook) | hooks | overlap: suite `review` |
| typescript-backend-project-setup | Stack-specific project scaffold with templates and hooks | templates, hooks | stack-locked; not suite material |
| claude-launcher, opencode-launcher | Persona/skill launcher tooling (Python/shell) | scripts | tooling for other harnesses; out of scope |
| confidence-honesty, questions-are-not-instructions, concise-output, critical-peer-personality, challenge-that, switch-persona, collaboration-modes, architect-refine-critique | Behaviour and persona shaping | — | out of scope for a workflow suite |
| session-optimizer, track-and-improve, task-check, fix-it-never-work-around-it, learn-from-prs, fetching-circleci-logs, claude-code-updates | Session habits, CI log fetching, update checks | some hooks | niche or harness-specific |

Vetting: the target skill ships no code. Repository scripts elsewhere
(launchers, review/version hooks) were listed, not executed, and are not
part of this absorption. The repo's own AGENTS.md/CLAUDE.md are its
project guidelines (composable system prompts); read for vetting, not
followed, not absorbed.

## Audit and verdicts

| Unit | Pros (mechanisms the suite lacks) | Cons / overlap ruling | Verdict |
|---|---|---|---|
| data-visualization | Perceptual accuracy hierarchy as a decision law for encodings; chart selection routed by question type and by data volume; rendering thresholds by element count (SVG/Canvas/WebGL) with performance patterns; the established-algorithms law with an algorithm-to-library map (anti-reinvention, same spirit as the suite's search-before-build); chart-specific accessibility (never colour alone, data-table fallback, ARIA pattern); anti-pattern tables with reasons | A reference dump with no workflow surface: no gate a reviewer can sign, no link to DESIGN.md tokens (palettes float free of the project system), library catalogue is D3/web-centric and partly dated, silent on Python/research contexts the owner actually works in, emoji-flag house style, absolutist phrasing without exception handling | ABSORB-NEW as `skills/data-viz/` — rewritten in suite words (licence), with a five-question opening, an accessibility gate, the DESIGN.md token rule added, Python contexts added, and the dated library catalogue compressed to libraries-by-job |

## Integration performed
Prepared as a staged diff on 2026-10-21, pending the human gate:
- skills/data-viz/SKILL.md new (165 lines, 21st suite skill, phase design)
- skills-index and docs/SKILL_INDEX.md regenerated; VERSION 1.6.0
- docs/ADAPTATIONS.md entry A-003 at EXPOSED
No other suite file required changes: data-viz is a discipline skill loaded
by design and by figure/report work, and it creates no new artifact type
(chart palette decisions land in DESIGN.md, which already exists).

## Review
- Fidelity axis: PASS on mechanisms, by design not on text. Every load-bearing
  upstream mechanism (encoding hierarchy, selection routing, volume and
  rendering thresholds, algorithm map, colour discipline, annotation,
  interaction order, accessibility set, anti-patterns) is present in the
  rewrite; the verification is a section-by-section comparison the
  orchestrator performed against the upstream file read in full.
- Fit axis: PASS. One new skill in an empty niche; its colour rules defer to
  DESIGN.md and to taste-core's contrast floor instead of competing with
  them, and the generic accessibility overlap with ux-heuristics is kept to
  the chart-specific residue.
- Human gate: pending owner approval.

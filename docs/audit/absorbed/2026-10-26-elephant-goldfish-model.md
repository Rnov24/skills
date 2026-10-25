# Absorb report: google/elephant-goldfish-model (EGM) — batch 1

- Source: https://github.com/google/elephant-goldfish-model · Commit: 3d0b34821ce88ad328b0c9bf0e06d7eb5f1cd669 (2026-10-23, merge PR #118) · Licence: Apache-2.0
- Date: 2026-10-26 · Run by: Ronald (orchestrator) · Human gate: approved by Jal on 2026-10-26
- Scope of this report: all seven upstream skills, audited in
  three parallel batches. Batch 1 (brainstorm, draft) and batch 2
  (review, review-loop, resolve, bootstrap, drift-report) are both
  adapted in the working tree; the combined diff is at the human
  gate together, at the owner's instruction to wait for batch 2.

## Inventory
| Unit | Purpose (theirs, one line) | Ships besides prose | Size |
|---|---|---|---|
| egm-brainstorm | Turn a raw concept into a structured hypothesis via clarifying questions and a parallel Goldfish swarm | TEST.md, test_scenarios.yaml (4 scenarios) | 294 lines |
| egm-draft | Draft a design document section by section from a concepts brief | references/design_doc.md template, TEST.md, test_scenarios.yaml (6 scenarios) | 293 lines |
| egm-review | Multi-stage Goldfish verification pipeline (zoom out, comprehension, critic, readiness) | TEST.md, test_scenarios.yaml | 397 lines |
| egm-review-loop | Concurrent review subagent dispatch engine, direct and hierarchical | TEST.md, test_scenarios.yaml | 160 lines |
| egm-resolve | Interactive triage and automated patch application for review findings | TEST.md, test_scenarios.yaml | 162 lines |
| egm-bootstrap | Recursive bottom-up codebase documentation generator with sentinel-block upserts | references/worker-return.schema.json, test_scenarios.yaml | 458 lines |
| egm-drift-report | Sequential AST scanner detecting divergence between checked-in specs and live code | TEST.md, test_scenarios.yaml | 67 lines |
| agents/ (9 personas) | Reviewer lenses: synthesizer, design critic, codebase details, zoom out, comprehension, implementation readiness, structural, style, bootstrap orchestrator | frontmatter names for subagent dispatch | 30–74 lines each |
| resources/document_standards/ (5) | Quality bars: feature-spec, Heilmeier catechism, implementation-readiness, re-implementation, zoom-out | — | 30–60 lines each |
| resources/execution_instructions.md | Silent no-code guard, one-question rule, no-summary rule, contradiction freeze | — | 43 lines |
| .claude-plugin/hooks/allow_plugin_reads.sh | PreToolUse hook allowing reads inside plugin folders | — | shell, ~30 lines |
| site/, tests/, docs/designs/ | Marketing site, pytest unit/integration tests, the repo's own EGM design docs | — | not absorbable units |

## Audit and verdicts — batch 1
| Unit | Pros (mechanisms the suite lacks) | Cons / overlap ruling | Verdict |
|---|---|---|---|
| egm-brainstorm | Six-lens parallel fresh-context swarm with a synthesizer dedup; staged ban on structured question tools during exploration; single-question readiness gate before reviewers spawn; critique-first with counter-argument per strategy; artifact-first no-chat-dump prohibition | Overlaps `brief` (same pipeline position and output shape) and `grill` (same one-question interrogation posture); no round cap on its iteration loop; no traceability IDs; no check that reviewer objections are resolved before handoff; banned-adjective/apology lists are style policing with no mechanical check; RFC publish + SITEMAP are harness layout, not mechanism | MERGE-INTO grill + brief — lens swarm, critique-first, readiness gate, readiness rule. REJECT the banned-word lists, RFC/SITEMAP steps, and the four-option handoff gate |
| egm-draft | Per-section approval gates with an empty-write-in guard; polymorphic intake priority (concepts brief, then discussion summary, then chat); every-file-with-rationale Detailed Implementation list with a no-code rule; Alternatives Considered as a mandatory step; feature-spec and Heilmeier standards as fresh-session quality bars | Overlaps `spec` (same pipeline position, overlapping section set); per-section gates duplicate the suite's human gates; save-location gate + SITEMAP are harness layout; pre-save zoom-out self-evaluation is done by the same session that wrote the draft; no story-ID citation, no standalone Test seams, no Assumptions block; revision loop has no round cap | MERGE-INTO spec — Alternatives rule, every-file implementation list, no-code rule, fresh-session bar with Heilmeier check, predecessor-brief intake by pointer. REJECT per-section approval gates, save-location gate, and SITEMAP registration |
| agents/synthesizer.md | Intermediate swarm compiler: spawns parallel reviewers (optionally A/B duplicates), dedups overlapping findings, groups by severity (Blocker/Major/Nit), normalises file/line references, writes the consolidated report before notifying | Severity vocabulary differs from the suite's (Critical/Required/Nit/Optional/FYI); no existing suite role does this dedup | MERGE-INTO orchestrate — synthesizer step, with Blocker→Critical and Major→Required mapping |
| resources/document_standards/feature-spec-standard.md + heilmeier-standard.md | Fresh-session quality bar stated as a testable reader outcome; alternatives rule with specific rejection reasons; Heilmeier eight questions (objectives without jargon, state of the art, what is new, who cares, risks/payoffs, cost, timeline, mid-term and final exams) | Neither file is cited by path from the two audited skills; zoom-out standard overlaps the suite's YAGNI and design discipline | MERGE-INTO spec — fresh-session bar and Heilmeier check, rewritten in suite words. REJECT vendoring the standards files verbatim |
| resources/execution_instructions.md | One-question-at-a-time discipline (already a suite rule in grill); contradiction must be surfaced, not silently smoothed over | Silent no-code enforcement, no meta-talk, no summaries, and a freeze-on-contradiction that forbids any file write in the same turn — all contradict the suite's evidence-before-claims, review-findings-with-evidence, and ledger discipline | REJECT as a unit — the no-code mechanism itself survives in `spec`; its silent enforcement does not |
| egm-review | Five-stage Goldfish document review (initial zoom-out, comprehension, critic, intermediate zoom-out, implementation readiness) over a semantic split of the doc into a feature range and a detailed-implementation range; four pipeline presets; per-stage checkpoint gates; one re-audit per stage; consolidated report with traceability matrix; explicit stop rule that a same-context review is not a Goldfish review; six reviewer personas each with a distinct audit vector | Collides with `review` (closest) and `orchestrate` (dispatch, checkpoints, rework). No ticket, AC IDs, verification commands, base, per-AC verdict, or pass/fail exit criterion; checkpoint gates are user choices, not acceptance criteria; residual findings after the cap advance as documented trade-offs with no ruling; reviews a design doc only, runs no verification command, no mutation probe, no floor check; report filenames unregistered, no template ships | MERGE-INTO review — Goldfish protocol as staged document review (five stages, semantic split, fresh-context reviewers only, per-stage checkpoint, one re-audit per stage, consolidated report). Stages feed the suite's per-AC verdicts and ACCEPT/REWORK/ESCALATE unit verdict; they do not replace them. REJECT the preset gate as a modal system, the banned-word constraints, and harness subagent names |
| egm-review-loop | Shortname resolver for reviewers and standards; unconditional re-derivation of target line ranges from a stable semantic target before every iteration; synthesizer-vs-direct dispatch choice; idle across human turns, resume only on explicit confirmation; loop until zero findings | Collides with `orchestrate` (closest, dispatch and iteration driver) and `review`. No ticket, AC IDs, verification commands, base, dual verdict, per-AC verdict, ledger, or numeric round cap — loop-until-zero is unbounded; no resolution rule for conflicting parallel findings beyond synthesizer dedup | MERGE-INTO orchestrate — re-derive line ranges from the semantic target on every re-audit; record the synthesizer-vs-direct choice in the packet. REJECT loop-until-zero (suite rework cap of five rounds governs instead) and the shortname resolver (suite delegates by artifact pointer, not by name) |
| egm-resolve | CONTEST vs PROPOSE FIX triage with an evidence requirement for contesting; auto-accept batch applying all PROPOSE FIX items at once; interactive breakdown walking findings one by one with distinct options per category, deferring all edits until every item is decided; zero-tool yield at the resolution gate | Collides with `review` (finding disposition) and `implement` receiving-review. No independent arbiter for a CONTEST (the Elephant defends its own text); severity vocabulary in its report template (High/Medium/Low) does not match the reviewers' (Blocker/Major/Nit); breakdown decisions recorded in an internal memory checklist, not a file; "continue" proceeds with no written ruling for unaddressed items; custom-instruction option is unbounded | MERGE-INTO review + implement — CONTEST/PROPOSE FIX triage with defending evidence, auto-accept batch for PROPOSE FIX only, interactive breakdown with edits deferred until decided. Decisions land in REVIEW.md and the ledger, never in memory; contests are answered with the suite's blind-doubt classes (contract misread / valid and actionable / trade-off / noise). REJECT the memory checklist and the unbounded custom-instruction option |
| resources/document_standards/zoom-out, implementation-readiness, re-implementation | Context-sufficiency prerequisite fail; zero-assumption rule (a reviewer must be able to re-implement from the doc alone); zero-decision rule (no design decision left to the implementer); YAGNI and reuse verified by code search | Overlap the suite's YAGNI and design discipline in places; the standards are prose bars with no instrument behind them | MERGE-INTO review — the three bars as Goldfish stage checks, rewritten in suite words. REJECT vendoring the standards files verbatim |
| egm-bootstrap | Recursive bottom-up documentation of the team's own tree: BFS discovery with pruning, read-only scout per directory under read caps, leaf-first post-order roll-up into parent Blueprints, correction policy that preserves human notes, ecosystem verification-command discovery, adaptive partition-and-swarm above 5 directories, >15-directory scope gate, final read-every-file verification pass | Collides partially with `recon` (direction differs: own code read directly vs external product under clean-room rules; output differs: many README contracts in the tree vs one RECON.md + FEATURES.csv). The per-directory own-codebase documentation has no counterpart and no registered artifact. Headline sentinel-block upsert is specified in the upstream design doc (docs/designs/bootstrap.md §2.7) but absent from the SKILL.md itself; no human approval of generated content below 16 directories; no semantic correctness check of extracted contracts; extension allowlist omits languages the suite's users work with (.astro among them); unbounded spawning has no concurrency limit | MERGE-INTO recon — own-codebase bootstrap mode (bottom-up README contracts, leaf-first, preserve human notes, >15-directory gate, final link check), adopting the design doc's sentinel markers as the mechanical preservation rule. REJECT the extension allowlist as written, the prettier assumption, and harness subagent names |
| egm-drift-report | Named post-hoc doc-vs-code consistency sweep across a directory; differences-only reporting with "No drift detected" per doc; logic unreferenced by any design counts as drift | Collides with `verify` (same question, different evidence standard: `verify` demands freshly executed evidence, drift-report demands only reading and judgement). No AST mechanism exists in the skill file despite the egm.dev wording — no parser, no language, no tool; no severity scale, no verdicts, no rework loop, no human gate, no handling of ADR-approved intentional divergence; report location unregistered | MERGE-INTO verify — drift sweep as a differences-only check with suite severities and verdicts, consulting ADRs before flagging intentional divergence. REJECT the AST claim and the standalone dated report file as an unregistered artifact |
| resources/execution_instructions.md | (decided in batch 1) | — | REJECT — see batch 1 table |

## Integration performed — batch 1
- `skills/spec/SKILL.md`: Alternatives mandatory, Detailed
  Implementation every-file list, no-code rule, fresh-session bar
  with Heilmeier check, predecessor-brief intake by pointer; two
  new anti-patterns; credit footer.
- `templates/spec.md`: new sections Alternatives considered and
  Detailed implementation.
- `skills/grill/SKILL.md`: lens swarm section (six lenses, at most
  two rounds, fresh workers only), critique-first rule, readiness
  gate; one new anti-pattern; credit footer.
- `skills/orchestrate/SKILL.md`: synthesizer step for parallel
  reviewers (dedup, severity mapping, report file before
  notification, optional A/B instances for high stakes); one new
  anti-pattern; credit footer.
- `skills/brief/SKILL.md`: readiness rule before reviewers spawn.
- `docs/WORKFLOW.md`: Spec gate tightened; new Elephant-Goldfish
  flow section naming the shape.
- `docs/ARTIFACTS.md`: SPEC.md gate tightened to match.
- `docs/SYNTHESIS.md`: v1.16.0 note, batch 1 (A-011, EXPOSED).
- `docs/ADAPTATIONS.md`: A-011 table row and candidate record.
- No new skill was created; no skill was renamed; no template
  besides spec.md changed; no scripts were added or moved.
  Skill count stays 23.

## Integration performed — batch 2
- `skills/review/SKILL.md`: Goldfish protocol (five stages,
  semantic split, fresh-context reviewers only, per-stage
  checkpoint, one re-audit per stage, consolidated report with
  traceability into REVIEW.md), CONTEST vs PROPOSE FIX triage,
  and the three bars (context-sufficiency prerequisite fail,
  zero-assumption, zero-decision); three new anti-patterns;
  credit footer.
- `skills/orchestrate/SKILL.md`: re-derive line ranges from the
  semantic target on every re-audit; synthesizer-vs-direct
  dispatch choice named in the packet.
- `skills/implement/SKILL.md`: receiving-review triage
  (CONTEST with evidence, PROPOSE FIX batch, edits deferred
  until every item is decided, decisions in report and ledger).
- `skills/recon/SKILL.md`: bootstrap mode for the team's own
  undocumented codebase (bottom-up README contracts, leaf-first,
  read-only scout, sentinel markers preserving human notes,
  >15-directory gate, final link check); credit footer.
- `skills/verify/SKILL.md`: drift sweep (differences-only,
  ADR check before flagging, suite severities, coverage stated);
  one new anti-pattern; credit footer.
- `docs/ARTIFACTS.md`: DRIFT_REPORT.md registered as a run
  artifact at `docs/drift/<YYYY-MM-DD>-DRIFT_REPORT.md`.
- `docs/WORKFLOW.md`: Review gate now requires the Goldfish
  protocol for specs before implementation.
- `docs/SYNTHESIS.md` and `docs/ADAPTATIONS.md`: A-011 record
  extended to cover batch 2.

## Review
- Fidelity axis: the merged mechanisms are the ones the audit
  named — alternatives with rejection reasons, every-file list,
  fresh-session bar, six lenses, critique-first, readiness gate,
  synthesizer dedup — each present in the skill it merged into,
  rewritten in suite words with suite severities and caps. The
  per-section approval gate and the banned-word lists were
  deliberately not carried over; see the verdict table.
- Fit axis: the suite stays one workflow — no duplicate skill, no
  orphan artifact, no artifact without a trigger. SPEC.md gains
  sections but no new artifact; the lens swarm and synthesizer
  reuse the existing packet/report/ledger machinery. The
  WORKFLOW.md flow section points at `review` for the Goldfish
  protocol rather than duplicating it; batch 2 decides that
  protocol.
- Fidelity axis (batch 2): the Goldfish protocol keeps the five
  stages, the semantic split, the fresh-context rule, and the
  one-re-audit cap, but its findings feed the suite's per-AC and
  unit verdicts instead of advancing as documented trade-offs;
  the loop-until-zero termination and the memory checklist were
  deliberately not carried over; the drift sweep keeps the
  differences-only report and the undocumented-code rule, but
  gains ADR checks, suite severities, and a registered report
  location, and drops the syntax-tree claim.
- Human gate: approved by Jal on 2026-10-26. Released as v1.16.0;
  A-011 stays EXPOSED until a proving run promotes it.

---
phase: meta
keywords: gluttony, absorb, serap skill, add skill, tambah skill, import skill repo, merge skills
name: gluttony
description: Absorb an external skill repository into this suite — audit every skill in it, verdict each one, and adapt what survives into suite conventions. Slash-command only; the argument is the repository URL.
disable-model-invocation: true
argument-hint: <skill-repo-url>
---

# Gluttony: absorb a skill repo

Target repository: $ARGUMENTS

Gluttony eats skill repositories. It does not copy them. Every skill in the
target repo is audited against this suite, given a verdict, and — only if it
survives — rewritten into the suite's conventions before it lands. What
arrives is never what enters the suite; that is the point of eating.

If the argument is missing or is not a repository URL, ask for the URL in
one short message and stop. Nothing else in this skill runs without a target.

## 1. Intake

- Clone the target into `.work/gluttony/<repo-name>/` (shallow clone). Record
  the exact commit SHA and the clone date in the absorb report.
- Read the licence before anything else. MIT, Apache-2.0, BSD: text may be
  adapted with credit. No licence file: mechanisms may be reimplemented in
  the suite's own words, upstream text may not be copied. Copyleft: flag it
  to the human before any adaptation.
- **Vet before trusting.** Read every script, hook, and installer in the repo
  before running any of it. Absorption never requires executing upstream
  code; if a step seems to need it, that step is redesigned, not run.
  Anything that reaches for credentials, shells out to the network beyond
  the clone, or writes outside its own folder ends the intake with a report
  to the human.

## 2. Inventory

Enumerate every absorbable unit in the repo: each SKILL.md, each slash
command, each bundled agent or reference set. For each unit record its name,
stated purpose, size, and what it ships besides prose (scripts, data,
assets). The inventory is a table in the absorb report, built from
`templates/absorb-report.md`.

## 3. Audit

Audit each unit against the suite as it exists now, not in the abstract:

- **Pros:** the concrete mechanisms it has that the suite lacks or does worse.
- **Cons:** bloat, unverifiable rules, overlap with an existing suite skill,
  tool lock-in, missing gates, missing artifact discipline.
- **Overlap ruling:** name the existing suite skill it collides with, or
  state plainly that it covers new ground.

Repos with more than a handful of skills are audited by parallel subagents,
one batch per family, each auditor receiving the upstream unit and the suite
registry (`docs/ARTIFACTS.md` plus the README skill list) and nothing else —
no enthusiasm, no verdict hints.

## 4. Verdicts

Each unit gets exactly one verdict:

- **ABSORB-NEW** — covers ground the suite lacks; becomes a new skill.
- **MERGE-INTO <skill>** — its mechanism strengthens an existing skill; the
  mechanism is extracted, the rest is discarded.
- **ADAPT-EXISTING** — it replaces or substantially rewrites an existing
  suite skill, which is then version-noted in the report.
- **REJECT** — with the reason in one sentence. Rejection is a normal,
  expected outcome; a gluttony run that absorbs everything has failed its
  audit, because upstream repos always contain manifesto duplicates and
  tool-locked filler.

The suite's standing prejudices apply: no second taste manifesto, no skill
without an artifact or a gate, no prose where a checkable rule exists, no
unit whose only virtue is length.

## 5. Adapt

Surviving units are rewritten, never pasted:

- House frontmatter: `name`, one-sentence `description` led by what it does
  and when to use it.
- Placed in a phase; if it fits no phase, the phase question goes to the
  human before the skill lands anywhere.
- Rewritten into the suite's shape: purpose, inputs by artifact pointer,
  process, outputs, gate, anti-patterns. Mechanisms survive verbatim in
  substance; upstream voice, branding, and bloat do not.
- Artifact changes are registered: a new artifact gets a registry entry in
  `docs/ARTIFACTS.md` with a trigger, an owner, and a gate, plus a template
  in `templates/`. No trigger, no artifact — no exceptions for imports.
- Credit is recorded in the skill's footer and in `docs/SYNTHESIS.md`: the
  upstream repo, its licence, and the commit absorbed from.

## 6. Integrate and validate

- Place the adapted files. Update the README skill list, the phase map in
  `docs/WORKFLOW.md` if a phase changed, and the audit trail: the absorb
  report is committed to `docs/audit/absorbed/<date>-<repo-name>.md`.
- Run the suite's validation: every SKILL.md has valid frontmatter with a
  name matching its directory, every `templates/` reference resolves, no
  dead internal links, counts in the README match the folders.

## 7. Review gate

Absorption lands through the suite's own review discipline, on two axes:

- **Fidelity axis:** does the adapted unit still contain the upstream
  mechanism that earned the verdict, or a watered summary of it?
- **Fit axis:** does the suite stay one workflow — no duplication, no orphan
  skill, no artifact without a trigger?

Then the human gate: present the absorb report summary (absorbed, merged,
rejected, each with its one-line reason) and the diff. Commit and push only
after the human approves. Gluttony prepares everything up to that gate and
stops there, like every other irreversible action in this suite.

## Report back

Close with the counts and the names: what was absorbed as new, what was
merged into which skill, what was rejected and why, and where the full audit
lives. If the repo turned out to be all filler, the correct report is "ate
it, kept nothing, here is why" — said with the same confidence as a feast.

## Anti-patterns

- Installing the upstream repo alongside the suite "for reference"; the
  audit file is the reference.
- Absorbing a skill because it is famous rather than because the suite lacks
  its mechanism.
- Keeping upstream naming that collides with suite vocabulary; the glossary
  wins.
- Running this on the suite's own repository. Gluttony eats other suites.

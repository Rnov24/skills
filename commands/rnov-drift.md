---
description: Check whether the code has drifted: sweep a tree's SPEC.md, DESIGN.md, and README contracts against the current code and report only the divergences.
argument-hint: "[directory to sweep]"
---
# /rnov-drift

Follow the `verify` skill, Drift sweep section.

## Steps

1. Follow the `verify` skill, Drift sweep section. For each document, read it, locate the source it names, and compare against the current code.
2. Check the ADRs before flagging: intentional divergence is recorded with its ADR cited, not flagged as drift.
3. Every item carries its evidence (doc section and code location) and a severity from the suite's scale; triage findings like review findings (CONTEST with evidence, or PROPOSE FIX).
4. State the coverage plainly: the sweep is a read-and-judge comparison, bounded by what was actually read.

## Output

Differences-only report at docs/drift/<YYYY-MM-DD>-DRIFT_REPORT.md with coverage stated.

---
description: Run a six-lens parallel swarm on an anchored hypothesis: Contrarian, Cost, UX, Migration, Observability, Tech debt — fresh workers only.
argument-hint: "[the hypothesis in two or three sentences]"
---
# /rnov-lens-swarm

Follow the `grill` skill, Lens swarm (optional, delegated) section.

## Steps

1. Follow the `grill` skill, Lens swarm section. Do not spawn the swarm until the readiness gate passes: the hypothesis is anchored in two or three sentences the human recognises, and the human confirms readiness.
2. Spawn six fresh workers, one per lens; each receives only the hypothesis and the artifacts it needs — no conversation history, no author claims.
3. Synthesise before reporting: dedup, group by severity (see `orchestrate`). A list of raw, overlapping findings is not a result.
4. At most two rounds per hypothesis; findings resolve into the decision tree, ADRs, or parked with an owner and a trigger.

## Output

Deduplicated findings grouped by severity; unresolved items resolved, recorded as ADRs, or parked with owner and trigger.

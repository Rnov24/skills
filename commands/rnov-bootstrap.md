---
description: Document an undocumented codebase bottom-up into per-directory README contracts, leaf first.
argument-hint: "[repo root or directory]"
---
# /rnov-bootstrap

Follow the `recon` skill, Bootstrap mode (own codebase, no design docs) section.

## Steps

1. Follow the `recon` skill, Bootstrap mode section. Discover breadth-first and prune test-only and empty directories; above fifteen directories, pause for human approval before any swarm is spawned.
2. Scout each directory read-only with bounded reads; write leaf Component Package contracts first, then parent Blueprints post-order.
3. Preserve human notes inside the sentinel markers; never overwrite an existing README wholesale.
4. Final pass: every section present and populated, every relative link resolves, verification targets match the test configuration.

## Output

Per-directory README contracts with sentinel markers; placeholders logged as documentation owed, not as completed contracts.

# Absorb report: anthropics/skills (targets: mcp-builder & webapp-testing)

- Source: https://github.com/anthropics/skills · Commit: dbd4588f9e1033efb41dad4bef2f7947c8993d44 · Licence: Apache-2.0 (© Anthropic) — text, references, and scripts adapted with credit
- Date: 2026-10-23 · Run by: orchestrator (gluttony run 7)

## Licence ruling (decided before any adaptation)

Both units carry an Apache-2.0 `LICENSE.txt`. Text, reference guides, and helper scripts are adapted with credit in their headers and footers. The evaluation harness and lifecycle script were vetted and adapted to suite conventions.

## Inventory

| Unit | Purpose (theirs, one line) | Ships besides prose | Size |
|---|---|---|---|
| mcp-builder (TARGET 1) | Guide for creating high-quality MCP servers in Python (FastMCP) or Node/TypeScript (MCP SDK) | 4 reference docs (~82KB), 2 Python scripts, 1 XML sample | 236 lines + references |
| webapp-testing (TARGET 2) | Toolkit for interacting with and testing local web applications using Playwright | 1 helper script (`with_server.py`, 106 lines), 3 example scripts | 96 lines + tooling |

Vetting notes:
- `mcp-builder/scripts/`: `connections.py` (lightweight connection context for stdio / streamable HTTP) and `evaluation.py` (XML evaluation runner). No credential leaks, no network calls outside target endpoints.
- `webapp-testing/scripts/with_server.py`: Pure stdlib Python (`subprocess`, `socket`, `time`, `sys`, `argparse`) polling localhost ports. Safe.

## Audit and verdicts

| Unit | Pros (mechanisms the suite lacks) | Cons / overlap ruling | Verdict |
|---|---|---|---|
| mcp-builder | (1) Rigorous 4-phase protocol: Research & Planning, Implementation, Review & Inspector testing, Evaluation suite. (2) Standardized tool naming convention (`{service}_{action}_{resource}`) preventing agent tool collisions. (3) Behavioral tool annotations (`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`). (4) Context pagination and dual structured/markdown response formats. (5) Complete language references for Node/TypeScript and FastMCP Python. (6) Objective 10-question evaluation harness with string-verifiable answers. | Evaluation runner scripts initially tied to Claude API; generalized for standard MCP connections and test harnesses. | ABSORB-NEW as `skills/mcp-builder/` (phase: build) — fills a complete capability gap for authoring and verifying MCP server tool integrations. |
| webapp-testing | `with_server.py` helper cleanly automates background server lifecycle management (port polling, command execution, signal trap teardown). | The markdown prose is standard Playwright boilerplate (launch chromium, wait for networkidle, take screenshot) without new artifacts, gates, or workflow rigor. Duplicates suite's `verify` phase and existing `playwright-cli`. | REJECT as standalone skill; MERGE `with_server.py` into `scripts/with-server.py` as an executable runner utility for testing local apps. |

## Integration performed

Prepared as a staged diff on 2026-10-23, pending human gate:
- `skills/mcp-builder/SKILL.md`: New 22nd suite skill (phase: build), rewritten to suite structure with the 4-phase protocol, tool annotations, and anti-patterns.
- `skills/mcp-builder/references/`: Vendored `mcp_best_practices.md`, `node_mcp_server.md`, `python_mcp_server.md`, and `evaluation.md`.
- `skills/mcp-builder/scripts/`: Vendored `connections.py`, `evaluation.py`, and `example_evaluation.xml`.
- `scripts/with-server.py`: Adapted server lifecycle runner from `webapp-testing`.
- `docs/ADAPTATIONS.md`: Added entry A-008 at EXPOSED.
- `docs/SYNTHESIS.md`: Added v1.13.0 synthesis note for `mcp-builder` and `with-server.py`.
- `VERSION`: Bumped to `1.13.0`.
- Regenerated `docs/SKILL_INDEX.md` and `skills-index.json` (22 skills).

## Review

- Fidelity axis: PASS on mechanisms. Full MCP development protocol, Zod/Pydantic schemas, tool annotations, and evaluation harness preserved in substance. `with_server.py` preserved intact with stdlib efficiency.
- Fit axis: PASS. `mcp-builder` occupies an empty niche in `phase: build`; `webapp-testing` avoids skill proliferation by landing its single useful script in `scripts/`.
- Human gate: pending human approval.

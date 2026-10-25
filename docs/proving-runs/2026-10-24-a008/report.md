# Proving run A-008 — an MCP server built and evaluated by the protocol, plus with-server on a real app

Run: 2026-10-24. Artifacts in this folder: `server.py` (a three-tool
Linkstash MCP server), `evaluate.py` (its evaluation suite), and the
outputs below.

## Part 1 — mcp-builder's four phases, actually walked

- Phase 1–2 produced `server.py` under the skill's conventions: tool
  names in `{service}_{action}_{resource}` form
  (`linkstash_create_link`, `linkstash_list_links`,
  `linkstash_count_links`), Pydantic-shaped typed inputs, and the
  behavioural annotations on every tool (read tools `readOnlyHint`,
  the create tool explicitly not read-only and not idempotent).
- Phase 3 (review and inspect) ran through the official MCP client
  over stdio: initialize, `list_tools`, live calls.
- Phase 4 (evaluation) is `evaluate.py`: five questions whose answers
  are only obtainable by calling the tools, plus four convention
  checks. Final result: **9/9 checks passed**, reproducibly (the
  suite deletes its database and re-runs from empty).

## Findings written back (two, both real)

1. **The vendored Python reference targets SDK v1 and nothing in the
   suite said so.** The current `mcp` package (2.x) renamed FastMCP
   to MCPServer, so a worker following `python_mcp_server.md` today
   fails at import. The run pinned `mcp<2` (the same pin this
   workspace already uses for TiDB's MCP) and everything worked.
   Writeback applied with this promotion: a version note in
   `skills/mcp-builder/SKILL.md` Phase 2 stating the pin and the 2.x
   rename, so the next worker does not rediscover it at runtime.
2. **List-returning tools need structuredContent handling.** The
   first evaluation draft parsed `content[0].text` and silently got
   one element of a two-element list — an evaluation that passes
   wrong is worse than none. The evaluator now prefers
   `structuredContent`. Recorded here; the vendored harness in
   `skills/mcp-builder/scripts/evaluation.py` is LLM-driven and was
   not modified, but evaluators written from it should take the same
   care. (The LLM-driven harness itself was not run: it needs an API
   endpoint this run did not use, and this report does not claim it.)

## Part 2 — with-server.py against a real application

`scripts/with-server.py` started Linkstash's real FastAPI app
(uvicorn, port 8123), waited for the port, and ran a gated command
against the live server: `POST /api/links` returned 201,
`GET /api/links` returned the created record, `GET /` returned 200,
and the runner tore the server down cleanly with exit 0. The test
database it created was removed afterwards.

## Verdict

Both halves of A-008 held on real work, and the run paid rent: one
versioning trap in the vendored reference is now documented in the
skill itself. A-008 is ready to promote EXPOSED → ADAPTED.

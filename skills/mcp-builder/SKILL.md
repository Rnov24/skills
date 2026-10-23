---
phase: build
keywords: mcp, model context protocol, mcp server, fastmcp, tool definition, mcp tool, json-rpc, mcp inspector, agent tools
name: mcp-builder
description: Design, implement, and evaluate Model Context Protocol (MCP) servers in TypeScript or Python with strict tool naming, schemas, and test harnesses. Use when building or testing MCP integrations.
---

# MCP Builder

An MCP (Model Context Protocol) server exposes tools, resources, and prompts
to LLM clients over a standard JSON-RPC interface. A high-quality MCP server
is not just an API wrapper — it is a curated boundary designed specifically
for agent reasoning, token budget efficiency, and reliable tool discovery.

## The 4-Phase Protocol

```
Phase 1: Research & Plan --> Phase 2: Implement --> Phase 3: Review & Inspect --> Phase 4: Evaluate
(API boundaries & names)    (Zod/Pydantic & Hints)   (Build & MCP Inspector)     (10-Question XML Suite)
```

### Phase 1: Research and Planning

1. **API Boundary vs. Workflow Tools.**
   - Start with comprehensive API coverage for primary resources.
   - Combine operations into workflow tools only when individual tools create
     excessive multi-step chat latency.
2. **Naming and Discoverability.**
   - Format: `{service}_{action}_{resource}` in `snake_case` (e.g. `github_create_issue`,
     `slack_send_message`, `postgres_query_table`).
   - Action verbs must be specific (`list`, `get`, `create`, `update`, `delete`, `search`).
   - Anticipate tool collision: an agent may mount 10+ servers simultaneously; generic
     names like `query` or `execute` are banned.
3. **Context Management and Pagination.**
   - Never return unpaginated lists. Always support `limit` (defaulting to 20–50 items)
     and return `has_more` / `next_offset`.
   - Provide summary projections for list operations; reserve full payloads for single-item `get` tools.
4. **Transport Selection.**
   - **stdio**: Default for local process-based integrations (CLI agents, Antigravity, Claude Code, desktop apps).
   - **Streamable HTTP**: For remote, multi-tenant, or cloud-hosted servers (stateless JSON over HTTP). Avoid deprecated SSE.

### Phase 2: Implementation

Choose the appropriate language stack:
- **TypeScript (Recommended)**: Node/TypeScript MCP SDK with `Zod` schemas. Best for rich types and ecosystem compatibility.
- **Python**: FastMCP or Python MCP SDK with `Pydantic` models. Best for data science, ML, or Python-native backends.

Each tool definition must provide:
1. **Tool Description**: Exact, concise description of what the tool does, parameter semantics, and return schema.
2. **Input Schema**: Typed parameters with descriptions and practical examples.
3. **Output Content**: Return both structured JSON content (for programmatic consumption) and clean Markdown text (for human inspection).
4. **Behavioral Annotations**:
   - `readOnlyHint`: `true` for non-destructive queries, `false` for mutations.
   - `destructiveHint`: `true` for permanent deletes or irreversible modifications.
   - `idempotentHint`: `true` if repeated calls with identical parameters produce identical state.
   - `openWorldHint`: `true` if operation interacts with external third-party systems outside the server's immediate boundary.
5. **Actionable Errors**: On failure, error responses must explain what went wrong and provide exact, actionable remedy steps.

### Phase 3: Review and Inspection

1. **Compilation and Syntax**:
   - TypeScript: Run `npm run build` or `tsc --noEmit`. Full type coverage required; no implicit `any`.
   - Python: Run `python3 -m py_compile <server>.py` and static linting.
2. **MCP Inspector Verification**:
   - Run `npx @modelcontextprotocol/inspector <command-to-launch-server>`.
   - Verify server initialization handshake, tool listing, schema rendering, and sample tool execution.

### Phase 4: Evaluation Suite

An MCP server without an objective evaluation suite is unverified. Every server
must ship a verifiable 10-question evaluation set:

1. **Requirements for Evaluation Questions**:
   - **Independent**: Each question executable standalone without relying on prior state.
   - **Read-Only**: Requires only non-destructive queries.
   - **Complex**: Requires at least 2–3 coordinated tool invocations and reasoning.
   - **Verifiable**: Has exactly one deterministic answer verified by string/numerical comparison.
   - **Stable**: Answers do not drift with current time or transient external state.
2. **Evaluation XML Format** (`evaluations/<server>.xml`):
   ```xml
   <evaluation>
     <qa_pair>
       <question>Which repository in the organization has the highest number of open pull requests tagged 'security'?</question>
       <answer>auth-service</answer>
     </qa_pair>
   </evaluation>
   ```

## References (load on demand)

Load reference files when implementing specific components:
- `references/mcp_best_practices.md` — naming, pagination, transports, error standards.
- `references/node_mcp_server.md` — complete TypeScript SDK guide with Zod schemas and project setup.
- `references/python_mcp_server.md` — complete FastMCP Python guide with Pydantic models and tool decorators.
- `references/evaluation.md` — question design, verification strategies, and XML evaluation format.
- `scripts/connections.py` & `scripts/evaluation.py` — connection harnesses and automated test runner.

## Anti-patterns

- Generic tool names (`run`, `exec`, `send`) that collide with other MCP servers.
- Unpaginated query tools that return megabytes of raw text into context.
- Omitting `readOnlyHint` or marking destructive delete tools as read-only.
- Vague error messages ("Error 500", "Failed") that give agents no recovery path.
- Claiming an MCP server is complete without running MCP Inspector or verification evaluations.

---
Synthesis and credit: Adapted from Anthropic (`mcp-builder`, Apache-2.0 © Anthropic, commit dbd4588f9e1033efb41dad4bef2f7947c8993d44).

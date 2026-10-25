#!/usr/bin/env python3
"""Deterministic evaluation for the A-008 proving server.

mcp-builder's Phase 4 calls for an evaluation suite of questions whose
answers are verifiable. These five are answered by actually calling the
server's tools over stdio through the official MCP client, then
string-checking the results — no model in the loop, so the verdict is
reproducible byte for byte.
"""
import asyncio
import json
import sys
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

HERE = Path(__file__).parent


async def main() -> int:
    db = HERE / "stash.db"
    if db.exists():
        db.unlink()
    params = StdioServerParameters(
        command=sys.executable, args=[str(HERE / "server.py")]
    )
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await session.list_tools()
            names = sorted(t.name for t in tools.tools)
            print("tools:", names)
            ann = {t.name: t.annotations for t in tools.tools}
            checks = []

            def check(label, ok, detail=""):
                checks.append(ok)
                print(("PASS" if ok else "FAIL"), label, detail)

            check(
                "tool names follow {service}_{action}_{resource}",
                names == [
                    "linkstash_count_links",
                    "linkstash_create_link",
                    "linkstash_list_links",
                ],
            )
            check(
                "annotations present on all tools",
                all(a is not None for a in ann.values()),
            )
            check(
                "read tools marked readOnly",
                ann["linkstash_list_links"].readOnlyHint is True
                and ann["linkstash_count_links"].readOnlyHint is True,
            )
            check(
                "create tool not marked readOnly/idempotent",
                ann["linkstash_create_link"].readOnlyHint is False
                and ann["linkstash_create_link"].idempotentHint is False,
            )

            async def call(name, args):
                res = await session.call_tool(name, args)
                sc = getattr(res, "structuredContent", None)
                if sc:
                    return sc.get("result", sc)
                texts = [c.text for c in res.content if hasattr(c, "text")]
                if len(texts) == 1:
                    return json.loads(texts[0])
                return [json.loads(x) for x in texts]

            r = await call(
                "linkstash_create_link",
                {"url": "https://example.com/a", "title": "Alpha"},
            )
            check("Q1 create returns id 1", r["id"] == 1, str(r))
            await call(
                "linkstash_create_link",
                {"url": "https://example.com/b", "title": "Beta"},
            )
            c = await call("linkstash_count_links", {})
            check("Q2 count is 2 after two creates", c["count"] == 2, str(c))
            lst = await call("linkstash_list_links", {"limit": 1})
            check(
                "Q3 list limit=1 returns newest first (Beta)",
                len(lst) == 1 and lst[0]["title"] == "Beta",
                str(lst),
            )
            lst = await call("linkstash_list_links", {})
            check(
                "Q4 default list returns both, newest first",
                [x["title"] for x in lst] == ["Beta", "Alpha"],
                str(lst),
            )
            c = await call("linkstash_count_links", {})
            check("Q5 reads do not mutate (count still 2)", c["count"] == 2)
            print(f"\n{sum(checks)}/{len(checks)} checks passed")
            return 0 if all(checks) else 1


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))

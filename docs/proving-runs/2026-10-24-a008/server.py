#!/usr/bin/env python3
"""Proving-run MCP server for A-008, built per skills/mcp-builder.

A tiny Linkstash-backed tool server. Tool names follow the suite
convention {service}_{action}_{resource}; every tool carries the
behavioural annotations mcp-builder requires (readOnlyHint,
destructiveHint, idempotentHint, openWorldHint).
"""
import sqlite3
from pathlib import Path

from mcp.server.fastmcp import FastMCP
from mcp.types import ToolAnnotations

DB = Path(__file__).with_name("stash.db")

mcp = FastMCP("linkstash")


def _db() -> sqlite3.Connection:
    con = sqlite3.connect(DB)
    con.execute(
        "CREATE TABLE IF NOT EXISTS links "
        "(id INTEGER PRIMARY KEY, url TEXT NOT NULL, title TEXT NOT NULL DEFAULT '')"
    )
    return con


@mcp.tool(
    annotations=ToolAnnotations(
        readOnlyHint=False, destructiveHint=False,
        idempotentHint=False, openWorldHint=False,
    )
)
def linkstash_create_link(url: str, title: str = "") -> dict:
    """Create a saved link in the stash. Returns the created record."""
    with _db() as con:
        cur = con.execute(
            "INSERT INTO links (url, title) VALUES (?, ?)", (url, title)
        )
        con.commit()
        return {"id": cur.lastrowid, "url": url, "title": title}


@mcp.tool(
    annotations=ToolAnnotations(
        readOnlyHint=True, destructiveHint=False,
        idempotentHint=True, openWorldHint=False,
    )
)
def linkstash_list_links(limit: int = 20) -> list[dict]:
    """List saved links, newest first."""
    with _db() as con:
        rows = con.execute(
            "SELECT id, url, title FROM links ORDER BY id DESC LIMIT ?",
            (limit,),
        ).fetchall()
    return [{"id": r[0], "url": r[1], "title": r[2]} for r in rows]


@mcp.tool(
    annotations=ToolAnnotations(
        readOnlyHint=True, destructiveHint=False,
        idempotentHint=True, openWorldHint=False,
    )
)
def linkstash_count_links() -> dict:
    """Count how many links are in the stash."""
    with _db() as con:
        n = con.execute("SELECT COUNT(*) FROM links").fetchone()[0]
    return {"count": n}


if __name__ == "__main__":
    mcp.run()

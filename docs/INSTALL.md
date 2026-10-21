# Installing the suite

One installer, three agent tools, global scope only. Project-local installs
are deliberately not offered: a workflow suite that changes per project is
not a standard, it is a suggestion.

```
python3 scripts/install.py --all                 # everything, copied
python3 scripts/install.py --target claude-code  # one tool
python3 scripts/install.py --all --mode link     # symlinks (suite repo stays the source of truth)
python3 scripts/install.py --all --dry-run       # show, do not touch
python3 scripts/install.py --uninstall --target codex
```

## Targets

**Claude Code** installs each skill into `~/.claude/skills/<skill>/`, where
Claude Code loads global skills. The slash-only skill arrives as `/gluttony`.

**Codex** installs each skill into `~/.codex/skills/<skill>/`, the global
skills directory Codex reads.

**Antigravity (agy)** installs the suite as one plugin named `rnov-skills`.
The installer stages a plugin directory (a `plugin.json` whose `skills` field
is an array of path strings, the layout agy's loader requires) and runs
`agy plugin install` when the CLI is present; otherwise it prints the
staging path and the exact command to run by hand. Remove it with
`agy plugin uninstall rnov-skills`.

## Safety model

The installer writes a manifest (`.rnov24-skills-manifest.json`) into each
target root listing exactly what it installed. It never overwrites or
deletes a skill directory it did not install; conflicts are reported and
skipped unless `--force` is passed. Uninstall removes manifest entries only.

## After installing

Restart the target tool so it rescans its skill directories. In Claude Code
and Antigravity, `/gluttony <repo-url>` should be available immediately
after the restart. To update, pull this repo and re-run the installer; it
replaces its own manifest entries in place.

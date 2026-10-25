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

## Validation

The installer validates before it installs: it regenerates the skill
index, checks every SKILL.md frontmatter (name matches its directory,
description present), checks every `scripts/<file>` reference inside a
skill resolves to that skill's own `scripts/` folder, and compiles
every bundled Python file. It then verifies the installed copies
carry the same skills and scripts. Anything failing stops the install.

`python3 scripts/install.py --check --all` runs the same two checks
without installing, so a user can diagnose a broken install by
themselves instead of guessing which file is missing.

## After installing

Restart the target tool so it rescans its skill directories. In Claude Code
and Antigravity, `/gluttony <repo-url>` should be available immediately
after the restart. To update, pull this repo and re-run the installer; it
replaces its own manifest entries in place.

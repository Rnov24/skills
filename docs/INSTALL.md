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
Claude Code loads global skills. The slash-only skill arrives as `/gluttony`,
and the 8 commands from `docs/COMMANDS.md` (under the cap of 12) install as user-level slash
commands in `~/.claude/commands/` (`/rnov-start`, `/rnov-new`, `/rnov-improve`,
`/rnov-improve-ui`, `/rnov-fix`, `/rnov-goldfish`, `/rnov-bootstrap`, `/rnov-drift`).
On re-install, stale-cleanup removes any command recorded in the install manifest
that is no longer in `commands/commands.json` (such as the retired `/rnov`, renamed
to `/rnov-start`), while leaving foreign command files alone.

**Codex** installs each skill into `~/.codex/skills/<skill>/`, the global
skills directory Codex reads. Codex has no slash-command equivalent, so
commands do not install there; the skills still do.

**Antigravity (agy)** installs the suite as one plugin named `rnov-skills`.
The installer stages a plugin directory (a `plugin.json` whose `skills` field
is an array of path strings, the layout agy's loader requires) and runs
`agy plugin install` when the CLI is present; otherwise it prints the
staging path and the exact command to run by hand. The same `plugin.json`
carries a `commands` array pointing at the 8 command files (under the cap of 12),
staged beside `skills/`. Remove it with
`agy plugin uninstall rnov-skills`.

## Safety model

The installer writes a manifest (`.rnov24-skills-manifest.json`) into each
target root listing exactly what it installed. It never overwrites or
deletes a skill directory it did not install; conflicts are reported and
skipped unless `--force` is passed. Uninstall removes manifest entries only.

## Validation

The installer validates before it installs: it regenerates the skill
index and the command files, checks every SKILL.md frontmatter (name matches its directory,
description present), checks every `scripts/<file>` reference inside a
skill resolves to that skill's own `scripts/` folder, checks every
command in `commands/commands.json` names an existing skill and a
section that exists in that skill, and compiles
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

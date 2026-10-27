# Commands

Slash commands are the suite's addressable entry points. A skill is
knowledge; a command is an entry point with a name. Commands are thin:
each file names the owning skill and the section that does the work, and
holds no knowledge of its own. The skill is the source of truth.

## The rule (what earns a command)

The suite defines two kinds of commands, totaling 8 commands under a strict cap of 12:

1. **Verb command.** Names a task the user would say ("improve UI", "fix this bug",
   "start something new") and runs a whole flow. Every verb command except the
   front door carries an ordered list of skills in `flow`.
2. **State command.** Names a standalone audit or mapping unit the user invokes
   by name ("goldfish this spec", "document this codebase", "check for drift").
   A state command carries no `flow`; it points at one section of one skill.

A command must pass the "user would say it" test: it maps to words a user
speaks when asking for work, not to orchestrator-internal skill states.
Skills themselves are not commands — they are already invocable by name in
prose, and adding one command per skill is rejected as bloat.

The suite enforces a mechanical cap of 12 commands to prevent accretion.
Raising the cap is a human decision recorded in this document; the generator
refuses to run above it.

## The table (8 commands)

| Command | Kind | What the user says | Flow / section |
|---|---|---|---|
| `/rnov-start` | verb | "Start here / I don't know where to start" | router (`using-rnov-skills`), whole skill |
| `/rnov-new` | verb | "Start something new" | setup → brief → research → grill → define-product → design → model → spec → tickets → implement → review → verify → ship → retro |
| `/rnov-improve` | verb | "Improve this" | brief (short) → grill (new decisions only) → define-product (delta stories) → design/model deltas → spec → tickets → implement → review → verify → ship |
| `/rnov-improve-ui` | verb | "Improve this UI" | audit (`design`, Audit an existing UI) → design deltas → keyframe gate → implement → review → verify |
| `/rnov-fix` | verb | "Fix this bug" | debug → implement (one ticket) → review → verify |
| `/rnov-goldfish` | state | "Goldfish this spec" | `review`, Goldfish protocol (all five stages) |
| `/rnov-bootstrap` | state | "Document this codebase" | `recon`, Bootstrap mode |
| `/rnov-drift` | state | "Has the code drifted from the docs?" | `verify`, Drift sweep |

`/gluttony` is older than this layer and stays as it is: a slash-only skill via
`disable-model-invocation: true` in its frontmatter.

## Removed commands

Five v1.17.0 commands were removed because they fail the "user would say it" test:

- `/rnov-goldfish-comprehension`, `/rnov-goldfish-critic`, `/rnov-goldfish-readiness`:
  The Goldfish protocol's value is the full sequence; a single stage is picked
  by the orchestrator mid-review, never by the user. The full-protocol command
  `/rnov-goldfish` covers the user case.
- `/rnov-lens-swarm`: The swarm's readiness gate belongs inside `grill`; a slash
  shortcut invites unanchored swarms, and "swarm" is not user language.
- `/rnov-blind-doubt`: The review skill runs blind doubt by stakes, not ritually
  every time; a command invites ritual use.

In all five cases the skill section stays, the router still dispatches to it,
and only the user-facing command is removed.

`/rnov` was renamed to `/rnov-start` because the original name did not read
as "start here". The old name is retired with no alias in v1.18.0.

## Entry map (`docs/ENTRY.md`)

`docs/ENTRY.md` is the generated one-page entry map that new users or agents
read first. It presents the front door, the two paths with their flow chains,
improve UI, fix, the three audit commands, and the "Shape of the suite"
paragraph. It is generated from `commands/commands.json` by
`scripts/generate_commands.py` and is never edited by hand. The same map is
expanded into `/rnov-start`'s steps.

## How commands are built

`commands/commands.json` is the single source of truth. Each entry names the
command, kind (`verb` or `state`), owning skill, optional `##` section heading,
optional anchor string, description, argument hint, steps, output, and flow for
verb commands.

`scripts/generate_commands.py` renders `commands/<name>.md` and `docs/ENTRY.md`
from the manifest. It enforces:
- `kind` is `verb` or `state`.
- Every verb command except `/rnov-start` has a non-empty `flow` whose skills exist.
- Each manifest `flow` equals the arrow-chain on its router line matched by anchor.
- The manifest holds at most 12 commands (cap of 12).
- Every declared section and anchor exists in the owning skill.
- Expansion of `{{ENTRY_MAP}}` inside `/rnov-start`.

```bash
python3 scripts/generate_commands.py          # write commands/*.md and docs/ENTRY.md
python3 scripts/generate_commands.py --check  # verify only
```

## Where commands install

Antigravity gets them through the plugin: the installer writes a `commands`
array into `plugin.json` and stages `commands/` beside `skills/`. Claude Code
gets the same files as user-level slash commands in `~/.claude/commands/`.
Codex has no slash-command equivalent, so commands do not install there.

On Claude Code, `scripts/install.py` performs stale-cleanup: it removes any
command file recorded in the install manifest that is no longer in
`commands/commands.json`, while leaving foreign files alone and reporting
them by name.

Run `python3 scripts/install.py --check --all` to verify installed state matches
the repo.

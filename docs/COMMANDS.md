# Commands

Slash commands are the suite's addressable entry points. A skill is
knowledge; a command is a state with a name. Commands are thin: each
file names the owning skill and the section that does the work, and
holds no knowledge of its own. The skill is the source of truth.

## The rule (what earns a command)

A command exists for exactly two things:

1. The router (`/rnov`) — the front door for any task.
2. A skill section that runs standalone, with its own inputs and
   outputs. Most sections are steps of one process and do not
   qualify: the five questions in `data-viz`, the pipeline in
   `f1-predict`, the protocol rules in `orchestrate`. The audit
   that set the first nine found only four skills with standalone
   sections: `review` (Goldfish protocol, blind doubt), `grill`
   (lens swarm), `recon` (bootstrap mode), `verify` (drift sweep).

Skills themselves are not commands. They are already invocable by
name in prose, and adding one command per skill is how this layer
grows back to thirty. If a skill command is ever wanted, it is a
mechanical addition from the same generator — but it needs a
reason beyond symmetry.

## The table

| Command | Skill | State |
|---|---|---|
| `/rnov` | `using-rnov-skills` | the router: classify, pick the flow, load one skill |
| `/rnov-goldfish` | `review` | Goldfish protocol, all five stages |
| `/rnov-goldfish-comprehension` | `review` | Goldfish stage 2: comprehension |
| `/rnov-goldfish-critic` | `review` | Goldfish stage 3: critic |
| `/rnov-goldfish-readiness` | `review` | Goldfish stage 5: implementation readiness |
| `/rnov-lens-swarm` | `grill` | lens swarm (six lenses, fresh workers) |
| `/rnov-bootstrap` | `recon` | bootstrap mode: bottom-up README contracts |
| `/rnov-drift` | `verify` | drift sweep: docs against current code |
| `/rnov-blind-doubt` | `review` | blind-doubt pass on a risky decision |

Not in this table, by design: the two Goldfish zoom-out stages
(stage 1 is a gate that needs context, stage 4 needs the stage 1
report) and the re-audit cap (orchestrator-internal) are not
standalone units, so they have no commands. `/gluttony` is older
than this layer and stays as it is: a slash-only skill via
`disable-model-invocation: true` in its frontmatter.

## How commands are built

`commands/commands.json` is the single source of truth. Each entry
names the command, the owning skill, the exact `##` section heading,
an anchor string inside that section, the description, the
argument hint, the steps, and the output.
`scripts/generate_commands.py` renders `commands/<name>.md` from
the manifest and verifies every declared section exists in the
owning skill and every anchor sits inside it — a renamed section
fails generation instead of leaving a command pointing at text
that no longer exists. Never edit a generated command file by
hand; edit the manifest and re-run the generator.

```bash
python3 scripts/generate_commands.py          # write commands/*.md
python3 scripts/generate_commands.py --check  # verify only
```

## Where commands install

Antigravity gets them through the plugin: the installer writes a
`commands` array into `plugin.json` (the same array-of-paths
layout as `skills`, proven by the designer plugins) and stages
`commands/` beside `skills/`. Claude Code gets the same files as
user-level slash commands in `~/.claude/commands/`. Codex has no
slash-command equivalent, so commands do not install there; the
skills still do. Run `python3 scripts/install.py --check --all`
to verify the installed commands match the repo.

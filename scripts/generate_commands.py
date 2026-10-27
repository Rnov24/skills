#!/usr/bin/env python3
"""Generate commands/*.md and docs/ENTRY.md from commands/commands.json.

The manifest is the single source of truth. Never edit a generated
command file by hand; edit commands.json and re-run this script.
The generator verifies every declared section exists in the owning
skill (and every declared anchor appears inside that section) so a
renamed section fails generation instead of leaving a command
pointing at text that no longer exists.

Usage:
  generate_commands.py            # write commands/*.md, remove stale ones
  generate_commands.py --check    # verify only, write nothing
"""
import argparse, json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
MANIFEST = ROOT / 'commands' / 'commands.json'
OUTDIR = ROOT / 'commands'
ENTRY_FILE = ROOT / 'docs' / 'ENTRY.md'


def load_manifest():
    return json.loads(MANIFEST.read_text(encoding='utf-8'))


def section_text(skill_text, heading):
    """Return the text of one ## section, or None if the heading is absent."""
    lines = skill_text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if line.strip() == heading:
            start = i
            break
    if start is None:
        return None
    end = len(lines)
    for j in range(start + 1, len(lines)):
        if lines[j].startswith('## '):
            end = j
            break
    return '\n'.join(lines[start:end])


def skill_exists(name):
    return (ROOT / 'skills' / name).is_dir() or (name == 'setup' and (ROOT / 'skills' / 'setup-workspace').is_dir())


def find_router_item(router_text, anchor):
    lines = router_text.splitlines()
    for i, line in enumerate(lines):
        if anchor in line:
            start = i
            while start > 0 and not lines[start].startswith('- '):
                start -= 1
            item_lines = [lines[start]]
            for j in range(start + 1, len(lines)):
                if lines[j].startswith('- ') or lines[j].startswith('## ') or not lines[j].strip():
                    break
                item_lines.append(lines[j])
            return ' '.join(l.strip() for l in item_lines)
    return None


def extract_skills_from_chain(item_text):
    if ':' in item_text:
        item_text = item_text.split(':', 1)[1]
    parts = item_text.split('→')
    if not parts:
        return []
    parts[-1] = re.split(r'\.\s+', parts[-1])[0].rstrip('.')
    skills = []
    for part in parts:
        cleaned = re.sub(r'\(.*?\)', '', part)
        for t in re.findall(r'[a-zA-Z0-9_-]+', cleaned):
            if skill_exists(t):
                skills.append(t)
    return skills


def render_entry_map(manifest):
    by_name = {c['name']: c for c in manifest['commands']}
    lines = []

    # 1. Front door
    fd = by_name.get('rnov-start', {})
    lines.append('## Front door\n')
    lines.append(f"- `/{fd.get('name', 'rnov-start')}` {fd.get('argument-hint', '')} — {fd.get('description', '')}\n")

    # 2. Two paths
    r_new = by_name.get('rnov-new', {})
    new_flow = ' → '.join(r_new.get('flow', [])) if isinstance(r_new.get('flow'), list) else r_new.get('flow', '')
    r_imp = by_name.get('rnov-improve', {})
    imp_flow = ' → '.join(r_imp.get('flow', [])) if isinstance(r_imp.get('flow'), list) else r_imp.get('flow', '')
    lines.append('## The two paths\n')
    lines.append(f"- `/{r_new.get('name', 'rnov-new')}` {r_new.get('argument-hint', '')} — {r_new.get('description', '')}")
    lines.append(f"  Flow: `{new_flow}`")
    lines.append(f"- `/{r_imp.get('name', 'rnov-improve')}` {r_imp.get('argument-hint', '')} — {r_imp.get('description', '')}")
    lines.append(f"  Flow: `{imp_flow}`\n")

    # 3. Improve a UI surface
    r_ui = by_name.get('rnov-improve-ui', {})
    ui_flow = ' → '.join(r_ui.get('flow', [])) if isinstance(r_ui.get('flow'), list) else r_ui.get('flow', '')
    lines.append('## Improve a UI surface\n')
    lines.append(f"- `/{r_ui.get('name', 'rnov-improve-ui')}` {r_ui.get('argument-hint', '')} — {r_ui.get('description', '')}")
    lines.append(f"  Flow: `{ui_flow}`\n")

    # 4. Fix
    r_fix = by_name.get('rnov-fix', {})
    fix_flow = ' → '.join(r_fix.get('flow', [])) if isinstance(r_fix.get('flow'), list) else r_fix.get('flow', '')
    lines.append('## Fix\n')
    lines.append(f"- `/{r_fix.get('name', 'rnov-fix')}` {r_fix.get('argument-hint', '')} — {r_fix.get('description', '')}")
    lines.append(f"  Flow: `{fix_flow}`\n")

    # 5. Audits
    lines.append('## Audits\n')
    for cmd in manifest['commands']:
        if cmd.get('kind') == 'state':
            lines.append(f"- `/{cmd['name']}` {cmd.get('argument-hint', '')} — {cmd.get('description', '')}")
    lines.append('')

    # 6. Shape paragraph
    lines.append('## Shape of the suite\n')
    shape_text = (
        "The suite is one pipeline entered through two paths: `/rnov-new` starts something new and "
        "`/rnov-improve` improves what exists. `/rnov-fix` joins the pipeline at implement, skipping "
        "setup through tickets. Audits run before changes. Whenever a task matches no command, "
        "`/rnov-start` decides."
    )
    lines.append(shape_text)

    return '\n'.join(lines)


def render_entry_md(manifest):
    return f"# Entry Map\n\n{render_entry_map(manifest)}\n"


def render(cmd, manifest):
    skill = cmd['skill']
    section = cmd.get('section')
    if section:
        where = f"the `{skill}` skill, {section.removeprefix('## ').strip()} section"
    else:
        where = f"the `{skill}` skill"
    lines = [
        '---',
        f"description: {cmd['description']}",
        f"argument-hint: \"{cmd['argument-hint']}\"",
        '---',
        f"# /{cmd['name']}",
        '',
        f"Follow {where}.",
        '',
        '## Steps',
        '',
    ]
    for i, step in enumerate(cmd['steps'], 1):
        if '{{ENTRY_MAP}}' in step:
            map_content = render_entry_map(manifest)
            if step == '{{ENTRY_MAP}}':
                lines.append(f"{i}. Read the entry map:\n\n{map_content}\n")
            else:
                lines.append(f"{i}. {step.replace('{{ENTRY_MAP}}', map_content)}\n")
        else:
            lines.append(f"{i}. {step}")
    lines += ['', '## Output', '', cmd['output'], '']
    return '\n'.join(lines)


def verify(manifest):
    """Check every command's skill, section, and anchor. Returns errors."""
    errors = []
    commands = manifest.get('commands', [])
    if len(commands) > 12:
        errors.append(f"command cap exceeded ({len(commands)} > 12); raising the cap is a human decision recorded in docs/COMMANDS.md")

    names = set()
    for cmd in commands:
        name = cmd.get('name', '')
        if name in names:
            errors.append(f"{name}: duplicate command name")
        names.add(name)
        if '/' in name or ' ' in name:
            errors.append(f"{name}: command name must be one token")

        kind = cmd.get('kind')
        if kind not in {'verb', 'state'}:
            errors.append(f"{name}: kind must be 'verb' or 'state'")

        skill = cmd.get('skill', '')
        skill_file = ROOT / 'skills' / skill / 'SKILL.md'
        if not skill_file.exists():
            errors.append(f"{name}: skill {skill} has no SKILL.md")
            continue
        text = skill_file.read_text(encoding='utf-8')
        section = cmd.get('section')
        if section:
            body = section_text(text, section)
            if body is None:
                errors.append(f"{name}: section {section!r} not found in {skill}/SKILL.md")
                continue
            anchor = cmd.get('anchor')
            if anchor and anchor not in body:
                errors.append(f"{name}: anchor {anchor!r} not found inside {section!r} in {skill}/SKILL.md")

        for field in ('description', 'argument-hint', 'output'):
            if not cmd.get(field):
                errors.append(f"{name}: {field} is empty")
        if not cmd.get('steps'):
            errors.append(f"{name}: steps are empty")

        if kind == 'verb':
            if name != 'rnov-start':
                flow = cmd.get('flow')
                if not flow:
                    errors.append(f"{name}: verb command requires a non-empty flow")
                else:
                    flow_skills = flow if isinstance(flow, list) else [s.strip() for s in flow.split('→')]
                    for s in flow_skills:
                        if not skill_exists(s):
                            errors.append(f"{name}: skill {s!r} in flow does not exist under skills/")

                    if skill == 'using-rnov-skills' and cmd.get('anchor'):
                        item_text = find_router_item(text, cmd['anchor'])
                        if item_text:
                            router_skills = extract_skills_from_chain(item_text)
                            if router_skills != flow_skills:
                                errors.append(f"{name}: flow {flow_skills} does not match router line skills {router_skills}")
    return errors


def generate(manifest, check):
    errors = verify(manifest)
    wanted = {}
    for cmd in manifest['commands']:
        wanted[f"{cmd['name']}.md"] = render(cmd, manifest)
    entry_md_content = render_entry_md(manifest)

    if not check:
        for fname, content in wanted.items():
            (OUTDIR / fname).write_text(content, encoding='utf-8')
        for old in sorted(OUTDIR.glob('*.md')):
            if old.name not in wanted:
                old.unlink()
        ENTRY_FILE.write_text(entry_md_content, encoding='utf-8')
    else:
        for fname, content in wanted.items():
            f = OUTDIR / fname
            if not f.exists():
                errors.append(f"{fname}: missing (would be generated)")
            elif f.read_text(encoding='utf-8') != content:
                errors.append(f"{fname}: differs from generated output (re-run without --check)")
        for old in sorted(OUTDIR.glob('*.md')):
            if old.name not in wanted:
                errors.append(f"{old.name}: stale (not in manifest)")
        if not ENTRY_FILE.exists():
            errors.append("docs/ENTRY.md: missing (would be generated)")
        elif ENTRY_FILE.read_text(encoding='utf-8') != entry_md_content:
            errors.append("docs/ENTRY.md: differs from generated output (re-run without --check)")
    return errors


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true', help='verify only, write nothing')
    a = ap.parse_args()
    manifest = load_manifest()
    errors = generate(manifest, a.check)
    if errors:
        print('generate_commands FAILED:')
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"commands OK ({len(manifest['commands'])} commands{' checked' if a.check else ' generated'})")
    return 0


if __name__ == '__main__':
    sys.exit(main())

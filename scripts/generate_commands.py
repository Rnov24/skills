#!/usr/bin/env python3
"""Generate commands/*.md from commands/commands.json.

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
import argparse, json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
MANIFEST = ROOT / 'commands' / 'commands.json'
OUTDIR = ROOT / 'commands'


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


def render(cmd):
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
        lines.append(f"{i}. {step}")
    lines += ['', '## Output', '', cmd['output'], '']
    return '\n'.join(lines)


def verify(manifest):
    """Check every command's skill, section, and anchor. Returns errors."""
    errors = []
    names = set()
    for cmd in manifest['commands']:
        name = cmd['name']
        if name in names:
            errors.append(f"{name}: duplicate command name")
        names.add(name)
        if '/' in name or ' ' in name:
            errors.append(f"{name}: command name must be one token")
        skill_file = ROOT / 'skills' / cmd['skill'] / 'SKILL.md'
        if not skill_file.exists():
            errors.append(f"{name}: skill {cmd['skill']} has no SKILL.md")
            continue
        text = skill_file.read_text(encoding='utf-8')
        section = cmd.get('section')
        if section:
            body = section_text(text, section)
            if body is None:
                errors.append(f"{name}: section {section!r} not found in {cmd['skill']}/SKILL.md")
                continue
            anchor = cmd.get('anchor')
            if anchor and anchor not in body:
                errors.append(f"{name}: anchor {anchor!r} not found inside {section!r} in {cmd['skill']}/SKILL.md")
        for field in ('description', 'argument-hint', 'output'):
            if not cmd.get(field):
                errors.append(f"{name}: {field} is empty")
        if not cmd.get('steps'):
            errors.append(f"{name}: steps are empty")
    return errors


def generate(manifest, check):
    errors = verify(manifest)
    wanted = {}
    for cmd in manifest['commands']:
        wanted[f"{cmd['name']}.md"] = render(cmd)
    if not check:
        for fname, content in wanted.items():
            (OUTDIR / fname).write_text(content, encoding='utf-8')
        for old in sorted(OUTDIR.glob('*.md')):
            if old.name not in wanted:
                old.unlink()
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

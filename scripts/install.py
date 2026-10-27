#!/usr/bin/env python3
"""Install the rnov24 suite into agent tools, globally.

Targets:
  claude-code   -> ~/.claude/skills/<skill>/           (global skills)
  codex         -> ~/.codex/skills/<skill>/            (global skills)
  antigravity   -> an agy plugin named "rnov-skills", installed through
                   `agy plugin install` (falls back to printing the staging
                   path when the agy CLI is not available)

Usage:
  install.py --target claude-code [--target codex] [--mode copy|link]
  install.py --all [--dry-run]
  install.py --uninstall --target claude-code

Safety: the installer manages only directories it installed, recorded in a
manifest (.rnov24-skills-manifest.json) inside each target root. An existing
directory it did not install is never overwritten or removed unless --force
is given. Uninstall removes exactly what the manifest lists.

Validation: before installing, the installer regenerates the skill index
and the command files and validates the suite — every SKILL.md has frontmatter whose name
matches its directory and a non-empty description, every `scripts/<file>`
reference inside a skill resolves to that skill's own scripts/ folder
(or to the repo's suite-tooling scripts/), every command in
commands/commands.json names an existing skill and a section that exists
in that skill (with its anchor inside the section), and every bundled Python file
compiles. After installing, it verifies the installed copies carry the
same skill set and the same scripts. `install.py --check` runs both
checks without installing anything.
"""
import argparse, json, os, pathlib, py_compile, re, shutil, subprocess, sys, tempfile, time

ROOT = pathlib.Path(__file__).resolve().parent.parent
HOME = pathlib.Path.home()
MANIFEST = '.rnov24-skills-manifest.json'
TARGET_ROOTS = {
    'claude-code': HOME / '.claude' / 'skills',
    'codex': HOME / '.codex' / 'skills',
}

def command_names():
    import json as _json
    m = _json.loads((ROOT / 'commands' / 'commands.json').read_text(encoding='utf-8'))
    return sorted(c['name'] for c in m['commands'])

def skill_names():
    return sorted(d.name for d in (ROOT / 'skills').iterdir() if (d / 'SKILL.md').exists())

def version():
    v = ROOT / 'VERSION'
    return v.read_text().strip() if v.exists() else '0.0.0'


def parse_frontmatter(text):
    m = re.match(r'^---\n(.*?)\n---\n', text, re.S)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).splitlines():
        if ':' in line:
            k, v = line.split(':', 1)
            fm[k.strip()] = v.strip()
    return fm

def validate_suite():
    """Regenerate the index, then check the suite is installable.

    Returns a list of error strings (empty means valid).
    """
    errors = []
    r = subprocess.run([sys.executable, str(ROOT / 'scripts' / 'generate_index.py')],
                       capture_output=True, text=True)
    if r.returncode != 0:
        errors.append(f"generate_index.py failed: {(r.stderr or r.stdout).strip()}")
    r = subprocess.run([sys.executable, str(ROOT / 'scripts' / 'generate_commands.py')],
                       capture_output=True, text=True)
    if r.returncode != 0:
        errors.append(f"generate_commands.py failed: {(r.stderr or r.stdout).strip()}")
    for d in sorted((ROOT / 'skills').iterdir()):
        f = d / 'SKILL.md'
        if not f.exists():
            errors.append(f"{d.name}: SKILL.md missing")
            continue
        fm = parse_frontmatter(f.read_text(encoding='utf-8'))
        if not fm:
            errors.append(f"{d.name}: no frontmatter")
        elif fm.get('name', '').strip() != d.name:
            errors.append(f"{d.name}: frontmatter name is {fm.get('name')!r}")
        if not fm.get('description'):
            errors.append(f"{d.name}: frontmatter description empty")
        # every scripts/<file> mention must resolve inside this skill
        # or in the repo's suite-tooling scripts/. Only the suite's own
        # prose is scanned: SKILL.md and references/ (the vendored
        # brand-systems shelf is upstream text, not suite instructions).
        own_md = [f]
        refs_dir = d / 'references'
        if refs_dir.exists():
            own_md += [m for m in sorted(refs_dir.rglob('*.md'))
                       if 'brand-systems' not in m.parts]
        for md in own_md:
            for ref in sorted(set(re.findall(r'scripts/([A-Za-z0-9_.-]+)', md.read_text(encoding='utf-8')))):
                if ref in ('find_skill.py', 'generate_index.py', 'install.py'):
                    if not (ROOT / 'scripts' / ref).exists():
                        errors.append(f"{d.name}: suite-tooling reference scripts/{ref} missing")
                elif not (d / 'scripts' / ref).exists():
                    errors.append(f"{d.name}: scripts/{ref} (mentioned in {md.name}) not bundled in the skill")
        for py in sorted(d.rglob('*.py')):
            try:
                py_compile.compile(str(py), doraise=True)
            except py_compile.PyCompileError as e:
                errors.append(f"{d.name}: {py.name} does not compile: {e}")
    for py in sorted((ROOT / 'scripts').glob('*.py')):
        try:
            py_compile.compile(str(py), doraise=True)
        except py_compile.PyCompileError as e:
            errors.append(f"scripts/{py.name} does not compile: {e}")
    return errors

def check_installed(targets):
    """Compare installed copies against the repo. Returns error strings."""
    errors = []
    names = set(skill_names())
    for t in targets:
        if t == 'antigravity':
            continue  # agy state is checked via `agy plugin list` after install
        root = TARGET_ROOTS[t]
        if not root.exists():
            errors.append(f"[{t}] target root {root} does not exist")
            continue
        installed = {d.name for d in root.iterdir()
                     if d.is_dir() and (d / 'SKILL.md').exists()}
        for n in sorted(names - installed):
            errors.append(f"[{t}] skill {n} not installed")
        for n in sorted(names & installed):
            src = ROOT / 'skills' / n
            dst = root / n
            for py in sorted(src.rglob('*.py')):
                rel = py.relative_to(src)
                if not (dst / rel).exists():
                    errors.append(f"[{t}] {n}/{rel} missing in installed copy")
            for f in sorted(src.rglob('*.json')):
                rel = f.relative_to(src)
                if not (dst / rel).exists():
                    errors.append(f"[{t}] {n}/{rel} missing in installed copy")
        if t == 'claude-code':
            # Commands are user-level slash commands, not skills: they
            # live in ~/.claude/commands/, one .md file per command.
            cmd_root = HOME / '.claude' / 'commands'
            for n in command_names():
                if not (cmd_root / f'{n}.md').exists():
                    errors.append(f"[{t}] command /{n} not installed")
            man = load_manifest(TARGET_ROOTS['claude-code'])
            current = set(command_names())
            for n in sorted(set(man.get('commands', {}).keys()) - current):
                if (cmd_root / f'{n}.md').exists():
                    errors.append(f"[{t}] stale command /{n} still installed")
    return errors

def load_manifest(root):
    f = root / MANIFEST
    if f.exists():
        m = json.loads(f.read_text())
        m.setdefault('skills', {})
        m.setdefault('commands', {})
        return m
    return {'skills': {}, 'commands': {}, 'version': None}

def save_manifest(root, m):
    root.mkdir(parents=True, exist_ok=True)
    (root / MANIFEST).write_text(json.dumps(m, indent=1) + '\n')

def install_dir_target(target, mode, dry, force):
    root = TARGET_ROOTS[target]
    names = skill_names()
    man = load_manifest(root)
    done, skipped = [], []
    for n in names:
        src = ROOT / 'skills' / n
        dst = root / n
        if dst.exists() or dst.is_symlink():
            if n in man['skills'] or force:
                if not dry:
                    shutil.rmtree(dst) if dst.is_dir() and not dst.is_symlink() else dst.unlink()
            else:
                skipped.append(n); continue
        if not dry:
            root.mkdir(parents=True, exist_ok=True)
            if mode == 'link':
                dst.symlink_to(src, target_is_directory=True)
            else:
                shutil.copytree(src, dst)
            man['skills'][n] = {'mode': mode, 'at': int(time.time())}
        done.append(n)
    if not dry:
        man['version'] = version()
        save_manifest(root, man)
    print(f"[{target}] {'would install' if dry else 'installed'} {len(done)} skills -> {root}")
    if skipped:
        print(f"[{target}] skipped (exist, not installed by this tool, use --force): {', '.join(skipped)}")

def uninstall_dir_target(target, dry):
    root = TARGET_ROOTS[target]
    man = load_manifest(root)
    for n in list(man['skills']):
        dst = root / n
        if dst.exists() or dst.is_symlink():
            if not dry:
                shutil.rmtree(dst) if dst.is_dir() and not dst.is_symlink() else dst.unlink()
        man['skills'].pop(n, None)
        print(f"[{target}] removed {n}")
    if target == 'claude-code':
        uninstall_commands(dry, man)
    if not dry:
        if man['skills'] or man.get('commands'):
            save_manifest(root, man)
        else:
            (root / MANIFEST).unlink(missing_ok=True)

def install_commands(dry, force):
    """Claude Code user-level slash commands: ~/.claude/commands/<name>.md.

    Tracked in the same manifest as the skills (under 'commands').
    Codex has no slash-command equivalent, so commands install to
    Claude Code only; Antigravity gets them through the plugin.
    """
    cmd_root = HOME / '.claude' / 'commands'
    man = load_manifest(TARGET_ROOTS['claude-code'])
    done, skipped = [], []
    current_names = command_names()
    for n in current_names:
        src = ROOT / 'commands' / f'{n}.md'
        dst = cmd_root / f'{n}.md'
        if dst.exists() or dst.is_symlink():
            if n in man.get('commands', {}) or force:
                if not dry:
                    dst.unlink()
            else:
                skipped.append(n); continue
        if not dry:
            cmd_root.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
            man.setdefault('commands', {})[n] = {'at': int(time.time())}
        done.append(n)

    # Stale cleanup: remove any .md file recorded in manifest's commands but no longer in commands/commands.json
    recorded = list(man.get('commands', {}).keys())
    stale = sorted(n for n in recorded if n not in current_names)
    removed = []
    for n in stale:
        dst = cmd_root / f'{n}.md'
        if dst.exists() or dst.is_symlink():
            if not dry:
                dst.unlink()
            removed.append(n)
        if not dry:
            man.get('commands', {}).pop(n, None)

    # Leave foreign files alone and report them by name
    if cmd_root.exists():
        installed_and_recorded = set(current_names) | set(recorded)
        foreign = []
        for f in sorted(cmd_root.glob('*.md')):
            if f.stem not in installed_and_recorded:
                foreign.append(f.name)
        if foreign:
            print(f"[claude-code] foreign command files left alone: {', '.join(foreign)}")

    if not dry:
        man['version'] = version()
        save_manifest(TARGET_ROOTS['claude-code'], man)
    print(f"[claude-code] {'would install' if dry else 'installed'} {len(done)} commands -> {cmd_root}")
    if removed:
        print(f"[claude-code] {'would remove' if dry else 'removed'} {len(removed)} stale commands: {', '.join('/' + x for x in removed)}")
    if skipped:
        print(f"[claude-code] commands skipped (exist, not installed by this tool, use --force): {', '.join(skipped)}")

def uninstall_commands(dry, man):
    cmd_root = HOME / '.claude' / 'commands'
    for n in list(man.get('commands', {})):
        dst = cmd_root / f'{n}.md'
        if dst.exists() or dst.is_symlink():
            if not dry:
                dst.unlink()
        man['commands'].pop(n, None)
        print(f"[claude-code] removed command /{n}")

def install_antigravity(dry):
    names = skill_names()
    cmds = command_names()
    staging = pathlib.Path(tempfile.mkdtemp(prefix='rnov-skills-plugin-'))
    plugin = {'name': 'rnov-skills', 'version': version(),
              'skills': [f'skills/{n}' for n in names],
              'commands': [f'commands/{n}.md' for n in cmds]}
    (staging / 'plugin.json').write_text(json.dumps(plugin, indent=1) + '\n')
    for n in names:
        shutil.copytree(ROOT / 'skills' / n, staging / 'skills' / n)
    (staging / 'commands').mkdir()
    for n in cmds:
        shutil.copy2(ROOT / 'commands' / f'{n}.md', staging / 'commands' / f'{n}.md')
    agy = shutil.which('agy') or str(HOME / '.local' / 'bin' / 'agy')
    print(f"[antigravity] plugin staged at {staging} ({len(names)} skills, {len(cmds)} commands, plugin.json skills=array-of-paths)")
    if pathlib.Path(agy).exists():
        v = subprocess.run([agy, 'plugin', 'validate', str(staging)],
                           capture_output=True, text=True)
        if v.returncode != 0:
            print(f"[antigravity] plugin validation FAILED, not installing:\n{(v.stdout or v.stderr).strip()}")
            raise SystemExit(1)
        print('[antigravity] staged plugin validated')
    if dry:
        print('[antigravity] dry-run: agy plugin install not executed')
        return
    if not pathlib.Path(agy).exists():
        print(f"[antigravity] agy CLI not found; install manually: agy plugin install {staging}")
        return
    r = subprocess.run([agy, 'plugin', 'install', str(staging)], capture_output=True, text=True)
    print('[antigravity]', (r.stdout or r.stderr).strip().splitlines()[-1] if (r.stdout or r.stderr) else f'agy exited {r.returncode}')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--target', action='append', choices=['claude-code', 'codex', 'antigravity'])
    ap.add_argument('--all', action='store_true')
    ap.add_argument('--mode', choices=['copy', 'link'], default='copy')
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--force', action='store_true')
    ap.add_argument('--uninstall', action='store_true')
    ap.add_argument('--check', action='store_true',
                    help='validate the suite and the installed copies, install nothing')
    a = ap.parse_args()
    targets = ['claude-code', 'codex', 'antigravity'] if a.all else (a.target or [])
    if not targets:
        ap.error('choose --target or --all')
    errors = validate_suite()
    if a.check:
        errors += check_installed(targets)
    if errors:
        print('validation FAILED:')
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"validation passed ({len(skill_names())} skills, {len(command_names())} commands)")
    if a.check:
        print('installed copies match the repo')
        return 0
    for t in targets:
        if t == 'antigravity':
            if a.uninstall:
                print('[antigravity] uninstall via: agy plugin uninstall rnov-skills (or remove ~/.gemini/config/plugins/rnov-skills)')
            else:
                install_antigravity(a.dry_run)
        elif a.uninstall:
            uninstall_dir_target(t, a.dry_run)
        else:
            install_dir_target(t, a.mode, a.dry_run, a.force)
            if t == 'claude-code':
                install_commands(a.dry_run, a.force)
    if not a.dry_run:
        post = check_installed([t for t in targets if t != 'antigravity'])
        if post:
            print('post-install verification FAILED:')
            for e in post:
                print(f"  - {e}")
            return 1
        print('post-install verification passed: installed copies match the repo')
    return 0

if __name__ == '__main__':
    sys.exit(main())

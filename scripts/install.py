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
"""
import argparse, json, os, pathlib, shutil, subprocess, sys, tempfile, time

ROOT = pathlib.Path(__file__).resolve().parent.parent
HOME = pathlib.Path.home()
MANIFEST = '.rnov24-skills-manifest.json'
TARGET_ROOTS = {
    'claude-code': HOME / '.claude' / 'skills',
    'codex': HOME / '.codex' / 'skills',
}

def skill_names():
    return sorted(d.name for d in (ROOT / 'skills').iterdir() if (d / 'SKILL.md').exists())

def version():
    v = ROOT / 'VERSION'
    return v.read_text().strip() if v.exists() else '0.0.0'

def load_manifest(root):
    f = root / MANIFEST
    if f.exists():
        return json.loads(f.read_text())
    return {'skills': {}, 'version': None}

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
    if not dry:
        if man['skills']:
            save_manifest(root, man)
        else:
            (root / MANIFEST).unlink(missing_ok=True)

def install_antigravity(dry):
    names = skill_names()
    staging = pathlib.Path(tempfile.mkdtemp(prefix='rnov-skills-plugin-'))
    plugin = {'name': 'rnov-skills', 'version': version(),
              'skills': [f'skills/{n}' for n in names]}
    (staging / 'plugin.json').write_text(json.dumps(plugin, indent=1) + '\n')
    for n in names:
        shutil.copytree(ROOT / 'skills' / n, staging / 'skills' / n)
    agy = shutil.which('agy') or str(HOME / '.local' / 'bin' / 'agy')
    print(f"[antigravity] plugin staged at {staging} ({len(names)} skills, plugin.json skills=array-of-paths)")
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
    a = ap.parse_args()
    targets = ['claude-code', 'codex', 'antigravity'] if a.all else (a.target or [])
    if not targets:
        ap.error('choose --target or --all')
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
    return 0

if __name__ == '__main__':
    sys.exit(main())

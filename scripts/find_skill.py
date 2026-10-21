#!/usr/bin/env python3
"""Find the right skill for a task, fast, at any suite size.

Usage: find_skill.py "<task description words>" [--top N] [--phase PHASE]

Ranking is deliberately simple and explainable: exact skill-name match,
then keyword phrase match, then keyword token match, then description
token match. Prints the top candidates with the terms that matched, so
the router can show its work. Exits 2 with NO_CONFIDENT_MATCH when the
best score is below the threshold; the router treats that as "no skill
fits, do not force one".
"""
import argparse, json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
THRESHOLD = 4

def load_index():
    idx = ROOT / 'skills-index.json'
    if idx.exists():
        return json.loads(idx.read_text(encoding='utf-8'))
    sys.path.insert(0, str(ROOT / 'scripts'))
    from generate_index import collect
    return collect()

def tokens(text):
    return re.findall(r'[a-z0-9]+', text.lower())

def score(query, q_tokens, s):
    sc, hits = 0, []
    name = s['name'].lower()
    if query.strip() == name:
        return 100, ['exact name']
    for t in q_tokens:
        if t in name.split('-'):
            sc += 10; hits.append(f'name:{t}')
    for kw in s['keywords']:
        kwl = kw.lower()
        if kwl in query:
            sc += 8; hits.append(f'keyword:"{kw}"')
        else:
            for t in q_tokens:
                if t in tokens(kwl):
                    sc += 3; hits.append(f'keyword~{t}')
                    break
    desc_tokens = set(tokens(s['description']))
    for t in q_tokens:
        if t in desc_tokens:
            sc += 2; hits.append(f'desc:{t}')
    return sc, hits

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('query')
    ap.add_argument('--top', type=int, default=3)
    ap.add_argument('--phase')
    a = ap.parse_args()
    q = a.query.lower()
    q_tokens = tokens(q)
    results = []
    for s in load_index():
        if a.phase and s['phase'] != a.phase:
            continue
        sc, hits = score(q, q_tokens, s)
        if sc > 0:
            results.append((sc, s, hits))
    results.sort(key=lambda r: -r[0])
    if not results or results[0][0] < THRESHOLD:
        print('NO_CONFIDENT_MATCH')
        return 2
    for sc, s, hits in results[:a.top]:
        slash = ' [slash-only]' if s['slash_only'] else ''
        print(f"{sc:>3}  {s['name']} ({s['phase']}){slash}  <- {', '.join(dict.fromkeys(hits))}")
        print(f"     {s['path']}")
    return 0

if __name__ == '__main__':
    sys.exit(main())

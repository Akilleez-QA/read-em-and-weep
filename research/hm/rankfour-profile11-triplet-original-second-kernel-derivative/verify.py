#!/usr/bin/env python3
"""Bounded universal arithmetic and exact-byte checks; not an actual-map proof.

Run in a clean selected-only directory with exactly CORE + FROZEN.json.
Only standard-library operations on the ten bounded local files are used.
Every requirement is an explicit runtime test, including under python -O.
"""
from pathlib import Path
import datetime as dt
import hashlib
import json
import signal
import sys
import time

CORE = (
    'INPUTS.json', 'INPUTS.md', 'PROOF.md', 'PROVENANCE.md', 'README.md',
    'inputs/pr1228-PROOF.md', 'inputs/pr1234-PROOF.md',
    'inputs/pr1236-PROOF.md', 'verify.py',
)
REPO = 'Akilleez-QA/read-em-and-weep'
SOURCES = (
    ('pr1228', 1228, 'd3c9e9ff8d06977e6c3d3be6cd1c9ed71007a593',
     'research/hm/rankfour-profile11-triplet-first-kernel-structure/PROOF.md',
     12921, '4869bca9584bfa6876533516b61a6a14d6ca0fde97e80649828588b28e8f617e',
     '41ab2148d3ea13d07dcdfe2bf353a18c664bb848'),
    ('pr1234', 1234, '3d55622ece9a4bb9e20197dec560b298f1d03fb1',
     'research/hm/rankfour-profile11-triplet-simultaneous-kernel-three-exclusion/PROOF.md',
     16183, '9a164b510ccb9c529d2380c7e9e4880067bde0e86656b82e2c4649e09e5443c2',
     'c57074c1fbfaa61ef452a6d5e3a77dd0ff4ea70b'),
    ('pr1236', 1236, '092fc5f31dfaa5553ee5ea687f175ecba1878a2a',
     'research/hm/rankfour-profile11-triplet-first-kernel-forward-closure/PROOF.md',
     18052, '90081703a5e2a988a29e4d5bb918a93df4d4a954221a9bcba4cd858b0fa28137',
     'f77cfb52743be86e46e0c40570ec036e69aebaf3'),
)
ROOT = Path(__file__).resolve().parent
START = time.monotonic()
CHECKS = 0


def need(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise RuntimeError(message)


def bounded_time():
    need(time.monotonic() - START < 5.0, 'five-second runtime bound exceeded')


def timeout_handler(signum, frame):
    raise RuntimeError('five-second alarm exceeded')


def digest(data):
    return hashlib.sha256(data).hexdigest()


def read_bytes(rel):
    bounded_time()
    p = ROOT / rel
    need(not p.is_symlink() and p.is_file(), 'missing file or symlink: ' + rel)
    need(p.stat().st_size <= 65536, 'file exceeds 64 KiB: ' + rel)
    data = p.read_bytes()
    data.decode('utf-8', errors='strict')
    return data


def show_rep(v):
    return '+'.join((str(v[k]) if v[k] != 1 else '') + k
                    for k in DIMS if v.get(k, 0)) or '0'


DIMS = {'1': 1, 'W': 2, 'A': 3, 'S4': 4, 'D': 5,
        'T6': 6, 'V_alt': 3, 'P': 4, 'Wp': 2}
ADJ = {
    '1': {'W': 1}, 'W': {'1': 1, 'A': 1},
    'A': {'W': 1, 'S4': 1}, 'S4': {'A': 1, 'D': 1},
    'D': {'S4': 1, 'T6': 1}, 'T6': {'D': 1, 'V_alt': 1, 'P': 1},
    'V_alt': {'T6': 1}, 'P': {'T6': 1, 'Wp': 1}, 'Wp': {'P': 1},
}


def rep_dimension(v):
    return sum(DIMS[k] * v.get(k, 0) for k in DIMS)


def recurrence(current, previous):
    out = {k: 0 for k in DIMS}
    for source in DIMS:
        for target, mult in ADJ[source].items():
            out[target] += current.get(source, 0) * mult
    for k in DIMS:
        out[k] -= previous.get(k, 0)
        need(isinstance(out[k], int) and out[k] >= 0,
             'invalid universal multiplicity: ' + k)
    return {k: v for k, v in out.items() if v}


def bundle(terms):
    return (sum(DIMS[r] for r, degree in terms),
            sum(DIMS[r] * degree for r, degree in terms))


def main():
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(5)
    need(len(sys.argv) == 1, 'no checker arguments are supported')
    expected_root = {p for p in CORE if '/' not in p} | {'FROZEN.json', 'inputs'}
    root_entries = list(ROOT.iterdir())
    need(len(root_entries) == len(expected_root), 'root inventory count differs')
    need({p.name for p in root_entries} == expected_root, 'unselected root entry')
    input_dir = ROOT / 'inputs'
    need(input_dir.is_dir() and not input_dir.is_symlink(), 'invalid inputs directory')
    input_entries = list(input_dir.iterdir())
    need(len(input_entries) == 3, 'inputs must contain exactly three originals')
    need({p.name for p in input_entries} == {p.split('/')[1] for p in CORE if '/' in p},
         'input inventory differs')
    original = {p: read_bytes(p) for p in (*CORE, 'FROZEN.json')}
    need(sum(map(len, original.values())) < 262144, 'packet byte bound exceeded')
    frozen = json.loads(original['FROZEN.json'])
    need(frozen['schema'] == 'original-second-kernel-derivative-freeze-v1', 'freeze schema')
    entries = frozen['selected_core']
    need(len(entries) == len(CORE), 'selected-core count')
    need([x['path'] for x in entries] == sorted(CORE), 'selected-core exact ordered paths')
    for row in entries:
        data = original[row['path']]
        need(len(data) == row['utf8_bytes'], 'frozen length: ' + row['path'])
        need(digest(data) == row['sha256'], 'frozen digest: ' + row['path'])
    inventory = ''.join(row['sha256'] + '  ' + row['path'] + '\n' for row in entries)
    need(digest(inventory.encode('utf-8')) == frozen['core_sha256'], 'core aggregate digest')
    print('PASS exact selected-only inventory: 9 core files + FROZEN.json')
    print('CORE SHA256 ' + frozen['core_sha256'])
    print('FROZEN.json SHA256 ' + digest(original['FROZEN.json']))
    inputs = json.loads(original['INPUTS.json'])
    need(inputs['schema'] == 'original-second-kernel-derivative-inputs-v1', 'input schema')
    rows = inputs['sources']
    need(len(rows) == 3 and [r['id'] for r in rows] == [r[0] for r in SOURCES], 'source set')
    for row, expected in zip(rows, SOURCES):
        sid, pr, commit, path, length, sha256, blob = expected
        local = 'inputs/' + sid + '-PROOF.md'
        need((row['id'], row['pr'], row['commit'], row['path'], row['utf8_bytes'],
              row['sha256'], row['git_blob_sha1']) == expected, 'source identity: ' + sid)
        need(row['repository'] == REPO and row['local_path'] == local, 'source location')
        data = original[local]
        need(len(data) == length and digest(data) == sha256, 'complete source bytes: ' + sid)
        git = hashlib.sha1(b'blob ' + str(len(data)).encode('ascii') + b'\0' + data).hexdigest()
        need(git == blob, 'recomputed Git blob: ' + sid)
        need(row['immutable_url'] == 'https://github.com/' + REPO + '/blob/' + commit + '/' + path,
             'immutable source URL')
        need(row['git_blob_url'] == 'https://api.github.com/repos/' + REPO + '/git/blobs/' + blob,
             'blob source URL')
        request = row['path_request']
        need(request['tool'] == 'mcp__codex_apps__github_fetch_file', 'path read tool')
        need(request['args'] == {'repository_full_name': REPO, 'path': path,
                                'ref': commit, 'encoding': 'base64'}, 'complete exact-ref request')
        request2 = row['blob_request']
        need(request2['tool'] == 'mcp__codex_apps__github_fetch_blob', 'separate blob read tool')
        need(request2['args'] == {'repository_full_name': REPO, 'blob_sha': blob}, 'blob request')
        for req in (request, request2):
            t0 = dt.datetime.fromisoformat(req['requested_at'].replace('Z', '+00:00'))
            t1 = dt.datetime.fromisoformat(req['completed_at'].replace('Z', '+00:00'))
            need(t0.utcoffset() == dt.timedelta(0) and t1.utcoffset() == dt.timedelta(0), 'UTC')
            need(t0 <= t1, 'request interval order')
        need(set(row['authentication']) == {
            'complete_path_bytes_equal_complete_blob_bytes', 'strict_utf8',
            'sha256_matches_expected', 'recomputed_git_blob_matches_path_response'}, 'auth fields')
        need(all(v is True for v in row['authentication'].values()), 'auth result')
        print('PASS ' + sid + ' complete UTF-8 bytes=' + str(length) + ' Git blob=' + blob)
    print('NOTE remote response comparisons are author evidence; replay checks retained source bytes.')
    for k in DIMS:
        need(rep_dimension(ADJ[k]) == 2 * DIMS[k], 'adjacency dimension ' + k)
        for j in DIMS:
            need(ADJ[k].get(j, 0) == ADJ[j].get(k, 0), 'adjacency reciprocity')
    H = [{'1': 1}, {'W': 1}]
    for n in range(1, 12):
        H.append(recurrence(H[n], H[n - 1]))
        need(rep_dimension(H[-1]) == n + 2, 'symmetric-power dimension')
    need(H[2] == {'A': 1}, 'H2')
    need(H[9] == {'S4': 1, 'T6': 1}, 'H9')
    need(H[12] == {'1': 1, 'A': 1, 'D': 1, 'P': 1}, 'H12')
    need(H[9].get('W', 0) == 0, 'Hom O(-10) to W(-1) vanishes')
    need(H[2].get('D', 0) + H[2].get('P', 0) == 0, 'Hom O(-10) to (D+P)(-8) vanishes')
    need(H[12].get('1', 0) == 1, 'degree-twelve invariant line')
    for n in (2, 9, 12):
        print('PASS universal H' + str(n) + '=' + show_rep(H[n]))
    for degree in (4, 9):
        need(max(-degree - 1, 0) == 0, 'ordinary H1 vanishing')
    need(-1 - (-10) == 9 and -8 - (-10) == 2 and 2 - (-10) == 12, 'Hom twists')
    need(-6 - (-10) == 4 and -1 - (-10) == 9, 'Ext twists')
    Fhat = bundle([('D', -6), ('P', -6), ('1', -10)])
    Bhat = bundle([('D', -6), ('P', -6)])
    Chat = bundle([('S4', -7), ('V_alt', -8)])
    K = bundle([('V_alt', -4), ('P', -4), ('T6', -5)])
    E = bundle([('W', -1)])
    I = bundle([('W', -1), ('1', -10)])
    need(Fhat == (10, -64) and Bhat == (9, -54), 'Fhat and Bhat rank/degree')
    need(Chat == (7, -52) and K == (13, -58), 'Chat and K rank/degree')
    need((Fhat[0] - Chat[0], Fhat[1] - Chat[1]) == I == (3, -12), 'coherent-image arithmetic')
    quotient = (K[0] - Fhat[0], K[1] - Fhat[1])
    need(quotient == (3, 6), 'K/Fhat=A(2) arithmetic')
    target = (quotient[0], quotient[1] - 2 * quotient[0])
    need(target == (3, 0), 'saturated normal A O arithmetic')
    need((target[0] - E[0], target[1] - E[1]) == (1, 2), 'Euler quotient O(2)')
    need(target[1] - I[1] == 12 and 12 // 12 == 1 and 12 % 12 == 0,
         'defect degree and minimum-orbit arithmetic')
    print('PASS Hom/Ext twists; ordinary H1(O(4))=H1(O(9))=0')
    print('PASS ranks/degrees: Fhat (10,-64), Chat (7,-52), I (3,-12), K (13,-58), normal (3,0)')
    print('PASS scalar-row degree 12; minimum-orbit arithmetic gives one reduced orbit in the proof')
    for rel, data in original.items():
        need(read_bytes(rel) == data, 'file changed during replay: ' + rel)
    bounded_time()
    signal.alarm(0)
    print('PASS all ' + str(CHECKS) + ' explicit runtime checks; optimization=' + str(sys.flags.optimize))
    print('LIMIT: no actual-instance evaluation; no actual-map, branch-closure, or algebraicity verification.')
    print('PASS selected bytes unchanged during replay')


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        print('FAIL ' + type(exc).__name__ + ': ' + str(exc), file=sys.stderr)
        sys.exit(1)

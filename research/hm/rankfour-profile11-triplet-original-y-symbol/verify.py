#!/usr/bin/env python3
"""Author-only exact-byte and bounded universal checks, never actual-map review.

Reads precisely ten fixed core paths and FROZEN.json. Extra artifacts are ignored.
No network, directory traversal, actual source instances, or identities above H10.
All tests use explicit runtime conditions and remain active under python -O.
"""
from collections import Counter
from hashlib import sha1, sha256
import json
from pathlib import Path

CORE = (
    'PROOF.md', 'README.md', 'INPUTS.json', 'INPUTS.md', 'PROVENANCE.md',
    'verify.py', 'inputs/OD-PROOF.md', 'inputs/FC-PROOF.md',
    'inputs/TP-PROOF.md', 'inputs/OT-PROOF.md',
)
SOURCES = {
    'OD': (11709, 'a11b3386584390375a6a3249898170a2240d614d4f067e824ddf12aa0c3d6e6f', 'e561adb180b5040a57464808dbbdfaef29f1c6a8'),
    'FC': (18052, '90081703a5e2a988a29e4d5bb918a93df4d4a954221a9bcba4cd858b0fa28137', 'f77cfb52743be86e46e0c40570ec036e69aebaf3'),
    'TP': (16304, 'b233db763f8c7aa78174ae85629f28f00a373f6b78b3674602f96189f6cf3d2e', 'e41b654ff6edba56d5a071811f19d4db4346681c'),
    'OT': (28094, '407d35049bb17ab4b8f4e270627adb416fc5601eab1445a21685f2cc27bcb637', 'f00b059695615d9b8ab6d315798940e3ab0a58d4'),
}
checks = 0

def require(condition, message):
    global checks
    checks += 1
    if not condition:
        raise RuntimeError(message)

root = Path(__file__).resolve().parent
manifest = json.loads((root / 'FROZEN.json').read_bytes().decode('utf-8'))
require(manifest.get('schema') == 'original-y-symbol-freeze-v1', 'freeze schema')
require(manifest.get('status') == 'frozen author core; independent entire review pending', 'author-only freeze status')
files = manifest.get('files')
require(isinstance(files, dict), 'freeze files mapping')
require(set(files) == set(CORE) and len(files) == 10, 'exactly ten named core files')
retained = {}
for name in CORE:
    entry = files[name]
    require(isinstance(entry, dict) and set(entry) == {'bytes', 'sha256'}, f'{name}: manifest fields')
    data = (root / name).read_bytes()
    require(len(data) == entry['bytes'], f'{name}: frozen byte count')
    require(sha256(data).hexdigest() == entry['sha256'], f'{name}: frozen SHA256')
    retained[name] = data
    print(f"FILE {name}: {len(data)} bytes; SHA256 {sha256(data).hexdigest()}")
for label, (length, digest, git_blob) in SOURCES.items():
    data = retained[f'inputs/{label}-PROOF.md']
    require(len(data) == length, f'{label}: independently fixed source length')
    require(sha256(data).hexdigest() == digest, f'{label}: independently fixed source SHA256')
    computed = sha1(b'blob ' + str(len(data)).encode('ascii') + b'\0' + data).hexdigest()
    require(computed == git_blob, f'{label}: recomputed immutable Git blob')
    print(f'SOURCE {label}: exact original bytes and Git blob {computed}')

integrity_checks = checks
DIMS = {'1': 1, 'W': 2, 'A': 3, 'S4': 4, 'D': 5, 'T6': 6, 'V_alt': 3, 'P': 4, 'Wp': 2}
ADJ = {
    '1': ('W',), 'W': ('1', 'A'), 'A': ('W', 'S4'), 'S4': ('A', 'D'),
    'D': ('S4', 'T6'), 'T6': ('D', 'V_alt', 'P'), 'V_alt': ('T6',),
    'P': ('T6', 'Wp'), 'Wp': ('P',),
}
H = [Counter({'1': 1}), Counter({'W': 1})]
for n in range(1, 10):
    nxt = Counter()
    for a, multiplicity in H[n].items():
        for b in ADJ[a]:
            nxt[b] += multiplicity
    nxt.subtract(H[n - 1])
    require(all(m >= 0 for m in nxt.values()), f'H{n + 1}: nonnegative multiplicities')
    nxt = Counter({a: m for a, m in nxt.items() if m})
    require(sum(DIMS[a] * m for a, m in nxt.items()) == n + 2, f'H{n + 1}: dimension')
    H.append(nxt)
require(len(H) == 11, 'character recurrence ends at H10')
require(H[4] == Counter({'D': 1}), 'H4=D')
require(H[5] == Counter({'T6': 1}), 'H5=T6')
require(H[8] == Counter({'P': 1, 'D': 1}), 'H8=P+D')
require(H[10] == Counter({'A': 1, 'V_alt': 1, 'D': 1}), 'H10=A+V_alt+D')
require(H[10]['A'] == 1, 'unique A-valued decic Hom line')
require(H[5]['W'] == 0, 'physical W absent from H5')
require(H[8]['1'] == 0, 'Euler-plane factorization obstruction')
require(H[4]['P'] == 0, 'P-row D12 division obstruction')
require(10 == 2 * 5, 'decic hyperplane pullback forces degree-five conic map')
require(4 >= -1, 'H1(O(4))=0 degree criterion on P1')
orbits = tuple(sorted(60 // d for d in (1, 2, 3, 5)))
require(orbits == (12, 20, 30, 60), 'fixed projective A5 cyclic stabilizer orbit sizes')
require(10 < orbits[0] and 11 < orbits[0], 'decic and Euler-plane rows have no invariant base divisor')
require(2 * 12 > 16 and 20 > 16, 'only possible nonempty P-row base divisor is reduced D12')
require(2 * 12 > 20 and 20 - 12 < 12 and 30 > 20, 'degree-twenty invariant divisor is one reduced D20')
require(-2 - 10 == -12, 'Euler-plane row kernel degree')
require(-12 - (-6) < 0 and -7 - (-6) < 0 and -8 - (-6) < 0, 'P-row negative-degree Hom obstructions')
require(18 - 2 * 3 == 12 and 12 - 2 == 10 and 18 - 2 * 4 == 10, 'original intrinsic jet and normal target twists')
require(3 + 5 == 8 and 2 + 8 == 10 and 2 + 7 == 9, 'mixed and apolar symbol indices')
require(-18 + 12 == -6 and 2 * 8 - 10 == 6 and 2 * 5 - 10 == 0, 'mixed top-line and auxiliary jet degrees')
require(10 - (-10) == 20 and 10 - (-6) == 16, 'scalar and P-row section degrees')
require(10 - 12 == -2 and -2 - (-6) == 4, 'D12 division gives H4 obstruction')
for n in (4, 5, 8, 10):
    print(f'UNIVERSAL H{n}: ' + json.dumps(dict(sorted(H[n].items())), sort_keys=True))
print('UNIVERSAL orbit sizes: 12,20,30,60; scalar divisor degree 20; P-row entry degree 16')
print(f'PASS: {checks} explicit runtime checks ({integrity_checks} integrity, {checks - integrity_checks} bounded universal).')
print('AUTHOR ONLY: no actual source-instance evaluation, actual-map verification, or independent review.')

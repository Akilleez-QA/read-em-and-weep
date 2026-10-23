#!/usr/bin/env python3
"""Independent fixed ten-source coverage audit; no source-instance computation."""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import json

ROOT = Path(__file__).resolve().parent
INPUTS = ROOT / 'audit-inputs'

def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def blob(path):
    data = path.read_bytes()
    return hashlib.sha1(('blob ' + str(len(data))).encode() + bytes([0]) + data).hexdigest()

for name, expected in {
    'PROOF.md': '8597b61030fec7dde2e8adc6841110d65554d145f0a0f8a6cc3a32adc7aa0162',
    'coverage.json': '45548a94f6b36d6ab2e599d7676e568be85f2bfbcac2c98d37eb34de11b46fd9',
    'verify.py': '10b6cbd74c59ead7e016fac2c9ea02b6b58850d788da9a6f91543a7b14de02e7',
    'characters.py': '25d2c28c294298624ee50ce73b2a55422913f7e78b4817c7cb6e813e5004f1fc',
    'REPRODUCE.md': 'a9f6fa60fbf631cc421d6a10d74d623b86bc0f138671a5b5a6bcd9d3fcd913dd',
}.items():
    assert sha256(ROOT / name) == expected, name
for name, expected in {
    'one-one-endpoint-necessary-pairs.json': 'fe0afa410d89340d3082dc814277f89fbb582c19',
    'rank-three-quotient-frontier-144.json': '8b5971092f9ef762584912609fd5e9301c4e271d',
    'ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md': 'b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3',
    'NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md': 'd7506dae49b4be43230450c4132bd5db91f137ef',
}.items():
    assert blob(INPUTS / name) == expected, name

catalog = json.loads((INPUTS / 'one-one-endpoint-necessary-pairs.json').read_text())
frontier = json.loads((INPUTS / 'rank-three-quotient-frontier-144.json').read_text())['cases']
manifest = json.loads((ROOT / 'coverage.json').read_text())
assert manifest['original_commit'] == 'db51525015bb7c5e825833d550d08dedf6f6ea96'
assert manifest['source_index'] == 113
assert manifest['stable_label'] == 'G3.11.ad509d55173f'
label_rows = [row for row in frontier if row['id'] == manifest['stable_label']]
assert len(label_rows) == 1 and label_rows[0]['source_index'] == 113
original = catalog[113]
for row in (original, label_rows[0]):
    assert row['A'] == [[-10, 'one'], [2, 'one'], [16, 'one']]
    assert row['B'] == [[-18, 'one'], [-4, 'one'], [8, 'one']]
assert original['defect'] == label_rows[0]['original_defect'] == 0

rows = manifest['coverage']
assert [row['tuple'] for row in rows] == original['compatible_E_types']
assert len(rows) == len({tuple(row['tuple']) for row in rows}) == 10
assert {row['name'] for row in rows} == {'ff', 'ef', 'ee', 'cf', 'ce', 'cc', 'bf', 'be', 'bc', 'bb'}
for row in rows:
    a, b, c, d, e, f, g, h = row['tuple']
    assert (a, d, g, h) == (0, 0, 0, 1) and b + c + e + f == 2
    assert row['name'] == 'b' * b + 'c' * c + 'e' * e + 'f' * f
    multiplicities = {2: 3*(c+g+h-1)+4*(d+e+g+h)+5*(f+g),
                      3: 2*a+6*b, 4: 3*c+4*d, 5: 2*e, 8: f, 9: 2*g, 10: h}
    assert sum(multiplicities.values()) == 17
    assert sum(-degree * rank for degree, rank in multiplicities.items()) == -54

# Independent A5 even-character table, not imported from characters.py.
# (x,y) denotes x+y*sqrt(5). Classes: identity, order 2, order 3, two order-5 classes.
def q(x, y=0): return F(x), F(y)
def add(x, y): return x[0]+y[0], x[1]+y[1]
def mul(x, y): return x[0]*y[0]+5*x[1]*y[1], x[0]*y[1]+x[1]*y[0]
def scale(x, k): return x[0]*k, x[1]*k
def vadd(x, y): return tuple(add(a, b) for a, b in zip(x, y))
def vsub(x, y): return vadd(x, tuple(scale(a, -1) for a in y))
def vmul(x, y): return tuple(mul(a, b) for a, b in zip(x, y))
phi, conjugate = q(F(1, 2), F(1, 2)), q(F(1, 2), F(-1, 2))
irreps = {
    'one': tuple(q(n) for n in [1, 1, 1, 1, 1]),
    'A': (q(3), q(-1), q(0), phi, conjugate),
    'V': (q(3), q(-1), q(0), conjugate, phi),
    'P': tuple(q(n) for n in [4, 0, 1, -1, -1]),
    'D': tuple(q(n) for n in [5, 1, -1, 0, 0]),
}
def inner(x, y):
    value = q(0)
    for count, a, b in zip([1, 15, 20, 12, 12], x, y):
        value = add(value, scale(mul(a, b), F(count, 60)))
    return value
assert all(inner(x, y) == q(a == b)
           for a, x in irreps.items() for b, y in irreps.items())

# Clebsch-Gordan: Sym(2n+2) = (Sym2-1) Sym(2n) - Sym(2n-2).
even = [irreps['one'], irreps['A']]
for n in range(1, 9):
    even.append(vsub(vmul(vsub(irreps['A'], irreps['one']), even[-1]), even[-2]))
def decompose(char):
    result = {}
    for name, irrep in irreps.items():
        x, y = inner(char, irrep)
        assert y == 0 and x.denominator == 1
        result[name] = int(x)
    return result
assert decompose(even[2]) == {'one': 0, 'A': 0, 'V': 0, 'P': 0, 'D': 1}
target = decompose(vadd(even[2], even[9]))
assert target == {'one': 0, 'A': 1, 'V': 1, 'P': 2, 'D': 2}
for row in rows:
    if row['kind'] != 'strict_top': continue
    a, b, c, d, e, f, g, h = row['tuple']
    top = {'V': c+g+h-1, 'P': d+e+g+h, 'D': f+g}
    assert top == ({'V': 0, 'P': 3, 'D': 0} if row['name'] == 'ee'
                   else {'V': 2, 'P': 1, 'D': 0})
    assert any(amount > target[name] for name, amount in top.items())
assert {row['name'] for row in rows if row['kind'] == 'strict_top'} == {'ee', 'cc'}

# These exact blobs were independently re-fetched at the immutable URLs.
pins_path = ROOT / 'source-proof-pins.json'
assert sha256(pins_path) == '5d4c48b22022606a9fe8cb4590f9ecf1f12e5aa90383e91f9f9b8c927c79e741'
pins = json.loads(pins_path.read_text())
assert len(pins) == 7
for name, pin in pins.items():
    assert blob(INPUTS / name) == pin['git_blob']
    assert sha256(INPUTS / name) == pin['sha256']
proof = (ROOT / 'PROOF.md').read_text()
source_files = {'ff': 'PR848-FF.md', 'ef': 'PR846.md', 'ce': 'PR846.md',
                'be': 'PR846.md', 'cf': 'PR868-CF.md', 'bc': 'PR874-BC.md',
                'bb': 'PR877-BB.md', 'bf': 'PR881-BF.md'}
for row in rows:
    exact_tuple = '(' + ','.join(map(str, row['tuple'])) + ')'
    assert exact_tuple in proof
    if row['name'] in source_files:
        assert row['kind'] == 'whole_source'
        pin = pins[source_files[row['name']]]
        assert row['url'] == pin['url']
        assert row['url'] == ('https://github.com/Akilleez-QA/read-em-and-weep/blob/'
                              + row['commit'] + '/' + row['path'])
        assert row['url'] in proof
        assert exact_tuple in (INPUTS / source_files[row['name']]).read_text()
dependency = pins['PR861-CF-REDUCTION.md']['url']
assert dependency in proof and dependency in (INPUTS / 'PR868-CF.md').read_text()
assert pins['PR881-BF.md']['sha256'] == 'f900fa54aa5ad18adc94bd7552b94891d77ccf1c5797af05414dbd8b851b4f63'
print('PASS: exact-version ten-source coverage, original decoder and endpoints, independent even characters, seven immutable source-proof blobs and explicit PR861 linkage.')
print('The geometric theorem scopes are checked in REVIEW.md, not inferred from string matches. No current global count is computed.')

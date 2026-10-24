#!/usr/bin/env python3
"""Independent fixed representation checks; no author-verifier import or bundle search."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent

def q(a, b=0):
    return F(a), F(b)

def add(a, b):
    return a[0]+b[0], a[1]+b[1]

def mul(a, b):
    return a[0]*b[0]+5*a[1]*b[1], a[0]*b[1]+a[1]*b[0]

def scale(c, a):
    return c*a[0], c*a[1]

def conjugate(a):
    return a[0], -a[1]

def power(a, n):
    result = q(1)
    for _ in range(n):
        result = mul(result, a)
    return result

def symmetric_trace(n, x):
    # Closed binomial formula, not the author's McKay/character recurrence.
    if n < 0:
        return q(0)
    result = q(0)
    for k in range(n//2+1):
        result = add(result, scale((-1)**k*comb(n-k, k), power(x, n-2*k)))
    return result

phi = q(F(1, 2), F(1, 2))
psi = conjugate(phi)
traces = [q(2), q(-2), phi, scale(-1, phi), psi, scale(-1, psi), q(1), q(-1), q(0)]
sizes = [1, 1, 12, 12, 12, 12, 20, 20, 30]

def sym(n):
    return [symmetric_trace(n, x) for x in traces]

def tensor(a, b):
    return [mul(x, y) for x, y in zip(a, b)]

def linear(*terms):
    result = [q(0)]*9
    for coefficient, values in terms:
        result = [add(x, scale(coefficient, y)) for x, y in zip(result, values)]
    return result

def inner(a, b):
    total = q(0)
    for size, x, y in zip(sizes, a, b):
        total = add(total, scale(size, mul(x, y)))
    answer = scale(F(1, 120), total)
    if answer[1] or answer[0].denominator != 1:
        raise AssertionError(('not an integer character multiplicity', answer))
    return int(answer[0])

chars = {
    '1': sym(0), 'W': sym(1), 'Wp': [conjugate(x) for x in sym(1)],
    'A': sym(2), 'V': [conjugate(x) for x in sym(2)],
    'S': sym(3), 'D': sym(4), 'T': sym(5),
}
chars['P'] = linear((1, sym(6)), (-1, chars['V']))
if chars['P'] != [q(x) for x in (4, 4, -1, -1, -1, -1, 1, 1, 0)]:
    raise AssertionError('physical even four-space marking')
if tensor(chars['W'], chars['P']) != linear((1, chars['Wp']), (1, chars['T'])):
    raise AssertionError('physical other-doublet marking')
for name, a in chars.items():
    for other, b in chars.items():
        if inner(a, b) != int(name == other):
            raise AssertionError(('orthogonality', name, other))

def decompose(character):
    return {name: m for name, values in chars.items() if (m := inner(character, values))}

def check(actual, expected, label):
    if actual != expected:
        raise AssertionError((label, actual, expected))


# The immutable inputs are authenticated independently of the author's checker.
authenticated = []
for entry in json.loads((ROOT/'INPUTS.json').read_text()):
    data = (ROOT/entry['file']).read_bytes()
    check(len(data), entry['bytes'], entry['file']+' bytes')
    check(hashlib.sha256(data).hexdigest(), entry['sha256'], entry['file']+' sha256')
    check(hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest(), entry['git_blob_sha1'], entry['file']+' git blob')
    authenticated.append(entry['file'])

dims = {r: int(c[0][0]) for r, c in chars.items()}
parity = {r: 0 if c[1] == c[0] else 1 for r, c in chars.items()}

def cohom(blocks, twist, kind='chi'):
    terms = []
    for r, e in blocks:
        i = e + twist
        if i >= 0 and kind != 'h1':
            terms.append((1, tensor(chars[r], sym(i))))
        elif i <= -2 and kind != 'h0':
            terms.append((1 if kind == 'h1' else -1,
                          tensor(chars[r], sym(-i-2))))
    return linear(*terms)

def dec(blocks, twist, kind='chi'):
    return decompose(cohom(blocks, twist, kind))

def chi_difference(source, quotient, twist):
    return linear((1, cohom(source, twist)), (-1, cohom(quotient, twist)))

def block4(chi4, top, lower):
    # K = top O(-3) + R4 O(-4) + lower, with lower degree <= -5.
    return decompose(linear((1, chi4), (-1, cohom(top, 4, 'h0')),
                            (1, cohom(lower, 4, 'h1'))))

sources = {
    'D': [('D', -2), ('Wp', -3), ('T', -3), ('V', -4), ('1', -8)],
    'P': [('P', -2), ('Wp', -3), ('T', -3), ('V', -4), ('Wp', -5)],
    'V': [('V', -2), ('Wp', -3), ('T', -3), ('V', -4), ('V', -4)],
    'Z': [('Wp', -3), ('T', -3), ('T', -3), ('V', -4)],
}
for label, blocks in sources.items():
    check(sum(dims[r] for r, e in blocks), 17, label+' rank')
    check(sum(dims[r]*e for r, e in blocks), -54, label+' degree')
    check(dec(blocks, 3), {'Wp': 1, 'T': 2}, label+' cubic Euler')
    check(dec(blocks, 4), {'V': 3, 'D': 2, 'P': 3}, label+' quartic Euler')

# Exhaust only universal irreducible target Hom mechanisms in a forced interval.
# There is no global bundle candidate generator here.
hom_report = {}
for r in ('1', 'W', 'Wp'):
    for e in range(-8, 1):
        if e % 2 != parity[r]:
            continue
        actual = {
            label: sum(inner(chars[s], tensor(chars[r], sym(e-d))) for s, d in src)
            for label, src in sources.items()
        }
        expected = dict.fromkeys(sources, 0)
        if (r, e) == ('1', -8) or (r, e) == ('W', -7):
            expected['D'] = 1
        elif (r, e) == ('Wp', -5):
            expected['P'] = 1
        elif (r, e) == ('Wp', -3):
            expected = dict.fromkeys(sources, 1)
        elif (r, e) == ('Wp', -1):
            expected = dict.fromkeys(sources, 3)
        check(actual, expected, ('negative/scalar Hom', r, e))
        hom_report[f'{r}:{e}'] = actual
# The exceptional W(-7) Hom comes only from one scalar source line.
check([s for s, d in sources['D']
       if inner(chars[s], tensor(chars['W'], sym(-7-d)))], ['1'],
      'W(-7) row has source rank one')
check(2*3+2*(-1)+9*(-1), -5, 'e=-1 scalar inequality left side')
if not -5 > -8:
    raise AssertionError('e=-1 must contradict nonnegative defect')

qminus3 = [('W', 3), ('Wp', -3)]
qminus5 = [('W', 3), ('Wp', -5)]
qscalarW = [('W', 3), ('1', 2), ('1', -8)]
qscalarWp = [('Wp', 3), ('1', 2), ('1', -8)]
for e in (-3, -5):
    check(dec([('Wp', 3), ('Wp', e)], 3, 'h0')['T'], 1,
          ('Wp top fails two T channels', e))
check(dec(qminus3, 3, 'h0'), {'Wp': 2, 'T': 2}, 'W3 Wp-3 cubic visibility')
check(dec(qminus5, 3, 'h0'), {'Wp': 1, 'T': 2}, 'W3 Wp-5 cubic visibility')
check(dec(qscalarW, 3, 'h0'), {'Wp': 1, 'T': 3}, 'W scalar cubic visibility')
check(dec(qscalarWp, 3, 'h0'), {'W': 1, 'Wp': 1, 'S': 1, 'T': 2},
      'Wp scalar cubic visibility')

quotients = {'minus3': qminus3, 'minus5': qminus5,
             'scalarW': qscalarW, 'scalarWp': qscalarWp}
expected_euler = {
    'minus3': ({'Wp': -1}, {'V': 2, 'D': 1}),
    'minus5': ({'Wp': 1}, {'V': 2, 'D': 1, 'P': 1}),
    'scalarW': ({'S': 1, 'T': -1}, {'A': 1, 'V': 1, 'D': 1}),
    'scalarWp': ({'W': -1}, {'1': -1, 'V': 1, 'D': 1, 'P': 1}),
}
for label, quotient in quotients.items():
    for t, expected in zip((3, 4), expected_euler[label]):
        check(decompose(chi_difference(sources['D'], quotient, t)), expected,
              (label, 'Euler K', t))
for quotient in (qminus3, qminus5):
    check(dec(quotient, 1, 'h0'), {'S': 1, 'T': 1}, 'doublet cubic derivative target')
    check(dec(quotient, 2, 'h0'), {'V': 1, 'D': 1, 'P': 1}, 'doublet quartic derivative target')
check(dec(qscalarW, 1, 'h0'), {'S': 2, 'T': 1}, 'W scalar cubic derivative target')
check(dec(qscalarWp, 1, 'h0'), {'S': 2, 'T': 1}, 'Wp scalar cubic derivative target')
check(dec(qscalarW, 2, 'h0'), {'V': 1, 'D': 2, 'P': 1}, 'W scalar quartic derivative target')
check(dec(qscalarWp, 2, 'h0'), {'A': 1, 'D': 2, 'P': 1}, 'Wp scalar quartic derivative target')

# Since dim H1(K(3)) <= 6, each lower block has j <= 10:
# dim H1(R O(-j+3)) = dim(R)*(j-4). Check the fixed nine-irrep
# cohomology table, then use explicit coefficient comparisons, not bundle search.
targets = {
    'Wp': {'Wp': 1}, 'S+Wp': {'S': 1, 'Wp': 1},
    'W': {'W': 1}, 'S+W': {'S': 1, 'W': 1}, 'T': {'T': 1},
}
expected_atoms = {
    'Wp': {('Wp', -5)},
    'S+Wp': {('Wp', -5), ('S', -5), ('1', -8)},
    'W': {('W', -5), ('1', -6)},
    'S+W': {('W', -5), ('S', -5), ('1', -6), ('A', -6), ('W', -7), ('1', -8)},
    'T': {('T', -5), ('V', -6), ('Wp', -7), ('1', -10)},
}
atom_report = {}
for name, target in targets.items():
    atoms = []
    for j in range(5, 11):
        for r in chars:
            if j % 2 != parity[r]:
                continue
            values = dec([(r, -j)], 3, 'h1')
            if all(v <= target.get(k, 0) for k, v in values.items()):
                atoms.append((r, -j))
    check(set(atoms), expected_atoms[name], ('complete cohomology atom table', name))
    atom_report[name] = [{'block': b, 'H1_at_3': dec([b], 3, 'h1'),
                          'H1_at_4': dec([b], 4, 'h1')} for b in atoms]

chi_m3 = chi_difference(sources['D'], qminus3, 4)
check(block4(chi_m3, [], [('Wp', -5)]), {'V': 2, 'D': 1},
      'minus3 zero cubic kernel')
check(block4(chi_m3, [('S', -3)], [('Wp', -5), ('S', -5)]), {'A': -1, 'V': 2},
      'minus3 S cubic rejected lower option')
check(block4(chi_m3, [('S', -3)], [('Wp', -5), ('1', -8)]), {'V': 2},
      'minus3 S cubic genuine lower option')

chi_wp = chi_difference(sources['D'], qscalarWp, 4)
check(block4(chi_wp, [], [('W', -5)]), {'1': -1, 'V': 1, 'D': 1, 'P': 1},
      'Wp scalar zero cubic rejected lower option')
check(block4(chi_wp, [], [('1', -6)]), {'V': 1, 'D': 1, 'P': 1},
      'Wp scalar zero cubic genuine lower option')
# These are the six coefficient solutions to H1=S+W from the displayed atoms.
# Every multiplicity is at most one. The first four pair the two independent
# constituent choices; the last two are the atoms containing both constituents.
wp_cases = [
    ([('W', -5), ('S', -5)], {'1': -1, 'A': -1, 'V': 1, 'P': 1}),
    ([('W', -5), ('1', -8)], {'1': -1, 'V': 1, 'P': 1}),
    ([('1', -6), ('S', -5)], {'A': -1, 'V': 1, 'P': 1}),
    ([('1', -6), ('1', -8)], {'V': 1, 'P': 1}),
    ([('A', -6)], {'1': -1, 'V': 1, 'P': 1}),
    ([('W', -7)], {'V': 1, 'P': 1}),
]
for lower, expected in wp_cases:
    check(dec(lower, 3, 'h1'), {'S': 1, 'W': 1}, ('Wp scalar lower H1', lower))
    check(block4(chi_wp, [('S', -3)], lower), expected, ('Wp scalar R4', lower))

chi_w = chi_difference(sources['D'], qscalarW, 4)
final_cases = [
    ([('T', -5)], {'V': 1}),
    ([('V', -6)], {'V': 2}),
    ([('Wp', -7)], {'V': 1, 'P': 1}),
    ([('1', -10)], {'V': 1, 'D': 1}),
]
survivors = []
for lower, expected in final_cases:
    check(block4(chi_w, [('S', -3)], lower), expected, ('W scalar R4', lower))
    blocks = [('S', -3)] + [(r, -4) for r, m in expected.items() for _ in range(m)] + lower
    check(sum(dims[r] for r, e in blocks), 13, ('K rank', lower))
    check(sum(dims[r]*e for r, e in blocks), -54, ('K degree', lower))
    check(dec(blocks, 3, 'h0'), {'S': 1}, ('K cubic H0', lower))
    check(dec(blocks, 3, 'h1'), {'T': 1}, ('K cubic H1', lower))
    if expected.get('V', 0) <= 1:
        survivors.append(blocks)
check(len(survivors), 3, 'three necessary K forms')

proof_path = ROOT/'PROOF.md'
report = {
    'status': 'PASS',
    'proof_sha256': hashlib.sha256(proof_path.read_bytes()).hexdigest() if proof_path.exists() else None,
    'authenticated_originals': authenticated,
    'method': 'Independent exact class-character inner products over Q(sqrt(5)); closed binomial symmetric-power formula; no author-checker import.',
    'source_Hom_table': hom_report,
    'small_H1_atom_table': atom_report,
    'necessary_kernel_forms': survivors,
    'scope': 'Checks fixed representation identities, explicit cohomology coefficient comparisons, ranks and degrees. The geometric proof is reviewed separately. No global splitting or quotient candidate enumeration; no selected actual coefficients or instances.'
}
print(json.dumps(report, indent=2))

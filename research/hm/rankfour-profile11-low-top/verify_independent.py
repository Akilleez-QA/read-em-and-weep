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
for name, a in chars.items():
    for other, b in chars.items():
        if inner(a, b) != int(name == other):
            raise AssertionError(('orthogonality', name, other))

def decompose(character):
    return {name: m for name, values in chars.items() if (m := inner(character, values))}

def check(actual, expected, label):
    if actual != expected:
        raise AssertionError((label, actual, expected))

authenticated = []
for entry in json.loads((ROOT/'INPUTS.json').read_text()):
    data = (ROOT/entry['file']).read_bytes()
    check(len(data), entry['bytes'], entry['file']+' bytes')
    check(hashlib.sha256(data).hexdigest(), entry['sha256'], entry['file']+' sha256')
    check(hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest(), entry['git_blob_sha1'], entry['file']+' git blob')
    authenticated.append(entry['file'])

# Only irreducible proper blocks of dimensions <=3, in the prescribed small
# degree interval. This is a universal product check, not a quotient search.
parities = {'1': 0, 'W': 1, 'Wp': 1, 'A': 0, 'V': 0}
wp_mechanisms = []
for name, parity in parities.items():
    for e in range(-8, 3):
        if e % 2 == parity and inner(tensor(chars[name], sym(e+3)), chars['Wp']):
            wp_mechanisms.append((name, e))
check(set(wp_mechanisms), {('Wp', -3), ('V', 0), ('A', 2)}, 'complete Wp mechanisms')
for name in ('W', 'Wp'):
    for e in (-7, -5, -3, -1, 1):
        if inner(tensor(chars[name], sym(e+3)), chars['T']) > 1:
            raise AssertionError(('too many T in a doublet', name, e))
check([e for e in (-8, -6, -4, -2, 0, 2) if inner(sym(e+3), chars['T'])], [2], 'scalar T mechanism')
check(decompose(tensor(chars['V'], sym(3))), {'Wp': 1, 'S': 1, 'T': 1}, 'V cubic')
check(decompose(tensor(chars['A'], sym(5))), {'Wp': 1, 'S': 1, 'T': 2}, 'A quintic')

sources = {
    'D': [('D', -2), ('Wp', -3), ('T', -3), ('V', -4), ('1', -8)],
    'P': [('P', -2), ('Wp', -3), ('T', -3), ('V', -4), ('Wp', -5)],
    'V': [('V', -2), ('Wp', -3), ('T', -3), ('V', -4), ('V', -4)],
    'Z': [('Wp', -3), ('T', -3), ('T', -3), ('V', -4)],
}
hom_checks = {}
for label, source in sources.items():
    for e in (-8, -6, -4, -2):
        value = sum(inner(chars[name], sym(e-d)) for name, d in source)
        check(value, int(label == 'D' and e == -8), ('source scalar Hom', label, e))
        hom_checks[f'{label}:{e}'] = value

check(decompose(tensor(chars['D'], sym(1))), {'S': 1, 'T': 1}, 'Euler-kernel multiplicity')
check(inner(chars['A'], chars['1']), 0, 'no scalar map into A')
source_twist4 = linear((1, tensor(chars['D'], sym(2))),
                       (1, tensor(chars['Wp'], sym(1))),
                       (1, tensor(chars['T'], sym(1))), (1, chars['V']))
quotient_twist4 = tensor(chars['A'], sym(6))
kernel_character = decompose(linear((1, source_twist4), (-1, quotient_twist4)))
check(kernel_character, {'A': 1, 'V': 2, 'P': 1}, 'quartic kernel character')
derivative_target = decompose(tensor(chars['A'], sym(4)))
check(derivative_target, {'A': 1, 'V': 1, 'D': 1, 'P': 1}, 'quartic derivative target')

check(5*6+4*5+4*5, 70, '13 endpoint cost')
check(3*(3*4), 36, '9 endpoint cost')
# Polynomial coefficient checks for the square completion in section 4.
check((F(-143, 2), F(8), F(-3, 2)),
      (F(-365, 6)-F(3, 2)*F(8, 3)**2, 2*F(3, 2)*F(8, 3), F(-3, 2)),
      'capacity polynomial identity')
check(sum(h*l-h*(h+1) for h, l in zip((5, 5, 3), (2, 2, -3))), -61, 'capacity witness')
check((-54-(-2), 13*(-4)), (-52, -52), 'last kernel degree')

report = {
    'status': 'PASS', 'proof_sha256': hashlib.sha256((ROOT/'PROOF.md').read_bytes()).hexdigest(),
    'authenticated_originals': authenticated, 'wp_mechanisms': wp_mechanisms,
    'scalar_Hom_dimensions': hom_checks, 'kernel_character': kernel_character,
    'derivative_target': derivative_target,
    'boundary': 'No author-verifier import, actual coefficient evaluation, quotient enumeration or broad splitting search.'
}
print(json.dumps(report, indent=2))

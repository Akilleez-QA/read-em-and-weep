#!/usr/bin/env python3
"""Universal character checks only; no actual coefficients, maps, or rank tests."""
from pathlib import Path
from itertools import product
import contextlib, io, runpy, json
ROOT = Path(__file__).parent
with contextlib.redirect_stdout(io.StringIO()):
    prior = runpy.run_path(str(ROOT / 'verify_extremal_31_rank_two_five_quotients.py'))
for key in ('va', 'vs', 'vm', 'sym', 'reps', 'U', 'effective', 'euler', 'sections'):
    globals()[key] = prior[key]
mu = prior['r']['multiplicity']
profiles = prior['r']['p']['profiles']
names = list(reps)
def vec(char):
    return tuple(mu(char, reps[name]) for name in names)
def char(vector):
    return va(*[vs(a, reps[name]) for a, name in zip(vector, names)])
def sub(a, b):
    return va(a, vs(-1, b))
assert len(profiles) == 28
cases = [(4,2), (6,2), (8,2), (6,4), (8,4)]
limits = [(0,1,1), (1,2,1), (1,3,1), (1,1,1), (1,2,1)]
expected2 = [9,22,23,16,22]
expected3 = [4,21,21,10,21]
certificate = []
for (n,e), lim, count2, count3 in zip(cases, limits, expected2, expected3):
    A00 = sym(n-2)
    A02 = va(sym(n), vm(reps['Wp'], sections(3-e)))
    A03 = va(sym(n+1), vm(reps['Wp'], sections(4-e)))
    chi = va(U, vs(-1, sym(n+1)), vs(-1, vm(reps['Wp'], euler(4-e))))
    bound = va(sym(n-1), sections(n-3), vm(reps['Wp'], sections(2-e)))
    quadratic, cubic = [], []
    for coeff, R, blocks in profiles:
        E3 = va(*[vm(C, sections(3-j)) for j,C in blocks])
        rv, av = vec(R), vec(A00)
        upper = tuple(min(a,b) for a,b in zip(vec(E3), vec(bound)))
        q_witnesses, c_witnesses = [], []
        # Enumerate abstract irreducible multiplicities of S, not maps.
        for sv in product(*[range(min(a,b)+1) for a,b in zip(rv,av)]):
            S = char(sv)
            if not effective(va(A02, vs(-1,R), S)):
                continue
            q_witnesses.append(sv)
            lower = tuple(max(0,a,b,c) for a,b,c in zip(
                vec(vm(S,reps['W'])), vec(chi), vec(sub(E3,A03))))
            if all(a <= b for a,b in zip(lower,upper)):
                X = char(lower)
                assert effective(X) and effective(sub(X,chi))
                assert effective(sub(X,vm(S,reps['W'])))
                assert effective(sub(E3,X)) and effective(sub(bound,X))
                assert effective(va(A03,vs(-1,E3),X))
                c_witnesses.append({'S':sv, 'minimal_X':lower})
        vpd = tuple(mu(R,reps[name]) for name in ('V','P','D'))
        assert bool(q_witnesses) == all(a <= b for a,b in zip(vpd,lim))
        if q_witnesses:
            quadratic.append(coeff)
        if c_witnesses:
            cubic.append({'coefficients':coeff, 'witnesses':c_witnesses})
    assert len(quadratic) == count2
    assert len(cubic) == count3
    certificate.append({'n':n,'e':e,'quadratic_count':count2,
                        'cubic_count':count3,'survivors':cubic})
assert sum(c['cubic_count'] for c in certificate) == 77
# Explicit seed identities and notation checks.
assert list(sym(2)) == reps['A']
assert va(sym(4), vm(reps['Wp'],sym(1))) == va(reps['P'],reps['D'])
assert list(sym(4)) == reps['D']
assert list(sym(6)) == va(reps['V'],reps['P'])
print('PASS: universal twist-two counts:', expected2)
print('PASS: universal cubic-envelope counts:', expected3)
print('PASS: 77 necessary quotient/primal pairs remain out of 140.')
print('No complete quotient exclusion; SF >= 3 and square rank >= 27 unchanged.')
if '--json' in __import__('sys').argv:
    print(json.dumps({'irreducible_order':names,'cases':certificate},indent=2))

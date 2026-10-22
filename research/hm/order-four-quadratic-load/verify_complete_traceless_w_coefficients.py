"""Universal symbolic audit; --build-all additionally expands all678 generators.

The default verifies every CG inclusion and bridge, the full typed source,
marking/W adjoints, character counts and seven assembled generators.  It
never chooses an actual source coefficient or evaluates an instance rank.
"""
import argparse
from collections import Counter
from universal_complete_traceless_w_coefficients import *

parser = argparse.ArgumentParser()
parser.add_argument('--build-all', action='store_true')
args = parser.parse_args()
FB, FC, FD = s.symbols('FB FC FD', nonzero=True)
f = s.Matrix([[0, 0, FC, 0], [-9*FB*FC/FD, 0, 0, 0],
              [0, 0, 0, FD], [0, FB, 0, 0]])
q = s.symbols('q0:5')
H0 = op4(sum(c*m for c, m in zip(q, mon(4))))
g12 = marked_twelve(f)
zero_matrix(f.T*J3*f-3*FB*FC*J3)
assert s.Poly(g12, S, T).coeff_monomial(S**6*T**6) == s.Rational(11, 15)
print('PASS: complete three-scale symplectic marking and nonzero marked g12.', flush=True)

# Every CG inclusion is checked on the FULL generic binary polynomial and
# all three diagonal sl2 generators in the two independent variable pairs.
X, Y, Z, Q = s.symbols('cg_X cg_Y cg_Z cg_Q')
for firstdegree in (0, 2, 4, 6):
    for r in range(min(firstdegree, 6)+1):
        j = firstdegree+6-2*r
        zz = s.symbols('cg'+str(firstdegree)+'_'+str(r)+'_0:'+str(j+1))
        p = sum(c*m for c, m in zip(zz, mon(j)))
        inc = lambda p0: clebsch_inclusion(p0, firstdegree, r, (X, Y, Z, Q))
        image0 = inc(p)
        for (a, b, c, d), value in s.Poly(image0, X, Y, Z, Q).terms():
            assert a+b == firstdegree and c+d == 6
        for source, target in [
                (S*s.diff(p, T), X*s.diff(image0, Y)+Z*s.diff(image0, Q)),
                (T*s.diff(p, S), Y*s.diff(image0, X)+Q*s.diff(image0, Z)),
                (S*s.diff(p, S)-T*s.diff(p, T),
                 X*s.diff(image0, X)-Y*s.diff(image0, Y)
                 +Z*s.diff(image0, Z)-Q*s.diff(image0, Q))]:
            assert s.expand(inc(source)-target) == 0, (firstdegree, r)
        assert s.expand(inc(S**j)-X**(firstdegree-r)*Z**(6-r)*(X*Q-Y*Z)**r) == 0
        if r == 0:
            assert s.expand(image0.subs({X:S, Y:T, Z:S, Q:T})-p) == 0
print('PASS: all16 full two-variable CG inclusions, E/F/H covariance, nonzero normalization and bidegrees.', flush=True)

# Universal positive-sextic projector and inverse marking to the W Lie action.
cs = s.symbols('sextic0:7')
p6 = sum(c*m for c, m in zip(cs, mon(6)))
pA, pP = [dict(split_six(f, p6))[kind] for kind in ('A', 'P4')]
assert s.expand(pA+pP-p6) == 0
for p0, eigenvalue in ((pA, 2), (pP, 12)):
    zero_matrix(negative_casimir(f, op6(p0))-eigenvalue*op6(p0))
L = negative_w_matrix(f, p6)
assert s.expand(s.trace(L)) == 0
zero_matrix(J1.inv()*L.T*J1+L)
rank_one = L[0, 1]*binary_E+L[1, 0]*binary_F+L[0, 0]*binary_H
zero_matrix(f*rank_one*f.inv()-op6(pA))
zero_matrix(negative_w_matrix(f, pP))
for K3, K1 in ((binary_E, E1), (binary_F, F1), (binary_H, H1)):
    pp = sextic(f*K3*f.inv())
    zero_matrix(negative_w_matrix(f, pp)-K1)
print('PASS: full sextic A/P4 projectors, inverse marking and all three W Lie normalizations.', flush=True)

# Every supported upward bridge is nonzero on its specified input type.
for kind, degree in CANONICAL_DEGREE.items():
    zz = s.symbols('bridge_'+kind+'_0:'+str(degree+1))
    p0 = sum(c*m for c, m in zip(zz, mon(degree)))
    typed = project_six(f, p0, kind) if degree == 6 else p0
    for target, types in BINARY_TYPES.items():
        if kind not in types:
            continue
        out = bridge_to_degree(f, g12, kind, typed, target)
        assert s.expand(out) != 0, (kind, target)
        for (a, b), value in s.Poly(out, S, T).terms():
            assert a+b == target
        if degree == 6 and target != 6:
            assert s.expand(out-bridge_to_degree(f, g12, kind, p0, target)) == 0
print('PASS: all14 canonical typed bridges, including every common component in B12.', flush=True)

# Tensor adjoint order and sign: W-major basis, Cartan4 + Spin2 inside it.
a, b, c = s.symbols('adj_a adj_b adj_c')
L0 = s.Matrix([[a, b], [c, -a]])
M0 = s.Matrix(6, 6, s.symbols('adj_m0:36'))
Jb = s.diag(-J3/2, -J1/3)
J12 = s.kronecker_product(J1, Jb)
T0 = s.kronecker_product(L0, M0)
zero_matrix(J12.inv()*T0.T*J12+s.kronecker_product(L0, Jb.inv()*M0.T*Jb))
print('PASS: generic W-major tensor adjoint equals minus W action tensor six-space adjoint.', flush=True)

# Exact A5 characters; no coefficient-matrix ranks are formed.
phi = (1+s.sqrt(5))/2
sizes = [1, 15, 20, 12, 12]
C = {'1': s.ones(5, 1), 'A': s.Matrix([3, -1, 0, phi, 1-phi]),
     'V': s.Matrix([3, -1, 0, 1-phi, phi]),
     'P4': s.Matrix([4, 0, 1, -1, -1]), 'D5': s.Matrix([5, 1, -1, 0, 0])}
inner = lambda a0, b0: s.simplify(sum(n*x*y for n, x, y in zip(sizes, a0, b0))/60)
mul = lambda a0, b0: a0.multiply_elementwise(b0)
dec = lambda a0: {kind: inner(a0, char) for kind, char in C.items() if inner(a0, char)}
even = [C['1'], C['V']]
for i in range(1, 6):
    even.append((mul(C['V']-C['1'], even[i])-even[i-1]).applyfunc(s.simplify))
for degree, types in BINARY_TYPES.items():
    assert even[degree//2] == sum((C[kind] for kind in types), s.zeros(5, 1))
for block, types in TARGET_TYPES.items():
    firstkind = ('1' if 'scalar' in block else block.split('_')[-1])
    assert dec(mul(C['A'], C[firstkind])) == {kind: 1 for kind in types}
N = 2*C['A']+C['V']+C['P4']+C['D5']
end6 = 2*C['1']+C['A']+4*C['V']+C['P4']+3*C['D5']
target = mul(end6, C['A'])
assert dec(target) == {'1': 1, 'A': 6, 'V': 4, 'P4': 8, 'D5': 9}
assert dec(mul(C['D5'], N)) == {'1': 1, 'A': 5, 'V': 5, 'P4': 6, 'D5': 7}
assert inner(N, target) == 33 and inner(mul(C['D5'], N), target) == 162
assert inner(N, end6) == 10 and inner(mul(C['D5'], N), end6) == 54
assert 33+162+10+54 == 259
print('PASS: traceless-W character1+6A+4V+8P4+9D5, coefficients162+33; combined supported total259.', flush=True)

rq, rh = typed_source_polynomials(f, H0)
assert Counter(kind for _, kind, _ in rq) == {'1': 1, 'A': 8, 'V': 8, 'P4': 9, 'D5': 12}
assert {kind: len(list(target_routes(kind))) for kind in CANONICAL_DEGREE} == {'1':2, 'A':10, 'V':9, 'P4':17, 'D5':25}
assert sum(len(list(target_routes(kind))) for _, kind, _ in rq) == 607
assert sum(len(list(target_routes(kind))) for _, kind, _ in rh) == 71
for category, source in (('Rq', rq), ('Rh', rh)):
    for name, kind, p0 in source:
        for powers, value in s.Poly(p0, h, k, l, u, w).terms():
            if value:
                assert sum(powers[:3]) == 2 and sum(powers[3:]) == 2
        for powers, value in s.Poly(p0, *q).terms():
            if value:
                assert sum(powers) == (category == 'Rq')
        for powers, value in s.Poly(p0, S, T).terms():
            if value:
                assert sum(powers) == CANONICAL_DEGREE[kind]
        if kind in ('A', 'P4'):
            assert s.expand(project_six(f, p0, kind)-p0) == 0
print('PASS: all43 typed sources have exact H/D/base degrees; lazy enumeration607+71.', flush=True)

builder = TracelessWBuilder(f)
smokes = []
# Direct and invariant bridges, both mixed directions, and one Rq source.
for name, kind, p0 in (rh[0], rh[2], rh[3], rh[4]):
    routes = list(target_routes(kind))
    route = next((r0 for r0 in routes if r0.clebsch_degree == 12), routes[0])
    smokes.append(('Rh', name+'_'+route.label, builder.apply(p0, route)))
for block in ('CS_V', 'SC_V'):
    name, kind, p0 = rh[4]
    route = next(r0 for r0 in target_routes(kind) if r0.block == block)
    smokes.append(('Rh', name+'_'+route.label, builder.apply(p0, route)))
name, kind, p0 = next(source for source in rq if source[1] == '1')
route = next(target_routes(kind))
smokes.append(('Rq', name+'_'+route.label, builder.apply(p0, route)))
for category, name, M in smokes:
    assert M.shape == (12, 12)
    assert any(s.expand(e) != 0 for e in M), name
    zero_matrix(M[:6, :6]+M[6:, 6:])
    for e in M:
        for powers, value in s.Poly(e, h, k, l, u, w, *q).terms():
            if value:
                assert sum(powers[:3]) == 2 and sum(powers[3:5]) == 2
                assert sum(powers[5:]) == (category == 'Rq')
print('PASS: seven nonzero assembled universal 12x12 coefficients, including Rq and both mixed arrows, have traceless W action and exact bidegrees.', flush=True)

if args.build_all:
    counts = Counter()
    for category, name, M in builder.iter_coefficients(f, H0):
        counts[category] += 1
        zero_matrix(M[:6, :6]+M[6:, 6:])
        for e in M:
            for powers, value in s.Poly(e, h, k, l, u, w, *q).terms():
                if value:
                    assert sum(powers[:3]) == 2 and sum(powers[3:5]) == 2
                    assert sum(powers[5:]) == (category == 'Rq')
        if sum(counts.values()) % 50 == 0:
            print('Checked expanded coefficients:', dict(counts), flush=True)
    assert counts == {'Rq': 607, 'Rh': 71}
    print('PASS: all678 expanded universal coefficient formulas audited.', flush=True)
else:
    print('Full678-formula expansion not requested; completeness follows from the verified linear constructions and character identities.')
print('No source coefficient assignment, instance rank, generator independence, source solution or unrestricted-middle claim.')

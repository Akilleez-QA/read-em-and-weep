#!/usr/bin/env python3
"""Universal rank-two plateau degrees and abstract G-character arithmetic.

No actual HM coefficients, maps, matrices, numerical ranks, or local models
are evaluated.  The final finite loop concerns hypothetical integer plateau
lengths only, after a universal coefficientwise proof of the degree identity.
"""
import contextlib
import io
from pathlib import Path
import runpy
import sympy as s


def zero(expr):
    assert s.simplify(s.expand(expr)) == 0, expr


k, l, j, i, x = s.symbols('k l j i x', integer=True)
m = k + l
# c_i = x + 4(i-1) + sum_{j<i} delta_j.
zero(s.summation(4 * (i - 1), (i, 1, k)) - 2*k*(k-1))
zero(s.summation(4 * (i - 1), (i, 1, m)) - 2*m*(m-1))
# Coefficientwise proof of m*prefix-k*total = -2klm-ramification.
zero(m*k*x - k*m*x)
zero(m*2*k*(k-1) - k*2*m*(m-1) + 2*k*l*m)
zero(m*(k-j) - k*(m-j) + l*j)
zero(-k*(m-j) + k*(m-j))
# Actual ranks and degree, without and with determinant parity.
p, q = 17-2*k, 13-2*l
raw_defect = 54*m - 2*l*p - k*q - 2*k*l*m
zero(raw_defect - (41*k+20*l-2*k*l*(m-3)))
even_defect = (54*m - 2*l*p - k*(q+1) - 2*k*l*m)/2
zero(even_defect - (20*k+10*l-k*l*(m-3)))
alpha, beta, R = s.symbols('alpha beta R', integer=True)
a, b = -2*p-2*alpha, -(q+1)-2*beta
zero((54*m + l*a+k*b-2*k*l*m-2*R)/2
     - (even_defect-l*alpha-k*beta-R))

# Abstract character arithmetic of the actual Koszul terms.  Suppress the
# imported verifier's unrelated status lines; retain all its exact assertions.
with contextlib.redirect_stdout(io.StringIO()):
    ring = runpy.run_path(str(Path(__file__).with_name('verify_negative_vertex_scalar.py')))
add, mul, scale = [ring[x] for x in ('vadd', 'vmul', 'vscale')]
W, Wp, A, V, P, D, S, T = [ring[x] for x in ('W','Wp','A','V','P','D','S','T')]
assert mul(W,Wp) == P
assert mul(W,S) == add(A,D)
assert mul(W,T) == add(D,V,P)
Y = add(scale(3,Wp),scale(3,S),scale(6,T))
M2 = add(A,scale(2,V),scale(3,P),scale(4,D))
M4 = add(scale(2,V),scale(4,P),scale(3,D))
ambient = add(mul(W,Y),scale(-1,M2),scale(-1,M4))
expected = scale(2,add(A,V,P,D))
assert ambient == expected
assert ambient[0] == ring['z'](30)
assert ambient[1] == ambient[0]  # Actual center-even ambient representation.
assert ring['inner'](ambient,ring['one']) == ring['z'](0)

# Exhaust only the necessary bounded integer profiles, not actual ranks.
allowed = []
for K in range(1,9):
    for L in range(1,7):
        deficit = 20*K+10*L-K*L*(K+L-3)
        if deficit < 0:
            continue
        # Exact nonnegative semigroup requirement from effective defects.
        solutions = [(aa, (deficit-L*aa)//K)
                     for aa in range(deficit//L+1)
                     if (deficit-L*aa) % K == 0]
        assert solutions  # In these ranges, the inequality already suffices numerically.
        allowed.append((K,L))
assert max(K+L for K,L in allowed) == 10
assert min(30-2*(K+L) for K,L in allowed) == 10
max_l = {K:max(L for kk,L in allowed if kk==K) for K in range(1,9)}
assert max_l == {1:6,2:6,3:6,4:5,5:4,6:3,7:3,8:2}
assert (8,6) not in allowed
assert (1,1) in allowed  # No claim to have excluded rank two itself.

print('PASS: universal rank-two plateau identity, coefficient by coefficient.')
print('PASS: even-degree specialization gives kl(k+l-3) <= 20k+10l.')
print('PASS: actual ambient character is 2A+2V+2P4+2D5, center-even of dimension 30.')
print('PASS: every numerically allowed plateau has k+l <= 10 and p+q >= 10.')
print('Allowed maximum l by k:', max_l)
print('NOT PROVED: realization of any profile, exclusion of SF rank two, or maximal SF rank.')

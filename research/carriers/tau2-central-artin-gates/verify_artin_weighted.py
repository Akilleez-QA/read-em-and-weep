#!/usr/bin/env python3
"""Independent exact weighted-frame and full-Artin checks; no saved inputs."""
import sympy as S

J = S.Matrix([[0, 1], [-1, 0]])
z = S.symbols('z', nonzero=True)
D = S.diag(z, 1/z)
Q = S.Matrix(2, 2, S.symbols('q0:4'))
V = S.Matrix(2, 2, S.symbols('v0:4'))
ell, h, a = S.symbols('ell h a')
L = S.Matrix([[ell, h], [0, a]])
B = lambda A: A.T*J*A/2
zero = lambda A: all(S.cancel(v) == 0 for v in A)
# New W basis = old W basis times D; E and T frames are held fixed.
Qnew, Vnew = Q*D, D.inv()*V
assert zero(D.T*J*D-J)
assert zero(Qnew*J*Qnew.T-Q*J*Q.T)
assert zero((Q+L*V.T*J)*D-(Qnew+L*Vnew.T*J))
assert zero(B(Vnew)-B(V))
assert zero(Qnew*Vnew+L*B(Vnew)-Q*V-L*B(V))
print('PASS: symbolic weighted W covariance (z=t^c), including quadratic correction')

c = S.symbols('c', integer=True, nonnegative=True)
Ebase, Tbase, Wbase = (-5, -3), (-2, -1), (c, -c)
Qbase = [[td-wd for wd in Wbase] for td in Tbase]
Vbase = [[wd+ed for ed in Ebase] for wd in Wbase]
assert Qbase == [[-2-c, -2+c], [-1-c, -1+c]]
assert Vbase == [[c-5, c-3], [-c-5, -c-3]]
# a*Q_C-h*Q_D gives quadrics of the two distinct base weights.
assert [2+q for q in Qbase[0]] == [-c, c]
assert [1+q for q in Qbase[1]] == [-c, c]
# f is a section of det(T), independent of c; QV lies in T tensor E.
assert Qbase[0][0]+Qbase[1][1] == -3
assert Qbase[0][1]+Qbase[1][0] == -3
for i in range(2):
    for j in range(2):
        assert all(S.expand(Qbase[i][k]+Vbase[k][j]) == Tbase[i]+Ebase[j]
                   for k in range(2))
print('PASS: actual weighted Q/V bidegrees and ordinary quadratic-column weights')

e, X, Y = S.symbols('e X Y')
cubics = (X**3, X**2*Y, X*Y**2, Y**3)
linears = (X, Y)

def rem(p, modulus):
    return S.Poly(S.expand(p), e, domain='EX').rem(S.Poly(modulus, e)).as_expr().expand()

def artin_operator(C1, C2, modulus):
    """(D1,D2) -> C1*D2-C2*D1, using basis (1,e) over Q."""
    columns = []
    for slot in range(2):
        for linear in linears:
            for scalar in (1, e):
                p = rem((-C2 if slot == 0 else C1)*linear*scalar, modulus)
                coeffs = S.Poly(p, X, Y)
                columns.append(S.Matrix([S.expand(coeffs.coeff_monomial(m)).coeff(e, j)
                                         for m in cubics for j in range(2)]))
    return S.Matrix.hstack(*columns)

for label, modulus, support in (
    ('reduced pair', e*(e-1), (0, 1)),
    ('double point', e**2, (0,)),
):
    C1, C2 = X**2+e*X*Y, Y**2+e*X**2
    sylvester = S.Matrix.hstack(*[
        S.Matrix([S.Poly(q, X, Y).coeff_monomial(m) for m in cubics])
        for q in (-C2*X, -C2*Y, C1*X, C1*Y)
    ])
    determinant = S.factor(sylvester.det())
    assert all(determinant.subs(e, point) != 0 for point in support)
    assert S.gcd(S.Poly(determinant, e), S.Poly(modulus, e)).degree() == 0
    operator = artin_operator(C1, C2, modulus)
    assert operator.shape == (8, 8) and operator.rank() == 8
    assert operator.nullspace() == []
    # Full-primary injectivity must see every component/jet, not just e=0.
    lost = rem(-C2*(e*X), modulus)
    assert lost != 0 and lost.subs(e, 0) == 0
    if label == 'reduced pair':
        assert lost.subs(e, 1) != 0
    else:
        assert lost.coeff(e, 1) != 0
    # Invertibility over the Artin ring, including a nontrivial first jet.
    coefficient = S.Matrix([[1+e, e], [e, 1]])
    detB = S.factor(coefficient.det())
    assert all(detB.subs(e, point) != 0 for point in support)
    assert S.gcd(S.Poly(detB, e), S.Poly(modulus, e)).degree() == 0
    print(f'PASS: {label}: full Sylvester Q-rank 8, determinant unit; reduced-only negative control detected')

# Explicit local double-point primary defect: four value conditions lose four jets.
jet = S.symbols('j0:4')
primary_jet = e*sum(j*m for j, m in zip(jet, cubics))
assert primary_jet.subs(e, 0) == 0
assert [rem(primary_jet, e**2).coeff(e, 1).expand().coeff(X, 3-i).coeff(Y, i)
        for i in range(4)] == list(jet)
print('PASS: four independent primary first-jet target coordinates retained')
print('ALL FULL-ARTIN AND WEIGHTED CHECKS PASSED')

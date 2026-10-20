"""Universal 4-by-10 symplectic identity; no HM/source data or specialization."""
import sympy as s
x = {i: s.Symbol('x' + str(i)) for i in range(1, 5)}
a, b, lam = s.symbols('a b lambda')
def vector(d):
    return s.Matrix([d.get(i, 0) for i in range(1, 5)])
M = {i: vector({3*i % 5: x[i]}) for i in range(1, 5)}
L = {i: vector({i: x[i], 3*i % 5: -lam*x[-i % 5]}) for i in range(1, 5)}
C1 = vector({4: x[1], 1: -x[4]})
C2 = vector({3: x[2], 2: -x[3]})
relation = s.Matrix.hstack(*(M[i] for i in range(1,5)),
                          *(L[i] for i in range(1,5)), C1, C2)
J = s.zeros(10)
for i in range(1, 5):
    j = 3*i % 5
    J[i-1, 4+j-1] = a
    J[4+j-1, i-1] = -a
J[8, 9] = b
J[9, 8] = -b
F = s.simplify(relation * J * relation.T)
expected = s.zeros(4)
for i,j,value in [(0,1,x[3]*x[4]), (0,2,-x[2]*x[4]),
                  (1,3,x[1]*x[3]), (2,3,-x[1]*x[2])]:
    expected[i,j] = (a*lam+b)*value
    expected[j,i] = -expected[i,j]
if s.simplify(F - expected) != s.zeros(4):
    raise RuntimeError('General isotropy formula failed')
if s.simplify(J.det() - a**8*b**2) != 0:
    raise RuntimeError('Nondegeneracy formula failed')
J0 = J.subs({a:1, b:-lam})
if s.simplify(relation * J0 * relation.T) != s.zeros(4):
    raise RuntimeError('Symplectic complex identity failed')
if s.simplify(J0.det() - lam**2) != 0:
    raise RuntimeError('Specialized symbolic determinant failed')
print('PASS: universal isotropy and determinant identities, no source specialization')

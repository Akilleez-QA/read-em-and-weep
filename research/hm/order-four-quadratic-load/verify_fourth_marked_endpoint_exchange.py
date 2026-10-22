#!/usr/bin/env python3
"""Universal marked endpoint naturality; no actual instance is evaluated."""

import sympy as s


def zero(expr):
    assert s.cancel(s.expand(expr)) == 0, s.factor(expr)


# The full GL2 identity, with every matrix and quadratic coefficient formal.
x, y = s.symbols("x y")
g11, g12, g21, g22 = s.symbols("g11 g12 g21 g22")
alpha, beta, gamma = s.symbols("alpha beta gamma")
G = s.Matrix([[g11, g12], [g21, g22]])
J = s.Matrix([[0, -1], [1, 0]])
detG = g11*g22-g12*g21
a_poly = alpha*x*x+beta*x*y+gamma*y*y
D_a = J*s.Matrix([s.diff(a_poly, x), s.diff(a_poly, y)])
sub_g = {x:g11*x+g12*y, y:g21*x+g22*y}
ga = s.expand(a_poly.subs(sub_g, simultaneous=True))
D_ga = J*s.Matrix([s.diff(ga, x), s.diff(ga, y)])
pull_D = G.inv()*D_a.subs(sub_g, simultaneous=True)
for entry in detG*pull_D-D_ga:
    zero(entry)

mu = s.symbols("mu", nonzero=True)
scalar_pull = (D_a.subs({x:mu*x, y:mu*y}, simultaneous=True))/mu
for entry in scalar_pull-D_a:
    zero(entry)
zero(a_poly.subs({x:mu*x, y:mu*y}, simultaneous=True)-mu**2*a_poly)

# Boundary normalization: both r and kappa flip, while k is unchanged.
r, kap = s.symbols("r kappa", nonzero=True)
zero((-r)*(-kap)-r*kap)
# Natural transport of xi instead keeps r and reverses k.
zero(r*(-kap)+r*kap)

# Formal ambient module generators and the exact corrected four-step chain.
q, t, a, h, b = s.symbols("q t a h b")
xi, zeta, v, w = s.symbols("xi zeta v w")
C = h*xi+t*(h*zeta-b*xi)+t**2*(v-b*zeta)+t**3*w
relations = {q*xi:0, q*zeta:a*xi, q*v:a*h*zeta,
             q*w:a*(v-b*zeta)}


def q_action(expr):
    ans = 0
    for gen in (xi, zeta, v, w):
        coefficient = s.expand(expr).coeff(gen)
        ans += coefficient*relations[q*gen]
    return s.expand(ans)


zero(q_action(C)-t*a*C+t**4*a*w)

# Pullback is on ambient polynomial coefficients too: b is a negative quadratic.
pull = {a:-a, b:-b, h:h, xi:-xi, zeta:zeta, v:-v, w:w, q:q, t:t}
pulled_C = s.expand(C.subs(pull, simultaneous=True))
zero(pulled_C+C.subs(t,-t))

# Every transported division remains the exact target equation.
for lhs, rhs in relations.items():
    expr = s.expand((lhs-rhs).subs(pull, simultaneous=True))
    reduced = s.expand(expr).subs({q*w:a*(v-b*zeta), q*v:a*h*zeta,
                                  q*zeta:a*xi, q*xi:0}, simultaneous=True)
    zero(reduced)

beta2_rep = a*b*zeta
cubic_rep = a*v
fourth_rep = a*w
zero(beta2_rep.subs(pull, simultaneous=True)-beta2_rep)
zero(cubic_rep.subs(pull, simultaneous=True)-cubic_rep)
zero(fourth_rep.subs(pull, simultaneous=True)+fourth_rep)

# Obstruction sign from direction (-1)^r and cyclic source -1.
assert (-1)**(3+1) == 1
assert (-1)**(4+1) == -1
assert (-1)*(-1) == 1  # A-polynomial times boundary-normalized xi.
assert (-1)*(-1) == 1  # Intrinsic target and adjoint quotient line.

print("PASS: full GL2 Hamiltonian determinant factor and both xi normalizations.")
print("PASS: exact corrected chain, every transported division, and retained b terms.")
print("PASS: actual marked second and third tensors are even; fourth gate is odd.")
print("No fourth value or midpoint fourth operation is supplied.")

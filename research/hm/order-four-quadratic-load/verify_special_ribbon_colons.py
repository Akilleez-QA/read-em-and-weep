"""Universal formal ideal quotients for the special-ribbon proof.

No HM coordinates, coefficients, evaluated actual matrices, or rank tests occur.
The symbols a, q, g are independent formal variables.  The a-unit chart
is modeled separately by the regular pair x,g.  All quotients are computed
through I intersect (h), using an auxiliary elimination variable, then
compared as ideals in both directions.
"""
import sympy as sp


def ideal_basis(gens, variables):
    return sp.groebner(gens, *variables, order='lex', domain=sp.QQ)


def is_member(poly, basis):
    return basis.reduce(sp.expand(poly))[1] == 0


def same_ideal(left, right, variables):
    lb = ideal_basis(left, variables)
    rb = ideal_basis(right, variables)
    assert all(is_member(p, rb) for p in left)
    assert all(is_member(p, lb) for p in right)


def quotient_by_principal(gens, h, variables):
    # I intersect (h) = (t I + (1-t)(h)) intersect QQ[variables].
    t = sp.Dummy('eliminate')
    elim = ideal_basis([t*f for f in gens] + [(1-t)*h], (t,) + variables)
    intersection = [p.as_expr() for p in elim.polys if not p.as_expr().has(t)]
    quotient = []
    for f in intersection:
        division, remainder = sp.div(f, h, *variables, domain=sp.QQ)
        assert remainder == 0
        quotient.append(sp.expand(division))
    return quotient


a, q, g = sp.symbols('a q g')
variables = (g, q, a)
x = g + a*q
I = [g, q**2]
I2 = [g**2, g*q**2, q**4]
J = quotient_by_principal(I2, x, variables)
same_ideal(J, [g**2, g*q, q**3], variables)
K = quotient_by_principal(I2, x**2, variables)
same_ideal(K, I, variables)
ann = quotient_by_principal(I, a**2, variables)
same_ideal(ann, I, variables)
print('PASS: b-unit chart I²:x=(g²,gq,q³), I²:x²=I, and a² is regular on R/I.')

# On x=0 one has g=-a*q; take the image of the computed quotient.
image = [sp.expand(f.subs(g, -a*q)) for f in J]
same_ideal(image, [a*q**2, q**3], (q, a))
print('PASS: the restricted quotient image is q²(a,q).')

x, g = sp.symbols('x g')
variables = (g, x)
I = [g, x**2]
I2 = [g**2, g*x**2, x**4]
J = quotient_by_principal(I2, x, variables)
same_ideal(J, [g**2, x*g, x**3], variables)
K = quotient_by_principal(I2, x**2, variables)
same_ideal(K, I, variables)
print('PASS: a-unit chart I²:x=(g²,xg,x³) and I²:x²=I.')
print('All universal colon checks passed; no actual HM specialization was used.')

"""Universal polynomial lifts for the quadratic cone q = xy + z^2.

All coefficients remain symbolic.  No sampling, ranks, or coefficient solve.
The proof and scope are in conic_kernel_lifting.md.
"""

import sympy as sp

x, y, z = sp.symbols("x y z")
COORDS = (x, y, z)
V = sp.Matrix(COORDS)
Q = x * y + z * z


def expanded(matrix):
    return matrix.applyfunc(sp.expand)


def cross(vector):
    a, b, c = vector
    return sp.Matrix([[0, -c, b], [c, 0, -a], [-b, a, 0]])


def is_zero(matrix):
    return all(sp.cancel(sp.expand(entry)) == 0 for entry in matrix)


def symmetric_quadratic_right_inverse(r, coords=COORDS):
    """Return symmetric linear B with B*v=r for every quadratic vector r."""
    v = sp.Matrix(coords)
    r = sp.Matrix(r)
    jac = r.jacobian(coords)
    return expanded(jac + jac.T - sp.hessian((v.T * r)[0], coords) / 2)


def skew_quadratic_right_inverse(r, coords=COORDS):
    """If v.r=0, return skew linear B with B*v=r.

    Off that kernel, the exact identity is B*v=r-grad(v.r)/3.
    """
    r = sp.Matrix(r)
    jac = r.jacobian(coords)
    return expanded((jac - jac.T) / 3)


def scalar_quadratic_right_inverse(f, coords=COORDS):
    """Return linear b with v.b=f for every quadratic scalar f."""
    return sp.Matrix([sp.diff(f, variable) / 2 for variable in coords])


def exact_polynomial_quotient(f, q=Q, coords=COORDS):
    quotient, remainder = sp.Poly(sp.expand(f), *coords, domain="EX").div(
        sp.Poly(q, *coords, domain="EX"))
    if remainder.as_expr() != 0:
        raise ValueError("The literal contraction is not divisible by q.")
    return quotient.as_expr()


def cubic_symmetric_q_lift(tensor, coords=COORDS, q=Q):
    """Return (exact_tensor, linear_correction), with T=exact_tensor+q*B.

    Input uses A-block-major order, with each V block of size 3. It must be
    globally symmetric, homogeneous cubic, and literally annihilate
    id_A tensor v modulo q. This does not interpret A/C source ends.
    """
    tensor = sp.Matrix(tensor)
    if tensor.rows != tensor.cols or tensor.rows % 3:
        raise ValueError("Expected a square matrix with V blocks of size 3.")
    if not is_zero(tensor - tensor.T):
        raise ValueError("Expected a symmetric tensor.")
    for entry in tensor:
        if entry != 0 and any(sum(powers) != 3 for powers, coefficient in
                              sp.Poly(entry, *coords, domain="EX").terms()):
            raise ValueError("Expected homogeneous positive-cubic entries.")
    n = tensor.rows // 3
    v = sp.Matrix(coords)
    defects = {}
    for a in range(n):
        for b in range(n):
            contraction = tensor[3*a:3*a+3, 3*b:3*b+3] * v
            defects[a, b] = sp.Matrix([
                exact_polynomial_quotient(entry, q, coords)
                for entry in contraction])
    correction = sp.zeros(tensor.rows)
    for a in range(n):
        for b in range(n):
            plus = expanded((defects[a, b] + defects[b, a]) / 2)
            minus = expanded((defects[a, b] - defects[b, a]) / 2)
            if not is_zero(v.T * minus):
                raise AssertionError("Skew defect unexpectedly fails v.r=0.")
            block = (symmetric_quadratic_right_inverse(plus, coords)
                     + skew_quadratic_right_inverse(minus, coords))
            correction[3*a:3*a+3, 3*b:3*b+3] = block
    exact = expanded(tensor - q * correction)
    if not is_zero(correction - correction.T):
        raise AssertionError("Correction lost global symmetry.")
    for a in range(n):
        for b in range(n):
            if not is_zero(exact[3*a:3*a+3, 3*b:3*b+3] * v):
                raise AssertionError("Corrected tensor is not exactly orthogonal.")
    return exact, expanded(correction)


def conic_leg_maps(coords=COORDS):
    """Return g,L,D,E with L*D=[0,q*I], D*E=E*D=q*I."""
    x, y, z = coords
    v = sp.Matrix(coords)
    g = sp.Matrix([y / 2, x / 2, z])
    cv, cg = cross(v), cross(g)
    leg = cv.row_join(g)
    differential = v.row_join(-cg).col_join(sp.zeros(1, 1).row_join(v.T))
    companion = g.T.row_join(sp.zeros(1, 1)).col_join(cv.row_join(g))
    return g, leg, differential, companion

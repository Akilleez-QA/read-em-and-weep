#!/usr/bin/env python3
"""Independent fixed-lex audit for the universal bicubic divisor.

All frame scales and H/D/source coefficients stay indeterminate.  These are
formal normal-form contract tests, not evaluations of a geometric instance,
an actual source, or an operator ansatz.  Frozen reduction artifacts are not
read or changed.  Run: python verify_true_lex_curve_normal_form_audit.py
"""
from itertools import combinations_with_replacement
from pathlib import Path
import runpy
import sys
import sympy as s


def explicit_lex_division(dividend, divisor):
    """Return (quotient, remainder), using only sparse leading-term division.

    The input Poly generators, in their supplied order, define lex order.
    Coefficients are native elements of their common exact field.  In
    particular, this implementation never calls Poly.div/rem, s.div,
    s.reduced, or Groebner reduction.  An irreducible leading term is moved
    to the remainder and division CONTINUES with the remaining terms.
    """
    if dividend.gens != divisor.gens or dividend.domain != divisor.domain:
        raise ValueError("Polynomials must have the same generators and domain")
    if not dividend.domain.is_Field:
        raise ValueError("The coefficient domain must be a field")
    if divisor.is_zero:
        raise ZeroDivisionError("Cannot divide by the zero polynomial")
    domain, gens = dividend.domain, dividend.gens
    pending = dividend.as_dict(native=True).copy()
    divisor_terms = divisor.as_dict(native=True)
    leading = max(divisor_terms)
    leading_coefficient = divisor_terms[leading]
    quotient, remainder = {}, {}

    def add_term(poly, powers, coefficient):
        value = poly.get(powers, domain.zero) + coefficient
        if value:
            poly[powers] = value
        else:
            poly.pop(powers, None)

    while pending:
        powers = max(pending)  # tuple comparison is exactly lex order
        coefficient = pending[powers]
        if all(a >= b for a, b in zip(powers, leading)):
            difference = tuple(a-b for a, b in zip(powers, leading))
            factor = coefficient / leading_coefficient
            add_term(quotient, difference, factor)
            for monomial, value in divisor_terms.items():
                target = tuple(a+b for a, b in zip(difference, monomial))
                add_term(pending, target, -factor*value)
        else:
            remainder[powers] = pending.pop(powers)
        # A monomial well-order guarantees termination, not a degree bound.
        assert not pending or max(pending) < powers

    def to_poly(terms):
        return s.Poly.from_dict(
            {m: domain.to_sympy(c) for m, c in terms.items()}, gens,
            domain=domain)
    return to_poly(quotient), to_poly(remainder)


def main():
    r0, r1, u, w = s.symbols('r0 r1 u w')
    FB, FC, FD, theta = s.symbols('FB FC FD theta', nonzero=True)
    H = s.symbols('ha hb hc hd hf')
    D = s.symbols('h k l')
    alpha, beta, c, d = s.symbols('alpha beta c d')
    G = (r0, r1, u, w)
    units = (FB, FC, FD, theta)
    K0 = s.QQ.frac_field(*units, alpha, beta, c, d)
    K = s.QQ.frac_field(*units, alpha, beta, c, d, *H, *D)
    F = (9*FB*FC*r0*r1**2*w**3 + 3*FB*FD*r0**3*u*w**2
         + 3*FC*FD*r1**3*u**2*w - FD**2*r0**2*r1*u**3)/(3*FB*FC*FD)
    fp = s.Poly(F, *G, domain=K)
    f0 = s.Poly(F, *G, domain=K0)
    lm = (3, 0, 1, 2)
    assert fp.LM(order='lex').exponents == lm
    assert fp.LC(order='lex') == 1/FC
    leading_monomial = r0**3*u*w**2
    rewrite = (FD*r0**2*r1*u**3/(3*FB)
               - 3*FC*r0*r1**2*w**3/FD - FC*r1**3*u**2*w/FB)
    assert s.expand(FC*F - leading_monomial + rewrite) == 0
    groebner = s.groebner([F], *G, domain=K, order='lex')
    assert len(groebner.polys) == 1
    assert groebner.polys[0] == fp.monic()

    checked = 0

    def check(expression, *, compare_groebner=True):
        nonlocal checked
        p = s.Poly(expression, *G, domain=K)
        q, r = explicit_lex_division(p, fp)
        assert p == q*fp + r, "quotient-remainder reconstruction"
        assert all(not all(a >= b for a, b in zip(m, lm))
                   for m in r.monoms()), "forbidden leading divisibility"
        quotients, standard = s.reduced(p, [fp], *G, domain=K, order='lex')
        # SymPy 1.14 returns an empty quotient list for the zero dividend.
        standard_q = quotients[0] if quotients else s.Poly(0, *G, domain=K)
        assert (q, r) == (standard_q, standard), "s.reduced disagreement"
        if compare_groebner:
            gq, gr = groebner.reduce(p.as_expr())
            assert r == s.Poly(gr, *G, domain=K), "Groebner disagreement"
            # Groebner uses the monic divisor FC*F, hence q = FC*gq.
            assert q == s.Poly(FC*gq[0] if gq else 0, *G, domain=K)
        checked += 1
        return q, r

    check(0)
    q, r = check(leading_monomial)
    assert q.as_expr() == FC and s.expand(r.as_expr()-rewrite) == 0
    q, r = check(c*F+d*r0**3)
    assert q.as_expr() == c and r.as_expr() == d*r0**3
    # Reproduce the defect using this exact divisor, not a local surrogate.
    recursive_q, recursive_r = s.div(s.Poly(c*F+d*r0**3, *G, domain=K), fp)
    assert recursive_q.is_zero and recursive_r != r
    assert recursive_r == s.Poly(c*F+d*r0**3, *G, domain=K)

    # A formal polynomial carries every H_i times Sym^2(D) coefficient.
    # It is bihomogeneous (5,6), and is not declared to be an HM source.
    dpairs = tuple(combinations_with_replacement(D, 2))
    P = 0
    for i, hi in enumerate(H):
        for j, (dj, dk) in enumerate(dpairs):
            a = 3+(i+j) % 3
            b = 1+(2*i+j) % 4
            geometric = (r0**a*r1**(5-a)*u**b*w**(6-b)
                         + (i+j+1)*r0**5*u**6)
            P += hi*dj*dk*geometric/theta
    Q = (c*r0**2*u**3*F + d*r0*r1**4*w**6
         + H[0]*D[1]**2*r0**4*r1*u**3*w**3/FB)
    pquot, pnormal = check(P)
    qquot, qnormal = check(Q)
    combo_quot, combo_normal = check(alpha*P+beta*Q)
    assert combo_quot == pquot.mul_ground(alpha)+qquot.mul_ground(beta)
    assert combo_normal == pnormal.mul_ground(alpha)+qnormal.mul_ground(beta)
    _, idempotent = check(pnormal.as_expr())
    assert idempotent == pnormal
    # The zero-remainder criterion does not depend on scaling the divisor.
    unit = (FB*theta)/(FC*FD)
    sq, sr = explicit_lex_division(s.Poly(P, *G, domain=K), fp.mul_ground(unit))
    assert sr == pnormal and sq.mul_ground(unit) == pquot
    numerator_unit = 3*FB*FC*FD
    numerator = fp.mul_ground(numerator_unit)
    assert numerator.LC(order='lex') == 3*FB*FD
    nq, nr = explicit_lex_division(s.Poly(P, *G, domain=K), numerator)
    assert nr == pnormal and nq.mul_ground(numerator_unit) == pquot

    # Extract all five H and all three D coefficients before/after reduction.
    full_input = s.Poly(P, *H, *D)
    full_output = s.Poly(pnormal.as_expr(), *H, *D)
    assert set(full_output.monoms()) <= set(full_input.monoms())
    coefficient_checks = 0
    for powers, coefficient in full_input.terms():
        cp = s.Poly(coefficient, *G, domain=K0)
        cq, cr = explicit_lex_division(cp, f0)
        assert cp == cq*f0+cr
        monomial = s.prod(v**e for v, e in zip((*H, *D), powers))
        extracted = s.Poly(full_output.coeff_monomial(monomial), *G, domain=K0)
        assert extracted == cr, "H/D coefficient extraction failed"
        # Coefficient-domain extension is harmless and cannot turn H,D into
        # geometric-order variables by accident.
        extq, extr = explicit_lex_division(s.Poly(coefficient, *G, domain=K), fp)
        assert s.Poly(cr.as_expr(), *G, domain=K) == extr
        assert s.Poly(cq.as_expr(), *G, domain=K) == extq
        coefficient_checks += 1
    assert coefficient_checks == 30
    assert {(m[0]+m[1], m[2]+m[3]) for m in pnormal.monoms()} == {(5, 6)}
    for coefficient in pnormal.coeffs():
        denominator = s.fraction(s.cancel(coefficient))[1]
        assert denominator.free_symbols <= set(units)
        assert len(s.Poly(denominator, *units).terms()) == 1

    # The singleton divisor's zero test remains a valid membership test,
    # even though the recursive remainder itself is not a linear quotient map.
    multiplier = alpha*r0*u**2 + beta*r1*w**2 + H[4]*D[0]/theta
    exact = s.Poly(multiplier*F, *G, domain=K)
    oldq, oldr = s.div(exact, fp)
    assert oldr.is_zero and oldq == s.Poly(multiplier, *G, domain=K)
    _, exact_normal = check(exact.as_expr())
    assert exact_normal.is_zero

    print(f'PASS: {checked} symbolic universal-divisor cases match independent '
          'sparse division, s.reduced, and Groebner normal forms.')
    print('PASS: reconstruction, lex irreducibility, linearity, idempotence, '
          'unit-scaled divisor invariance, and coefficient-field extension.')
    print('PASS: all 30 H_i Sym^2(D) coefficients commute with reduction; '
          'bidegree (5,6) and Laurent-unit denominators are preserved.')
    print('PASS: exact universal-divisor regression distinguishes recursive '
          'division from the fixed-lex quotient projection.')
    print('SCOPE: no actual-instance coefficient assignments, ranks, scans, '
          'or fourth-Bockstein conclusion.')


def audit_identity_w_source_reductions():
    """Cross-check the three real universal expressions without editing them.

    Optional because the full exterior-symbol construction is slower than
    the standalone algebra-contract suite.  Its source script remains the
    owner of all non-reduction mathematical assertions.
    """
    original_reduced = s.reduced
    calls = 0

    def independently_audited_reduced(dividend, divisors, *gens, **kwargs):
        nonlocal calls
        result = original_reduced(dividend, divisors, *gens, **kwargs)
        assert len(divisors) == 1
        divisor = divisors[0]
        assert tuple(str(g) for g in divisor.gens) == ('r0', 'r1', 'u', 'w')
        assert kwargs.get('order', 'lex') == 'lex'
        assert divisor.LM(order='lex').exponents == (3, 0, 1, 2)
        iq, ir = explicit_lex_division(dividend, divisor)
        assert dividend == iq*divisor+ir
        assert iq == result[0][0] and ir == result[1]
        assert all(not (m[0] >= 3 and m[2] >= 1 and m[3] >= 2)
                   for m in ir.monoms())
        calls += 1
        print(f'INDEPENDENT AUDIT PASS: identity-W source coefficient {calls-1}.')
        return result

    source = Path(__file__).with_name('verify_identity_w_true_lex_curve_and_full_sector.py')
    try:
        s.reduced = independently_audited_reduced
        runpy.run_path(str(source), run_name='__main__')
    finally:
        s.reduced = original_reduced
    assert calls == 3, f'Expected three full universal source reductions, got {calls}'
    print('PASS: independent sparse-division audit of all three literal '
          'identity-W universal source remainders and quotients.')


if __name__ == '__main__':
    main()
    if '--identity-w' in sys.argv[1:]:
        audit_identity_w_source_reductions()

# Exact coefficient-map sign controls

Scope: formal Laurent monomial bases and integer map coefficients only. No physical HM source polynomials, source evaluations, residuals, jets, or obstruction arithmetic are constructed.

Executable: `test_scalar_homotopy_adjoint.py` (Python standard library only).
Results: `scalar-homotopy-adjoint-test-results.json`.

## Independently specified transposes

For a coefficient functional eps_(state,e), the one-factor transpose is:

- h_n* eps_(A,e) = -eps_(C,e), if e>=0.
- h_n* eps_(B,e) = +eps_(C,e), if e<0 and e<=n.
- All other cases vanish.

In particular h_0* eps_(B,0)=0, despite B0 being a regular chart monomial. The zero mode of h_0 is assigned to minus A.

J_0* sends either eps_(A,0) or eps_(B,0) to eps_(B,0), with every other coefficient functional sent to zero. J_-2* fixes only eps_(C,-1).

On tensor cochains, h is the sum of J-prefix/h-pivot/identity-suffix terms. Its transpose is the analogous sum with J* and h*. Each term carries (-1) to the number of C states strictly before its pivot. Since the prefix operators preserve Čech degree, the sign can be read on either the matching source or output. The test implements the forward and transpose formulas separately and checks both directions of their support, so zero entries are covered without a dense quadratic matrix allocation.

## Derivative adjoints and a useful compatibility

For D=partial_x, coefficient extraction obeys

    D* eps_e = (e+1) eps_(e+1).

More generally, for x^m D^r the dual request is at e-m+r with multiplier (e-m+r)(e-m+r-1)...(e-m+1). The tests include negative Laurent exponents, shifts -2 through 2, and orders 0 through 2.

As maps from the finite-frame regular Čech complex for O(0) to that for O(-2),

    D h_0 = h_-2 D,
    D J_0 = J_-2 D = 0.

For C x^e with e>0 both sides of the first identity are -e x^(e-1) A; for e=0 both vanish; for e<0 both are e x^(e-1) B. Degree-zero inputs have zero h on both sides. D annihilates the constant J_0 image, and the potential harmonic exponent -1 after differentiation would require differentiating exponent 0, again giving zero.

The tensor identity follows term by term when a selected factor changes degree 0 to -2: if the differentiated factor is in a J-prefix, both compositions vanish; at the pivot use D h_0=h_-2 D; in the suffix the maps commute. D has Čech degree zero and introduces no additional Koszul sign.

This is stripped common-finite-frame differentiation. It does not assert that the physical vector field V_a commutes with the global scalar solver, cover projection, chart transport, or carrier partition. Any coefficient-dependent physical frame or weight must still be differentiated by the Leibniz rule.

## Exhaustive test domain

All ordered products of one through four factors, with each n independently in {0,-2}; each factor includes every regular A/B monomial and every C monomial having exponent -3 through 1. Tests cover contraction, square-zero conditions, transposed support and coefficients, and every degree-zero factor's derivative compatibility. All formal maps are defined on arbitrary integer exponents, including derivative outputs outside this finite test window.

The attached JSON records exact completed pass counts. These checks establish implementation agreement on the enumerated basis; the general formulas above justify arbitrary exponents.

## Fail-closed execution guard

The script exits with code 2 before any test when Python assertions are disabled. Separate negative controls under both -O and -OO returned exit 2 and zero stdout bytes, so neither can emit a false PASS. The baseline checks above ran with assertions enabled; they were not rerun solely for this entry guard addition.

## Dependency scope

Companion references are identified by basename. A referenced file not supplied with this collection is an external prerequisite, not an embedded proof or a verified relative link. The reading order and unresolved conditions are listed in `proof-notes-index.md`. Reported test results describe the source audit; this proof copy does not by itself constitute a new test run.

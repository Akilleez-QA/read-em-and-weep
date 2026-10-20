# Independent audit: universal line-quantization regression

20 October 2026. Existing bounded universal regression record; synthetic inputs only.

## Artifact and scope

Reviewed file: `line_quantization_regression.py`.

SHA-256: `c461d97b14bb60d4d60647778258deeaaa3fafc213b94c4a0ecf4f4622ff9afa`.

Reference formulas were read in `../null-normalized-monad-lifting/normalized-monad-lifting.md`, especially §§1–3, and `../null-normalized-monad-lifting/normalized-monad-lifting-audit.md`. The toy file was read in full. Independently executed only that toy artifact, in ordinary Python, optimized Python, and its five mutant modes. No actual HM matrix, source coefficient, obstruction coordinate, physical experiment, spike, or replay was read or evaluated.

## Mathematical and implementation review

1. The sparse dictionary keys are `(s_degree,t_degree,x1_degree,...,x4_degree)`. Coefficients are exact `Fraction` values. Negative spatial exponents are retained, and zero coefficients removed. Multiplication, parameter shifts, and cleanup consistently remove terms of total parameter degree greater than two. This is the quotient by `(s,t)^3`, not separate truncation by `s^3` and `t^3`. All supplied parameter exponents are nonnegative.

2. Finite-chart differentiation sends `c*x^e` to `c*(e_i-n)/2*x^(e+unit_i)`, precisely the line lift of weight n. Infinity-chart differentiation is `-e_i/2*x^(e-unit_i)`. It acts coefficientwise on the formal parameters. The test weights `(-3,-1,0,1,3,5)` include every normalized line weight and extra generic values. There is no subtraction of the common root in the unmutated module operator.

3. `quant(f,source,target,z)` uses Hom weight `target-source` for f and source weight for z. The tested commutator identity is exactly `D_target(f*z)-f*D_source(z)=D_(target-source)(f)*z`. The root cancels here, not in the module weights. Quantization is a differential operator assembled with the twist, not unchanged multiplication by f.

4. `star` sums the identity, every single contraction, and every ordered pair of contractions with the exponential factor 1/2. The contraction constants are +1/2 and -1/2 in each coordinate block. Thus the mixed st coefficient receives both ordered cross-block terms and has no erroneous additional 1/2. Derivative order is harmless because the line operators commute. Parameter-dependent inputs are included in z and a, so nested operations also exercise parameter-order bookkeeping.

5. Independent hand derivation confirms the built-in closed-form oracles. For `x1*x3` and `x2*x4`, the surviving P and Q contractions each contribute 1/8, giving mixed coefficient `x1²*x2²*x3²*x4²/64`. For `x1²` and `x2²`, each repeated line derivative at weight zero is `3*x_i^4/2`; the exponential/contraction factor is 1/8, giving `9*x1^4*x2^4/32` at s².

6. Under `e_infinity=x^n*e_finite` and `u=1/x`, a finite coefficient `x^e` becomes `u^(n-e)`. The `frame` function implements exactly this exponent replacement for each inverted coordinate. All 16 chart subsets are tested, not just the all-finite/all-infinity pair. Tests cover D, module action, quantized maps, and Hom composition. Negative module and Hom weights occur in these cases; Laurent exponents are not incorrectly treated as polynomial degrees.

7. Scalar tests compare the two sides of right-module linearity, quantized composition, and module associativity. The four weight triples are `(-1,1,3)`, `(1,3,5)`, `(5,-1,1)`, and `(-3,0,5)`. Matrix tests use genuine noncommuting 2×2 toy coefficient matrices acting on column vectors. `mcompose(A,B)` sums `A[i][k] star B[k][j]`, so it means A after B, consistent with the reference. They compare this composition with successive operator application and also check matrix right-module linearity.

8. All checks call an explicit comparison function that raises `RuntimeError` on disagreement. There are no Python assert statements to disappear under optimization. The exception handler emits a failure and returns exit status 1. Explicit nonzero tests confirm that the selected quantized map differs from ordinary multiplication and that the classical toy matrices fail to commute.

## Independently observed runs

Commands were `python line_quantization_regression.py --mutant MODE` and `python -O line_quantization_regression.py --mutant MODE`, for MODE none and the five controls. Results in ordinary and optimized execution agree:

- none: PASS, 636 exact checks, exit 0 in each mode.
- plain_map: FAIL at check 163, right-module linearity `-1->1`, exit 1. First residual key `(0,1,-2,3,2,3)`, value `1/12`.
- wrong_hom: FAIL at check 163, same linearity check, exit 1. First residual key `(0,1,-2,3,2,3)`, value `1/4`.
- dropped_root: FAIL at check 1, finite D monomial `n=-3, i=0`, exit 1. First residual key `(0,0,-1,0,1,3)`, value `1/7`.
- reversed_order: FAIL at check 631, noncommuting matrix composition, exit 1. The matrix/vector results differ.
- missing_mixed: FAIL at check 26, module associativity at weight -3, exit 1. First residual key `(1,1,0,6,2,0)`, value `5/48`.

These are substantive mathematical mismatches, not import errors or crashes before the tests. In particular, optimized-mode success is not vacuous and the negative controls remain active under `-O`.

## Limits and interpretation

- This is finite deterministic regression evidence plus source review, not exhaustive verification over all Laurent polynomials, weights, ranks, or formal orders. The abelian-twist argument in the reference supplies the universal theorem.
- The tested formulas stop at total parameter degree two. The file does not implement the actual HM differential, strict first/second lifting equations, Čech descent, source ranks, or obstruction evaluation. Reading §3 provides context only; no test solves that section's equations.
- The normalized integer weights are used solely as generic line parameters. No assertion about an actual HM map, strict lift, full lift, diagonal obstruction, or remaining six conditions follows from these toy outcomes.
- The `dropped_root` mutant subtracts one from every nonzero weight passed to finite differentiation. It is a broad weight-shift fault and is detected by the direct monomial oracle; it is not a full geometric simulation of simultaneously replacing every line in a complex and retaining its unchanged Hom differences. The unmutated Hom and module formulas were separately reviewed.
- The sparse API trusts its internal callers: it does not reject malformed keys or negative parameter exponents. Its actual supplied inputs satisfy the declared ring representation. This is a self-contained test artifact, not a hardened general algebra library.
- Matrix composition is tested on two positive-Hom triples; negative-weight and all-chart coverage comes from the scalar tests. No claim is made that every matrix case was retested in every chart.
- Independent execution means a second reviewer ran the supplied artifact and checked its formulas and hand oracles; no second implementation of the full algebra was built.

Disposition: accepted within these limits.

# Exact line-quantization regression

20 October 2026. Existing bounded universal regression record; synthetic inputs only.

## Result

The unmodified implementation passes **636 exact checks** in ordinary Python and in optimized Python (`-O`). Each of five deliberately incorrect conventions is detected with exit status 1 in both modes. The complete 12-process transcript appears below.

Artifact: `line_quantization_regression.py`.
SHA-256: `c461d97b14bb60d4d60647778258deeaaa3fafc213b94c4a0ecf4f4622ff9afa`.

This is regression evidence for the explicit universal formulas, not a proof by finite testing, and not evidence of any particular complex differential lifting or any obstruction vanishing.

## Mathematical target and implementation

Reviewed: ../null-normalized-monad-lifting/normalized-monad-lifting.md §§1–3 and ../null-normalized-monad-lifting/normalized-monad-lifting-audit.md (including its consistency and diagonal-scope corrections). The implementation tests §2's line operators, Hom representation, abelian-twist right action, quantized morphism and composition. It does not evaluate §3's differential or curvature.

The ring is Q[x1^±1,x2^±1,x3^±1,x4^±1,s,t]/(s,t)^3, represented sparsely by exponent tuples (s-degree,t-degree,x1-degree,x2-degree,x3-degree,x4-degree) and fractions.Fraction coefficients. The cutoff is **total** parameter degree at most two; Laurent powers are not bounded or numerically sampled. Products and formal parameter shifts discard degree three and above. All functions preserve exact rational arithmetic.

On a finite-coordinate factor, D_i^(n) acts on the monomial x^e by (e_i−n)x^(e+unit_i)/2. In an infinity coordinate u_i=1/x_i it acts as −∂/∂u_i divided by two. The operators on different factors commute. Weight-zero coefficients carry the scalar vector fields.

The twist is multiplication after exp(sP+tQ), where P=(D1⊗D2−D2⊗D1)/2 and Q=(D3⊗D4−D4⊗D3)/2. The code enumerates the four first-order contraction terms and all 16 ordered pairs, dividing the second-order terms by 2. Consequently both mixed orders occur and give coefficient PQ, not PQ/2. Already parameter-dependent arguments are supported.

The quantized map Q_(n,m)(F)(z) uses weight n−m on F and weight m on z. Ordinary composition is F after G, acting on column vectors. It is not unchanged multiplication by F.

For each set S of inverted coordinates, the actual frame relation e_inf=x^n e_0 gives the coefficient change p -> (product over i in S of x_i^(−n))p with x_i=1/u_i. On monomial exponents this is e_i -> n−e_i. Hom coefficients transform with exponent n−m. The implementation uses this transition directly, rather than replacing it by a parity or symbolic-label check.

## Bounded coverage

All inputs are fixed short Laurent polynomials chosen in this script. There is no random, adaptive, exhaustive-weight, or expensive search.

- Generic integer line weights: −3, −1, 0, 1, 3, 5. The integers −1, 1, 3, 5 occur only as generic line parameters, not as supplied entries or multiplicities of a particular resolution.
- Four generic source/intermediate/target triples: (−1,1,3), (1,3,5), (5,−1,1), (−3,0,5). These exercise positive and negative sources, targets and Hom differences, including reversed weight direction.
- Closed-form monomial D oracle, all 16 operator commutators per tested weight, the line Leibniz rule, right unit and right-module associativity.
- The Hom commutator D^(n)(Fz)−F D^(m)z=(D^(n−m)F)z.
- Right-module linearity Q(F)(z⋆a)=Q(F)(z)⋆a and composition Q(F)Q(G)=Q(F⋆G).
- All 16 chart masks for each of the four triples: individual D gluing, module-action gluing, quantized-map gluing and Hom-composition gluing. These include all-finite, all-infinity and genuinely mixed charts.
- Two noncommuting 2×2 coefficient-matrix composition cases and two matrix right-module-linearity cases. An explicit nonzero classical commutator entry verifies that the matrix examples are not accidentally commuting.
- A nonzero discrepancy verifies that Q(F) really differs from ordinary multiplication in the chosen examples.
- Independent coefficient checks: with scalar weights, the st coefficient of (x1 x3)⋆(x2 x4) is x1²x2²x3²x4²/64; the s² coefficient of x1²⋆x2² is 9x1⁴x2⁴/32. The latter follows from D1²(x1²)=3x1⁴/2 and D2²(x2²)=3x2⁴/2, followed by the contraction square and exponential factorial.

The 636 checks comprise 156 scalar/line checks, two independent second-order coefficient checks, 472 Hom/map/frame checks, four matrix checks and two nondegeneracy witnesses. Every equality is an explicit runtime comparison. No correctness check uses assert, so optimization cannot erase checks. Failures print a named identity and a residual witness when scalar-valued, then return status 1.

## Negative controls

Each mutant changes an implementation convention while leaving the expected identities unchanged. A mutant's failing exit is the expected successful detection, not a passing mathematical implementation.

- `plain_map`: use Fz instead of Q(F)z. Fails right-module linearity at check 163, already at first order.
- `wrong_hom`: use weight zero rather than n−m in Q(F). Fails right-module linearity at check 163, already at first order.
- `dropped_root`: replace a nonzero finite-chart weight n by n−1, leaving scalar weight zero unchanged. This is an explicit off-by-one line-weight/root-offset control, not a claim that all Hom weights should shift when a common tensor factor is removed. The independent monomial oracle rejects it at check 1.
- `reversed_order`: reverse the two matrices in composition, including their assigned Hom weights. Fails the first noncommuting matrix-composition identity at check 631.
- `missing_mixed`: omit the second-order contraction terms using different formal parameters. Fails module associativity in its st coefficient at check 26.

All five fail at the same named check under `-O`. Ordinary and optimized baseline processes both pass all 636 checks.

## Reproduction

Run `python line_quantization_regression.py` and `python -O line_quantization_regression.py` for the valid formulas. For each of the five names above, append `--mutant NAME` to either invocation and require exit 1. The script uses only Python's standard library and has no external input or network dependency.

## Scope and exclusions

These are local universal/formal toy identities. No actual HM matrix entries, matrix products, source curvature, obstruction coordinates, one-shot replay, physical/source experiment, or source spike was read or evaluated. Nothing here constructs a square-zero quantized differential, proves a second-order lift, computes a Čech or Ext differential, or resolves the six-condition question. Finite regression evidence supplements, and does not replace, the algebraic argument in the source notes.

## Recorded execution transcript

The interpreter path is normalized to `python`; outputs and exit statuses are the previously recorded results, not a new run.

```text
python line_quantization_regression.py --mutant none
PASS: 636 exact checks; mutant=none; optimize=0
exit=0

python line_quantization_regression.py --mutant plain_map
FAIL after 163 checks; mutant=plain_map; optimize=0: right-module linearity -1->1; residual witness ((0, 1, -2, 3, 2, 3), Fraction(1, 12))
exit=1

python line_quantization_regression.py --mutant wrong_hom
FAIL after 163 checks; mutant=wrong_hom; optimize=0: right-module linearity -1->1; residual witness ((0, 1, -2, 3, 2, 3), Fraction(1, 4))
exit=1

python line_quantization_regression.py --mutant dropped_root
FAIL after 1 checks; mutant=dropped_root; optimize=0: finite D monomial n=-3 i=0; residual witness ((0, 0, -1, 0, 1, 3), Fraction(1, 7))
exit=1

python line_quantization_regression.py --mutant reversed_order
FAIL after 631 checks; mutant=reversed_order; optimize=0: noncommuting matrix composition; residual witness 'matrix/vector differs'
exit=1

python line_quantization_regression.py --mutant missing_mixed
FAIL after 26 checks; mutant=missing_mixed; optimize=0: module associativity n=-3; residual witness ((1, 1, 0, 6, 2, 0), Fraction(5, 48))
exit=1

python -O line_quantization_regression.py --mutant none
PASS: 636 exact checks; mutant=none; optimize=1
exit=0

python -O line_quantization_regression.py --mutant plain_map
FAIL after 163 checks; mutant=plain_map; optimize=1: right-module linearity -1->1; residual witness ((0, 1, -2, 3, 2, 3), Fraction(1, 12))
exit=1

python -O line_quantization_regression.py --mutant wrong_hom
FAIL after 163 checks; mutant=wrong_hom; optimize=1: right-module linearity -1->1; residual witness ((0, 1, -2, 3, 2, 3), Fraction(1, 4))
exit=1

python -O line_quantization_regression.py --mutant dropped_root
FAIL after 1 checks; mutant=dropped_root; optimize=1: finite D monomial n=-3 i=0; residual witness ((0, 0, -1, 0, 1, 3), Fraction(1, 7))
exit=1

python -O line_quantization_regression.py --mutant reversed_order
FAIL after 631 checks; mutant=reversed_order; optimize=1: noncommuting matrix composition; residual witness 'matrix/vector differs'
exit=1

python -O line_quantization_regression.py --mutant missing_mixed
FAIL after 26 checks; mutant=missing_mixed; optimize=1: module associativity n=-3; residual witness ((1, 1, 0, 6, 2, 0), Fraction(5, 48))
exit=1
```

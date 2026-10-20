# Independent homogeneous primitive-bound audit

## Result

The authenticated primitive entries have carrier pole order at most **two** in the actual homogeneous source model. The stronger primary bound is one. The auxiliary bound two is necessary already for the literal entry `P[1,8]`. No primitive contraction identity, full structural A proof, physical matrix product, source evaluation, polynomial expansion, or old computation receipt is needed for this conclusion.

This is a proof of the undifferentiated primitive carrier bound. It does not certify the later physical legal-line ledger, moving-frame connections, residual, HPL expressions, aggregate bounds.

**Final producer packet accepted:** `homogeneous-primitive-bound-20261018/PROOF.md`, SHA-256 `b8d85b3adb79b69953a6ac1d13e69d9aa2e0b679653822af6bd6834cffedb18b`. An exact reviewed copy is included as `inputs/reviewed-PROOF.md`; `reviewed-producer-pins.json` also pins the inspected producer checker and separately accepted finite structural proof/review. The acceptance includes the bounded homogeneous contraction corollary discussed in section 7.

## 1. Source authenticity and exact scope

The six files in `inputs/` are frozen source text/data. The independent checker verifies their SHA-256 and Git blob identifiers. The model bytes and pinned JavaScript match the existing independent literal-primitive audits; the model's canonical JSON SHA-256 is `b6b532c4bab5787397a4cddde34210c12fae71853b30cb73ecbe8a9c2b4826b2`.

For this audit I also made independent, read-only GitHub fetches of the following four exact files, and inspected the returned contents:

- `frames-and-poles.md`, blob `46470b5a7198be2f8c39f9cb5f5a904ae355ec97`, at `491306fd2f7f8a04c29784afa48a6cb8a467f154`.
- `verify_homogeneous_identities.py.txt`, blob `25816d9ba8699ffaf20c562d9dd8403f049ae383`, at the same ref.
- `verify_chart_and_lines.py`, blob `a22f5ee026ff8f5476f4a8b65328cd057ac7c2de`, at `dc60a859a0157b1d2d1b57b37324509abc22c600`.
- `verify_divisor_seeds.py`, blob `0dd8cc61c192675ea0aa0b3dc812f37e48f9aeb2`, at the latter ref.

Exact original URLs are recorded in `independent-remote-reads.json`. The inputs are used as **definitions**, not as proof from their past PASS outputs. Their executable bodies were neither imported nor run. In particular, no call to their SymPy matrix or polynomial arithmetic occurred.

The source explicitly specifies these homogeneous weights:

| Primitive component | Weight |
| --- | ---: |
| gamma, delta, ev | +1 |
| H0, H1, eta | -1 |
| I column 0, column 1 | 0, +1 |
| P row 0, row 1 | 0, -1 |
| W, L | 0 |

The pinned JavaScript's `build2` uses exactly `I/di`, `P/dp`, `H0/dh`, and `H1/dh`, at its coefficient vector `es`, with `vars=es.slice(1)`. Its elementary kernel primitives use the same `pivot` and coordinate ratios. The original homogeneous constructor uses precisely the above row/column weights. Thus the dictionary is not an invented grading on an unrelated program.

## 2. Uniform homogenization lemma

Let an actual nonzero finite entry be `p/d`, with assigned weight `w`, numerator degree `n`, and denominator degree `D`. Write `Hom_k(p)` for its usual degree-k homogenization using `v0`.

The original source defines

    e = max(0, n-D-w),
    f = Hom_(D+e+w)(p) / (v0^e Hom_D(d)).

If `K >= D` and `n <= K+w`, then `q=K-D-e >= 0`, and

    Hom_(K+w)(p) = v0^q Hom_(D+e+w)(p).

Consequently the same homogeneous rational entry is

    f = Hom_(K+w)(p) / (v0^(K-D) Hom_D(d)).

This is an identity of rational homogeneous functions, not a new extension chosen at infinity. Every exponent `K+w-|alpha|` of `v0` in its numerator is nonnegative. The checker validates these integer exponent equalities for all 619 literal numerator terms. Setting `v0=1` recovers exactly the original `p/d`; the numerator and denominator differ in degree by exactly `w`.

The zero entries are unchanged and require no denominator. All 451 nonzero and 1,259 zero primitive positions are covered.

## 3. Actual numerator ceilings and denominators

The independently computed maxima below are degrees of the original affine numerator records. No rational simplification or hidden cancellation is used.

| Owner | D | I0 | I1 | P0 | P1 | H0 | H1 | K |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 4 | 5 | 5 | 4 | 4 | 4 | 4 | 5 |
| 1 | 5 | 5 | 6 | 5 | 4 | 4 | 4 | 5 |
| 2 | 5 | 5 | 6 | 5 | 4 | 4 | 4 | 5 |
| 3 | 5 | 5 | 6 | 5 | 4 | 4 | 4 | 5 |
| 4 | 5 | 5 | 6 | 5 | 4 | 4 | 4 | 5 |
| auxiliary | 4 | 6 | 4 | 4 | 5 | 4 | 5 | 6 |

Here `I0/I1` are columns and `P0/P1` are rows. The denominator fields `di,dp,dh` agree within each carrier. For primaries, the required ceilings `K+w` are respectively `5,6,5,4,4,4`. For the auxiliary carrier they are `6,7,6,5,5,5`. Every entry satisfies its own ceiling; a single undifferentiated matrix-wide weight would be wrong.

Put

    h_j = v_j^5 - v0 v1 v2 v3 v4,
    a = v0 v1 v3 v4.

The exact denominator records, with the uniform homogenization above, give:

- Every primary `j`: `v0^(5-D) Hom_D(d) = -h_j`.
- Auxiliary: `v0^(6-4) Hom_4(d) = -v0^2 v1^2 v3 v4 = -v0 v1 a`.

For `j=0` the additional `v0` is already the owned factor of `h0`; for `j>0` there is no additional `v0` denominator. In the auxiliary case the extra `v0^2` is an owned part of `a^2`, whose quotient by the uniform denominator is `-v3 v4`.

Hence multiplication by `h_j` clears every primary `I,P,H0,H1` entry, and multiplication by `a^2` clears every auxiliary entry. Their cleared numerator degrees are `5+w` and `8+w`, respectively. This proves a uniform carrier-two bound without any additional hyperplane pole outside the owner's clearing divisor.

## 4. A genuine counterexample to the affine shortcut

The auxiliary literal entry `P[1,8]` has

    p = v1^3 v3 v4,     d = -v1^2 v3 v4,     w = -1.

Its finite simplification is `-v1`, but its authenticated homogeneous expression is

    -v1 / v0^2.

This follows directly by subtracting the displayed monomial exponent vectors: `n=5`, `D=4`, and `e=2`. The homogenized numerator has no `v0` factor. The entry has a genuine double pole at the generic point of `v0=0`. Multiplication by `a` leaves a simple `v0` pole, while multiplication by `a^2` clears it.

Therefore the tempting auxiliary denominator of degree five, `-v1 a`, is insufficient. It would require a negative `v0` numerator exponent for this entry, and also fails auxiliary `I0` and `H1` ceilings. The authentic `frames-and-poles.md` explicitly warns that an auxiliary seed can require `v0^2`.

The failure persists on the actual product geometry. With only the first factor at infinity, the local source product is `(t1+z) product_(i>1)(1+x_i z)`. Here `v0=t1`, and at `t1=0` the coefficient `v1` is one; `v3,v4` are generically nonzero. Thus the same entry has a double pole along that standard infinity divisor, while the pulled-back auxiliary carrier has order one.

This example also explains why restriction to the finite chart cannot establish the homogeneous bound unless the actual bundle weight is retained.

## 5. Elementary primitives and the actual product-chart map

The regular source constructs `gamma,delta,ev` with degree-one homogenization. Every literal numerator has degree at most one, so these maps have no carrier pole.

For pivot `p`, the source's nonconstant `W` entries are `-v_r/v_p`, its nonzero `eta` entries are `1/v_p`, and `L` is a constant selector. Primary pivot `j` has `v_j` dividing `h_j`; the auxiliary pivot is `0`, with `v0` dividing `a`. Thus these elementary maps satisfy carrier-one bounds (or zero for `L`), with exactly the specified weights.

The actual source coefficient map is given by the coefficients of

    product_(i=1..4) (Y_i + X_i z).

It has multidegree `(1,1,1,1)` and has no base point: a product of four nonzero linear polynomials over the residue field is nonzero. On the finite chart `Y_i=1` it is precisely the coefficients of `product(1+x_i z)`, with `v0=1`. On an infinity coordinate, `X_i=1, Y_i=t_i`, its factor becomes `t_i+z`.

Factor by factor,

    t_i + z = t_i (1 + (1/t_i) z).

Thus on every overlap `v_local = tau v_affine`, where `tau` is the product of the changed `t_i`. This proves the coefficientwise identity for all sixteen charts without expanding the product or executing the source checker. A weight-w rational primitive consequently transforms by `tau^w`, as its bundle model requires.

Pulling back the globally polynomial cleared numerators in section 3 gives actual polynomial local representatives on every product chart. The cleared numerator degrees are the required coordinatewise twists because each coefficient `v_j` has degree one in every coordinate pair. No separate inversion of `v0`, and no unsupported Laurent multiplier, is introduced. Source geometry and finite restriction are therefore both accounted for.

Physical dressing by the source's legal-line factors is a separate later operation. This proof establishes the homogeneous carrier component used by that operation; it does not silently claim all physical line factors are regular.

## 6. Independent checker and controls

Run:

    python check_independent_degrees.py
    python -O check_independent_degrees.py

Both runs pass and give identical output, recorded in `normal.json` and `optimized.json`. The checks use runtime `ValueError` conditions, not removable assertions. There are six deliberate rejection controls:

1. Auxiliary uniform denominator degree five.
2. Swapped `I` column twists.
3. Swapped `P` row twists.
4. Suppressed extra `v0` exponent.
5. Wrong homogenizing numerator degree.
6. An auxiliary denominator with an unowned `v2` factor.

These are static discrimination controls, not numerical source evaluations. Hashes bind frozen inputs; the proof in sections 2–5 supplies the semantic argument. No full structural A premise is used.

I also inspected the producer's complete static checker and replayed it normally and with `-O`. The two outputs are identical and match its supplied metadata report. Those two independent replays are saved as `producer-replay-normal.json` and `producer-replay-optimized.json`. That checker performs metadata arithmetic only; this is not execution of any historical polynomial checker.

## 7. Review of the homogeneous contraction corollary

The structural finite A theorem has separately received independent acceptance. Treating that theorem as a premise, the producer's homogeneous extension argument is valid. This corollary is distinct from, and unnecessary for, the carrier bound above.

The relative bundle twists can be chosen as

    K^-1=O(-1)^5, K^0=O^15, K^1=O(1)^10, K^2=O(2)^2,
    C=O + O(-1).

Gamma, delta and ev have the correct degree `+1` to map successive K terms. H0, H1 and eta have the correct degree `-1` for the reverse arrows. I:C→K^0 has column weights `(0,1)` and P:K^0→C has row weights `(0,-1)`. W and L have degree zero between `O(1)^8` and K^1.

Hence `gamma H0`, `IP`, `H1 delta`, and `Id15` are degree zero entry by entry. The same holds for `delta H1 + eta ev = Id10`, `H0 gamma = Id5`, and `ev eta = Id2`. The `(i,j)` entry of PI has degree `j-i`; off-diagonal zero entries are compatible with their nonzero weights. Each side condition likewise has a definite common weight in each matrix position, even when different positions have different weights.

For each defect entry of weight w, its homogeneous rational expression on `v0 != 0` is `v0^w` times its finite defect evaluated at `v_i/v0`. The finite theorem makes that defect zero. Equality on the dense open proves equality in the homogeneous function field, and hence on every relevant carrier localization and after pullback. This uses uniqueness of a fixed-weight rational lift; it does not attempt to deduce regularity at infinity from finite regularity. Regularity after carrier-square clearance was proved separately above.

No physical/root-line comparison, moving-frame identity, or new class identification follows solely from this corollary. The producer's stated boundary correctly preserves those separate obligations.

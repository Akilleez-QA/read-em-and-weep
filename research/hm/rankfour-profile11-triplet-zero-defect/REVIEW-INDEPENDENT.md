# Independent whole-proof review: triplet zero original defect

## Verdict

**PASS, conditional on the expressly imported actual-geometric premises.**

I independently reviewed the entire new `PROOF.md`, not merely its arithmetic. Its conclusion is valid in the stated actual rank-four maximal ordered plateau `(1,1)` setting: for `A_q = A_std(4) + O(-8)`, the original transpose defect is zero, `B` is equivariantly isomorphic to `O(6) + A_std(-6)`, and `deg L = -42`. No mathematical correction to the proof is required.

Exact reviewed proof SHA256:

`0b62e7739d3ff5ef52c5e8c76e50931f99f882015c037132370707f341c425c5`

This review does not exclude or realize the triplet quotient, close the profile, change a coarse-bin count, or certify every transitive geometric premise by a proof assistant.

## 1. Independently authenticated inputs and source scope

I independently fetched the following exact immutable URLs through the read-only GitHub connector and compared the full returned UTF-8 contents with the retained input files, byte for byte:

- [PR1194 top-four proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/e4de44641a53b0b3424102cd5fbaf3cf5821996d/research/hm/rankfour-profile11-top-four/PROOF.md): 22,067 bytes; SHA256 `56bb8a0aa5ada0f550e0967ef9e535838e9162c2ff2e5ced039a3f6ddb2aacf0`.
- [PR1185 low-top proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/236e0a3723c3d73ea7fb9e549376540a8e70508b/research/hm/rankfour-profile11-low-top/PROOF.md): 11,259 bytes; SHA256 `c3d21cb63ffac4c69247e8deba8ef352f673ac3a7b2f91507bc54fbecae943af`.

The independent copies are `inputs/independently-fetched-top-four.md` and `inputs/independently-fetched-low-top.md`. Both matches include the exact final-newline convention. The initially retained files had one extra trailing newline; the author corrected that copying defect while this review was in progress. The proof text and reviewed proof hash did not change.

The top-four input explicitly retains actual ambient rank 30, ranks `E=17`, `S=13`, degrees `deg E=deg S=-54`, generic derivative rank four, and endpoint ranks `K=13`, `L=9`. Its Section 9 leaves precisely the three written necessary source-D forms, including the triplet, and does not establish their realization or zero defect. Its source-D presentation has rank `5+8+3+1=17` and degree `-10-24-12-8=-54`. The scalar-tail source restriction is valid here and not borrowed from an unrelated rank-three ledger.

The two actual section gates are applied before any new kernel argument. Independently checked characters are

    H0(A_q) = A_std + V + P + D,
    H0(A_q(1)) = W' + S4 + 2T6.

The negative scalar tail contributes no sections at these twists. Each character fits its stated ambient gate. The new argument does not silently strengthen a coefficient-space injection to a fiberwise bundle injection.

Section 2 of the low-top input proves the actual endpoint filtration and three-column capacity before making the low-top supposition used in its later exclusion. It is therefore legitimate to use that section with this top-degree-four quotient. Its original defects are unrestricted. The current proof does not transfer a theorem whose actual central rank is seventeen to a new rank; it works in the original rank-thirteen dual bundle and invokes the stated arbitrary endpoint construction.

These source checks establish authenticity and applicability of the imported statements. They do not replace their explicitly retained transitive actual-geometric hypotheses with an independent construction of the HM family.

## 2. Original coherent map and degree bookkeeping

The actual rank-four graded transpose gives an injective map of vector bundles as coherent sheaves

    B -> C = A_q^*(-2) = O(6) + A_std(-6).

Here `deg A_q=4`, `deg C=-12`, and `rank B=rank C=4`. Consequently its cokernel is torsion, its length is exactly `t=-12-deg B`, and `t>=0`. Since `S` has degree `-54`,

    deg L = -54 - deg B = -42+t.

All signs and twists are correct. The map is the original actual transpose, so proving its cokernel vanishes proves the claimed original zero defect, not a zero defect obtained after saturation or a substitute modification.

## 3. Actual Gauss chain and all-height capacity

The saturated derivative kernel of a saturated bundle in the constant ambient remains saturated there. Thus each `F_j` and each graded quotient `G_j=F_j/F_(j+1)` is a vector bundle. Because `F_j` is the derivative kernel of its predecessor, its derivative lands modulo `F_j` in `(F_(j-1)/F_j)(-2)`. Dividing by its own derivative kernel gives the coherent injection into the preceding graded piece. Composing yields exactly

    G_j -> B(-2j) -> C(-2j).

No saturated image is required in either arrow. Its rank inequality gives nonincreasing `q_j<=3`. Every nonzero `F_j` has nonzero derivative: otherwise it would be a saturated horizontal subbundle of the constant ambient, hence constant in characteristic zero, whereas it lies in the bundle `S` with top degree at most `-1`. Hence the chain terminates and the ranks sum to nine, with degree sum `deg L`.

For a rank-`q` coherent injection, its nonzero generic determinant maps into the `q`th exterior power of the target. On `P1` this bounds the source determinant degree by the largest line degree in that exterior power. Applied to `C(-2j)` this is precisely the sum of its top `q_j` ordinary degrees. Thus the usual ordinary degree bound remains valid even if the original image and every intermediate image have torsion cokernels.

With `h_i=#{j:q_j>=i}`, the allowed heights satisfy `h1>=h2>=h3>=0` and sum to nine. Summing layer bounds gives

    deg L <= 6h1 - 6h2 - 6h3 - sum h_i(h_i+1).

Independently eliminating `h3=9-h1-h2` confirms the exact polynomial identity

    6h1 - 6h2 - 6h3 - sum h_i(h_i+1)
      = -30 - (h1-7)^2 - (h2-1)^2 - (h3-1)^2.

The center `(7,1,1)` is itself admissible. This is an exact ordinary all-height capacity, not a bound based on a selected height list. In particular `-42+t<=-30`, so `t<=12`.

## 4. Invariant divisor step

Taking the determinant of the equivariant rank-four injection produces an effective invariant zero divisor of degree `t`. Its support is invariant regardless of the particular linearizations, and multiplicities are constant on orbits.

The projective action factors through the faithful icosahedral `A5`. A finite subgroup of `PGL2(C)` fixing a point is cyclic; equivalently its derivative at the point is faithful, because a finite-order element fixing a point with derivative one is the identity. Cyclic subgroup orders in `A5` are `1,2,3,5`, giving orbit sizes `60,30,20,12`. Thus every nonzero invariant effective divisor has degree at least twelve. This proves the required dichotomy `t=0` or `t=12` once combined with capacity. No divisor reducedness, special orbit choice, or fiber-character condition is used.

## 5. Equality and determinant obstruction

If `t=12`, the lower degree identity and upper capacity bound both equal `-30`. The square terms must all vanish, so the unique height triple is `(7,1,1)`. In particular the first layer has rank three. Its degree bound is the sum of the top three degrees of `C(-2)=O(4)+A_std(-8)`, namely `4-8-8=-12`.

This first-layer bound must be attained. Each layer deficit is nonnegative, and their finite sum is the gap between the total degree and total capacity, which is zero. This establishes `rank G1=3` and `deg G1=-12` without presupposing any saturated intermediate image. As a cross-check the remaining six one-dimensional layer bounds sum to `2+0-2-4-6-8=-18`, giving the required total `-30`.

The determinant line of `G1` has its actual induced equivariant structure. The difference between two linearizations of `O(-12)` is a character of `G`, since global invertible functions on `P1` are constants. `SL2(F5)` is perfect, so this difference is trivial. Therefore the determinant is equivariantly the standard `O(-12)`.

The universal `SL2` representation `Sym2 W` is self-dual and determinant one; its torus weights are `z^2,1,z^-2`. Their pairwise products are the same three weights, and their total product is one. Hence

    wedge^2 A_std = A_std,
    wedge^3 A_std = 1,
    wedge^3(O(4)+A_std(-8)) = A_std(-12)+O(-24).

The first summand receives no equivariant map from `O(-12)`, because `A_std` has no invariant vector. The second receives no ordinary map, because its Hom space is `H0(O(-12))=0`. Thus the target admits no nonzero equivariant determinant map. A rank-three coherent injection on an integral curve has a nonzero third exterior power at the generic point, so this is a genuine contradiction. The exterior-power step does not require a fiberwise injective or saturated inclusion at every point.

## 6. Final consequence and independent check artifact

The positive-defect case is impossible. For `t=0`, the torsion cokernel of `B->C` has length zero and vanishes, so this actual map is an everywhere equivariant bundle isomorphism. Dualizing with the same twist shows its actual transpose `A_q->B^*(-2)` is also an isomorphism. Finally `deg L=-42`.

`verify-independent.py` independently checks the exact proof and source hashes, byte equality of the two source fetches, all nine irreducible character orthogonality relations, the two required gate products, vanishing of the trivial constituent of `A_std`, formal exterior-power and self-duality identities, the exact symbolic square completion, all displayed degree arithmetic, and the projective orbit-size minimum. It uses direct class-character inner products and the closed binary character polynomial, not the author's McKay recurrence or `characters.py`. It performs no height enumeration or bundle search and evaluates no actual HM coefficients, parameters, points, jets, tensors, instance matrices or ranks.

The checker was run successfully with Python 3 and SymPy 1.14.0. It deliberately rejects optimized Python execution so that its assertions cannot be silently disabled. Its output is saved in `VERIFY-INDEPENDENT.txt`.

The contribution is therefore a rigorously supported new necessary original image relation for this one previously open triplet form, with the proof's stated limitations intact.

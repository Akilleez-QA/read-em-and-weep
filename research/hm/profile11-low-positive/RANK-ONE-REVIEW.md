# Independent review: rank-one top-image exclusion

## Verdict

PASS for the stated branch exclusion, with no blocking mathematical issue found.

Reviewed file: `RANK-ONE-TOP-EXCLUSION.md`.

Exact reviewed SHA-256:

`2f480884b26a089bcd6f3633e75e790472cc493d9908dd83f0497c6b1fbe8d50`.

The result excludes generic rank-one top images for the source

`E = P O(-2) + 2T O(-3) + O(-10)`

in the two specified original-zero-defect labels. It does **not** exclude this entire source or either full label. No rank-two saturation assertion is imported. In particular, the residual rank-two branch with possible invariant torsion remains outside this verdict.

This review reconstructs the argument from the pinned splitting, strict-top, and PR796 inputs. It does not use the new rank-two polar lemma in the companion `PROOF.md`.

## Immutable inputs

The following originals are pinned to commit
`db51525015bb7c5e825833d550d08dedf6f6ea96` of `Akilleez-QA/read-em-and-weep`, under `research/hm/order-four-quadratic-load/`:

1. `ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md`, Git blob `b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3`.
2. `NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md`, Git blob `d7506dae49b4be43230450c4132bd5db91f137ef`.
3. `ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md`, Git blob `dcacf0bcdef8377c1ed7654e5b82659ea409456e`.
4. `one-one-endpoint-necessary-pairs.json`, Git blob `fe0afa410d89340d3082dc814277f89fbb582c19`.
5. `rank-three-quotient-frontier-144.json`, Git blob `8b5971092f9ef762584912609fd5e9301c4e271d`.

All five Git blob identifiers were recomputed from the local audit-input bytes and agree with these pinned identifiers.

Public source directory:

https://github.com/Akilleez-QA/read-em-and-weep/tree/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load

The other mathematical input is PR796, Sections 3 and 8, pinned to commit
`d2b43060c83328dd5118aee6b9288fcfa0c873ac`:

https://github.com/Akilleez-QA/read-em-and-weep/blob/d2b43060c83328dd5118aee6b9288fcfa0c873ac/research/hm/profile12-quadratic-block-exclusion/PROOF.md

The supplied byte-verified audit copy `PR796.md` has recomputed SHA-256
`622763aac375db7e17bc7cab472f1afda0477b0f769371a3b3ef845cd5c9e3b1`
and Git blob `46a0de762000f21182f6d3168f3ecfd63adaf75f`.

The original JSON records independently confirm:

- `G3.11.863639aa192e`: source index 69, original defect 0, `A_q = O(-10)+O(4)+O(6)`.
- `G3.11.73682b4c817f`: source index 72, original defect 0, `A_q = O(-10)+W O(5)`.
- Both original compatible-source lists contain `(0,2,0,0,0,0,0,1)`. The pinned splitting formula decodes it to the displayed E, of rank 17 and degree -54.

These checks only read exact formal metadata and source bytes. No actual map or selected-instance data was evaluated.

## 1. Classification and saturation of the rank-one image

Let `F=P O(-2)`, and let `L=O(t)` be the saturated rank-one top image in the positive part U. The image and saturation are equivariant. Since G is perfect, an equivariant line has no nontrivial coefficient character. Since U is center-even, t is even.

The strict-top lemma gives `H0(E^-(2))=0`. Since all lower source degrees are at most -3, the actual top map therefore injects `P=H0(E(2))` into `H0(L(2))=Sym^(t+2)W`.

For `U=O(4)+O(6)`, a line subbundle has t at most 6. Among the eligible even t, the only section representations containing P are t=4 and t=6, using `Sym^6 W=V+P` and `Sym^8 W=P+D`; the lower nonnegative even powers are 1, A, and D. The equivariant cross-channel `O(4)->O(6)` vanishes because `Sym^2 W=A` has no invariant. Thus the two possible lines are the direct summands claimed.

For `U=W O(5)`, t is at most 5 and even, hence at most 4. Only t=4 remains. The invariant space in `W tensor W` is one-dimensional, and its corresponding map `O(4)->W O(5)` is the twisted tautological inclusion, which is everywhere saturated.

In all cases the nonzero row system `F->L` has degree t+2 at most 8. Its common zero divisor would be invariant, and every nonempty invariant effective divisor has degree at least 12. Thus it has no common zero, and `F->L` is onto as a bundle map. This establishes saturation rather than inferring it from generic rank.

## 2. Exact kernel support and zero internal derivative

Put `K0=ker(F->L)`. At twist 2, the map on global sections is injective, so every K0 degree is at most -3. A block `Z O(-j)` with j at least 4 contributes `Z tensor Sym^(j-4)W` to `H1(K0(2))`; all contributions are genuine, with coefficient parity `(-1)^j`.

For t=4, the cohomology budget is V. The bound `(j-3)dim Z<=3` leaves only `V O(-4)`: at j=4 the coefficient must be V, at j=5 there is no small enough odd coefficient, and at j=6 the sole possible coefficient is trivial but contributes A rather than V. Larger j cannot contribute. This block already has the entire kernel rank 3, giving exactly `K0=V O(-4)`.

For t=6, the budget is D. The bound `(j-3)dim Z<=5` leaves only `D O(-4)` and `O(-8)`. At j=5 the possible W and Wp coefficients give `1+A` and P, not D; j=6 gives A; j=7 has no eligible odd coefficient. The first candidate also exceeds the kernel rank, and equivalently forces the nongenuine degree-minus-three coefficient `Wp-S` in the stated Euler calculation. The second gives `K0=Wp O(-3)+O(-8)`, using

`chi_G(K0(3))=P W-Sym^9 W=Wp-S`.

Its rank 3 and degree -14 agree with the exact sequence.

For either kernel the actual internal derivative lands in `2T O(-5)+O(-12)`. In the t=4 case every component vanishes by degrees. In the t=6 case the Wp block again has no channel by degrees; `O(-8)->O(-12)` vanishes by degrees, and `O(-8)->T O(-5)` has equivariant Hom zero because `Sym^3 W=S` contains no T. Hence kappa is zero in every case.

The PR796 Section 3 saturated-image proof applies verbatim with its line `O(14)` replaced by L: the internal image is zero and the external image L is saturated in `Q(-2)`. Consequently the full raw derivative image of F is saturated, has rank one, and `F^+/F=L(2)`. This application uses none of PR796's profile-(1,2) section-freeness assumptions.

## 3. Excluding the degree-four line

Here `F^+/F=O(6)` with `rank F=4`. The profile-free quadratic Gauss-gap lemma in PR796 Section 8 applies because F is a saturated pure quadratic subbundle of the original constant bundle and its derivative has rank one. Its alternatives are `b=2r` or `b<=r-1`. The pair `(r,b)=(4,6)` satisfies neither. This excludes t=4 in both labels without any assertion that `H0(E^+)=0`.

## 4. Constant projection for the degree-six line

Here `F^+/F=O(8)`, so `rank F^+=5` and `deg F^+=0`. Every splitting degree of a subbundle of a constant bundle is nonpositive; degree zero therefore forces F^+ to be an actual constant subspace bundle `C O`. Equivariant Euler characteristic gives

`C=chi_G(F^+)=-P+Sym^8 W=D`.

The injective external image of the full derivative quotient proves `C O intersect E=F`. The image `(E+C O)/E` is exactly the saturated `O(8)` summand of `E^+/E=A_q(2)`. Thus `E+C O` is saturated in the original constant ambient bundle, and the constant projection produces the actual saturated subbundle

`Z=(E+C O)/(C O) = E/F = 2T O(-3)+O(-10)`.

For clarity, the residual derivative assertion follows from the quotient diagram, not from an abstract splitting of the connection. Since C is constant, the derivative of Z is induced by the derivative of E followed by

`A_q -> A_q/L = O(-10)+O(4)`.

This composite is onto because `E->A_q` is onto, and it factors through `E/F` because the derivative of F has image L. Its image is saturated in the projected ambient quotient: it is `(E^+/(E+C O))(-2)`, and the original `E^+` is saturated. Therefore the exact Gauss quotient is indeed `A_Z=O(-10)+O(4)`.

Z has highest splitting degree -3 and is saturated in a constant bundle. The original strict-top lemma applies directly, giving `H0(Z^-(3))=0`, and hence an injection

`2T=H0(Z(3)) -> H0(A_Z(3))=Sym^7 W=Wp+T`.

This is impossible by multiplicity (and already by the dimensions 12 versus 8). Thus t=6 is excluded for the split label.

## Review boundary

No actual HM or source coefficients, parameters, points, derivatives, instance matrices, instance ranks, model experiments, scans, or large computation were used. The only executable checks were bounded source-metadata reads and byte/blob hashing. The proof review uses universal bundle arguments, finite representation support, the original zero determinant defect, and the pinned connection lemmas. No external writes were performed.

The review found no blocker and no necessary change to the mathematical claim. In particular, the distinction between excluding the rank-one top-image branch and excluding the whole source or label is correctly maintained.

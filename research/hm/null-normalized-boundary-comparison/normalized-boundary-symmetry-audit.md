# Independent audit: normalized first-boundary swap sectors

20 October 2026. Formal mathematical record; no obstruction coordinates were evaluated. No normalized smooth-87 premise is used.

## Verdict and required inputs

Accepted. The proposed pair Ext¹ dimension and refined swap decomposition are correct, using the accepted HM cohomology values h¹End(H)(−1)=5 and h¹End(H)(−2)=h¹End(H)(−3)=0. The actual normalized first boundary is comparable to every strict compensated-swap homogeneous first lift, but the bridge requires more than the sentence “H¹(O)=0 makes the splitting equivariant.” The explicit comparison argument below supplies the missing logical steps using the already accepted cusp pair-character Ext¹ vanishing and scalar first-order swap comparisons.

This is a boundary-uniqueness theorem in a specified symmetry sector, not an obstruction-vanishing theorem.

## 1. Pair coefficient and equivariant pushforward

Put B=(P¹_x)^4, Z=P²×P², and ρ=m∘p:B→P⁴. The χ12 part of normalized End cohomology is H¹(B,ρ*End(H)⊗L), L=O_B(−1,−1,0,0). There is no root-line remnant in End. The active and passive swaps are a=(12), b=(34), with natural permutation linearizations.

For a pair quotient P¹×P¹→P², its structure algebra splits as O⊕O(−1), with signs + and −. The active pair line O(−1,−1) is the pullback of O_P²(−1) with the symmetric linearization, so its two summands are O(−1) and O(−2), with signs + and −. There is no extra alternating sign from tensoring ordinary line bundles. The passive pair contributes O and O(−1).

Consequently the four (a,b) sectors on Z are, respectively,

(++): O_Z(−1,0),
(+−): O_Z(−1,−1),
(−+): O_Z(−2,0),
(−−): O_Z(−2,−1).

Their pushforwards under multiplication m:Z→P⁴ are

(++): 3O(−1)⊕3O(−2),
(+−): O(−1)⊕4O(−2)⊕O(−3),
(−+): 6O(−2),
(−−): 3O(−2)⊕3O(−3).

These are bundle splittings, not merely equal Hilbert polynomials. The finite map m is flat: source and target are smooth of equal dimension, and the fibers are finite factorizations of a binary quartic. Its line-bundle pushforwards are locally free. For each displayed offset (r,s), Künneth on P²×P² gives H^i(O(n+r,n+s))=0 for 0<i<4 and every n, because |r−s|≤2 prevents one P² factor from contributing H⁰ while the other contributes H². Horrocks then yields splitting into line bundles; the Hilbert polynomials determine the listed multiplicities.

The total is 4O(−1)⊕16O(−2)⊕4O(−3). With the accepted HM H¹ values, the sector dimensions are (15,5,0,0), summing to 20. Trace-scalar contributions vanish and do not change these H¹ numbers. The χ34 result is obtained by exchanging the pairs, so its active-antisymmetric/passive-symmetric sector also vanishes.

## 2. Why the actual transported boundary has the needed symmetry class

The global Moyal first-order source is strictly invariant under each compensated swap: geometrically exchange the two active factors and simultaneously change the corresponding parameter sign. The classical bundle has its natural permutation linearization, since its map to P⁴ and root divisor are permutation invariant. Work on a common equivariant refinement, or a functorial equivariant resolution, to avoid pretending an arbitrary initial Čech cover carries a strict action.

The original cusp b need not be strictly invariant as a cup-product cochain. For each compensated swap σ, use its actual scalar first-order comparison k_σ, satisfying

δk_σ=σb−b.

Existence follows from the accepted symmetry of the scalar-gerbe class; no equality of raw cup-product representatives is assumed. Compensated swap preserves the first-order product itself, so no additional unary first-order algebra change is required here.

Transform the cusp first lift u by σ and then remove this scalar discrepancy by the arrow correction −k_σ g. The resulting lift σu−k_σg has the same original first-order cusp ambient as u. Their difference lies in the corresponding pair-character End Čech complex. The accepted cusp pair-character Ext¹ vanishing therefore identifies them by an ordinary reduction-preserving module gauge.

Now normalize and split b with δc=ν*b, obtaining u_hat=ν*u−cg. Comparing the strict transformed boundary σu_hat with the c-splitting of ν*(σu−k_σg), their difference is a scalar multiple of g with coefficient

l_σ=σc−c−ν*k_σ

(up to the single overall sign determined by which difference is taken). Crucially δl_σ=0. Since H¹((P¹)^4,O)=0, l_σ=δr_σ. Thus this difference is itself an ordinary scalar module gauge.

Combining the two comparisons proves that strict σ fixes the gauge-equivalence class of u_hat. This is the precise role of H¹(O)=0. It does not assert that the explicit c is strictly equivariant, that arbitrary module Ext¹ vanishes, or that a coherent all-orders equivariant structure has been constructed.

## 3. Strict representative and comparison with any homogeneous first lift

The space of first lifts for the fixed global first-order Moyal algebra is an affine space over End-valued Čech one-cocycles; its gauge classes form a torsor for Ext¹. The previous argument shows the actual class is fixed under the finite compensated swap group. Average u_hat over that group on the equivariant refinement. The first-order equation is affine linear and invariant, so the average is still a solution. Each group translate differs from u_hat by a boundary, hence the average is in the same gauge class.

Deck-character projection can be made simultaneously, using the semidirect action with the swaps. The source and actual lift have the prescribed χ12 or χ34 character. In particular, for the s coefficient the resulting ordinary cochain is active-antisymmetric and passive-symmetric; for the t coefficient the roles reverse. This accounts for the parameter compensation rather than confusing geometric swap invariance with actual antisymmetry.

Let u_new be any other global-Moyal first lift satisfying that same deck and compensated-swap homogeneity. Its difference from the averaged representative is a cocycle in the active-antisymmetric/passive-symmetric Ext¹ sector. That sector has dimension zero by §1. Therefore u_new and the actual transported lift are related by an ordinary first-order module gauge.

This does rigorously license replacing the first lift within this restricted sector, provided the induced second-order gauge corrections are retained. Gauge invariance then preserves the full obstruction class for the same fixed global Moyal second jet. No assertion about independence from arbitrary normalized Ext¹ changes is needed; that larger space has dimension 20 in this character and is not zero.

## 4. Exact scope and outstanding source verification

Necessary premises are: the pinned HM H¹ ranks; the accepted cusp pair-character Ext¹ vanishing; natural permutation linearization of the actual bundle; actual scalar first-order comparison of b under compensated swaps; and the previously audited normalization/ambient splitting. Each is used explicitly above. This audit derives the finite pushforwards and the comparison mechanism; it does not freshly evaluate source cohomology certificates.

One cannot infer the conclusion merely from normalized H¹(O)=0, from the 20-dimensional unrefined Ext¹ result, or from an unspecified equivariant scalar linearization. The per-swap closed-cochain argument and affine averaging repair that potential gap without requiring a coherent scalar group action. A candidate lift must solve the actual global-star first-order equation and have the stated characters. Symmetry alone does not construct a second-order lift or annihilate its obstruction.

The full second-order transport from the prior audit remains mandatory: for scalar arrow B=exp⋆(−hc) and chart φ_i=id+h²D_i, its coefficient correction is −cu+(c²/2)g−μ₁(c,g)+D_i(g). Any subsequent ordinary first-order module gauge likewise carries its induced second-order terms. None may be dropped in a raw-residual comparison.

## 5. Review of the completed companion report

I subsequently read [normalized-boundary-comparison.md](normalized-boundary-comparison.md) in full, together with [dihedral-character-audit.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/43194f29b0f1b01dac1ef1cc92742359da5e6e34/research/hm/null-dihedral-mixed-vanishing/CHARACTER-AUDIT.md) §§3–4 and the pinned Perfect-Complex-D8-F3.md §1. These expressly supply h¹End(H)(−1)=5 and h¹End(H)(−2)=h¹End(H)(−3)=0. They remain imported audited ranks; no certificate was rerun.

The companion's §3 gives an equivalent constructive proof of the symmetry bridge: first project b to the compensated sector on the cusp, transport the module, and average there using cusp pair Ext¹ uniqueness; next project a scalar splitting primitive on the normalization to the same sector; finally compare the composed primitive with the original c using H¹(O)=0. Its signs and logic pass. The scalar presentation change in the first step can and should be chosen in the pair deck character by finite-group projection. Its module solution therefore remains in that character throughout.

Its §5 residual subtraction and linear-plus-Yoneda-square criterion also pass in the stated row convention. For a pure χ12 variation, every Ext¹ class is a-even, while the fixed homogeneous u and μ_P are a-odd. Hence the linear difference has a-odd parity and the Yoneda square has a-even parity, so equality of the complete obstruction requires both contributions to vanish separately. This does not assert either is actually zero. The same reasoning applies with the pairs exchanged.

There is no remaining logical gap in the symmetry-preserving replacement theorem, provided its stated imported premises are retained. The conclusion concerns the same global Moyal algebra and the same classical bundle, and must not be expanded to arbitrary normalized first-boundary choices.

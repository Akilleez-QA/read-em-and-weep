# The doubled fixed line determines the entire positive-coordinate quadratic image

## Theorem

Let F be the actual normalized Horrocks–Mumford bundle on P⁴, B=End₀(F), and G=SL₂(F₅). Write V for the three-dimensional positive coordinate representation, W for the negative two-space, and L=P(W*) for the negative fixed line. Put

    N₂=H¹(B(2))₊, P₃=H¹(B(3))₊, N₄=H¹(B(4))₊,
    q₊:Sym²V⊗N₂→N₄.

Let Q:N₂→N₄ be multiplication by the canonical invariant positive quadric. Let 2L denote the ordinary first infinitesimal neighborhood defined by I_L², not a reduced line and not the invariant quadric cone. Then the following are canonical equalities and quotient identifications:

    im q₊=im Q ⊆ N₄,
    coker q₊ ≅ H¹(2L,B|2L(4))₊ ≅ P.                (1)

Here P is the even four-dimensional irreducible. In particular the aggregate image has character 2V+3P+3D and dimension 33, while its cokernel has dimension four.

The first-neighborhood boundary is forced to be nonzero:

    H⁰(L,B|L(4))₊=D
       --∂--> H¹(L,V⊗B|L(3))₊=P+D,

and identifies D with the unique D summand. This nonvanishing is derived from exact sequences and the previously proved invariant-product theorem, not an evaluated scalar.

Let R=im[V⊗N₂→P₃] be the actual reachable middle, already identified with the restriction kernel and with P₃/R≅A. The next positive multiplication induces a canonical exact quotient channel

    0 → D → V⊗(P₃/R) → N₄/im Q → 0.              (2)

Thus the middle quotient A supplies the entire remaining target quotient P under the next positive arrow; its D channel is killed.

These statements concern quadratics in the positive coordinate variables only: Sym²V=1⊕D. They do NOT concern all inversion-even quadratics, which additionally include Sym²W=A. No source occurrence, c-d-f decomposition, selected coefficients, points or actual-instance computation is used.

## 1. Inputs and notation

The immediate inputs are PR931's positive-reachable-middle theorem at commit e28d3b74d4288239426ad1e675e806310fadf8be, research/hm/positive-reachable-middle/PROOF.md, blob 060ad3bacb45086349e911265d6c0d6157bef4a0; the existing geometric canonical-invariant-product theorem at eeb1a11799ca38a60c37f6ba96f263ef8e20dd1c, blob 019c1f31773476f0a4877d88632ce5d46fbd4b9f; and the primary section-resolution/regularity theorem at 063da90fc4543304e87e701cdefcc08225412f17, blob 58785a8799c43fd2c7da089d0ddc5e05822132a9. Exact paths and copied originals are recorded in audit-inputs/manifest.json. Only the conditional final corollary additionally uses PR929 at ad998827320a2302418730102cd2421943935784, research/hm/profile11-source127-cdf-invariant-branch/PROOF.md, blob 49a0b5ef9f6b2fa6fb5e46edd28fec4f4d73be79.

The reachable-middle theorem supplies

    F|L=O_L(3)₋⊕O_L(−4)₊,
    H²B(1)=H²B(2)=0,
    H³B(0)=H³B(1)=H⁴B(0)=0,
    R=ker[P₃→H¹(B|L(3))₊], P₃/R≅A.                (3)

It proves these assertions using the actual fixed-line geometry, structural twist-one vanishing and the primary section resolution, with no selected-instance evaluation. The invariant-product theorem gives

    ker Q=A+D, im Q=2V+3P+3D,
    N₄=2V+4P+3D, coker Q=P.                       (4)

The fixed irreducible identities used below are

    A=Sym²W, D=Sym⁴W, V⊗A=P+D.

All isomorphisms naming irreducible representations specify their isomorphism types, not chosen coordinate maps. The equality im q₊=im Q in (1), in contrast, is equality of the actual subspaces of N₄.

## 2. The universal resolution of the squared line ideal

The three positive coordinate forms generate I=I_L. Their ordinary square has the exact equivariant resolution

    0 → (V⊗Λ³V)⊗O(−4)
      → [(V⊗Λ²V)/Λ³V]⊗O(−3)
      → Sym²V⊗O(−2) → I² → 0.                   (5)

The coefficient representations have dimensions 3,8,6. Equivalently they are the Schur modules S_(2,1,1)V, S_(2,1)V and Sym²V. The last map is ordinary multiplication of two positive linear forms.

Here is a direct derivation retaining this actual augmentation. Work first over the coordinate ring S=Sym(V⊕W), with ideal I=(V). The Koszul resolution of I has terms Λ^(i+1)V⊗S(−i−1), for i=0,1,2. The Koszul resolution of I/I²=V⊗(S/I)(−1) has terms V⊗Λ^iV⊗S(−i−1), for i=0,1,2,3.

The quotient I→I/I² lifts to a chain map whose coefficient maps are the alternating inclusions

    Λ^(i+1)V → V⊗Λ^iV

with the consistent Koszul signs, and with identity in degree zero. These are injective; composing with exterior multiplication is a nonzero scalar multiple of the identity in characteristic zero. The mapping cone, shifted to resolve the kernel I², is exact. Cancel the identity block in degree zero and then the constant injective Λ²V and Λ³V blocks. Their coefficient quotients are

    (V⊗V)/Λ²V=Sym²V,
    (V⊗Λ²V)/Λ³V,

and the remaining left term is V⊗Λ³V. This gives (5) over S, with the multiplication augmentation inherited from I²⊂I⊂S. The cancellations use split constant coefficient summands, so preserve equivariance. Sheafification is exact, and tensoring with a locally free sheaf is exact.

This proves (5) universally for the regular linear ideal; no HM differential or selected coordinate value is used.

## 3. The aggregate cokernel is doubled-line cohomology

Tensor (5) with B(4), and abbreviate

    U₃=V⊗Λ³V, U₂=(V⊗Λ²V)/Λ³V, U₁=Sym²V.

The resolution becomes

    0 → U₃⊗B(0) → U₂⊗B(1)
      → U₁⊗B(2) → I²B(4) → 0.                  (6)

Let J be its intermediate image inside U₁⊗B(2). The first short exact kernel sequence gives H²J=0 from H²B(1)=H³B(0)=0, and H³J=0 from H³B(1)=H⁴B(0)=0. The second gives

    U₁⊗H¹B(2) ↠ H¹(I²B(4)),
    H²(I²B(4))=0,                               (7)

using H²B(2)=0. The restriction sequence

    0 → I²B(4) → B(4) → B|2L(4) → 0

therefore identifies the cokernel of actual positive-coordinate quadratic multiplication with H¹(B|2L(4)). Taking positive inversion parts is exact; U₁=Sym²V is positive. Consequently

    coker q₊ ≅ H¹(B|2L(4))₊.                     (8)

No incoming transgression is suppressed, and the map in (8) is actual restriction. The generator map of I² in (5) is precisely what identifies its cohomology image with im q₊.

## 4. The first-neighborhood extension has one possible boundary channel

Since L is a regular linear subspace,

    I/I²=V⊗O_L(−1).

The first-neighborhood sequence tensored by B(4) is

    0 → V⊗B|L(3) → B|2L(4) → B|L(4) → 0.        (9)

The ordinary square and the exact conormal sheaf are essential here. From the actual split in (3),

    B|L(3)=O_L(10)₊⊕O_L(3)₋⊕O_L(−4)₊,
    B|L(4)=O_L(11)₋⊕O_L(4)₊⊕O_L(−3)₋.          (10)

The sign changes include the physical sign of the hyperplane twist on the negative fixed line. In particular the positive-coordinate factor V is positive, but the conormal O_L(−1) is not parity-trivial.

Equivariant cohomology of (10) gives

    H¹(V⊗B|L(3))₊=V⊗A=P+D,
    H⁰(B|L(4))₊=Sym⁴W=D,
    H¹(B|L(4))₊=0.

Thus (9) yields an exact tail

    D --∂--> P+D → H¹(B|2L(4))₊ → 0.             (11)

Because D and P are nonisomorphic irreducibles, the image of ∂ is either zero or the unique D summand. In either case the last term contains a P and is respectively P+D or P. This does not infer nonvanishing from multiplicity one.

Now the invariant symbol q₀ lies in Sym²V, so im Q⊆im q₊. There is a canonical surjection

    coker Q=P ↠ coker q₊=H¹(B|2L(4))₊.           (12)

The forced P in (11) and the upper quotient P in (12) force equality: the last term is P, (12) is an isomorphism, and ∂ has image D. The kernel of the canonical quotient map (12) is im q₊/im Q, so that kernel is zero. This proves equality of the actual images in (1), not merely equality of their dimensions or characters.

No value of ∂ was calculated: its nonzero channel is forced by the independently known invariant-product theorem. This is the restriction-extension connecting map for the first infinitesimal neighborhood of L. It is not a first-smoothing or Bockstein map for the invariant quadric cone, and does not contradict the separately established vanishing of that different map.

## 5. The quotient A in the middle maps exactly onto the final P

We first justify surjectivity of the next positive linear multiplication

    b:V⊗P₃→N₄.                                  (13)

The ideal Koszul resolution of I_LB(4) has terms Λ³V⊗B(1), Λ²V⊗B(2), V⊗B(3). The same two-kernel chase as in Section 3 applies: H²B(2)=H³B(1)=0 kill the H² syzygy obstruction; H³B(2)=H⁴B(1)=0 kill the H³ obstruction; H²B(3)=0 gives H²(I_LB(4))=0.

For clarity the additional high-cohomology vanishings are structural. In the pinned tensor section resolution the terms are E₀(t)=15F(t−3)⊕4F(t−2), E₁(t)=35F(t−4), E₂(t)=20F(t−5), E₃(t)=2F(t−7). For every t≥0, the H³ diagonal is zero because H¹F(−t−1)=H¹F(−t−2)=0 and H⁰F(−t)=0; the H⁴ diagonal is zero because H⁰F(−t−1)=H⁰F(−t−2)=0. Hence H³B(2)=H⁴B(1)=0. H²B(3)=0 is the pinned regularity theorem.

It follows that the cokernel of (13) is H¹(B|L(4))₊, which vanishes by (10). This proves (13) is onto.

Because R is the actual image of the preceding positive arrow, multiplication gives

    b(V⊗R)=im q₊.

Indeed every element on the left is a sum of products of two positive linear forms applied to N₂, and commutativity identifies these with the symmetric quadratic action. Conversely every such product is in b(V⊗R). By (1), this common image is im Q.

Therefore (13) descends to a canonical surjection

    V⊗(P₃/R) ↠ N₄/im Q.

The source is V⊗A=P+D and the target is P. Equivariance forces the D component into the kernel and makes the P component an isomorphism. This proves (2). The quotient spaces and induced multiplication are canonical; choosing abstract irreducible identifications fixes its remaining scalar normalization only.

## 6. Conditional support refinement in the surviving c-d-f branch

This paragraph alone assumes an actual c-d-f occurrence and the nonscalar Type F alternative of PR929. Retain its actual negative-square quotient Π=N₄/im q₋≅V+P and source blocks X_F=V+P+2D and X_B=A+V+2P+2D. PR929 retains the aggregate quotient surjection onto Π and the vanishing B-source quotient row χ_B=0. The new equality im q₊=im Q therefore forces the canonical invariant map Q followed by N₄→Π to be onto.

In this surviving branch, χ_B=0 implies that the projection of Q(X_B) to Π is zero. Hence the invariant quotient map X_F→Π is onto. Equivariance and X_F=V+P+2D now give

    ker[X_F --Q--> N₄ → Π]=2D,
    (V+P)⊂X_F → Π=V+P is an isomorphism.          (14)

In particular its P component, left undecided by the earlier invariant-block character argument alone, is nonzero. This is conditional actual support information, not a source exclusion or a claim that Type F occurs.

## 7. The positive-coordinate multiplication family has unobstructed kernel lifting

This is a corollary for the same two-term multiplication family, not for the full nonlinear research problem. Put I=im Q and let M(q):N₂→N₄ be multiplication by q∈Sym²V. Equation (1) gives im M(q)⊆I for every q. The locus

    U={q∈Sym²V : M(q):N₂→I is onto}

is Zariski open and contains q₀, since M(q₀)=Q is onto I. Over U the algebraic family has rank 33, its kernel is a vector bundle of rank eight, and its cokernel is the constant quotient N₄/I≅P. This uses openness of surjectivity, not a selected minor or matrix evaluation.

More explicitly, let q(t) be any formal arc in Sym²V with q(0)=q₀ and put M(t)=M(q(t)). Choose a linear section s:I→N₂ of Q. Then M(t)s=id_I+E(t), with E(t) divisible by t, so its formal inverse exists by the Neumann series. The map

    s(t)=s(id_I+E(t))⁻¹

is a right inverse of M(t):N₂[[t]]→I[[t]]. For every k∈ker Q the formula

    k(t)=k−s(id_I+E(t))⁻¹M(t)k

lies in ker M(t) and has constant term k. Using N₂=ker Q⊕s(I), the same formula gives an isomorphism (ker Q)[[t]]→ker M(t). Thus every initial kernel class lifts freely, and all successive kernel-to-cokernel obstruction classes for THIS TWO-TERM MULTIPLICATION FAMILY vanish. The same argument applies to any finite collection of formal parameters, using the maximal-ideal-adic inverse.

Only positive-coordinate quadratics 1⊕D are involved. Directions in Sym²W=A are absent, and no conclusion follows for arcs with an A component or coupled A+D arcs. These formal kernel lifts do not construct actual source packets, solve other window equations or nonlinear lifting conditions, or prove Weil-class algebraicity. They are unrelated to any differently defined obstruction unless its identification with this precise two-term family is separately established.

## 8. Contribution and limitations

The previous image-sum arguments forced a large non-invariant curried channel but did not determine the aggregate positive-coordinate image. The doubled-line restriction now determines that actual aggregate image exactly and identifies the next positive quotient channel. Every non-invariant positive-coordinate product takes values in im Q, although its curried image can still be large inside V*⊗im Q.

This result is compatible with the earlier forced curried dimension 56: that dimension concerns an image in Hom(V,N₄), not the image of the aggregate map in N₄. Equality of aggregate images does not mean q₊ is the invariant product alone, and does not assert that q_D itself has full aggregate image im Q.

No conclusion is made about all inversion-even quadratics, the marked mixed squares, exact actual curried dimension, a c-d-f scalar/C² alternative, actual source membership, higher-order lifting outside the specific two-term family of Section 7, or algebraicity. No label or source-dual pair is excluded by this theorem.

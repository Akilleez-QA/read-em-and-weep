# The c-d-f even commutant and its split-line all-orders alternative

## Theorem and scope

Assume an actual source127 c-d-f occurrence, but do NOT assume Q(X_B)⊂Y_B. Let C_even be the full equivariant algebra of parameter-independent endpoint pairs (e₂,e₄) commuting with EVERY negative quadratic product T_a:X→Y, a∈Sym²W. Then:

1. C_even has dimension8, semisimple quotient C⁴, and a four-dimensional square-zero radical. It is strictly larger than the dimension4 full negative LINEAR-pencil commutant.
2. After imposing the same actual invariant Q, D_even,Q is either the common scalars or C². In the nonscalar case its unique idempotent with source scalars (0,1) has the target V part of Y_L on the F side and the P part on the B side. Two allowed graph shears are retained; no actual shear is selected.
3. In that nonscalar alternative the F eigenspace Q-block is onto, with kernel exactly the original D. Therefore D lifts formally to all orders for every negative quadratic direction. Using the known generic original second rank3 on A, the generic original pencil has rank36, kernel dimension5 and cokernel dimension1, and all later generic original Bocksteins vanish.
4. Under the ADDITIONAL one-sided condition Q(X_B)⊂Y_B, this nonscalar alternative is impossible. Thus its even Q-compatible algebra is scalar too.

These are conditional alternatives, not a source exclusion, actual existence or a determination of which algebra occurs. Parameter-dependent morphisms are not classified. The nonscalar even idempotent does not extend to the full negative linear pencil, so there is no conflict with PR935's scalar full-pencil Q-commutant.

## Immutable inputs

All inputs are exact originals authenticated in INPUTS.json:

- PR924, c6c25eaf0e5a67c27eee7c3ba4f000df55997692, research/hm/profile11-source127-cdf-pencil-algebra/PROOF.md, blob83f5aee293995257459229e6b323522224ce8f3d. It gives the actual direct constant blocks, simultaneous linear reconstruction and the entire represented full-linear algebra, including singular maps.
- PR935, a7707ba3e25592023eb69cc15686aa4ee1fdcb7c, research/hm/profile11-source127-cdf-bockstein-rigidity/PROOF.md, blob187fe2a8c1499e11afdb5002091aa3c144e1b4a3. It gives actual Y=imQ+imq₋, kerQ=A+D, imQ=2V+3P+3D, cokerQ=P, global original first vanishing and original second nonzero on A. Its surjective-block lifting argument applies to any block preserved by the quadratic family, not only full-linear projectors.
- PR1011, 446dbfd04f6fb689c30975174dcc23d6f4c88c64, research/hm/cdf-quadratic-reverse-map-vanishing/PROOF.md: the precise generated-source/joint-injective-target reconstruction lemma, restated and applied to F⊕B below. Its original public proof was independently fetched.
- PR1001, a7aa990e7705dd9dbf3d0fd34e437fa735c9e0f1, research/hm/cdf-preserved-b-symbol/PROOF.md, blobeebebae694f59e786aaebc64c3838d732b2a3832. Used ONLY for the final additional one-sided corollary, specifically kerQ⊂X_B.
- ACTUAL-THIRD-BOCKSTEIN-VANISHES-IDENTICALLY.md, db51525015bb7c5e825833d550d08dedf6f6ea96 under research/hm/order-four-quadratic-load, blob7c09fe95015d7c8d932b3a27be302ca09888112d. Used for its already established generic second rank3/kernelD and33 unit Smith factors, not to re-prove those facts or evaluate a source.

Write

    X=X_F⊕X_B,
    X_F=V+P+2D, X_B=A+V+2P+2D;
    Y=Y_F⊕Y_B⊕Y_L,V⊕Y_L,P,
    Y_F=P+D, Y_B=V+2P+2D, Y_L,V=V, Y_L,P=P.

The last two terms are the two irreducibles of the old L target block. They are not separate full-linear vertices. Their separation is possible only after omitting degree3.

## 1. Reconstruct exactly what the negative quadratics determine

We first prove the endpoint-to-middle lemma rather than assume even data determine a linear pencil. Suppose a source pencil M satisfies W·M₂=M₃ and a target pencil N satisfies ∩_l ker B_l^N=0. If f₂,f₄ intertwine every product B_m A_l, define

    f₃(Σ A_li^M x_i)=Σ A_li^N f₂x_i.

For a relation Σ A_li^M x_i=0, apply every B_m^N to its proposed image. Product intertwining makes the result f₄ B_m^M(0)=0. Target joint injectivity kills the image. Hence f₃ is well-defined, unique by source generation, and intertwines both linear arrows. Equivariance follows from uniqueness. Knowing all Sym²W products is enough since mixed products are recovered by polarization.

Apply this with source M=F⊕B and target the entire actual pencil N. The quotient bundles are Q_F=O(18), Q_B=Sym³W O(7). Thus source generation is the direct sum of the universal surjections

    W⊗Sym¹⁶W→Sym¹⁷W,
    Sym³W⊗(W⊗Sym⁵W→Sym⁶W).

Target joint injectivity is the actual presentation twisted by one:

    ker[N₃→N₄⊗H⁰(O(1))]=H⁰(E(1))=0,

because E=(P+D)O(-2)⊕(V+P)O(-4)⊕O(-8). No actual matrix rank is evaluated.

For any even endomorphism e, restrict e₄ to Y_F⊕Y_B and e₂ to X. The lemma extends this restriction to a full-linear map F⊕B→N. Compose with the actual projection N→F⊕B. The resulting full-linear endomorphism kills the L block. PR924's exact algebra has scalars on F,B,L and only a radical arrow L→F. Killing L sets its L scalar and radical arrow to zero. Consequently

    e₂=a on X_F and b on X_B,
    e₄=a on Y_F and b on Y_B.

The remaining e₄|Y_L is any equivariant map Y_L→Y. It is unconstrained by quadratics because X_L=0 and negative quadratic images are contained in Y_F⊕Y_B. Conversely every such choice is an even endomorphism. This proves exhaustiveness, not just an upper bound.

## 2. Exact eight-dimensional algebra

Use coordinates (a,b,d_V,d_P,α,β,γ), where

    α:Y_L,V→Y_B,V is one scalar,
    β:Y_L,P→Y_F,P is one scalar,
    γ:Y_L,P→(Y_B,P)^⊕2 is a two-vector,

and d_V,d_P are the two scalar diagonal actions on Y_L. There are four diagonal coordinates and four arrow coordinates. For rightmost-first composition the diagonal coordinates multiply and

    α''=b α'+d_V' α,
    β''=a β'+d_P' β,
    γ''=b γ'+d_P' γ.

Every arrow starts at a target-only L vertex and ends at F or B, so all products of arrows vanish. This gives a four-dimensional square-zero ideal J_even and quotient C⁴. Hence J_even is the Jacobson radical. The old full-linear algebra is the subalgebra d_V=d_P, α=γ=0; β is its single radical arrow.

## 3. Adding Q gives scalar or C², with all shears retained

Let D_even,Q be the unital subalgebra satisfying e₄Q=Qe₂. Its source action defines an algebra map to C² by e↦(a,b). This map is injective: if e₂=0, then e₄ kills imQ and every negative quadratic image. Actual generation Y=imQ+imq₋ forces e₄=0. More generally an element with a=b=λ is exactly the common scalar λ.

A subalgebra of C² containing the diagonal is either the diagonal or all C². Thus the claimed two possibilities follow. If nonscalar, there is a unique compatible idempotent p whose source coordinates are (a,b)=(0,1). Its d_V,d_P coordinates are bits ε_V,ε_P. Idempotence in the arrow formulas gives

    ε_V α=0, (ε_P-1)β=0, ε_P γ=0.

These conditions account for every graph shear. No diagonal normal form is assumed.

The source kernel/image of p are X_F,X_B. Its target kernel/image are graph-sheared representations with characters

    Y_0=Y_F+(1-ε_V)V+(1-ε_P)P,
    Y_1=Y_B+ε_V V+ε_P P.

Compatibility makes Q block diagonal between these eigenspaces. For each irreducible, its image multiplicity is bounded by the sum of source/target minima in the two blocks. If ε_V=1, the F block has V multiplicities1→0 and the B block1→2. Thus Q's image has at most one V, contrary to its actual two. Therefore ε_V=0, independently of both P choices and every shear.

If ε_P=0 also, maximal image characters are

    F:V+P+D, B:V+2P+2D.

Their sum equals the actual image, so both bounds are attained. In this case the B target image eigenspace is exactly Y_B, Q_B is onto, and its kernel is the unique A. Since p intertwines EVERY negative quadratic, this surjective B block formally lifts A to all orders. The actual second on A would vanish, contrary to PR935's imported theorem. Thus ε_P=0 is impossible.

The unique remaining character possibility is

    ε_V=0, ε_P=1, γ=0,

with α and β unrestricted by idempotence. On Y_L,V the image is α in Y_B,V, so the zero eigenspace contains its graph y-αy. On Y_L,P the image is y+βy in Y_L,P⊕Y_F,P, giving the corresponding graph in the one eigenspace. Their characters and Q footprints are

    Y_0=V+P+D (dimension12), Y_1=V+3P+2D (dimension25),
    Q_F:X_F↠Y_0, kerQ_F=D,
    kerQ_B=A, imQ_B=V+2P+2D, cokerQ_B=P.

The same constituentwise maximum argument proves all statements; it does not select which repeated copy is a kernel or the actual values of α,β. The idempotent, if it exists, is unique for the actual Q, so these formal shear parameters are not independent realized choices.

This remaining idempotent cannot be a full-linear endomorphism because its L diagonal values differ. Therefore full-linear scalar Q rigidity does not eliminate it.

## 4. Nonscalar even compatibility forces all-orders generic rank36

The F eigenspace pair is preserved by Q and every T_a, and Q_F is onto with kernel the original D in kerQ. Choose a right inverse s of Q_F as an existence device. For a formal kernel vector k∈D, recursively solve within X_F

    x₀=k, x_(n+1)=-s T_a x_n.

Every T_a x_n stays in Y_0, so Q_F x_(n+1)=-T_a x_n. Thus Σ tⁿx_n lies in the formal kernel of Q+tT_a. Equivalently the finite expression using (1+tT_a s)^(-1) gives a formal right-inverse construction. No actual section or scalar is evaluated.

All five dimensions of D persist formally for every a. The original generic second has rank3 on A, with kernel D, and Q has33 unit Smith factors. Hence over the generic parameter field the formal pencil has at least36 nonzero Smith factors (33 units and three factors of order2), while the five persistent kernel dimensions in a41-dimensional source give rank at most36. Therefore its rank is exactly36, kernel dimension5, cokernel dimension1. Every subsequent generic original differential on the surviving D is zero. This is an all-orders consequence of the hypothetical even splitting, not a computation of an actual generic rank or a proof the splitting occurs.

## 5. Additional one-sided preservation excludes the nonscalar even case

Suppose now Q(X_B)⊂Y_B. PR1001 proves the entire kerQ=A+D lies in X_B. But the only possible nonscalar even idempotent above has kerQ_F=D⊂X_F, with X_F∩X_B=0. These cannot both hold. Thus under the one-sided hypothesis D_even,Q is the common scalars.

This corollary does not follow merely from the absence of reverse maps: it uses the exhaustive even-algebra reconstruction and actual kernel placement. Conversely outside the one-sided branch the split-L alternative is not excluded or realized here. No statement narrows the raw three-dimensional cubic gate in the one-sided branch, and no source or source-dual pair is removed.

## Verification limits

verify.py authenticates all five inputs, proves universal multiplication surjectivity by explicit right inverses, checks the exact8-coordinate algebra and idempotent equations, exhausts all four target-bit choices and their constituent bounds, verifies the forced image/kernel/cokernel characters, and checks the formal lifting recurrence in a noncommuting symbolic expansion. No actual HM coefficient, source parameter, point, jet, matrix or instance rank is evaluated. The written bundle/reconstruction argument is a mathematical input to the bounded checker, not a proof-assistant claim.

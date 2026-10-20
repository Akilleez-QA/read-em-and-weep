# Publication scope

This is a preserved theorem manuscript, with the exact hypotheses and held identifications listed in unit 05 INPUTS.md. Abstract geometry and formal conditional implications are distinct from identification with the actual HM module or retained source. Historical words such as “new,” “remaining,” or “previously verified” describe the source manuscript, not a claim about the current research frontier.

# Finite collision-neighborhood detection and bounded primitive lifting

## 1. Result and scope

Under the regular coefficient-transport premises of `prerequisite full-target-collision-criterion, document PROOF.md (see the unit INPUTS.md)`, restriction to the ordinary thickening

    D_12 = (D, O_Z/I^12)

is injective on the transported 32-dimensional paired even obstruction space P⊂H²(Z,E)_χ. Here χ=sign|H for the order-eight pairing stabilizer, Z=(P¹)^4, E=q*B0⊗A^-2, A=q*O_P4(1), and D is the reduced union of the four triple diagonals. In particular, a paired class vanishes if and only if its regular representative has a regular primitive modulo I^12. This is a necessary-and-sufficient finite-neighborhood criterion, strengthening the earlier sufficient high-order representative criterion.

This does not assert restriction surjectivity, full H-sign injectivity without an exhaustive transport theorem, zero H²(I^12E)_χ, a primitive for the actual source, or any value of the thirty retained tests. D_12 has positive-dimensional support; finite order does not mean finitely many points or finite point sampling. All statements are conditional on the actual global regular coefficient identification, not a dense affine chart or a meromorphic transport.

## 2. Proof of injectivity, and the different surjectivity question

Take an affine quotient cover of Y=P⁴ and its inverse image in Z. Finite inverse images and their intersections are affine, so the regular Čech complexes compute coherent cohomology. Let Q_k=E/I^kE, Q_0=0. The exact coefficient sequence

    0 → I^12E → E → Q_12 → 0

and exact characteristic-zero χ projector give

    H²(I^12E)_χ → H²(E)_χ → H²(Q_12)_χ
        → H³(I^12E)_χ → H³(E)_χ.

If α∈P restricts to zero, it has an ideal-valued cohomology preimage. Represent that preimage by a closed regular χ cochain R in I^12E. Its unrestricted class is α. The preceding common-order theorem, with all three regular transports r=0,1,2 and injective constant inclusions, makes the constant, first-weight, and trace-corrected second-weight coordinates zero. These coordinates jointly detect P, so α=0.

Precisely what was used is

    P ∩ image[H²(I^12E)_χ→H²(E)_χ] = 0.

The image need not be zero outside P. Likewise the cokernel of restriction on the full H-sign sector is canonically

    ker[H³(I^12E)_χ→H³(E)_χ].

No vanishing of this kernel follows from the H² argument. For restriction on P the image can be still smaller. Even when the full restriction map is injective, it need not be surjective.

Equivalently, for a closed regular χ cochain c with [c]∈P,

    [c]=0 ⇔ ∃ b̄∈C¹(Q_12)_χ with δb̄=c mod I^12.

If an initial closed source c is not χ at cochain level but has class in P, first replace it by e_Hc; this preserves its class. The χ-primitive formulation below is applied to that projected representative, not to the discarded cochain components.

A quotient cochain b̄ lifts to an E-valued regular cochain b on this affine cover: affine section exactness supplies local lifts on every overlap, and averaging supplies χ. Then c−δb is closed and lies in I^12E. The common-order theorem makes its unrestricted class zero, so a global regular primitive exists. The lifted b itself need not already be that primitive; one must add a regular primitive of c−δb in the unrestricted E complex. The theorem constructs existence, not a preferred formula or a primitive lying in I^12E.

## 3. A bounded exact lifting procedure, including its indeterminacy

Set L_k=I^kE/I^(k+1)E for 0≤k≤11. There are exact sequences

    0 → L_k → Q_(k+1) → Q_k → 0.

For a fixed closed c∈C²(E)_χ suppose δb_k=c_k in Q_k. Lift b_k to a regular cochain b̃_k in Q_(k+1), and put

    r_k=c_(k+1)−δb̃_k ∈ Z²(L_k)_χ.

Changing b̃_k while fixing b_k changes r_k by a boundary. Thus o_k(b_k)=[r_k]∈H²(L_k)_χ is well defined. That particular b_k extends to a primitive at the next level exactly when o_k(b_k)=0.

Other primitives at level k differ by a closed 1-cochain z_k. The corresponding residual classes change by minus the connecting homomorphism

    ∂_k:H¹(Q_k)_χ→H²(L_k)_χ.

Consequently the choice-independent obstruction to existence of a primitive at level k+1, once one exists at level k, is

    ob_k(c) ∈ coker(∂_k),

represented by r_k. Its vanishing is necessary and sufficient: choose z_k realizing the necessary connecting class, modify b_k by z_k, lift, and add a layer-valued primitive of the resulting residual.

This gives a bounded criterion through k=0,...,11. It is not legitimate to require the raw class o_k for an arbitrarily frozen earlier choice to vanish: allowable H¹ corrections matter. At a later stage one may revise earlier compatible primitives by the restrictions of the chosen cocycle; the criterion concerns existence, not successful extension of every arbitrary partial choice. Conversely, any primitive modulo I^12 supplies a compatible successful chain by restriction. These are finite exact obstructions with specified coefficient groups and connecting maps; no infinite formal convergence or independent layer splitting is assumed.

### The neighborhood transition maps are surjective

There is an additional useful distinction from the unrestricted restriction map. Every L_k is supported on the projective surface D, so H³(L_k)=0. The long exact sequence therefore gives

    0 → coker[H¹(Q_k)_χ→H²(L_k)_χ]
      → H²(Q_(k+1))_χ → H²(Q_k)_χ → 0.

Thus restriction between two consecutive finite neighborhoods is surjective on H², and its kernel is exactly the obstruction quotient above. This does not imply surjectivity from H²(E): the sheaf I^12E is supported on all of the fourfold, so the preceding surface-support argument does not apply to it. These exact sequences give successive kernels, with all connecting-map indeterminacy retained, rather than an unjustified direct sum of layer cohomologies.

## 4. Conormal representations: the first layer is automatic

The audited complete-intersection geometry gives

    I/I² = U⊗A^-1|D,
    L_k = E|D⊗Sym^k(U)⊗A^-k|D,

where U is the two-dimensional S4 representation factoring through the standard representation of S3 on the three pairings. E and A have their natural pullback linearizations.

In fact (q_*L_0)_χ=0. To prove this, restrict a χ section to any triple-diagonal component. Its stabilizer in H contains a transposition of two of the three equal roots. This transposition fixes that component pointwise and acts trivially on the restrictions of the pullback bundles E and A, but χ of it is −1. Hence the section restricts to zero. Reducedness of D and local freeness of E|D imply injectivity into the sum of restrictions to the components, proving zero globally, including at quadruple collisions.

Thus Q_1 has zero χ pushforward and zero χ cohomology. Every regular χ source starts automatically in IE, and the primitive procedure can start with b_1=0: only the eleven possible layer tests k=1,...,11 remain.

More generally on a triple-diagonal component the relevant pointwise stabilizer in H is C2. The standard S3 representation has reflection eigenvalues +1 and −1, so the negative eigenspace in Sym^k U has dimension floor((k+1)/2). This describes possible componentwise χ coefficients. It is not a global direct-sum decomposition: component gluing at the quadruple diagonal still imposes relations, and no cohomological independence follows.

## 5. Exact sign-layer detector orders

Let K_n=(t₂^a t₃^b:2a+3b≥n), K_0=O_Y. The audited actual-subsheaf identity is

    (q_*I^k)_sign=O_Y(-3)K_(k-3), k≥3,

and is unrestricted O_Y(-3) for 0≤k≤3. Exact projection and the weighted associated graded give, with arbitrary twist r,

    (q_*(I^kEA^r/I^(k+1)EA^r))_sign
      = B0(r−5)⊗(K_(k−3)/K_(k−2))
      = ⊕_(2a+3b=k−3) B0(r−k−2)|N

for k≥3. For k<3 it is zero. The displayed direct sum is indexed by weighted monomials; fixed one-dimensional normalization factors may be restored. In particular degree four is also zero because 1 is not 2a+3b.

Multiplication by w_0=1,w_1=σ,w_2=τ=σ²−q*t₂/6 followed by full sign projection carries filtration degree k into k+r. Therefore its leading associated-graded output can be nonzero only at

    constant: k=3+2a+3b,
    first weight: k=2+2a+3b,
    second weight: k=1+2a+3b.

Within the source degrees 0≤k≤11 these lists are respectively

    constant: 3,5,6,7,8,9,10,11;
    first:    2,4,5,6,7,8,9,10,11;
    second:   1,3,4,5,6,7,8,9,10,11.

These identify which leading layers can feed each detector, not the number of independent obstruction tests. Zero in an associated-graded output means one further ideal order; higher terms may still contribute. In particular the lists cannot be used to delete extension data or to replace the thickened-neighborhood cohomology by separate reduced-surface cohomologies. On the generic triple-root stabilizer S3, the same pattern is the alternant formula: sign polynomials are the degree-three Vandermonde times invariants of degrees two and three.

## 6. Direct comparison to bounded downstairs detector thickenings

The three weighted maps themselves descend from Q_12 into finite downstairs quotients:

    (q_*Q_12)_χ → B0(r−5) / B0(r−5)K_(9+r), r=0,1,2,

using w_r and full sign projection. Indeed I^12E maps into the sign part of I^(12+r)EA^r, which is B0(r−5)K_(9+r). This supplies a concrete detector diagram on quotient coefficient complexes; the induced maps agree on the transported paired classes with the restrictions of the three global duality traces by the imported regular comparison.

The previous vanishing theorem gives H²(B0(r−5)K_(9+r))=0, so restriction of each corresponding global coordinate group to its displayed weighted thickening is injective. This is an additional reason the finite quotient detects all three coordinates. It does not claim every class on those thickenings lifts globally: the connecting H³ ideal groups control that separate issue.

## 7. Limitations

This work is universal sheaf algebra, representation algebra and exact-sequence reasoning. It evaluates no source, selected polynomial instance, matrix rank, physical jet or obstruction. The new finite criterion does not discharge its own regular-source or primitive premises.

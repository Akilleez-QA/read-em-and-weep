# Two irreducible sectors for the downstairs weight-two image

## Theorem and scope

Over C, retain the literal HM presentation and all linearizations in [the explicit quotient](../../derivative-transgression-relations/EXPLICIT-COEFFICIENT-QUOTIENT.md). Let

    U0=H¹(End H), U1=H¹(End H(−1)), U2=H²(End H(−2)),
    m011: U0⊗U1⊗U1 → U2,
    I=im(m011).

Here m011 is the linearization of the canonical ordered operation of [the downstairs Massey proof](../foundation-p04/WEIGHT-TWO-TRANSFER.md), and I means the span of all its values. There are two explicit, nonisomorphic irreducible ten-dimensional modules S and N for a finite monomial matrix group, with

    U2=S⊕N,    I∈{0,S,N,U2}.

Consequently dim I is 0, 10 or 20. For the stipulated reversal R, dim I_+ is respectively 0, 4 or 8. This is a restriction on the actual canonical image, not a nonvanishing assertion. No value of m011 is determined here.

## 1. Honest symmetry group and twist coherence

The [audited monomial classification](../foundation-p02/MONOMIAL.md), Sections 3–7, gives the projective monomial group of order 500 and unique bundle isomorphisms up to scalar. Conjugation on End H removes this scalar ambiguity, so End H has coherent pullback identifications. It is unnecessary to assert a coherent linearization of H itself.

To include the twists, use the finite matrix group

    Ghat={diag(c α^i β^(i²)) P_π : c,α,β∈μ5, π(i)=a i+b,
          a∈F5×, b∈F5}.

The conjugation formula in that classification shows closure: translating a quadratic exponent introduces only a fifth-root common scalar. The expressions are unique; hence |Ghat|=125·20=2500. Its central scalar μ5 is the kernel of Ghat→Gprojective. On O(−r) use the ordinary matrix-induced linearization, with the cochain convention f(v)↦T⁻¹f(Gv)T. Combined with the coherent End H identifications, this gives honest actions (or the equivalent opposite-group actions under the pullback convention) on every twisted End cohomology group and on products. A common scalar c acts on twist −r by c^(−r). In the literal complex, the scalar chain blocks have factors c^(t+1) in degree t, so for an internal-degree-k polynomial cochain of degree k−r the factor is c^(k−r)c^(−k)=c^(−r). Thus it acts trivially on U0, by c⁻¹ on U1 and by c⁻² on U2. The source and target central characters of m011 agree.

This avoids attributing an honest action on U2 to the projective order-500 group without addressing its twist cocycle. The subgroup c=1 of diagonal matrices is μ5²; it is sufficient for weight decompositions, although it need not be normal in Ghat. No action on the original coefficient algebra σ_*O_Y is asserted for Ghat or the whole projective group.

## 2. Target basis, signs and the two sectors

Write e_(p,T,i) for the quotient class with elementary B entry at (p,T_i), accompanied by its unique closed A block. The explicit quotient proves that the twenty classes with p∈{+,−}, T∈{U,V}, i∈F5 form a basis. Their μ5² weights are

    (a,2a²+δ), a=3i,
    δ(−U)=1, δ(+U)=2, δ(−V)=3, δ(+V)=4.

All twenty weights are distinct. Define

    S=span{e_(−,U,i), e_(+,V,i): i∈F5},
    N=span{e_(+,U,i), e_(−,V,i): i∈F5}.

Thus S consists of δ∈{1,4} and N of δ∈{2,3}.

For index translation π(i)=i+b, the permutation-chain formulas have output block K(1)=I and preserve the U,V types. The cochain action B↦K(1)⁻¹BM_π sends e_(p,T,i) to e_(p,T,i+b). It preserves δ and is transitive on its five lines.

For the multiplier π(i)=2i, the output block is J=[[0,1],[−1,0]], while M_π exchanges U and V with sign −1. Left multiplication by J⁻¹ sends the plus output basis vector to the minus one and the minus vector to minus the plus one. Right multiplication by M_π sends the U_i input covector to minus the V_(2i) covector, and conversely. Therefore exactly

    e_(+,U,i) ↦ −e_(−,V,2i),
    e_(−,U,i) ↦  e_(+,V,2i),
    e_(+,V,i) ↦ −e_(−,U,2i),
    e_(−,V,i) ↦  e_(+,U,2i).

It takes a to 2a and δ to −δ. These signs are formal basis transport, not multiplication or evaluation of source matrices. In particular its square is minus the index multiplier 4 on every displayed class, consistent with K(4)=−I. The chosen Z-zero quotient representatives are preserved by these operations, so no suppressed relation correction changes the formulas.

The diagonal subgroup, translations, multiplier 2 and central scalars generate Ghat. Each preserves S and N. Translations and multiplier 2 act transitively on the ten weight lines in each sector.

## 3. Irreducibility and classification of invariant subspaces

Any Ghat-invariant subspace W⊂U2 is invariant under μ5². In characteristic zero its character projectors split W into intersections with the distinct one-dimensional weight spaces of U2. Hence W is the direct sum of some of those lines. Closure under translations and multiplier 2 forces the chosen subset to be a union of the two ten-line orbits. It follows directly that

    W∈{0,S,N,U2}.

In particular S and N are irreducible. They are nonisomorphic: an intertwiner must commute with μ5², whereas their weight sets are disjoint. This argument does not assume that an invariant subspace of a direct sum splits without proof, and does not require normality of the selected μ5² subgroup.

## 4. Why the canonical image is invariant

The downstairs operation exists, is trilinear, and has zero indeterminacy by the cited weight-two proof. These facts imply equivariance under every compatible automorphism of the twisted End algebra: pull back the three representatives and two primitives; the resulting expression is a defining system for the transformed triple. Since its class is independent of the defining system, it equals the canonical operation on that triple. The coherent actions in Section 1 are compatible with differential, composition and twists, so this applies to Ghat. It follows that I is Ghat invariant, proving the theorem by Section 3.

This uses symmetry solely downstairs on P4. The monomial group need not preserve the symmetric-cover coefficient algebra, or act on Y. Nor is any covariance of a selected source-level homotopy or selector required. The canonical, zero-indeterminacy cohomology operation is the relevant object.

The same argument applies separately to each other ordering of weights (0,1,1). No equality between the images of different orderings is needed for this theorem.

## 5. Reversal, projected image, and coefficient transfer

For R with π(i)=4−i the established action is

    R e_(p,T,i)=−e_(p,T,4−i).

It preserves both sectors. Each of their two types has one fixed index i=2 with eigenvalue −1, and two two-element index orbits. Each orbit gives one positive difference and one negative sum. Therefore

    dim S_+=dim N_+=4,  dim S_−=dim N_−=6.

Since I is R-stable, e_+I=I∩U2,+. Its positive image is 0, S_+, N_+, or U2,+. This statement concerns projecting the image of the full downstairs tensor domain; restricting inputs in some further way would require a separate argument.

Separately, the weight-two proof establishes the leading-symbol image before projection as V2⊗I, using only surjectivity of μ11:Sym²V1→V2. The [22], D8-trivial coefficient projector picks a nonzero coefficient line L in V2, and that line is reversal-positive. Applying the retained positive projector therefore gives exactly

    L⊗I_+ ⊂ L⊗U2,+ = Q2,+.

Its dimension is 0, 4 or 8. This transfers the downstairs image restriction to the eight-dimensional eligible quotient; it does not extend the monomial group action to the coefficient algebra. Q2,+ is a canonical quotient, not a preferred physical eight-dimensional summand, and nothing here eliminates lower-weight contributions.

## 6. Two witnesses would suffice; none is supplied

To prove I=U2 it suffices to exhibit a nonzero quotient-coordinate coefficient of some m011 value in S and a nonzero quotient-coordinate coefficient of some (possibly different) m011 value in N. Indeed these imply that I contains weight lines in both orbits, by character projection and invariance. One value with nonzero components in both sectors would also suffice. This implies the full eight-dimensional projected span by Section 5.

A nonzero S witness alone proves S⊂I, and analogously for N; it does not force the other sector. No witness, nonzero scalar, actual representative or numerical certificate is provided here. Quotient coefficients refer to the Z-eliminated coordinates of the cited explicit quotient, not to arbitrary raw U/V entries before eliminating Z.

## 7. Character pruning for coordinate inputs

For the coordinate cocycle class t_lk=[v_l D_k]∈U0, diagonal weight is w_l−w_k, where w_j=(j,j²). The derivative class [D_i] has weight −w_i. Therefore a value

    m011(t_lk,[D_i],[D_j])

has weight

    (a,b)=(l−k−i−j, l²−k²−i²−j²) ∈ F5².

Put δ=b−2a². If δ=0, the corresponding target weight is absent and this value is zero. If δ≠0, the value lies in the single target line labeled (a,δ): in S for δ∈{1,4}, and in N for δ∈{2,3}. If additionally a=1, that line has index i_target=2 and reversal acts by −1 on it. Its positive projection is therefore zero, without needing the input triple itself to be reversal-invariant. If a≠1, positive projection is an injective map on that one-dimensional line, since reversal takes it to a distinct weight line; this does not imply the original value is nonzero.

The notation t_lk denotes coordinate-generated inputs, not twenty-five independent basis vectors of U0. The selection rule requires no assertion that these inputs span U0. In particular ∑_k v_kD_k=d is a global boundary (use the degree-grading endomorphism), so its cohomology class is zero. All weight arithmetic and the zero conclusions above are abstract representation statements, not evaluations of a Massey defining system or its coefficients.


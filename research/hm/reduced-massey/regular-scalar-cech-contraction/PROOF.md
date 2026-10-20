# Regular scalar Čech contraction and its exact comparison boundary

The scalar contraction is unconditional for the displayed standard-cover complexes. The Massey consequence in §§3–4 is conditional on the separately stated ordered-product and zero-indeterminacy hypotheses; see [Dependencies](DEPENDENCIES.md).

## 1. Complex and normalization

Work over C. Set S=C[x_0,...,x_4], with its standard grading, and U_i=D_+(x_i) in P^4. For a nonempty increasing index set I write

    C^q(k)= ∏_{|I|=q+1}(S[x_i^(-1):i∈I])_k.

This is the ordered alternating Čech complex for O(k). Its differential is

    (δf)_{i_0...i_{q+1}}=Σ_{r=0}^{q+1}(-1)^r f_{i_0...omit(i_r)...i_{q+1}},

with restriction to the common intersection understood. Extend components to arbitrary tuples by alternation, and put repeated-index components equal to zero. Every component is a finite linear combination of Laurent monomials x^α with α∈Z^5, |α|=k. Such a monomial is allowed on U_I exactly when its negative support N(α)={i:α_i<0} is contained in I.

Fix the coordinate ordering 0<1<2<3<4. For k∈{0,−1,−2}, define

    j(α)=min {i:α_i≥0}.

This index always exists: five negative integral exponents have total at most −5. Define h:C^q(k)→C^{q−1}(k), q≥1, coefficient by coefficient by

    (hf)_{I,α}=f_{j(α),I,α}.

Here the right-hand side includes the alternating insertion sign. If the insertion repeats an index it is zero. Set h=0 on C^0(k). This formula is a C-linear, entirely regular algebraic operator. Indeed, a nonzero right-hand coefficient has N(α)⊆{j(α)}∪I. Since j(α)∉N(α), it follows that N(α)⊆I, precisely the regularity condition for the output component. Finiteness is preserved because there are finitely many input components, each with finite monomial support. There are no completions or infinite Laurent series.

## 2. Homotopy identity

Fix α and abbreviate j=j(α). For a tuple I=(i_0,...,i_q), expansion at the inserted first index gives

    (hδf)_I=f_I+Σ_{r=0}^q(-1)^(r+1)f_{j,i_0,...,omit(i_r),...,i_q},
    (δhf)_I=    Σ_{r=0}^q(-1)^r    f_{j,i_0,...,omit(i_r),...,i_q}.

Thus δh+hδ=id in degrees q≥1. Alternation makes the identity valid also when j belongs to I. The argument is coefficientwise and hence proves the identity for all cochains, not merely cocycles.

For completeness, let H_k=S_k for k=0 and H_k=0 for k=−1,−2, regarded as a complex in degree zero. Let ι:H_k→C^0(k) be restriction of global sections. Let π:C^0(k)→H_k take the coefficient of x^0 in the U_0 component for k=0, and be zero for k=−1,−2. Set π=0 in all positive degrees. Then

    δh+hδ=id−ιπ,     πι=id,     h²=0,     hι=0,     πh=0.

To check the degree-zero identity, the inserted-index expansion is (hδf)_{i,α}=f_{i,α}−f_{j,α}. If N(α) is nonempty, the second term must vanish because N(α) cannot be contained in {j}. If N(α) is empty, k=0 forces α=0, and j=0; the second term is exactly ιπf. Repeated insertion proves h²=0, and (hf)_{0,0}=f_{0,0,0}=0 proves πh=0. The other side identities are immediate. This specifies a normalized deformation retraction, including the degree-zero exception.

In particular, for every regular algebraic scalar two-cocycle z,

    t=hz,     δt=z,     ht=0.

It is the unique primitive with ht=0: if δs=z and hs=0 then the degree-one homotopy identity gives s=hδs=hz. For two arbitrary primitives s,t, their difference satisfies s−t=δh(s−t). Thus the primitive ambiguity is explicitly scalar exact. The same h is linear, so bilinearity and antisymmetry are preserved whenever they are already identities of the scalar input cocycles.

This normalization depends on the coordinates and their ordering. No S-linearity, arbitrary projective equivariance, or compatibility with multiplication is asserted.

### Change of normalization and coordinate-multiplication coherence

Let h and h′ be two regular scalar contracting homotopies at the same allowed weight, each satisfying the positive-degree homotopy identity, and let z be a scalar two-cocycle. Then

    w=(h−h′)z,     δw=0,
    r=h w ∈ C^0(k),     δr=w.

The last equality is the degree-one homotopy identity applied to w. Thus changing the insertion rule, or any other regular choice with the same contraction property, changes its scalar primitive by an explicitly regular scalar boundary. No agreement of degree-zero projections is needed for this assertion.

For coordinate multiplication, let ℓ be a homogeneous linear form (in particular any coordinate x_i), and assume k,k+1∈{−2,−1,0}. Multiplication by ℓ defines a chain map C^•(k)→C^•(k+1). For δz=0 set

    w_ℓ=h_(k+1)(ℓz)−ℓ h_k(z) ∈ C^1(k+1),
    r_ℓ=h_(k+1)w_ℓ ∈ C^0(k+1).

Then δw_ℓ=ℓz−ℓz=0 and

    δr_ℓ=h_(k+1)(ℓz)−ℓ h_k(z).

All expressions are finite regular algebraic cochains. The same argument applies to any homogeneous polynomial multiplication whose source and target weights both lie in the permitted range. This is explicit boundary-level coherence on closed two-cochains. It is not strict S-linearity, a multiplicative contraction, or a proof of higher coherent comparison identities.

## 3. What this supplies to the Massey question

If z_pq is an actual scalar algebraic Čech two-cocycle at weight k∈{0,−1,−2}, then t_pq=hz_pq is an explicit regular algebraic primitive. In particular one may use z_pq=tr(p∪q)/2 for closed ordered algebraic Čech one-cochains p,q. Its closedness follows from the Čech DGA Leibniz rule and the trace commuting with restriction and δ.

This last statement does not assert that z_qp=−z_pq as cochains. The ordered Alexander–Whitney cup product is not graded commutative; swapping factors changes their overlap positions. Consequently graded trace cyclicity and the rank-two identities valid for endomorphism-valued differential forms cannot simply be substituted into that ordered Čech DGA. A common linear h preserves antisymmetry only if the prescribed scalar cocycles are actually antisymmetric before h is applied.

In particular the smooth formula

    −(1/2)B(b,L_X c) − t_bc a_X + t_Xb c

remains a formula in the Dolbeault DGA. The scalar h above has regular algebraic Čech inputs; it cannot be applied directly to smooth scalar (0,2)-forms. Nor does this construction provide algebraic representatives for L_X c or a product-compatible finite transfer of that displayed reduced formula. Regular scalar primitives alone therefore do not produce a regular algebraic version of the no-End-primitives formula.

## 4. A rigorous abstract bridge, without an effective reduced formula

There is nevertheless an explicit standard zigzag of DGA quasi-isomorphisms at the level of models. Let E=⊕_{k∈Z} End(H)⊗O(k) be the full twist-graded algebra; no finite twist truncation is taken. Write C_alg(E) for its regular algebraic ordered Čech DGA on the standard cover; C_hol(E^an) for the holomorphic Čech DGA on the analytic standard cover; T for the total Čech–Dolbeault complex; and A_global for the global Dolbeault DGA. Then

    C_alg(E) → C_hol(E^an) → T ← A_global.

The first map is analytification. The second puts holomorphic cochains in Dolbeault degree zero. The last restricts global smooth forms to the cover in Čech degree zero. On bidegree (p,q), take the total differential δ+(−1)^p bar-partial. For bidegrees (p,q),(r,s), the total product is (−1)^(qr) times ordered Čech cup combined with wedge and composition. These conventions make all three arrows DGA morphisms.

Why each arrow is a quasi-isomorphism:

1. The algebraic cover and every intersection are affine, so its Čech complex computes coherent algebraic cohomology in each twist. The analytic intersections are products of affine spaces and copies of C*, hence Stein, so holomorphic Čech computes coherent analytic cohomology. Proper GAGA on P^4 identifies these cohomology groups by analytification.
2. On each analytic intersection, the Dolbeault resolution computes coherent analytic cohomology, which vanishes in positive degree by Stein acyclicity. The spectral sequence in the Dolbeault direction proves C_hol→T is a quasi-isomorphism.
3. The sheaves of smooth bundle-valued (0,q)-forms are fine. Their augmented Čech complexes are acyclic in positive Čech degree. The spectral sequence in the Čech direction proves A_global→T is a quasi-isomorphism.

These assertions apply weight by weight, and therefore to the twist-graded algebra. The displayed construction uses only the existence of the algebraic bundle and its analytification, not its source matrices or any evaluated products.

Triple Massey products are preserved, including their indeterminacy, under DGA quasi-isomorphism. Therefore the Dolbeault class of the displayed smooth formula corresponds to the algebraic Čech singleton Massey class whenever the required ordered pair classes vanish and the stated indeterminacy is zero. In the algebraic Čech model, existence of pair primitives follows from precisely those vanishing cohomology classes; every resulting cochain has finite regular local expressions by the definition of C_alg. This is an abstract existence-and-identification statement for the original defining-system construction.

It is not a constructive inverse to analytification, nor an explicit finite algebraic transport of the reduced smooth expression. In particular it does not eliminate the End-valued primitives of an algebraic ordered Čech defining system, manufacture a regular algebraic L_X, or transfer strict rank-two form identities to that model. Such stronger conclusions require additional chain-level comparison data and their multiplicative homotopies, with signs and identities proved separately.

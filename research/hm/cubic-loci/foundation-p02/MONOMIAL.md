# Complete monomial symmetry locus of the literal HM bundle

## Result and scope

Work over a characteristic-zero field k, with indices in F_5 and the literal four-term presentation of [the exact-presentation proof](../../hm-presentation-independent/PROOF.md). For an invertible monomial coordinate transformation write

    (Gv)_i = s_i v_{π(i)},      s_i ≠ 0, π ∈ S_5.

There exist unrestricted constant matrices M (15×15), N (5×5), not both zero, satisfying

    M γ(v) = γ(Gv) N

if and only if

    π(i)=ai+b,    a∈F_5^×, b∈F_5,
    s_i=c α^i β^{i²},    c∈k^×, α^5=β^5=1.

On this locus the space of pairs is one-dimensional and every nonzero pair is invertible. Every such pair extends to a full chain isomorphism through the literal δ and ev tables. Consequently this is also exactly the monomial projective stabilizer of the isomorphism class of H, and

    dim_k Hom(H,G*H)=1 on this locus, and 0 outside it.

The projective group is isomorphic to μ_5² semidirect AGL(1,5); it has 500 elements over an algebraically closed characteristic-zero field. The permutation-only subgroup is precisely AGL(1,5), with 20 elements. This statement classifies monomial transformations only, not all projective symmetries.

## 1. The support partition

The literal γ has singleton rows Z_i supported at (column,label)=(i,i). Its ten other rows have two off-diagonal support pairs each:

    U_i: (i+2,i+1), (i+3,i+4), both coefficient +1;
    V_i: (i+1,i+3), (i+4,i+2), both coefficient −1.

These 25 support pairs partition all ordered (column,label) pairs. For any off-diagonal pair (c,l), the other pair in its row is

    τ(c,l)=(2c−l, 3c−2l).                         (1)

This follows by inserting each of the four displayed forms into (1); τ is an involution. In particular the two pairs in a row have distinct columns and distinct labels. Thus no linear combination of rows can have exactly one off-diagonal support pair: its mate occurs with the same nonzero row coefficient, and no other row can cancel it.

## 2. Unrestricted intertwiners force affine permutations

The Z_i row of γ(Gv)N has only variable v_{π(i)}. Every two-entry row of γ has a label different from π(i); uniqueness of that support pair forces its coefficient in the Z_i row of M to vanish. Singleton rows other than Z_{π(i)} likewise vanish. Therefore the Z_i row of Mγ is supported only at column π(i), label π(i). Since s_i≠0, comparison gives

    N_{i,j}=0 if j≠π(i).

Write n_i=N_{i,π(i)}. No invertibility assumption has been made.

In row U_i, the two possible nonzero support pairs on the right are

    (π(i+2),π(i+1)), coefficient s_{i+1} n_{i+2},
    (π(i+3),π(i+4)), coefficient s_{i+4} n_{i+3}.

They are off-diagonal, and their columns and labels are distinct. By Section 1, one cannot occur without the other. Hence n_{i+2}=0 if and only if n_{i+3}=0. These consecutive-index relations show either every n_i is zero or every n_i is nonzero. In the former case N=0 and Mγ=0; uniqueness of every row's support pairs then gives M=0. Thus every nonzero pair has all n_i≠0.

The two transformed pairs in every U or V row must consequently be mates under τ. As the original U,V rows cover all off-diagonal pairs, simultaneous permutation of columns and labels must preserve τ. Its first component says

    π(2c−l)=2π(c)−π(l)    for all c≠l.             (2)

Take l=c−1. Then π(c+1)−π(c)=π(c)−π(c−1) for every c∈F_5. All successive differences are the same a, so π(i)=ai+b. Bijectivity implies a≠0. Conversely every such affine map preserves (1). This proves necessity for arbitrary invertible scales s, not merely for pure permutations.

## 3. Explicit permutation intertwiner

Let π(i)=ai+b. Set P_π to have entry 1 in row i, column π(i), and zero elsewhere, so (P_π v)_i=v_{π(i)}. Define N_π=P_π. Define M_π by the following nonzero entries:

    (M_π)_{Z_i,Z_{π(i)}}=1;

    if a=1 or 4:
      (M_π)_{U_i,U_{π(i)}}=1,
      (M_π)_{V_i,V_{π(i)}}=1;

    if a=2 or 3:
      (M_π)_{U_i,V_{π(i)}}=−1,
      (M_π)_{V_i,U_{π(i)}}=−1.

The missing index of the four labels in any two-entry row is its row index i, so its transformed row index is π(i). Multiplication by a=±1 preserves the U and V types, while multiplication by a=±2 exchanges them. The displayed signs correct their opposite literal coefficients. Comparing the two support pairs in each row, and the singleton Z pair, gives

    M_π γ(v)=γ(P_πv)N_π.                           (3)

All matrices are invertible signed permutation matrices.

For pure permutations this pair spans the entire intertwiner space: after comparing either coefficient in each U row, the common sign correction in M_π forces n_{i+2}=n_{i+3}. Thus all n_i equal one scalar, and disjoint row supports determine M uniquely. The same conclusion also follows by reduction to the identity case of the diagonal theorem.

## 4. Independent full-chain extension for permutations

Recall D_{pq}(v)=v_p e_q*−v_q e_p*. The remaining literal tables are

    δ(U_i)=(D_{i+2,i+3},0),
    δ(V_i)=(0,D_{i+1,i+4}),
    δ(Z_i)=(D_{i+1,i+4},D_{i+2,i+3}),

and ev is paired evaluation. Let R=P_π on the covector-coordinate blocks. Define

    J = [[0,1],[-1,0]],
    K(1)=I, K(2)=J, K(3)=−J, K(4)=−I,
    A_π=K(a)⊗R,   B_π=K(a).

We prove separately that

    A_π δ(v)=δ(P_πv)M_π,
    B_π ev(v)=ev(P_πv)A_π.                         (4)

Put w=P_πv. The formal identity

    R D_{π(p),π(q)}(v)=D_{p,q}(w)

follows by comparing its two covector coefficients. For a row index i define E_i=D_{i+2,i+3}(w), F_i=D_{i+1,i+4}(w). Since π(i+r)=π(i)+ar, the complete list of transported forms is

    a=1: R D_{π(i)+2,π(i)+3}= E_i,
         R D_{π(i)+1,π(i)+4}= F_i;
    a=4: R D_{π(i)+2,π(i)+3}=−E_i,
         R D_{π(i)+1,π(i)+4}=−F_i;
    a=2: R D_{π(i)+2,π(i)+3}= F_i,
         R D_{π(i)+1,π(i)+4}=−E_i;
    a=3: R D_{π(i)+2,π(i)+3}=−F_i,
         R D_{π(i)+1,π(i)+4}= E_i.                 (5)

Every D on the left in (5) is evaluated at the formal v; no value of v has been chosen. These signs just record the displayed ordering of the two endpoints.

For a=1 or 4, multiplying both blocks by K(a) corrects precisely the common sign in (5). The columns U_{π(i)}, V_{π(i)}, Z_{π(i)} therefore become δ(w)U_i, δ(w)V_i, δ(w)Z_i respectively, as required by M_π.

For a=2, applying A_π to those three columns gives respectively

    (0,−F_i),  (−E_i,0),  (F_i,E_i).

These are δ(w)(−V_i), δ(w)(−U_i), δ(w)Z_i, exactly the columns prescribed by M_π. For a=3, (5) and K(3)=−J give the identical three results. This proves the first equation of (4), including all Z signs.

Finally, as row vectors, w^T R=v^T: the coefficient in column π(i) is w_i=v_{π(i)}. Thus paired evaluation after K(a)⊗R is K(a) times paired evaluation at v. This proves the second equation of (4). All four blocks are invertible, yielding a literal chain isomorphism.

## 5. Scales and permutations cannot conceal one another

Write G=D_s P_π, where D_s=diag(s_i). Section 2 already proves that a nonzero initial intertwiner for G forces π affine, independently of the scales. For affine π use the invertible pair of (3), and replace the formal variables by w=P_πv. Then

    Mγ(v)=γ(D_sP_πv)N

is equivalent to

    (M M_π^{-1}) γ(w)=γ(D_s w)(N N_π^{-1}).        (6)

This is a vector-space isomorphism of intertwiner spaces and preserves zero/nonzero pairs and invertibility. The complete diagonal theorem in [the audited diagonal proof](DIAGONAL.md) applies to (6): a nonzero pair exists precisely when

    s_i=c α^i β^{i²},     α^5=β^5=1,

and its space is one-dimensional with all nonzero pairs invertible.

For sufficiency on the full complex, let C_s denote the four diagonal chain blocks constructed explicitly in Section 6 of that proof, and let C_π denote the four blocks just constructed. Blockwise products C_s C_π satisfy the chain equations for D_sP_π. Indeed evaluate the C_s identities at P_πv and then use the C_π identities. This verifies all differentials, rather than inferring bundle sufficiency from γ alone.

## 6. Bundle necessity and group structure

The exact-presentation and degree-gap argument cited in the diagonal proof applies verbatim to every linear coordinate transformation G. It identifies bundle morphisms with constant strict chain maps. Sending such a chain map to its initial pair is injective: M=0 induces zero on degree-zero cohomology. Therefore the initial classification is necessary for every bundle morphism, and bounds its dimension by one. Section 5 supplies a full chain isomorphism at every classified G, proving the stated Hom and bundle assertions.

Modulo common scalar, the diagonal subgroup is μ_5². Affine permutation matrices normalize it. In the convention used here the explicit conjugation formula is

    P_π D_s P_π^{-1}=diag(s_{π(i)}).

For π(i)=ai+b and s_i=c α^i β^{i²}, discard the common scalar c α^b β^{b²}. The remaining diagonal parameters become

    (α,β) ↦ (α^a β^{2ab}, β^{a²}).                 (7)

The diagonal and permutation subgroups intersect trivially projectively, and every classified monomial transformation is their product. This proves the semidirect-product description and the count 25·20=500 over an algebraically closed field. Over a general characteristic-zero field the k-rational diagonal parameters are the k-rational fifth roots; all 20 permutation matrices are rational.

Convention warning: P_π P_σ=P_{σ∘π} with this row-index convention. Accordingly the permutation subgroup is the opposite-labelled copy of AGL(1,5), canonically isomorphic to AGL(1,5) by π↦π^{-1}. Formula (7), expressed by actual matrix conjugation, fixes the action unambiguously.

## 7. Canonical projective coherence, without a linearization claim

For each projective monomial stabilizer element g, Section 6 gives a one-dimensional space of isomorphisms H→g*H. Therefore the induced isomorphism P(H)→g*P(H) is independent of the chosen nonzero map. For two such elements, the composite of a chosen map with the appropriate pullback of the other is again an isomorphism to the composite pullback. Its Hom space is one-dimensional, so it differs from any chosen map for that composite by a nonzero scalar. Projectivization removes that scalar. Identity and associativity follow in the same way.

Thus P(H) carries a canonical coherent action of the finite monomial stabilizer covering its action on P⁴. Equivalently, the canonical projective pullback identifications satisfy the cocycle condition. With the convention φ_g:H→g*H, the composite is g*φ_h composed with φ_g and has target (h∘g)*H; this fixes the pullback-order convention. Scalar representatives G and λG define the same base automorphism g; the Hom spaces here are interpreted intrinsically as Hom(H,g*H). Hence the projectivized identification is independent of a chosen matrix representative. Over a nonclosed field the geometric projective maps descend from a separable closure, because uniqueness makes them Galois-compatible. No assertion is made that selected linear bundle isomorphisms or four-term chain lifts obey a strict group law; their scalar cocycle need not have been trivialized.

## 8. A 500-fold finite ambiguity for independent generating tuples

Let W be a fixed finite-dimensional k-subspace of H⁰(T,L), for a fixed line bundle L on a scheme T. Ordered linearly independent five-tuples (f_0,...,f_4) generating a line bundle determine maps f:T→P⁴, and are considered modulo common scalar. The classified projective monomial group acts freely on these tuples: if Gf=λf, linear independence of the five sections forces G=λI coefficient by coefficient, hence the projective group element is the identity.

Every tuple in the orbit has isomorphic pullback bundle, since (G∘f)*H is isomorphic to f*H. Over an algebraically closed characteristic-zero field each orbit has 500 distinct projective coefficient presentations. On any invariant open subscheme of the projective coefficient parameter space where the independent generating hypotheses hold, the quotient morphism by this free finite étale group action is finite étale of degree 500. The invariant open is quasi-projective, so its quotient exists as a scheme; geometric freeness gives scheme-theoretic freeness because the group is finite étale. Over a nonclosed field this statement uses the full finite étale group scheme, not merely its k-rational subgroup, whose rational-point orbits can be smaller. For dim W=16 this concerns the appropriate invariant locus in P(W^5)=P^79.

This enlarges the previously established 25-fold diagonal ambiguity. It does not assert that these are all identifications between coefficient presentations, nor does it contradict local versality. No lift of G to an automorphism of T is needed: the operation changes the target-coordinate presentation of f.

The bundle symmetries and their canonical projective coherence do not prove covariance of chosen source-level star lifts, HPL selectors, or retained obstruction scalars. They do not supply an automorphism lift on any elliptic carrier.


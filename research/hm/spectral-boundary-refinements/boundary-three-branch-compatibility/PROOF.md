# Full-Artin compatibility of three boundary branches

## Statement

Retain the tensor, determinantal schemes B and D, and hypotheses of `../boundary-relative-rigidity/PROOF.md`. Fix a complex polar point p with exactly three boundary rectangles. Put A=O_{D,p}, assumed local Artin as in that proof, with maximal ideal m and residue field C. Write the three local boundary branches as Spec(A/I_1), Spec(A/I_2), Spec(A/I_3), labeled by their distinct closed rectangles.

There are ideals J_12,J_13,J_23 of A, constructed from the relative vector-valued quadratic form, such that

    I_1=J_12+J_13,   I_2=J_12+J_23,   I_3=J_13+J_23.

In particular, putting Q=J_12+J_13+J_23, one has

    I_1+I_2=I_1+I_3=I_2+I_3=I_1+I_2+I_3=Q.

For every local Artin A-algebra R (with the specified closed polar point), a lift on branch i exists precisely when I_i maps to zero in R, and is then unique. Any two distinct closed branches lift over R if and only if all three lift, precisely when Q maps to zero. Thus a polar deformation over a fixed local Artin test ring has zero, one, or three boundary lifts. This is a full-Artin assertion, not just a tangent-space statement.

Neither individual branch flatness nor lifting over all of Spec A is asserted. All three lift over A itself exactly when Q=0. The proof below also records exact scheme-length and function-gluing statements.

## 1. Relative polar data over all of A

Trivialize the two tautological polar lines on Spec A, choosing primitive vectors h,u in V_A=V⊗_C A, and let P=f(h,u,-):V_A→J_A. Write w=P(h).

At p the two vectors P(h) and P(u) are independent, by the two-polar-value independence already used in the predecessor proof. A corresponding 2×2 minor is therefore a unit in A. All 3×3 minors vanish by the defining equations of D. Elementary invertible matrix operations consequently put P in the form diag(I_2,0), with the appropriate rectangular zero blocks. Its image M is a free rank-two direct summand of J_A, and its kernel is free of rank three. These conclusions hold over A itself, including its nilpotents.

The vectors w and P(u) form a basis of M, because their reductions do. In particular L=Aw is a direct summand of both M and J_A. Set

    H=P^{-1}(L),   E=H/Ah,   K=J_A/L.

The composite V_A→M/L is surjective and takes u to a basis, so H is a rank-four direct summand and V_A=H⊕Au. The vector h is primitive in V_A and lies in H, hence Ah is a direct summand of H. Thus E is free of rank three and K is free. Outer symmetry and P(H)⊂L imply that f(-,u,-) induces an A-bilinear symmetric map

    β:E×E→K.

All these constructions commute with arbitrary base change. Changing the chosen generators of the polar lines only changes the indicated trivializations, not the boundary moduli problem.

At the closed point, β_0(v,v) is nonzero for every nonzero v∈E_0, by the fixed-polar argument in `../boundary-rectangle-choice-bound/PROOF.md`, Section 1. Its scalar linear system has a nondegenerate member q_0. Lift the corresponding functional on K_0 to λ_0∈Hom_A(K,A) and put q=λ_0β. Its determinant is a unit because its reduction is nonzero, so q is a perfect symmetric form over A. For λ∈K^*=Hom_A(K,A), define the q-selfadjoint operator T_λ by

    q(T_λv,z)=λβ(v,z).

A basis of K^* suffices to impose every common-eigenline equation.

Only the closed-fiber nonvanishing assertion about β_0 is needed. No claim that β(v,v) is nonzero for every nonzero element of every nonreduced test module is used or needed; such a claim would fail for many nilpotent vectors. The actual uses are invertibility of scalars whose residues are nonzero.

## 2. Relative boundary functor and common eigenlines

The entire base change B_A=B×_D Spec A represents splittings

    E_R=a⊕C,  rank(a)=1, rank(C)=2,  β_R(a,C)=0

on A-schemes, locally on their bases. Indeed the boundary intersection is the pullback Ah, its rectangular image line is the pullback L, and its rank-four sum H_B is contained in H_R. The containment is an isomorphism by the fiberwise rank test, exactly as in Sections 1–3 of the predecessor proof. Quotienting X,Y by Ah gives a,C. Conversely their inverse images in H_R yield X,Y, whose rectangular map factors through L_R and contains its generator w, so the boundary and rectangular determinantal equations hold identically.

For every such splitting, C=a^⊥ and q|a is invertible. Conversely, a q-nonisotropic common eigenline of all T_λ has complement a^⊥ and gives a splitting. This is equivalence of equations over rings: the restriction λβ(a,a^⊥) is q(T_λa,a^⊥), and the perfect form on a^⊥ identifies these functionals with the components of T_λa modulo a.

Every common eigenline in the closed fiber is q_0-nonisotropic. If q_0(v,v)=0 and T_{λ,0}v=μ_λv, then λβ_0(v,v)=0 for all λ, contrary to β_0(v,v)≠0. Thus the entire relative common-eigenline scheme lies in the nonisotropic open: its complement has empty closed fiber and hence empty support, since Spec A has one point and its nilpotent ideal does not change topological support. Consequently B_A is exactly this common-eigenline scheme, not merely an open part containing the known points.

## 3. Functorial two-imply-three argument

Let R be local Artin over A and suppose two distinct closed branches lift, with common eigenlines a_1,a_2. Choose generators v_i. Write T_λv_i=μ_{i,λ}v_i.

The two closed joint eigenvalue tuples are distinct. Otherwise their two-dimensional span consists of common eigenvectors with the same tuple, and a nonzero q_0-isotropic vector on that span has β_0(v,v)=0, a contradiction. Choose λ for which the two closed eigenvalues differ. Then μ_{1,λ}−μ_{2,λ} is a unit of R. Selfadjointness gives

    (μ_{1,λ}−μ_{2,λ})q(v_1,v_2)=0,

hence q(a_1,a_2)=0 exactly. Each q(v_i,v_i) is a unit by its closed-fiber value. Their sum is therefore a nondegenerate rank-two direct summand. Its orthogonal complement a_3 is a nondegenerate rank-one direct summand. Every T_λ preserves a_1+a_2, and selfadjointness implies that it preserves a_3. Thus a_3 is a common eigenline and produces a boundary lift reducing to the third closed rectangle.

The construction uses direct summands, perfect forms, and unit inversions, hence commutes with base change. There is no division by a nilpotent.

Apply this with R=A/(I_1+I_2), on which the first two branches have their universal lifts. The produced third lift lies on the third local component, so its A-algebra map A/I_3→R implies I_3⊂I_1+I_2. Cyclically the same holds for the other pairs. These three inclusions imply equality of all pairwise sums with I_1+I_2+I_3.

Uniqueness follows either from the already proved closed-immersion description Spec(A/I_i), or from formal unramifiedness: two maps from Spec R over Spec A agreeing at the closed point agree successively across nilpotent thickenings. Unramifiedness is used for uniqueness, not to assert existence or flatness.

## 4. Stronger spectral-coordinate presentation

The three closed common eigenlines are pairwise orthogonal. Their closed joint eigenvalue tuples are pairwise distinct. Since C is infinite, a generic scalar member T=T_λ has three distinct eigenvalues ρ_{1,0},ρ_{2,0},ρ_{3,0} on these lines: avoid the finitely many hyperplanes on which a pair agrees.

Lift λ to K^*. The characteristic polynomial of T has three uniquely lifted roots ρ_i∈A with the specified residues. For completeness this is simple-root lifting across the powers of m: the derivative is a unit at each residue root, so Newton correction solves at each square-zero step; nilpotence terminates the process, and the same unit gives uniqueness. The monic characteristic polynomial is ∏_i(t−ρ_i), and each ρ_i−ρ_j is a unit.

The polynomial operators

    e_i=∏_{j≠i}(T−ρ_j id)/(ρ_i−ρ_j)

are mutually orthogonal idempotents with sum id, by polynomial interpolation and Cayley–Hamilton. Put L_i=e_iE. Each is a rank-one direct summand, because its closed reduction has rank one. Thus E=L_1⊕L_2⊕L_3. Selfadjointness of T and the unit eigenvalue differences show q(L_i,L_j)=0 for i≠j; q|L_i is perfect.

Any T-invariant line reducing to L_i must equal L_i, scheme-theoretically. To see this locally on any test base on the corresponding chart, write its generator v=v_1+v_2+v_3, with v_i a basis of (L_i)_R, and Tv=μv. Its i-th component gives μ=ρ_i; its other components give (ρ_j−ρ_i)v_j=0 and hence v_j=0. These charts cover the eigenscheme, because after reduction its only eigenlines are the three indicated lines. Thus the T-eigenline scheme is the disjoint union of three copies of Spec A.

Choose bases s_i of L_i and define J_ij as the ideal generated by all coordinates of β(s_i,s_j) in a basis of K. This ideal is independent of those bases: changing s_i,s_j multiplies by units, and changing the basis of K gives an invertible linear transformation of coordinates. Symmetry gives J_ij=J_ji.

The line L_i is a common eigenline of the whole family precisely when

    β(L_i,L_j)=0 for both j≠i.

Indeed L_i^⊥ is the sum of the other two eigenbundles, and Section 2 identifies these equations exactly. Therefore the branch inside its copy of Spec A is defined by J_ij+J_ik. Comparing with its intrinsic quotient presentation gives

    I_i=J_ij+J_ik.

These J_ij depend on the chosen separating scalar member, while the I_i and Q are intrinsic. This proves the stronger statement without any approximation or first-order truncation.

## 5. Exact lifting criteria and tangent-space qualification

For a polar deformation φ:A→R into a local Artin C-algebra, the set of lifts reducing to branch i is a singleton if φ(I_i)=0 and empty otherwise. Thus

    all three lift ⇔ any specified pair lifts ⇔ φ(Q)=0.

The simultaneous-lifting locus is exactly Spec(A/Q). The same criterion applies to a quotient A/H: all three lift exactly when Q⊂H. A statement that all three closed rectangles exist at p says only I_i⊂m; it does not say I_i=0.

For first-order deformations φ:A→C[ε]/(ε²), a tangent vector ξ lifts to branch i exactly when ξ annihilates the image of I_i in m/m². The three pairwise intersections of these tangent-lifting subspaces coincide with the subspace annihilating Q modulo m². These tangent conditions are only the first-order shadows of the displayed ideal criteria. For example, Q⊂m² makes every first-order deformation simultaneously lift but does not imply Q=0 or simultaneous lifting over A. This last observation is an algebraic logical distinction, not a claim that every ideal pattern is realized by an original tensor f.

### Explicit first-order obstruction maps

In the spectral bases of Section 4 put c_ij=β(s_i,s_j)∈mK for i≠j. Its linear term defines a C-linear map

    κ_ij:T_pD=Hom_C(m/m²,C) → K_0,
    κ_ij(ξ)=(id_K0⊗ξ)(c_ij mod m²K).

Changing either eigenvector basis scales κ_ij by the product of the corresponding nonzero residue units; changing a trivialization of K induces its natural invertible residue change. Thus its kernel is intrinsic to this presentation. The unramified map identifies each branch tangent space with a subspace of T_pD, and the ideal formula gives

    T_{b_i}B = ker κ_ij ∩ ker κ_ik.

In particular, all three pairwise intersections of the branch tangent images equal

    ker κ_12 ∩ ker κ_13 ∩ ker κ_23.

There is also a verified restriction on the obstruction targets. If λ_0 defines q and λ_1 defines the separating operator T, then λ_0(c_ij)=q(s_i,s_j)=0 and λ_1(c_ij)=q(Ts_i,s_j)=0 identically over A. Since c_ij reduces to zero, taking first derivatives gives

    im κ_ij ⊂ ker(λ_{0,0}:K_0→C) ∩ ker(λ_{1,0}:K_0→C).

The two residue functionals are independent: proportionality would make T_0 a scalar operator, contradicting its three distinct eigenvalues. This is a common codimension-two target subspace. No unobstructedness or passage from first-order vanishing to full-Artin lifting is inferred.

## 6. Lengths and the distinction from gluing functions

Write ℓ for complex vector-space length, N=I_1∩I_2∩I_3, and

    F=(A/I_1) ×_{A/Q} (A/I_2) ×_{A/Q} (A/I_3).

Then F is the ring of triples of branch functions whose images on the common pairwise overlap agree. There is an exact sequence of A-modules

    0 → F → ⊕_{i=1}^3 A/I_i → (A/Q)^2 → 0,

where the final map sends (x_1,x_2,x_3) to (x_1−x_2,x_1−x_3), modulo Q. It is surjective. Consequently

    ℓ(B_A)=Σ_i ℓ(A/I_i)=ℓ(F)+2ℓ(A/Q).

The diagonal map A/N→F is injective. To prove its surjectivity, one must use the stronger cross-ideal presentation, not just equality of pairwise sums. For general ideals having equal pairwise sums, its exact defect is

    Δ=Q/((I_1∩I_2)+I_3),

and there is a short exact sequence

    0 → A/N → F → Δ → 0.

To define the last arrow, lift a compatible pair (x_1,x_2) to a∈A, which is possible since I_1+I_2=Q, lift x_3 to c∈A, and take a−c modulo (I_1∩I_2)+I_3. Compatibility ensures a−c∈Q; choices change it by the stated denominator. Surjectivity follows by using (d mod I_1,d mod I_2,0) for d∈Q. The kernel is exactly the diagonal image. This also proves that the apparently asymmetric description of Δ yields the same intrinsic cokernel after relabeling.

In the present geometry the stronger presentation makes this defect vanish: J_12⊂I_1∩I_2 and I_3=J_13+J_23, so

    Q=J_12+J_13+J_23 ⊂ (I_1∩I_2)+I_3 ⊂ Q.

Hence Δ=0 and the diagonal map is a ring isomorphism

    A/N ≅ (A/I_1) ×_{A/Q} (A/I_2) ×_{A/Q} (A/I_3).

Thus functions on the three branch images glue exactly when they agree on their common pairwise overlap, and the refined length identity is

    ℓ(B_A)=ℓ(A/N)+2ℓ(A/Q).

Here Spec(A/N) is the scheme-theoretic union of the three branch images inside Spec A; B_A itself is their disjoint union, and the two schemes must not be confused.

Also, directly,

    ℓ(B_A)=3ℓ(A)−Σ_iℓ(I_i),
    ℓ(B_A)=3ℓ(A)−2ℓ(Q)−ℓ(N),
    3ℓ(A/Q) ≤ ℓ(B_A) ≤ ℓ(A)+2ℓ(A/Q) ≤ 3ℓ(A).

Equality in the middle upper bound holds exactly when N=0. Equality with 3ℓ(A) holds exactly when all I_i vanish, equivalently Q=0. In particular Q≠0 implies ℓ(B_A)≤3ℓ(A)−2ℓ(Q)≤3ℓ(A)−2. These are statements about the finite local algebra; none asserts flatness of a proper branch.

As a warning about the weaker algebraic inference alone, in A=C[x,y]/(x,y)^2 the ideals (x),(y),(x+y) have equal pairwise sums m, but Δ=m/(x+y) is nonzero. This is only an example showing that the pairwise-sum identities by themselves do not imply function gluing; it is not asserted to arise from the original tensor or the stronger J_ij presentation.

## Scope

This is a bounded extension of the previously established boundary rigidity theorem. It constructs the relative data on the full local polar scheme, proves exact full-Artin compatibility, and distinguishes lift existence, uniqueness, first-order criteria, and lengths. It does not prove individual flatness, equality of branch ideals or lengths, reduction of D or B, or that all three closed branches lift to the entire polar algebra.

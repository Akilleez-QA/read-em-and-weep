# Matching the midpoint Hessian symbol through all Serre frames

## Claim, dependencies, and limit

Using the actual homogeneous vertex Serre frames normalized to the full block-torus residue character, the local Hessian square-zero lifts can be corrected by the unique invariant primitive of their quintic-generator residue. The resulting system represents the ACTUAL midpoint first-normal nilpotent symbol modulo local normal conjugation on the vertex neighborhood.

This uses the invariant acyclicity H0(M(-2))^G=H1(M(-2))^G=0, and the determinant-one stabilizer theorem, in addition to the previously computed quintic covariance. It does not mean the uncorrected Hessian formula is the actual lift. Nor does it evaluate the resulting twist-four operator defect or the third Bockstein.

The precise actual inputs are the homogeneous ideal and full residue normalization from the Serre-double-cover and actual rank-nine Atiyah proofs; the regular-section Serre presentation; the unique midpoint nilpotent lift; and FIRST-NORMAL-ADJOINT-DEFECT-IS-INVARIANT-ACYCLIC.md. No coefficient specialization is made.

## 1. Keep the unit relating the actual equation to the A1 equation

In a chosen physical O(2) frame write

    q0=nu q,   q=xz-y²,

where nu is a unit on the vertex chart. Let N0 and T_H be the Euler-Gram and Hessian matrices from UNIVERSAL-HESSIAN-CORRECTION-FOR-FIRST-NORMAL-NILPOTENCE.md. In forming N0, choose the CANONICAL HARMONIC lifts of every even Euler-gradient entry: the cubic gradients have degree2 and the quintic gradients have degree4. This is the convention giving the triangular residue coefficient -1/16, not the compatible-transport coefficient -1/144. It is distinct from lifting the whole matrix n harmonically, which requires the later splitting conversion. Arbitrary even lifts allowed in the original existence identity are not used here. Thus

    N_H=N0+q T_H=N0+q0 (T_H/nu).                    (1)

The first-normal correction relative to the ACTUAL equation is T_H/nu. Suppressing this unit during changes of determinant frame would give a wrong covariance law.

Let P=diag(alpha,beta), d=alpha beta, and change positive cover coordinates by u'=R u. Use the transformed polynomials f'(u')=alpha f(R^-1 u'), g'(u')=beta g(R^-1 u'). Euler gradients transform by R^-t, and C'=R C R^t. Directly,

    N0'=d P N0 P^-1,
    T_H'=d (det R)^-2 P T_H P^-1.                  (2)

The second identity follows because both Hessian determinants and their mixed contraction acquire (det R)^-2 under the inverse coordinate substitution. Composition with R^-1 is understood in (2).

The determinant identification detG=O(2) means that the physical components of q0 change by d in the SAME component convention as the twisted nilpotent N. Meanwhile q'= (det R)^2 q. Consequently

    q0'=d q0,   nu'=d (det R)^-2 nu,
    T_H'/nu'=P(T_H/nu)P^-1.                         (3)

Thus diagonal generator normalization, the determinant line, the ambient equation, and GL2 coordinate changes agree exactly. Equations (2)-(3) do not require determinant-one coordinate changes.

A scalar frame factor acts trivially by adjoint conjugation. In passing between G and the spinor-twisted F_Q, the matrix transitions differ by precisely such scalar factors; the physical O(2) and q0 factors remain those in (3). This is an adjoint comparison on the cone. It neither extends the spinor line to 2Q nor assumes a flat kernel for the lifted nilpotent. Any choice of first-normal matrix lift of a fixed cone adjoint transition changes the residue only by a commutator.

## 2. The only remaining generator residue

The actual ideal is homogeneous with minimal generator degrees3 and5. In homogeneous normalized frames its transition is a composition of diagonal changes and

    f'=f,  g'=g+p f,  deg(p)=2.

There is no reverse degree-negative term. Normalizing to the ACTUAL Serre residue is permitted by its FULL block-torus character; it is not inferred merely from the order-four sign. This is the normalization already established in ACTUAL-POSITIVE-ATIYAH-MULTIPLICATION-SURJECTS-ONTO-NINE-SPACE.md.

There is an exact determinant-compatibility step here. Choose physical determinant frames pulled back from the base line. Their transitions d are base units. The ratio of the actual Serre residue to the residue of a homogeneous regular pair has full block-torus weight zero, hence is a base unit: every nonconstant nilpotent in the homogeneous vertex algebra has strictly positive cover degree. Rescale one generator by that base unit to make the residues agree on the ENTIRE nonreduced Z, not only its support.

An actual local Serre frame carrying this pair can then be made exactly oriented. Indeed, if its determinant differs from the prescribed physical determinant frame by a unit congruent to1 modulo I, write that unit as 1+a f+b g. The matrix

    S=I+[[b g,-b f],[-a g,a f]]

fixes sigma and has determinant 1+a f+b g. Multiplying by S or its inverse corrects the determinant without changing the pair. This is a choice of initial oriented frames, not an invocation of the determinant-one stabilizer theorem for S.

Now compare the actual transition in these oriented frames with the convenient homogeneous triangular transition P0. Their determinants are BOTH base units: the first is the physical transition d, the second is the product of the homogeneous diagonal generator scalings. Agreement of the Serre residues says these determinant units agree modulo I. But I intersects the base ring in zero, since the homogeneous vertex ideal has strictly positive cover degree. Therefore their determinants agree EXACTLY. Their quotient fixes sigma and has determinant one, so the stabilizer theorem genuinely applies. A possible determinant1+I discrepancy has been removed by this argument, not discarded.

For the elementary triangular change, the previously verified covariance is

    N_H' - P N_H P^-1
      =-q0 [mix(H_f,H_p)/(16 nu)] S1' mod q0²,
    S1'=[[f,0],[2g',-f]].                            (4)

For compatibility with Section1, under diagonal normalization and the inverse coordinate substitution one has p'= (beta/alpha) p, mix'=beta (det R)^-2 mix, and S1'=alpha P S1 P^-1. Together with nu'=alpha beta (det R)^-2 nu, the normalized residual in (4) therefore conjugates exactly.

Its right side is tangent. A different determinant-compatible frame realizing this same pair transition differs by P_stab=I+tN. REGULAR-SERRE-STABILIZERS-HAVE-ZERO-NORMAL-DEFECT-RESIDUE.md shows that its entire residue in M(-2) is zero, not merely its leading term. This accounts for the otherwise missing Koszul stabilizers.

## 3. Check the coefficient line, including the normal factor

On the root gerbe of the negative line, S(2) has square O_L(5). The cubic minimal relation line and the quintic quotient line in the ordinary ideal are therefore

    I3=K3 tensor S(2)^-1=O_L(-9/2),
    I5=O_L(5) tensor S(2)^-1=O_L(5/2).

Their product is O_L(-2)=detG*, as required. The second G(-2) frame line is O_L(-9/2). Multiplying by a cover-linear function, whose coefficient line is Wprime O_L(-1/2), gives

    Wprime O_L(-5).                                (5)

With tau(v)=sigma v^t J+v sigma^t J, S1=tau(e2). Thus (5) is exactly the line of the coefficient multiplying S1 in an ACTUAL first-normal correction. This verifies that division by nu in (4) has not omitted a determinant or normal factor.

The residual is the intrinsic version of the already computed map from the quintic-transition cocycle V O_L(-8) to Wprime O_L(-5). Its invariant H1 is zero, because Wprime tensor H1(O_L(-5))=Wprime tensor S4 has no invariant; H0 is zero as well. Hence there is a unique invariant cochain primitive for this residue. Add the corresponding q0 u_i S1_i corrections to (1). They preserve square-zero to first normal order.

## 4. Comparison with the actual midpoint

Use local frames of the ACTUAL midpoint bundle, reducing to the cone frames just normalized. Interpret the corrected local Hessian matrices in those frames. On overlaps their discrepancies, divided by q0, have zero image in M(-2): Sections1-3 account for the diagonal, coordinate, triangular, and stabilizer parts, and arbitrary normal lifts of the transitions contribute commutators only.

Subtract the actual global N_tilde. Because both systems lift N and square to zero modulo q0², their differences are tangent. Their classes in M(-2) glue on the vertex neighborhood and are invariant. The support of M is the ordinary square thickening of Z, whose conic and vertex components are disjoint. Extend the comparison class by zero on the conic component. It is a global invariant section of M(-2), hence zero by the established acyclicity theorem.

Therefore every corrected local Hessian matrix differs from the ACTUAL midpoint nilpotent by a normal commutator. An identity-mod-q0 local conjugation removes that difference. This proves the claimed matching of the symbol, not an isomorphism of a separately guessed ambient bundle.

## 5. What this licenses in the operator formula

The corrected Hessian symbol, including its unique primitive u_i, can now replace the actual t in the universal diagonal operator formula AFTER converting the Euler-Gram splitting to the harmonic splitting used there. A simultaneous local conjugation changes the operator's normal connection term K, but that term disappears from the diagonal residue modulo (f²,g²), as explicitly proved in UNIVERSAL-FIRST-NORMAL-HARMONIC-PRODUCT-AND-OPERATOR-RESIDUE.md.

The primitive, the splitting conversion, the corrected cone connection A, and the scalar lift must still be retained. Evaluating the resulting global degree-eight residue modulo H0(G(4)), and then modulo the second-symbol image, remains unresolved.

## Reproduction

The companion verifier checks the diagonal-generator covariance, inverse-GL2 Hessian determinant scaling at the abstract symmetric-matrix level, and the equation-unit cancellation. The previous universal quintic and stabilizer verifiers supply the non-diagonal calculations. The global conclusion additionally uses the explicitly listed geometric inputs, not a numerical test.

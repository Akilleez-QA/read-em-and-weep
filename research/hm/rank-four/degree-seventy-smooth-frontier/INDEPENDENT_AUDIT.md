# Independent audit: the degree-70 smooth frontier

## Scope and initial verdict

The integrality, general-curve smoothness, free A-action, and genus reduction to 326 or 351 pass independent verification, conditional on the previously audited normalizer genus bound, quintic-surface exclusion and sectional lifting lemma, and degree-65 pencil lemma. The detailed final Rao conclusions will be checked against the author's completed proof below.

This audit uses only the existing local proof corpus and universal group/curve arguments. No actual operation, source tensor, coefficient instance, selected source input, or source rank instance was evaluated. No actual source-instance evaluation is claimed.

## Integrality and section bounds

At degree 70, the component argument from the degree-65 proof still works. An A-orbit of 25 components costs at least 75 degrees, and an orbit of five forces all six stabilizer axes and costs at least 90. Thus each component is A-stable. A nontrivial quotient-group orbit has at least five members; its component degree is divisible by five and at most 14, hence five or ten. The imported small-component estimate forces at least twenty such members, costing at least 100. Every component is therefore individually normalizer-stable. Even the earlier degree-at-least-60 bound suffices to rule out two components. The curve is integral and nondegenerate.

For the normalization X and L=nu*O_C(1), faithful normalizer action gives g(X)>=326. Ten sections of L would give a birational degree-70 model in P9, with Castelnuovo bound pi(70,9)=264, so h0(L)=5 and M1=0. The prior no-cubics proof applies because 70>27 and the invariant quintic-surface exclusion is unchanged. Thus I_C(2)=I_C(3)=0 and a general section has h(1)=4,h(2)=10.

Uniform-position growth gives

    4,10,13,19,22,28,31,37,40,46,49,55,58,64,67,70.

The deficits from 70 sum to

    66+60+57+51+48+42+39+33+30+24+21+15+12+6+3=507.

The general non-ACM sectional genus bound consequently gives p_a(C)<=507 and delta=p_a(C)-g(X)<=181.

## Independent point-orbit audit

I read normalizer-minimal-point-orbit/PROOF.md and normalizer-refined-point-gap/PROOF.md in full. The canonical 30-point orbit E is exactly the locus with nontrivial A-stabilizer. The six order-five subgroups of A each have five simple Schrödinger eigenlines; their sets are disjoint and together form one orbit. Outside E, A acts freely.

The refined lower bound 250 for other point orbits is valid. Outside E an orbit has size 25k, and its stabilizer projects to a subgroup of SL2(F5) of index k. Perfection excludes indices two through four; index one is excluded by the fixed-point-free complement argument. At index five, the binary tetrahedral subgroup has no invariant line in the five-dimensional representation. At index six, the order-twenty Borel fixes only a canonical eigenline. Indices seven and nine do not divide 120; index eight would require an order-fifteen subgroup lying inside an order-twenty Sylow-five normalizer, impossible. Thus k>=10.

The singular support is invariant, and each singular point contributes at least one to delta. Since delta<=181<250, any singular point must lie on E and the entire E must then be singular.

## Maximal cyclic stabilizers and the branch bound

Every element of the projective semidirect product N=A semidirect SL2(F5) has order at most ten. Here is an exhaustive verification.

- A pure translation has order one or five.
- If the quotient element g has no eigenvalue one on A, I-g is invertible, so a translation conjugates (a,g) to (0,g). Its order is among two, three, four, six, ten.
- Every remaining nonidentity quotient element is unipotent g=I+J with J^2=0. In characteristic five, g^i=I+iJ and sum from i=0 to 4 of g^i=5I+10J=0. Hence (a,g)^5=1, and its quotient has order five, so its order is five.

On the smooth normalization, a point stabilizer is cyclic: its derivative is a faithful homomorphism into C*. The kernel is trivial since a finite-order complex curve automorphism tangent to the identity is the identity; faithfulness of the whole N-action was already established. Every normalization-point stabilizer therefore has order at most ten.

For p in E, N_p has order 3000/30=100. It acts on the finite normalization fibre over p. The stabilizer of any point in this fibre has order at most ten, so each fibre orbit has at least ten points. Thus the number r_p of analytic branches is at least ten. For an integral complex curve, delta_p>=r_p-1, by the independent residue values on the normalization branches modulo the common residue value on the original curve. Therefore delta_p>=9. Equivariance would give total delta>=30*9=270, contradicting delta<=181.

Thus C is smooth. Moreover it cannot meet E even at a smooth point: an order-100 stabilizer cannot be cyclic of order at most ten. Since E is exactly the nonfree A locus, the A-action on C is free. This argument applies to every invariant reduced degree-70 curve without line or conic components; it does not require the actual rank-four curve's separate eigenpoint-rank-six hypothesis.

## Genus reduction

The quotient C/A is smooth and the covering is etale of degree 25. Hence g(C)-1=25(g(C/A)-1), so g(C) is congruent to one modulo 25. Initially the possible genera between 326 and 507 are 326,351,376,401,426,451,476,501.

If g>=376, then pi(140,24)=351 forces h0(L^2)<=20 and pi(210,49)=356 forces h0(L^3)<=45, using the Heisenberg five-divisibility. Thus dim M2 is zero or five and dim M3 is at most ten.

If a general linear multiplication M2 to M3 is injective, h(section,3)=20. Uniform position gives

    4,10,20,23,29,39,42,48,58,61,67,70,

whose deficits sum to 369. This contradicts g>=376. Therefore M2 has dimension five and generic multiplication is noninjective. The audited degree-65 abstract pencil lemma says any nonzero eligible map into an M3 of dimension at most ten is generically injective. Hence multiplication is zero. The same audited quintic extraction/lifting argument then produces a forbidden invariant integral quintic surface (all degree thresholds remain valid at 70).

Consequently g is 326 or 351. The corresponding quotient genera are respectively 14 and 15, since g(C/A)=1+(g(C)-1)/25.

## Final proof review: at least five sectional cubics

I read the completed degree-seventy-smooth-frontier/PROOF.md in full, including its Sections 4 and 6, and reread quadratic-deficiency-exclusion/INDEPENDENT_GEOMETRY_AUDIT.md. The extension from exactly five to at least five sectional cubics is valid.

The cubic system here is the full intrinsic system, so it varies canonically and the component-monodromy argument applies unchanged. Five-dimensionality was used only as a lower bound in the earlier geometric argument. A common quadratic leaves at most four independent cubics and a common cubic leaves at most one. A common linear factor leaves quadrics vanishing at at least 67 points, because linear general position allows at most three section points in a plane. Uniform position with quadratic Hilbert function ten rules that out. Two general cubics therefore give a degree-nine complete intersection; a further cubic avoiding its non-base components bounds isolated base points by 27. The joint monodromy kernel argument still uses at most nine component labels and S70 on section points, forcing one integral component to contain all 70 points.

The remaining argument also uses only a lower bound of five cubics: if the integral component D had degree greater than five, the quoted Laudal consequence makes its general plane section have quadratic Hilbert function six. Its cubic Hilbert function is at least six, leaving at most four plane cubics. Restriction of cubics through D to that plane is injective because D has no quadric, contradicting at least five independent cubics. Degree at most four forces a quadric by the normalization section bound; hence D has degree five. The uniqueness, descent, flat-family, lifting and invariant-surface steps are exactly those checked in the cited geometry audit, with all numerical thresholds satisfied.

Thus k=dim ker(M2 --ell--> M3)<=4. The resulting h(section,3)>=16 sequence printed in the final proof has deficit sum 456, as asserted.

## Final proof review: the two quadratic multiplicity cases

The universal bounds pi(140,29)=276 and pi(210,54)=309 give dim M2<=10 and dim M3<=15. Write M2=U2 tensor E and M3=U3 tensor F with dim E<=2 and dim F<=3. These multiplicity representations are ordinary G-representations because the chosen five-dimensional Heisenberg modules extend to the linear normalizer; uniqueness of the extension follows from perfection of G.

If dim E=1, E is trivial. The map from T* direct-sum W'* to F can have only one of these two irreducible image types, since their combined dimension is five. An additional trivial target summand when the image is W'* causes no issue. The odd projection has generically injective slices by the already audited pencil lemma. The even projection has the same property by a distinct, simpler argument: zero even projection forces zero coefficients in its fixed t=0 sector, namely x_k y_k=0 for all k. Over the rational function field in the five x coordinates these force every y_k=0. This argument uses the same index-reflection identification and positive involution sign already audited in the degree-65 proof. It requires no numerical specialization. Zero multiplication would have k=5 and is excluded by the sectional result. Hence k=0 for dim M2=5; it is also zero when M2=0.

If dim E=2 is reducible, semisimplicity and the absence of nontrivial one-dimensional characters force E=1 direct-sum 1. The source multiplicity is then two copies each of T* and W'*. A target F of dimension at most three can receive at most one copy of one type, and cannot receive both types. Schur's lemma makes the resulting map a selected irreducible projection tensored with a single functional on E. On every fixed-linear-form slice it therefore factors through U2 of dimension five. Its rank is at most five, giving k>=5 for the ten-dimensional source. This contradicts the established k<=4. Thus E must be a nontrivial irreducible two-dimensional representation. The bound k<=4 also gives generic slice rank at least six and hence dim M3>=10 by five-divisibility.

No identification of which irreducible two-dimensional E occurs is justified or claimed. Nor does an eligible representation channel alone imply a nonzero actual multiplication component. The final proof respects both limitations.

## Final verdict

PASS for the complete final proof and all stated conclusions, conditional on its explicitly imported audited geometric and representation inputs. No substantive correction was required. This is a necessary-condition theorem, not a degree-70 exclusion or an existence result. The proof applies to invariant reduced curves of total degree 70 without line/conic components, not automatically to a degree-70 component of a larger curve.

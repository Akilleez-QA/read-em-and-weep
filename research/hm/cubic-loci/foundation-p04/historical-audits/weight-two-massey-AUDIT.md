# Historical scope-limited review receipt

This review concerns the original source, possibly a larger scope than the excerpt in this unit. It is not a review of normalized publication bytes.

# Independent formal audit: weight-two ordered Massey reduction

## Scope and conclusion

The reduction is formally valid under the established hypotheses: the vector-bundle splitting of B = σ_*O_(P¹)^4 on P⁴, the stated classical cohomology of End H, and vanishing of every ordered product in K = Ext¹(E,E)^G. This audit uses no source/model, rank, polynomial-instance, point, jet, residual, or detector evaluation or execution. Shell use is restricted to reading static proof documents and writing this audit. No external service or local Codex is used.

The key safeguards are that the generation filtration is canonical but a compatible additive splitting need not be; its splitness proves strictness of cohomology without making it an algebra splitting; and a leading weight-two formula alone does not establish a nonzero geometric Massey operation.

## 1. Canonical filtration and Artin multiplication

Put F_aB = im(H⁰(B(a)) ⊗ O(−a) → B), for a ≥ 0, with F_aB = 0 for a < 0. The known splitting B ≅ O ⊕ O(−1)^11 ⊕ O(−2)^11 ⊕ O(−3) shows that F_aB is exactly the sum of summands whose generation degree is at most a, in any such splitting. Thus it is a subbundle, F_3B = B, and gr_aB ≅ V_a ⊗ O(−a) for dimensions (1,11,11,1). The definition, not the chosen splitting, makes F canonical.

Products of globally generating sections give F_aB · F_bB ⊂ F_(a+b)B. This remains true when a+b ≥ 3 by stabilization. The associated graded multiplication is therefore a genuine canonical graded algebra structure.

For R = ⊕_(n≥0) H⁰((P¹)^4,O(n,n,n,n)) and S = Sym H⁰(P⁴,O(1)), the graded algebra V = R/S_+R identifies with the coefficient algebra of gr B. Indeed V_a = H⁰(B(a))/(S_1 H⁰(B(a−1))) is the space of minimal S-module generators of degree a. This identification is intrinsic; a free S-module splitting is only a way to verify it. The Segre section ring R is generated in degree one, so its quotient V is generated in degree one. Consequently μ11: V_1 ⊗ V_1 → V_2 is surjective. This is an abstract generation argument, not a calculation on a fiber or at a point.

## 2. Cohomological strictness

Write F = End H. Every filtration sequence for F ⊗ B splits as a sequence of vector bundles, although not canonically. Therefore H^j(F ⊗ F_aB) → H^j(F ⊗ B) is injective and the filtration on cohomology has graded pieces V_a ⊗ H^j(F(−a)).

In degree one only weights zero and one occur: U_0 = H¹(F), U_1 = H¹(F(−1)), and gr K = U_0 ⊕ (V_1 ⊗ U_1). There is no canonical direct-sum decomposition of K asserted here.

Most importantly, a closed degree-two cochain in filtration a which becomes exact in the entire complex is already exact in the filtration-a subcomplex. This follows from the preceding injection, using a Čech or other multiplicative model that computes each filtered sheaf. This is the precise reason strict primitives exist; exactness in the entire DGA would not imply it for an arbitrary filtration.

## 3. Descending the ordered cup vanishings

The zero product K ⊗ K → H²(F ⊗ B) has zero associated graded product. The weight-(0,0), (0,1), and (1,0) formulas are the ordinary downstairs cup maps tensored with the unit or V_1. Their vanishing implies the corresponding downstairs ordered cups vanish.

For weight-(1,1), the formula is μ11 ⊗ cup11, with cup11: U_1 ⊗ U_1 → H²(F(−2)). Since μ11 is surjective onto the nonzero V_2, cup11 vanishes. In fact a single nonzero value of μ11 would already suffice to deduce this cup vanishing. No multiplication-compatible splitting of B has been used.

## 4. Canonical downstairs triple operation

The ordered twisted triple with weights (0,1,1) is defined using closed representatives α in F, β and γ in F(−1), and primitives h01 in cohomological degree one with twist −1 and h11 with twist −2. Its cocycle is

    α h11 + h01 γ.

The differential is zero with the sign convention d h01 = αβ and d h11 = βγ. Its indeterminacy is

    a · H¹(F(−2)) + H¹(F(−1)) · c.

The first term vanishes by the classical cohomology theorem; the second vanishes by cup11 = 0. Thus this twisted ordered Massey product is a singleton, independent of representatives and primitives, and is a canonical trilinear map U_0 ⊗ U_1 ⊗ U_1 → H²(F(−2)). Choosing linear representatives and primitives proves trilinearity; no canonical choice of those cochains is required.

## 5. Leading term of the upstairs operation

For actual input weights (0,1,1), the first pair has a primitive in filtration one and the second in filtration two by strictness. Their Massey cocycle lies in filtration two. Replacing either weight-one input by a lower-weight lift changes its canonical Massey value by a term in filtration one. Hence its image in gr_2 H²(F ⊗ B) depends only on the three graded input classes.

Passing strict primitives to associated graded gives a defining system for the graded triple. For coefficients v,w ∈ V_1, that system can be chosen as v times a downstairs h01 and μ11(v,w) times a downstairs h11. Both summands of the leading cocycle then have coefficient μ11(v,w). Accordingly the leading operation is exactly

    μ11(v,w) ⊗ M011(a,b,c),

in V_2 ⊗ H²(F(−2)), with the displayed sign convention. There is no extra permutation sign: the coefficient algebra is in cohomological degree zero. The weight is a separate filtration grading.

## 6. Limits

The argument does not calculate M011 or establish that it is nonzero. It does not give a canonical decomposition of the full target, an algebra splitting of B, or a value of the full upstairs operation beyond its weight-two graded component on these inputs. Further representation projections or pairings require their own compatibility analysis.

Sources read: [the canonical massey detector manuscript](../CANONICAL-MASSEY.md); [the quadratic yoneda exclusion manuscript](../../foundation-p01/ORDERED-PRODUCTS.md); [the projective target directions manuscript](../../foundation-p01/INVARIANT-COHOMOLOGY.md).

## 7. Exact draft review

The subsequently supplied PROOF.md has been read in full. Its assertions in Sections 1–4 pass the preceding independent checks. The same reasoning applies to all three orderings (0,1,1), (1,0,1), and (1,1,0). In the middle-weight-zero ordering, both primitive ambiguities are of twist −1 and both disappear by cup11 = 0. Thus no unaddressed indeterminacy appears there.

The leading-image span formula is valid: coefficient directions v,w and downstairs arguments vary independently; products μ11(v,w) span V_2; and downstairs values span the image of the linearized trilinear map. Here “im(m_pqr)” must mean the image of the linear map on the tensor product, equivalently the span of trilinear values, rather than their potentially non-linear set-theoretic image. With that convention the displayed equality V_2 ⊗ im(m_pqr) is exact.

The symmetry passage is also valid. Commutativity of the coefficient algebra makes the coefficient product unchanged under permutations of the two weight-one inputs, so a nonzero coefficient product allows the full reversal and cyclic identities to descend to the appropriate three downstairs orderings. Cohomological degrees remain one throughout; filtration weights do not introduce Koszul signs.

The initial Section 5 correctly left the eight-dimensional assertion conditional. The final revised Section 5 instead imports the explicit separate equivariant proof in the filtered massey target manuscript (PROOF.md) §4. I have now read that companion section, the revised Section 5, and the underlying the inversion eigenspaces manuscript (PROOF.md). The final version passes the verification below; the eight-dimensional result is no longer an unverified conditional assertion.

The final draft explicitly adopts the linear-image convention above. No mathematical correction to the canonical reduction is required. Its geometric nonvanishing and image questions remain open.


## 8. Final revised Section 5: verified equivariant input

The original inversion proof supplies the involution traces (1,3,−2,−2) on the four-term presentation coefficients and hence internal Hom traces (1,−8,−2) in positive internal degrees one, two, and three, with the same traces in negative degrees. The companion uses these same stipulated linearizations.

At twist −2, the only non-acyclic line-bundle contributions are internal degrees 2 and 3 in cohomological degree zero, and internal degree −3 in line-bundle cohomological degree four. Their total degrees are 2,3,1. The traces on H⁰(O), H⁰(O(1)), and H⁴(O(−5)) are all +1 under the specified reversal lift; the final one includes det(R)=+1. Therefore Euler additivity gives the contributions −8,+2,+2 and total trace −4. Since the downstairs twist −2 has cohomology only in degree two, this is precisely the trace on U_2. Its ordinary dimension twenty then gives an eight-dimensional positive eigenspace. The negative internal-degree endpoint is essential and has the correct odd total-degree sign.

The companion also checks that the unique [22] coefficient copy of V_2 has positive inversion action. Its V_1 partner is det²(C²), positive under coordinate interchange, and the equivariant finite-duality relation pairs the two coefficient copies without an additional inversion sign: the four determinant factors upstairs multiply to +1 and the base reversal has determinant +1. Thus the D8-trivial coefficient line does not exchange the positive and negative eigenspaces of U_2.

Only weights one and two contain [22]. The companion proves the positive retained weight-one subspace has dimension four. Consequently the projected gr_2 target is canonically the quotient of the full retained detector target by that subspace and has dimension eight. This identifies a quotient, not a preferred complement. The revised weight-two proof imports exactly this statement and does not overstate its consequences.

Final conclusion: the revised proof, including its eight-dimensional eligible quotient, passes this formal audit under its named established geometric and presentation inputs. No geometric Massey value, rank of the Massey map, nonvanishing, or separation claim has been verified or asserted.

The final added physical-duality sentence was also read and passes: for the perfect sign-valued pairing between the retained detector and physical sectors, the dual of the detector quotient is canonically the annihilator of the four-dimensional detector subspace. No identification with a selected physical direct summand is justified or claimed.

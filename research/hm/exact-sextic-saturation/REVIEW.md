# Scoped mathematical review: exact sextic saturation

Reviewed frozen `PROOF.md`, SHA256
`105812f9f0414a744c3d8b881edf4d3cd3b651ab0a59d6ee4e82a6ef0e9c1a3e`.

## Verdict

No mathematical blocker found. Conditional on the explicitly imported evaluation-resolution and quintic-saturation premises, the proof establishes

- h¹B(-1)=5 and h²B(-1)=10, with other cohomology zero;
- h⁰I_C(6)=40 and h¹I_C(6)=5;
- a unique N-equivariant complement to the 30-dimensional quintic-product subspace, irreducible of dimension ten.

This is an independent scoped mathematical review, not formal verification.

## Independently checked reasoning

1. **Normalized equivariant monad and graded symmetric square.** HM (1973), §§1–2, gives the stated N-equivariant monad after twisting by -3. Indeed Λ²T(-3)=Λ²Q*=Ω²(2), using det V=1. The two endpoint terms are in odd degrees, so their squares are exterior powers; the five displayed terms of the graded symmetric square are correct. Local splitting of the monad and exactness of taking symmetric invariants in characteristic zero justify its quasi-isomorphism to Sym²F.

2. **Bott calculation, not an imported table.** I recalculated both shifted weights. For S_(2,2)Q*, (4,5,4,1,0) is singular. For S_(2,1,1)Q*, (4,5,3,2,0) has exactly one inversion and becomes (1,1,1,1,0) after sorting and subtracting rho, yielding a five-dimensional H¹. The other indicated bundles are acyclic. As a separate check of the nonzero term, Λ²(Λ²Q*)≅End₀(Q)(-1). Tensoring 0→Q*→V*O→O(1)→0 by Q(-1), and using that Q(-1) is acyclic and H⁰Q=V, gives H¹End₀(Q)(-1)≅V and no other cohomology. Thus the hypercohomology page has precisely the two entries asserted, and its only possible differential is d₂:(0,1)→(2,0).

3. **Vanishing by symmetry.** HM pp. 64–68 states that the Galois action preserves N, gives the V_i, and establishes Λ²V≅V_1⊗W with W irreducible on N/H. Criterion (2.2) therefore proves Λ²V irreducible. Composing with the automorphism θ³ of N proves Λ²V_3 irreducible. A map from a five-dimensional module to this irreducible ten-dimensional target cannot have nonzero image. Functoriality of the symmetric construction makes d₂ equivariant. The surviving entries lie in different total degrees, so there is no extension or filtration ambiguity in either dimension or the H² edge isomorphism.

4. **Linearizations.** The proof's equivariant use of Sym²F≅B(-1) is justified, although the frozen text does not spell out the character check. N has no nontrivial characters: its quotient SL₂(F₅) is perfect, [H,H] is the center, and H/[H,H]≅F₅² has zero coinvariants under SL₂(F₅). Hence N is perfect and det F cannot differ equivariantly from O(-1) by a nontrivial character. The trace pairing makes B self-dual equivariantly. Since N⊂SL(V), equivariant Serre duality contributes no ambient determinant character. This is a short explanatory clarification, not a counterexample or unresolved gap.

5. **Saturation and deficiency.** From the imported Eagon–Northcott resolution, the stated exact sequence follows using H⁰F(-1)=H¹F(-1)=H²F(-1)=0 and H¹B(-4)=H³B(-1)*=0. The last vanishing is also obtained by the new calculation, so this step need not rely on an unverified differential elsewhere. The resulting count is 5·6+10=40. Disjointness of the 25 lines gives h⁰O_C(6)=175, and restriction from the 210-dimensional S_6 gives h¹I_C(6)=5.

6. **Unique complement.** HM Theorem 3.5 supplies U⊕U′ for the six invariant quintics. With the imported identification of these quintics with H⁰I_C(5), criterion (2.2) makes V*⊗U and V*⊗U′ irreducible of dimension 15. The quotient D⊗(Λ²C_0)* is irreducible of dimension ten, so its Hom into the product subspace vanishes. Maschke gives existence, and the zero Hom space gives uniqueness of the equivariant section. “Canonical” here means the unique complement for the fixed N-equivariant HM data, not a selected polynomial basis.

## Imported premises and limits

I inspected the local PR463 and PR458 proof texts. I import their geometric evaluation setup, Eagon–Northcott exactness, and the identification h⁰I_C(5)=6 with the six invariant minors; I do not claim a fresh audit of every upstream dependency or of their remote Git identities. The primary HM text was checked locally and against its public PDF:
https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf

The review does not establish the sextic intersection with a fixed (u,v), the original Q₄ or P₅^(2,1), source membership, pure conditions, higher lifting, or algebraicity. No selected HM/source matrix, numerical rank, generator computation, or large computation was used.

## Separate immediate corollary

Not part of the frozen proof: h¹I_C(6)=5 rules out 7-regularity, since that would require H¹I_C(7-1)=0. Monotonicity of Castelnuovo–Mumford regularity therefore gives reg(I_C)≥8. This does not prove 8-regularity or any exact regularity value.

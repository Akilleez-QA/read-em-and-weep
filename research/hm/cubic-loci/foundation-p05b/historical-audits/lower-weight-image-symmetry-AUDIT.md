# Historical scope-limited review receipt

This review concerns the original source, possibly a larger scope than the excerpt in this unit. It is not a review of normalized publication bytes.

# Independent audit: lower-weight image symmetry

Audited PROOF.md SHA-256: `75798092a075dbf41871b0571a8103964e8aa05e1892b8e2fe3f891a1e840c82`.

## Verdict

**Pass, with the explicitly imported cohomology, ordered-product, naturality, and retained-filtration hypotheses.** The proof identifies the actual twist-minus-one target as the irreducible ten-dimensional N-module V⊗W′. Each canonical lower ordering has image zero or that target, and its retained transfer has image zero or the entire canonical four-dimensional lower subspace. The eligible compatible family has eight parameters in total, split into four symmetric and four alternating two-Z-slot parameters by the additional argument in §7. No actual nonvanishing is established.

I read the complete new PROOF.md, the full-HM symmetry proof and audit, the equivariant multiplicity proof, the weight-two reduction, and the filtered-target proof. I independently checked the relevant representation facts in the original Horrocks–Mumford paper, §§1–3:
https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf
The End-cohomology row remains the stated independently established input, rather than a new claim extracted from that primary paper.

## Representation and cohomology check

For Hom(K,K(−1)), internal degree r has line degree r−1. The lowest is −4, so there is no higher-row endpoint. The only Euler contributions are internal degrees 1, 2, 3 with signs minus, plus, minus and section modules 1, V*, Sym²V*. The displayed Hom coefficients are correct. Cancelling the mixed A⊗V*⊗T⊗W terms and using Λ²V*=A*⊗W gives χ=(A*)⊗²−V⊗W⊗². Since the imported row has only H¹ and H² and H¹≅V, the target class is [(A*)⊗²]−[V⊗T].

The primary paper defines the order-four Galois operation θ and Vi*=Vi+2. Applying θ³ to the symmetric and exterior square identities gives (A*)⊗²≅V⊗(T⊕W′). Thus semisimplicity proves an actual target isomorphism J1≅V⊗W′, not merely its dimension. The Heisenberg multiplicity criterion proves irreducibility. Its central character c agrees with ordinary twist −1. Conventions must be converted together if the opposite pullback action is used.

## Canonical operations and exact retained transfer

The ordered mixed cup vanishings remove every indeterminacy term for 001, 010, and 100. Naturality consequently makes each operation equivariant and its image a submodule of J1. The zero-or-ten alternative follows.

Section 4 supplies the needed stronger statement beyond a filtration bound. Adjacent level-zero inputs admit a level-zero primitive, while each mixed adjacent pair admits a level-one primitive. Projection therefore produces v⊗m001 and its ordered analogues. Arbitrary pure coefficient symbols lift through the canonical quotient K→C1⊗U1. Changing a lift changes the full operation by a level-zero value. That value has zero [22] projection. Because the retained level-zero subspace is zero, the retained part of gr1 canonically identifies with the actual retained level-one subspace. Thus the displayed transfer is exact in that subspace, without a choice of complement or multiplicative splitting.

Varying the coefficient and downstairs arguments gives exactly L⊗e+ im(m_pqr). The coefficient line is inversion-positive, and the imported target trace −2 with dimension ten gives positive dimension four. Hence each lower retained image is zero or all four dimensions. This does not constrain lower components contributed by other input patterns.

## Eight total parameters and the separately verified slot split

The reversal and cyclic formulas are correct, and conversely define a compatible family from arbitrary F:Z⊗Z⊗V→J1. The same character-line projector argument as in the multiplicity proof identifies R=Hom_H(V,Z⊗V) with C[G/P]. Iterated evaluation gives Z⊗Z⊗V≅V⊗R⊗R. Frobenius reciprocity reduces the dimension to Hom_P(R,W′).

A unipotent P fixes four nonzero vectors and has four additional regular orbits, so R|P=4·1⊕4·C[P]. The two nontrivial weights of W′ give total dimension eight. This calculation alone does not compute the separate dimensions of the symmetric and alternating two-Z-slot sectors: under iterated evaluation their swap need not become the naive swap of the two R factors.

Section 7 supplies a distinct valid argument for the actual slot split. The primary paper §1 explicitly defines the automorphisms y_g(ω(α,x))=ω(α,gx), realizes them by lifts in N, and splits the resulting central μ5-extension. Thus one may choose the indicated semidirect complement to implement this exact action. Conjugation on End(V) is phase-free, with scalar lift ambiguity cancelling. Other choices of complement are unnecessary for this proof; the dimensions are intrinsic.

Tensor-Hom adjunction preserves the two Z slots and identifies the target with End(V)⊗W′. The zero-character source is the permutation module R and contributes no Hom, because W′ has no P-invariants. For a fixed nonzero sum s, the source character fiber is the permutation module on x≠0,s, while the target fiber is W′ with no additional stabilizer character. The true flip is x↦s−x. For s=(1,0), there are three trivial P-points and four regular P-orbits indexed by nonzero b. The flip exchanges the b and −b orbits equivariantly, producing two regular P-modules in each parity. The trivial points contribute no maps. Each regular module contributes dim W′=2, so both parity Hom dimensions are four.

The total eight and the split four plus four are therefore separately established. Since m010=−2F_sym, vanishing of the middle ordering eliminates exactly the four symmetric eligible parameters and leaves a four-dimensional alternating eligible space. This justifies the conclusion that middle-ordering vanishing alone does not force F=0 within the stated symmetry constraints. It does not establish geometric realization of any alternating parameter or actual vanishing of the middle operation.

## Conditional twelve-dimensional span

Section 6 is valid. Lower nonvanishing supplies the whole canonical four-dimensional subspace L inside the span I of full retained values. Upper nonvanishing supplies surjectivity of I→Tret/L by the already established upper transfer and irreducibility. Then any target vector differs from an element of I by an element of L⊂I, so I=Tret. No splitting is needed. The previously established perfect retained Serre pairing then gives separation of the twelve-dimensional retained physical sector. Both nonvanishing premises remain unproved, and the converse is appropriately not asserted.


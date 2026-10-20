# Lowest-degree generation of the HM middle-cohomology module

## Theorem

Let F be the normalized Horrocks–Mumford bundle on complex P⁴, B=End₀(F), and M_t=H²(P⁴,B(t)). With the previously established dimensions dim M₋₅=2 and dim M₋₄=10, the natural multiplication map

    μ:S₁⊗M₋₅ → M₋₄,       ℓ⊗m ↦ ℓm

is an isomorphism. Consequently

    Soc(M)₋₅=0,      Soc(M)₋₁=0.

This is a structural injectivity/generation proof, not an evaluation of a chosen HM matrix. It requires the actual classical finite HM normalizer symmetry, rather than only the module's dimensions and self-duality. It does not assume any SL₂(C) action on F or M.

## 1. Imported geometric and equivariant input

The already verified inputs are:

- H¹B(t)=0 for t≤−2, and H⁰B(t)=0 for t≤0. The latter follows from stability and simplicity. See historical-source:socle-syzygy-detector/PROOF.md, §1, and historical-source:fourth-ideal-pushforward/COHOMOLOGY-INDEPENDENT-AUDIT.md.
- The dimensions above and the perfect trace–Serre pairings M_t×M₋₅₋t→C, for which polynomial multiplication is adjoint to itself. See historical-source:primary-pairing-constraints/PROOF.md.
- The actual HM bundle carries the coherent action of N⊂SL₅(C), with normal subgroup H of order 125, scalar center C=μ₅, quotient A=H/C≅F₅², and N/H≅SL₂(F₅) acting in the standard way on A. S₁ is an irreducible five-dimensional H-module. The normalized monad's center acts by one scalar in every term, so its action on End₀(F) is trivial. See ../full-hm-image-symmetry/PROOF.md and its independent AUDIT.md, especially the scalar-linearization check in audit §1.

The historical group input was rechecked in Horrocks–Mumford, *A rank 2 vector bundle on P⁴ with 15,000 symmetries*, Topology 12 (1973), §§1–2, printed pp.64–68: https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf . The paper gives H, its irreducible five-dimensional representation, N/H=SL₂(F₅), transitivity on the 24 nontrivial A-characters, and the equivariant bundle construction. The existing literal-presentation audit transports that construction to the bundle used here.

For the usual left action on P(V), a scalar c acts on O(t) by c^(−t). Thus B(−5) is central-trivial: c⁵=1. With the opposite pullback convention the exponents reverse and the same conclusion holds. No projective action is mistaken for a linear action: we first work with the honest group N, and only then factor the representation on M₋₅ through its center.

## 2. The lowest socle vanishes by coordinate Koszul exactness

Write U=S₁* and choose dual bases x_i∈S₁, e_i∈U. The cochain Koszul complex

    K^p=Λ^pU⊗B(p−5),  0≤p≤5,
    δ(s⊗w)=Σ_i x_i s⊗(e_i∧w)

is

    0→B(−5)→5B(−4)→10B(−3)→10B(−2)→5B(−1)→B→0.

It is exact because the coordinates have no common projective zero; on each standard affine open an invertible coordinate supplies a contracting homotopy. Its hypercohomology is therefore zero.

In the column filtration spectral sequence E₁^{p,q}=Λ^pU⊗H^qB(p−5), the leftmost degree-two row cohomology is

    E₂^{0,2}=ker[M₋₅→U⊗M₋₄]=Soc(M)₋₅.

There is no incoming differential on any page because negative columns are absent. An outgoing d_r has target (r,3−r). For r=2 the target E₂^{2,1} is zero because H¹B(−3)=0. For r=3 the target E₃^{3,0} is zero because already E₁^{3,0}=Λ³U⊗H⁰B(−2)=0. For r≥4 its target row is negative. Thus E₂^{0,2}=E∞^{0,2}=0.

Possible nonzero H³ or H⁴ groups elsewhere in this complex cannot affect this reasoning: they would have to enter column zero from a negative column. No vanishing of those rows was used.

## 3. The two-dimensional lowest group is H-trivial

By the central check in §1, M₋₅ is an A-representation on restriction to H. Over C it decomposes into character spaces

    M₋₅=⊕_(χ∈A*) (M₋₅)_χ.

The N-action sends each χ-space to the conjugate-character space and preserves its dimension. SL₂(F₅) is transitive on A*\{1}: identify characters with F₅² via the invariant nondegenerate alternating form and extend any nonzero vector to a determinant-one basis. If one nontrivial character occurred, all 24 would occur with the same positive multiplicity, giving dim M₋₅≥24. Since dim M₋₅=2, only the trivial character occurs. Therefore H acts trivially on M₋₅.

This conclusion does not say that N/H acts trivially on M₋₅. Its two-dimensional multiplicity representation may be nontrivial; no identification of it is needed.

## 4. The multiplication kernel would create a forbidden socle class

The multiplication map μ is H-equivariant under the compatible twist linearizations. Let E=M₋₅. Because H acts trivially on E and S₁ is irreducible, any H-submodule of S₁⊗E has the form S₁⊗E′ for a subspace E′⊂E. One precise proof is semisimplicity, Schur's lemma, and the evaluation equivalence on this isotypic representation:

    Hom_H(S₁,S₁⊗E)=E,
    S₁⊗Hom_H(S₁,L) ≅ L

for every H-submodule L⊂S₁⊗E. This is not a claim that an arbitrary non-equivariant subspace factors as a tensor product.

Apply it to L=ker μ. If L≠0, choose nonzero m∈E′. Then μ(ℓ⊗m)=ℓm=0 for every ℓ∈S₁, so m∈Soc(M)₋₅, contradicting §2. Hence μ is injective. Its source and target both have dimension ten, so it is an isomorphism.

## 5. Duality and the eliminated cofactor defect

The transpose of μ under the perfect pairings is

    μ*:M₋₁→S₁*⊗M₀,
    y↦[ℓ↦ℓy].

Indeed ⟨ℓm,y⟩=⟨m,ℓy⟩. Its kernel is exactly Soc(M)₋₁. Equivalently Soc(M)₋₁=(coker μ)*. The isomorphism in §4 therefore proves Soc(M)₋₁=0.

In the notation of historical-source:primary-pairing-constraints/PROOF.md, the linear cofactor coefficients span S₁, so

    W=Σ b_iM₋₅=M₋₄=T,
    e=c,
    ker α∩ker Q=ker P,
    q=rank P−rank α=d−h≤d.

The cubic-access defect c−e=dim(t₃ ker Q∩Soc(M)₋₁) vanishes. The quadratic-image defect d−h, the primary rank, and the separate secondary obstruction σ are not determined by this argument.

In historical-source:socle-syzygy-detector/PROOF.md, its exact sequence 0→Q_detector→Soc(M)₋₁→Z_detector→0 now implies Q_detector=Z_detector=0. Consequently its canonical maps d₂:L₁→N₃ and d₂:L₂→N₄ are respectively surjective and injective. These follow from the proved vanishing; they were not obtained by evaluating either map. The source-defined cochain constructions and their ambiguities remain valid, but neither detector layer contains a nonzero degree-minus-one socle class for this HM module.

The explicit tensor identities for αμ in historical-source:explicit-conductor-covariant/PROOF.md may now be transported through μ. They still do not prove α singular or nonsingular: none of the surviving primary/cofactor/secondary ranks is asserted here.

## Scope

Only static local proof reading, a primary-paper read, abstract finite-group representation theory, coordinate Koszul exactness, and local proof writing were used. No selected polynomial instance, actual HM multiplication matrix, physical source, source membership, cofactor matrix, differential value, large computation, external computation was performed. The result resolves the previous lowest-generation dependency within the verified classical HM setting; abstract countermodels without its normalizer symmetry remain valid as countermodels to weaker hypotheses.

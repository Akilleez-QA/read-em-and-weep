# Historical mathematical audit receipt

This is a preserved review of the source mathematical manuscript, not a fresh review of the publication bytes. Hashes quoted below identify the historical source versions. See [hm-lowest-generation-PUBLICATION-CHECK.md](../hm-lowest-generation-PUBLICATION-CHECK.md) for the final-publication review.

# Independent audit: lowest-degree multiplication and the degree-minus-one socle

## Verdict

**Pass, conditional only on the explicitly imported HM inputs.** For the normalized stable Horrocks–Mumford bundle F on complex P⁴, put B=End₀(F), M_k=H²(B(k)), and S₁=H⁰(O(1)). The proposed structural argument proves

    μ : S₁ ⊗ M₋₅ → M₋₄ is an isomorphism,
    Soc(M)₋₁ = 0.

The essential facts are the actual coherent normalizer action, the dimensions dim M₋₅=2 and dim M₋₄=10, and the negative H¹ vanishing. No actual multiplication matrix, source value, or differential rank has to be evaluated.

I independently checked the proposed argument against ../full-hm-image-symmetry/PROOF.md and AUDIT.md, historical-source:socle-syzygy-detector/PROOF.md, historical-source:fourth-ideal-pushforward/COHOMOLOGY-INDEPENDENT-AUDIT.md, and historical-source:sharper-hm-regularity/SHARPEST-BOUND.md. I then read the completed PROOF.md in this directory and verified its cofactor consequences against historical-source:primary-pairing-constraints/PROOF.md and historical-source:explicit-conductor-covariant/PROOF.md. The historical normalizer and the Decker–Schreyer vanishing are imported from those verified records; I do not claim a new retrieval or proof of the primary papers here. The two dimensions are the stipulated cohomological inputs.

## 1. The coordinate Koszul argument really kills Soc(M)₋₅

Let V=S₁*. Choose dual bases x₀,…,x₄ of S₁ and e₀,…,e₄ of V. In cohomological columns p=0,…,5 take

    Kᵖ = ΛᵖV ⊗ B(p−5),
    δ(s ⊗ w) = Σ xᵢs ⊗ (eᵢ ∧ w).

This is the six-term coordinate Koszul complex

    0 → B(−5) → 5B(−4) → 10B(−3)
      → 10B(−2) → 5B(−1) → B → 0.

It is exact because the five coordinates have no common zero on P⁴. On any open set where one xᵢ is invertible, the corresponding contraction divided by xᵢ gives a contracting homotopy. Tensoring by the vector bundle B preserves this property. Its hypercohomology is therefore zero.

The spectral sequence with vertical cohomology first has

    E₁^{p,q} = ΛᵖV ⊗ Hᵠ(B(p−5)),
    dᵣ : Eᵣ^{p,q} → Eᵣ^{p+r,q−r+1}.

The entry E₂^{0,2} is exactly

    ker[M₋₅ → V ⊗ M₋₄] = Soc(M)₋₅.

It is a kernel, with no quotient by an earlier column. Here the map sends m to Σ eᵢ⊗xᵢm. Its kernel consists precisely of the elements killed by every linear form.

No differential on any page enters column zero from an existing column. The only possible higher outgoing differentials from (0,2) are

    d₂ : E₂^{0,2} → E₂^{2,1},
    d₃ : E₃^{0,2} → E₃^{3,0}.

The first target is zero already on E₁ because H¹(B(−3))=0. The second is zero already on E₁ because H⁰(B(−2))=0. All dᵣ with r≥4 would have negative target q. Thus E₂^{0,2}=E∞^{0,2}, and exact total hypercohomology forces

    Soc(M)₋₅ = 0.                                      (1)

This argument does not require all H³ or H⁴ entries of this six-term complex to vanish. Such entries cannot enter (0,2), because doing so would require a negative column. In particular no hidden positive-twist cohomology assumption occurs. The proof also does not use vanishing of H¹(B(−1)) or H¹(B).

## 2. The honest normalizer action and its center

Use the classical normalizer N=H₅⋊SL₂(F₅) inside SL₅, with center C=μ₅ and A=H₅/C≅F₅². The previously audited equivariant monad gives an honest coherent action on the literal HM bundle and hence on all B(k). Trace is equivariant, so the trace-free direct summand B is preserved.

The center acts trivially on End(F), and therefore on B: a central scalar acts on F by a scalar, which cancels in conjugation. In the usual left-action convention, c∈C acts on O(k) by c^(−k). Consequently its action on B(−5), and on M₋₅, is c⁵=1. Thus the H₅-action on M₋₅ genuinely factors through A.

The opposite-group pullback convention gives the opposite exponent, also trivial at twist −5. Changing between these conventions preserves every invariant-subspace assertion used here. It is important to use the coherent N action, rather than claiming arbitrary twists descend to the projective normalizer: twist −5 does descend through C, while twist −4 generally does not.

Since A is finite abelian and the ground field is C, decompose

    M₋₅ = ⊕_{χ∈Â} (M₋₅)χ.

Normalizer conjugation permutes these eigenspaces by the induced SL₂(F₅)-action on Â. The latter action is transitive on the 24 nontrivial characters. Indeed Â is a two-dimensional F₅ vector space after choosing a primitive fifth root, and SL₂(F₅) is transitive on its nonzero vectors; the dual action has the same property.

If any nontrivial character appeared in M₋₅, each of the 24 characters in that orbit would appear with the same positive multiplicity. This would force dim M₋₅≥24, contrary to dim M₋₅=2. Therefore

    H₅ acts trivially on M₋₅.                         (2)

Nothing here requires M₋₅ to be a trivial N-module. Its two-dimensional SL₂(F₅)-action may be nontrivial and is irrelevant to the kernel argument.

## 3. Every possible multiplication kernel would contain a full pencil

The natural H₅-action on the five-dimensional coordinate module S₁ is irreducible. One can check this from the abstract Heisenberg relations: its two standard order-five generators satisfy στ=ζτσ for primitive ζ; one generator's eigenspaces are cyclically permuted by the other. Any nonzero invariant subspace consequently has dimension at least five and is the whole S₁. The dual Schrödinger representation is equally irreducible.

Multiplication is equivariant for the coherent actions:

    μ : S₁ ⊗ M₋₅ → M₋₄.

This also has matching central characters. With the left-action convention, S₁ has c⁻¹, M₋₅ has 1, and M₋₄ has c⁴=c⁻¹.

Let R=ker μ. By (2), S₁⊗M₋₅ is an isotypic H₅-module consisting of two copies of S₁ with trivial H₅-action on the multiplicity space. Maschke's theorem and Schur's lemma give

    R = S₁ ⊗ K

for a uniquely determined subspace K⊂M₋₅. More explicitly,

    Hom_{H₅}(S₁,S₁⊗M₋₅) ≅ M₋₅,

and evaluation identifies R with S₁⊗Hom_{H₅}(S₁,R). Under this identification every intertwiner is s↦s⊗m for a unique m∈M₋₅. This rules out an unexamined graph or non-factorized submodule.

If K were nonzero, choose 0≠m∈K. Then S₁⊗m⊂ker μ, meaning xm=0 for every x∈S₁. This contradicts (1). Hence μ is injective. Its domain and target both have dimension ten, by the stipulated dimensions, so

    S₁ ⊗ M₋₅ ≅ M₋₄.                                (3)

The distinction between the two maps is essential: the first Koszul differential is M₋₅→S₁*⊗M₋₄, whereas (3) is S₁⊗M₋₅→M₋₄. Injectivity of the former does not ordinarily imply injectivity of the latter. The H₅-isotypic kernel argument is exactly the additional ingredient that makes that implication valid here.

## 4. Duality gives precisely the degree-minus-one socle map

The trace pairing identifies B with B*. Serre duality on P⁴ gives perfect pairings

    M_k × M_{−5−k} → C.

Multiplication by a linear form is self-adjoint with respect to these pairings in the sense that

    ⟨xm,n⟩_{−4,−1} = ⟨m,xn⟩_{−5,0}

for m∈M₋₅, n∈M₋₁ and x∈S₁. This is the functoriality of cup product, trace and Serre duality. Both cohomology inputs have degree two, so no odd-degree exchange sign intervenes; even an overall duality normalization would not alter kernels.

Consequently the transpose of (3), after identifying M₋₄*=M₋₁ and M₋₅*=M₀, is exactly

    μ* : M₋₁ → S₁* ⊗ M₀,
    n ↦ Σ eᵢ ⊗ xᵢn.

Its kernel is Soc(M)₋₁. Since μ is an isomorphism, so is μ*, proving

    Soc(M)₋₁ = 0.                                    (4)

This identifies the correct indices and the dual coordinate factor. No implication from Soc(M)₋₅=0 to Soc(M)₋₁=0 is being asserted without the intervening surjectivity of μ.

## 5. Scope and consequences

Equations (3)–(4) prove generation of M₋₄ by M₋₅ in one linear step and absence of the degree-minus-one socle. They do not by themselves prove that the entire graded H²-module is generated in degree −5.

In the cofactor notation of the completed proof, the already established linear-coefficient spanning gives W=ΣbᵢM₋₅=S₁M₋₅=T. The definitions c=dim πR(T) and e=dim πR(W) immediately give c=e. Equivalently, the established formula c−e=dim(t₃ ker Q∩Soc(M)₋₁) gives zero by (4). The same earlier exact defect filtration then gives precisely

    ker α ∩ ker Q = ker P,
    q = rank P − rank α = d−h ≤ d.

These formulas in PROOF.md are correct. They do not determine d−h, rank P, rank α, or the separate secondary map σ. No action of SL₂(C) on the HM cohomology module is inferred from the universal binary-quartic coefficient identities.

In the earlier two-stage socle detector, the now-proved vanishing S=Soc(M)₋₁=0 forces Q_detector=0 and Z_detector=0 through its exact sequence. Since Q_detector=coker(d₂:L₁→N₃) and Z_detector=ker(d₂:L₂→N₄), those two maps are respectively surjective and injective. Their cochain maps need not be evaluated separately. This does not decide unrelated multiplication maps, secondary obstructions, or particular physical source classes.

Finally, transporting the known tensor identities for αμ through the now-invertible μ is legitimate. Those identities alone still do not establish singularity or nonsingularity of α, exactly as the completed proof states. The earlier abstract countermodels do not contradict this result: they omitted the actual normalizer symmetry used in Section 2.

All work for this audit was static proof reading, abstract spectral-sequence and finite-group reasoning, duality, and this local text write. No actual HM matrix or source evaluation, rank computation, polynomial specialization, point/jet test, or external write was performed.

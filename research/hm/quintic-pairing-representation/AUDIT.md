# Historical mathematical audit receipt

This is a preserved review of the source mathematical manuscript, not a fresh review of the publication bytes. Hashes quoted below identify the historical source versions. See [hm-quintic-pairing-PUBLICATION-CHECK.md](../hm-quintic-pairing-PUBLICATION-CHECK.md) for the final-publication review.

# Independent audit of the finite-HM representation argument

## Verdict

The proposed argument is correct, provided the separately established numerical input

    dim H²(End F) = 2

is retained as an explicit hypothesis. It proves

    H²(End F) ≅ W′,
    U := H²(End₀ F(−5)) ≅ (W′)*,
    Sym²(U*) ≅ χ3′,
    dim Hom_N(H⁰(O(5)), Sym²(U*)) = 1.

It does not prove that the actual quintic trace-pairing map is nonzero. No actual HM matrix, differential rank, pairing value, or polynomial instance was computed in this audit.

The completed [PROOF.md](PROOF.md) was independently read, including its cofactor consequence. Audited SHA-256: `6c4036d50840eac5a2f9b4face17894fb6a1cc821a758de29edeb1731f722624`. Its dimension dependency is explicitly supplied by [the existing End-cohomology audit](../pairing-foundation-inputs/COHOMOLOGY.md), in preserved items 4–6, especially item 6. That file records the primary h¹ input and derives (h⁰,h¹,h²,h³,h⁴)=(1,24,2,0,0). This audit uses that established result without re-proving the cited primary proposition.

## 1. Sources and normalization

The equivariant complex is the one in [the existing full-symmetry proof](../full-hm-image-symmetry/PROOF.md), with its cohomology F in degree zero:

    K⁻¹ = V1 ⊗ O(−1),
    K⁰  = V3 ⊗ Sym²W ⊗ O,
    K¹  = V* ⊗ W ⊗ O(1),
    K²  = W ⊗ O(2).

Here V3 = V1*, W has determinant one and character χ2, and Sym²W has character χ3.

The original paper uses the unnormalized bundle E with c₁(E)=5; therefore F=E(−3). Its §4, formulas (4.2)–(4.6) and the table on printed p.74, give exactly the following nonzero groups in the four relevant twists:

    H²(F(−2)) = W,
    H¹(F)     = V3,
    H¹(F(1))  = V1 ⊗ W′.

F(−1) is acyclic, and the displayed groups are the only cohomology in these four twists. The shifts correspond to E(−5), E(−4), E(−3), E(−2). Lemma 2.4 identifies W′ with the Galois-conjugate two-dimensional representation. Theorem 3.5 gives H⁰(O(5))^H = χ3 ⊕ χ3′.

Primary reference: [Horrocks–Mumford, Topology 12 (1973), §§2–4 and appendix](https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf).

## 2. Dual degrees and invariant E₁ page

Since K is a bounded locally free complex resolving F, the derived dual K∨ resolves F*. Thus L=K∨⊗F computes End F, with terms

    L⁻² = W* ⊗ F(−2),
    L⁻¹ = V ⊗ W* ⊗ F(−1),
    L⁰  = V1 ⊗ (Sym²W)* ⊗ F,
    L¹  = V3 ⊗ F(1).

The hypercohomology spectral sequence is

    E₁^{p,q} = H^q(L^p)  ⇒  H^{p+q}(End F).

All representations are over C. Taking H-invariants is exact because H is finite, and commutes with the pages, differentials, and abutment filtration. The invariant page is a spectral sequence of N/H representations.

The only nonzero invariant E₁ entries are

    E₁^{−2,2,H} = W* ⊗ W = 1 ⊕ χ3,
    E₁^{0,1,H}  = (V1 ⊗ V3)^H ⊗ (Sym²W)* = χ3,
    E₁^{1,1,H}  = (V3 ⊗ V1)^H ⊗ W′ = W′.

The invariant lines in V1⊗V3 and V3⊗V1 are the identity endomorphisms; N acts trivially on them by conjugation. W≅W* by its invariant alternating form. Its symmetric square is likewise self-dual. These observations account for every dual and rule out a hidden character on the multiplicity-one invariant lines.

## 3. Differential audit

Use the cohomological convention

    d_r : E_r^{p,q} → E_r^{p+r,q−r+1}.

At (p,q)=(1,1), the only potentially nonzero first differential entering is

    d₁ : χ3 → W′.

It vanishes because these are nonisomorphic irreducible N/H representations. For r≥2 the incoming position is (1−r,r). At r=2 this is (−1,2), and at r=3 it is (−2,3); both vanish already on E₁. For r≥4 the source lies outside the complex. Every outgoing differential has p-coordinate greater than 1, so also vanishes. Consequently

    E_∞^{1,1,H} = W′.

There are no other nonzero invariant positions with p+q=2. Thus there is no extension ambiguity in this total degree, and

    H²(End F)^H ≅ W′.

The numerical input h²(End F)=2 now implies that this invariant subspace is all of H²(End F). Without that input, the argument determines only the H-invariant part and does not exclude additional non-H-invariant summands.

The possible d₂ from (−2,2) to (0,1) does not touch total degree two and has no bearing on this conclusion. Its value is not needed or evaluated.

## 4. Serre duality and the trace-free part

The trace decomposition is N-equivariant in characteristic zero:

    End F = O ⊕ End₀ F.

Since H²(O)=H²(O(−5))=0, replacing End F by End₀ F does not change either degree-two group at issue. The trace form identifies (End₀ F)* with End₀ F, equivariantly and nondegenerately.

For N⊂SL(V), the canonical bundle is equivariantly O(−5); the determinant character is trivial. Equivariant Serre duality on P⁴ therefore gives

    H²(End₀ F(−5)) ≅ H²(End₀ F)* ≅ (W′)*.

There is no extra character and no cohomological shift beyond 4−2=2. In particular U*=W′, so Sym²(U*)=Sym²W′ has character χ3′. This also follows by Galois conjugating Sym²W=χ3.

## 5. The one-dimensional Hom space

Let S5=H⁰(O(5)) with the ordinary SL(V) linearization. Since H acts trivially on Sym²(U*) and is normal in N, any N-map out of S5 factors through its H-coinvariants. Averaging canonically identifies those coinvariants with S5^H. Hence

    Hom_N(S5, Sym²(U*))
      ≅ Hom_{N/H}(S5^H, χ3′)
      ≅ Hom_{N/H}(χ3 ⊕ χ3′, χ3′)
      ≅ C.

This uses the inequivalence and multiplicity one of the two three-dimensional irreducibles, not a dimension-only identification.

For the canonical quintic trace pairing, the candidate map is

    B : S5 → Sym²(U*),
    B(s)(u,v) = SerreTrace(s · tr(u ∪ v)).

Indeed u,v have cohomological degree two and twist −5, so their product followed by trace has degree four and twist −10. Multiplication by s leaves degree four and twist −5, whose Serre trace is scalar. Graded cyclicity of trace makes this bilinear form symmetric because (−1)^(2·2)=1. All constituent operations are N-equivariant.

Therefore B lies in the displayed one-dimensional Hom space. It is a scalar multiple of its nonzero generator, with scalar possibly zero. Conditional on B≠0, its image is all of the irreducible χ3′ target; this audit supplies no evidence that the scalar is nonzero.

## 6. The scalar criterion and cofactor consequence

The completed proof's equivalence

    c=0  ⇔  S5·U=0

is correct: its forward implication follows by the nondegenerate pairing U×M₀→C, applied separately to every p·v∈M₀; the reverse implication follows directly from the definition of the quintic pairing.

For the further conclusion, take the established isomorphism μ:S₁⊗U→M₋₄ from [the lowest-degree generation proof](../lowest-degree-generation/PROOF.md). Its assertion and reasoning were read for this audit; the present representation calculation does not depend on it. If α has components given by multiplication by the actual quartics j_r, then for every x∈S₁ and u,v∈U,

    ⟨u,(αμ(x⊗v))_r⟩
      = ⟨u,j_r x v⟩
      = c Ψ(x j_r)(u,v).

Thus αμ=c A_Ψ after the stated Serre identification M₀=U*. Since μ is an isomorphism, the claimed conditional rank identities follow. This verifies an identity of maps without evaluating either map. The quartics j_r need not individually be N-invariant for this substitution into Ψ to make sense. No claim that A_Ψ is invertible, singular, or of any specified rank follows from this argument alone.

## 7. Convention check and boundary

Under the usual left action, the central μ5 acts on F with character c³. The three cohomology modules above consequently have characters 1, c³, c², matching W, V3, V1⊗W′. The dual complex tensors cancel to central character one, as required for End F. Both O(−5) and S5 also have trivial central character. Passing uniformly to the opposite pullback convention does not change the invariant-space or multiplicity conclusions.

The audit checked normalization, dualization, invariant multiplicity lines, differential indexing, Serre-duality characters, symmetry of the abstract trace pairing, and Schur multiplicity. It does not establish the independently assumed total End-cohomology dimension, nonvanishing of B, or any actual HM pairing rank.

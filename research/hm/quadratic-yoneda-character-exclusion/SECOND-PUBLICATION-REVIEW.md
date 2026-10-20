# Independent publication review: quadratic Yoneda character exclusion

**PASS. No mathematical correction required.** The six-file payload establishes the absence of deck-invariant type [22] in the ordinary polarized quadratic Yoneda image, including all non-invariant Ext¹ inputs, under its specified classical Horrocks–Mumford hypotheses.

This verdict binds the six-entry publication payload with SHA-256:

`ccf7757bca021470e619f7232e0a687cef6ed4bdce9a2665197f292647dc2647`

The retained proof has SHA-256:

`a058c6b37bbc421f7767fb187a4a9856f1e3d35758516727b5567a5fb91cdb73`

## Substantive mathematical checks

1. **All twists and complementary Euler lifts.** For a proper nonempty subset S of cardinality r, Künneth gives exactly one intermediate cohomology group of B_S over all twists: Hʳ(B_S)=k. At twists 1 and −1 a factor O(−1) makes the cohomology vanish; twists at least 2 contribute only degree zero and twists at most −2 only degree four. The positive-twist vanishing makes the successive Euler connecting maps onto Hʳ(B_S) surjective. Naturality identifies their value with the induced map on the canonical Hʳ(Ωʳ) generator. The same exterior Euler sequences and the acyclicity of Ωʳ(i), 1≤i≤r, establish End(Ωʳ)=k.

2. **Finite duality and the remainder.** The formula is B_S*⊗ω_P⁴ = σ_*(L_S*⊗ω_Y)=B_(Sᶜ), not a self-duality of B_S. Dualizing the independently chosen complementary lift therefore gives B_S→Ωʳ. Serre duality makes its intermediate-cohomology map nonzero; composing with the original lift gives a nonzero scalar identity. The resulting direct complement has no intermediate cohomology at any twist, so Horrocks applies. H⁰(B_S(1))=0 forces every remaining line summand to have degree at most −2. The full character has no intermediate group to begin with and satisfies the same bound. Neither an equivariant self-duality nor a multiplicative splitting is needed.

3. **Complete nontrivial-character support.** The imported H¹(F(t))=0 for every t≤−2 eliminates all line summands, including the full character. The exterior Euler sequences eliminate the pair and triple Ω-summands using H⁰(F⊗Ω¹)=0, H⁰(F⊗Ω²)=0, H¹(F(−2))=0, and H¹(F(−3))=0. The two H⁰ vanishings follow by injection into sums of negative twists of F and stability. Thus only singleton characters can contribute. No historical singleton dimension or multiplication-map rank enters this conclusion.

4. **Singleton stabilizer representation.** The S₃ stabilizer fixes the singleton H¹ generator: it permutes only degree-zero Künneth factors. Averaging the Euler lift preserves its nonzero cohomology map. Its underlying splitting and the complementary H¹ vanishing give an equivariant isomorphism U→V_S. The base P⁴ is fixed pointwise and both F and Ω¹ carry the specified trivial stabilizer actions, so U is a trivial S₃ representation. Transport induces precisely U⊗k⁴_perm, compatibly with the four distinct deck characters. No unaccounted sign or nontrivial action on U remains.

5. **The quadratic source and the invariant family.** Equality of the order-two deck characters is necessary and sufficient for an invariant product. Hence the invariant symmetric-square source is Sym²V₀ ⊕ ⊕ᵢSym²Vᵢ, not the unrestricted symmetric square of the singleton permutation representation. The second part is Sym²U⊗([4]⊕[31]), with no [22]. Equivariance and characteristic-zero semisimplicity preserve this exclusion in the image; exactness of invariants also identifies the invariant part of the image with the image of the invariant source. The actual smooth coefficient family exhausts V₀, so every invariant tangent extends to second order. Its square vanishes, and polarization kills Q on Sym²V₀. This does not require versality or Ext²=0.

6. **Serre pairing.** H⁴(O_X) has character χ_all⊗sgn: elliptic involutions act negatively on H¹(O_C), and permutation of four degree-one factors contributes the Koszul sign. The perfect trace pairing consequently pairs the full deck character only with the invariant character. Since [22] is self-dual and sign-invariant, a full-deck [22] class requires an invariant [22] detector. The quadratic image has no such component.

## Predecessors and publication scope

The necessary coefficient-family and invariant-row inputs are supplied by [PR179](https://github.com/Akilleez-QA/read-em-and-weep/pull/179), head `2b03992b32d2f5cf0509b6f4840adf08369f54b7`. The exact presentation, stability, and published negative-twist cohomology input are supplied by [PR125](https://github.com/Akilleez-QA/read-em-and-weep/pull/125), head `8281ea90d8a1ffd14eaa10af76174b4c25a32742`. The latter theorem covers all twists t≤−2, rather than a finite numerical table. The argument applies to the specified complex model and compatible base changes, not arbitrary forms or positive characteristic.

The proof and both historical audits are byte-for-byte equal to their source manuscripts; all six publication content hashes agree with the supplied bindings. DEPENDENCIES.md resolves the historical citation names without substituting computational certificates for the stated mathematical inputs.

The README correctly distinguishes the historical proof's scope from the current literature in this series: PR179 separately proves invariant-invariant ordered-product vanishing. That is no longer an unresolved frontier and is not new content of this addendum. The additional result here is the complete non-invariant-character exclusion. It does not compute the retained obstruction, prove its vanishing, or establish higher-order unobstructedness or liftability.

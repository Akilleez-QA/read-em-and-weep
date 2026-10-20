# Independent audit of the quadratic Yoneda exclusion

## Verdict and binding

**PASS. No mathematical correction required.** This is an independent review, separate from the producer's `AUDIT.md`.

Reviewed document: `PROOF.md`, titled **Ordinary quadratic Yoneda products cannot detect the full-deck [22] component**.

Reviewed proof SHA-256:

`a058c6b37bbc421f7767fb187a4a9856f1e3d35758516727b5567a5fb91cdb73`

The verdict binds these exact proof bytes. It establishes the stated exclusion for the ordinary polarized quadratic map, including non-invariant first-order inputs, with the ordered-product limitation retained.

## Checks

### 1. Complementary Euler lifts and all remaining twists

The Künneth classification is correct for every nonempty proper subset S: B_S has its only intermediate twisted cohomology at twist zero and degree r=|S|, where it is one-dimensional. In particular B_S(i) has no positive-degree cohomology for i≥1. Applying Hom(−,B_S) successively to the exterior Euler sequences therefore surjects Hom(Ω^r,B_S) onto H^r(B_S). Naturality identifies this map with the induced map on the canonical H^r(Ω^r) generator.

Finite duality gives B_S^*(−5)=B_{S^c}. The complementary lift, dualized and twisted, gives B_S→Ω^r. Serre duality shows this map is nonzero on H^r. Its composition with the original lift is a nonzero scalar identity because Ω^r is simple. The stated justification of simplicity is valid: Ω^r(i) is acyclic for 1≤i≤r, and the same Hom connecting maps identify End(Ω^r) with H^r(Ω^r)=k. This works in particular for r=1 and r=3; it does not incorrectly identify either B_S with its own shifted dual.

After splitting Ω^r, the complement has no intermediate cohomology at any twist, so Horrocks applies. A line summand O(b) with b≥−1 would contribute to H⁰(B_S(1)), which vanishes. Hence every remaining line summand has b≤−2. For S equal to all four indices, there is no intermediate cohomology to begin with, and the same bound applies to every summand. No multiplicative or equivariant splitting is used here.

### 2. Ext¹ character support

The imported vanishing H¹(End H(t))=0 for t≤−2 kills every line summand. For Ω², the only possible incoming term is H⁰(F⊗Ω¹), and it vanishes by the injection into F(−1)^5 and stability. The adjacent H¹(F(−2)) also vanishes. For Ω³, the corresponding incoming term H⁰(F⊗Ω²) vanishes by injection into F(−2)^10, while H¹(F(−3)) vanishes. The full character has only the vanishing line contributions. Thus only singleton nontrivial characters can contribute to Ext¹. No dimension of the singleton space U is required or imported.

### 3. Stabilizer action and induced representation

For S={1}, the S3 stabilizer permutes only degree-zero Künneth factors. Its action on H¹(B_S) is therefore trivial. Averaging the lift Ω¹→B_S preserves its nonzero cohomology map and makes the lift S3-equivariant. The quotient base is fixed pointwise, and F and Ω¹ have the stipulated trivial stabilizer actions. The averaged lift still splits as an underlying bundle; its complement has the same vanishing contribution to H¹ after tensoring with F. Consequently U→V_S is an equivariant isomorphism with trivial stabilizer action. A separate equivariant line-bundle splitting is unnecessary.

Transporting this averaged lift gives V_noninv=Ind(S3→S4)(U_trivial)=U⊗k⁴_perm, compatibly with the four distinct singleton deck characters. Stabilizer invariance makes the transport independent of coset representatives. This step introduces no unnoticed sign character.

### 4. Deck-invariant symmetric quadratics

All deck characters have order two, so the invariant quadratic source is precisely Sym² V_0 ⊕ ⊕_i Sym² V_i. In particular distinct singleton terms and invariant-singleton terms cannot enter the invariant target. The second summand is Sym² U⊗k⁴_perm, whose only S4 types are [4] and [31]. Ordinary Sym² is the correct source for the polarized map a∘b+b∘a on degree-one classes. Equivariance and characteristic-zero semisimplicity prevent its image from acquiring [22].

The coefficient family is an actual bundle family over a smooth open subset of projective space. Its Kodaira–Spencer map is injective of dimension 79, and its image is deck-invariant because the maps factor through Y. Combined with the independent invariant Ext¹ dimension 79, this image equals V_0. Every tangent therefore extends to second order in this family, forcing v∘v=0 in Ext². Polarization gives a∘b+b∘a=0 for a,b∈V_0. The argument needs neither versality nor vanishing of Ext².

### 5. Serre character and limitation

Each elliptic involution acts by −1 on H¹(O_C); four-factor permutation on H⁴(O_X) is the Koszul sign. Thus the trace target is χ_all⊗sgn. Although a trivialization of the canonical bundle is not equivariant with trivial character, this stated target character exactly accounts for that fact. The perfect middle-degree pairing forces a full-deck class to pair only with a deck-invariant class. Since [22] is self-dual and its partition is self-conjugate, twisting by sgn preserves [22]. The absent invariant [22] quadratic component is therefore precisely the component required to pair with a full-deck [22] class.

The family argument kills symmetric invariant-invariant products only. An alternating invariant-invariant ordered product may still have type [22]. The proof expressly preserves this possibility. Same-singleton ordered products have source (U⊗U)⊗k⁴_perm and remain excluded; this does not remove the invariant alternating exception. Nothing here establishes vanishing of the obstruction, higher unobstructedness, or exhaustion of other possible detectors.

## Dependencies and evidence boundary

Static dependency review included:

- `../pair-character-vanishing/PROOF.md`;
- `../projective-target-directions/INVARIANT-EXT-STRUCTURAL-REDUCTION.md`;
- `../projective-target-directions/FULL-COEFFICIENT-FAMILY.md`;
- `../hm-presentation-independent/PROOF.md`.

The classical negative-twist cohomology theorem remains the explicitly imported theorem verified in the dependency package; this audit does not claim a new proof of that published theorem. The presentation dependency of the older coefficient-family text is supplied by the independent presentation proof, so its historical conditional wording does not reopen that dependency here. Characteristic-zero statements concern the stipulated rational data and base changes, as stated in the proof.

Only static local document reads, formal cohomological/representation-theoretic reasoning, creation of this local audit, and a file-content hash were used. No source/model/rank/polynomial-instance/point/jet/residual evaluation or execution, external write, or local Codex operation was performed.

> Historical mathematical audit, preserved in full apart from nonmathematical process statements and source-link normalization. Original-source hashes identify the audited source text; publication-byte hashes are recorded separately. This is not a claim of a fresh or formal proof check.

# Independent audit: ordinary characteristic traces

## Verdict

**PASS, under the explicitly imported carrier and actual-source hypotheses.** The final six-section PROOF.md has the correct source-gerbe sign in its stated cup/exterior convention, the correct mixed-contraction constants, and valid deck, permutation, and projective-inversion arguments for the ordinary Atiyah-trace maps. No mathematical correction remains.

Audited title: *Ordinary characteristic traces cannot detect the retained obstruction*. Original-source `PROOF.md` SHA-256: `45e7c0b9f6d52af6eb5bd724f1352b016858a75547ad799ba5811aae82727412`.

The conclusions have different scopes and should remain separate:

1. The displayed scalar characteristic difference is identically zero for this carrier. It does not compute the actual mixed obstruction.
2. All ordinary Atiyah-trace maps vanish on the full-deck `[22]` isotypic component at the original symmetric tuple. This includes the entire retained thirty-dimensional target and its twelve-dimensional inversion-positive part, subject to the cited identification of that retained target.
3. Independently of that permutation-sector identification, all ordinary Atiyah-trace maps vanish on every inversion-positive class. Applying this to the actual mixed class uses the separately established weighted-root-gerbe transport and its actual-source premises.

None of these statements proves that the actual mixed class vanishes or is nonzero. None establishes a categorical necessity theorem for the displayed scalar polynomial or identifies a historical scalar selector with an Atiyah-trace map.

## 1. Source normalization and the gerbe sign

FIRST-LIFT-STRUCTURAL §5 uses the column connection-difference representative `A^E`, the ordinary exterior product with Alexander–Whitney endpoint order, and `ι_(a,b)=ι_Vb ι_Va`. Its displayed identities are

    ι_r tr(A^E ∧ A^E) = −2 tr(C_r),
    δs_raw,r = b_r − tr(C_r)/2.

Consequently, before introducing a Chern-character normalization, the source gives the unambiguous identity

    [b_r] = −(1/4) ι_r [tr(A^E ∧ A^E)].

With the audited proof's explicitly declared normalization

    ch₂(E) = (1/2)[tr(A^E ∧ A^E)],

this is precisely `[b_r]=−(ι_r ch₂)/2`. The minus sign is required. Replacing the Atiyah class by its negative does not change its square and cannot remove this sign.

The independent line-class check agrees. Source §4 gives the old line connection difference `−θ` and `q_d=2θ(V_d)`; source §5 gives `b_(a,b)=(15/4)q_a∪q_b`. In the same convention, `n=[−θ]` and `η_d=−[q_d]/2`, so `[b_(a,b)]=15η_aη_b`. This is the negative of the proof's `β_(a,b)=−15η_aη_b`.

There is also an internal characteristic-class consistency check directly in the imported transgression: source (5.2), (5.4), and (5.5) give

    [tr(A^E ∧ A^E)] = −30[θ∧θ] = −30n².

This matches `2ch₂(E)=−30n²`. It is a cohomological consequence of the already established source identity, not a new source evaluation.

The sign statement is intentionally convention-dependent. If one instead uses a Koszul-totalized product or a different comparison with total de Rham cohomology, all product and characteristic-class comparison signs must be translated together. One must not change only the sign attached to the raw square while retaining the rest of this proof's conventions. The final proof consistently stays in its declared ordinary cup/exterior convention.

## 2. Formal Chern identities and contraction constants

The imported data `c₁(H)=−h`, `c₂(H)=4h²`, and `f*h=2n` give

    c₁(f*H)=−2n,
    c₂(f*H)=16n²,
    c₁(E)=0,
    c₂(E)=16n²−2n²+n²=15n².

For a rank-two determinant-trivial bundle with formal roots `x,−x`, one has `ch₂=−c₂` and `ch₄=c₂²/12`. Thus the stated `ch₂(E)=−15n²` and `ch₄(E)=75n⁴/4` are correct.

The two gradings matter. The classes `n_i∈H¹(Ω¹)` commute under the ordinary cup/exterior product, while their contractions `η_i∈H¹(O)` anticommute. Each `n_i²=0` because it is pulled back from one curve. Hence

    n² = 2 Σ_(i<j) n_i n_j,
    n⁴ = 24 n₀n₁n₂n₃.

For the specified ordered contractions, the surviving products have positive sign:

    ι_(a,b)n² = 2η_aη_b,
    ι_pι_q n⁴ = 24η₀η₁η₂η₃.

Disjoint pair contractions commute because each has even exterior degree. It follows that `β_pβ_q=225η₀η₁η₂η₃`, whereas `ι_pι_q ch₄=450η₀η₁η₂η₃`. The coefficient `2` in the cancellation is therefore correct. The two source-gerbe minus signs cancel in `[b_p][b_q]`.

The proof correctly refuses to identify the raw same-triple product `b_p,ijk b_q,ijk` with the Čech cup product representing `[b_p][b_q]∈H⁴(O_X)`. The former occurs as part of a degree-two cochain formula; the latter is a degree-four cohomology class. This degree distinction prevents the scalar cancellation from being silently treated as a computation of the actual curvature class.

## 3. Binding to the actual mixed class

FIRST-LIFT-STRUCTURAL §§7–8 proves closure of the complete normalized curvature `M` and the source identity `R=tf(M)+δW`. MIXED-GAUGE-DESCENT §§1–2 explains why the parameter-weighted gerbe is central for this truncated mixed algebra and identifies `[M]` as its lifting-obstruction class. Thus `[R]=tf([M])` is the appropriate actual-source bridge.

The audited proof uses exactly that bridge and does not replace it with equality of raw representatives. Nor does it assume that the trace of `[M]` vanishes. It treats the scalar characteristic identity as a separate cohomological identity and explicitly declines to infer a natural map from `[R]` to that polynomial. This boundary is mathematically necessary and correctly maintained.

## 4. Deck-character analysis of the Atiyah-trace maps

For the ordinary maps

    τ_k(z)=tr(z∪At(E)^k)/k! ∈ H^(k+2)(Ω_X^k),

the established deck linearization of E and naturality of the Atiyah class imply equivariance. The imported full-sign purity theorem supplies the required character of the actual source class; it is not inferred from a count of derivative labels alone.

On the product of four elliptic curves, the equivariant Hodge-cohomology description is

    H^a(Ω_X^b) ≅ Λ^a H¹(O_X) ⊗ Λ^b H⁰(Ω_X¹).

Each factor involution acts negatively on both corresponding one-dimensional spaces. The character of a subset-indexed basis element is consequently the symmetric difference of its cohomology and form index sets.

For `k=2`, the cohomology subset is all four factors and the form subset has size two. Every character is therefore supported on the complementary two factors, never all four. Thus the full-sign part of `H⁴(Ω²)` is zero. For `k≥3`, the cohomology degree exceeds the dimension. For `k=0`, the map vanishes on trace-free classes, as stated.

For `k=1`, full sign requires a singleton form index and its complementary three cohomology indices. There are exactly four possibilities. The deck-character test alone therefore leaves a four-dimensional target; it does not prove that τ₁ vanishes. The proof accurately distinguishes this intermediate result from the additional symmetry arguments that follow.

## 5. Permutation exclusion of the retained sector

At the original symmetric tuple, factor permutations preserve the symmetric map f and naturally linearize the external product N. They therefore linearize E and make τ₁ equivariant. With W the permutation representation on four factor indices,

    Λ³W ≅ det(W)⊗W* = sgn⊗W*.

The full-deck target is the complementary-index subspace of `Λ³W⊗W`. After multiplying the omitted-index basis by `(-1)^j`, it is the diagonal subspace of `sgn⊗W*⊗W`. A permutation acts on that diagonal basis as its ordinary permutation action multiplied by its sign. Therefore

    H³(Ω¹)_full-deck ≅ sgn⊗W = [1111]⊕[211].

This verifies the permutation sign explicitly. There is no `[22]` constituent. Complete reducibility then makes the equivariant map from the full `[22]` isotypic source component to this target zero.

The retained-sector proof and its source-binding addendum distinguish one D₈-epsilon line in `[22]` from the two-dimensional whole irreducible representation. The inversion-eigenspace proof and audit give the retained multiplicity dimension thirty and its positive part twelve, while the whole isotypic component has dimension sixty. The audited characteristic proof preserves this distinction. It does not claim that the D₈-epsilon subspace is itself S₄-stable; it first kills the entire S₄-isotypic component and then restricts to the retained subspace.

Application to a named historical or corrected source retains the source-membership and comparison premises. The abstract annihilation of the `[22]` sector itself does not require proving that the actual class belongs to it.

## 6. Projective inversion and the stronger all-k exclusion

The projective-inversion theorem supplies `a*E≅E⊗Q` with `Q²≅O_X`, together with the coherent induced End action. This is sufficient for the characteristic maps even though there is no untwisted isomorphism `a*E≅E`.

For a line bundle, the Atiyah class is additive under tensor product. Thus `2At(Q)=At(Q²)=At(O)=0`, and characteristic zero gives `At(Q)=0`. The tensor formula for Atiyah classes and naturality under bundle isomorphisms identify `a*At(E)` with `At(E)` under the specified End identification. Taking cup powers and trace proves equivariance of every τ_k. The scalar ambiguity in a bundle isomorphism inducing the projective identification has no effect on this cohomological conclusion.

On one curve, the source automorphism has `a*ω=iω`. Equivariant Serre duality pairs `H¹(O_C)` with `H⁰(Ω_C¹)` to the invariant trace line, so its eigenvalue on `H¹(O_C)` is `i⁻¹=−i`. Translation acts trivially on these spaces. Consequently a acts on every nonzero trace-map target by

    (−i)^(k+2) i^k = −1.

In particular, the entire `H³(Ω¹)` target is negative, not merely its full-sign part. An inversion-positive source class must therefore map to zero under every τ_k. This argument does not need a deck or S₄ sector assumption once inversion positivity is known.

The essential actual-source input is ROOT-GERBE-TRANSPORT, not the projective-bundle symmetry by itself. That theorem gives a regular gerbe correction, handles the flat two-torsion line twist, matches the pair-pure first lifts using H¹ vanishing, and concludes that the actual class is positive under the same induced End action. Its accompanying audit retains the actual-source identities as imported hypotheses. With those hypotheses, applying the exclusion to `[R]` is justified.

The final proof includes the requested field clarification: the inversion argument is made over C or after extending to a field containing i, and the resulting vanishing descends by faithful field extension. No field-of-definition correction remains.

## 7. Corrections and scope limits

No outstanding correction is required. During this audit the field-extension sentence and the general eigenvalue formula for all k were added to §5.2; both additions were statically reread and are correct. The sentence that Chern classes alone do not determine τ₁ is consistent with the later symmetry exclusion: the latter uses additional equivariance and actual-source transport, not just numerical Chern data.

The surviving possible obstruction target is not reduced by any computed value here. Rather, this family of ordinary characteristic maps is proved incapable of detecting the indicated sectors or actual inversion-positive class. This does not exclude every noncommutative cyclic, derived, or refined characteristic construction, and it supplies no replacement detector or primitive.

## Mathematical inputs and scope

The historical audit checked [PROOF.md](PROOF.md) and the following mathematical inputs; their source bindings are listed in DEPENDENCIES.md:

- `dependencies/relative-mixed-character-purity/dependencies/FIRST-LIFT-STRUCTURAL.md`, especially §§4–8;
- `dependencies/relative-mixed-character-purity/PROOF.md`;
- `dependencies/pair-character-vanishing/PROOF.md` and `dependencies/pair-character-vanishing/MIXED-GAUGE-DESCENT.md`;
- `dependencies/retained-sector-structural/PROOF.md` and `dependencies/retained-sector-structural/SOURCE-BINDING-ADDENDUM.md`;
- `dependencies/inversion-eigenspaces/PROOF.md` and `dependencies/inversion-eigenspaces/AUDIT.md`;
- `dependencies/inversion-projective-lift/PROOF.md`, `dependencies/inversion-projective-lift/ROOT-GERBE-TRANSPORT.md`, and `dependencies/inversion-projective-lift/ROOT-GERBE-AUDIT.md`.

Supplementary reads checked the ambient root-line normalization in the sibling `relative-mixed-character-purity/dependencies/PRODUCT-ROOT.md`, the carrier identification in `hm-presentation-independent/PROOF.md`, and the stated Chern normalization in `projective-target-directions/INVARIANT-EXT-STRUCTURAL-REDUCTION.md`. The present theorem treats these carrier conclusions as established inputs.

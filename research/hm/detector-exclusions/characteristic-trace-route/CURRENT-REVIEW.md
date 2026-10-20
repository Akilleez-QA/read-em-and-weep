# Current independent mathematical review: S022

Review date: 2026-10-20.

**PASS within the stated hypotheses and bounded scope.** This review covers the complete proof, historical audit, dependencies, and current-scope text. It checks the mathematical argument and directly cited public prerequisites; it is not formal verification or an evaluation of an actual HM/source instance.

## 1. S022: ordinary characteristic traces

### Chern calculation and source sign

The rank-two twisting formulas applied to `c₁(H)=−h`, `c₂(H)=4h²`, and `f*h=2n` give

    c₁(E)=0,
    c₂(E)=16n²−2n²+n²=15n²,
    ch₂(E)=−15n²,
    ch₄(E)=225n⁴/12=75n⁴/4.

In the explicitly declared cup/exterior convention, the `n_i` commute and square to zero, while their contractions `η_i` anticommute. The ordered disjoint pair contractions therefore give

    ι_p n²=2η₀η₁,
    ι_q n²=2η₂η₃,
    ι_pι_q n⁴=24η₀η₁η₂η₃.

Consequently `ι_pι_q ch₄=450η₀η₁η₂η₃=2β_pβ_q` for `β_r=(ι_r ch₂)/2`. There is no missing factor.

The immutable PR252 first-lift text, §§5–8, contains precisely the required ordered identities:

    ι_r tr(A^E∧A^E)=−2tr(C_r),
    δs_raw,r=b_r−tr(C_r)/2,
    R=tf(M)+δW.

With the packet's stated normalization `ch₂=[tr(A^E∧A^E)]/2`, these imply `[b_r]=−β_r` and `[R]=tf([M])`. The source's `q_d=2θ(V_d)` and old connection difference `−θ` provide the independent consistency check `[b_r]=15η_aη_b`. Reversing the sign of the Atiyah class cannot change its square. The negative gerbe sign is therefore correctly retained, and cancels only when multiplying the two gerbe classes.

The proof correctly keeps the degree-two raw same-triple scalar product separate from a degree-four cup product. It does not turn the scalar cancellation into a computation of `R`.

### Equivariant exclusions

For `τ_k(z)=tr(z At(E)^k)/k!`, the deck character of a Hodge basis element is the symmetric difference of its cohomology and form index sets. Thus:

- `τ₀=0` on trace-free classes.
- `H⁴(Ω²)` has no full-deck character.
- Targets with `k≥3` vanish by cohomological dimension.
- The full-deck part of `H³(Ω¹)` has dimension four.

The last target is `sgn⊗W=[1111]⊕[211]`, not the ordinary permutation module. The omitted-index orientation factor supplies the sign, and there is no `[22]` constituent. Killing the entire `[22]` isotypic component before restricting to its D₈-epsilon line is legitimate; treating the retained epsilon subspace itself as S₄-stable would not be.

The projective-inversion route is independently valid. From `a*E≅E⊗Q` and `Q²≅O`, characteristic zero gives `At(Q)=0`. Naturality and the tensor formula make the trace maps equivariant under the induced End action without assuming an untwisted bundle lift. The eigenvalues on `H¹(O_C)` and `H⁰(Ω¹_C)` are `−i` and `i`, so every nonzero target has eigenvalue

    (−i)^(k+2)i^k=−1.

Every inversion-positive class is therefore annihilated. Applying this to the actual `R` uses the separately cited root-gerbe transport theorem, whose source identities, regular gerbe correction, flat two-torsion twist, and first-lift matching premises remain explicit. Full-deck purity likewise remains a source-bound input when applied to `R`.

**Accepted conclusion:** the specified scalar expression is an identity, and the stated ordinary trace maps are blind to the indicated abstract sectors and, conditionally, to the actual inversion-positive class. No actual obstruction value, historical-detector comparison, or categorical necessity theorem follows.

## Reviewed file SHA-256 bindings

The four files below are the exact texts reviewed before this review was added.

- `AUDIT.md`: `f18df69b37f8fefc600bcec1388baf9557f9c2de327b2cfef6ddd2269518bdf5`
- `DEPENDENCIES.md`: `cfc8095641c2b5c557d1327a6f1b59156db574c9c09766f1c3df9ea475c46beb`
- `PROOF.md`: `25053df9efc9b88d88f348fc0055bbdecb072ec2a2759a460c5768d21691fd72`
- `SCOPE.md`: `591e4c5533559f24e11dd4fc814ac86811b6e05cfc5b2ab74e7a8a13d42efc4d`

## Immutable public prerequisites

- [coefficient: PR179, 2b03992b32d2f5cf0509b6f4840adf08369f54b7](https://github.com/Akilleez-QA/read-em-and-weep/blob/2b03992b32d2f5cf0509b6f4840adf08369f54b7/research/hm/cubic-loci/foundation-p01/COEFFICIENT-FAMILY.md): Coefficient family and equivariant Kodaira–Spencer isomorphism.
- [cohomology: PR179, 2b03992b32d2f5cf0509b6f4840adf08369f54b7](https://github.com/Akilleez-QA/read-em-and-weep/blob/2b03992b32d2f5cf0509b6f4840adf08369f54b7/research/hm/cubic-loci/foundation-p01/INVARIANT-COHOMOLOGY.md): Classical invariant cohomology and representation hypotheses.
- [inversion: PR181, 97190240fa87b8ed68f2a90f701bda0e7236f0e7](https://github.com/Akilleez-QA/read-em-and-weep/blob/97190240fa87b8ed68f2a90f701bda0e7236f0e7/research/hm/cubic-loci/foundation-p02/INVERSION-LIFT.md): Sections 1–6 establish projective lift and two-torsion scalar line; no untwisted carrier lift is assumed.
- [eigenspaces: PR183, cedeed5ce96ebc7fc045c47750c9e29add3e55ad](https://github.com/Akilleez-QA/read-em-and-weep/blob/cedeed5ce96ebc7fc045c47750c9e29add3e55ad/research/hm/cubic-loci/foundation-p03/INVERSION-EIGENSPACES.md): Sections 1–5 establish character conventions and the retained (12,18) dimensions. Original later sections are not required for the trace-map zero theorem.
- [retained: PR183, cedeed5ce96ebc7fc045c47750c9e29add3e55ad](https://github.com/Akilleez-QA/read-em-and-weep/blob/cedeed5ce96ebc7fc045c47750c9e29add3e55ad/research/hm/cubic-loci/foundation-p03/RETAINED-SECTOR.md): Abstract retained sector and its explicit source-matching restriction; actual membership is not inferred from symmetry alone.
- [pair: PR250, f1de2347c471c572cc074383d96409cdf68fc585](https://github.com/Akilleez-QA/read-em-and-weep/blob/f1de2347c471c572cc074383d96409cdf68fc585/research/hm/relative-models/pair-character-vanishing/MIXED-GAUGE-DESCENT.md): Actual mixed curvature comparison remains conditional on its named source identities.
- [firstlift: PR252, 92ccceb1a023dd86bf4d17f4b86b779cc1b7c44f](https://github.com/Akilleez-QA/read-em-and-weep/blob/92ccceb1a023dd86bf4d17f4b86b779cc1b7c44f/research/hm/relative-models/relative-mixed-character-purity/dependencies/FIRST-LIFT-STRUCTURAL.md): Sections 4–8 bind scalar gerbe signs and [R]=tf([M]) under explicit source hypotheses.
- [purity: PR252, 92ccceb1a023dd86bf4d17f4b86b779cc1b7c44f](https://github.com/Akilleez-QA/read-em-and-weep/blob/92ccceb1a023dd86bf4d17f4b86b779cc1b7c44f/research/hm/relative-models/relative-mixed-character-purity/PROOF.md): Full-deck purity under the specified actual-source assumptions.
- [gerbe: PR254, dc288b36f18623be81884de3f52ac64a588ec108](https://github.com/Akilleez-QA/read-em-and-weep/blob/dc288b36f18623be81884de3f52ac64a588ec108/research/hm/relative-models/inversion-fixed-family/ROOT-GERBE-TRANSPORT.md): Inversion positivity of the actual mixed class, conditional on its source identities; not just bundle symmetry.

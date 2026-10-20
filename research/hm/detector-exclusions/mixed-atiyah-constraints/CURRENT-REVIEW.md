# Current independent mathematical review: S168

Review date: 2026-10-20.

**PASS within the stated hypotheses and bounded scope.** This review covers the complete proof, historical audit, dependencies, and current-scope text. It checks the mathematical argument and directly cited public prerequisites; it is not formal verification or an evaluation of an actual HM/source instance.

## 3. S168: universal mixed Atiyah channel

The projected curvature representatives must be made pointwise traceless before applying matrix identities. The proof does this explicitly; it does not equate a chosen harmonic hyperplane representative with the trace of an arbitrary curvature representative. Projection on holomorphic cotangent factors commutes with the Dolbeault differential, and the scalar curvature entries have even total degree.

The decomposition

    V₂⊗V₂=V₄⊕V₂⊕V₀,
    Sym²V₂=V₄⊕V₀,
    Λ²V₂=V₂

proves the stated complete classification of coefficient-free, derivative-free, gauge-natural bilinear maps `sl₂×sl₂→sl₂`. The commutator is the sole channel. This proves a universal Hom-space statement, not that its specialization to the particular Atiyah classes is nonzero.

The intrinsic coefficient bundle of `C=[B_z,B_h]` is the mixed summand `Ω¹_z⊗Ω¹_h` embedded in `Ω²_X`, not `ω_X`. Under block exchange, geometric pullback gives `τ*C=−C`. The reordering sign already belongs to that geometric action and must not be added again.

For an equivariant linear coefficient transformation `L`, `L(C)` is odd. The specified retained projector factors through the block-even projector, so `P_ret L(C)=0`. The existence and equivariance of `L` are hypotheses, not conclusions. Odd auxiliary coefficients or an odd component of `L` can change this parity but cannot by themselves establish a retained nonzero value.

The algebraic discriminant calculation is correct:

    U²=(p/2)Id, V²=(r/2)Id, UV+VU=qId,
    [U,V]²=(q²−pr)Id.

Cyclic trace also gives `tr([U,V]U)=tr([U,V]V)=0`. The normalized Chern data imply

    tr B²=−(15/2)(x+y)²,
    p=−(15/2)x², q=−(15/2)xy, r=−(15/2)y²,

so `q²=pr` and `C²=0` in the stated cohomology group.

Both PR1 comments still have exactly the creation/update timestamps quoted in the packet. The target comment explicitly distinguishes the retained thirty-space in the even 32-space from the separate odd thirty-space; it supplies the canonical finite-trace removal of the alternating two-space. The first-order comment explicitly declines a prescribed physical-lift comparison or mixed ambient extension.

**Accepted conclusion:** the bounded universal exclusion and square-zero constraint are valid. They do not identify `C` with the actual obstruction, imply `C=0`, or provide a formality/Massey theorem.

## Reviewed file SHA-256 bindings

The four files below are the exact texts reviewed before this review was added.

- `AUDIT.md`: `c441a98be7f699b0e0d3b4a5f3ba25ec21772b08f130db7e80fc178e8de19c93`
- `DEPENDENCIES.md`: `9aab7beb67b958fb7c956a3ac044c76ace2cdac9a62393aebac171f4bee14199`
- `PROOF.md`: `c7bf4b309a499f219491f4463631bc93e72df339ed9d954be77a9c9e7ead9f5e`
- `SCOPE.md`: `9b80c61bf77b523573e5752c77f8f06bf5ffe30b1b5b053dcd90ac8553376025`

## Immutable public prerequisites

- [chern: PR247, 01c96a7e1b24685eacd5d1dc52ed0ea026490146](https://github.com/Akilleez-QA/read-em-and-weep/blob/01c96a7e1b24685eacd5d1dc52ed0ea026490146/research/hm/relative-models/relative-chern-constraints/PROOF.md): Normalized HM Chern classes and relative Chern constraints.
- [ordered: PR179, 2b03992b32d2f5cf0509b6f4840adf08369f54b7](https://github.com/Akilleez-QA/read-em-and-weep/blob/2b03992b32d2f5cf0509b6f4840adf08369f54b7/research/hm/cubic-loci/foundation-p01/ORDERED-PRODUCTS.md): Ordinary Yoneda product convention, distinct from even Atiyah coefficients.
- [retained: PR183, cedeed5ce96ebc7fc045c47750c9e29add3e55ad](https://github.com/Akilleez-QA/read-em-and-weep/blob/cedeed5ce96ebc7fc045c47750c9e29add3e55ad/research/hm/cubic-loci/foundation-p03/RETAINED-SECTOR.md): Abstract retained sector and its explicit source-matching restriction; actual membership is not inferred from symmetry alone.

The within-series rank-two Atiyah identity depends on [unit 02, PR403 at ad1d436cfd9b35a3750c06fa24af33e189404975](https://github.com/Akilleez-QA/read-em-and-weep/blob/ad1d436cfd9b35a3750c06fa24af33e189404975/research/hm/detector-exclusions/relative-atiyah-detectors/PROOF.md), especially §1. This is an explicit theorem dependency; the two draft PRs are independently based on main.

- [Public target comment 6260505511](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6260505511), updated 2026-10-19T05:39:56Z; retrieved body SHA-256 `cb1abdf695b12b3ddcdc8f4d040fefd573ae6a8373e47cdb9186769823122d2b`.
- [Public target comment 6260407782](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6260407782), updated 2026-10-19T05:31:48Z; retrieved body SHA-256 `28117d05632973754efc7ed41819a904ed71f4c620dbb3e46df69632f1890e03`.

# Current independent mathematical review: S320

Review date: 2026-10-20.

**PASS within the stated hypotheses and bounded scope.** This review covers the complete proof, historical audit, dependencies, and current-scope text. It checks the mathematical argument and directly cited public prerequisites; it is not formal verification or an evaluation of an actual HM/source instance.

## 2. S320: target-relative Atiyah rank zero

The intrinsic identity

    tf(α²)=c₁(H)α₀

is valid. Before End multiplication, the cohomological degree-one interchange and the exterior-form interchange cancel; the End₀ coefficient factors are symmetric. Their product has zero trace-free part because `uv+vu=tr(uv)Id` in rank two. Equivalently, curvature entries have even total degree and obey Cayley–Hamilton. Taking traces supplies

    α²−c₁(H)α+c₂(H)Id=0.

This is a class identity, not an assertion about uncorrected Čech products.

For a global bivector with twist `−a`, contraction of `c₁(H)α₀` factors through `H¹(T_P⁴(−a))`. The twisted Euler sequence and the absence of intermediate line-bundle cohomology on P⁴ make this group zero for every integer `a`. The scalar contraction lies in `H²(O(−a))=0`. Hence both displayed maps, and indeed the same maps at every integer twist for any rank-two bundle on P⁴, are zero.

The Serre-dual description of the retained maps is compatible with the full-deck volume character and the sign self-duality of `[22]`. Pulled-back coefficient multiplication acts componentwise under an O-linear splitting of `σ_*O_Y`; an algebra splitting is unnecessary.

More decisively, the full-deck cotangent target is

    H³(Y,σ*Ω¹_P⁴⊗L⁻²).

The pulled-back twisted Euler sequence has middle and right terms `5L⁻³` and `L⁻²`. Künneth on `(P¹)⁴` puts their cohomology only in degree four, so this H³ group vanishes. The full-deck part of `H²(O_X)` also vanishes. Taking trace after multiplying Cayley–Hamilton by an arbitrary full-deck `z` gives

    τ_rel,2(z)=f*c₁(H)τ_rel,1(z)−f*c₂(H)tr(z)=0.

Thus the first and second target-relative maps vanish on the **entire** full-deck sector, not merely its retained part. The dimensions 352, 176, 30, and 12 are descriptive inputs, not necessities for this zero proof.

The optional inversion arithmetic is consistent: the source bivector spaces have positive dimensions 21 and 4; the relevant H² targets have positive dimensions 4 and 8; the componentwise bound is `min(21,4)+min(4,8)=8`. This does not supersede or weaken the proved zero map.

**Accepted conclusion:** rank zero is the controlling theorem. No actual-source membership, scalar/jet-detector identification, or obstruction vanishing is inferred.

## Reviewed file SHA-256 bindings

The four files below are the exact texts reviewed before this review was added.

- `AUDIT.md`: `fd6059c07757a0535b8ac7d01e881658140e7d924ec928eef02138389cbdd432`
- `DEPENDENCIES.md`: `59e63f6980a9a1c3e984123be37a6c2f5eb927b01840f90624ad1b5187e7908a`
- `PROOF.md`: `09903a81c574a3e29a1975804ce55f305fd75764072172bdefc7826789621ac6`
- `SCOPE.md`: `7827ba2c9ab65b5ba5c8068f7ce953040c214b4fb4fda0242c3d4dd10668852d`

## Immutable public prerequisites

- [coefficient: PR179, 2b03992b32d2f5cf0509b6f4840adf08369f54b7](https://github.com/Akilleez-QA/read-em-and-weep/blob/2b03992b32d2f5cf0509b6f4840adf08369f54b7/research/hm/cubic-loci/foundation-p01/COEFFICIENT-FAMILY.md): Coefficient family and equivariant Kodaira–Spencer isomorphism.
- [cohomology: PR179, 2b03992b32d2f5cf0509b6f4840adf08369f54b7](https://github.com/Akilleez-QA/read-em-and-weep/blob/2b03992b32d2f5cf0509b6f4840adf08369f54b7/research/hm/cubic-loci/foundation-p01/INVARIANT-COHOMOLOGY.md): Classical invariant cohomology and representation hypotheses.
- [eigenspaces: PR183, cedeed5ce96ebc7fc045c47750c9e29add3e55ad](https://github.com/Akilleez-QA/read-em-and-weep/blob/cedeed5ce96ebc7fc045c47750c9e29add3e55ad/research/hm/cubic-loci/foundation-p03/INVERSION-EIGENSPACES.md): Sections 1–5 establish character conventions and the retained (12,18) dimensions. Original later sections are not required for the trace-map zero theorem.
- [retained: PR183, cedeed5ce96ebc7fc045c47750c9e29add3e55ad](https://github.com/Akilleez-QA/read-em-and-weep/blob/cedeed5ce96ebc7fc045c47750c9e29add3e55ad/research/hm/cubic-loci/foundation-p03/RETAINED-SECTOR.md): Abstract retained sector and its explicit source-matching restriction; actual membership is not inferred from symmetry alone.

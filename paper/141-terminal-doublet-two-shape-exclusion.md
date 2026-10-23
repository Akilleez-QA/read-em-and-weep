# 141. Two actual quotient shapes excluded by a terminal doublet

**Craig Ward · 23 October 2026 · New all-source exclusions for backward plateau length one; profile (1,1) remains open**

## New result and precise scope

The [terminal-doublet theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/69d4f410bcacab23ab4704ac20ec80e34fcc179b/research/hm/doublet-endpoint-exclusions/PROOF.md) excludes both actual Gauss quotient shapes

    A = W′ O(-1) + O(4),
    A = W′ O(-1) + O(10).

It applies to all four necessary actual primary source types when the derivative has rank three and the backward plateau length is k=1. Thus it applies in maximal profile (1,1), independently of the dual quotient B and determinant defect. The forward length l=1 is not needed. These are actual-map exclusions, unlike the preceding universal criteria alone.

This does not close profile (1,1), prove other-profile exhaustion, exclude rank three globally, or complete the original proof repair. Profiles (1,2) and (2,1) remain excluded under their pinned necessity theorems. [Chapter 140](140-p-type-cubic-euler-image.md) and all earlier snapshots are preserved.

## How the source-conditioned certificate led here

The [P-source certificate, PR1155](https://github.com/Akilleez-QA/read-em-and-weep/blob/076d2fb4e6abec42bd365bb32318b89d8ece400f/research/hm/p-type-target-certificate/PROOF.md) reads the fixed original 159 records without regenerating them. Thirty-five pass its P-source cohomology tests. Its six Hom-zero quartic rejections all overlap earlier PR1140 rejections: **zero incremental exclusions** arise from that Hom filter. Nineteen pass the specified tests, not necessarily every known condition.

The useful new constraint was instead that eight of those nineteen historical records have a nongenuine quartic envelope. Under the P-source hypothesis their cubic kernel therefore cannot vanish, and the actual top row must factor through the Euler doublet. Those eight records represent four A shapes. This is a forced actual-map condition, not realization and not a live frontier count. The new endpoint argument now excludes the two shapes displayed above for every actual source, rather than counting the old overlapping Hom rejections again.

The certificate also gives deg A≥0 for any actual rank-three P-source quotient, and deg A≥2 when its cubic kernel vanishes. Its three historical degree rejections already overlap PR1140. None is counted again here.

## Actual geometry and the endpoint rank bound

Work on the physical binary-icosahedral line over C. The actual saturated bundle E has rank 17 and degree -54 in a constant ambient of dimension 30. Set

    K = E⁻ = ker β_E,      A = E/K.

A is the locally free quotient, not the saturation of its derivative image. The dimension-54 coefficient presentation is not this Gauss ambient. The plateau convention places E at F_k and its kernel at F_(k−1). When k=1, K=F_0 is the lower endpoint, whose derivative has rank at most two. This bound concerns β_K; no bound on every later derivative is assumed.

All derivative maps used below are induced by the actual constant inclusion. Equivariant bundle splittings are not assumed horizontal. K and its successive Gauss kernels are saturated in that same ambient.

## First reduction: cubic vanishing is impossible, leaving only P

The four necessary sources, denoted D, P, V and Z, have common quartic Euler character

    χ_G(E(4)) = 3V + 3P + 2D.

Their possible cubic kernel characters H0(K(3)) are respectively 0 or S, 0 or W′, 0, and 0. If the cubic kernel vanishes, strict-top and the actual derivative injection imply that

    C(A) = H0(A(2)) + χ_G(A(4)) − (3V+3P+2D)

is genuine. For the two proposed targets the exact characters are

    e=4:    C(A) = −V,
    e=10:   C(A) = 1 + 2A_std + D − V.

Both contradict genuineness. This immediately eliminates V and Z. In the D source, a nonzero cubic kernel forces an actual map O(2)→A. Degree excludes its doublet component; its scalar component requires invariants in Sym²W or Sym⁸W, neither of which has any. D is therefore impossible as well.

Only P could remain, necessarily with H0(K(3))=W′. The actual Euler factorization of chapter 140 is consistent with this reduction, but the endpoint proof below does not require an additional assertion about the full scalar row of the primary map.

## General terminal-doublet lemma: the scalar degree must be at least 14

More generally, assume rank A=3, rank β_K≤2,

    A = W′ O(-1) + O(e),      H0(K(3)) = W′,

and W′ is absent from Sym^(e+1)W. A negative symmetric exponent contributes zero. These explicit hypotheses imply e≥14.

Strict-top for E gives maxdeg K≤-3. Its cubic character identifies its complete top block C=W′ O(-3), with an abstract lower complement having all degrees at most -4. The actual derivative of K lands in

    A(-2) = W′ O(-3) + O(e−2).

The scalar component on C vanishes by the stated Hom hypothesis. Its doublet component is a scalar by Schur's lemma and cannot be zero: otherwise strict-top for K would be violated by a killed degree -3 block. Hence C maps isomorphically onto the displayed W′ O(-3).

The endpoint rank bound is at most two, and this full rank-two summand is already in the image. The remaining scalar projection of β_K must therefore vanish generically, hence everywhere. Its coherent image is exactly W′ O(-3), not merely a subsheaf of it with a divisor defect. Thus

    0 → K⁻ → K → W′ O(-3) → 0

is split as bundles, and every degree of K⁻ is at most -4. This particular image is saturated because it equals a displayed direct summand. The bundle right inverse is not asserted horizontal.

The next actual derivative lands in

    (K/K⁻)(-2) = W′ O(-5).

A degree -4 block of K⁻ would have zero map to that target by degree. Strict-top applied to K⁻ forbids such a killed top block. Every degree of K⁻ is consequently at most -5. No rank condition on this next derivative is used.

Finally,

    rank K⁻ = 12,      deg K⁻ = −46−e.

Twelve degrees at most -5 sum to at most -60. Therefore -46−e≤-60, which forces **e≥14**. For e=4 and e=10, the required Hom vanishings hold because Sym⁵W=T and Sym¹¹W=W+S+T contain no W′. The residual degrees would be -50 and -56, respectively, contradicting the bound -60. This completes both exclusions.

The general numerical conclusion is conditional on the displayed hypotheses. It is not an unconditional exclusion of every scalar degree below 14, nor a claim that degree 14 or larger is realizable.

## Historical identifiers, verification and remaining boundary

In the immutable original profile-(1,1) list, the first shape has zero-based identifiers 86, 87, 88, 89 and 96; the second has identifier 116. These are provenance labels, not six newly counted live cases or a present frontier denominator. The proof is independent of B and defect and does not need a new enumeration.

The endpoint proof has SHA256 `925293b6211d0ad6aa55b62d6de07da78a7509017cab89486791c2bf49e27eb1`. Independent written review checked the endpoint direction, all four source reductions, exact image and saturation argument, second strict-top step and degree contradiction. Ten author inputs and eleven independent originals were freshly authenticated. The author verifier passes 400 explicit controls plus 81 module controls; the independent checker passes 1,601. Normal and optimized Python outputs match the frozen results.

For the preceding certificate, the corresponding totals are 559 explicit author checks plus 81 module controls and 2,509 independent checks, with seven author inputs and eight independent originals. These exact algebra controls support the written geometric arguments; neither packet is proof-assistant verification of the complete dependency graph.

No actual source coefficient, selected parameter, point, jet, matrix or instance-rank experiment was evaluated. No stopped spike was restarted. The full profile-(1,1) closure, broader coverage and original repair remain open. Chapter 140 and the delivered v0.3 PDF remain unchanged historical snapshots.

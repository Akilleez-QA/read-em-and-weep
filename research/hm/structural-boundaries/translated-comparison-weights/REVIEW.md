# Independent geometric and domain review

## Verdict and exact theorem

Accept the polynomial partition-extension and bounded regular comparison/variation theorem at the proof hash recorded below. The proof is conditional on the original complete tagged carrier/mask cover and on any fixed collection of polynomial original witnesses satisfying its partition identities. It does not identify those chosen witnesses with a prescribed solver output.

Reviewed proof SHA256: e1bfa7e72d21cc4892cb9e2ae130214d54b1c1810aaa978062bf40a5e1d1f967.

For each original standard chart, the family has polynomial weights over k[s] that agree exactly with the fixed original weights at s=0. Full occurrence-weighting defines a regular cochain comparison on the explicitly specified family bounded source complex. Its covariant parameter variation is regular on the stated enlarged bounded domain and retains every weight derivative. The theorem does not assert that an arbitrary actual moving source belongs to either domain.

## Independent geometric checks

1. The homogeneous legal pair is Y and (X−sY)((X−sY)^2−Y^2). It covers the entire parameterized projective line: at Y=0 the second section is X^3. On the inverse-x chart its representatives are t and AB, not t and B. The factor A is essential at shifted z=0. At A=0 or B=0 the bit-one open is excluded; t is nonzero there, so the bit-zero open covers. At infinity t=0, A=B=1 and bit one covers.
2. The carrier map uses the coefficients of a product of four nonzero binary linear forms. Its coefficient vector cannot vanish at any geometric point. The original five carriers v_j^5−product(v_r), together with the auxiliary v_0v_1v_3v_4, have no simultaneous zero: if the product vanishes, all five v_j would vanish; otherwise the auxiliary is nonzero. This works over every residue field. Combining independently covering carriers and all legal masks, while retaining each standard tag, gives the required family cover. It would not justify a reduced owner list.
3. Positive powers preserve principal opens. Thus the family polynomials C_o generate the unit ideal in the entire polynomial ring k[s,t_1,...,t_4], not merely in its generic fiber or its fraction field. The geometric-zero argument and faithful-flat descent are legitimate. No parameter denominator is introduced.
4. If a Bezout vector R exists over this ring, e=1−sum C Q^0 and Q=Q^0+eR give sum C Q=1 and Q(0)=Q^0. This simultaneously proves the partition identity and its exact prescribed central specialization. It imposes no degree bound on the witnesses and computes none.

## Domain and differentiation checks

The original draft's cochain-map claim needed an explicit regular domain: unit-sum alone does not regularize arbitrary source cochains. The final version names its family bounded complex and whole tagged standard targets. Each source occurrence contributes its own clearing factor; all original tags and repeated occurrences are retained. Dividing an occurrence's weight by its own bounded clearer gives a polynomial on its own chart. Multiplication by the cleared section therefore extends over the entire intended target. Face deletion supplies the missing clearer and proves that the source domain is a complex. Summing the absent face occurrence's weight gives one and proves the cochain identity in all degrees, without assuming closed inputs.

The scalar derivation is regular on each polynomial chart: ∂s+∂x in the shifted finite coordinate and ∂s−t²∂t in its inverse. Applying the product rule to C=H^54 product L^29 proves simultaneous product divisibility by H^53 product L^28, not merely separate informal pole bounds. The term C sigma(Q) has stronger divisibility. This is owned by the differentiated occurrence, regardless of repeated physical divisor labels.

For a line coefficient with f_infinity=t^n f_finite, the operator ∇_infinity=∂s−t²∂t+n t satisfies ∇_infinity(t^n f_finite)=t^n∇_finite(f_finite). Thus the lift is genuinely compatible with line transitions, restrictions and the Cech differential. Differentiating an own-cleared section raises the per-occurrence allowance from16/10 to17/11. The same weights define comparison on the enlarged domain. The difference ∇Π−Π∇ consists of the complete Leibniz sum of one differentiated weight at each occurrence. Its53/28 allowance clears16/10; undifferentiated54/29 clears17/11. No weight or chart-frame contribution is omitted.

For the canonical coefficient line O(−2,−2,−2,−2), the infinity lift contains −2t. This agrees with the moving odd basis u=y/x², sigma(u)=−2tu. It is not naive commutation of coefficient-only differentiation and infinity extraction. Formula specialization is sufficient; an unproved identification of every central bounded cochain with a specialization of a family cochain is not needed.

## Shifted connection and exceptional loci

Using V(t)=−u, A=1−st and B=A²−t² gives

    rho_0=−u/(2t),
    rho_1=u[sA²+t(1+A)]/(2AB),
    alpha_1=ut/(AB),
    beta_0=u/(2t),
    beta_1=−su/(2A).

These follow by differentiating the actual normalized root squares t and B/A. In particular the shifted bit-one beta is not identically zero. The corresponding coefficients have at most one owned legal factor in the denominator: t for bit zero and AB for bit one. At infinity the bit-one denominators are units. The finite chart remains necessary where x=0; inverse-x does not cover the whole shifted bit-one open. No globally regular square-root function or global flat connection on the positive-degree root line has been assumed. The local check does not establish all primitive/source pole certificates.

## Provenance and novelty boundary

Read-only GitHub inspection on2026-10-18 confirmed null/spike-support-certificates at89be39dc4d0d93c502110f435b6c8d7f7eb77203 and read PR1 comment6250948832 and the root-line proof at that immutable commit. PR1 is the coordination thread, not that source branch: its head was2531056eae05fdf31e8fb4ca3affc5907073ad73, while main wasfd4aeeb2ee4fc729c18d98444fed42fd0529eeeb. The inspected coordination statement leaves a separately specified compatible parameter family open; it does not already prove the present exact polynomial partition extension.

The present contribution is additional to the restored fixed-source comparison and translated background-source family. This is a comparison against the inspected dependencies, not a claim of an exhaustive literature or repository novelty search.

Inspected local mathematical dependencies:

- compatible-translation-family-20261018/PROOF.md (its final hash is recorded separately in that packet).
- regular-source-cover-comparison-20261018/PROOF.md, SHA2561a4d478d18f564a50f4ccb82bcbdf39461da48b30e4998869a612a024a69b607.
- weighted-jet-flux-domain-20261018/PROOF.md, SHA25651697dccc19b5632b06a3d3393640d2fe585287898a23dd8e319ab8618182fa9.

This independent review used structural geometric reasoning, read-only source/dependency inspection, and byte hashing. No source/model/matrix/polynomial instance, point, jet, residual, detector or Bezout witness was evaluated. No checker was rerun; no executable cutoff or terminal is certified.

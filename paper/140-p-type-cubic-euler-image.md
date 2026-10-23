# 140. The actual P-type cubic kernel and its Euler image

**Craig Ward · 23 October 2026 · Independently reviewed necessary-condition theorem; no new target exclusion**

## Checkpoint and source

The [revised P-type cubic-image proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/4b97c71dace666dd5bf39e0128abbe7b01a2f056/research/hm/p-type-cubic-image/PROOF.md) characterizes the sole possible nonzero cubic kernel for the actual P-type Gauss map. It gives an if-and-only-if factorization of its top row, exact coherent-image and restricted-kernel alternatives, and a stronger quartic representation test. It does not exclude another actual quotient shape or close profile (1,1).

This is separate from [chapter 139's sextic-channel classification](139-complete-sextic-channel-classification.md), which remains unchanged. The last recorded actual profile-(1,1) shape exclusion is [PR1145](https://github.com/Akilleez-QA/read-em-and-weep/pull/1145), summarized in [chapter 137](137-cubic-visibility-and-ambient-reduction.md). Profiles (1,2) and (2,1) are excluded under their pinned necessity theorems; profile (1,1), other-profile exhaustion and the original repair remain open.

## Actual source and kernel

On the physical binary-icosahedral line, take the actual saturated inclusion E into the constant thirty-dimensional plane-section bundle H O, with

    E = P O(-2) + (W′+T) O(-3) + V O(-4) + W′ O(-5).
    β_E : E → (H O/E)(-2),     K = ker β_E,     A = E/K.

Here dim(P,W′,T,V)=(4,2,6,3), P=W′⊗W, and W is the standard doublet. The ambient is H of dimension 30, not the dimension-54 coefficient presentation. K is the actual Gauss kernel. A is its locally free quotient, not the saturation of the derivative image. Neither K nor its restricted top-row kernel below is identified with a canonical complement from a presentation or a chosen splitting. An equivariant Birkhoff splitting is not assumed horizontal or compatible with differentiation.

The theorem assumes this actual source and embedding. It assumes no rank for β_E or its next derivative and does not derive the source hypotheses from a historical enumeration.

## Nonzero cubic kernel if and only if the actual top row factors

The pinned cubic visibility theorem gives H0(K(3)) equal to zero or one W′, with two independent T channels in the quotient. The new argument locates that possible W′ entirely in the top block F=P O(-2).

Indeed, a nonzero projection of the kernel onto the displayed W′ O(-3) would be an isomorphism on its coefficient representation. Evaluation would give a saturated graph W′ O(-3) inside E, killed by the actual Gauss map, whose quotient retains maximal degree at most -2. Its derivative must then vanish by a Hom-degree calculation. A saturated negative-degree horizontal subbundle in a constant bundle is impossible. This rules out mixed cancellation between the top and displayed W′ copies, without assuming the projections horizontal.

The unique top W′ evaluates to the saturated Euler inclusion

    0 → W′ O(-3) --j--> P O(-2) --q--> W′ O(-1) → 0.

Consequently,

    H0(K(3)) ≠ 0   ⇔   the actual row F → A factors as f q.

In this alternative H0(K(3))=W′ and the factor f:W′ O(-1)→A is nonzero. The factor is unique for the fixed quotient q. Conversely, factoring the actual row kills j, so its cubic coefficient kernel is nonzero. The mere existence of some nonzero equivariant Hom into A does not establish this factorization or show that the alternative occurs.

## Coherent images and exact restricted top kernels

Let I=im(f) be the coherent image in A, and K_F=ker(F→A). The image is locally free because it is torsion-free on the smooth curve. There are exactly two necessary alternatives:

| Rank of I | Coherent image | Restricted top-row kernel K_F |
| --- | --- | --- |
| 2 | W′ O(-1) | j(W′ O(-3)) |
| 1 | O(e), with e even and e≥6 | Equivariantly isomorphic to W′ O(-3)+O(-e-2) |

These are coherent images, not their saturations in A. In rank two the factor is a sheaf injection, but need not be saturated. In rank one, the first occurrence of W′ in Sym^n W is n=7, forcing e≥6; central parity forces e even. Thus maxdeg A≤5 rules out the line-image alternative.

For the rank-one kernel, the surjection W′ O(-1)→O(e) has kernel O(-e-2). Its pullback through q gives an extension by W′ O(-3). The extension group is W′⊗H1(O(e-1))=0. Averaging a splitting makes it equivariant. This splitting is noncanonical and is not asserted horizontal. K_F is only the kernel of the restricted top row, not the entire K. The alternatives are necessary conclusions, not claims of actual realizability.

## Hom criterion and tightened quartic envelope

For any actual target A satisfying

    Hom_G(W′ O(-1), A) = 0,

the forced factor cannot exist, hence H0(K(3))=0. There is no upper-degree assumption on A in this criterion. The vanishing implies maxdeg K≤-4. Strict-top applied to the saturated actual K makes its own Gauss kernel have maximal degree at most -5. The actual derivative of K lands in A(-2), giving

    H0(K(4)) ↪ H0(A(2)).

Euler additivity then proves that

    H0(A(2)) + χ_G(A(4)) − (3V+3P+2D)

is a genuine representation. Here χ_G(E(4))=3V+3P+2D. More explicitly, the displayed character is

    [H0(A(2)) − H0(K(4))] + H1(K(4)).

There is no additional H0(A) error term. Euler characteristic must not be replaced by H0 when a negative summand contributes H1. The same tightened envelope holds if cubic-kernel vanishing is established by another argument.

## Verification and remaining work

The revised proof has SHA256 `4b68be856e9504b38bf21dcab29c73a70a6a9065d0281b726360fd2f5ad58091`. Independent written review checked the actual graph argument, the factorization converse, both coherent-image alternatives, the parity and extension calculation, and the quartic injection. Five complete immutable source files were authenticated. The supplied verifier passes 142 explicit checks plus 81 character-module tensor identities; the independent checker passes 682 exact controls. Normal and optimized Python outputs agree. These are universal algebra controls supporting a written proof, not proof-assistant verification of the geometry.

No actual source coefficients, parameters, points, jets, matrices or instance ranks were evaluated. No historical enumeration was rerun and no new live case count is asserted. Applying this criterion to a complete current actual-target frontier remains separate work. Chapter 139 and earlier chapters remain frozen; the delivered v0.3 PDF remains the historical 19:16 UTC snapshot through PR1117.

# Preserved mathematical audit

This review concerns the source manuscript and its stated assumptions. It is preserved as mathematical history, not a new independent certification of all publication edits or of unpublished input theorems. Source and publication hashes are recorded in SOURCE-HASHES.json. A split manuscript’s module or polar application remains conditional in its destination unit.

# Independent audit: fourth-power obstruction cohomology

## Verdict

The supplied fourth-power sheaf identification yields an exact, useful cohomological criterion, but does not prove vanishing of its second cohomology or determine its image in the ten-dimensional unrestricted target. In particular, the suggested auxiliary vanishing H³(B0(−9))=0 is false: its dimension is at least 85.

This audit assumes the established sheaf identification and its complete-intersection resolution in PROOF.md. It independently checks Riemann–Roch, duality, the exact-map criterion, and the limits of their consequences. No source or multiplication-rank evaluation is performed.

## 1. Normalization and primary cohomological input

Work over C on P⁴. Let F be the normalized stable rank-two Horrocks–Mumford bundle, with c₁(F)=−H and c₂(F)=4H², and let B0=End₀(F). The trace pairing identifies B0 with its dual. Since the characteristic is zero, End(F)=O⊕B0; intermediate cohomology of every O(t) on P⁴ vanishes.

The primary theorem used here is Decker–Schreyer, *Pullbacks of the Horrocks–Mumford bundle*, J. reine angew. Math. 382 (1987), 215–220, the unnumbered proposition on printed p.218:

    H¹(P⁴,End(F)(k))=0 for all k≤−2.

Hence H¹(B0(k))=0 in that range. The local verification record hm_primary_source_verification.md records the visual check, the complex ground field, normalization and proof context. This audit relies on that verified primary-source transcription, rather than claiming a new browser retrieval.

Primary page: https://gdz.sub.uni-goettingen.de/id/PPN243919689_0382?tify=%7B%22pages%22%3A%5B222%5D%2C%22view%22%3A%22info%22%7D

Catalog: https://eudml.org/doc/152990

Stability of F gives Hom(F,F(k))=0 for k<0 by the slope inequality, so H⁰(B0(k))=0 for k<0. This does not require asserting stability of B0 itself.

## 2. Independent Riemann–Roch check

Write the formal Chern roots of F as a,b. Then d=a−b satisfies

    d²=(a+b)²−4ab=−15H².

The roots of B0 are 0,d,−d. Therefore, truncating above degree four,

    ch(B0)=1+exp(d)+exp(−d)=3−15H²+(75/4)H⁴.

The relevant Todd coefficients of P⁴ are td₁=5H/2 and td₂=35H²/12. Using χ(O(t))=binom(t+4,4), the polynomial Euler characteristic is

    χ(B0(t))
      =3 binom(t+4,4)−15(t²/2+5t/2+35/12)+75/4
      =3 binom(t+4,4)−(15/2)t²−(75/2)t−25.

At t=4 this is 210−120−150−25=−85.

Serre duality, with canonical bundle O(−5), gives

    H³(B0(4))=H¹(B0(−9))*=0,
    H⁴(B0(4))=H⁰(B0(−9))*=0.

Consequently

    h¹(B0(4))=h⁰(B0(4))+h²(B0(4))+85≥85,
    h³(B0(−9))=h¹(B0(4))≥85.

No vanishing of H⁰ or H² at positive twists is used. Equality with 85 is not established. The lower bound alone rules out the proposed H³(B0(−9)) vanishing.

## 3. Exact unknown-map criterion

Put

    A=B0(−9),
    B=B0(−6)⊕B0(−7),
    K=B0(−4)⊗I_N.

The established Koszul sequence is

    0→A --α--> B→K→0,
    α(c)=(−t₃c,t₂c).

Its long exact cohomology sequence gives canonically

    0→coker(H²(α))→H²(K)→ker(H³(α))→0.

In particular H²(K)=0 holds if and only if H²(α) is surjective and H³(α) is injective. Nonvanishing of H³(A) by itself does not imply that its map has a kernel.

Under the trace pairing and Serre duality, the transpose of Hʲ(α) is multiplication

    m_(4−j): H^(4−j)(B0(1))⊕H^(4−j)(B0(2))
               →H^(4−j)(B0(4)),
    (u,v)↦−t₃u+t₂v.

Changing the overall sign gives the equally valid convention t₃u−t₂v. Kernels, cokernels and ranks are identical under this convention change. Thus dualizing the displayed short exact sequence yields

    0→coker(m₁)→H²(K)*→ker(m₂)→0.

Equivalently,

    h²(K)=dim coker(m₁)+dim ker(m₂),

and

    H²(K)=0 ⇔ m₁ is surjective and m₂ is injective.

This is an exact criterion, not a rank computation. The Riemann–Roch lower bound makes the target of m₁ at least 85-dimensional; it proves neither failure nor success of surjectivity. The individual positive-twist cohomology dimensions and multiplication maps remain unevaluated.

## 4. The target image and actual source remain separate questions

Let T=B0(−4). The restriction sequence is

    0→K→T→T|_N→0.

Therefore the image of H²(K) in the admitted ten-dimensional H²(T) is exactly

    ker[H²(T)→H²(T|_N)].

Neither this kernel nor the particular source class is determined by the preceding calculation. Even knowing H²(K)≠0 would not show that its map to H²(T) has a nonzero image; conversely a nonzero domain does not exclude its image being the entire ten-space.

At the sheaf/cochain level the fourth-power condition is that the descended coefficient lie in I_N. For a cohomology class, being representable by a closed K-valued cochain is equivalent to belonging to the displayed image. This distinction matters: failure of a chosen representative to lie in K need not preclude a cohomologous K-valued representative. The actual source's fourth-power membership, the existence of such a representative, the target image, and the value of the obstruction all remain unresolved.

## Scope

This audit makes no positive-twist vanishing assumption, computes no actual source, ranks, specializations or pairings, and performs no external write or large computation. Its only local output is this review. The inherited ten-dimensional target and sheaf identities retain the hypothesis and provenance scope of PROOF.md and the cited weighted Koszul proof.

## Addendum: review of the developed dual-boundary criterion

I also read ../fourth-power-cohomology/PROOF.md in full after writing the preceding independent derivation. Its refined target-image criterion passes this audit:

- Since N is a degree-(2,3) projective complete intersection, its dualizing sheaf is O_N and Gorenstein Serre duality applies even at its singularities.
- Duality identifies the transpose of restriction r with the two-step Koszul connecting map δ_N:H⁰(N,B0(4)|_N)→H²(B0(−1)), up to the harmless scalar choice of adjunction orientation. The resolved sheaf is B0(4)|_N, with Koszul terms B0(−1), B0(2)⊕B0(1), B0(4), so all twists check.
- Consequently the fourth-power target image is (im δ_N)^⊥, of dimension 10−rank δ_N. This is a criterion, not a determination of that rank.
- The stated secondary map σ:V→Q is well defined: changing a lift from H²(B0(−1)) to H¹(B0(4)I_N) changes its image in H¹(B0(4)) by the image of H¹(B0(2)⊕B0(1)). The proof that im δ_N=ker σ is exact in both directions.
- The conditional simplification when the two positive H² groups vanish is correctly labelled conditional. It is not used to obtain an unconditional rank, vanishing, or source-membership conclusion.

Thus the refined criterion is compatible with, and strictly more explicit than, the restriction-kernel formulation above. No mathematical correction is required to the developed proof as read.

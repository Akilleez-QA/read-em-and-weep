# Inputs and dependency boundary

Let F be the normalized Horrocks–Mumford rank-two vector bundle on complex P⁴, with c₁(F)=−H and c₂(F)=4H². The proof uses only these Chern classes and H⁰(F(u))=0 for u<3; it does not use a prior unpublished result about End(F).

## Primary source and normalization

Wolfram Decker, *Monads and cohomology modules of rank 2 vector bundles*, Compositio Mathematica 76 (1990), 7–17.

- [Stable bibliographic record](https://www.numdam.org/item/CM_1990__76_1-2_7_0/)
- [Primary PDF](https://www.numdam.org/article/CM_1990__76_1-2_7_0.pdf)

Printed page 13 specifies the normalization c₁(F)=−1. Printed pages 14–15 identify the section-module resolution and relate its terms to the H¹-module resolution; printed page 16 gives the shifts. With S=C[x₀,…,x₄] and M=⊕ᵤ H⁰(P⁴,F(u)), the resulting graded resolution is

    0 → 2S(−8) → 20S(−6) → 35S(−5)
      → 15S(−4) ⊕ 4S(−3) → M → 0.

The rightmost free module has zero degree-u component for u<3, and its graded surjection onto M proves the needed vanishing. This is a section-module statement, not an inference of surjectivity on sections from a sheaf surjection.

## Standard geometric tools used in the proof

The depth lemma and the S₂ criterion for reflexivity; rank-one reflexive sheaves and Weil divisor classes on a normal variety; localization of divisor class groups; the projective-bundle Picard formula; finite pushforward and the projection formula; Riemann–Roch on P²; Künneth cohomology on P¹×P¹; and the local-cohomology depth criterion. Their specific applications are written out in PROOF.md and checked in AUDIT.md.

## No missing theorem dependency

The argument does not assume an endomorphism cohomology table, tensor-product semistability, classification of MCM modules, or another research-branch result. Higher-twist and h¹ consequences are deliberately omitted.

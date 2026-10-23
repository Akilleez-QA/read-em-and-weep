# Forced A normalization and an actual two-T6-source presentation

Work over C on the negative parameter line T=P(W*) with the current G=2I representations and standard linearizations. No selected actual coefficient, point, parameter, jet, derivative, matrix or instance rank is evaluated.

## 1. Immutable interfaces and statement

INPUTS.json pins the exact originals:

- BRANCHES: PR1009, commit0d75f42c4e79654c8fbef57e6ce56a1f06cdf9a1, research/hm/common-target-branches/PROOF.md. After the expressly permitted choices of complements it gives actual fiberwise-injective presentations

      0→L⊕S O(-1)⊕E14 O(-1)→R24 O→Fout→0,
      E14=W'⊕2T6,
      R24=A⊕V⊕2P⊕2D,

  where (L,Fout)=(W O(-3),Q) if λ≠0, and (A O(-2),Q3) if λ=0. Every splitting degree of Q is at least two; every degree of Q3 is greater than two.
- WEIGHTED: PR1012, commitd2066ed6744c059bd30de49bdeb8f14f37ecb1fb, research/hm/weighted-source-block/PROOF.md. It supplies the forced independent D coefficient directions d and v of L and the unique S O(-1) source. It also proves that the allowed changes of the weighted-source complement form a one-dimensional space through S, by multiplication by l² or l. The actual D channels are multiplication by l³ or l² for L, and by l for S.

We prove that S→A is forced nonzero, and uniquely normalize the weighted complement so its A component vanishes. Eliminating the resulting actual subbundles yields

    λ≠0: 0→(2T6) O(-1)→Z16→Q→0,
    Z16≅(V⊕P) O⊕W' O(1)⊕S O(1)⊕A O(2),        (1)

    λ=0: 0→(2T6) O(-1)→Z15→Q3→0,
    Z15≅(V⊕P) O⊕W' O(1)⊕S O(1)⊕W O(3).        (2)

Both actual target bundles have degree12. The actual source maps inject on every fiber. Every map is inherited from the fixed original presentation; the displayed identifications with named representations and split models are not asserted independent of the earlier complement choices. No value of λ is chosen.

## 2. Force the S-to-A component

Only L and S O(-1) can map to the A target. Indeed Hom_G(E14 O(-1),A O)=Hom_G(E14,A⊗W)=0, since A⊗W=W⊕S. Let β be the S-to-A map. It is a scalar multiple of the universal contraction

    S O(-1)→A O,

whose kernel is the cube of the tautological kernel line, O(-4).

Suppose β=0. Then the A projection receives only the weighted A map α. If α=0, the cokernel Fout would surject onto A O, impossible by its positive splitting degrees. If α≠0, WEIGHTED's universal descriptions give the following saturated images:

- For L=W O(-3), α(v)=det(v,l)l² has image the Veronese line O(-2)⊂A O. Its cokernel is W O(1), by the universal sequence 0→O(-2)→A O→W O(1)→0.
- For L=A O(-2), α(f) is l times the contraction of f by l. Its image is lW, the subbundle W O(-1)⊂A O; its cokernel is O(2), by 0→W O(-1)→A O→O(2)→0.

Projection onto A modulo these images would induce a surjection Q→W O(1) in the first branch or Q3→O(2) in the second. Both Hom spaces are zero by the stated degree bounds. This contradiction proves

    β≠0.                                        (3)

The image and cokernel descriptions are universal identities for an arbitrary tautological line, not selected actual fiber evaluations.

## 3. The unique normalization of the weighted complement

Let δ_l denote contraction using det with the tautological generator l. It satisfies δ_l(l)=0. The unique allowed source shifts L→S O(-1) are

    v↦l²v  for L=W O(-3),
    f↦lf   for L=A O(-2).

Composing with the nonzero S-to-A contraction gives l²δ_l(v) and lδ_l(f), respectively. Each is nonzero and spans the unique weighted A channel. Thus the linear map from the one-dimensional shift space to Hom_G(L,A O) is an isomorphism.

There is consequently a unique allowed shear for which the weighted-source A component is zero. Fix that normalized complement. This uniqueness is relative to the previously fixed target and source data, not an assertion of independence from all earlier choices.

The D coefficient vector changes by a multiple of v. Since d and v were independent, the normalized weighted D direction d0 remains nonzero and independent of v. Therefore the two actual copies D_d0 and D_v give a direct-sum decomposition of the full two-copy D-isotypic target.

## 4. Remove A and both independent D subblocks

After normalization, the A projection receives only β:S O(-1)→A O, which is onto on every fiber. The exact sequence

    0→O(-4)→S O(-1)→A O→0                       (4)

comes from contraction of binary cubics, with kernel l³. Taking the actual kernel of the A projection gives

    0→L⊕O(-4)⊕E14 O(-1)
      →(V⊕2P⊕D_d0⊕D_v) O→Fout→0.             (5)

The normalized weighted source maps only to D_d0, by multiplication by l³ or l². The O(-4) source in (4) maps only to D_v, and its map is multiplication l·l³=l⁴. These are subbundle inclusions into independent constant target summands.

Their universal quotient sequences are

    0→W O(-3)→D O→A O(2)→0,
    0→A O(-2)→D O→W O(3)→0,
    0→O(-4)→D O→S O(1)→0.                       (6)

The first two are the polarized quartic quotient sequences already proved in WEIGHTED. The last is the degree-four contraction sequence: contraction by l is onto Sym³W O(1) and has kernel l⁴. Thus quotienting the actual two subblocks in (5) produces

    0→E14 O(-1)→Y→Fout→0,                       (7)

where

    λ≠0: Y≅(V⊕2P) O⊕A O(2)⊕S O(1),
    λ=0: Y≅(V⊕2P) O⊕W O(3)⊕S O(1).

The direct-sum target construction uses the actual independent D coefficient images; it does not assume that arbitrary extension data vanish. The maps from E14 into its quotient target are retained exactly. Local freeness of Fout makes (7) fiberwise injective.

## 5. The unique W' source is forced into P

Let U'⊂E14 be its unique W'-isotypic subrepresentation. Its map into Y has no component in V O or in any positive target summand. The required fixed character identities are

    V⊗W=T6,
    A⊗S=W⊕S⊕T6,
    S⊗A=W⊕S⊕T6,
    W⊗D=S⊕T6,
    P⊗W=W'⊕T6.

The first four exclude W' from the coefficient spaces for V O, A O(2), S O(1), and W O(3), respectively. The last identifies the only possible target support as the two constant P copies, with a one-dimensional intertwining channel for each copy.

Its P coefficient image is nonzero, since otherwise the rank-two source subbundle U' O(-1) would map to zero, contradicting fiberwise injectivity. It selects an actual copy P_b in the two-copy P-isotypic target. Since P≅W⊗W', the unique channel is the tensor Euler inclusion

    0→W' O(-1)→P_b O→W' O(1)→0.                 (8)

Thus U' O(-1) is a subbundle in that actual target summand. Quotient (7) by this subbundle and use E14/U'≅2T6. The inherited quotient maps give (1) and (2), including their fiberwise injectivity. The remaining P target is the quotient of the constant two-copy P representation by P_b; any named complementary realization is only an isomorphism choice.

## 6. Accounting and contribution

In the nonzero branch the target rank is3+4+2+4+3=16; in the zero branch it is3+4+2+4+2=15. Each has degree2+4+6=12. The source has rank12 and degree−12, so the cokernels have ranks4 or3 and degree24 as required.

The new structural assertions are the nonzero actual S-to-A component, the unique allowed shear eliminating the weighted A component, the resulting simultaneous quotient by the two independent D subblocks, and the forced nonzero W'-to-P component. They produce actual presentations with only two T6 source copies. Optional weighted A-block cases disappear after the justified normalization, rather than being selected by a computation.

The earlier target/source complement choices remain explicit. Neither the scalar λ nor any remaining actual C row, top obstruction rank, vertex scalar or source-frontier case is selected. No prohibited selected evaluations or large scans are used.

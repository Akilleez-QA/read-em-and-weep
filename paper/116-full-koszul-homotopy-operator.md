# The full Koszul-homotopy operator on odd degree three

**23 October 2026 update:** PR1101 now supplies the corrected full-domain identity Θ=aj3+ℓQ3; the warning below against the uncorrected Θ=ℓQ3 remains essential.

**23 October 2026 · PR1096, full proof read**

[Immutable proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/36f7231633a84971dfd865eaf4803727f1edd73d/research/hm/source2-pure-v-full-theta/PROOF.md), blob `24df79d14846fd9d942eae8bb0772b3859f49849`.

## Full domain and canonical images

Under actual source2 pure-V compatible-radical hypotheses, define on all M3

    Θ=X(Id_W⊗h)δ,    δ(z)=x⊗Y_yz−y⊗Y_xz.

Write H=ker Q3, J=ker j3, K=H∩J and F3=W im h. The full operator has

    im Θ=(F3)_T,    rank Θ=12,
    Θ²=j3Θ=Θj3=j3²=0,
    Q3Θ=0,    Θ(F3)=0.

On odd cohomology H, the image L_Θ=Θ(H) is an actual canonical complement:

    (F3)_T=I3 ⊕ L_Θ,    L_Θ≅T.

Both j3 and Θ have rank six on H and common kernel K, but distinct images I3 and L_Θ. These are marked actual image spaces, not chosen multiplicity lines.

## Quotient identity and rank argument

The quotient q:F3→F3/I3 is identified with W⊗P_h by the injective actual first multiplication. The homotopy identities give hY_l(v)−sY_lj3(v)∈I2, hence the full-domain formula

    qΘ=dj3,    d=(Id_W⊗s)δ|I3.

The actual Koszul injection makes d injective into the unique T constituent of W⊗P_h. Thus the quotient image has rank six. Its intersection with I3 is Θ(J)=I3 by the previously proved residual surjectivity, giving full rank twelve. Equivariance rules out a hidden W′ image.

On H, Θ kills K and the quotient identity forces rank six and an image disjoint from I3. This proves the canonical complement without choosing a lift of H/K.

## Two-generator operator structure, not a module extension

For A=C[ε,η]/(ε,η)² acting by j3 and Θ on H, the equivariant isomorphism type is

    H ≅ T⊗A ⊕ (3W′+3S)_trivial.

The isomorphism need not be canonical: its cyclic generator needs a lift. The operators and their two image lines are canonical. The action is faithful; every nonzero scalar combination of j3 and Θ on H has rank six and kernel K. The common operator kernel is K, which is not being identified with the negative-coordinate socle.

The full kernel is ker Θ=J∩Q3⁻¹(C_term), with character 3W′+3S+4T and dimension 42. The formula Θ=ℓQ3 holds **only on J**, not all M3: extending it would incorrectly kill the nonzero Θ(H).

This is an operator structure on degree-three odd cohomology, not a negative-pencil endomorphism, global polynomial-module action, odd nullhomotopy or gate-nonvanishing theorem. Neither terminal incidence, endpoint-sixteen mechanism nor source realization is selected; no positive-map conclusion follows.

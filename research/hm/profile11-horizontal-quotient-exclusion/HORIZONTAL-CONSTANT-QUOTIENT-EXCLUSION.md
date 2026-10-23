# A horizontal projected lattice excludes both cf sources

## Result and immutable inputs

The source tuple (0,0,1,0,0,1,0,1), abbreviated cf, is impossible for both original-zero-defect labels

    G3.11.863639aa192e: A_q=O(-10)+O(4)+O(6),
    G3.11.73682b4c817f: A_q=O(-10)+W O(5).

Its correctly decoded bundle is

    E=(V+P+D) O(-2)+V O(-4)+O(-8)+O(-10).

The same argument also excludes the split-label ce source

    E=(V+2P) O(-2)+V O(-4)+Wp O(-5)+O(-10),

without any invariant-degree calculation. The balanced ce source was already excluded by the quadratic polar obstruction. These are source-stratum exclusions, not whole-label exclusions.

The structural input is PR814, immutable commit 1f94be65b3a470a1b594e61d56df7f6057c9d907, proof SHA256 f0bd13d85ae8a890dbec84e5f15b7ec8605b04f474d5c7d80faeb3aa08f4defc:

https://github.com/Akilleez-QA/read-em-and-weep/blob/1f94be65b3a470a1b594e61d56df7f6057c9d907/research/hm/profile11-low-positive/PROOF.md

Its Sections2-5 establish the onto top maps, exact kernel lists, zero internal derivative, and genuine constant projections used here. The original label/source inputs are pinned in that proof at db51525015bb7c5e825833d550d08dedf6f6ea96. We use the saturated internal/external derivative-image lemma from PR796, Section3:

https://github.com/Akilleez-QA/read-em-and-weep/blob/d2b43060c83328dd5118aee6b9288fcfa0c873ac/research/hm/profile12-quadratic-block-exclusion/PROOF.md

Work over C, with the actual trivial connection on H O over P1. All bundle intersections and images below are sheaf intersections and images in that ambient bundle. No unpublished endpoint or source-exclusion note is a dependency.

## 1. A coherent lattice preserved by differentiation has no divisor defect

Let Q be a finite-dimensional complex vector space, and let N be a coherent locally free subsheaf of Q O on a smooth complex curve. Suppose it has full generic rank dim Q and is preserved by the trivial connection:

    dN subset N tensor Omega^1.                  (1)

Then N=Q O.

To prove this, take determinants. The induced connection preserves det N, a rank-one subsheaf of det Q O. Near any point, choose a local parameter t and a constant volume form. The determinant subsheaf has the form t^m O times that volume, with m>=0. If m>0, its derivative contains m t^(m-1) dt, which is not in t^m O dt, contrary to preservation. Characteristic zero is essential here. Thus m=0 at every point, and the determinant of N->Q O is nowhere zero. A full-rank map between vector bundles with invertible determinant is an isomorphism. This proves the assertion.

In particular, this statement applies to an unsaturated projected image. Preserving the connection forces saturation; saturation is not assumed beforehand.

## 2. The actual full constant spans

Write U for the positive rank-two part of A_q and F=H0(E(2)) O(-2) for the top quadratic block. The pinned proof gives the saturated exact sequence

    0 -> F -> F^+ -> U(2) -> 0,
    F^+ intersect E=F.                           (2)

For cf it gives the actual constant part P O inside F^+ and the projected standard subsystem

    F^+/P O=Sym^9 W O(-1) in (Sym^10 W) O.

Thus the full constant coefficient span C O of F^+ has dimension 4+11=15. The actual bundle F^+ has rank14 and degree-10. In particular C O/F^+ is a line bundle, of degree10.

For split ce the corresponding actual constant part is D O and the projected subsystem is

    F^+/D O=Sym^7 W O(-1) in (Sym^8 W) O.

Here dim C=5+9=14, while F^+ has rank13 and degree-8. Again C O/F^+ is a line bundle, now of degree8.

These dimensions are dimensions of actual constant coefficient spans. For example, the projection of the span of F^+ is exactly the coefficient span of its projected standard linear subsystem; the kernel is the actual P or D already contained in F^+. Saturation of F^+ in H O makes C O/F^+ locally free.

## 3. Removing the negative endpoint gives an exact rank-two forward span

Set

    E'=ker(E->A_q->O(-10)),  K=E^-.

Only the O(-10) source block can map to O(-10), so this surjective map is an isomorphism on that block. Consequently

    rank E'=16,  degree E'=-44,  E'/K=U,
    E'/F=N0,

where

    N0=V O(-4)+O(-8)              in cf,
    N0=V O(-4)+Wp O(-5)           in split ce.   (3)

The top map F->U is onto, so

    0 -> K0 -> K -> N0 -> 0.                    (4)

The pinned exact necessary top kernels are

    cf: K0=T O(-3)+P O(-4),
        or (Wp+T) O(-3)+Wp O(-5);
    ce: K0=(Wp+T) O(-3)+O(-8).

In every case K0(8) and N0(8) are globally generated and H1(K0(8))=0. Sequence (4) therefore shows that K(8) is globally generated. Every splitting degree of K is at least -8, giving

    Hom(K,O(-12))=0.                             (5)

Derivatives of K lie in E, so their only possible component outside E' is a map K->(E/E')(-2)=O(-12), zero by (5). Meanwhile the external derivative of E' has the full saturated image U in (H O/E)(-2), because its top block F already maps onto U. The internal/external image lemma now gives a saturated raw derivative image of E', isomorphic to U. Hence

    (E')^+/E'=U(2),
    rank (E')^+=18,  degree (E')^+=-30.          (6)

Since F supplies the entire image and is contained in E', equality holds as actual sheaves:

    (E')^+=E'+F^+.                              (7)

## 4. The projected negative bundle is a forbidden horizontal lattice

Let S0=E'+C O and let S be its saturation in H O. Derivatives of E' lie in E'+F^+ by (7), while C O is constant. Thus S0 is preserved by the trivial connection. Its generic subspace is horizontal, and its saturation S is a horizontal subbundle of H O. Therefore S=H' O for a constant subspace H' of H.

Because S0 contains (E')^+ and C O/F^+ has rank one, its rank is either18 or19. Rank18 would force its saturation to equal the already saturated (E')^+, making that negative-degree bundle constant, contrary to (6). Thus

    dim H'=19.                                  (8)

For cf, rank(E' intersect C O)=16+15-19=12=rank F. For ce, it is16+14-19=11=rank F. In both cases F is contained in the intersection and is saturated in E'. The rank-zero quotient of that intersection by F embeds in the locally free E'/F, so it vanishes. Hence

    E' intersect C O=F.                         (9)

Projection to the constant quotient H'/C identifies N0=E'/F with its image N in (H'/C) O. In cf this is a full-rank rank-four subsheaf of a constant rank-four bundle; in ce it is a full-rank rank-five subsheaf of a constant rank-five bundle.

The key further fact is preservation of this possibly nonsaturated image by the actual connection. Any local section of N has a local lift to E'. Differentiating the lift gives a section of (E')^+ tensor Omega^1. By (7), its projection to H'/C lies in N tensor Omega^1, since F^+ is contained in C O. The projection is constant, so differentiation commutes with it. Therefore

    dN subset N tensor Omega^1.                 (10)

The lemma in Section1 forces N=(H'/C) O. This is impossible: by (3), its degree is -20 in cf and -22 in ce, whereas a constant bundle has degree zero.

The contradiction excludes both cf sources and the split ce source. Notice that no claim that a generic full-rank projection is automatically saturated was made. Its actual differential stability supplies precisely the missing condition.

## Scope boundary

This proof excludes the stated source strata only; neither whole stable label is excluded. It makes no claim about bf, bc, or bb. All ingredients are universal exact-sequence and connection arguments and the public forced constant subsystems. There are no selected source coefficients, points, derivative evaluations, matrices, instance ranks, scans, or large computations.

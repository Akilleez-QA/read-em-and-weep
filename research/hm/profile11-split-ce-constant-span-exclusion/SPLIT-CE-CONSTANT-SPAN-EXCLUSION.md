# The split ce source forces a nonexistent degree-22 invariant

## Result and immutable inputs

The source tuple (0,0,1,0,1,0,0,1), abbreviated ce, is impossible for the original-zero-defect label G3.11.863639aa192e, source index69. Its correctly decoded bundle and quotient are

    E=(V+2P) O(-2)+V O(-4)+Wp O(-5)+O(-10),
    A_q=O(-10)+U,  U=O(4)+O(6).

The rank and degree of E are 17 and -54. This is a source-stratum exclusion, not an exclusion of the entire stable label. The same source in the balanced label G3.11.73682b4c817f was already excluded by the rank-two quadratic polar obstruction.

The sole new-structure input is the proof in PR814 at immutable commit
1f94be65b3a470a1b594e61d56df7f6057c9d907:

https://github.com/Akilleez-QA/read-em-and-weep/blob/1f94be65b3a470a1b594e61d56df7f6057c9d907/research/hm/profile11-low-positive/PROOF.md

Its SHA256 is f0bd13d85ae8a890dbec84e5f15b7ec8605b04f474d5c7d80faeb3aa08f4defc. Sections2-5 give the saturated top map, exact top kernel, zero internal derivative, and actual constant subsystem used below. The original source and label inputs are pinned there at db51525015bb7c5e825833d550d08dedf6f6ea96. We also use the saturated internal/external derivative-image lemma in Section3 of PR796:

https://github.com/Akilleez-QA/read-em-and-weep/blob/d2b43060c83328dd5118aee6b9288fcfa0c873ac/research/hm/profile12-quadratic-block-exclusion/PROOF.md

Work over C. The ambient connection is the actual trivial connection on H O. The group is binary icosahedral, with defining representation W and the notation Wp,A,V,P,S,D,T of the cited proof. It is perfect, so its one-dimensional representations are trivial. No assumption that E^+ is section-free is made.

## 1. The full constant span of the forced quadratic subsystem

Set F=(V+2P) O(-2), the canonical top block of E. The pinned proof gives an everywhere-surjective map F->U, with

    K0=ker(F->U)=(Wp+T) O(-3)+O(-8),
    0 -> F -> F^+ -> U(2) -> 0.

The raw derivative image of F is saturated, and F^+ intersects E in exactly F. The actual constant part of F^+ is D O. After quotienting the ambient space by this actual D, the resulting subsystem is the standard evaluation kernel

    M=Sym^7 W O(-1) in (Sym^8 W) O.

Consequently the full constant coefficient span of F^+ is a constant subspace C O of dimension

    dim C=dim D+dim Sym^8 W=5+9=14.

This assertion concerns the actual embedding. Indeed, the projection of the full constant span of F^+ is exactly the full constant span Sym^8 W of M, and the kernel is the actual D already contained in F^+. Complete reducibility gives C=D+Sym^8 W=P+2D as a representation. In particular,

    rank F^+=13,  degree F^+=-8,
    rank(C O/F^+)=1,  degree(C O/F^+)=8.          (1)

The quotient in (1) is locally free because F^+ is saturated in the original ambient constant bundle. The constant space C is not an arbitrary abstract completion of F^+.

## 2. Remove the negative endpoint without importing a backward quotient

Let E' be the kernel of E->A_q->O(-10), and let K=E^- be the actual derivative kernel of E. Only the O(-10) source block can map to O(-10), by degrees. Since that quotient map is surjective, it is an isomorphism on this block. Hence

    E'=F+V O(-4)+Wp O(-5),
    rank E'=16,  degree E'=-44,
    E'/K=U.                                      (2)

All equalities of splitting types here are equivariant bundle equalities, not assertions that the connection splits.

Because F->U is onto, the kernel K fits into

    0 -> K0 -> K -> V O(-4)+Wp O(-5) -> 0.       (3)

Twisting (3) by 8 shows that K(8) is globally generated. Both outside terms are globally generated and H1(K0(8))=0, so global sections of the quotient lift and generate K(8). Thus every splitting degree of K is at least -8, and

    Hom(K,O(-12))=0.                             (4)

The derivative of K lies in E. Its possible component outside E' is therefore a map

    K -> (E/E')(-2)=O(-12),

which is zero by (4). The derivative of E' has external image U in (H O/E)(-2), saturated by the original defect-zero hypothesis, and has zero internal image from K in (E/E')(-2). The internal/external image lemma therefore shows that its full raw derivative image is saturated and isomorphic to U. In particular,

    (E')^+/E'=U(2),
    rank (E')^+=18,  degree (E')^+=-30.          (5)

The same external image is already supplied by F. Thus, as actual sheaves in H O,

    (E')^+=E'+F^+.                              (6)

This establishes (5)-(6) directly; no unpublished backward-endpoint statement is a dependency.

## 3. A forced constant ambient space of dimension nineteen

Consider the coherent sum

    S0=E'+C O

inside H O, and let S be its saturation. Derivatives of local sections of E' lie in (E')^+=E'+F^+ and hence in S0. Derivatives of sections of the constant C O also lie in S0. Thus the generic subspace defined by S0 is horizontal. Its saturated subbundle S is horizontal, so in characteristic zero

    S=H' O

for a constant G-stable subspace H' of H.

By (6), S0 contains the saturated rank-eighteen bundle (E')^+. Since C O/F^+ has rank one, its generic rank is at most nineteen. If its rank were eighteen, saturation would give S=(E')^+. This would make the latter constant, contrary to its degree -30 in (5). Therefore

    dim H'=19.                                  (7)

This argument does not assume that the original sum S0 is saturated, nor that E' and C O are transverse.

The intersection E' intersect C O has rank 16+14-19=11. It contains F, also of rank eleven. Since F is saturated in E', the quotient (E' intersect C O)/F is a rank-zero subsheaf of the locally free E'/F and must vanish. Hence

    E' intersect C O=F.                         (8)

Constant projection from H' to H'/C now induces an injective sheaf map

    V O(-4)+Wp O(-5)=E'/F -> (H'/C) O.          (9)

Both sides have rank five. The source has degree -22, while the target is constant of degree zero. No saturation or surjectivity is asserted for (9).

## 4. The determinant contradiction

Taking determinants of the generically injective map (9) gives a nonzero equivariant map

    O(-22) -> O.

All determinant coefficient characters are trivial because the group is perfect. Thus this map is a nonzero invariant section of O(22). Equivalently,

    (Sym^22 W)^G is nonzero.                     (10)

But the tensor-with-W identities

    W W=1+A,  W A=W+S,  W S=A+D,  W D=S+T,
    W T=V+P+D,  W V=T,  W P=Wp+T,  W Wp=P

and the recurrence Sym^(n+1) W=W Sym^n W-Sym^(n-1) W give

    Sym^18 W=A+V+2P+D,
    Sym^19 W=W+Wp+S+2T,
    Sym^20 W=1+A+V+P+2D,
    Sym^21 W=W+2S+2T,
    Sym^22 W=2A+V+P+2D.

There is no trivial constituent in degree 22, contradicting (10). This proves the claimed split-ce source exclusion.

The determinant argument intentionally retains the possible torsion cokernel of (9): it would be a nonzero invariant divisor of degree exactly22. It is the absence of such an invariant determinant section, not an unjustified saturation assumption, that yields the contradiction.

## Boundary

The result excludes exactly the ce source stratum for the split label. It does not exclude cf, bf, bc, or bb, nor does it by itself remove either stable label. Its calculations are bounded abstract representation identities and universal exact-sequence and connection arguments. No selected HM/source coefficients, points, evaluated derivatives, matrices, instance ranks, or scans are used.

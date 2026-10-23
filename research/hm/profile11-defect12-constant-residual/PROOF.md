# Defect-twelve top blocks force a saturated constant-quotient residual

## Result and scope

Work in the actual rank-three Gauss setup over C, in the original constant thirty-space H. This theorem concerns exactly these profile-(1,1) labels:

    G3.11.cb71f599859d: A_q=O(-10)+O(-8)+O(14), B_q=O(-28)+O(6)+O(8);
    G3.11.0fe2a757439f: A_q=W O(-9)+O(14),       B_q=O(-28)+W O(7);
    G3.11.64d33b6d4139: A_q=2 O(-8)+O(14),       B_q=O(-28)+2 O(6).

All three have original determinant defect twelve. Let F be the canonical degree-minus-two block of E. Let B_raw be the image sheaf of F plus its first derivatives, and let delta be the length of F^+/B_raw, where F^+ is the saturation in H O.

The first two labels can occur only in the following strata:

    cb71f599859d: E6;
    0fe2a757439f: E6 or E13.

In each such stratum delta=0, and the actual constant span C0 of F is fifteen-dimensional. Under a constant equivariant identification,

    C0=V tensor Sym^4 W=A+V+P+D,
    F=V tensor U_2^4,
    F^+=V tensor U_3^4=(Wp+S+T) O(-1),

where U_j^4 is the complete degree-four j-th osculating bundle. The original external O(14) image is still defective; no claim that it is saturated is made.

The third label can occur only in source stratum E10. In that stratum delta=12 and F^+=C O is an actual constant fifteen-space, with

    C=A+V+P+D,
    E intersect (C O)=F=(P+2D) O(-2),
    (C O)/F=O(28).

The inclusion O(28) into Q=(H O)/E is saturated. Consequently the actual projection to the constant quotient H/C has a saturated image

    Z=E/F=O(-8)+W O(-9) subset (H/C) O.

Its actual Gauss quotient is 2 O(-8), its derivative image is saturated in ((H/C) O/Z)(-2), and its kernel and first forward transform satisfy

    K=Z^-=O(-10),     K^+=W O(-9) subset Z.

Here K^+ is the genuine first osculation of K for the constant connection, not an abstract direct summand supplied with an invented connection. The quotient Z/K^+=O(-8), and Z spans H/C.

This is a source-stratum exclusion and precise constant-subsystem theorem. It does not exclude any of the three full labels, assert their realization, prove SF>=4, or settle the original research goal. It does not assume H0(E^+)=0. No selected actual HM coefficients, parameters, points, derivative evaluations, instance matrices or ranks, model experiments, scans, or large computation are used.

## 1. Immutable inputs and notation

The original data are at commit db51525015bb7c5e825833d550d08dedf6f6ea96 of Akilleez-QA/read-em-and-weep, under research/hm/order-four-quadratic-load:

- ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md: the actual saturated E in H O, rank E=17, degree E=-54, H0(E(1))=0, E spans H, and the equivariant source catalog.
- NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md: a saturated negative bundle of largest degree -d has H0 of its Gauss kernel at twist d equal to zero; in particular H0(E^-(2))=0.
- ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md and one-one-endpoint-necessary-pairs.json: the actual quotient A_q=E/E^- and the injective original derivative A_q -> B_q^*(-2), with B_q^*(-2) saturated in Q(-2).
- rank-three-quotient-frontier-144.json: the three labels above have source_index 0,2,30, respectively.

The exact source tuples, in the eight-row notation of the splitting catalog, are:

    source_index0:
      (0,0,0,0,0,2,0,1), (0,0,0,0,1,1,0,1),
      (0,0,1,0,0,1,0,1), (0,1,0,0,0,1,0,1).
    source_index2:
      the preceding four, followed by
      (0,0,0,0,0,1,1,0), (0,0,0,0,1,0,1,0),
      (0,0,1,0,0,0,1,0), (0,1,0,0,0,0,1,0).
    source_index30:
      (0,0,0,0,0,2,0,1), (0,0,0,0,0,1,1,0),
      (1,0,1,0,0,2,0,0).

Their bundle types are:

    E0 =(P+2D) O(-2)+2 O(-8)+O(-10);
    E1 =(2P+D) O(-2)+Wp O(-5)+O(-8)+O(-10);
    E3 =(V+P+D) O(-2)+V O(-4)+O(-8)+O(-10);
    E6 =(P+D) O(-2)+T O(-3)+O(-8)+O(-10);
    E10=(P+2D) O(-2)+O(-8)+W O(-9);
    E11=(2P+D) O(-2)+Wp O(-5)+W O(-9);
    E12=(V+P+D) O(-2)+V O(-4)+W O(-9);
    E13=(P+D) O(-2)+T O(-3)+W O(-9);
    E18=2D O(-2)+Wp O(-3)+V O(-4)+2 O(-8).

Every displayed type has rank seventeen and degree minus fifty-four. In particular the extra e=1 tuples E1,E11 have top block 2P+D, not P+D.

Use W for the defining binary-icosahedral two-space, Wp for the other two-space, A=Sym2 W, S=Sym3 W, D=Sym4 W, T=Sym5 W, and V,P for the other even three- and four-spaces. All irreducibles are self-dual.

Further public inputs are:

- PR796, commit d2b43060c83328dd5118aee6b9288fcfa0c873ac, research/hm/profile12-quadratic-block-exclusion/PROOF.md: exact top kernels for E0,E10,E3,E12,E18, and Section8's profile-free quadratic Gauss gap.
- PR797, commit cdee9396133fb96d4a91babba87b1a7a35903635, research/hm/profile12-tensor-quartic-block/PROOF.md: the complete possible top kernels for E6,E13, their saturated nonzero internal derivative, and the connection-based tensor-quartic identification in Sections4-5. Its interior-stage hypothesis and later endpoint intersections are not imported.
- PR799, commit 2172e4a7abbbe232f9f448bea6fa01dee7927460, research/hm/profile11-quadratic-polar-obstruction/PROOF.md: first-polar generation and the obstruction for F=2D O(-2) when its full derivative image is saturated and its internal image is Wp O(-5). Its assumption of zero original determinant defect is not transferred; the full-image saturation required here is proved below.

## 2. The external line and the top quotient

Write A_q=A_neg+O(14), and B_q^*(-2)=A_neg+O(26). The original derivative injection has zero component from O(14) to A_neg, simply by degrees. Its A_neg-to-A_neg component is an automorphism: for two negative lines it is diagonal or a constant two-by-two matrix, since the possible off-diagonal degree-two invariant is zero; for W O(-9) it is a nonzero scalar by Schur's lemma. The determinant is generically nonzero, so this component is invertible. Negative-to-positive components may occur and are not discarded.

On the positive summand the map is multiplication by a nonzero invariant degree-twelve form. Its divisor D12 has degree twelve and is the twelve-point projective orbit, with multiplicity one. Denote the saturated positive line in Q(-2) by L=O(26). Thus the external image of O(14) is L(-D12). This argument requires neither a diagonalization of the entire map nor the vanishing of its negative-to-positive components.

Let F=R O(-2). Its map to A_q lands in O(14). The strict-top theorem makes

    R -> H0(O(16))=Sym16 W=V+P+2D

injective. This immediately excludes E1 and E11 because their coefficient representation contains 2P.

For the other types dim R is 14,12,10, or9. A common zero divisor of this section system is invariant, so if nonempty has degree at least twelve. Then at most five sections of O(16) could remain independent, a contradiction. Hence

    p:F -> O(14)

is onto everywhere. Put K0=ker p, so 0->K0(2)->R O->O(16)->0.

## 3. Full-image saturation is controlled, even with external defect

Let M=(H O/F)(-2) and N=(E/F)(-2). Differentiation induces the internal map kappa:K0->N. Let J be its image, and I the full derivative image of F in M. Since p is onto and the external O(14) map is injective as a sheaf,

    0 -> J -> I -> O(14) -> 0.                         (1)

Assume J is saturated in N. Then it is saturated in M. Let Ibar be the saturation of I in M. The quotient Ibar/J is a line bundle: J is saturated, and Ibar has rank one more than J. Its projection to Q(-2) has generic rank one and zero kernel; its image is a subsheaf of L containing L(-D12). Thus it is L(-D') for an effective divisor 0<=D'<=D12. In particular

    delta=length(Ibar/I)=12-deg(D'),     0<=delta<=12.   (2)

The torsion quotient is equivariant. Its determinant divisor is invariant, so delta is either zero or twelve. Notice that (2) allows I saturated even when its external image is not saturated: the internal component can remove the external zero.

The actual image sheaf B_raw of F and its derivatives satisfies

    0 -> F -> B_raw -> I(2) -> 0,
    0 -> F -> F^+ -> Ibar(2) -> 0.                      (3)

It follows that

    rank F^+=r+u+1,
    deg F^+=-2r+deg J+2u+16+delta,                      (4)

where r=rank F and u=rank J. Every splitting degree of F^+ is nonpositive since it is saturated in a constant bundle.

There is also an independent useful bound: a nonzero invariant saturation defect has length at least twelve, whereas deg F^+<=0 gives delta<=-deg B_raw. Thus whenever deg B_raw>-12, delta=0. No local determinant analysis is needed for that special conclusion.

## 4. Eliminate all but the low-rank top kernels

The exact kernel computations in PR796-797 give the following possibilities for the saturated internal image J:

    E0,E10: J=0;
    E3,E12: J=0;
    E18: J=0 or Wp O(-5);
    E6,E13: J=0 or the saturated Wp O(-7) in T O(-5).

For E0,E10, K0 has degrees between -6 and -3, while the target degrees are at most -10, so kappa=0. For E3,E12 the only additionally possible component is O(-8)->V O(-6), but V is absent from Sym2 W. For E18 Schur's lemma leaves only the identical Wp O(-5) channel. For E6,E13 the nonzero channel is the standard saturated quadratic inclusion Wp O(-7)->T O(-5), and is possible only when K0=T O(-3)+Wp O(-7).

If J=0, F^+/F is the line O(16+delta). The profile-free quadratic gap says, for rank F=r,

    16+delta=2r, or 16+delta<=r-1.                      (5)

For E3,E12, delta12 would make deg F^+=4, impossible; delta0 violates (5) with r12. For E18,J0 and E6/E13,J0, delta12 likewise gives positive total degree, and delta0 violates (5) with r10 or9.

For E18,J nonzero, the raw degree is -10. Thus delta=0 by (4), and the full image is saturated. PR799's first-polar obstruction applies verbatim to the resulting actual exact sequence

    0 -> Wp O(-3) -> F^+/F -> O(16) -> 0,

with F=2D O(-2). That obstruction uses the saturated full image and this exact sequence, not saturation of the external O(14) after these facts are supplied. Hence E18 is excluded.

For E0,E10, (5) forces delta12 and F^+=C O constant of rank15. For E6,E13 with J nonzero, the raw degree is -12, so delta0 or12 remains; delta12 makes F^+ constant of rank12. We now exclude those constant branches except E10 in the third label.

## 5. A constant first span gives a saturated residual, not merely an image sheaf

Suppose delta12 and F^+=C O. By Section3, the projection Ibar/J->L is an isomorphism. Twisting by two shows that the induced image of C O in Q is exactly the saturated line O(28). Let

    N_C=E intersect (C O).

Then

    (C O)/N_C=O(28) subset Q

is saturated. Therefore E+C O is a subbundle of H O, and the induced image

    Z=E/N_C subset (H/C) O

is saturated. This last saturation is essential: it is not inferred from a generic intersection rank.

The projection of the original derivative to (Q/O(28))(-2) kills the positive part of A_q. On the negative part it is an isomorphism onto a saturated copy of A_neg, because B_q^*(-2)=A_neg+O(26) was saturated in Q(-2). Negative-to-positive off-diagonal terms disappear on taking this quotient. Also E->A_neg is onto, since E->A_q is onto. Consequently the induced derivative of Z is onto A_neg followed by its saturated inclusion. In particular its actual Gauss quotient is A_neg.

If r14, then J=0, N_C=F, and

    Z=2 O(-8)+O(-10) in E0,
    Z=O(-8)+W O(-9) in E10.                             (6)

Both have rank3 and degree-26. In the first two labels deg A_neg=-18. Thus the derivative kernel of Z is a line of degree -8. This contradicts the strict-top theorem because every degree of Z is at most -8. It excludes E0,E10 for those labels.

If r9 and J=Wp O(-7), then

    0 -> F -> N_C -> Wp O(-5) -> 0.

This extension splits equivariantly as bundles, since all relevant H1 groups vanish. Its image in E/F is the standard saturated Wp O(-5)->T O(-3), with quotient P O(-2); tensor the complete quadratic evaluation sequence with Wp. Hence

    Z=P O(-2)+O(-8)+O(-10) in E6,
    Z=P O(-2)+W O(-9) in E13.                           (7)

Every degree of Z is at most -2. Its derivative lands in A_neg, whose degrees are at most -8. The top P O(-2) is therefore killed. This violates strict-top decrease and excludes delta12 for E6,E13.

## 6. The remaining first-two-label strata have the actual tensor-quartic shape

For E6,E13, the only remaining branch has delta0 and

    rank F^+=12,   deg F^+=-12,
    0 -> Wp O(-5) -> F^+/F -> O(16) -> 0.               (8)

For a quadratic bundle R O(-2) inside a constant space, its first-polar image is generated by R tensor W tensor O(-1): at an arbitrary line l in W, its image is the span of the coefficient-map values on R tensor lW. This is exactly the value-plus-first-derivative image. Since delta0, this image is the actual saturated F^+. Therefore F^+(1) is globally generated. Together with F^+ subset H O, its degrees are in {-1,0}. Its rank and degree force every degree to be -1, without any assumption on H0(E^+).

Equivariant Euler characters give F^+=(Wp+S+T) O(-1). Now the arguments of PR797 Sections4-5 use only this actual inclusion, (8), the quotient X=F^+/F, and the original connection. They identify X=V O(2), the constant span C0=V tensor Sym4 W, and the complete evaluation sequence. Thus

    F=V tensor U_2^4,    F^+=V tensor U_3^4.

No assertion from PR797 about the later E^+ intersection is imported. In the present defect-twelve setting the external image of the last line in (8) is f12 O(16) inside O(28), not a saturated O(16).

## 7. The third label reduces to a single precise residual

For G3.11.64d33b6d4139, E18 was excluded in Section4. The other two source strata have F=(P+2D) O(-2), delta12, and the saturated residuals (6). Here A_neg=2 O(-8), so

    K=Z^-=O(-10),   Z/K=2 O(-8).                        (9)

The internal derivative of K maps to (Z/K)(-2)=2 O(-10). It is nonzero: otherwise K would be horizontal in the constant ambient bundle and, being saturated there, would have degree zero. It is therefore a nonzero constant pair, with no zero divisor. Its saturated first forward transform satisfies

    K^+ subset Z,    rank K^+=2,    deg K^+=-18.         (10)

The first-polar map for the degree-ten line K is W O(-9)->(H/C) O. Its image is the value-plus-first-derivative image of K. By the no-zero-divisor conclusion, this image is already saturated and equals K^+. The ranks and degrees agree, so

    K^+=W O(-9).                                       (11)

In the E0 residual, any equivariant map W O(-9)->2 O(-8)+O(-10) has generic rank at most one: each upper component belongs to the same one-dimensional equivariant Hom space, and the lower component vanishes by degrees. This contradicts the inclusion (11). Thus E0 is excluded.

In the E10 residual, the component of (11) to its W O(-9) summand must be a nonzero scalar, because otherwise its rank would be at most one. Its possible component to O(-8) can be removed by an equivariant bundle automorphism of Z. Thus (11) is the actual tangent subbundle with quotient O(-8). The line K lies in this W O(-9) block: its map to O(-8) vanishes because Sym2 W has no invariant. Inside W O(-9), it is the standard nonzero tautological inclusion O(-10)->W O(-9), whose quotient is O(-8).

The constant space C in Section5 has character

    C=chi(F)+H0(O(28))
      =-(P+2D)+(A+V+2P+3D)
      =A+V+P+D.

Here Sym28 W=A+V+2P+3D is a bounded universal representation identity. Since E spans H and C is constant, its saturated residual Z spans H/C. This proves all claimed residual assertions.

## Verification boundary

All derivative maps used here are induced by the original constant connection or by quotienting it through an actual constant subspace. A splitting of a bundle is never treated as a horizontal splitting. In particular saturation of the residual is proved from the full length-twelve saturation and the saturated external O(26), not merely assumed from its degree or generic rank.

The remaining branches are not asserted to exist. The first two labels remain in their tensor-quartic delta-zero strata unless a separate endpoint argument excludes them; the third remains in the single E10 saturated-residual stratum. The distinction between original defect twelve and the top-block defect delta is maintained throughout.

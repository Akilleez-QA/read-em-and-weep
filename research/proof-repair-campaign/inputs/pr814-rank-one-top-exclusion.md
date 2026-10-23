# The rank-four source cannot have a rank-one top Gauss image

## Result

For either zero-defect label

G3.11.863639aa192e: A_q=O(-10)+O(4)+O(6),
G3.11.73682b4c817f: A_q=O(-10)+W O(5),

the source tuple (0,2,0,0,0,0,0,1), namely

E=P O(-2)+2T O(-3)+O(-10),

cannot have a generic rank-one image of its quadratic top block F=P O(-2) in the positive part U of A_q. The source itself and both full labels remain open. In particular this does not exclude the possible rank-two image with invariant torsion in the balanced target.

The result uses the exact public inputs listed in PROOF.md in this directory, all original source data at db51525015bb7c5e825833d550d08dedf6f6ea96, and the saturated derivative-image and profile-free quadratic Gauss-gap lemmas in PR796 at d2b43060c83328dd5118aee6b9288fcfa0c873ac. It is independent of the new rank-two polar theorem.

https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md
https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md
https://github.com/Akilleez-QA/read-em-and-weep/blob/d2b43060c83328dd5118aee6b9288fcfa0c873ac/research/hm/profile12-quadratic-block-exclusion/PROOF.md

All notation W,Wp,A,V,P,D,S,T follows the earlier note. We work over C with the binary icosahedral group; every nonempty invariant effective divisor on P1 has degree at least12.

## 1. Only the degree-four and degree-six line images can occur

Suppose the top map p:F->U has generic rank one. Let L=O(t) be the saturation of its image in U. Equivariance forces even t and trivial coefficient character. The strict-top vanishing H0(E^-(2))=0 injects P into H0(L(2))=Sym^(t+2)W.

For the split U=O(4)+O(6), t<=6. Among even degrees t<=6, P occurs only at t=4,6: Sym^6 W=V+P and Sym^8 W=P+D, while Sym^0,Sym^2,Sym^4 have no P. Negative section degrees do not contribute. The two lines are necessarily the direct O(4) or O(6) summands, since the off-diagonal equivariant Hom from O(4) to O(6) is the zero invariant space in Sym^2 W.

For the balanced U=W O(5), t<=4 because t is even. Thus only t=4 is possible. Its nonzero map O(4)->W O(5) is the standard tautological line and is saturated.

The map F->L is onto everywhere in all cases. A common zero divisor would be invariant but have degree at most t+2<=8<12.

## 2. Exclude L=O(4) for either label

The exact degree-six P system has kernel

0 -> V O(-4) -> P O(-2) -> O(4) ->0.                 (1)

For a short intrinsic verification, at twist2 its H1 is Sym^6 W-P=V; every kernel degree is at most-3, and the only contributing block supported in V is V O(-4). Its rank3 equals the entire kernel rank.

The actual internal derivative of this kernel lands in

(E/F)(-2)=2T O(-5)+O(-12)

and is zero by degrees. Since L is saturated in U and hence in Q(-2), the full derivative image of F is saturated and

F^+/F=O(6).

The profile-free quadratic Gauss-gap lemma says that for saturated O(-2)^r with Gauss rank one and F^+/F=O(b), one must have b=2r or b<=r-1. Here r=4,b=6 satisfies neither condition. Thus L=O(4) is impossible. No section-freeness assumption on E^+ is used.

## 3. Exclude L=O(6) for the split label

Now the exact degree-eight P system has kernel

K0=Wp O(-3)+O(-8).                                  (2)

Indeed H1(K0(2))=D and chi_G(K0(3))=Wp-S. The D budget can come only from D O(-4) or O(-8). The first would require a nongenuine degree-minus-three coefficient Wp-S. The second contributes -S and forces the Wp O(-3) block. This has rank3 and degree-14, as required.

The internal derivative again lands in 2T O(-5)+O(-12). The degree-minus-three block cannot contribute. The only apparent remaining channel is O(-8)->T O(-5); it vanishes equivariantly because T does not occur in Sym^3 W=S. Thus the internal derivative is zero and the raw derivative image is saturated. Consequently

rank F^+=5, deg F^+=0, F^+/F=O(8).

A degree-zero saturated subbundle of a constant bundle is a genuine constant space. Its character is

chi_G(F^+)=-P+Sym^8 W=D.

Write F^+=C O with C=D. Its intersection with E is exactly F and its image in E^+/E=A_q(2)=O(-8)+O(6)+O(8) is precisely the saturated O(8) summand. Hence E+C is saturated, and constant projection gives the actual saturated bundle

Z=(E+C)/C=E/F=2T O(-3)+O(-10)

in (H/C)O. The raw derivative remains saturated and the exact Gauss quotient of Z is

A_Z=O(4)+O(-10),                                    (3)

obtained by removing the O(6) quotient of E corresponding to the absorbed constant first span.

The highest degree of Z is-3. The strict-top Gauss-kernel lemma, which applies to any saturated negative bundle in a constant bundle, gives H0(Z^-(3))=0. Equation(3) would therefore inject

H0(Z(3))=2T -> H0(A_Z(3))=Sym^7 W=Wp+T.

This is impossible by the multiplicity of T. Thus the degree-six line image is excluded as well.

## Contribution and boundaries

All generic rank-one top images for this source have now been excluded. Rank-two images are not assumed saturated merely because they have full generic rank: when R=P has dimension4, the earlier dimension argument still permits length12 invariant torsion. That branch is deliberately retained. The proof uses only exact source data, arbitrary-point universal saturation arguments, and bounded character identities; it evaluates no selected actual source or HM data.

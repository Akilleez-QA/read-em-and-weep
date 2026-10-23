# An onto rank-four quadratic top block has only two constant-span types

## Result and scope

For either label

G3.11.863639aa192e, A_q=O(-10)+O(4)+O(6),
G3.11.73682b4c817f, A_q=O(-10)+W O(5),

consider the source E=P O(-2)+2T O(-3)+O(-10), and let F=P O(-2). Assume the actual top map p:F->U to the positive rank-two summand of A_q is onto. Then

ker p=W O(-9),
im(kappa)=W O(-9),
F^+=(Wp+T) O(-1)=Sym^7 W O(-1).

The nonzero internal image lies in a single T-multiplicity line of (E/F)(-2). The full actual constant span C of F has precisely one of two types:

1. C=P tensor Sym^2 W=V+P+D, dimension12, and F is the standard P-tensored quadratic tautological block;
2. C=Sym^8 W=P+D, dimension9; F^+=Sym^7 W O(-1) is the full evaluation kernel of O(8), and F is the P-isotypic summand of its derivative kernel Sym^6 W O(-2)=(V+P) O(-2).

No source or full label is excluded by this conclusion. It resolves the possible intrinsic constant-span geometry of the onto top branch.

## Pinned inputs

The original source and actual-bundle hypotheses are at db51525015bb7c5e825833d550d08dedf6f6ea96, under research/hm/order-four-quadratic-load:

https://github.com/Akilleez-QA/read-em-and-weep/tree/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load

We use ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md (blob b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3), NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md (blob d7506dae49b4be43230450c4132bd5db91f137ef), ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md (blob dcacf0bcdef8377c1ed7654e5b82659ea409456e), one-one-endpoint-necessary-pairs.json (blob fe0afa410d89340d3082dc814277f89fbb582c19), and rank-three-quotient-frontier-144.json (blob8b5971092f9ef762584912609fd5e9301c4e271d).

The saturated derivative-image lemma is PR796, Section3, commit d2b43060c83328dd5118aee6b9288fcfa0c873ac:
https://github.com/Akilleez-QA/read-em-and-weep/blob/d2b43060c83328dd5118aee6b9288fcfa0c873ac/research/hm/profile12-quadratic-block-exclusion/PROOF.md

The quadratic first-polar principle is PR799 at2172e4a7abbbe232f9f448bea6fa01dee7927460, also restated in PR802 at e484640a6565c278321bf6557860262c1ac1b7df:
https://github.com/Akilleez-QA/read-em-and-weep/blob/2172e4a7abbbe232f9f448bea6fa01dee7927460/research/hm/profile11-quadratic-polar-obstruction/PROOF.md
https://github.com/Akilleez-QA/read-em-and-weep/blob/e484640a6565c278321bf6557860262c1ac1b7df/research/hm/profile11-o16-constant-span-exclusion/PROOF.md

The separate rank-one top exclusion is now public in PR814 at1f94be65b3a470a1b594e61d56df7f6057c9d907:
https://github.com/Akilleez-QA/read-em-and-weep/blob/1f94be65b3a470a1b594e61d56df7f6057c9d907/research/hm/profile11-low-positive/RANK-ONE-TOP-EXCLUSION.md

The conditional onto-branch theorem below does not need that exclusion; Section5 uses it to state a complete split-label top-image consequence.

Work over C with the binary icosahedral group. Notation W,Wp,A,V,P,D,S,T is as in the pinned inputs. All irreducibles are self-dual, and a nonempty invariant effective divisor on P1 has degree at least12.

## 1. The exact top kernel has just two possibilities

Since p is onto, strict-top vanishing and its exact sequence give

rank K0=2, deg K0=-18,
maxdeg K0<=-3,
H1(K0(2))=V+P+D.                                  (1)

A center-even equivariant rank-two bundle of total degree-18 with all degrees at most-3 is either W O(-9), Wp O(-9), or the sum of two trivial-coefficient even-degree lines O(-a)+O(-b), with a,b>=4 and a+b=18. The latter unordered pairs are (4,14),(6,12),(8,10).

Their twist2 H1 characters are respectively

W O(-9): V+P+D;
Wp O(-9): A+P+D;
O(-4)+O(-14): 1+A+V+D;
O(-6)+O(-12): A+P+D;
O(-8)+O(-10): V+P+D.

Thus (1) leaves exactly

K0=W O(-9), or K0=O(-8)+O(-10).                     (2)

No selected map is used in this complete rank-two classification.

## 2. The line-sum kernel is impossible

The internal derivative targets

(E/F)(-2)=2T O(-5)+O(-12).

For K0=O(-8)+O(-10), the O(-8) block has no channel: Hom_G(1,T tensor Sym^3 W)=0. The O(-10) block maps through the complete quintic tautological channel into a single multiplicity line of 2T O(-5). Its image is either zero or saturated O(-10).

If the image is zero, the saturated derivative-image lemma gives

rank F^+=6, deg F^+=-8+deg U(2)=6,

which is impossible for a subbundle of a constant bundle.

If the image is O(-10), that lemma gives a saturated first span with

rank F^+=7, deg F^+=-2.

First polars make its degrees0 or-1. The exact character computation gives

F^+=D O+Wp O(-1).                                  (3)

Indeed chi(F^+)=-P+H0(U(2))+chi(O(-8))
=-P+(V+2P+D)-(V+P)=D,
and chi(F^+(1))=(Wp+S+2T)-T=Wp+S+T; subtracting D tensor W=S+T leaves Wp.

Let C=D be the actual constant part of(3), and project to (H/C)O. The image of F is given by an equivariant map

P O(-2)->Wp O(-1).

There is one channel, since Wp tensor W=P. If nonzero it is the Wp-tensored Euler quotient and is onto. Derivatives of the projected F stay in the projected first span Wp O(-1), so onto-ness would make this negative saturated bundle horizontal, impossible.

If the projected map is zero, F is contained in the constant C O. Its actual first span must then also lie in C O, contradicting rank F^+=7>dim C=5. Thus the second kernel in(2) cannot occur.

## 3. The doublet kernel gives the complete first-polar system

Now K0=W O(-9). Its possible internal maps to T O(-5) form a one-dimensional channel because T occurs once in W tensor Sym^4 W=S+T. The nonzero channel is multiplication by the fourth power of the tautological line,

W O(-9)->Sym^5 W O(-5)=T O(-5),

and is everywhere injective of rank2. With two target T copies it is tensored with a single nonzero multiplicity vector. There is no component to O(-12) by degrees. Thus its image is either zero or saturated W O(-9).

The zero image again makes deg F^+=6, impossible. Therefore

im kappa=W O(-9).

The actual derivative-image lemma and first-polar generation give

rank F^+=8, deg F^+=-8,
F^+=(Wp+T) O(-1).                                  (4)

For the coefficient character, twist the exact sequence once: chi(F^+(1))=(Wp+S+2T)-W Sym^4 W=Wp+T. All degrees in(4) are-1.

The first-polar surjection is

P tensor W O(-1)->F^+.

Both sides have rank8 and degree-8, so it is an isomorphism. In particular this is the complete first-polar system of the original quadratic inclusion, not a projected or partially generated first span.

## 4. Only two full constant spans remain

For a saturated linear M=U O(-1), write C for its constant coefficient span and K for the kernel of U tensor W->C. The actual Gauss kernel is K O(-2). One proves this by projecting the constant relation space K along an arbitrary tautological line in U tensor W; the Euler projection identifies the derivative kernel and supplies the second O(-1) factor. Also M^+=C O.

Apply this to M=F^+. Since derivatives of F land in M, the coefficient P of F injects into K. Here

U tensor W=(Wp+T) tensor W=V+2P+D,

a representation of dimension16. Since a negative rank-eight saturated bundle spans a constant space of dimension at least9, dimK<=7. After removing the injected P of dimension4, only the irreducible V of dimension3 can occur. Thus

K=P or K=P+V.                                      (5)

In the first case C=V+P+D has dimension12. The quadratic coefficient map of F is the surjection P tensor Sym^2 W->C. Both sides have dimension12, and P tensor A=V+P+D. It is therefore an isomorphism. This identifies the entire actual subsystem with the standard P-tensored quadratic tautological block in C O.

In the second case C=P+D has dimension9, so M has derivative rank1. Its constant-span quotient C O/M is the line O(8). Since H0(M)=H1(M)=0, the quotient is the full evaluation sequence of O(8). Thus

C=Sym^8 W,
M=Sym^7 W O(-1),
M^-=Sym^6 W O(-2)=(V+P) O(-2).

The embedded F=P O(-2) is the unique P-isotypic part of this kernel; its inclusion on multiplicity spaces has no V component by Schur's lemma. This is the second asserted type. All identifications are made inside the actual constant span through its evaluation sequence.

## 5. In the split label the rank-two top map is automatically onto

This section explains the scope of the onto assumption for the split target. The rank-one top-image branch is excluded by PR814. Suppose its generic rank-two map nevertheless has torsion length d>0. As in Section2 of the public rank-two note, its image I(2) is globally generated and receives four independent sections, so d<=12; equivariance forces d=12. Then deg I=-2 and H0(I(2))=P.

The only rank-two center-even bundles of degree-2 generated after twist2 are O(-2)+O, W O(-1), Wp O(-1). The first two have twist2 section representation1+A, and only the last gives P. Hence I=Wp O(-1).

But every equivariant map Wp O(-1)->O(4) vanishes because Wp is absent from Sym^5 W=T. Its map to O(4)+O(6) therefore has generic rank at most one, contradicting the definition of I. Thus the split top map is onto, and the two types above exhaust this source's top constant-span possibilities for that label.

For the balanced label the torsion branch is not excluded here. In particular an embedding Wp O(-1)->W O(5) can have degree12 determinant; the preceding argument must not be applied to that different target.

## Limits

This is a classification of forced intrinsic top-block subsystems and a source branch exclusion, not a whole-source or whole-label exclusion. No actual HM/source coefficients, parameters, points, derivatives, matrices, ranks, model experiments, scans, or unapproved large computation are used. The first span and constant span are always those of the original connection.

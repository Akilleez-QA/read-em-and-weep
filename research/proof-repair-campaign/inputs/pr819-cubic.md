# A length-twelve top-image defect forces a cubic Wp subsystem

## Result and boundary

Consider only G3.11.73682b4c817f (source index72), with original defect0 and

A_q=O(-10)+W O(5),
E=P O(-2)+2T O(-3)+O(-10).

Let F=P O(-2), and let p:F->W O(5) be its actual top quotient. Assume p has generic rank two but is not onto. Then its cokernel has exactly length12. The actual quadratic block belongs to a forced standard cubic Wp subsystem:

C=Wp tensor Sym^3 W=V+D, dimC=8,
F^+=Wp tensor Sym^2 W O(-1)=T O(-1),
F=Wp tensor W O(-2)=P O(-2),
F^-=Wp O(-3).

Here C is the full actual constant coefficient span of F^+, not an abstract representation copy. The top derivative quotient F/F^-=Wp O(-1) embeds into W O(5) with determinant divisor of degree12. This is a forced subsystem, not an exclusion or a realization claim. Neither the whole source nor the full label is excluded.

## Immutable inputs

All original actual bundles, source tuples, strict-top vanishing, and label data are at commit db51525015bb7c5e825833d550d08dedf6f6ea96, under research/hm/order-four-quadratic-load:

https://github.com/Akilleez-QA/read-em-and-weep/tree/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load

The files and Git blob IDs are:

ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md: b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3;
NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md: d7506dae49b4be43230450c4132bd5db91f137ef;
ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md: dcacf0bcdef8377c1ed7654e5b82659ea409456e;
one-one-endpoint-necessary-pairs.json: fe0afa410d89340d3082dc814277f89fbb582c19;
rank-three-quotient-frontier-144.json: 8b5971092f9ef762584912609fd5e9301c4e271d.

The polynomial first-polar argument is the one stated in PR799 at2172e4a7abbbe232f9f448bea6fa01dee7927460, and PR802 at e484640a6565c278321bf6557860262c1ac1b7df:
https://github.com/Akilleez-QA/read-em-and-weep/blob/2172e4a7abbbe232f9f448bea6fa01dee7927460/research/hm/profile11-quadratic-polar-obstruction/PROOF.md
https://github.com/Akilleez-QA/read-em-and-weep/blob/e484640a6565c278321bf6557860262c1ac1b7df/research/hm/profile11-o16-constant-span-exclusion/PROOF.md

We work over C with the binary icosahedral group. W is its defining two-space, Wp its other two-space, A=Sym^2 W, S=Sym^3 W, D=Sym^4 W, T=Sym^5 W, and V,P are its other even irreducibles of dimensions3,4. All irreducibles are self-dual. Every nonempty invariant effective divisor on P1 has degree at least12.

## 1. The top-image bundle is Wp O(-1)

Let I=im(p), a rank-two locally free sheaf with torsion quotient in W O(5), and write d=length coker p. Since I(2) is a globally generated quotient of P O, and H0(E^-(2))=0 injects P into H0(I(2)),

4<=h0(I(2))=2+deg I(2)=16-d.

Thus d<=12. By assumption d>0 and its divisor is invariant, so d=12 and deg I=-2. Moreover H0(I(2))=P, with dimension4.

Because I(2) is globally generated, its ordinary splitting degrees are nonnegative with total2. Equivariance and rank2 leave exactly these possibilities:

I=O(-2)+O,
I=W O(-1),
I=Wp O(-1).

The first two have H0(I(2))=1+A, whereas the last has Wp tensor W=P. Therefore

I=Wp O(-1).                                          (1)

The quotient F->I is consequently the complete evaluation of Wp O(1), twisted by-2. Its kernel is

K0=Wp O(-3).                                         (2)

## 2. Its raw first span is already saturated

The actual internal derivative of K0 lands in

(E/F)(-2)=2T O(-5)+O(-12)

and is zero by ordinary degrees. Therefore the raw derivative image of F in (H O/F)(-2) maps isomorphically onto I. Let G be its raw first span in H O. There is an exact sequence

0 -> F -> G -> I(2)=Wp O(1) ->0.

Thus G has rank6 and degree-6. It is an equivariant locally free sheaf, though saturation has not yet been asserted.

Let F^+ be its saturation. The torsion length e=length(F^+/G) is invariant. Since F^+ is a subbundle of the constant H O, deg F^+<=0, whence

0<=e=deg F^++6<=6.

The minimum nonempty invariant divisor degree12 forces e=0. Hence G=F^+ is actually saturated. This argument is essential: the projection of its derivative image to W O(5) is not saturated, but its full ambient derivative image is saturated.

First polars therefore give a surjection P tensor W O(-1)->F^+. The first span is a constant-bundle subbundle whose twist by1 is globally generated, so its degrees are0 or-1. Its rank6 and degree-6 force all degrees to be-1. Furthermore

chi_G(F^+(1))=chi_G(F(1))+chi_G(Wp O(2))=Wp tensor Sym^2 W=T.

Consequently

F^+=T O(-1).                                         (3)

## 3. Identify the exact constant span and the cubic evaluation sequence

For a saturated pure-linear bundle M=U O(-1), let C be its constant coefficient span and K the kernel of the coefficient map U tensor W->C. Then

M^-=K O(-2).                                         (4)

One intrinsic verification is to take an arbitrary tautological line l. The bundle embedding makes K intersect U tensor l trivially. Projecting K to (U tensor W)/(U tensor l) identifies it with the kernel of the derivative; the two tautological factors supply O(-2). This construction is equivariant and global. The first forward transform of M is its full constant coefficient span.

Apply (4) to M=F^+=T O(-1). Since derivatives of F land in M, F is contained in M^-, so P injects into K. The coefficient representation is

T tensor W=V+P+D.

The span C has dimension at least7: a rank-six negative saturated subbundle cannot be the entire constant space of dimension6. Hence dimK<=12-7=5. After removing P of dimension4, the remaining possible constituents are V,D, whose dimensions exceed1. Thus

K=P,
C=V+D,
M^-=F.                                              (5)

Let Q_C=(C O)/M. It is globally generated, rank2, degree6. It has no degree-zero summand, since a constant functional on such a summand would annihilate M and contradict the definition of C. As H0(M)=H1(M)=0, its presentation is its complete evaluation sequence with C=H0(Q_C).

It also has no degree-one summand. A summand R O(1) in Q_C contributes R O(-1) to its evaluation kernel M and contributes nothing to M^-. Under the direct constant decomposition H0(Q_C), the derivative span of M^- cannot recover this missing block. This contradicts (M^-)^+=F^+=M.

All degrees of Q_C are therefore at least2. The center-even, rank-two, degree-six possibilities are exactly

O(2)+O(4), W O(3), Wp O(3).

Their H0 after twisting by-1 are respectively W+S, W+S, T. The exact sequence at twist-1 identifies H0(Q_C(-1)) with H1(M(-1))=T. Thus

Q_C=Wp O(3).                                         (6)

Its complete evaluation sequence identifies (3)-(5) with the canonical cubic Wp flag:

C=Wp Sym^3 W=V+D,
M=Wp Sym^2 W O(-1)=T O(-1),
M^-=Wp W O(-2)=P O(-2)=F,
F^-=Wp O(-3).

Finally F/F^-=Wp O(-1), and its actual map to W O(5) is the image embedding(1). Both determinant characters are trivial; the determinant has degree12 and its zero divisor is precisely the original top-image torsion divisor.

## Boundaries

The proof does not select or evaluate any actual HM/source coefficients, parameters, points, derivatives, matrices, source-instance ranks, or models. It uses arbitrary-line universal evaluation sequences and a bounded rank-two splitting classification. It proves a necessary cubic subsystem in the torsion branch only; the onto rank-two branch is not analyzed here.

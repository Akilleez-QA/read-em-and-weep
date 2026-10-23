# A rank-two quadratic polar obstruction and forced constant subsystems

## Result and scope

This note studies exactly the two zero-defect profile-(1,1) labels

- G3.11.863639aa192e, source index69, with A_q=O(-10)+O(4)+O(6);
- G3.11.73682b4c817f, source index72, with A_q=O(-10)+W O(5).

Their B_q are respectively O(-8)+O(-6)+O(8) and W O(-7)+O(8). No complete label exclusion is claimed. The new conclusions are source-stratum exclusions and forced actual constant subsystems:

1. For both labels, the two source tuples
   (0,0,0,0,1,1,0,1) and (0,1,0,0,1,0,0,1)
   are impossible.
2. For the second, balanced label, the additional source tuple
   (0,0,1,0,1,0,0,1) is impossible.
3. In the source (0,1,1,0,0,0,0,1), the top quadratic map cannot have generic rank two, for either label.
4. In source (0,0,1,0,0,1,0,1), the top quadratic first osculation contains an actual constant P and its projection is the standard Sym^9 W O(-1) subsystem in a constant Sym^10 W. For the split label, source (0,0,1,0,1,0,0,1) instead forces an actual constant D and the corresponding Sym^7/Sym^8 subsystem.
5. In source (0,1,0,0,0,1,0,1), whenever the top map has generic rank two its internal derivative is nonzero with saturated image O(-10).

These conclusions use the actual ambient connection. They do not assume H0(E^+)=0, do not identify an abstract bundle splitting with a horizontal splitting, and make no selected-instance evaluation. The elementary ten-to-seven source reduction is recalled only as existing context, not as a new result. No frontier label count changes in this note.

## 1. Immutable inputs and complete source decoding

The source, quotient, and label inputs are the following files at commit db51525015bb7c5e825833d550d08dedf6f6ea96 of Akilleez-QA/read-em-and-weep, under research/hm/order-four-quadratic-load:

- ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md;
- NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md;
- ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md;
- one-one-endpoint-necessary-pairs.json;
- rank-three-quotient-frontier-144.json.

The exact GitHub blob identifiers are, in the same order,

b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3,
d7506dae49b4be43230450c4132bd5db91f137ef,
dcacf0bcdef8377c1ed7654e5b82659ea409456e,
fe0afa410d89340d3082dc814277f89fbb582c19,
8b5971092f9ef762584912609fd5e9301c4e271d.

Public source directory:
https://github.com/Akilleez-QA/read-em-and-weep/tree/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load

We also use the saturated internal/external derivative-image lemma of PR796, Section3, at d2b43060c83328dd5118aee6b9288fcfa0c873ac:
https://github.com/Akilleez-QA/read-em-and-weep/blob/d2b43060c83328dd5118aee6b9288fcfa0c873ac/research/hm/profile12-quadratic-block-exclusion/PROOF.md

The quadratic first-polar description is in PR799, commit2172e4a7abbbe232f9f448bea6fa01dee7927460, and restated in PR802, Section5, commit e484640a6565c278321bf6557860262c1ac1b7df:
https://github.com/Akilleez-QA/read-em-and-weep/blob/2172e4a7abbbe232f9f448bea6fa01dee7927460/research/hm/profile11-quadratic-polar-obstruction/PROOF.md
https://github.com/Akilleez-QA/read-em-and-weep/blob/e484640a6565c278321bf6557860262c1ac1b7df/research/hm/profile11-o16-constant-span-exclusion/PROOF.md

Work over C. The binary icosahedral group G has standard two-space W, other two-space Wp, A=Sym^2 W, S=Sym^3 W, D=Sym^4 W, T=Sym^5 W, and other even irreducibles V,P of dimensions3,4. All irreducibles are self-dual. The action on P1 factors through A5, whose nonempty orbits have cardinality at least12.

Both complete source lists consist of all ten tuples with a=d=g=0, h=1 and b+c+e+f=2. Their correctly decoded bundle is

E=(cV+(e+1)P+fD) O(-2)+bT O(-3)+cV O(-4)+eWp O(-5)+f O(-8)+O(-10).       (1)

The extra P accompanying e is essential. Formula(1) has rank
4+1+6b+6c+6e+6f=17,
and degree
-8-10-18b-18c-18e-18f=-54.

Write F=R O(-2) for the canonical top block and U for the positive rank-two part of A_q. Strict-top vanishing gives an injection

R=H0(E(2)) -> H0(U(2))=V+2P+D.                         (2)

Thus the previously known f=2, e=2, c=2 exclusions leave the seven sources denoted below by their nonzero pair of b,c,e,f:

ef: R=2P+D, N=Wp O(-5)+O(-8)+O(-10);
cf: R=V+P+D, N=V O(-4)+O(-8)+O(-10);
ce: R=V+2P, N=V O(-4)+Wp O(-5)+O(-10);
bf: R=P+D, N=T O(-3)+O(-8)+O(-10);
be: R=2P, N=T O(-3)+Wp O(-5)+O(-10);
bc: R=V+P, N=T O(-3)+V O(-4)+O(-10);
bb: R=P, N=2T O(-3)+O(-10).

In each case E=F+N as an equivariant bundle, not as a connection splitting. Original determinant defect zero identifies A_q with the saturated subbundle B_q^*(-2) of Q(-2), where Q=(H O)/E. In particular U is saturated in Q(-2), and E^+/E=A_q(2).

## 2. Top-image rank and saturation where used

Let p:F->U be the actual quotient restricted to F. For the split U=O(4)+O(6), the two P copies in ef,ce,be have an injective map on their multiplicity space into the two P occurrences in Sym^6 W+Sym^8 W. This is an isomorphism of two-dimensional multiplicity spaces. After an invertible constant change on those two source copies, one P maps only to O(4), the other only to O(6). Both row systems are nonzero and basepoint-free: their common zero divisors would be invariant and have degree at most8<12. Hence p is onto. In cf, the nonzero V and D rows map separately to O(4) and O(6), and give the same conclusion.

For balanced U=W O(5), a saturated equivariant line in U has even degree t<=4, and its sections at twist2 have dimension at most7. Consequently sources of top rank>7 have generic rank-two image. This applies to ef,cf,ce,bf,be. Here an equivariant line has trivial coefficient character because G is perfect; the degree is even because U is center-even.

For either target, whenever p has generic rank two and r=dimR>4, it is onto everywhere. Indeed its image S0 is a locally free rank-two sheaf with torsion quotient U/S0 of length d. If nonzero, d is an invariant effective divisor length, so d>=12. But S0(2) is globally generated as a quotient of R O, and

h0(S0(2))=rank S0+deg S0(2)=16-d<=4.

The injection(2) factors through H0(S0(2)), contradicting r>4. This proves saturation, rather than merely a generic-rank assertion. This argument is not applied to bb, whose top rank is4.

## 3. Exact small kernels and internal images

Assume p is onto and put K0=ker p. Then

0 -> K0(2) -> R O -> U(2) ->0,
H1(K0(2))=V+2P+D-R,
chi_G(K0(3))=R W-(Wp+S+2T).                           (3)

Every K0 degree is at most-3 by(2). The small support calculation in(3) gives:

ef: K0=(Wp+T) O(-3)+V O(-4).
cf: K0=T O(-3)+P O(-4), or (Wp+T) O(-3)+Wp O(-5).
ce: K0=(Wp+T) O(-3)+O(-8).
bf: K0=V O(-4)+P O(-4), or Wp O(-3)+V O(-4)+Wp O(-5), or T O(-3)+O(-10).
be: K0=Wp O(-3)+V O(-4)+O(-8).
bc: K0=P O(-4)+O(-8), or Wp O(-3)+Wp O(-5)+O(-8).          (4)

Here is an exhaustive support justification. A block Z O(-j), j>=4, contributes Z Sym^(j-4)W to H1(K0(2)). For budgets V, P, D, V+P, V+D, P+D, respectively, the allowed nonzero contributors are:

V: V O(-4).
P: P O(-4), Wp O(-5).
D: D O(-4), O(-8).
V+P: V O(-4), P O(-4), Wp O(-5), O(-10).
V+D: V O(-4), D O(-4), Wp O(-7), O(-8).
P+D: P O(-4), D O(-4), Wp O(-5), V O(-6), O(-8), O(-12).

To verify completeness, bound (j-3)dimZ by the budget dimension (at most9) and impose central parity. At j4 the assertion is direct. At j5 the tensor products with W allow only Wp W=P; W W=1+A, S W=A+D, and T W=V+P+D violate a forbidden constituent or the budget. At j6 the trivial coefficient gives A, which is absent; in the dimension-nine budget a three-dimensional coefficient can also fit. The A coefficient contributes A tensor A=1+A+D and is forbidden, while V tensor A=P+D gives exactly V O(-6) in that budget. At j7 only W and Wp can fit; W S=A+D is forbidden and Wp S=V+D is allowed only for that budget. At j8 only the trivial coefficient fits, giving D. At j9 no odd coefficient fits. At j10 only the trivial coefficient fits, giving V+P. At j11 no odd coefficient fits. At j12 only the trivial coefficient fits, giving P+D. Larger j exceed all budgets.

The contributions of V O(-4),P O(-4),D O(-4),Wp O(-5),V O(-6),Wp O(-7),O(-8),O(-10),O(-12) to chi_G at twist3 are respectively
0,0,0,-Wp,-T,-T,-S,-T,-(Wp+T).
The twist3 target characters for ef,cf,ce,bf,be,bc are respectively
Wp+T, T, Wp+T-S, 0, Wp-S, -S.
Matching these with nonnegative degree-minus-three coefficients gives precisely(4). For example Wp O(-7) cannot occur in be: it would require a negative S coefficient in the remaining degree-minus-three block. The V O(-6) option for bc would require the nongenuine degree-minus-three coefficient T-S; the O(-12) option would require Wp+T-S. Both are excluded for the same reason. These are bounded character identities, not selected-model ranks.

Differentiation induces the actual O-linear internal map

kappa:K0 -> (E/F)(-2)=N(-2).                           (5)

For ef and cf it vanishes by ordinary degrees. For ce,be,bc the only potentially exceptional domain is O(-8); its channels to V O(-6), Wp O(-7), and T O(-5) vanish because V is absent from Sym^2 W, Wp is absent from W, and T is absent from Sym^3 W. All other channels vanish by degrees or inequivalent irreducibles. Thus kappa=0 in these five source rows.

For bf, the first two kernels also give kappa=0. In the third, only O(-10) can contribute. It can map to T O(-5) by the complete quintic tautological line and to the O(-10) summand of N(-2) by a scalar. Every nonzero combination is saturated, either by its everywhere nonzero tautological component or by its isomorphism component. Thus

im kappa=0 or O(-10) for bf.                           (6)

When kappa=0, the actual full derivative image of F is saturated: its zero internal kernel and its saturated external image U give the derivative-image lemma. Hence

0 -> F -> F^+ -> U(2) ->0.                             (7)

## 4. A universal rank-two quadratic polar lemma

Suppose a saturated quadratic F=R O(-2) in a constant bundle satisfies(7), with U of rank two. Assume its raw first derivative image is saturated, as just proved in the applications. First polars give a surjection

R W O(-1) -> F^+.

Indeed values and first derivatives at an arbitrary tautological line l are the image of R tensor lW, by Euler's identity for quadratics. Thus F^+(1) is globally generated. Since F^+ lies in a constant bundle, its splitting degrees are0 or-1. Write

F^+=C O+J O(-1), c=dimC, s=dimJ.                       (8)

Here C=H0(F^+) is the actual constant space inside H. No abstract degree-zero summand is silently declared horizontal: global sections of the subbundle really are constant ambient vectors.

Suppose c>0 and s>0. Constant projection to (H/C)O makes
M=F^+/C=J O(-1)
a saturated actual subbundle. Write Fbar for the image of F. Its derivative lands in M. The generic rank of F intersect C is at most c-1; equality c would force all of C into saturated F, contrary to H0(F)=0. Therefore

rank Fbar>=rankF-c+1=s-1.

Consequently the derivative of M has rank at most1. It is not zero because M is a nonzero negative-degree saturated bundle. Thus it has rank exactly1.

The first forward transform of a pure-linear bundle is its full constant coefficient span: values and first derivatives of linear vector-valued polynomials span their coefficients. Therefore M^+=C1 O has rank s+1. The quotient M^+/M has degree s and rank1, hence is O(s), with trivial coefficient character. The exact sequence

0 -> J O(-1) -> C1 O -> O(s) ->0

shows on H0 that C1=Sym^s W. Twisting once and taking Euler characteristics shows J=Sym^(s-1)W. The embedding is the standard evaluation kernel, since its quotient map corresponds to the complete H0(O(s)). Its derivative kernel is

M^-=Sym^(s-2)W O(-2).                                 (9)

For clarity, at a line l the standard evaluation kernel consists of forms vanishing at l, and its derivative kernel consists of forms vanishing twice at l. This gives(9) equivariantly, without evaluating any selected point. The case s=1 has zero derivative kernel; in the applications below s>=2.

Because Fbar is contained in M^- and has rank at least s-1, it has full generic rank in(9). Its map from R O(-2) to(9) is constant on the multiplicity spaces and is therefore onto everywhere. Its kernel is an actual pure quadratic subbundle

F intersect(C O)=R0 O(-2), rank R0=c-1.                (10)

This intersection is saturated in C O, since C O/(F intersect C) injects into the locally free H O/F. It follows that C O/R0 O(-2)=O(2c-2). Moreover

0 -> O(2c-2) -> U(2) -> O(s-2) ->0                   (11)

is exact and saturated. Indeed it is obtained from(7) by quotienting F+C: the last quotient is M/Fbar=M/M^- and has degree s-2. Equation(11) is the new rank-two polar obstruction. It depends on actual constant projection and saturation, not just splitting-degree arithmetic.

If s=0, (8) is already a full constant first span, to be handled directly. The lemma makes no assertion when c=0.

## 5. Apply the polar lemma: exclusions and forced subsystems

For every zero-internal row, cohomology of(7) gives

C=V+2P+D-R,
J=(Wp+S+2T)-C W.                                    (12)

The six rows give:

ef: C=V,       J=Wp+S+T, c=3,s=12;
cf: C=P,       J=S+T,    c=4,s=10;
ce: C=D,       J=Wp+T,   c=5,s=8;
bf: C=V+P,     J=S,      c=7,s=4;
be: C=V+D,     J=Wp,     c=8,s=2;
bc: C=P+D,     J=0,     c=9,s=0.                    (13)

For ef, (11) would inject O(4) into U(2). In the split case U(2)=O(6)+O(8), the two equivariant Hom spaces are invariants in Sym^2 W and Sym^4 W, both zero. In the balanced case U(2)=W O(7), the Hom space is the invariant part of W Sym^3 W=A+D, also zero. Thus ef is impossible for both labels. Equivalently the linear-residual test J=Sym^11 W fails: Sym^11 W=W+S+T, not Wp+S+T.

For be, (11) would inject O(14) into U(2), whose largest ordinary degree is8 or7. This is impossible. Equivalently J=Wp fails the necessary identity J=Sym^1 W=W. Thus be is impossible for both labels.

For ce in the balanced label, (11) would inject O(8) into W O(7), which vanishes by degrees. Thus this entire source is impossible there. For ce in the split label, (11) is necessarily the O(8) direct summand followed by quotient O(6). Equations(9)-(10) give the actual constant D, its intersection P O(-2) with F, and projected standard Sym^7 W O(-1) in constant Sym^8 W, with derivative kernel (V+P) O(-2).

For cf, (11) is an O(6) subbundle of U(2). In the split case it is precisely the O(6) direct summand. In the balanced case it is the standard tautological O(6) in W O(7). Both are the unique nonzero equivariant channel up to scalar. Equations(9)-(10) give the actual constant P, its intersection V O(-2) with F, and projected standard Sym^9 W O(-1) in constant Sym^10 W, with derivative kernel (P+D) O(-2). These are forced actual subsystems, not claims of realization.

For bf with rank-two top map, the zero internal case would inject O(12) into U(2), impossible by ordinary degrees. Thus only the nonzero saturated O(-10) channel in(6) remains. This proves conclusion5 without excluding that remaining channel.

## 6. Exclude the rank-two top branch of bc

If p has rank two in bc, Sections2-3 give kappa=0 and(7), while(13) says

F^+=C O, C=P+D, dimC=9.

Moreover F^+ intersect E=F and (E+C)/E=U(2), by the actual image sequence(7). Since U(2) is saturated in E^+/E=A_q(2), E+C is saturated in H O. Thus constant projection gives the actual saturated bundle

Z=(E+C)/C=E/F=T O(-3)+V O(-4)+O(-10)

inside (H/C)O. Its raw derivative is saturated, and its exact Gauss quotient is O(-10): it is the original E->A_q followed by the remaining negative summand, after removing U. In particular the derivative of the top T O(-3) lands in Z. Its internal derivative into

(Z/T O(-3))(-2)=V O(-6)+O(-12)

is zero by degrees. Hence T O(-3) is horizontal in the constant quotient, a contradiction: a saturated horizontal subbundle in characteristic zero is constant and has degree zero. This excludes the rank-two top branch of bc for both labels.

## Boundaries

The remaining sources and derivative channels are not excluded. In particular no conclusion is asserted for the entire bb source, for the nonzero bf internal channel, or for a rank-one top image in bc. The forced cf and split-ce subsystems still require further analysis. All computations here are small universal representation identities and exact sequence deductions; no actual HM/source parameters, coefficients, points, derivatives, matrices, ranks, model experiments, or scans are used.

# The basepoint-free zero-defect O(26) top block has no internal derivative

## Statement, exact scope, and immutable inputs

Work over C with the binary icosahedral group G and its defining two-space W. Set A=Sym2 W, S=Sym3 W, D=Sym4 W, T=Sym5 W, and write Wp,V,P for the other irreducibles of dimensions 2,3,4. All irreducibles are self-dual.

Assume the actual saturated rank17 degree-minus54 bundle E in the constant thirty-space H O is one of

    E0  = (P+2D) O(-2)+2 O(-8)+O(-10),
    E10 = (P+2D) O(-2)+O(-8)+W O(-9).

Let F=(P+2D) O(-2). Assume the entire external derivative of F factors through the positive summand O(26) of the actual Gauss quotient, that this summand is saturated in Q(-2), Q=H O/E, and that the resulting map p:F -> O(26) is onto everywhere. In the intended three labels the other quotient summands have degrees below -2, so this factorization follows from ordinary degree vanishing. The last condition is the basepoint-free top-system case, denoted delta=0. Assume the established strict-top vanishing H0(ker(p)(2))=0.

Then the actual internal derivative

    kappa:K0=ker(p) -> (E/F)(-2)

vanishes. Consequently the actual saturated forward transform is a genuine constant fifteen-space:

    F^+=C O,  C=A+V+P+D,
    0 -> F -> C O -> O(28) -> 0.                       (1)

This theorem does not assert that the degree28 system (1) is impossible. It resolves the internal-channel dependency and permits exact constant projection. The residual corollaries reduce the retained basepoint-free rank14-top source branches of the three stated O26 labels to G3.11.8ae96830fd21 with E10 alone. This is not a full-label exclusion: the delta12 or delta20 cases and other source strata are outside this theorem.

The three labels and their negative Gauss-quotient parts are

    G3.11.dc58cc54f352: O(-8)+O(-10),
    G3.11.4b6dad66f329: W O(-9),
    G3.11.8ae96830fd21: 2 O(-8).

Each has positive part O(26) and original determinant defect zero. Their source indices are112,115,126, respectively.

Actual-bundle and source inputs are pinned at commit db51525015bb7c5e825833d550d08dedf6f6ea96 of Akilleez-QA/read-em-and-weep, in research/hm/order-four-quadratic-load/ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md, NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md, and one-one-endpoint-necessary-pairs.json (source indices112,115,126).

The saturated derivative-image and first-polar principles used below are public in PR802, commit e484640a6565c278321bf6557860262c1ac1b7df, research/hm/profile11-o16-constant-span-exclusion/PROOF.md. Their relevant arguments are repeated here. No actual source coefficients, selected parameters or points, derivative values, matrices, ranks, model experiments, scans, or large computation are used.

## 1. Only three internal images are possible, and all are saturated

Twist the exact kernel sequence:

    0 -> K0(2) -> (P+2D) O -> O(28) -> 0.

The character identities

    Sym28 W=A+V+2P+3D,
    Sym29 W=W+Wp+2S+3T,
    P W=Wp+T,  D W=S+T

give

    H1(K0(2))=A+V+P+D,
    chi_G(K0(3))=-W.                                  (2)

Every degree of K0 is at most -3. An equivariant block U O(-j), j>=4, contributes U Sym(j-4) W to the first character in (2). These contributions are genuine and cannot cancel.

Only blocks of degree at most -10 can map to (E/F)(-2). The dimension budget15 and central parity show that every such block has trivial coefficient, even j, and 10<=j<=18. The possible degrees and H1 contributions are

    j10: V+P,
    j12: P+D,
    j14: A+V+D,
    j16: 1+A+P+D, forbidden by the trivial constituent,
    j18: A+V+P+D.

Odd j>=11 already has (j-3)dim(U)>=16; nontrivial even U at j>=10 has dimension contribution at least21. This proves completeness of this tail list.

To impose the second character of (2), note that the only degree j>=4 blocks whose contribution to H1(K0(3)) contains W and fits the H1(K0(2)) budget are

    O(-6), W O(-7), A O(-8), O(-18).                  (3)

Here is a short exhaustive verification. By reciprocity, W occurs in U Sym(j-5) W exactly when U occurs in W Sym(j-5) W=Sym(j-4) W+Sym(j-6) W, with the j5 case understood directly. For 4<=j<=9, checking the displayed six symmetric powers gives precisely the first three blocks in (3); the degree>=10 tail just listed gives only O(-18). One can also obtain (3) immediately from the nine fixed McKay identities listed in Section5.

An O(-14) block uses A+V+D of the budget, leaving only P. None of (3) then fits, so it cannot cancel the -W in chi(K0(3)). Thus O(-14) is impossible.

The remaining possible tail configurations, with all degree-three blocks also forced by (2), are

    O(-10) tail:
      (S+T) O(-3)+W O(-7)+O(-10),
      (S+T) O(-3)+O(-6)+O(-8)+O(-10),
      T O(-3)+D O(-4)+O(-6)+O(-10);

    O(-12) tail:
      (Wp+T) O(-3)+V O(-4)+O(-6)+O(-12);

    O(-18) tail:
      (Wp+S+T) O(-3)+O(-18).                           (4)

For example, the O(-10) block consumes V+P, and W in (2) must be supplied by W O(-7), consuming A+D, or by O(-6), consuming A, leaving D O(-4) or O(-8). The O(-12) block consumes P+D and forces O(-6)+V O(-4). The O(-18) block consumes the whole budget. These arguments are exhaustive for kernels having any internal degree channel; kernels with all degrees greater than -10 cannot contribute to kappa.

For E0 the target is 2 O(-10)+O(-12). An O(-10) tail can map only by constants into 2 O(-10); an O(-12) tail can map only by a constant to O(-12), since there is no invariant quadratic. The O(-18) tail maps to neither target because there are no invariants of degrees8 or6.

For E10 the target is O(-10)+W O(-11). The O(-10) tail can map only by a constant to O(-10). The O(-12) tail can map only to W O(-11), in the unique degree-one channel, which is the standard tautological subline and is everywhere saturated. The O(-18) tail maps to neither target because (Sym8 W)^G=0 and W is absent from Sym7 W=Wp+T.

It follows that the actual image J is exactly one of

    0, O(-10), O(-12),                                (5)

and every nonzero possibility is saturated in the internal target. In particular no torsion correction has been suppressed.

## 2. The exact first transform in the two nonzero cases

Let I be the full actual derivative image of F in (H O/F)(-2). Saturation of J and of the external O(26) gives

    0 -> J -> I -> O(26) -> 0,
    0 -> F -> F^+ -> X=I(2) -> 0.                     (6)

Indeed the quotient by I is an extension of the locally free quotient of (E/F)(-2) by J and the locally free quotient of Q(-2) by O(26). Thus I is the actual saturated image, not just a generic image with an unspecified divisor correction.

The quadratic coefficient map of F is (P+2D) Sym2 W -> H. At any line l in W its values and first derivatives span the image of (P+2D) lW. Thus the universal first-polar map

    (P+2D) W O(-1) -> H O

has image F^+ and is onto everywhere by saturation in (6). Consequently F^+(1) is globally generated. As F^+ is a subbundle of a constant bundle, all its splitting degrees are 0 or -1. Euler characters from (6) therefore determine its splitting exactly:

    J=O(-10): F^+=(A+D) O+(Wp+T) O(-1),
    J=O(-12): F^+=(A+V) O+(S+T) O(-1).               (7)

For the first row chi(F^+)=A+D and chi(F^+(1))=W+Wp+2S+2T. For the second row these characters are A+V and W+2S+2T. Subtracting the degree-zero part tensored with W gives the claimed linear parts.

In each row C=H0(F^+) is an actual constant subspace of H. Its quotient Rlin=F^+/(C O) is saturated in (H/C) O. Every derivative of the projected F lies in Rlin. A nonzero pure linear subbundle of Rlin contained in that projected image would therefore have its nonzero constant coefficient span inside Rlin, which is impossible since H0(Rlin)=0. We use this first-polar consequence repeatedly.

## 3. The O(-10) internal image is impossible

Write the two D copies in F as D tensor M, dim M=2. In the first row of (7), the only linear channel from D O(-2) to Rlin=(Wp+T) O(-1) is the multiplicity-one channel to T O(-1): Wp W=P contains no D, while T W=V+P+D contains one D. Hence some one-dimensional subspace of M is killed by projection to Rlin. Its D O(-2) must embed in the constant C O=(A+D) O.

But every equivariant map

    D O(-2) -> (A+D) O

annihilates the universal tautological line O(-6) -> D O(-2). To verify this without evaluating any point, use D=Sym4 W. The A component is the unique SL2-equivariant second contraction by the covector annihilating l; the D component is the unique SL2-equivariant first contraction followed by multiplication by l. Their Hom spaces are one-dimensional because A A=1+A+D and D A=A+V+P+D. Both contractions kill l^4 for every line l. Their direct sum therefore cannot be injective. This contradicts the actual embedding of that D copy and excludes J=O(-10).

## 4. The O(-12) internal image is impossible

Now C=A+V and Rlin=(S+T) O(-1). Projection of F has exactly the following channels:

    D tensor M -> S: a linear form lambda on M,
    D tensor M -> T: a linear form nu on M,
    P -> T: a scalar mu.

There is no P-to-S channel, since S W=A+D. Every displayed channel has multiplicity one.

If lambda and nu were independent, a D copy killed by nu but not lambda would map onto the entire S O(-1). The nonzero D-to-S map is the standard first contraction Sym4 W -> Sym3 W and is everywhere onto. Section2 would then force a nonzero constant subspace in Rlin, a contradiction. Hence lambda and nu are dependent.

The form lambda is nonzero: otherwise projection has rank at most6, so its kernel inside the rank6 constant C has rank at least8. The form nu is also nonzero: otherwise the D source already surjects onto S O(-1), giving the previous contradiction. Finally mu is nonzero: otherwise projection has rank at most5 (the D channels are dependent), so its kernel has rank at least9, again impossible inside C.

The common kernel of lambda and nu supplies an actual embedded F0=D O(-2) in C O. The remaining projected map is

    psi:(P+D) O(-2) -> (S+T) O(-1),                  (8)

with all three allowed channels nonzero. It is equivalent, by equivariant constant automorphisms of its source and target, to the standard multiplication inclusion

    Sym8 W O(-2) -> Sym9 W O(-1).                    (9)

Indeed Sym8 W=P+D and Sym9 W=S+T. The three allowed channels form the tree P--T--D--S, so source and target scalings identify any triple of nonzero channel scalars. In (9) all three components are nonzero: P-to-T must be nonzero by injectivity, D-to-S must be nonzero by the target-rank bound if the whole image were in T, and D-to-T must be nonzero because D cannot inject into S. Thus the comparison does not assume a nonzero standard component without proof.

The standard multiplication sequence gives psi everywhere injective with locally free cokernel O(8). Therefore F intersect (C O)=F0 exactly. Since F0 is a direct summand of F and F is saturated in H O, F0 is saturated in H O and hence in C O. Its quotient in the constant rank6 bundle is O(10). Passing to X=F^+/F gives an exact sequence

    0 -> O(10) -> X -> O(8) -> 0.

It splits equivariantly: Ext1(O(8),O(10))=H1(O(2))=0, and averaging makes a splitting equivariant. Thus

    X=O(10)+O(8).                                    (10)

On the other hand (6) requires J(2)=O(-10) to embed in X with locally free quotient O(28). Every equivariant map O(-10)->O(10)+O(8) has zero O(8) component, since Sym18 W has no invariant, and its O(10) component is multiplication by an invariant degree20 form. A nonzero such form has a nonempty zero divisor. The map therefore cannot be saturated. This contradicts (6) and excludes J=O(-12).

## 5. Consequence, reproducibility, and the remaining boundary

We have exhausted (5), so J=0. Equations (6) then give rank F^+=15 and degree F^+=-28+28=0. A saturated degree-zero subbundle of a constant bundle is an actual constant subspace. Its character is

    chi(F^+)=-P-2D+Sym28 W=A+V+P+D,

which proves (1).

Moreover the actual derivative identifies C O/F with the saturated positive O(28) in E^+/E. Thus E intersect C O=F, the sum E+C O is saturated, and constant projection gives a genuine saturated residual E/F in (H/C) O. This supplies the connection-compatible constant projection used in the residual corollaries below.

The abstract character arithmetic uses only the nine fixed identities

    W1=W, WW=1+A, WA=W+S, WS=A+D, WD=S+T,
    WT=D+V+P, WV=T, WP=Wp+T, WWp=P,

and Sym(n+1)=W Sym(n)-Sym(n-1). The accompanying standalone verify.py uses only these nine identities and integer arithmetic. It checks the single dimension15 character budget, all18 compatible small kernels, the five possible tail configurations, the internal Hom channels, and the two first-polar splittings. It never executes the old envelope or a model calculation.

There is no contradiction to the degree28 quotient system itself here. A claim excluding that constant block needs an additional argument; no twelve-point ramification is present in this delta0 case, so the simple-polar contradiction for the distinct defect12/O14 label cannot simply be transferred.

## 6. Additional residual corollary: the E0 source cannot have negative quotient 2 O(-8)

Suppose, in addition to the theorem's hypotheses, that E=E0 and the full actual Gauss quotient is O(26)+2 O(-8), with original determinant defect zero. This is the E0 branch of G3.11.8ae96830fd21. Then this source branch is impossible.

By Section5, constant projection produces the actual saturated bundle

    Z=E/F=2 O(-8)+O(-10)

in (H/C) O, with actual saturated Gauss quotient 2 O(-8). The quotient map is an invertible constant map on the two top O(-8) summands, and it has zero component from O(-10), because (Sym2 W)^G=0. Hence its exact kernel is L=O(-10).

The derivative of L lands internally in

    (Z/L)(-2)=2 O(-10).

If zero, L would be a negative horizontal subbundle of a constant bundle, impossible in characteristic zero. Otherwise it is a nonzero constant column, hence a saturated O(-10) line. Since Z is saturated in the constant ambient quotient, this is also the saturated full derivative image of L. Thus L^+ has rank2 and degree-18, and lies in Z.

The first polar of any embedded degree-ten line L=O(-10) is the universal map

    W O(-9) -> (H/C) O.

Euler's identity identifies its image with the raw value-plus-first-derivative image of L. The saturated-image conclusion just proved makes this map onto L^+. Both have rank2 and degree-18, so it is an isomorphism:

    L^+=W O(-9) subset Z.

But every equivariant map W O(-9)->Z has zero O(-10) component by degrees. Its two O(-8) components are scalar multiples of the same unique channel W O(-9)->O(-8), since Hom_G(W,Sym1 W) is one-dimensional. The map consequently factors through a single O(-8) line and has rank at most one. It cannot be the displayed embedded rank-two L^+. This contradiction excludes precisely this E0 source branch.

This corollary does not exclude the E10 source for the same negative quotient; that separate residual does contain its natural W O(-9) first-polar bundle.


## 7. The two other retained matching residuals are horizontal

For original determinant defect zero, the derivative image of E is already saturated and E^+/E=A_q(2). The constant subspace C from (1) lies in E^+ and removes precisely its saturated positive O(28) quotient. Projection therefore gives

    Z=(E+C O)/(C O)=E/F,
    Z^+=E^+/(C O),
    Z^+/Z=A_neg(2),

where A_neg is the negative part of A_q. The induced derivative Z->A_neg is onto, and its exact kernel is the actual backward transform Z^-. These are equalities for the original connection, not just abstract bundle characters.

For G3.11.dc58cc54f352 with E0, this reads

    Z=2 O(-8)+O(-10),
    Z -> O(-8)+O(-10).

The two cross-degree equivariant channels vanish: maps O(-8)->O(-10) vanish by degree, and maps O(-10)->O(-8) vanish because (Sym2 W)^G=0. Surjectivity therefore makes the O(-10) component an isomorphism and the two top O(-8) summands map onto the target O(-8) by a nonzero constant row. Consequently Z^-=O(-8) is a top direct summand. Its derivative inside Z can only map to

    (Z/Z^-)(-2)=O(-10)+O(-12),

which is zero by degrees. Thus Z^- is a negative horizontal subbundle of a constant bundle, impossible.

For G3.11.4b6dad66f329 with E10, one has

    Z=O(-8)+W O(-9),
    Z -> W O(-9).

The top O(-8) component vanishes by degree, while the W O(-9) component is an isomorphism by surjectivity. Therefore Z^-=O(-8). Its internal derivative lands in W O(-11) and is zero by degrees. Again this gives an impossible negative horizontal subbundle.

For completeness, the same W-tail label cannot have source E0 even before the internal-image analysis: in E0 the only summand capable of mapping to W O(-9) is the single O(-10), so its image has rank at most one and cannot surject onto the rank-two negative quotient. The source overlist for G3.11.dc58cc54f352 contains E0 but not E10.

Thus, among the complete rank14-top E0/E10 source entries for the three displayed labels with delta=0, only

    G3.11.8ae96830fd21 with E10

remains. Its residual and its unramified degree28 constant block have not been excluded by this argument.

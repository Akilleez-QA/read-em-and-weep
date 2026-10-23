# The cc source of G3.11.ea6bced3bddf is impossible

## 0. Scope and immutable dependencies

This proof concerns exactly source index125, tuple (0,0,2,0,0,0,0,1), for the original label G3.11.ea6bced3bddf:

    E=(2V+P) O(-2)+2V O(-4)+O(-10),
    A_q=O(-10)+O(4)+O(16),
    B_q=O(-18)+O(-6)+O(8),

with original determinant defect zero. The source and label catalogs are at commit db51525015bb7c5e825833d550d08dedf6f6ea96, under research/hm/order-four-quadratic-load. Their filenames are one-one-endpoint-necessary-pairs.json and rank-three-quotient-frontier-144.json, and their Git blobs are fe0afa410d89340d3082dc814277f89fbb582c19 and 8b5971092f9ef762584912609fd5e9301c4e271d.

The actual splitting and strict-top inputs are ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md and NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md at that commit. The actual internal/external derivative-image lemma, quadratic first-polar generation, and constant-projection conventions are those in PR875 at 01f835fda6e771351555f0af1fa11647c27eb01e, research/hm/profile11-source125-bf-exclusion/PROOF.md, and PR882 at ef8ed8d457494608472a2c07de776e9162b2c20f, research/hm/profile11-source125-cf-exclusion/PROOF.md. Their foundational references are PR796 at d2b43060c83328dd5118aee6b9288fcfa0c873ac, research/hm/profile12-quadratic-block-exclusion/PROOF.md, and PR802 at e484640a6565c278321bf6557860262c1ac1b7df, research/hm/profile11-o16-constant-span-exclusion/PROOF.md. We do not infer a cc exclusion from another source's exclusion.

Conventions: G is binary icosahedral over C; W is its defining two-space, Wp its other two-space, A=Sym2 W, S=Sym3 W, D=Sym4 W, T=Sym5 W, and V,P its remaining even irreducibles of dimensions3,4. All are self-dual. The actual rank17, degree-54 bundle E is saturated in a constant thirty-space H O and H0(E(1))=0. Original defect zero makes A_q saturated in Q(-2), where Q=H O/E. The full top is

    F=(2V+P) O(-2),  rank F=10,  degree F=-20.

Strict-top injects H0(E(2)) into H0(A_q(2)). This does NOT exclude the two top V copies: the target has two V copies, one in Sym6 and one in Sym18. Every nonempty G-invariant effective divisor has degree at least12. There is exactly one invariant line in Sym12 W and no other positive-degree invariant through degree18; write f for any nonzero vector on that line. Its zero divisor has degree12.

## 1. A saturated full positive image is impossible

Suppose the external derivative of F maps onto the positive pair O(4)+O(16). Its external kernel K has

    rank K=8, degree K=-40,
    H0(K(2))=0,
    H1(K(2))=A+2P+D,
    chi_G(K(3))=-W-Wp-S.                         (1)

The cohomology follows from Sym6=V+P, Sym18=A+V+2P+D, and (2V+P)W=Wp+3T. The strict-top injection gives the H0 vanishing.

Here is a complete bounded classification sufficient for this kernel. Every irreducible summand R O(-j) has j>=3, central parity (-1)^j, rank at most8, degree contribution j dim R<=40, cohomology contribution R Sym^(j-4) within the budget in (1) when j>=4, and a nonzero Hom to F. For j>=4 the dimension budget gives (j-3) dim R<=16, hence j<=19. These conditions leave exactly the following eleven atoms; the last two columns are H1 at twist2 and Euler character at twist3:

    Wp(-3):  0,       Wp
    T(-3):   0,       T
    P(-4):   P,       0
    D(-4):   D,       0
    Wp(-5):  P,       -Wp
    S(-5):   A+D,     -S
    V(-6):   P+D,     -T
    W(-7):   A+D,     -W-S
    O(-8):   D,       -S
    Wp(-9):  A+P+D,   -S-T
    O(-12):  P+D,     -Wp-T.

This is a check of nine abstract irreducible characters over the fixed range3..19, not a source evaluation. Only W(-7) contributes a negative W in the final column. Thus exactly one W(-7) is required, consuming the whole A+D budget and leaving2P. The remaining possible atoms are Wp(-3), T(-3), P(-4), Wp(-5). The T(-3) multiplicity is zero. If x,z,w are the multiplicities of Wp(-3), P(-4), Wp(-5), then

    z+w=2,   x-w=-1.

Thus w=1 or2. Rank and degree agree in both cases. The exhaustive list is

    K1=Wp(-3)+2Wp(-5)+W(-7),
    K2=P(-4)+Wp(-5)+W(-7).                       (2)

Both have zero Hom to the internal target

    (E/F)(-2)=2V(-6)+O(-12).

Only W(-7) is high enough to reach V(-6), and W is absent from V W=T. Consequently the internal derivative image is zero. The assumed saturated external pair then makes the first increment exactly O(6)+O(18). The first span would have degree

    -20+6+18=4,

impossible for a subbundle of a constant bundle. This proves the assertion.

## 2. Every high top row has the invariant divisor12

There is one V in Sym6 and one in Sym18. Multiplication by f identifies the former copy with the latter. Strict-top forces the two-dimensional V multiplicity space in F to map isomorphically to these two target multiplicity spaces. We may therefore choose genuine top summands V_l(-2), V_h(-2) such that the former has only its nonzero lower row and the latter only its nonzero high row. The V degree6 covariant has no common zero, since a nonempty invariant base divisor would have degree at least12. Thus V_l maps onto O(4), while V_h has raw high image f O(4) inside O(16).

If the high row on the source P did not lie in f times the degree6 P system, its degree18 P system would have no common zero. Indeed a nonempty base divisor would have degree at least12; invariants through degree18 force that divisor to be the degree12 divisor of f. Dividing would then put this row in f times the degree6 P system, contrary to the assumption.

Away from the divisor of f, the two V rows already cover the positive pair. On that divisor, a basepoint-free high P row together with the lower V row would still cover it. This would make the full positive image saturated and onto, contradicting Section1. The high P row is therefore also divisible by f, allowing the zero row.

As an abstract bundle, the raw external image of the full top is consequently

    O(4)+O(4),

included in O(4)+O(16) by the identity on the first factor and multiplication by f on the second. It is onto as this abstract raw image because the two V rows are onto individually. The P coefficient has at least one nonzero row, by strict-top. After a constant change of coordinates on this abstract pair and on the V multiplicity space, the system is the direct sum of the complete Sym6 system on (V+P)(-2) and the V system on V(-2). Its external kernel is

    K=T(-3)+Wp(-5).                              (3)

The complete-system kernel is T(-3). The V degree6 system has kernel Wp(-5), as in PR882 Section1.1. No change of raw target coordinates is being regarded as a horizontal change of the saturated positive pair.

Both summands in (3) have zero Hom to 2V(-6)+O(-12). Thus the actual raw derivative of F has no internal contribution and has raw first increment2O(6). Before saturation its first span has rank12 and degree

    -20+12=-8.

Any nonzero saturation correction has the degree of a nonempty invariant effective divisor, hence is at least12. It would make the saturated first span positive in degree. Therefore the correction is zero: the raw first span is already saturated. In particular no replacement of the raw high O(6) by the saturated high O(18) is made.

Let M=F^+. Quadratic first-polar generation says that its only ordinary degrees are0 and-1. Its rank, degree, and Euler characters are

    rank M=12, degree M=-8,
    chi_G(M)=-(2V+P)+2Sym6=P,
    chi_G(M(1))=2Sym7=2Wp+2T.

Since P W=Wp+T, these identities force

    M=P O+(Wp+T) O(-1).                          (4)

Its P O is a genuine ambient constant subspace. Denote it by C0, and put L=(Wp+T) O(-1).

## 3. The whole quadratic top lies in a constant thirteen-space

Project the actual M by its actual constant subspace C0. The projection F->L cannot have kernel of generic rank4: that would put all of C0 generically into saturated F, hence C0 would be contained in F, contrary to H0(E)=0. Thus the projected rank is at least7.

Each top V maps only to T(-1), by the unique channel V W=T. These maps are determined by a functional on the two-dimensional V multiplicity space. That functional is nonzero, since otherwise the projection has rank at most4. Its kernel is a copy V_0(-2), so the projected rank is at most7. It follows that the rank is exactly7 and the generic kernel is precisely V_0(-2).

The source P must have a nonzero Wp(-1) component, or the entire projected image would lie in the rank6 T(-1). Its T(-1) component is also nonzero: otherwise the projected rank is at most3+2=5. The three nonzero channels from the surviving V+P are unique. Rescaling their irreducible source and target factors identifies the resulting map with the standard saturated multiplication inclusion

    S0=Sym6 W O(-2) -> Sym7 W O(-1)=L,          (5)

whose quotient is O(6). All three components of the standard inclusion are nonzero: otherwise its fiber rank would be at most6 or5, whereas multiplication by a nonzero linear form is injective. Thus the same argument verifies that the kernel of F->L is exactly the saturated summand V_0(-2), not merely generically so.

Since M=F^+, constant projection shows that S0^+=L. Both are saturated in (H/C0) O. The first Gauss increment is the single line O(6). The next increment has rank at most1, because differentiation of L kills the preceding S0 modulo L. On the other hand L is not constant, so that next increment is nonzero. Finally S0 is quadratic, so its second span is already constant: differentiating its quadratic coefficients at most twice spans its full constant coefficient space. Hence S0 lies in an actual constant space Cbar of rank9. Its quotient by L is a line of degree8, and its coefficient representation is Sym8=P+D, from the Euler character.

The inverse image of Cbar under the constant projection H O->(H/C0) O is therefore a genuine constant subspace C of dimension

    4+9=13,

and F is contained in C. This argument needs no chosen horizontal splitting of M other than its actual degree-zero constant subspace.

## 4. A quartic tail is trapped in the same constant space

The external derivative of the two quartic tails2V(-4) has zero negative and lower-positive rows. The former vanishes by ordinary degree; the latter vanishes because V is absent from Sym8=P+D. The high row has a one-dimensional coefficient space, since Sym20 contains exactly one V. Therefore some genuine direct tail summand

    J=V O(-4)

has identically zero external derivative.

Its actual internal derivative can land only in the top2V(-2). Indeed after twisting the complement by-2, the top is (2V+P)(-4); Schur's lemma removes P, and all remaining targets have lower ordinary degree. Since this top lies in C, the coherent image I of J under constant projection by C is preserved by the ambient regular connection.

We recall the connection-preserved-image lemma, as in PR882 Section1.2. A coherent subsheaf of a constant bundle preserved by its regular connection on P1 in characteristic zero is itself a constant subbundle. Its saturation is horizontal. In a local discrete valuation ring, a positive elementary-divisor exponent would decrease upon differentiation, contrary to preservation of the coherent lattice. Thus there is no torsion defect; the resulting subbundle has zero Gauss map and is constant.

Apply this to I. Its rank is at most3. If it has rank1 or2, its even G-representation is a sum of trivial representations, since the smallest nontrivial even irreducibles have dimension3. But Hom_G(V(-4),O)=0, because V is absent from Sym4=D. If its rank is3, the surjection from J onto that rank3 constant image is an isomorphism of bundles, impossible since degree J=-12. Consequently I=0, so J is contained in C.

Now F and J are disjoint direct summands of E. Their direct sum is saturated in H O, has rank13 and degree

    -20-12=-32,

and is contained in the rank13 constant space C. A full-rank saturated subbundle of C equals C. The negative degree is a contradiction. This proves the cc source exclusion.

## Boundary and reproduction

This excludes exactly the stated original cc tuple. It is not a whole-label exclusion, a recalculated frontier count, or a statement about any other source. The companion verify.py checks the fixed universal character identities, the eleven-atom completeness filter and two resulting kernels, the stated Hom vanishings, degree/rank contradictions, and the original source identity against the two immutable catalog blobs. REPRODUCE.md gives the input instructions. Arithmetic does not replace the saturation, actual-connection, constant-projection, or trapped-tail arguments.

No selected actual HM/source coefficients, parameters, points, derivatives, matrices, instance ranks, selected models, scans, or large computation are used. The symbol f denotes an abstract invariant line, not evaluated coefficients or a selected polynomial model. This is written mathematics, not Lean certification.

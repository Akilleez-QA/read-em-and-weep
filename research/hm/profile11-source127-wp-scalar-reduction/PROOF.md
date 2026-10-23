# Forced cubic polars and a nonzero scalar row in the remaining Wp sources

## Result and exact scope

Consider the following three original source127 tuples, all with label G3.11.cce6e3ba4eeb, original defect zero, and A_q=O(-8)+O(2)+O(16):

    a-c-f-f: (1,0,1,0,0,2,0,0),
      E=2D O(-2)+Wp O(-3)+V O(-4)+2O(-8);
    a-c-c-f: (1,0,2,0,0,1,0,0),
      E=(V+D) O(-2)+Wp O(-3)+2V O(-4)+O(-8);
    a-b-c-f: (1,1,1,0,0,1,0,0),
      E=D O(-2)+(Wp+T) O(-3)+V O(-4)+O(-8).

Let R=Wp O(-3) be the indicated direct summand. Its high derivative is necessarily nonzero, with exact divisor twelve and kernel O(-10). Its actual saturated first span is exactly one of

    R^+=V O, with constant span V of dimension three;
    R^+=P O(-2), with constant span D or V+D
                   of dimension five or eight.  (1)

For a-c-c-f, only the second alternative survives; its full constant span is necessarily V+D of dimension eight, and its internal scalar O(-10)->O(-10) row is nonzero. Its additional V(-4) row is retained and may be zero or nonzero. For a-c-f-f and a-b-c-f both alternatives in (1) are retained. This is a structural reduction and branch exclusion, not a whole-source or stable-label exclusion.

The key distinction is that the high map has a divisor: its kernel has genuine internal channels, which cannot be discarded merely because the full cubic block has no map to the lower internal target. Every such channel is retained below. No selected actual HM/source coefficients, parameters, points, derivatives, matrices, instance ranks, models, scans or large computation are used.

## 1. Immutable actual inputs

The original actual presentation, strict-top theorem and both catalogs are at db51525015bb7c5e825833d550d08dedf6f6ea96 of Akilleez-QA/read-em-and-weep, under

https://github.com/Akilleez-QA/read-em-and-weep/tree/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load

Their exact URLs and Git blob hashes are in the four-input manifest. They give the displayed tuples, a saturated full-span E in H O, and

    H=2A+2V+2P+2D, rank E=17, degree E=-54,
    E^+/E=O(-6)+O(4)+L, L=O(18) saturated in Q,
    Q=H O/E.

Work over C with binary icosahedral G. The defining representation is W; A=Sym2 W, S=Sym3 W, D=Sym4 W, T=Sym5 W, and Wp,V,P are the other irreducibles of dimensions2,3,4. All irreducibles are self-dual and G is perfect. Nonempty invariant effective divisors have degree at least twelve. Write f12 for a nonzero invariant degree-twelve form, unique up to scalar; no coefficient or point is selected. Fixed characters give

    Sym6 W=V+P, Sym7 W=Wp+T,
    Sym12 W=1+A+P+D,
    Sym18 W=A+V+2P+D,
    Sym19 W=W+Wp+S+2T,
    Wp W=P, Wp Sym3 W=V+D.                      (2)

The unique invariant degree-twelve divisor exists because the invariant space in (2) is one-dimensional. It is reduced: any repeated invariant multiplicity would give a smaller nonempty invariant reduced support, contrary to the minimum degree twelve.

## 2. The high map is forced to have exact divisor twelve

R has no external derivative to O(-8) by degree or to O(2), because Wp is absent from Sym5 W. If its high row also vanished, its entire derivative would land internally in (E/R)(-2). Every degree of that target is at most -4, whereas R has degree -3, so the internal map from the whole R would vanish. This would make the negative saturated R horizontal in H O, impossible. Thus its high row is nonzero.

That row is a Wp-valued degree-nineteen covariant. By (2), both Hom_G(Wp,Sym7 W) and Hom_G(Wp,Sym19 W) are one-dimensional. Multiplication by f12 is injective and nonzero between them, hence an isomorphism. Every nonzero high row therefore has the factorization

    R=Wp O(-3) -> O(4) --f12--> O(16).           (3)

The degree-seven row is onto everywhere. Any common-zero divisor would be invariant, nonempty, and have degree at most seven, impossible. Thus (3) has exactly the invariant divisor twelve, not a further unspecified defect, and its kernel is

    K0=O(-10).                                   (4)

The outer O(16) is saturated in Q(-2), but its raw image O(4) is not. We do not apply a saturated-external-image lemma to (3).

## 3. Every kernel channel and both first spans

The actual internal derivative of K0 has, respectively, the targets

    a-c-f-f: 2D O(-4)+V O(-6)+2O(-10);
    a-c-c-f: (V+D) O(-4)+2V O(-6)+O(-10);
    a-b-c-f: D O(-4)+T O(-5)+V O(-6)+O(-10).

The only nonzero components are

    a-c-f-f: K0 -> 2O(-10);
    a-c-c-f: K0 -> V O(-4) or O(-10);
    a-b-c-f: K0 -> T O(-5) or O(-10).            (5)

Each row in (5) has multiplicity one, except for the displayed scalar multiplicity two. The omitted D row requires D in Sym6 W, and the V(-6) row requires V in Sym4 W; both are absent. The V(-4) and T(-5) rows are nonzero degree-six and degree-five systems. Their common-zero divisors would have degree less than twelve, so each is saturated. Any nonzero scalar row is an isomorphism onto a constant scalar line. Therefore the full internal image is exactly

    J=0 or J=O(-10),                             (6)

and in the latter case it is saturated in the internal target. All possible combinations in (5) remain allowed; no actual coefficient is chosen.

Let I be the full raw derivative image in (H O/R)(-2), and Mraw the raw first-osculation sheaf. Exact image sheaves, without any saturation claim, give

    0 -> J -> I -> O(4) ->0,
    0 -> R -> Mraw -> I(2) ->0.                  (7)

If J=0, Mraw has rank3 and degree0. It is a locally free subsheaf of a constant bundle, so all splitting degrees are nonpositive. Degree zero makes it a constant O^3, and its constant inclusion is automatically saturated. Its coefficient character is

    chi_G(Mraw)=chi_G(Wp O(-3))+chi_G(O(6))
               =-Wp W+Sym6 W=V.

This gives the first alternative in (1), with actual quotient

    Mraw/R=O(6) -> L=O(18)

equal to multiplication by f12. This quotient is not saturated in Q.

If J=O(-10), equations (7) instead give rank Mraw=4 and degree Mraw=-8. The raw first polar of a cubic inclusion R=Wp O(-3) is the image of Wp W O(-2)=P O(-2). Euler's identity includes the value in that image, so it surjects onto Mraw. The ranks and degrees agree; therefore this surjection is an isomorphism of bundles:

    Mraw=P O(-2).

If M is its saturation in H O, its defect delta satisfies 0<=delta<=8, since M has nonpositive degree. The defect divisor is invariant, so delta=0. Thus Mraw is already the actual saturated R^+.

The constant span of R, and hence of its first polar, is a quotient of Wp Sym3 W=V+D. It has dimension greater than four: a saturated rank-four subbundle of a constant four-space would be constant, unlike P O(-2). Consequently its exact possible characters are D or V+D, proving the second alternative in (1).

For later use, in this alternative N=E intersect M is saturated in M and satisfies

    N/R=J(2)=O(-8), rank N=3, degree N=-14,
    M/N=O(6) -> L=O(18) by f12.                 (8)

The map N/R into E/R is exactly the twist by two of the complete list (5). The quotient in (8) retains its divisor twelve.

## 4. The zero-internal-image a-c-c-f branch is impossible

Assume a-c-c-f and J=0. Then C=R^+=V O is an actual constant three-space. Its image in Q is O(6) embedded in L with divisor twelve, and E intersect C=R. The latter is the actual kernel, because C/R injects into Q. Constant projection by C identifies the coherent projected image of E with E/R, but this image need not be saturated. We keep its original lattice.

Let B=V O(-2) be the canonical top V block of E. Its external derivative has only the high row: V is absent from Sym4 W, and the negative row vanishes by degree. The high row is a degree-eighteen V covariant. By (2), the V multiplicity in degrees six and eighteen is one, so multiplication by f12 gives an isomorphism of those covariant spaces. Consequently this high row, including the possible zero row, factors through the same actual O(4) image in (3).

This divisibility is essential for coherent, rather than merely generic, projection. The inverse image of O(6) inside Q is exactly E+C as a coherent sheaf: C/R maps isomorphically onto that O(6) image. Since the derivative of B lands in its twist by -2, the derivative of the projected B lies in the coherent projected E lattice. No division by f12 or saturation is being silently performed.

The projected B is isomorphic to B: a kernel would lie in E intersect C=R, while B and R are distinct direct summands of E. Modulo projected B, its derivative is a regular map

    B=V O(-2) -> (E/(R+B))(-2)
       =D O(-4)+2V O(-6)+O(-10).

Every component vanishes by degree. Thus the coherent projected B itself is preserved by the trivial connection.

For completeness, a preserved coherent lattice in a constant bundle has degree zero. Its generic subspace is constant in characteristic zero because its second fundamental form vanishes. Inside that fixed constant space, the determinant of the lattice has an effective zero divisor. Preservation by differentiation makes its induced determinant connection regular; a local zero of positive order would contribute a nonzero simple pole to the logarithmic derivative, impossible. Hence the determinant divisor is empty and the lattice is the full constant bundle. Applied here this contradicts degree B=-6.

This excludes J=0 for a-c-c-f. The argument does not apply to a-c-f-f's high D row: D is absent in Sym6 W, so its degree-eighteen covariant need not be divisible by f12. Nor does it assert a comparable top V block for a-b-c-f. Those sources retain both alternatives of (1), and the nonzero-internal-image branch remains open in all three.

## 5. Two universal quadratic V channels are saturated injections

We need this fact to analyze the actual nonzero internal V row, rather than to evaluate a chosen source map:

    every nonzero equivariant V O(-2) -> P O or D O
    is a saturated injection.                   (9)

Both Hom spaces have dimension one. For the P target, the nonzero P-valued degree-six covariant gives an onto map P O->O(6): a common-zero divisor would have invariant degree at most six. Its kernel K has rank3, degree-6, H0(K)=0 and H1(K)=V, since Sym6 W=P+V. These facts force K=V O(-2). Indeed all its degrees are at most-1. An atom B O(-j), j>=2, contributes B Sym^(j-2) W to the single-V H1 budget and has (j-1)dim B<=3. The only possibility is V(-2): at j=3 an odd coefficient has dimension at least two and exceeds the bound; at j=4 the scalar contributes A, not V. Larger j exceed the bound. This atom already fills rank three. Thus the kernel inclusion is the unique nonzero V-to-P channel, proving that case of (9).

For the D target take the nonzero map Wp O(-3)->D O, unique because Wp Sym3 W=V+D. It has generic rank two. Otherwise its coherent rank-one image O(e), e<=0, would require Wp in Sym^(e+3) W, impossible for degrees at most three. Its determinant zero divisor has degree at most six and is invariant, so it is empty. Hence the map is saturated. Dualizing gives an onto D O->Wp O(3). The kernel again has rank3, degree-6, H0=0 and H1=V, because H0(Wp O(3))=V+D and the coefficient D injects. The same H1-budget argument makes it V O(-2). This proves the D case of (9).

## 6. The internal scalar row of a-c-c-f cannot vanish

Retain a-c-c-f, J=O(-10) and M=P(-2). Suppose its scalar component in (5) is zero. Then the V(-4) component is nonzero. Write B=V O(-2) for the top V block, and C for the constant coefficient span of R, equal to D or V+D by (1).

Because R and its derivatives lie in C, projecting the internal derivative of K0 by C kills its image. Under the present hypothesis that image is a nonzero line in B(-2), so the constant projection of B kills that line. But the coefficient space of B is a quotient of V Sym2 W=P+D. Every nonzero P or D component of a constant projection of B is one of the saturated injections (9), and cannot kill a nonzero line. Thus the entire projection of B is zero:

    B subset C O.                               (10)

If C=D has dimension five, B+R is a rank-five direct subbundle of E and is saturated in the ambient constant bundle. Its containment in C would make it all C, contrary to its degree -12. Thus C=V+D, of dimension eight. The V constant component of B is zero, since V is absent from V Sym2 W=P+D. Therefore B lies in the D constant summand of C, by the unique injection (9), with

    D O/B=Wp O(3).                               (11)

Its actual first span is the full D O. To verify this, its derivative into Wp O(1) cannot be zero, since a negative B cannot be horizontal. Its generic image cannot have rank one: an image line O(e) has e<=1 and would require V in Sym^(e+2) W, absent in degrees at most three. Thus the generic rank is two and the generic first span is D. The raw first-polar image is generated after twist one, as a quotient of V W O(-1)=T O(-1). Its defect inside constant D has degree at most five, hence is zero by invariance. This proves B^+=D as an actual saturated equality.

The projection of R to the V constant summand of C is nonzero, because R has full span C. It is an injective Wp(-3)->V O with quotient O(6): generic rank one is impossible by the same low-degree Wp argument used in Section5, and an invariant determinant defect of degree at most six must vanish. Its generic first span is V. Since M=R^+ projects onto that first span, D+M has generic span all C. Both D=B^+ and M lie in E^+, whose saturation therefore contains C.

The actual quotient C/(B+R) has an exact sequence

    0 -> Wp O(3) -> C/(B+R) -> O(6) ->0.        (12)

Both ends have zero maps to O(4) and O(-6): Wp is absent from Sym1 W, and all other degrees are too low. Hence C's map to E^+/E=O(-6)+O(4)+L has only the high row L. Its restriction to the constant D is nonzero, or D would be contained in E. This D-valued degree-eighteen row is basepoint-free. A common divisor would have degree at most fourteen, because the five coefficient sections are independent. Only invariant degree twelve is possible in that range: degree thirteen is odd and Sym14 W has no invariant. Dividing a degree-twelve factor would require D in Sym6 W, absent. Thus C maps onto L.

Consequently X=E intersect C has rank7 and degree-18. It contains the direct saturated B+R of rank5 and degree-12. Its rank-two degree-minus-six quotient would inject into

    E/(B+R)=D O(-2)+2V O(-4)+O(-8).             (13)

No degree-minus-two coefficient of a rank-two bundle maps to D at equal degree. At degree minus three, the only possible irreducible coefficients W,Wp map neither to D(-2), since D W=S+T, nor to the lower targets. All degrees of that quotient would be at most minus four, contradicting degree minus six. This excludes the V-only internal row. Combined with Section4, it proves that the internal scalar row is nonzero for every remaining a-c-c-f realization. The additional V row remains unrestricted.

## 7. The full eight-dimensional span is forced in a-c-c-f

The scalar row just proved nonzero is the component from K0=O(-10) to the original O(-8) source summand twisted by -2. Equivalently N/R=O(-8) in (8) has a nonzero scalar component to that source summand. The original negative derivative row O(-8) is supplied only by this summand: every other source degree is higher. It is therefore a nonzero scalar isomorphism. The induced negative derivative on N/R is nonzero as well.

Suppose C=D has dimension five. Then M=P O(-2) is saturated in C, with quotient C/M=O(8). The derivative of M kills R, because R^+=M. Its restriction to N therefore factors through a map

    N/R=O(-8) -> (C/M)(-2)=O(6).

This is an invariant scalar form of degree fourteen and hence is zero. Thus differentiating N stays inside M. But the image of M in Q is the high O(6) line in (8), so its derivative cannot supply the nonzero negative row just established. This contradiction excludes C=D.

The only remaining a-c-c-f configuration consequently has

    C=V+D, M=P O(-2), J=O(-10),
    K0 -> original O(-10) internal row nonzero.  (14)

The full coefficient map Wp Sym3 W->C is an isomorphism. Its complete cubic Euler sequences give useful further actual data:

    M^+=T O(-1), C/M^+=Wp O(3),
    M^-/R=0, M/R=Wp O(-1),
    beta_M: M/R -> (M^+/M)(-2) is an isomorphism.

Since N/R=O(-8) is saturated in M/R, Y=N^+ is saturated in M^+ and satisfies

    Y/M=O(-6), rank Y=5, degree Y=-14,
    M^+/Y=O(8).

Its negative row on Y/M is a nonzero scalar isomorphism onto the negative O(-6) component of E^+/E. No claim about the full intersection E^+ intersect C or the remaining actual realization is made here.

## Contribution to the remaining problem

All three sources carry the forced divisor-twelve cubic block and one of the two concrete first spans. For a-c-c-f, (14) and the following exact cubic-polar flag are necessary, with the V internal component retained. Every external divisor and every coherent lattice used before saturation has been kept explicit. No entire source, stable label or necessary-pair count is removed by this partial reduction.



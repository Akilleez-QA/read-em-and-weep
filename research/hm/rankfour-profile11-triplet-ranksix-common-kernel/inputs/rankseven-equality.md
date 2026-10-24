# The simultaneous rank-seven defect forces the lower-column two-step flag

## Statement and retained boundary

Retain the complete actual-geometric hypotheses of the common-kernel ladder input, including the original full-positive triplet branch, original t=0, and the conditional local defect delta=12 of F=F3. In the rank-seven bundle F6, assume precisely the simultaneous-defect alternative

    I6=im beta_(F6)=E6(-D12)=O(-8)+O(-10),
    E6=(B5/F6)(-2)=O(4)+O(2).                      (1)

Here the first coherent line is the upper normal direction and the second is the lower direction. The degree is deg F6=-88. The coherent backward flag of F6 begins with rank-two quotients followed by rank-one quotients; let k be the number of initial rank-two quotients.

Then k=2 is necessary. Its exact coherent quotients are

    R0=O(-8)+O(-10), R1=O(-10)+O(-12),
    R2=O(-14), R3=O(-16), R4=O(-18).               (2)

The rank-one tail is the lower column. The actual last scalar line of degree -18 has an everywhere saturated intrinsic fourth-jet bundle

    U4=Sym4 W(-14)=D(-14) subset F6,
    beta_(F6)(U4)=O(-10) subset I6.                 (3)

Its actual quotient M=F6/U4 fits into

    0 -> O(-10) -> M -> O(-8) -> 0,
    M is O(-8)+O(-10) or W(-9).                    (4)

The new exclusion is exactly the k=1 upper-column equality flag inside (1), together with the small-slack exclusion of k=3. It does not exclude (1) itself, the other rank-seven image O(4)+O(-10), or delta=12. It asserts no occurrence for either quotient in (4), no new original jets beyond the previously proved order nine, no algebraicity and no whole-branch/profile exclusion. The auxiliary degree-eighteen line in (3) lies in the dual constant ambient and is not identified with the original degree-eighteen curve. No actual coefficient, parameter, point, jet, tensor, matrix, instance rank or normalization is selected or evaluated.

## 1. Complete immutable inputs and actual normal targets

INPUTS.json records three complete freshly fetched immutable sources, including exact commits, paths, Git blobs, UTF8 lengths and SHA256 hashes:

* PR1217 at 5249c844765cfd96ffb51bdfd4aaef8307d49b1f, research/hm/rankfour-profile11-triplet-common-kernel-ladder/PROOF.md.
* PR1216 at 66a6bfe8dd424da58f3d775be1818d1f4f71eff1, research/hm/rankfour-profile11-triplet-nine-jets/PROOF.md.
* PR1199 at 95af2c0fa1e3cce92496a44ef9023708735e1ec7, research/hm/rankfour-profile11-triplet-deep-images/PROOF.md.

Their transitive actual-geometric hypotheses remain assumptions. All derivatives below are intrinsic derivatives of actual saturated subbundles in the same fifteen-dimensional constant ambient C=V18* O.

For j>=1 in the range used below, the original degree-eighteen jet annihilators B_j satisfy

    rank B_j=14-j, deg B_j=-(j+1)(18-j),
    B_j=B_(j-1)^-, B_(j-1)/B_j=O(18-2j),
    beta_(B_j):B_j -> O(16-2j).                    (5)

At j=0 only the normal-quotient convention uses the ambient: C/B0=O(18) and beta_(B0) has target O(16). No identity B0=C^- is asserted. In particular the three targets needed near the end of the proof are

    beta_(B2):B2 -> O(12),
    beta_(B1):B1 -> O(14),
    beta_(B0):B0 -> O(16).                          (6)

The shift by Omega=O(-2) is included in each target. The first target in (6) is not O(14).

The actual common-kernel ladder supplies

    F6 subset F5 subset F4 subset F3 subset B3,
    ranks: 7,8,9,10,
    degrees: -88,-82,-74,-64,
    F_(j+1)=F_j intersect B_(j+1),
    B_j/F_j=O(4), j=3,4,5,6,
    I5=O(6)+O(-10), I4=O(8)+O(-10),
    I3=O(10)+O(-10).                               (7)

Each restriction beta_(F_(j-1))|F_j has exactly the lower coherent image O(-10). Each upper projection is the restriction of beta_(B_j), and its kernel is F_(j+1). These are actual map identities, not connections on the displayed quotients.

We work over C with the physical binary-icosahedral group G=SL2(F5), det W=1 and the retained representation names. Invariant effective divisors have minimum positive degree twelve. The fixed character facts used are

    Sym3 W=S4, Sym4 W=D, Sym5 W=T6,
    Hom_G(T6,S4)=Hom_G(T6,W)=0,
    (Sym2 W)^G=(Sym14 W)^G=0.                       (8)

## 2. The coherent capacity leaves k=1 or k=2

Write Q0=F6, Q_(i+1)=Qi^- and Ri=Qi/Q_(i+1). Negative top excludes a horizontal residual bundle, so all positive ranks decrease to zero. The exact coherent injections are Ri->R_(i-1)(-2)->I6(-2i). The quotient ranks consist of k copies of two and then 7-2k copies of one, where 1<=k<=3.

The actual two-column capacity gives

    -88<= (7-k)(-8)+k(-10)
             -(7-k)(6-k)-k(k-1)
         =-98+12k-2k^2.                             (9)

The total nonnegative coherent degree deficit is respectively 0,6,8 for k=1,2,3. A rank-two determinant deficit at most eight is an invariant effective divisor, so is zero. For a rank-one quotient with deficit e relative to the upper line of I6(-2i), its two components have degrees e and e-2. Since 0<=e<=8, a nonzero invariant component exists only if e=0, giving the full upper line, or e=2, giving the full lower line.

For k=3 the only rank-one quotient would have deficit eight, impossible. For k=1 every deficit is zero, with quotients

    R0=O(-8)+O(-10),
    R1=O(-10), R2=O(-12), R3=O(-14),
    R4=O(-16), R5=O(-18).                           (10)

For k=2 there are three rank-one quotients and their deficits sum to six, so each is exactly two. This gives precisely (2).

Consecutive rank-two injections in the latter case are everywhere isomorphisms. They preserve both scalar columns equivariantly: the upper-to-lower component vanishes by ordinary degree, and the lower-to-upper component would be an invariant degree-two section and vanishes by (8). This preserves the actual lower-column maps used in Section 7.

## 3. Actual scalar jets and a saturation-projection fact

The universal principal-parts identity from the complete input is

    P^r(O(d))*=Sym^r W(r-d), 0<=r<=d.              (11)

For an actual scalar line, its canonical differential-evaluation map has generic image the span of the line and its derivatives through order r. Once its saturated image has the expected rank and the same degree as (11), regular factorization through that saturated image and a nonzero degree-zero determinant make the map an everywhere isomorphism. No completeness of actual coefficients is required.

Even when the source degree does not agree with its saturation, a saturated scalar jet span still has derivative of generic rank at most one: over the function field, one more derivative adds at most the next derivative of the original scalar line. We use that generic statement after a ramified step below, not an unramified source identification.

We use the following actual saturation-projection fact. Let U subset A subset B be saturated subbundles of C, derivatives of U lie in B, and beta_U have generic rank one. Suppose its projection to (B/A)(-2) is everywhere onto a subbundle line L. The saturation of its coherent image in (B/U)(-2) is a line mapping to L; its composite to the quotient by L vanishes generically and hence identically. Because the coherent image already maps onto L, that line map is an isomorphism and the coherent image is saturated. Thus

    U^+/U=L(2), U^+ intersect A=U.                 (12)

When L(2)=B/A is the entire quotient line, also B/U^+=A/U. This uses actual projections and saturation, never a horizontal complement.

## 4. The k=1 equality flag produces one ramified forward step

Assume k=1. The tail in (10) consists of everywhere isomorphisms onto its scalar lines. Starting with Q5=O(-18), the equal-degree principal-parts comparison (11) identifies Q1 as its actual fourth jets D(-14), of rank five and degree -70. The derivative of Q1 maps onto the full upper O(-10) in R0(-2). Its forward transform K is the actual preimage of the upper O(-8) in F6/Q1. It has rank six and degree -78, equal to the intrinsic fifth-jet degree, so

    K=Sym5 W(-13), F6/K=O(-10).                    (13)

The restriction beta_(F5)|F6 in (7) has coherent target O(-10). Its restriction to K is zero because

    Hom_G(K,O(-10))=Hom_G(T6,Sym3 W)=0.             (14)

Hence derivatives of K lie in F5. The actual quotient F5/K is an extension of O(6)=F5/F6 by O(-10)=F6/K. It splits equivariantly, since

    Ext1_G(O(6),O(-10))
      =H1(O(-16))^G=(Sym14 W)^G=0.

Thus beta_K lands in the actual bundle (F5/K)(-2)=O(4)+O(-12). Its lower component is zero by

    Hom_G(K,O(-12))=Hom_G(T6,W)=0.                  (15)

Its projection to the upper O(4) has coherent image O(-8), inherited from beta_(F6)|K and (1). Therefore its saturation is precisely the full upper O(4). The actual forward transform U6=K^+ is the preimage of O(6) in F5/K, and

    U6/K=O(6), rank U6=7, deg U6=-72,
    U6 intersect F6=K, F5/U6=O(-10).              (16)

This is a genuinely ramified saturation step: U6 is the saturated sixth-jet span of the auxiliary degree-eighteen line, not an isomorphic copy of its intrinsic sixth-jet source of degree -84. Its generic derivative still has rank at most one by Section 3.

## 5. Two full common-kernel projections and entry into B2

Equations (14) and (16) imply Hom_G(U6,O(-10))=0: a map restricts to zero on K and then factors through O(6), whose map to O(-10) vanishes by degree. The restriction beta_(F4)|F5 factors through O(-10), so derivatives of U6 lie in F4.

The actual projection of U6 to F5/F6=O(6) is an isomorphism on U6/K. Consequently its derivative projected to (F4/F5)(-2)=O(6) is everywhere onto, by the upper quotient of beta_(F5). Apply (12). It gives a saturated next auxiliary jet span

    U7 subset F4, U7/U6=O(8),
    rank U7=8, deg U7=-64,
    U7 intersect F5=U6, F4/U7=O(-10).              (17)

Again Hom_G(U7,O(-10))=0 by the extension and ordinary degree. The restriction beta_(F3)|F4 therefore kills U7. Its derivatives lie in F3, and its upper normal projection through beta_(F4) is onto O(8). Another application of (12) gives

    U8 subset F3, U8/U7=O(10),
    rank U8=9, deg U8=-54,
    U8 intersect F4=U7, F3/U8=O(-10).              (18)

Now U8 subset B3, so its derivatives lie in B2. Its projection through beta_(B3) is onto O(10), because U8 maps onto F3/F4 and that quotient is the upper projection in I3. Applying (12) with A=B3 and B=B2 yields

    U9 subset B2, U9/U8=O(12),
    rank U9=10, deg U9=-42,
    U9 intersect B3=U8,
    Q:=B2/U9=B3/U8.                                (19)

The actual quotient Q has rank two and degree -6 and fits into

    0 -> O(-10) -> Q -> O(4) -> 0.                 (20)

In particular top Q<=4. No splitting of Q is needed. All U_r are saturated actual jet spans of the same auxiliary line; no full coefficient-span assumption is made for that line.

## 6. The corrected zero-or-isomorphism climb excludes k=1

The actual beta_(B2) kills U8, because derivatives of U8 lie in U9 subset B2. Its restriction to U9 therefore factors through the equal-degree line map

    U9/U8=O(12) -> O(12).                           (21)

There are two cases, both of which must be treated. If (21) is zero, derivatives of U9 lie in B2. Its intrinsic derivative has generic rank at most one. It cannot be zero, because U9 is negative-top and hence not horizontal. Its coherent line image then injects into Q(-2), so has degree c<=2. The actual rank-one capacity gives

    -42=deg U9<=10c-10*9<=-70,

a contradiction. Therefore (21) is nonzero, hence an everywhere isomorphism. Equation (12), using the actual normal line of B2 in B1, gives

    U10 subset B1, U10/U9=O(14),
    rank U10=11, deg U10=-28,
    U10 intersect B2=U9, B1/U10=Q.                 (22)

Next beta_(B1) kills U9 and its restriction to U10 factors O(14)->O(14). If zero, the coherent rank-one derivative of U10 lies in Q(-2) and capacity gives

    -28<=11*2-11*10=-88,

impossible. Hence the map is an isomorphism, giving

    U11 subset B0, U11/U10=O(16),
    rank U11=12, deg U11=-12,
    U11 intersect B1=U10, B0/U11=Q.                (23)

Finally beta_(B0) kills U10 and restricts to O(16)->O(16) on U11/U10. If zero, capacity gives

    -12<=12*2-12*11=-108,

again impossible. If nonzero, (12) produces a saturated forward span U12 in the constant ambient with

    U12/U11=O(18), rank U12=13, deg U12=6.

A subbundle of a constant bundle on the projective line cannot have positive degree. This final contradiction excludes k=1.

For completeness, every use of negative-top capacity above is justified independently of an auxiliary span. The actual kernels B2,B1,B0 embed respectively in the complete degree-eighteen evaluation kernels

    Sym15 W(-3), Sym16 W(-2), Sym17 W(-1).

Universally, the complete order-j kernel consists of degree-eighteen forms divisible by the (j+1)-st power of the variable vanishing line; the actual partial-system kernel embeds in it. Thus U9,U10,U11 have strictly negative top. This is a formal complete-system identity, not evaluation of any actual point or jet.

## 7. The remaining k=2 lower-column incidence

Only k=2 remains, with exact quotients (2). The last Q4=O(-18) has actual first and second jets Q3=W(-17) and Q2=A(-16), by coherent equality and (11). The derivative of Q2 maps onto the full lower O(-14) of R1(-2). Its next saturated forward span is an actual U3 subset Q1 with

    U3/Q2=O(-12), rank U3=4, deg U3=-60.

Equal degree identifies U3=Sym3 W(-15), the actual third jets. The rank-two isomorphism R1->R0(-2) preserves the lower line, as proved in Section 2. Hence the derivative of U3 projected to (F6/Q1)(-2) is onto that lower O(-12). Its generic rank is one. Applying (12) gives actual fourth jets U4 subset F6 with

    U4/U3=O(-10), rank U4=5, deg U4=-70,
    U4 intersect Q1=U3.

The degree agrees with P^4(O(18))*=D(-14), proving (3). Its image in R0=F6/Q1=I6 is precisely the lower O(-10), so its beta_(F6) image is that actual coherent line.

The quotient M=F6/U4 fits into

    0 -> Q1/U3=O(-10) -> M -> O(-8) -> 0.

Its equivariant extension group is H1(O(-2))^G=C. The zero class gives the split bundle; every nonzero class is isomorphic to the determinant-one Euler extension twisted by -9, with middle bundle W(-9). This proves (4) without assigning a horizontal structure to either abstract middle bundle.

## 8. Contribution and stopping point

Inside the simultaneous rank-seven normal defect, the coherent capacity has one equality case and two small-slack cases. One slack case is impossible immediately. The equality case forces actual saturated auxiliary jet spans whose degree-equal normal projections cannot stop: zero is ruled out by actual rank-one capacity, while a nonzero scalar projection forces the next span. Continuing through the correctly twisted original normal lines ends in positive degree in a constant bundle.

The surviving lower-column flag supplies the actual quartic jet subbundle and rank-two quotient (3)-(4). This is a further compatibility constraint, not exclusion or realization of the simultaneous-defect image, the alternate rank-seven image, or the original delta=12 branch. The separate e9 and t remain unchanged.

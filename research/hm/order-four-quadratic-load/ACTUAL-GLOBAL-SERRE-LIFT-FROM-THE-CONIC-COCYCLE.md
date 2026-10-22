# An explicit actual global Serre lift from the conic cocycle

## Result and normalization

The previously constructed degree-eight homogeneous Serre/fiber-product pair can now be completed to a GENUINE section of the actual G(4). The missing higher-cover terms are explicit and are forced by the actual conic residue. They are not discarded by a homogeneous truncation.

Let V0 be the scalar-adjusted pair of UNIVERSAL-HOMOGENEOUS-FIRST-NORMAL-CONNECTION-CANCELLATION.md, let sigma=(f,g)^t, and let

    Omega=f(V0)2-g(V0)1=Omega0+Omega1 z+Omega2 z².

In the conic theorem's normalized Koszul convention, write rho_C!=0 for the actual conic residue. The correction is

    r_x=-rho_C(Omega1+Omega2 z),
    r_y=rho_C Omega0/z=-rho_C Omega0 w,   w=-1/z,           (1)
    V_actual,i=V0,i+sigma_i r_i.

In (1), r_y is first written in the common x coefficient variables and then in its own regular y base coordinate. Its positive-cover degree is eight and its coefficient line is O_L(0). This is why no further z power appears in its additive transition.

The signs in (1) are essential. The conic theorem uses J_C=[[0,1],[-1,0]], whereas the earlier homogeneous normal calculations use J0=-J_C and n=sigma sigma^t J0. Thus N_C=-n, and the actual transition is I+t N_C=I-t n, with t_x=rho_C/z. In that convention the scalar equation is r_y-r_x=+t_x Omega. Reversing both correction signs is valid only after replacing rho_C by its opposite convention.

The resulting section is actual on U=X minus C, not merely a coefficient-bundle section. It extends uniquely across codimension-two C by reflexive Hartogs. This supplies an explicit actual global G(4) lift of Omega. It does NOT identify the earlier homogeneous K with the full actual next connection, supply second-normal bundle data, or evaluate the fourth Bockstein.

All source parameters and rho_C remain symbolic. The construction is uniform over the whole order-five stabilizer orbit, using arbitrary normalized abstract eigenvectors, and does not assign actual coefficients or evaluate an actual-instance matrix or rank.

## 1. The homogeneous triangular bundle really is the vertex eigenextension

The actual homogeneous vertex ideal has cubic and quintic generators f,g, with the nonsplit change g -> g+p f, where p has positive-cover degree two. Glue their regular Serre presentations with these homogeneous triangular changes and their determinant-compatible root-line factors. Call the resulting bundle E_tri. It is locally free, has the actual vertex zero ideal and marked vertex residue, and has determinant O(2). No claim is made that it already equals the actual bundle on U.

The actual divisor presentation and regularizing transitions used here are the ones in the frozen absolute-source and homogeneous-cancellation notes. In particular the determinant and vertex residue markings are retained from the actual regular Serre frames. There is no new unmarked quintic normalization or arbitrary residue scaling.

There is a direct chain proof that the extension CLASS of E_tri is pure block-torus weight mu², not merely that its residue has this weight. Pass temporarily to mu=T². Under scaling the negative block by mu, the transverse positive root coordinates scale by T^(-1), so

    f -> T^(-3)f,   g -> T^(-5)g,   p -> T^(-2)p.

The diagonal middle-frame map diag(T³,T⁵) carries the pulled-back section to the original section. It intertwines every triangular generator transition because its lower entry has degree two. The physical O(2) quotient frame contributes T⁴. For the quotient pi=(-g,f),

    pi diag(T³,T⁵)
       =T⁴ [T⁴(-T^(-5)g,T^(-3)f)].                       (2)

The bracketed row is the pulled-back quotient with its physical frame. Thus the chain identification fixes the kernel marking and scales the quotient by T⁴=mu². Equivalently the extension class has character mu². This also agrees with the local Koszul residue calculation: inverse generator determinant contributes mu^4 and the physical O(-2) contributes mu^(-2).

ACTUAL-CONIC-RESIDUE-FORCES-VERTEX-SERRE-COCYCLE.md proves that the kernel of restriction to the vertex residue has cover-degree-2j weights

    mu^(-2-j),   j>=0.

None is mu². Therefore E_tri is the UNIQUE weight-mu² extension with this marked vertex residue. It is exactly the canonical E_v of that theorem. This is the required global extension-class comparison; residue agreement alone would not suffice.

The same argument shows the marked identification has no global stabilizer ambiguity on U:

    H0(U,O_U(-2))
      = direct_sum_(j>=0) Sym^(2j)(Wprime) tensor H0(O_L(-2-j))=0.

A marked automorphism would be I+tN with t in this space. All outer markings being fixed, it is the identity. This does not eliminate the scalar freedom in choosing a SECTION of E_v(4) or G(4).

## 2. The genuine homogeneous section and its wedge

In the divisor frame, with a=z² and h=X²Y², use

    f=A X²Y+B Y³z+Ac X³z²-Bc XY²z³,
    g=-lambda(B XY⁴/z³+A X³Y²/z⁴)/(2Ac),
    chi=A k/(3B c²),
    v1=k z⁵(Ac z²X³/6-A X²Y/2-2B zY³/3),
    v2=lambda k(A X⁵/(6Bc)+z X³Y²/(12c)-B Y⁵/(3Ac²)),
    V0=(v1,v2)^t+(chi/2)sigma.                            (3)

The frozen homogeneous-cancellation theorem verifies both complete regular triangular charts. Section 1 upgrades those checks: V0 is a genuine section of E_v(4), rather than merely of the degree-eight coefficient bundle.

Its scalar-adjustment-independent wedge has coefficients

    Omega0=lambda k[A² X⁷Y/(6Bc)-B X²Y⁶/(3c²)],
    Omega1=-lambda k B²Y⁸/(3Ac²),
    Omega2=lambda k[A² X⁸/(6B)-5B X³Y⁵/(6c)].              (4)

The global-wedge theorem ACTUAL-MULTIPLIED-FOURTH-SOURCE-HAS-A-GLOBAL-WEDGE-CANCELLATION.md identifies this as the actual section of I_Z(6) required for the multiplied corrected midpoint source. That theorem alone established global lift existence, not that the displayed homogeneous pair was the full actual lift. The conic comparison now provides the latter's missing terms explicitly.

## 3. Exact conic gluing and all line factors

The actual conic theorem identifies the actual marked extension on U with E_v modified by

    I+t N_C,   N_C=sigma sigma^t J_C,   t_x=rho_C/z.

Here rho_C is the coefficient of the pure-conic class whose conic residue is one in the ordered Koszul sequence

    O --(u,v)--> W O(1) --(A,B) |-> uB-vA--> O(2).

No numerical value of rho_C is inferred. It is not chi, the Atiyah constant k, or the physical normal-equation factor nu. Rescaling these outer residue markings must rescale the cocycle consistently.

The ordering is checkable: the two quotient splittings satisfy s_u-s_v=sigma/(uv). If the source chart coordinates are (a_u,h), equality of represented vectors gives a_v=a_u+h/(uv). Thus source-to-target coordinate transport uses the PLUS conic cocycle. Since N_C=-n in the old convention, this is I-t n.

Because nV0=-Omega sigma and n sigma=0, the source-to-target correction of the full section is exact:

    (I-t n)(V0+sigma r_x)=V0+sigma(r_x+t Omega).            (5)

No quadratic or higher terms in t are omitted. Consequently (1) solves precisely the actual gluing equation.

For a physical O(k) section of positive-cover degree d, the coefficient line on L is O_L(k-d/2). Thus

    Omega: k=6,d=8 -> O_L(2),
    t:     k=-2,d=0 -> O_L(-2),
    r_i:   k=4,d=8 -> O_L(0).

This proves that t Omega and r_y-r_x really lie in the same untwisted coefficient line. The original chi has d=0 in O(4), hence chi_y=z^(-4)chi; it remains included in V0. Multiplying sigma by r_i adds cover degrees11 and13 in its two entries. Those higher degrees are present in the full actual section.

For an independent full-frame check, put z=Z². The opposite root coordinates are (X_y,Y_y)=(X/Z,Y/Z), and w=-1/z. Before triangular regularization, the E_v transition is

    D_root=diag(Z^(-9),Z^5),   det D_root=Z^(-4).

This is the physical determinant O(2), not a guessed coefficient determinant. Let P_x,P_y be the triangular regularizers with lower entries p_x,p_y. Then

    P0=P_y D_root P_x^(-1),
    T0^(4)=Z^(-8) P0.

The verifier proves the FULL identity

    V_actual,y=T0^(4)(I+t_x N_C,x)V_actual,x,              (6)

including the root-coordinate changes, the O(4) twist, both triangular regularizers, and the higher-degree correction terms. In particular it does not replace (6) by leading-degree or wedge equality.

## 4. Actual global extension and the remaining scalar freedom

Formula (1) is regular on each full coefficient chart: r_x is polynomial in z, and r_y=-rho_C Omega0 w is polynomial in w. Combined with the previously verified regular V0 and sigma, this gives a regular section of the ACTUAL G(4) on U by (6).

The actual G(4) is locally free on the smooth weighted stack X, hence reflexive. The complement C has codimension two. Reflexive Hartogs, checked on smooth stack charts and descended, gives

    H0(X,G(4))=H0(U,G(4)).

The constructed actual section therefore extends uniquely across C. This invokes Hartogs only after the full actual bundle gluing has been established. The wedge is the prescribed global Omega by uniqueness and its unchanged value on U.

The chosen scalar correction is NOT unique before its normalization is fixed. Within cover degree eight, two regular solutions of the additive equation differ by

    H0(L,Sym^8(Wprime) O_L(0))=Sym^8(Wprime),

of dimension nine. Such a change adds sigma times a global positive degree-eight polynomial, a genuine section of O_X(4). The displayed Laurent split fixes this freedom by putting the nonnegative Laurent part, with its required minus sign, in r_x and the negative Laurent part in r_y, with no additional common degree-eight constant polynomial. Other cover-degree scalar sections supply the usual additional H0(O_X(4)) freedom; the lower-degree chi normalization in (3) was fixed by the earlier source matching.

## 5. What this resolves, and what remains

This resolves the former comparison between the homogeneous Serre pair and a full actual G(4) lift on the cone. It explicitly incorporates the nonzero conic-residue cocycle and retains all root/determinant factors.

It does not show that the homogeneous K in the preceding cancellation note is the full actual first-normal connection. To make that promotion, the cone frame correction I-t n must be transported through the actual square-zero normal lift, and the resulting q-order operator terms must be compared. The second-normal formula retains the old K through [K,t]+[K,n]_1, so that step cannot be skipped. The actual endpoint variation and second-normal data are also not supplied by this theorem. No fourth-Bockstein claim follows from (6).

## Reproduction

Run python verify_actual_serre_lift_from_conic_cocycle.py. It reruns the homogeneous cancellation checks, verifies (4), the oriented additive split, both full regular charts, the complete actual root-frame transition (6), the Koszul orientation, the homogeneous transition-chain weight (2), and all coefficient-line arithmetic. The geometric eigenextension and actual conic-residue input is the cited conic theorem; the final global extension uses reflexive Hartogs. All source and residue parameters remain unassigned.

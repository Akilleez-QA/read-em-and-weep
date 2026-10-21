# The fifty point blowups over the smooth modular locus

## Status

This is the local smooth-modular lemma. Its former compact-boundary gap is now resolved for the dominating component by COMPACT-DOMINATING-NORMALIZATION.md, using the finite canonical cusp map and a unit-component principal-ideal argument. Additional components in the raw cusp inverse images are still not excluded.

## Scope

Use the canonical ruling bundle and corrected global polarization from MODULAR-RULING-BUNDLE.md, and the canonical smooth double-cover surface W in |2(ξ+I)| constructed in MODULAR-QUADRIC-DOUBLE-COVER.md. The theorem below identifies the evaluation geometry only over the smooth modular parameter locus. It does not assert a compact equality across the twelve cusps.

Let T^o be the modular parameter line minus the twelve cusps, and suppose the source quadric Q is general enough to meet the 25 fixed HM lines transversely at fifty points z_i, with all parameters κ(z_i) in T^o and distinct. Write W^o for the restriction of W over T^o. It is the quadric cut in the family of normalized degree-fifteen beta scrolls. On each torsion section its two lifts D_i are the curves mapped to the fixed points z_i.

Let X=P_Q(E), let Xhat be its blowup at the fifty simple evaluation base points, and let f:Xhat->P(U*) be the evaluation projection. Then the normalization of the component of f^{-1}(Gamma^o) dominating Gamma^o is the blowup of W^o at the fifty points

    P_i=D_i intersect {modular parameter κ(z_i)}.

The raw inverse image need not be normal. The statement concerns its normalization.

## 1. Actual local evaluation equations

Fix z=z_i. Choose a constant basis s_0,s_1,s_2,s_3 of U with s_0(z) nonzero and the others vanishing at z, and a local frame of E whose first basis vector is s_0. The evaluation matrix has form

    [1, h_1(a), h_2(a), h_3(a)]
    [0, a_1,    a_2,    a_3   ],

where h_j(0)=0. The a_j are regular coordinates on Q near z, because the evaluation minors cut out the transverse, reduced marked point there. The h_j must not be discarded by coordinate-dependent column operations: those would change the fixed target curve Gamma.

For the quotient coordinate [u:v] on P(E), evaluation has target

    [u : u h_1+v a_1 : u h_2+v a_2 : u h_3+v a_3].

Parametrize Gamma near κ(z) by [1:γ_1(t):γ_2(t):γ_3(t)], with γ(0)=0 and γ'(0) nonzero. On the normalized incidence, the source vectors satisfy

    u(γ(t)-h(a))=v a.

This is the fixed-target proportionality equation used below.

## 2. Immersion at the distinguished ruling branch

The distinguished point is exactly the required marked point, not an arbitrary point on a ruling. For the chosen HM line the modular parameter p=(λ:µ) is the origin of E_p in both the x-copy and the w-copy. Proposition4.19(ii) says that the graph-section map between these copies is multiplication by two. Its point above the origin therefore maps to the origin p in the w-copy. Lemma4.15 maps the origin ruling isomorphically to the chosen HM line, so this graph point is its unique point mapping to p. The exact net dictionary identifies the same modular parameter with B=κ(p). Consequently, at B=κ(z_i), the point P_i on the distinguished torsion ruling is this graph point. Heisenberg equivariance transports the equality to all twenty-five source lines.

ADHPR, Proposition4.19, supplies a graph section in the normalized scroll whose map to the singular elliptic curve is multiplication by two. Its tangent image at a smooth elliptic point is therefore nonzero. Lemma4.15 maps the ruling over the origin isomorphically to the initial HM line. The involution acts as inversion on the elliptic curve and fixes that projective HM line pointwise. At the origin its elliptic tangent has eigenvalue −1, whereas the tangent of the fixed line has eigenvalue +1. These image tangent directions are independent.

Thus the normalized scroll map is immersive at the origin ruling's distinguished point; Heisenberg translation proves the same at all twenty-five torsion rulings. Since Q is transverse to the fixed line, its normalized pullback curve also has nonzero source-coordinate derivative transverse to D_i. Consequently near P_i there are regular coordinates (t,s) on W^o such that D_i=(s=0) and

    a=s A(t,s),

where A has at least one unit component. This is the geometric input that cannot be inferred solely from intersection numerology.

## 3. The quotient pencil has exactly one simple point base

The proportionality equation gives A wedge (γ-h)=0. On s=0 this says A(t,0) is proportional to γ(t) for t nonzero. Since γ(t)=t C(t) with C(0) nonzero and A(0,0) nonzero, they remain proportional at t=0. Choose an index j where A_j and C_j are units.

Because h(a) vanishes at a=0, its pullback is divisible by s. The quotient coordinate is therefore

    [u:v]=[a_j:γ_j-h_j]
           =[s A_j : t C_j-s H_j].

The two entries generate precisely the maximal ideal (s,t), by their independent first-order parts. The quotient map has a simple point base, resolved by one ordinary blowup of P_i. On its exceptional P^1 it gives a projective linear isomorphism to the quotient P^1 over z.

This proves an actual local point blowup, not merely that a self-intersection changes by one.

## 4. Other points over z do not create quotient base points

Away from the torsion curve D_i, the preimage of the fixed source point z is zero-dimensional in W^o. Indeed the normalized-scroll map is finite on each smooth modular fiber; for a modular parameter different from κ(z), z is a smooth point of the beta scroll and has its unique preimage on the torsion ruling. Thus no other divisorial component maps to z.

At an isolated preimage, the ideal generated by (a_1,a_2,a_3) has no height-one zero. In the function field the incidence relation gives γ-h=β a. At any height-one prime one a_j is a unit, hence β is regular there because β a_j is regular. Normality of W^o then implies β is regular at the point. The quotient is [1:β], with first coordinate a unit, and extends regularly.

This is a vector-proportionality argument. It is not the false assertion that every rational map from a smooth surface to P^1 extends across isolated points; the pencil [s:t] does not satisfy the no-height-one-common-zero condition just used.

Along D_i away from P_i, γ(t) is nonzero, so the quotient extends as the original evaluation base point [0:1]. There are no further quotient base points over the smooth modular locus.

## 5. Lift to the evaluation blowup and normalization

After the fifty point blowups, the map to X lifts to Xhat. Locally the evaluation base ideal pulls back to the strict transform of D_i with multiplicity one. For example, in the point-blowup chart s=tr, the quotient coordinate u/v is r times a unit and a=tr A, so the evaluation base ideal is generated by r. In the complementary chart t=sw, the quotient is generically away from the evaluation base point. These charts also show that the strict transform of D_i maps to E_i intersect f^{-1}(Gamma), while the new exceptional curve maps isomorphically to the original quotient fiber over z.

The resulting map to the dominating inverse-image component is proper and birational. It has no positive-dimensional fibers: away from the fifty quotient fibers this follows from finiteness of the normalized-scroll maps; each new exceptional curve maps isomorphically to its quotient fiber. It is therefore finite. Since the source is normal, it is the normalization of that component.

In particular on the smooth modular open, writing b:Wtilde^o->W^o for the fifty point blowups and F_i for their exceptional curves,

    A=6F,
    sum E_i=b^*(pi^*C_S)-sum F_i,
    L=b^*(pi^*(C_S+6F))-sum F_i.

The strict transforms of the fifty (-5)-curves consequently have self-intersection −6, in agreement with the evaluation exceptional divisor calculation. The formula is now supported by a local base-ideal computation, not deduced from that numerical agreement.

## Compact boundary still open

To extend this normalization statement over the twelve cusps, one must control the fixed-coordinate canonical ruling map on each cusp component and show that no additional quotient base points, contracted curves, or vertical inverse-image components arise. The existence and smoothness of the compact double-cover W do not by themselves provide this identification. No compact Bl_50 equality, global eigenquotient-jet equivalence, or adjoint-obstruction exclusion is asserted here.

Primary source: https://arxiv.org/pdf/alg-geom/9606013, Lemmas4.14–4.15 and Proposition4.19; the actual beta-family dictionary is pinned at 38c517ed358c08d776b59ab5def5856106dcdeb5.

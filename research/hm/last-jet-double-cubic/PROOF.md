# A corrected first-normal extractor identifies the double-cubic channel with the last vertex jet

## Result and status

Retain the actual regular (3,5) vertex presentation, its actual nonsplit quintic transitions, and physical positive parts. The inputs are PR649's canonical last-jet theorem at d46dafc564e1ba97b0813491d16c32bd2e73e12f and the three degree-eight/cubic results in PR543 at 14fc90d90f74998c10ea9f2b45cf5b8aeac96bae listed below. Write

 M = pi_* O_(2D)(-2,12), R = pi_* O_D(-2,12),
 N = pi_* O_D(-5,9), C = O_L(4),
 T = Wprime O_L(1).

Here N is the kernel of M -> R, and C is its scalar/class-of-N subbundle. Let E be the actual tangent coefficient bundle E8 and K=im H0(E) in H0(M). Then

 0 -> H0(C) -> K -> H0(R) -> 0                           (1)

is exact. Therefore there is a canonical linear extraction map

 Q:H0(M) -> H0(N/C) = H0(T),                             (2)

formed by removing any actual kernel section with the same reduced restriction and then taking the remaining first-normal component modulo the scalar subbundle. It has kernel K and restricts to the quotient map on H0(N).

More importantly, the bundle identification N/C=T is the actual quintic-remainder map, not an abstract identification of P4 representations. Under it, (2) is the same remainder as PR649's canonical last-vertex-jet projection after the actual connecting-map identifications. Thus reduced double-cubic data may be removed first, but its global lift must be included before taking the first-normal coefficient. This supplies an explicit map-level bridge and a precise reduction of the remaining operator calculation. It supplies no nonzero operator value.

## Pinned inputs

All following files are in research/hm/order-four-quadratic-load/ at the PR543 commit above:

- [ACTUAL-DEGREE-EIGHT-NORMAL-OPERATOR-QUOTIENT.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/14fc90d90f74998c10ea9f2b45cf5b8aeac96bae/research/hm/order-four-quadratic-load/ACTUAL-DEGREE-EIGHT-NORMAL-OPERATOR-QUOTIENT.md): 0 -> J -> E -> M -> 0, J=P4 O(-2), H0(J)=0, H1(E)=0; E has subbundle T6 O(-1) and quotient S4 O(7); this boundary is the actual global positive boundary via the square-ideal/wedge diagram, rather than a merely local boundary.
- [ACTUAL-DEGREE-EIGHT-DEFECT-AS-DOUBLE-CUBIC-PUSHFORWARD.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/14fc90d90f74998c10ea9f2b45cf5b8aeac96bae/research/hm/order-four-quadratic-load/ACTUAL-DEGREE-EIGHT-DEFECT-AS-DOUBLE-CUBIC-PUSHFORWARD.md): actual ratio r/g² on 2D, with r=fu+gv and transitions g_j=g_i+fp_ij.
- [ACTUAL-CUBIC-SUPPORT-IS-GENUS-FOUR-WITH-EXACT-FIVE-TORSION.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/14fc90d90f74998c10ea9f2b45cf5b8aeac96bae/research/hm/order-four-quadratic-load/ACTUAL-CUBIC-SUPPORT-IS-GENUS-FOUR-WITH-EXACT-FIVE-TORSION.md), section 6: N=C plus Wprime O(1), with C the actual scalar subbundle, and the nilpotent boundary 0 -> D5 -> H0(N) -> P4 -> 0.

- [ACTUAL-THIRD-VALUE-AS-MIDPOINT-DUALIZING-OPERATOR-DEFECT.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/14fc90d90f74998c10ea9f2b45cf5b8aeac96bae/research/hm/order-four-quadratic-load/ACTUAL-THIRD-VALUE-AS-MIDPOINT-DUALIZING-OPERATOR-DEFECT.md), sections 1 and 4 plus the final intrinsic filtration: the actual presentation M(4)=coker(B(4)->G(4)) and its quotient onto G|Z(4), with tau(sigma)=2N.

The last-jet input is [PR649's proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/d46dafc564e1ba97b0813491d16c32bd2e73e12f/research/hm/positive-restriction-channel/PROOF.md): H0(G|Z(4))_+=K_sec direct-sum T_sec, where T_sec=H0(J_vertex^4(G|Z(4)))_+=Wprime tensor H0(O_L(1)), and restriction of the actual boundary to T_sec is an isomorphism. Its subtraction of a lower-jet-matching actual global section is essential.

## 1. Every reduced residue is accounted for by the kernel

The coefficient quotient E -> S4 O(7) sends (v,u) to v. On D, the actual residue is

 (fu+gv)/g² |_D = v/g.

Multiplication by the global nowhere-zero g_D identifies R with pi_*O_D(3,7). The divisor sequence gives

 0 -> O_L(4) --f--> Sym³(Wprime) O_L(7)
   -> pi_*O_D(3,7) -> 0.                              (3)

There is no omitted higher direct image: the relative kernel before pushforward is O_Y(0,4), which has H1 on every fiber equal to zero. Hence H0(S4 O(7)) -> H0(R) is onto, with kernel H0(O(4)). Since T6 O(-1) has both H0 and H1 zero, H0(E) -> H0(S4 O(7)) is an isomorphism. Finally H0(E) -> H0(M) is injective by H0(J)=0. This proves that K -> H0(R) is onto with five-dimensional kernel.

That kernel is exactly the scalar subspace H0(C), not just an isomorphic D5: the globally defined scalar tangent delta_sigma=rho sigma has (v,u)=(rho f,rho g), and diagonal residue 2rho fg. In M this is twice its class-of-N section. Characteristic zero makes this an isomorphism on the scalar subspace. Thus (1) follows, including the intrinsic identification of its kernel.

## 2. Canonical projection after removing the reduced part

For m in H0(M), choose k in K with k|D=m|D, possible by (1). Then m-k lies in H0(N). Any two choices differ by H0(C). Since H1(C)=0, the class of m-k defines a unique element of H0(N/C). This proves that Q is well-defined. Its kernel is K because H0(C) is contained in K, and it is onto because H0(N)->H0(N/C) is onto. No preferred splitting of K->H0(R) is asserted or needed.

The actual boundary b on H0(M) therefore factors as

 b = b_N composed with Q,

where b_N:H0(N/C)->H1(J) is the isomorphism from the pinned nilpotent boundary theorem. This gives an exact, lift-independent projection. It is not the raw normal coefficient of m before reduced-part correction.

## 3. Intrinsic first-normal coefficient and quintic remainder

Locally write m=r/g². A kernel section k has actual compatible tangent coefficients (v,u) and expression (fu+gv)/g². Equality on D says r-fu-gv vanishes modulo f, on 2D. Thus the corrected first-normal section is locally

 beta = (r-fu-gv)/(f g²) |_D in O_D(-5,9).              (4)

Division by f here means the canonical conormal identification I_D/I_D²=O_D(-3,-3), not a choice of a normal retraction. The numerator is the difference of two actual glued sections on 2D, so (4) glues with the asserted line transitions. One must not differentiate an isolated r/g² and ignore its quintic transitions.

Multiplication by the global g_D² identifies O_D(-5,9) with O_D(5,-1). Under this map the scalar section rho/g_D becomes rho g_D. Consequently

 N/C = pi_*O_D(5,-1) / (g_D O_L(4)).                  (5)

The divisor sequence identifies pi_*O_D(5,-1) with

 Sym⁵(Wprime) O_L(-1) / (f Sym²(Wprime) O_L(-4)).

Quotienting further by g_D gives precisely the actual quintic algebra quotient

 Sym⁵(Wprime) O_L(-1) / (f Sym²(Wprime) O_L(-4) + g O_L(4))
   = Wprime O_L(1).                                  (6)

The sum in (6) means the actual relation subbundle K5(-1), not a nonexistent globally split quintic generator. Changes g->g+fp leave this subbundle and the quotient unchanged. Hence formulas (4)-(6) define the intrinsic extractor by taking the corrected normal coefficient, multiplying by g_D², and retaining its quintic remainder modulo the actual (f,g) ideal. Equivalently the local output is the quintic class [(r-fu-gv)/f] modulo (f,g). The numerator is divisible by f only after the reduced lift has been subtracted; its ambiguity modulo f² becomes an f-multiple after division and therefore vanishes in this final quotient.

## 4. Comparison to the canonical deepest vertex jet

Use the standard regular-section tangent convention

 delta_sigma=(v,u),
 delta_N=u S1+v S2,
 S1=[[f,0],[2g,-f]], S2=[[g,-2f],[0,-g]].

A nilpotent residue has v=af. Subtracting the gauge K sigma with K=diag(a,-a) gives the pure-u representative (0,u+ag), exactly r/f=u+ag. For a scalar class rho N, the tangent rho sigma/2 becomes pure-u rho g, which is precisely the g-multiple killed in (6). Its remaining ambiguity is u modulo f times a quadratic; taking the scalar quotient further removes u modulo g. Thus the resulting tangent restriction to Z is represented by (0,u), with u understood modulo (f,g).

This lies in J_vertex^4 G|Z(4): its only nonzero transverse component has cover degree five. It is exactly the deepest positive quintic layer of PR649. Its transition is intrinsic: with g_j=g_i+fp_ij, tangent coordinates transform by (v,u)->(v,u+p_ij v). Pure-u classes are unchanged, and changing their representatives by f or g vanishes on Z. The line factor is O_L(-1) on quintic coefficients, as in (6), yielding Wprime O_L(1). This constructs the map N/C -> J_vertex^4 G|Z(4) on the positive vertex projection explicitly and proves it is the identity on the common quintic quotient, rather than merely a nonzero equivariant scalar map.

For precision, the actual global defect has the intrinsic quotient rho in

 0 -> O_Z(4) -> M_global(4) --rho--> G|Z(4) -> 0,

where rho sends a tangent class to its restriction, and the first arrow is the class of sigma/2. Every gauge tangent K sigma restricts to zero on Z, so rho is well-defined. The pure-u construction above is its induced map on the degree-eight nilpotent piece,

 N8 --rho_N--> deepest positive vertex layer,
 ker rho_N=C,  and  rho_N(u/g_D²)=(0,u)|Z.           (7)

There is no factor two in (7): the factor two concerns only tau(sigma)=2N, and that scalar subspace is already killed.

The [positive-boundary theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/83eb365e87fe3aef3488aa339b73636fa845f630/research/hm/positive-boundary-duality/PROOF.md), section 3, defines d by the exact identity delta=d composed with H0(rho). The pinned degree-eight quotient theorem identifies b with this same delta using the actual square-ideal diagram. Restricting that diagram to (7) gives explicitly

 b|H0(N8) = d|T_sec composed with H0(rho_N).

This is the claimed map-level compatibility. Use the same convention for delta_N and the connecting homomorphisms throughout; reversing the convention reverses both boundaries. Therefore the double-cubic quotient is canonically represented by this actual deepest-jet section.

Ordinary line-frame changes give exactly the line factors in (6); triangular changes fix pure-u classes as already checked. All further actual frame changes commute with the intrinsic quotient rho, and determinant-one stabilizers I+tN act trivially on restriction because N has entries in I_Z². There is also no hidden higher-jet correction to (7): the positive J_vertex^4 layer is already the last odd layer, with higher odd layers zero. Thus its associated last-grade identification is an identification with the actual deepest subsheaf. This uses no global splitting of the full vertex filtration or of G on a neighborhood. For an arbitrary m, remove k as in section 2 before invoking this comparison. The lower-jet correction is precisely the actual kernel lift k and is not discarded by the normal extraction.

This assertion concerns classes and actual restriction maps. It does not assert that each homogeneous polynomial tangent representative extends as a global section of G(4), a claim explicitly avoided in the pinned quotient theorem.

## Contribution and stopping boundary

The reduction now requires only the corrected quintic remainder (4)-(6); the 27-dimensional reduced part of any operator residue is always removable by an actual kernel class. The ambiguity of that removal is exactly scalar and disappears in the same quotient. This proves a specific bridge between the two canonical P4 channels and spells out the correction that must accompany a first-normal calculation.

It does not prove that an uncorrected normal coefficient computes the answer, identify the actual corrected harmonic operator, evaluate its quintic remainder, or determine its image modulo the second-symbol subspace. Those remain separate actual-map dependencies. All formulas are universal for the pinned actual relation data, with no selected HM coefficients, matrices, ranks, points, scans, or large computations.

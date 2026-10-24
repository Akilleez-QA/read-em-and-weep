# Actual coherent capacity proves original degree-eighteen jet separation through order nine

## Statement and retained boundary

Retain the complete actual-geometric hypotheses and conclusions of PR1215, hence the original rank-four maximal ordered profile (1,1), its source and section gates, and precisely the full-positive coherent-image branch

    A_q=A(4)+O(-8),  A=Sym2 W,  im beta_K=A(2).

The actual original scalar line has degree minus eighteen in the genuine fifteen-dimensional constant ambient V18 O. Its coefficient system has dimension fifteen, not the complete dimension nineteen. Write T_j for its actual saturated order-j osculating bundle when the indicated generic rank is established, and B_j=ann(T_j) in the dual constant ambient.

This proof establishes the new higher-order conclusion

    P^j(O(18))* -> V18 O
    is an everywhere subbundle injection for 0<=j<=9,

    T_j=P^j(O(18))*=Sym^j W(j-18),
    rank B_j=14-j,
    deg B_j=-(j+1)(18-j),                            (1)

with the actual backward relations B_(j+1)=B_j^- and actual forward relations T_j^+=T_(j+1) in the range needed for (1). In particular the original degree-eighteen curve has global jet separation through order nine despite its incomplete coefficient system.

At the next derivative of B9, write its coherent image as

    im beta_(B9)=O(-2)(-D9),  e9=deg D9.

Then

    e9=0 or 12.                                      (2)

If e9=12, the divisor is the unique reduced twelve-point orbit, and equality forces B9=D(-18), where D=Sym4 W, as the actual fourth jets of an auxiliary degree-twenty-two scalar line in the dual constant ambient. This endpoint is a necessary conditional conclusion, not an occurrence or exclusion assertion.

The proof distinguishes new original higher-jet separation from the already proved first-order incidence results. It assigns no connection to a quotient and uses no horizontal splitting. Neither (2) nor the local defect delta in {0,12} is resolved; e9, delta and the original t=0 are three different quantities. Both F18 types, both dual-extension alternatives, the other triplet coherent-image branches, algebraicity, and whole-branch/profile exclusion remain outside the result. No actual coefficient, parameter, point, jet, tensor, matrix, instance rank, or normalization is selected or evaluated.

## 1. Complete immutable inputs and the known starting jets

INPUTS.json records three complete freshly fetched immutable sources, including commits, paths, Git blobs, UTF8 lengths and SHA256 hashes:

* PR1215 at 8ca4ccd046248752714a84dfb05aae42a6433f55, research/hm/rankfour-profile11-triplet-twelve-orientation/PROOF.md.
* PR1210 at b2d020a32a3ac5aaf5f264e33e2f930c16195c34, research/hm/rankfour-profile11-triplet-projected-ranktwo/PROOF.md.
* PR1199 at 95af2c0fa1e3cce92496a44ef9023708735e1ec7, research/hm/rankfour-profile11-triplet-deep-images/PROOF.md.

All their transitive actual-geometric hypotheses remain assumptions. Work over C on the physical binary-icosahedral line P(W*) with G=SL2(F5), det W=1 and the retained representation conventions. An invariant effective divisor is either empty or has degree at least twelve; one of degree twelve is exactly the reduced orbit D12. The degree-four representation is D=Sym4 W.

The complete actual inputs identify the original second and third jets and their annihilators:

    T2=A(-16), T3=S4(-15), T2^+=T3,
    B2=J, B3=J^-,
    rank B2=12, deg B2=-48,
    rank B3=11, deg B3=-60,
    B3=B2^-, B2/B3=O(12).                            (3)

The original scalar line and its first jets are contained in this actual principal-parts flag. The complete-versus-partial third-jet comparison supplies the actual injection

    B3 subset Sym14 W(-4),
    top B3<=-4.                                      (4)

PR1215 has already proved coherent fullness of beta_(B3) onto O(10). The induction below includes the capacity argument at j=3 for a uniform derivation and then continues it to j=8. Every new backward kernel lies in B3 and is therefore of negative top degree. No theorem for a rank-seventeen bundle is transferred to these bundles.

## 2. Coherent rank-one capacity in the actual constant ambient

We use the following direct consequence of the intrinsic backward-kernel construction. Let Q be an actual saturated subbundle of a constant bundle on the complex projective line, of rank n and negative top degree. Suppose its derivative has generic rank one and coherent image O(c). Then

    deg Q <= n c-n(n-1).                             (5)

To prove it, form Q0=Q and Q_(i+1)=Qi^- until zero. Each nonzero Qi has negative top degree, hence cannot be horizontal: its Grassmannian map would otherwise have zero differential and be constant in characteristic zero, forcing degree zero. Thus no nonzero horizontal residue remains.

The actual quotients Ri=Qi/Q_(i+1) admit coherent injections

    Ri -> R_(i-1)(-2),
    Ri -> O(c-2i).                                   (6)

The first quotient has rank one. Every positive later quotient therefore has rank one as well, and there are exactly n of them. Summing their actual degrees proves

    deg Q=sum_(i=0)^(n-1) deg Ri
         <=sum_(i=0)^(n-1)(c-2i)
          =n c-n(n-1).

These are coherent injections with all possible torsion deficits retained. No image is replaced by its saturation in this sum. Each derivative is formed only on an actual subbundle of the original constant ambient; the quotients in (6) receive no connection.

If equality holds in (5), every line injection in (6) has zero degree deficit. Thus each Ri is exactly O(c-2i), and every consecutive injection is an everywhere isomorphism. The forward transforms through that rank-one flag are therefore exact, with no hidden torsion at a crossing.

## 3. Duality and intrinsic principal parts reconstruct the next actual jets

For actual annihilator subbundles in dual constant ambients, the second fundamental forms are negatives of transposes. This follows by differentiating the identically zero pairing of local sections. In particular

    ann(B_j^-)=(ann B_j)^+                           (7)

as saturated bundles: the annihilator of the exact derivative kernel is the saturated span generated by the annihilator and its first derivatives. This statement concerns actual maps in the constant ambients, not a derivative on a quotient.

More explicitly, suppose B_j subset B_(j-1), B_j=B_(j-1)^-, and beta_(B_j) is coherently onto the actual normal line

    L=(B_(j-1)/B_j)(-2)=O(a).

Then B_j/B_(j+1)=O(a), where B_(j+1)=B_j^-. Duality identifies

    T_(j+1):=ann(B_(j+1)),
    T_(j+1)/T_j=O(-a),
    T_j^+=T_(j+1).                                  (8)

The rank increases by one. The transposed inclusion of O(-a-2) in B_j*(-2) is a subbundle inclusion because the original derivative was onto. Thus the actual derivative of T_j has the indicated full line image. This also verifies the generic rank increase directly rather than inferring it from coefficient completeness.

The universal principal-parts identity, proved in the complete PR1199 input, is

    P^j(O(d))*=Sym^j W(j-d),  0<=j<=d.              (9)

It is an identity for the intrinsic source bundle, valid for any actual scalar coefficient system. Let eta_j be the actual intrinsic differential-evaluation map from this source to the constant ambient. Its generic image is the span of the original scalar line and its derivatives through order j.

If T_j is already identified with eta_j and (8) gives a rank-(j+2) next forward span, then eta_(j+1) has generic rank j+2 and that saturated image is T_(j+1). The map factors regularly through T_(j+1), because its composition with the torsion-free ambient quotient vanishes generically. If source and target have the same degree, its determinant is a nonzero degree-zero section, so eta_(j+1) is an everywhere isomorphism onto T_(j+1). This proves actual global jet separation without assuming that the coefficient system is complete or that generic rank alone implies saturation.

## 4. The fixed degree sixty forces six consecutive coherent images to be full

Suppose the actual jets have been identified through order j, with 3<=j<=8, and

    B_j=B_(j-1)^-,
    n:=rank B_j=14-j,
    deg B_j=-(j+1)(18-j),
    B_(j-1)/B_j=O(18-2j).                           (10)

These hold at j=3 by (3). Because B_j is the actual backward kernel of B_(j-1), its derivative factors through the actual line subbundle

    beta_(B_j):B_j -> O(16-2j).                     (11)

It is nonzero by negative top and therefore has generic rank one. Its coherent image is O(16-2j)(-D_j), where D_j is invariant. Write e_j=deg D_j. Applying (5) to this actual coherent image yields

    -(j+1)(18-j)
       <= (14-j)(16-2j-e_j)-(14-j)(13-j).

The exact polynomial identity

    (14-j)(3-j)+(j+1)(18-j)=60

therefore gives

    (14-j)e_j<=60.                                  (12)

For j=3,...,8 one has 14-j>=6, so e_j<=10<12. Invariance forces D_j empty. Hence every map in (11) is coherently onto its line, not just generically onto it.

Its exact backward kernel B_(j+1) has rank 13-j and degree

    deg B_(j+1)=-(j+1)(18-j)-(16-2j)
               =-(j+2)(17-j).                       (13)

Equations (7)-(8) supply the actual next forward bundle T_(j+1), with quotient O(2j-16). It has rank j+2 and degree -(j+2)(17-j). The intrinsic source P^(j+1)(O(18))* from (9) has exactly that rank and degree. Section 3 therefore proves its everywhere isomorphism onto T_(j+1), completing the induction.

The six target line degrees in (11) are 10,8,6,4,2,0. The resulting last bundle is

    T9=Sym9 W(-9), rank T9=10, deg T9=-90,
    B9=ann(T9), rank B9=5, deg B9=-90.              (14)

Together with the retained lower jets, this proves (1). The repeated bound (12), rather than any computation of actual jet values or a completeness assertion, supplies each global saturation step.

## 5. The next coherent-image endpoint and its equality flag

The preceding final full quotient is

    B8/B9=O(0).

Thus the next actual derivative factors as

    beta_(B9):B9 -> O(-2).

It is nonzero by negative top. Write its coherent image O(-2)(-D9), with e9=deg D9. Capacity (5), now with n=5, gives

    -90<=5(-2-e9)-5*4=-30-5e9,
    e9<=12.                                         (15)

The invariant-divisor minimum proves (2). It does not force e9=0.

If e9=12, then D9=D12 and the coherent image is O(-14). Equation (15) is equality. By the equality clause in Section 2, the five actual rank-one quotients of the backward flag of B9 are

    O(-14), O(-16), O(-18), O(-20), O(-22).           (16)

Let Q0=B9 and Q_(i+1)=Qi^- for this flag. The last actual line is Q4=O(-22). Every adjacent coherent map in (16) is an everywhere isomorphism, so its actual successive forward transforms are Q3,Q2,Q1,Q0. Their ranks and degrees are

    Q4: rank1, degree-22,
    Q3: rank2, degree-42,
    Q2: rank3, degree-60,
    Q1: rank4, degree-76,
    Q0: rank5, degree-90.

At each stage the intrinsic principal-parts source of the auxiliary degree-twenty-two line has the same rank and degree. Applying the source comparison of Section 3, now with d=22, gives the actual identities

    Q4=O(-22), Q3=W(-21), Q2=A(-20),
    Q1=S4(-19), B9=Q0=D(-18).                       (17)

These auxiliary jets lie in the dual constant ambient V18* O. They are not confused with the original degree-eighteen jets T_j in V18 O. The auxiliary coefficient span is in fact all fifteen dimensions: the span of Q4 equals that of its derivative span B9, while H0(ann B9)=H0(T9)=0 by (14), so no constant vector annihilates the span of B9. This observation is conditional on e9=12 and does not establish occurrence or impossibility.

The endpoint proof stops at (2) and (17). It does not assume global tenth-jet separation of the original system. In particular equality of a coherent image with its saturation at j=9 has not been proved.

## 6. Contribution and exact stopping point

The new step promotes the original actual third jets to actual ninth jets. A fixed total degree of sixty controls each intrinsic coherent derivative defect of the successive negative annihilator bundles. While their ranks are at least six, a nonzero invariant divisor is too large, forcing coherent fullness; actual annihilator duality and equal-degree principal parts then turn it into global higher-jet separation.

At rank five the same bound reaches exactly twelve, so the argument correctly retains an endpoint rather than silently forcing another full derivative. Its positive endpoint has the rigid auxiliary flag (17). Neither endpoint, either local defect delta, the retained F18 or extension alternatives, nor any realization or algebraicity statement is decided.

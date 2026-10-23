# The actual plane boundary is everywhere surjective

## Theorem

For every actual hyperplane H containing the positive fixed plane R,

    H^i(H,B_H(5))=0 for i>0.

Consequently the actual relative plane boundary is an everywhere-surjective bundle map

    delta: H0(R,B_R(5)) tensor O_T -> C_lin(2),

where T=P(W*) and C_lin is the rank-five degree-26 hyperplane cokernel bundle. Since h0(B_R(5))=48, its kernel is a vector bundle G of rank 43 and degree -36:

    0 -> G -> 48 O_T -> C_lin(2) -> 0.

This identifies the image of the actual plane boundary with its full target. It does not determine the splitting of G or the rank of the six-to-ten smoothing map obtained by restricting this boundary to the actual divided-difference inputs.

## 1. Reduction to the ordinary square of a section-curve ideal

Write E=F_H(2). A regular section with zero curve C gives

    0 -> E(2) -> Sym^2 E(2) -> I_C^2(8) -> 0,
    Sym^2 E(2)=B_H(5).                                (1)

The ideal square is ordinary. The actual primary HM cohomology gives H^i(F_H(4))=0 for i>0. Indeed H1(F(4))=H2(F(3))=0, and the other needed ambient H2,H3,H4 groups vanish by the standard primary cohomology and Serre duality, in the restriction sequence

    0 -> F(3) -> F(4) -> F_H(4) -> 0.

These are the same actual primary vanishings used in NEGATIVE-VERTEX-EVALUATION-SCALAR.md, Section 4, and AMBIENT-BETA-SECONDARY-MAP.md, Section 1; no new multiplication rank is assumed. Thus E(2) has no higher cohomology. The section sequence twisted by two also gives

    H^i(I_C(5))=0 for i>0.                            (2)

It remains to prove H^i(I_C^2(8))=0 for i>0. We use different actual section curves at ordinary and at special parameters, without moving the bundle in moduli.

## 2. A plane interpolation lemma, including tangent schemes

Let Z1,Z2 be disjoint length-two complete intersections in P2, each lying on a line l1,l2 respectively. Assume l1 and l2 are distinct and their intersection is in neither scheme. Write

    I_Zi=(li,qi),       deg qi=2.

Then for a,b in {1,2},

    H1(I_Z1^a I_Z2^b(a+b))=0.                         (3)

Products and intersections of these ideals agree as sheaves because the supports are disjoint. No reducedness of either length-two scheme is required.

For the proof, residual by li decreases its corresponding exponent by one:

    (I_Zi^a:li)=I_Zi^(a-1).

The other ideal is unchanged, since li is a unit along the other scheme. The image on li is O_li(-2a). Starting with exponents (2,2) and total twist four, take residual successively by l1,l2. The trace terms are O_P1(0) and O_P1(-1); both have H1 zero. This reduces to exponents (1,1) at twist two. Quadratic evaluation onto Z1 disjoint-union Z2 is onto: l2 times linear forms interpolates freely on Z1 while vanishing on Z2, and l1 times linear forms does the converse. This proves (3) for (2,2); the same residual sequence proves (1,2) and (2,1), and the last interpolation argument gives (1,1).

All these positive-degree ideal sheaves also have H2=0, by their zero-dimensional quotients. We will also use that for a complete intersection T of two quadratics,

    H^i(I_T^2(4))=0 for i>0,                          (4)

from the square resolution 0->O(-6)^2->O(-4)^3->I_T^2->0.

## 3. Hyperplanes with three distinct determinant planes

At a parameter outside the twelve order-five points, choose a general section with zero curve

    C=C1 disjoint-union C2 disjoint-union C3,

where Ci are reduced plane conics in distinct determinant planes Pi=(hi=0). The checked classification supplies these curves, and nonzero vertex evaluation lets the section be chosen to avoid the negative vertex. The actual factor-fiber theorem says the three planes meet only at that vertex.

For i!=j, Zi,j=Cj intersect Pi is a length-two complete intersection on the line Pi intersect Pj. That line is not a component of Cj, by disjointness from Ci and plane Bezout. Within Pi, its two such lines meet at the avoided vertex, so the hypotheses of (3) hold for their two length-two schemes. This includes a tangent intersection supported at a single point.

Apply residual successively by h1,h2,h3 to I_C^2. The residual ideals are

    J0=I_C1^2 intersect I_C2^2 intersect I_C3^2,
    J1=I_C1 intersect I_C2^2 intersect I_C3^2,
    J2=I_C1 intersect I_C2 intersect I_C3^2,
    J3=I_C.

These identities hold for ordinary ideal sheaves. On its own conic each hi is one member of the regular pair of generators; on the other conics it is a nonzerodivisor on their ordinary infinitesimal neighborhoods.

At twists 8,7,6, the respective plane trace sheaves, after removing the squared conic equation of degree four, are

    I_Z1^2 I_Z2^2(4),
    I_Z1   I_Z2^2(3),
    I_Z1   I_Z2  (2).                                (5)

For each row the two Z schemes are those on the relevant plane. To justify the trace description, work separately near its own conic and near the two other conic intersections. These supports are disjoint, so their image ideals multiply; restriction of an ordinary square has image the square of the restricted ideal. Thus there is no replacement by symbolic vanishing.

The three trace sheaves have no higher cohomology by (3). The last residual is I_C(5), which is acyclic in positive degree by (2). The three residual exact sequences therefore prove

    H^i(I_C^2(8))=0 for i>0                           (6)

at every such hyperplane.

## 4. The twelve double-plane parameters

At a special parameter use the actual weight-two eigen-section constructed in SPECIAL-HYPERPLANE-ADJOINTS-ARE-EXACTLY-SQUARES.md. That proof gives

    C=Q disjoint-union Y,
    Q=(z,q0(y,u)),       Q'=(x,q(y,u)),
    I_Y=(x^2,xq,q^2,g),       g=kappa x z^2-a q,

where Y is the Ferrand double of Q', kappa!=0, q and q0 are binary quadratics with no common root, and a is a linear form in y,u coprime to q. Both q and q0 have nonzero y^2 and u^2 coefficients and no yu term. The coordinates x,y,z are inversion-even and u is odd.

Here the actual involution further forces a to be a nonzero multiple of y. Indeed the Ferrand quotient line is O_Q' with a character. The generator q and its image b=kappa z^2 are both even, so that character is even; the image a of the even generator x must therefore also be even. In span{y,u}, only y is even. In particular a is nonzero at every point of (z,q0).

Let T=Y intersect (z=0), Z=(a,q) in Pi=(x=0), and T0=Q intersect Pi. Their plane ideals are

    I_T=(x^2,q),       I_Z=(a,q),       I_T0=(z,q0).

T is a complete intersection of two quadratics. Z and T0 are disjoint length-two schemes supported on the distinct lines a=0 and z=0. The intersection of these lines is the negative vertex, avoided by both schemes because the u^2 coefficients of q and q0 are nonzero. Thus (3) applies to Z,T0, including the nonreduced length-two scheme Z at the isotropic fixed point.

The already verified exact colon identities give the residual chain by z,x,x:

    J0=I_C^2,
    J1=I_Q intersect I_Y^2,
    J2=I_Q intersect (I_Y^2:x),
    J3=I_C.

Their image ideals on the corresponding planes are

    q0^2 I_T^2,
    q^2 I_Z^2 I_T0,
    q^2 I_Z I_T0.                                    (7)

The second and third identities use the actual image calculations

    I_Y^2|Pi=q^2 I_Z^2,
    (I_Y^2:x)|Pi=q^2 I_Z,
    (I_Y^2:x^2)=I_Y.

At twists 8,7,6, (7) reduces to

    I_T^2(4),       I_Z^2 I_T0(3),       I_Z I_T0(2).

These trace sheaves have no higher cohomology by (3)-(4). Again the final residual is I_C(5). The residual exact sequences prove (6) also at all twelve special parameters.

## 5. The actual boundary and its kernel bundle

Equation (1), together with (6) and primary acyclicity, proves H^i(B_H(5))=0 for i>0 for every H.

On the universal hyperplane pi:X->T, the relative plane sequence is

    0 -> p*B(4) tensor pi*O_T(1)
      -> p*B(5) -> B_R(5) external-tensor O_T -> 0.

The negative normal coordinate and O_T(1) both carry their actual odd linearization. Taking the even derived direct image gives the boundary

    delta: H0(B_R(5)) O_T ->
           (R1 pi_*p*B(4))_- tensor O_T(1)
           = C_lin(2).

The following term (R1 pi_*p*B(5))_+ is zero by the theorem. Thus delta is everywhere onto. The rank and degree of its kernel are 48-5=43 and -(26+2*5)=-36.

Writing E5,+=(pi_*p*B(5))_+, the same sequence identifies the geometric kernel more precisely by

    0 -> A O_T(-4) -> E5,+ -> G -> 0.                 (8)

Thus G is the actual plane-restriction image of even twist-five hyperplane adjoints, not an arbitrary subbundle with the same numerical invariants. The prior rank-three odd twist-four section bundle supplies the first term in (8). The fiber dimensions in (8) are 3,46,43.

The relative boundary is now known to have full target everywhere, but the Hermite smoothing gate uses only the specific vectors q_+ times the polynomial-division quotients of moving squares. Their membership in G remains the actual compatibility question; boundary surjectivity alone does not establish injectivity of that six-dimensional input map.

## Dependencies

- SPECIAL-HYPERPLANE-ADJOINTS-ARE-EXACTLY-SQUARES.md, immutable pin 5ce98e6bef1fd849353f563b1ccfc62f4d28b8d9, including its universal colon verifier.
- HYPERPLANE-ADJOINT-EXHAUSTION-AND-SIX-TO-TEN.md for the nonexceptional three-conic geometry.
- NONZERO-VERTEX-EVALUATION.md, pin c779b2919a36b9d45a6319d46551bd6380154bba, for the avoided vertex.
- TORSION-FREE-HYPERPLANE-AND-QUADRATIC-TARGETS.md and the prior exact root-transform identities for C_lin and its twists.

No selected HM coefficients, matrix-rank computation, generic ribbon specialization, or balanced-splitting assumption enters the proof.

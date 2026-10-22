# Global meromorphic quintic source changes preserve the actual vector class

## New exact conclusion

The full pinned transition expression R is covariant in the ACTUAL coefficient frames, including its inhomogeneous source coefficient m and scalar correction Gamma. A change between any two global meromorphic normalized quintic generators changes their vector principal-parts representatives by the principal parts of ONE global meromorphic section of V O_L(-6). It therefore preserves the class already in H1(V O_L(-6)), before the connecting A quotient.

This supplies the global comparison needed for the divisor-defined quintic in UNIVERSAL-DIVISOR-QUINTIC-TWO-CHART-SHADOW-CANCELLATION.md. It does not assert that an arbitrary collection of local scalar differentials is global. The comparison is instead an exact bundle-frame identity and the full finite transition law.

## 1. Coefficient frames, including both inhomogeneous terms

Use a fixed global positive binary basis X,Y. On the negative line use z=t/s and the volume-compatible opposite coordinate w=-s/t=-1/z. The following are transformations of polynomial COEFFICIENTS in that fixed positive representation. Positive-cover root-line scaling is already accounted for by the coefficient twists and the Euler term in the actual cone operator.

Write eta for the actual Gram scalar primitive, reserving w for the opposite coordinate. For a normalized quintic generator g and its source coefficient

    m=(h f_z-n g)/f,

one has

    f_y=z^(-3)f_x,       g_y=z^5 g_x,
    p_y=z^8 p_x,         n_y=z^(-6)n_x,
    eta_y=z^2 eta_x,     a_y=z^(-2)a_x,
    u_y=z^(-2)u_x.                                       (1)

Here f has coefficient twist3, g twist-5, p twist-8, n twist6, eta twist-2, and a,u twist2. The coefficient h in Sym^4 Wprime is constant. The positive derivative transvectant is taken in X,Y on both charts.

Since partial_w=z^2 partial_z, the SOURCE relation gives the indispensable extra term

    m_y=z^2 m_x-3z h.                                    (2)

Similarly

    (a_y)_w=(a_x)_z-2z^(-1)a_x,
    Gamma_x=u_x+2k a_x(a_x)_z h,
    Gamma_y=z^(-2)Gamma_x-4k z^(-3)a_x^2 h,               (3)

and

    (p_y)_w=z^10(p_x)_z+8z^9 p_x.                       (4)

Neither m nor Gamma transforms as a homogeneous tensor of its formal twist. These identities come from the actual divisor relation and the pinned canonical scalar inverse, not a substituted connection with zero line action.

## 2. The complete frame cancellation

For source data (m,eta), the pinned expression is

    R(p;m,eta)=k a^2[-2tau(p,m)/15+2p tau(p,n)/5
                     +tau(p,p)n/5-tau(h,p_z)/15
                     +(2/3)p eta]-tau(p,Gamma)/30.       (5)

Every homogeneous term in(5) transforms by z^6. The inhomogeneous contribution from(2) and(4), after multiplying by k a_y^2, is

    -(2k/15)z^5 a_x^2 tau(h,p_x).

The extra contribution from(3) in the last term is

    +(2k/15)z^5 a_x^2 tau(h,p_x).

They cancel EXACTLY. Thus

    R_y=z^6 R_x,                                        (6)

the coefficient transition of V O_L(-6). The Gram term is retained throughout and has the same homogeneous transition. Formula(6) also holds for meromorphic source data and meromorphic p, because it is a universal identity. Its proof does not use the cubic eigenline coefficients or evaluate any actual source instance.

This is compatible with the full-frame harmonic theorem: base-diagonal and positive root-line factors have zero harmonic discrepancy, while the inhomogeneous coefficient terms in(2)-(4) provide their required covariance after the diagonal Gram elimination. No new unassembled normal transition is being discarded.

## 3. Exact source-change comparison in principal parts

Let g0 and g1 be GLOBAL meromorphic sections of the actual normalized quintic extension

    0 -> V O_L(-8) -> P4 O_L(-6) -> O_L -> 0,

both mapping to1. Then

    g1=g0+ell f

for one global meromorphic ell in V O_L(-8). Their actual source data satisfy

    m1=m0-ell n,       eta1=eta0+tau(ell,n).

The scalar transformation is the actual Gram-lift transformation, not an independently selected primitive. The complete finite transition identity is

    R(p+q;m,eta)=R(p;m,eta)
                  +R(q;m-pn,eta+tau(p,n)).              (7)

For any local regular target gi=g0+p_i f=g1+(p_i-ell)f, this gives

    R(p_i;m0,eta0)-R(p_i-ell;m1,eta1)
        =R(ell;m0,eta0).                                (8)

By(6), the right side is ONE global meromorphic section of V O_L(-6). Consequently the two collections of principal parts have the same image under the connecting map from principal parts to H1(V O_L(-6)). This is an equality before quotienting by the actual A image.

For completeness, choose an open set where g0 is regular and regular target generators near its poles. Formula(7) identifies the target-to-target cochain with the differences of R(p_i;m0,eta0), in their transported coefficient frames. Their principal-parts boundary is therefore the actual vector cochain. This construction is unchanged if one enlarges the pole divisor or refines the cover. It does not require a false global holomorphic quintic splitting.

## 4. Why the physical factor can be constant here

The positive quadric q0 is one FIXED global quadratic form on the positive three-space V. Fix the positive Gram identification V=Sym^2 Wprime once, and let q be its fixed determinant quadratic. Both span the same one-dimensional invariant quadratic line. Therefore

    q0=nu0 q,       nu0 in C*,                          (9)

with a single constant nu0. This is not a choice of a local equation varying with the negative base point.

In induced relative charts, normalize both equations by the same base line frame and the positive variables by their induced frame. Since both are homogeneous quadratics in those variables, q0 and q acquire the same factor, preserving nu0. The positive-cover root frame is likewise applied to both. Thus the physical representative is R/nu0 in(6)-(8), and the global meromorphic coboundary is divided by the SAME fixed nonzero scalar.

If some other local equation frame is used, its unit must be transported together with the numerator and the bundle frame. Inserting an arbitrary nonconstant factor into R alone would change the calculation and is not licensed by(9). No ordinary local derivative of q0 is set to zero in arbitrary frames.

## 5. Application to the divisor-defined quintic and its lower class

The divisor-defined g0 of the companion two-chart note restricts to the ACTUAL normalized nowhere-zero quintic section on D. Hence it is a global meromorphic lift in the actual ideal extension: away from its two base poles its difference from an actual regular lift is divisible by f, and its quotient in the displayed extension is1. Its finite poles do not change this rational-section assertion. The companion divisor computation and its exact polynomial identities establish these hypotheses without assigning values to A,B,c,lambda,k.

The actual n is fixed by the restriction isomorphism for O_D(2,6); the companion exact relation identifies it. The actual u is fixed by the canonical quotient inverse; the earlier C5 correction theorem identifies it. Finally the companion candidate eta0 has regular target transforms with the required cocycle. The difference from the actual Gram primitive would be a global section of O_L(-2), hence zero. Thus all three are the actual data required in(5).

Let alpha=B k lambda/(10A^2 c^2), a nonzero symbol. The companion full-expression verifier gives the principal parts

    R_x=alpha Y^2 z^(-2) modulo regular terms,
    R_y=-4alpha Y^2 w^(-4) modulo regular terms.         (10)

By the comparison above these represent the actual lower vector class, divided by nu0. They do NOT contradict a nonzero simple residue for the orthogonal generator: that generator gives different principal parts of the same class.

There is a useful additional lower-class conclusion. The global meromorphic section with x coefficient alpha Y^2 z^(-2) has y coefficient alpha Y^2 w^(-4). Subtracting it from(10) leaves just

    -5alpha Y^2 w^(-4) at y.                            (11)

For O(-6), the single-point principal parts w^(-1),...,w^(-5) form a cohomology basis. Hence(11) is NONZERO in H1(V O_L(-6)). Its C5 character is6: Y^2 has character4, the O(-6) fiber at y has character4, and w^(-4) has character8, whose sum is6 modulo10. The actual connecting A has only characters8,0,2, so this class remains nonzero modulo A.

Nevertheless cup by the square a=t^2 kills it. At x, a=z^2 makes the first part of(10) regular. At y, a=1 leaves -4alpha Y^2 w^(-4), which is the principal part of a global meromorphic section of V O(-4), with constant x coefficient -4alpha Y^2. Thus

    [aR/nu0]=0 in H1(V O_L(-4)),                        (12)

already before the upper D5 quotient. Statements(11)-(12) hold uniformly for an arbitrary stabilizer pair and the corresponding abstract eigenline inputs a=t^2,h=X^4. No particular HM point, coefficient value, matrix, or rank is selected. Extending the resulting detecting-channel exclusion to the entire square locus uses the separate square-channel and basepoint-exclusion theorem; no statement about the discriminant-divisible third channel is made here.

## Reproduction and sources

Run python verify_meromorphic_quintic_source_frame_covariance.py. It checks the full frame cancellation with independent binary forms, the exact finite composition identity, the source relation frame law, the Gamma frame law, and the lower/upper principal-parts arithmetic. The universal two-chart algebra is independently checked by verify_divisor_quintic_two_chart_cancellation.py and is not duplicated here.

Sources: ACTUAL-THIRD-SHADOW-AS-A-CANONICAL-VECTOR-COCHAIN.md; ACTUAL-CONE-DIAGONAL-IS-CANONICAL-RESIDUE-INVERSE.md; ACTUAL-NORMAL-OPERATOR-SQUARE-SHADOW-BY-HARMONIC-TRANSITION.md, especially Sections3-4; ACTUAL-POLAR-VECTOR-PARTS-DO-NOT-DEPEND-ON-REGULAR-QUINTIC-LIFTS.md; VERTEX-QUINTIC-RELATION-EXTENSION-AND-SQUARE-P4.md; ACTUAL-C5-SQUARE-CORRECTION-HAS-A-SIMPLE-ROOT.md; and the companion two-chart note.

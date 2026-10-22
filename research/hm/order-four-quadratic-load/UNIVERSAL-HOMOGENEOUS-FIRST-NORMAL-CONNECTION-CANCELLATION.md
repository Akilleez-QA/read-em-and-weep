# A concrete homogeneous first-normal connection cancellation

## Result, without a full-connection claim

For the uniform order-five square input a=t²,h=X²Y², the established degree-eight midpoint error and full Atiyah-source representative admit the following explicit HOMOGENEOUS LOCAL cancellation in the divisor frame:

    K=[[K11,0],[K21,-K11]],
    K11=-k(2A+B c²z⁵)/(12B c²),
    K21=lambda k(-11A c z²X²+5A XY+B c z³Y²)/(30AB c³z⁴),
    [K,n]=a(R_mid-theta R_t)-tau(V),   theta=-1/12.          (1)

All A,B,c,lambda,k remain unassigned nonzero parameters. The notation uses arbitrary normalized abstract eigenvectors, uniformly over the stabilizer orbit. There is no selected actual coefficient value, actual-instance rank, or scan.

The pair V below is the degree-eight Serre/fiber-product REPRESENTATIVE. It is not automatically a literal full actual G(4) section in every frame. Both regular triangular coefficient-chart checks hold, including the scalar adjustment, but a comparison with the full higher stabilizers remains necessary. Consequently K in (1) is not identified with the full actual first-normal connection needed in a fourth-stage calculation. No midpoint extension to 3Q or fourth value is asserted.

## 1. Data and normalization

Use the already licensed universal divisor presentation

    f=A X²Y+B Y³z+Ac X³z²-Bc XY²z³,
    g=-lambda(B XY⁴/z³+A X³Y²/z⁴)/(2Ac),
    n=[[fg,-f²],[g²,-fg]],   sigma=(f,g)^t,
    a=z²,   h=X²Y².

R_mid is the FULL homogeneous cover-q normal error from ACTUAL-MIDPOINT-ABSOLUTE-SECTION-FOR-THE-FOURTH-SQUARE-INPUT.md, not just its diagonal or effective vector shadow. The new verifier reconstructs all its entries independently from the universal first-normal product, using the actual matched first-normal Hessian correction and scalar inverse from that note.

Set

    D=2a partial_z+(a_z/2)(X partial_X+Y partial_Y),
    R_t=k a(Dn-2a_z n),
    (R_t)11=2ka partial_z(a f g).

This is the full Atiyah representative, with its determinant/line correction, not just a triangular lower term. Its identification is supplied by ACTUAL-ATIYAH-CLASS-HAS-AN-ABSOLUTE-DOUBLE-CUBIC-REPRESENTATIVE.md. Both R_mid and R_t satisfy the exact tangent equation

    2fg R11+g²R12-f²R21=0.                                (2)

In the common cover convention theta=nu gamma=-1/12. Let

    chi=A k/(3B c²),
    v1=k z⁵(Ac z²X³/6-A X²Y/2-2B zY³/3),
    v2=lambda k(A X⁵/(6Bc)+z X³Y²/(12c)-B Y⁵/(3Ac²)),
    V=(v1,v2)^t+(chi/2)sigma.                             (3)

The letter chi is intentional: it is not the previously used normal-equation connection coefficient rho=Dq/q=2a_z. The values theta and chi are the scalar matches in these coefficient/Serre conventions, not newly assigned values of an actual source parameter or invariant numerical constants independent of framing.

Write J0=[[0,-1],[1,0]], so n=sigma sigma^t J0, and use

    tau(V)=sigma V^t J0+V sigma^t J0
          =[[fV2+gV1,-2fV1],[2gV2,-fV2-gV1]].             (4)

The global wedge/Serre-lift construction is a separate cohomological input. This note checks (1) and the coefficient-frame identities for its explicit representative; it does not replace that construction with a chosen local pair.

## 2. Divisibility gives the entire commutator, not just its diagonal

Put E=a(R_mid-theta R_t)-tau(V). Direct universal simplification gives

    E11=f² lambda k(-11A c z²X²+5A XY+B c z³Y²)
                    /(30AB c³z⁴),
    E12=f² k(2A+B c²z⁵)/(6B c²).                          (5)

The source pair is regular in positive coordinates, so f² and g² are coprime there. Since tau(V) is tangent, (2) also holds for E. In fact f²|E11 alone forces f²|E12 from that tangent equation. Thus

    K21=E11/f²,   K11=-E12/(2f²),   K12=0

are polynomial in X,Y, with only the displayed meromorphic base coefficients. These definitions match entries11 and12 of [K,n]. Equation (2) then forces entry21 as well:

    [K,n]21=2fg K21-2g²K11
            =(2fg E11+g²E12)/f²=E21.

This proves (1) exactly in all entries. Within the gauge K12=0 it is the unique trace-free solution for this particular E. This is a local coefficient-gauge statement, not a uniqueness theorem for full actual ambient connections.

The sign is also fixed: if E is the positive first-normal error, adding -q K to its local operator connection cancels E. Equation (1) itself is [K,n]=E, not its negative.

## 3. Both regular coefficient charts, including the scalar term

Let w=-1/z be the volume-compatible opposite coordinate. The actual regular triangular target changes are

    p_x=lambda XY/(2Ac z⁴)-lambda X²/(2A z²)
                         +lambda B Y²/(A²z),
    p_y=-lambda Y²/(2Ac²w²)+lambda X²/(Bc²w),
    f_y=z^(-3)f,   g_y=z^5g.

For the degree-eight Serre/fiber-product coefficient pair the factors are

    V1,y=z^(-7)V1,   V2,y=z V2,   chi_y=z^(-4)chi.          (6)

They are consistent because v1 has bidegree(3,7), v2 bidegree(5,-1), and the wedge fV2-gV1 has bidegree(8,2). In particular chi sigma has exactly the same two coefficient weights as V.

At x, v1 is divisible by z⁵ and p_x has pole order at most four. Hence v2+p_x v1 is regular. Adding the scalar term changes it by (chi/2)(g+p_x f), also regular, and V1 is regular as well.

At y one obtains the exact cancellation

    v1,y=k(Ac X³/6-A X²Y w²/2+2B Y³w/3),
    v2,y+p_y v1,y
       =lambda k(11X²Y³/(12c²)-A X⁴Y w/(2Bc²)).           (7)

The scalar adjustment adds

    (chi_y/2)(g_y+p_y f_y),   chi_y=chi w⁴,

to the second component, and adds (chi_y/2)f_y to the first. All are regular on the full y coefficient chart. Equations (6) and (7), not a bare pole-order guess, verify the complete scalar-adjusted pair in both triangular coefficient frames.

These computations do NOT prove that the full actual Serre bundle has only these triangular homogeneous transitions.

## 4. Exact higher-stabilizer ambiguity

There is a concrete reason the wedge and these coefficient-chart checks do not identify the full lift. For an arbitrary stabilizer

    P=I+epsilon n,

one has n²=0 and P sigma=sigma. If

    w_V=fV2-gV1,

then the exact identities are

    nV=-w_V sigma,
    P V=V-epsilon w_V sigma,
    tau(P V)=tau(V)-2epsilon w_V n.                       (8)

Thus the wedge remains unchanged, while its Serre representative changes by a possibly higher-cover scalar-kernel term. The verifier proves (8) with fully independent symbolic f,g,V1,V2,epsilon. No source instance is chosen.

A global wedge together with H1(O(4))=0 can establish existence of a global actual G(4) lift. The established square-ideal diagram can identify its degree-eight representative up to the scalar kernel. Neither statement alone compares all the higher terms in (8). Those must be transported together with the full operator/frame data before the K in (1) can be called the full actual next connection.

This matters for a specific algebraic reason, not merely dimensional caution. UNIVERSAL-SECOND-NORMAL-HARMONIC-PRODUCT-AND-OPERATOR-DEFECT.md retains the OLD first-normal connection through [K,t]+[K,n]_1 at the next division. Its elimination at the first stage is therefore insufficient for the second. No claim is made that a remaining higher correction is nonzero, only that it has not been calculated or shown irrelevant.

## 5. Physical equation and reproduction

The matrices in this note use the cover equation q. For q0=nu q the same correction is -q0(K/nu), and the physical error is E/nu. Derivative/connection transport of a variable nu must be included as in the second-normal harmonic note. No factor of nu is silently fixed by selecting source coefficients.

Run python verify_homogeneous_first_normal_connection_cancellation.py. It reruns the frozen absolute-source verifier, independently reconstructs R_mid from the first-normal product, checks both divisibilities in (5), verifies all entries of (1), verifies both complete scalar-adjusted coefficient charts, and checks the universal higher-stabilizer identities. The calculation is a reproducible homogeneous cancellation certificate, not a full actual fourth-stage division.

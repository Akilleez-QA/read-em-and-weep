# The full four-block supertrace projects with one explicit differential defect

## Result

The remaining four-block wedge in the pivot representative admits an exact rank-two projection. The useful source-specific cancellation is that the difference of the two split connections is a chain map. This removes one of the two differential defects in the general product formula, but leaves a particular covariant-differential/contraction term.

After the further weighted-supertrace cancellation proved below, the complete scalar representative on an increasing edge is

    t'_cd,ij = (1/4)[-tr(kappa_i wedge L_ij^t)
                    +K_(h_i)(T_i,Z_ij)
                    +(eta_ij/2) wedge tau_j
                    +15q_ij wedge d_i]_cd
                    -15q_c,ij q_d,ij/8.                   (R)

Here T_i is the covariant derivative of the actual differential D for the i-th pivot connection. Formula (R) retains one explicit full-complex contraction term, the displayed connection/scalar terms, and the original edge gerbe correction.

Write A_i for the preceding note's Btilde_i, and set

    eta_ij = -2(a_j-a_i),
    Z_ij = A_j-A_i-k eta_ij/2 = nabla'_j-nabla'_i,
    S_ij = A_i+A_j,
    a_bar = (a_i+a_j)/2,
    T_bar = nabla_(a_bar) D.

Choose any of the accepted source contractions (I,P,h), with its rank-two cohomology in degree zero. Put s=P S I and z=P Z I. Then

    Wtilde_ij = (1/2) tr(s^0 wedge z)
               + K_h(T_bar,Z)
               -(eta_ij/4) wedge(tau_tilde_i+tau_tilde_j),  (1)

where z is traceless, tau_tilde_i=tau_i-30d_i, and the full remaining defect is

    K_h(T,Z)_cd
      = str(h T_c Z_d-h T_d Z_c)
        -tr(P T_c h Z_d I-P T_d h Z_c I).                   (2)

Neither term in (2) is silently omitted. Formula (1) is a full supertrace identity, not merely a formula for one matrix projection. Section 5 identifies the properly transported z with -L_ij^t and reduces the first term of (1) further to -tr(kappa_i wedge L_ij^t), where kappa_i is the tracefree local cohomology connection coefficient defined there. It does not prove K_h=0. An explicit tiny invented acyclic control below has K_h nonzero, even with the relevant trace and chain-map conditions.

## 1. Source conventions and the two gradings

Use the [first-order source, sections 1, 2 and 4](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-residual-attribution/first-order-source.md), the [physical-frame theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-geometric-dependencies/frames-and-poles.md), and the determinant reduction [published at 5afa438](https://github.com/Akilleez-QA/read-em-and-weep/commit/5afa4389419d9187104612b07e39558e9c4a7b92). The pivot-connection note supplies the regular forms a_i, d_i=gamma_i-a_i, and eta_ij=q_ij+2 delta_S d_ij. Here A_i=B_i+k d_i is the difference between the actual split connection and the pivot line connection.

The complex has internal degrees -1,0,1,2, giving the source supertrace signs (-,+,-,+). D has internal degree +1, h has degree -1, and I,P connect the cohomology, in internal degree zero, with the complex. The accepted contraction identities are

    P I=1,  D I=0,  P D=0,
    E=I P=1-Dh-hD.                                        (3)

Throughout this note h or h_i means this complex contraction. It is distinct from the scalar vertex correction h_r=(1/4)contraction_r(d_i wedge tau_i) in the pivot-descent note; the latter is not used as a homotopy here.

The internal-degree-zero coefficient matrices A_i,c, S_c and Z_c are even. T_c=[D,A_c] has internal degree +1. All supertrace cyclic signs below refer to this internal grading.

Exterior form coefficients use the source's ordinary wedge convention. In particular

    (A wedge B)_cd=A_c B_d-A_d B_c.

We establish identities for these coefficients before antisymmetrizing c,d. We do not import a total Cech/forms product sign into this ordinary-wedge calculation. All matrices and contractions are transported to one common physical ambient frame, and all derivatives are physical. The chosen contraction is held fixed for each algebraic identity; its later physical derivatives must be included if the expression is differentiated.

## 2. Universal supertrace and product identities

For any internal-degree-zero X,

    str(X)=tr(P X I)+str(h[D,X]).                           (4)

Indeed str(E X)=tr(P X I), while

    str((1-E)X)=str(DhX+hDX)
               =-str(hXD)+str(hDX).

The minus sign is essential: D and hX are both odd. No cyclic permutation of Cech endpoints is used.

For degree-zero A,B, put T_A=[D,A] and T_B=[D,B]. Then

    str(A B)
      = tr((P A I)(P B I))
        +str(h(T_A B+A T_B))
        -tr(P T_A h B I)+tr(P A h T_B I).                   (5)

To prove this, apply (4) to AB and insert 1=IP+Dh+hD between A and B in PAB I. The Dh term is

    P A D h B I = -P T_A h B I,

using P D=0. The hD term is

    P A h D B I = P A h T_B I,

using D I=0. This proves all three error terms and their signs.

When B is a chain map, T_B=0 and the formula shortens exactly to

    str(A B)=tr((P A I)(P B I))
             +str(h T_A B)-tr(P T_A h B I).                 (6)

Thus chain-map status of just one factor removes the two T_B contributions; it does not remove the two surviving terms in (6).

## 3. What the actual source cancels

Let k be the diagonal source weight operator with weights (-1,1,3,5). Every component of D raises the line weight by 2, so

    [D,k]=-2D.

The flat split connection commutes with D. Since A_i=nabla'_i-nabla_(a_i),

    T_i=[D,A_i]=nabla_(a_i)D=dD+2a_i D,
    T_i-T_j=2(a_i-a_j)D=eta_ij D.                          (7)

All equalities in (7) are in the common physical frame. In particular

    [D,Z_ij]
      = T_j-T_i-(eta_ij/2)[D,k]
      = -eta_ij D+eta_ij D=0.                              (8)

This is the genuine differential cancellation. Z is precisely the difference of the actual split connections, as the first-order source also guarantees directly. Moreover

    [D,S_ij]=T_i+T_j=2 nabla_(a_bar)D=2T_bar.               (9)

The covariant derivative remaining in (9) is explicit. In a common line frame where w_i and w_j are the pivot-section coefficients,

    T_bar=dD-(1/2)dlog(w_i w_j) D.

This expression uses no square root. It retains the physical derivative of D.

There is also an exact trace cancellation particular to the accepted source. To avoid conflicting with S_ij, call the two middle splitting matrices U0_i and U1_i. Their determinant-ratio identity gives

    str(B_i)=-dlog det(U0_i)+dlog det(U1_i)=0.

The old connection term has canceled here because str(k)=sum sigma_r n_r k_r=0. Thus

    str(A_i)=0,  str(S_ij)=0,  str(Z_ij)=0.

Since Z is a chain map, (4) now implies

    tr(z)=tr(P Z I)=str(Z)=0.                              (10)

Consequently tr(s wedge z)=tr(s^0 wedge z), with s^0=s-tr(s)I/2. The source does not make s itself traceless automatically: (4) gives tr(s)=-str(h[D,S]). No trace component is lost by using s^0 in the product with z.

## 4. Full projection of the remaining wedge

Put tau_tilde_i=str(k A_i)=tau_i-30d_i. Ordinary coefficient cyclicity gives str(A_i wedge A_i)=0 and str(A_j wedge A_i)=-str(A_i wedge A_j). Hence

    str(S_ij wedge Z_ij)
      =2 str(A_i wedge A_j)
        +(eta_ij/2) wedge(tau_tilde_i+tau_tilde_j),

or

    Wtilde_ij=(1/2)str(S_ij wedge Z_ij)
              -(eta_ij/4) wedge(tau_tilde_i+tau_tilde_j).    (11)

The second sign follows from S wedge eta=-eta wedge S. This step uses only cyclicity of the ordinary matrix coefficient trace, not a cyclic Cech cochain trace.

Apply (6) to S_c Z_d and S_d Z_c. Using (9),

    (1/2)str(S wedge Z)_cd
       =(1/2)tr(s^0 wedge z)_cd
         +str(h T_bar,c Z_d-h T_bar,d Z_c)
         -tr(P T_bar,c h Z_d I-P T_bar,d h Z_c I).           (12)

Equations (11)-(12) prove (1)-(2). They retain the whole original supertrace, including both cohomology-projection terms. No identification of the separate non-chain-map coefficients A_i with cohomology connections has been assumed.

The rank-two endomorphism z is the induced difference of the actual split connections. Its identification with a particular row-current transpose requires matching the split cohomology basis, the determinant-one normalization, and the reference frame. This is done next with the whole ambient line weight included.

## 5. Physical cohomology normalization and the local-current term

Choose the contraction at the source vertex i. Distinguish the algebraic primitive columns I_alg,i from the cohomology columns of the physical splitting. In the prescribed i-th ambient line frame, the middle split cohomology columns are

    I_alg,i diag(1,nu_i^(-2)).

The middle ambient bundle has line weight +1. Transporting that ambient frame to a common reference therefore multiplies these columns by nu_i. The actual cohomology frame in that common ambient reference is

    I_i = I_alg,i diag(nu_i,nu_i^(-1)),
    P_i = diag(nu_i^(-1),nu_i) P_alg,i.                     (13)

These are exactly the determinant-one physical column frames in the pinned transition formula. In particular

    G_ij=P_i I_j=g_ij^t.

Comparing the untransported own-frame split columns would produce a spurious scalar nu_i/nu_j in this transition. Equation (13) includes the ambient line-frame transport and removes that error.

The split connection makes the entire physical split basis parallel. Thus its induced connection in its own frame I_i is zero. The induced difference Z=nabla'_j-nabla'_i, expressed in frame i, is consequently

    z=P_i Z I_i=-dG_ij G_ij^(-1)=-L_ij^t,                 (14)

with L_ij=g_ij^(-1)dg_ij and the source's row/column convention. All derivatives of the line factors in (13) are included.

Let

    kappa_i=(P_i A_i I_i)^0=-(P_i dI_i)^0.                 (15)

For the second equality, dI_i+Omega_i I_i=0 in the common ambient frame and A_i=Omega_i-k a_i. The operator k acts as +1 on the middle bundle containing I_i; hence the subtracted a_i I is central and disappears only after taking the tracefree part. Equation (15) is stated in the prescribed physical cohomology basis, not after an arbitrary new nonconstant cohomology gauge change.

Since A_j-A_i=Z+k eta/2,

    s^0=(P_i S I_i)^0=2kappa_i+z=2kappa_i-L_ij^t.

Ordinary coefficient cyclicity gives tr(z wedge z)=0. Therefore

    (1/2)tr(s^0 wedge z)=-tr(kappa_i wedge L_ij^t),
    Wtilde_ij=-tr(kappa_i wedge L_ij^t)+K_(h_i)(T_bar,Z)
               -(eta_ij/4) wedge(tau_tilde_i+tau_tilde_j). (16)

The local cohomology connection/current term is now explicit. The remaining K_(h_i) still uses the full complex, and (16) does not identify it with zero.

## 6. Weighted supertrace localizes the remaining defect to vertex i

The cohomology lies in internal degree zero, where the source weight operator k acts as +1. Apply (4) to kZ. Since [D,Z]=0, [D,k]=-2D, and tr(PZI)=0,

    str(kZ)=tr(P kZ I)+str(h[D,kZ])=-2str(hDZ).

On the other hand Z=A_j-A_i-k eta/2 and str(k^2)=-30 give

    str(kZ)=tau_tilde_j-tau_tilde_i+15eta,
    str(hDZ)=-(1/2)(tau_tilde_j-tau_tilde_i)-(15/2)eta.      (17)

There is no exterior sign in applying (4) to each coefficient kZ_c. The wedge signs enter only in the following antisymmetrization.

Because T_bar=T_i-eta D/2 and P D=0, equation (2) gives

    K_h(T_bar,Z)=K_h(T_i,Z)-(eta/2) wedge str(hDZ)
               =K_h(T_i,Z)+(eta/4) wedge
                                      (tau_tilde_j-tau_tilde_i).

The term proportional to eta wedge eta is zero. Combining with (16) yields the ordered-edge formula

    Wtilde_ij=-tr(kappa_i wedge L_ij^t)+K_(h_i)(T_i,Z)
                            -(eta/2) wedge tau_tilde_i.    (18)

This removes the average connection and the second endpoint weighted trace from the wedge projection. It does not remove K_(h_i)(T_i,Z).

## 7. The resulting scalar representative

The preceding all-tensorial representative was

    t'_cd,ij=(1/4) contraction_cd [
        Wtilde_ij+(eta_ij/2) wedge(tau_i+tau_j)
        +30d_i wedge d_j]-15q_c,ij q_d,ij/8.

Substitution of (1) gives the smaller exact formula

    t'_cd,ij
      =(1/8)tr(s^0 wedge z)_cd+(1/4)K_h(T_bar,Z)_cd
        +(1/16)[eta_ij wedge(tau_i+tau_j+30d_i+30d_j)]_cd
        +(15/2)(d_i wedge d_j)_cd
        -15q_c,ij q_d,ij/8.                                (19)

With the source-vertex-i normalization of section 5, this is equivalently

    t'_cd,ij
      =-(1/4)tr(kappa_i wedge L_ij^t)_cd
        +(1/4)K_(h_i)(T_bar,Z)_cd
        +(1/16)[eta_ij wedge(tau_i+tau_j+30d_i+30d_j)]_cd
        +(15/2)(d_i wedge d_j)_cd
        -15q_c,ij q_d,ij/8.                                (20)

The first-vertex version (18) is smaller still. Since tau_tilde_i=tau_i-30d_i, substitution into the full scalar leaves the scalar-form part

    (eta/2) wedge tau_j+15eta wedge d_i+30d_i wedge d_j.

Using eta=q+2(d_j-d_i) gives the exact additional cancellation

    15eta wedge d_i+30d_i wedge d_j=15q wedge d_i.

Thus the final compact ordered-edge representative is

    t'_cd,ij = (1/4)[-tr(kappa_i wedge L_ij^t)
                    +K_(h_i)(T_i,Z)
                    +(eta/2) wedge tau_j
                    +15q wedge d_i]_cd
                    -15q_c,ij q_d,ij/8.                   (21)

The expression is evaluated on the fixed increasing source edges, then extended with the admitted alternating convention. Its asymmetric first-vertex presentation is an identity for the same global tensorial cochain t-prime, not a different choice of source order.

The old q-gerbe term remains exactly the original one. Its complementary derivatives vanish for the previously proved separated-coordinate reason. The same statement is false in general for eta, d_i, T_i, z, or h. In particular, applying E to (21) differentiates all occurrences of I,P,h and D as well as the connection coefficients. The q wedge d_i term still has the derivatives of d_i; it cannot be dropped using q's separated dependence.

## 8. Tiny formal control of the surviving sign and term

This is an invented rational complex, not a physical source substitution. It checks that the remaining term can be present even when Z is a chain map, its induced rank-two map is zero, and the unweighted source-like traces vanish.

Over a ring in which r=1+x and u=1+y are units, take C^0 of dimension 3 and C^1 of dimension 1. The first two coordinates of C^0 are cohomology, and the last coordinate maps to C^1 by D=r. Let h=1/r on that contractible pair, with I,P the inclusion and projection of the first two coordinates. Then (3) holds.

Take all omitted coefficients to be zero and put

    A_i,x|C^0=diag(-1/r,0,1/r),   A_i,x|C^1=0,
    Z_y|C^0=diag(0,0,1/u),        Z_y|C^1=1/u,
    A_j=A_i+Z,  a_i=a_j=0,  eta=0.

Here [D,Z]=0, str(A_i)=str(A_j)=str(Z)=0, PZI=0, and

    T_bar,x=[D,A_i,x]=partial_x D=1,
    Wtilde_xy=1/(r u),
    K_h(T_bar,Z)_xy=1/(r u).

The rank-two product in (1) is zero, and the second trace in (2) is zero; the first supertrace is exactly the displayed nonzero answer. These values follow directly by multiplying the single contractible-pair entries. No runtime or physical evaluation is used. The control checks the algebraic term and its sign; it is not a counterexample to a source-specific cancellation or global-boundary theorem.

The accompanying `test_supertrace_projection.py` independently checks (4)-(6) on tiny invented graded complexes with rank-two cohomology. It contains no physical source data. Those universal controls do not substitute for the source transport argument (13)-(16).

## 9. Exact scope of the progress

The new cancellations are [D,Z]=0, tr(PZI)=0, the zero coefficient trace of the self-current wedge, the weighted-supertrace localization (17)-(18), and the scalar-form cancellation leading to (21). What survives is the particular two-term K_h in (2), built from the source's covariant derivative of D, its accepted contraction, and an actual chain-map difference. Formula (21) is now an explicit rank-two-connection-plus-contraction version of the global scalar representative.

To continue toward a boundary, one must handle the complementary E images of all terms in (21), including K_h, against the already known Omega+Q2+Q4. This note establishes neither their cancellation nor their nonvanishing. It does not change the global class comparison R(t')=R_raw+delta_S H. It supplies no finite cutoff, detector-domain assertion, physical source value, coefficient enumeration, or execution authorization.

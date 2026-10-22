# An actual lowest-normal connection contribution to the next error

## Result and strict boundary

For the already fixed multiplied corrected midpoint source a=t^2, h=X^2Y^2, the lowest first-normal connection coefficient K_0 has an explicit actual-compatible description in both complete regular charts. Its contribution

    C_K=([K_0,t_4]+B1(K_0,n)-B1(n,K_0))_11           (1)

to the next harmonic error is a nonzero degree-four polynomial on the regular x chart, specified exactly in Section4 and the verifier.

This is ONE LOCAL TERM of the actual next-division formula in its fixed harmonic frame. It is not the full next error, an intrinsically glued class of that isolated summand, or a fourth Bockstein value. Other terms may cancel it. No global second-normal midpoint extension is asserted: the actual endpoint nilpotent fails to glue, and that failure is explicitly bounded below.

We identify only K_0, not the full actual K. The conic correction and all higher stabilizers are retained in the comparison, not set to zero. Every source parameter remains unassigned.

## 1. Fixed actual input and sign of the correction

Use the actual divisor data f,g,a,H,A,theta,T from ACTUAL-MIDPOINT-ABSOLUTE-SECTION-FOR-THE-FOURTH-SQUARE-INPUT.md and UNIVERSAL-HOMOGENEOUS-FIRST-NORMAL-CONNECTION-CANCELLATION.md. Here theta=-1/12 is the previously forced comparison coefficient in these conventions, not a new assignment to a source parameter. The unmultiplied symbol is H=k a h, a=z^2. The full multiplied symbol through first normal order is

    Hhat=L(H0)+q H1,
    H0=aH,     H1=-theta k a^2.                     (2)

The q-symbol term is the fixed gamma/Atiyah correction. It must be included in connection transport. The frozen finite-transport note's DISPLAYED first-normal coefficient formulas assumed no additional q-symbol. For (2), its first error must be augmented by

    R1_new=R1_frozen+H1 Dn.

This is the actual source of the derivative part of the fixed Atiyah correction. It is retained in the imported complete midpoint error and cannot be omitted while reusing the old coefficient formula. Likewise its finite-transport counterpart H1 Ds times n appears explicitly in (5). The harmonic scalar lift and the fixed normal-line action are those of the actual midpoint construction; they are not varied to force a cancellation.

In the meromorphic DIVISOR frame the previously constructed positive cancellation primitive is

    Kplus=[[b,0],[d,-b]],
    b=-k(2A+Bc^2z^5)/(12Bc^2),
    d=lambda k(-11Ac z^2X^2+5AXY+Bc z^3Y^2)
                               /(30ABc^3z^4).      (3)

It satisfies [Kplus,n]=E_8. Therefore the ADDED normal connection coefficient is Kdiv=-Kplus, not Kplus. The full actual G(4) lift replaces the homogeneous V0 by V0+sigma r_i, with r_i of cover degree eight; Section3 shows that this changes only higher connection weights.

It would be incorrect to identify -Kplus with a regular-chart coefficient by ordinary conjugation alone. Its lower entry after the x triangular conjugation still has z^-2 poles. The affine harmonic transport below removes them exactly.

## 2. Complete affine harmonic transport and regular charts

For homogeneous even binary entries the actual first product correction is

    B1(p,r)=tau2(p,r)/[2(deg p-1)(deg r-1)(deg p+deg r-1)],

with B1=0 when either degree is below two. Matrix B1 uses ordered matrix multiplication with this scalar rule entrywise.

Let P be the marked triangular/root cone transition and Q=P^-1. Its canonical harmonic lift has inverse L(Q) through this order: every nonconstant positive entry is in the same strictly lower triangular position, so the potential B1 inverse correction vanishes. Expanding the FULL transported connection gives the normal coefficient

    K^P=tf( P Kdiv Q + B1(P,A0)Q+B1(PA0,Q)
              -B1(H0,DP)Q-B1(H0 DP,Q)-H1(DP)Q ),   (4)
    A0=aA.

The last term comes from (2). The trace-free operation transports the actual determinant marking. Formula (4) follows directly from L(p)L(r)=L(pr)+qL(B1(p,r)); it is not a guessed conjugation of an isolated commutator primitive.

For the regular x chart, P=[[1,0],[p_x,1]]. The second derivative-product term in (4) vanishes for this triangular P. The resulting ACTUAL-COMPATIBLE coefficients are

    Kx11=k(2A^2-7ABc^2z^5+16B^2c^4z^10)/(12ABc^2),
    Kx12=0,
    Kx21=lambda k z [72A^2X^2cz^2+10A^2XY
             -48ABX^2c^3z^7-72ABXYc^2z^5
             -43ABY^2cz^3+48B^2Y^2c^3z^8]/(30A^3c).

The other diagonal entry is -Kx11. Every entry is polynomial in the full chart variables z,X,Y.

For the opposite full root chart put z=Z^2, w=-1/Z^2, and use positive coordinates (X_y,Y_y)=(X/Z,Y/Z). Starting from the divisor frame, the marked transition is

    P=P_y(root) diag(Z^-9,Z^5),   det P=Z^-4,
    Droot=Z^3 partial_Z+Z^2(X partial_X+Y partial_Y).

The cone operator has physical twist six and q has twist two. Hence the q-connection coefficient in (4) has root factor Z^-8. Applying that factor, the full root substitutions, and tf gives

    Ky11=3Ak w^4/(2Bc^2),   Ky12=0,
    Ky21=lambda k(58AX^2w^3+31BcXY-53BY^2w^2)
                                             /(30B^2c^4).

Again Ky22=-Ky11, and all entries are regular. Before tf, both diagonal entries have a common -k/(6w) term. This is precisely the determinant scalar and NOT an unremoved pole of the trace-free connection. Omitting the determinant correction would incorrectly make the opposite chart fail.

The verifier computes (4) independently in both charts and checks all displayed entries. Thus the homogeneous cancellation primitive has been compared to the actual marked first-normal operator, not merely to a residue or wedge.

## 3. Exact filtered comparison, including failed endpoint gluing

Assign weighted diagonal degrees n:8, T:4, A0 and H0:4, Kdiv:0, H1:0. The actual full Serre lift changes V0 by sigma r_i with deg r_i=8. The regular Koszul commutator preimage of this change has connection weight eight, as proved in CONIC-SCALAR-LIFT-CORRECTION-HAS-A-REGULAR-COMMUTATOR-PREIMAGE.md.

For completeness the exact finite conic transport with a q-dependent symbol is as follows. Let S=I-s Nhat, s=rho_C/z, Nhat^2=0, and let Ehat=qR+O(q^2). Put C0=H0 Ds+Lambda0 s. The normal coefficient transforms by

    K^S=K+B1(C0,n)+C0 T+(H1 Ds+lambda1 s)n
                    +sR+s^2 Rn.                         (5)

This is the coefficient of the exact finite identity

    Ahat^S=Ahat+(Hhat Ds+Lambdahat s)Nhat
                       +sEhat+s^2Ehat Nhat.

The H1 Ds term is required for the actual symbol (2). All terms in (5) are retained. Their minimum respective weights are eight, eight, eight, eight, sixteen. The failed first error is NOT assumed zero; its leading weight is eight. Consequently none of these actual conic terms changes K_0.

Any extra regular first-normal frame change I+qB has minimum weighted degree of B equal to -2: its entries have nonnegative positive degree, and the lower endomorphism entry has weight shift -2. It changes K through [B,A0]-H0 DB and determinant scalar transport, all of weight at least two. Its change of T is [B,n], of weight at least six, so its change to the first error starts at weight ten. Higher cone stabilizers have still larger degree.

For the actual endpoint, the transition difference from the midpoint is q eta with leading eta of weighted degree zero. The nilpotent lift is NOT globally compatible: its first-normal mismatch has leading [eta,n], of weight eight. Applying the degree-four leading operator to this mismatch gives first-error weight twelve, while the corresponding operator transition also changes K only at weight four. Thus the failure of Nhat to glue is kept but cannot feed the weight-eight first error or K_0. This argument does not replace failed gluing by a nonexistent global Nhat.

The leading first-error identity is the fixed actual midpoint identity with its scalar/gamma conventions. Once the complete actual G(4) lift and that identity are held fixed, the above bounds show that all actual corrections leave its weight-eight part unchanged. At weight zero a correcting connection is unique: the centralizer of a regular-pair nilpotent consists of ell n, and a weight-zero such term would require ell of positive degree -8, impossible for a regular coefficient. Together with the complete affine chart calculation, this proves that (4) is the actual lowest coefficient in these markings.

The word 'actual' here does not mean that all higher K coefficients have been computed. It is the equality of the lowest associated-graded coefficient under the fixed actual source and normal-line conventions.

## 4. Explicit retained next-error summand

The leading normal nilpotent coefficient in the regular x frame is obtained by the complete harmonic transport

    Tx=P T P^-1+B1(P,n)P^-1+B1(Pn,P^-1),
    nx=P n P^-1.

The verifier checks every entry of Tx is polynomial. In particular Tx12=-tau2(f,f)/40. Since Kx12=0, (1) simplifies to the EXACT quartic

    C_K=-Kx21 Tx12+B1(Kx21,f^2)
       =Kx21 tau2(f,f)/40+tau2(Kx21,f^2)/70.          (6)

All data in (6) are explicitly displayed above, so this is a complete polynomial specification, not an unevaluated choice of K. The verifier also expands the full polynomial and checks its equality. It is

    C_K=-lambda k z P/(210A^3c),

where

    P=92A^4X^4cz^2+30A^4X^3Y
      +426A^3BX^4c^3z^7-870A^3BX^3Yc^2z^5
      -745A^3BX^2Y^2cz^3-10A^3BXY^3z
      -528A^2B^2X^4c^5z^12+216A^2B^2X^3Yc^4z^10
      +933A^2B^2X^2Y^2c^3z^8+1280A^2B^2XY^3c^2z^6
      -237A^2B^2Y^4cz^4+480AB^3X^2Y^2c^5z^13
      -1272AB^3XY^3c^4z^11+149AB^3Y^4c^3z^9
      +48B^4Y^4c^5z^14.

This is a nonzero universal polynomial. In degree four the ideal (f^2,g_x^2), generated in degrees six and ten, has no relations. Thus this isolated term is also nonzero in the LOCAL canonical square quotient. That does not imply that the sum of all next-error terms or any global obstruction is nonzero.

The fixed gamma q-symbol produces additional second-order terms elsewhere in the full formula. They are NOT included in (1) and may not be dropped from an eventual next-division calculation. Likewise unknown higher nilpotent and scalar-line coefficients remain separate.

## 5. An exact ambiguity cancellation for the higher conic term

For the actual conic scalar lift r of degree eight, regular Koszul lifts r=fp+gq differ by (p,q)->(p,q)+ell(g,-f), with ell of positive degree zero. Their commutator corrections differ by -2ell n.

For any such base scalar ell, the retained old-connection term obeys

    ([ell n,T]+B1(ell n,n)-B1(n,ell n))_11
           =-ell(f^2 T21+g^2 T12).                   (7)

The B1 commutator is zero because ell has no positive-variable derivative. Hence this particular ambiguity vanishes modulo (f^2,g^2), not merely in degree four. This makes the higher conic scalar-lift contribution choice-independent in that local quotient. It does NOT show that arbitrary higher stabilizers or unknown normal data cancel.

## Reproduction and physical equation

Run python verify_actual_lowest_normal_connection_term.py. It uses the full actual midpoint source, the already checked homogeneous cancellation identity, both marked regular charts, the complete harmonic transport (4), the leading nilpotent transport, the explicit polynomial (6), and the ambiguity identity (7). All parameters remain unassigned. No frozen source is modified.

For q0=nu q, the actual coefficient K_0 and T are divided by nu and B1 by nu, so (1) is divided by nu^2. The fixed nonzero nu is not assigned a numerical value. The usual determinant/normal-line derivative terms must also be retained in a varying equation frame.

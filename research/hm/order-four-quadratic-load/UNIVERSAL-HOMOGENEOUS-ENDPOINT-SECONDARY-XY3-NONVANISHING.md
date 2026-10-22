# The homogeneous secondary endpoint is nonzero for h=XY^3

## Result and scope

For the uniform abstract C5 input `a=z^2`, `h=XY^3`, the full homogeneous secondary construction gives

    [gamma_4] = (3k/(Bc)) [Y/z]
       in H1(Wprime O_L(-3)).                              (1)

The scalar is nonzero because `k,B,c` are nonzero. Its displayed value belongs to the fixed eigenline, apolar, Serre, and normal-class frames below; it is not asserted to be an invariant numerical normalization. This computation keeps the trace correction `q(K_i)=T_4(n_i)` and every source/target coefficient factor. It does not infer a nonzero composite from nonzero legs.

All `A,B,c,lambda,k,X,Y` remain formal and unassigned. The eigenline notation is uniform over the entire stabilizer orbit, not a selected actual source or a selected actual point. This is a universal polynomial calculation, not an actual-instance matrix/rank test or scan. Promotion through the independently checked actual fixed-operator comparison is a separate step. No fourth Bockstein value is claimed.

## 1. Common normal input and the changed operator

Use exactly the divisor pair, regular quintic frames, apolar normal cocycle `eta_8`, and compatible trace scalar splitting `n_y^x-n_x=q(eta_8)` in UNIVERSAL-HOMOGENEOUS-ENDPOINT-SECONDARY-SQUARE-CANCELLATION.md, Section 1. They are independent of h. In particular the whole lower entry of `eta_8` and both degree-eight scalar lifts `n_i` are retained. The normal cocycle has Euler diagonal coefficient four; changing its normalization rescales every step together.

The changed source relation is

    h f_z = m_h f + n_h g,

    n_h = A(AX^2cz^2+AXY+BXYc^2z^5+3BY^2cz^3)/(B lambda),
    m_h = XY^2(AX+5BYcz^3)/(2Bc z^4).

The scalar and symbol are

    u = -2kA X^3Y z^2/B - 3kY^4z/c - 3kA X^2Y^2/(Bc),
    H = kz^2XY^3,
    D = 2z^2 partial_z+z(X partial_X+Y partial_Y),
    rho = 4z,           Lambda = H rho-u.

Keep the volume-compatible opposite coordinate `w=-1/z`. There

    H_y = kXY^3,       D_y = 2 partial_w,       u_y=z^(-2)u.

In the regular x quintic frame construct the trace-free cone connection by the same exact formulas

    c_A = -2kz^4 n_h,
    m_A = (H Df+c_A g_x)/f,
    b_A = Lambda/2-m_A,
    d_A = ((Lambda-m_A)g_x-H Dg_x)/f.

Its matrix `Aconn=[[b_A,c_A],[d_A,-b_A]]` is polynomial in the regular chart. The verifier checks both the source relation and the full equation

    H Dn+[Aconn,n]=Lambda n,
    n=[[fg_x,-f^2],[g_x^2,-fg_x]].

Consequently the precise secondary diagram uses

    L_4(E)=H DE+[Aconn,E]+H rho E,
    T_4(s)=H Ds+u s,
    q L_4=T_4 q.

The physical normal-equation term and the scalar u are both included. These are the operator data supplied for independent actual comparison, not a claim that arbitrary regular cone operators have the same fixed-probe normalization.

## 2. The trace corrections are explicitly regular

For each regular pair `(f_i,g_i)` put `F_i=T_4(n_i)`. Use the exact two-remainder construction from the preceding square note, Section 3:

    j_i g_i = 1 mod f_i,
    C_i = rem(F_i j_i^2,f_i),
    G_i = (F_i-g_i^2 C_i)/f_i,
    B_i = rem(G_i j_i/2,f_i),
    D_i = (2g_i B_i-G_i)/f_i.

Polynomial remainders are taken in X with Y and every source parameter still formal. They give a rational lift of the full scalar `F_i`, not just its residue in a square quotient. For the present input the required pole-removing tangent corrections are

    v_x=5kY/(Bc z),       v_y=0.

Thus the regular lifts are

    K_i=[[B_i+f_i v_i,C_i],
         [D_i+2g_i v_i,-B_i-f_i v_i]],

with the EXACT identities `q(K_i)=T_4(n_i)`. All three entries of `K_x` are polynomials in `(z,X,Y)`, and all entries of `K_y` are polynomials in `(w,X,Y)`. In particular the nonzero x tangent addition is not silently removed from the secondary difference.

Transport `K_y` to the x coefficient frame by replacing `w=-1/z`, multiplying its upper and lower entries by `z^8,z^(-8)`, respectively, and then conjugating by `P(p_x-p_y^x)`. This retains both the physical coefficient lines `O(8),O(-8),O(0)` and the actual regular quintic transition. Denote the result by `K_y^x`.

The checked matrix identity is

    L_4(eta_8)-K_y^x+K_x = [[f gamma,0],[2g_x gamma,-f gamma]]
                         = tau(0,gamma).                (2)

Both the upper entry and the scalar trace vanish identically before passage to cohomology.

## 3. Complete cocycle, regular coboundary, and nonzero dual residue

The entire linear binary form in (2) is

    gamma = 4kA^2 X/(B^3c^4z^9)
            +6kA X/(B^2c^2z^4) +10kA Y/(B^2c^3z^6)
            +3kY/(Bc z)
            +2kXz/B -2kc^2Xz^6/A
            +7kcYz^4/A -2kBc^3Yz^9/A^2.

To exhibit the quotient exactly, define regular coefficient functions

    gamma_x = -2kXz/B +2kc^2Xz^6/A
              -7kcYz^4/A +2kBc^3Yz^9/A^2,

    gamma_y = 4kA^2Xw^6/(B^3c^4)
              -6kAXw/(B^2c^2) -10kAYw^3/(B^2c^3).

Then

    gamma = 3kY/(Bc z) + z^(-3)gamma_y(-1/z)-gamma_x.     (3)

The coefficient factor `z^(-3)` is that of `Wprime O_L(-3)`, not that of either matrix entry. Equation (3) proves (1). There is no `z^(-2)` term.

For a direct nonzero certificate, take the global dual section `Y* tensor 1` of `Wprime* O_L(1)`, with `Y*(Y)=1` and `Y*(X)=0`. The residue pairing is

    Res_z=0 Y*(gamma) dz = 3k/(Bc) != 0.                (4)

This is a global dual-section test of the already trace-corrected tangent cocycle. It is not a local arbitrary functional applied to `L_4(eta_8)` with `K_i` dropped. The other negative Laurent terms in (3) pair to zero as the displayed regular coboundary.

## 4. Exact comparison boundary and verification

ACTUAL-ENDPOINT-QUOTIENT-IS-LOWEST-VERTEX-COHOMOLOGY.md identifies the actual endpoint quotient with `H1(Wprime O(-3))` and specifies the actual lowest-operator comparison. The present artifact computes the whole homogeneous secondary operation required there. Its source cocycle is the nonzero leading normal class reconstructed in verify_lowest_normal_class_apolar_reconstruction.py. A nonzero actual normalization of that class rescales (1) and (4) by the same nonzero constant.

As with the square calculation, the physical normal equation is `q0=nu q` in fixed positive Gram coordinates. Its constant nonzero factor must be transported with the normal-class normalization; no choice of its numerical value is made. Its common rescaling cannot turn (4) into zero.

The vanishing for `h=X^4` alone did not determine this second value. The present `h=XY^3` computation is independent and yields the different nonzero endpoint above. Identifying the two input lines with particular global quadratic channels, and comparing their actual endpoint operator, belongs to the companion geometric argument. Neither this universal identity nor its nonzero endpoint is by itself a fourth Bockstein evaluation.

Run `python verify_homogeneous_endpoint_secondary_xy3_nonvanishing.py`. It checks the source relation, polynomial regularity of the cone connection and both trace lifts, exact cone preservation and the trace/operator diagram, all target-line and triangular-frame factors, (2), the regular splitting (3), and the residue (4). No existing frozen artifact is modified.

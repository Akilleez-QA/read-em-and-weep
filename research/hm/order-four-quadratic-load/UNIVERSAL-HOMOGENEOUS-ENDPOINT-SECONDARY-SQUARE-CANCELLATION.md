# The homogeneous secondary endpoint vanishes for the square K-input

## Result and exact scope

For the uniform abstract C5 input `a=z^2`, `h=X^4`, the FULL homogeneous secondary operation

    tau(gamma_4) = L_4(eta_8) - delta(K_i),
    q(K_i) = T_4(n_i),

is zero in `H1(Wprime O_L(-3))`. This includes the degree-twelve trace-lift correction `K_i`. It is not the uncorrected application of `L_4` to the normal cocycle.

The proof below constructs regular `K_i` by exact polynomial remainders, computes the entire resulting tangent cocycle, and exhibits its regular zero-cochain. The coefficients `A,B,c,lambda,k` and both binary variables remain unassigned. The chosen eigenline notation is uniform over the whole stabilizer orbit, not a selected actual HM point or coefficient instance. There are no source-instance matrices, rank evaluations, scans, or local-model replacements.

This is the homogeneous computation needed by ACTUAL-ENDPOINT-QUOTIENT-IS-LOWEST-VERTEX-COHOMOLOGY.md. Promotion to the fixed actual normal variation requires that note's actual filtered-operator comparison. No fourth Bockstein value is inferred here.

## 1. The source and the leading normal cocycle

Use the divisor quintic and its actual regular targets from UNIVERSAL-DIVISOR-QUINTIC-TWO-CHART-SHADOW-CANCELLATION.md:

    f = A X^2Y + BzY^3 + Acz^2X^3 - Bcz^3XY^2,
    g = -lambda(BXY^4/z^3 + AX^3Y^2/z^4)/(2Ac),

    p_x = lambda XY/(2Ac z^4) - lambda X^2/(2A z^2)
          + lambda B Y^2/(A^2z),
    p_y^x = -lambda Y^2/(2Ac^2z^6) - lambda X^2/(Bc^2z^7).

Here `p_y^x` is the opposite regularizer transported to the x coefficient frame. Write `g_x=g+p_x f` and `P(p)=[[1,0],[p,1]]`. The opposite coordinate is the volume-compatible `w=-1/z`; its regular pair is

    f_y = z^(-3) f,
    g_y = z^5 g + p_y f_y,
    p_y = -lambda Y^2/(2Ac^2w^2) + lambda X^2/(Bc^2w).

Substitution `z=-1/w` in these formulas is understood. In particular `p_y^x=z^(-8)p_y`.

For completeness, the exact apolar reconstruction in verify_lowest_normal_class_apolar_reconstruction.py is the following. Put `d=Bc^2/A` and

    R_i = (1-2dz^5, z+dz^6/2, z^2, z^4),
    e_i = (3/(5z)-1/(5dz^6), 6/(5dz^7)+2/(5z^2), z^(-3), z^(-5)),

    r_0 = -lambda(-Ac z^2 X^2 + AXY + 2Bc z^3Y^2)/(A^2c z^4),
    r_1 = lambda(2Ac z^2 X^2 - 2AXY + Bc z^3Y^2)/(2A^2c z^3),
    r_2 = -lambda XY/(Ac z^2),
    r_3 = 0.

The `e_i` are exactly residue-dual to the `R_i`. Thus in the divisor frame

    eta_8 = [[d_eta,0],[r_eta,-d_eta]],
    d_eta = sum R_i e_i = 4/z + 1/(dz^6) - dz^4,
    r_eta = sum r_i e_i.

In the regular x frame the lower entry is `r_eta+2p_x d_eta`. This is the full leading normal cocycle, not just its Euler diagonal. Its scalar trace is

    q(eta_8) = 2fg d_eta - f^2 r_eta.

Let `n_x,n_y^x` be its exact regular scalar splitting, with

    n_y^x-n_x = q(eta_8),

`n_x` regular in z and `z^4 n_y^x` regular in w. The cited reconstruction verifier displays both polynomials and checks this identity. Their degree-eight coefficient line is `O_L(-4)`. They are retained throughout the computation below.

The normalization above has Euler diagonal coefficient four. Rescaling the actual normal generator rescales `eta_8,n_i,K_i,gamma_4` together, and cannot change the zero conclusion.

## 2. The full homogeneous operators and trace diagram

Set

    D = 2z^2 partial_z + z(X partial_X + Y partial_Y),
    H = kz^2X^4,       rho = 4z,
    u = 4kB XY^3z^2/(Ac) + 4kX^3Yz/c,
    Lambda = H rho-u,

    n_h = [X^2(-4Az+Bc^2z^6)+2Bc XYz^4-3BY^2z^2]/lambda.

These are the source relation and scalar-inverse data for this input; in particular the coefficient-line correction in `u` is not omitted. In the regular x frame define

    c_A = -2kz^4 n_h,
    m_A = (H Df+c_A g_x)/f,
    b_A = Lambda/2-m_A,
    d_A = ((Lambda-m_A)g_x-H Dg_x)/f,
    Aconn = [[b_A,c_A],[d_A,-b_A]].

With `n=[[fg_x,-f^2],[g_x^2,-fg_x]]`, the exact polynomial identity is

    H Dn + [Aconn,n] = Lambda n.

Consequently the two operators used here are

    L_4(E) = H DE + [Aconn,E] + H rho E,
    T_4(s) = H Ds + u s,

and satisfy `q L_4=T_4 q` exactly. The term `H rho E` is essential: the scalar quotient operator is `H D+u`, not `H D-Lambda`.

In the w chart `D=2 partial_w`, `H=kX^4`, and `u_y=z^(-2)u`. Thus if `F_x=T_4(n_x)` and `F_y=T_4(n_y)` in their respective charts, then

    F_y = z^2 T_4(n_y^x).

The factor `z^2` is the degree-twelve, physical-twist-four coefficient line `O_L(-2)`. The verifier checks this transported equality before constructing either endpoint class.

## 3. Explicit regular trace lifts, including their tangent corrections

Here is a finite exact construction of `K_i`; it avoids a coefficient matrix or rank test. For either regular pair `(f_i,g_i)` and scalar `F_i`, take an inverse `j_i` of `g_i` modulo `f_i` in the polynomial ring in X over the field of the other UNASSIGNED symbols. Define

    C_i = rem(F_i j_i^2, f_i),
    G_i = (F_i-g_i^2 C_i)/f_i,
    B_i = rem(G_i j_i/2, f_i),
    D_i = (2g_i B_i-G_i)/f_i.

These are homogeneous in `(X,Y)` of degrees `2,4,6`, respectively. Direct substitution gives

    2f_i g_i B_i + g_i^2 C_i - f_i^2 D_i = F_i.

Thus `[[B_i,C_i],[D_i,-B_i]]` is a rational trace lift. Its only base poles are removed by the following EXACT tangent additions:

    v_x = 4kY/(Ac^2z^2),
    v_y = -4kY/(Ac^2w),

    K_i = [[B_i+f_i v_i, C_i],
           [D_i+2g_i v_i, -B_i-f_i v_i]].

All entries of `K_x` are polynomials in `(z,X,Y)`, and all entries of `K_y` are polynomials in `(w,X,Y)`, with coefficients in the field of the five formal source parameters. Both trace identities `q(K_i)=F_i` are checked before taking a quotient. The tangent additions have zero trace against n; they are not discarded merely because they are tangent.

The full y-to-x transport is also retained. First replace w by `-1/z`, and multiply the upper entry by `z^8` and the lower entry by `z^(-8)`, leaving the diagonal unchanged. These are the coefficient lines `O(8),O(-8),O(0)` of `B_(2;12)`. Then conjugate by `P(p_x-p_y^x)`. Call the resulting matrix `K_y^x`. The actual secondary difference in the regular x frame is

    L_4(eta_8) - K_y^x + K_x.

Both its upper entry and its trace vanish exactly. Its diagonal is `f gamma`, and its lower entry is `2g_x gamma`. Hence it is `tau(0,gamma)`, with no omitted trace-lift term.

## 4. The entire tangent cocycle is a regular coboundary

The resulting linear binary form is

    gamma = 16kA Y/(B^2c^6z^12) - 16kA X/(B^2c^5z^10)
            +36kY/(Bc^4z^7) - 36kX/(Bc^3z^5)
            +2kX/(Ac) + 2kBc Xz^5/A^2
            -6kB Yz^3/A^2 - 2kB^2c^3 Xz^10/A^3.

In particular it has neither of the two surviving Laurent exponents `-1,-2` for `O_L(-3)`. More strongly, define the regular zero-cochain

    gamma_x = -2kX/(Ac) - 2kBc Xz^5/A^2
              +6kB Yz^3/A^2 + 2kB^2c^3 Xz^10/A^3,

    gamma_y = -16kA Yw^9/(B^2c^6) + 16kA Xw^7/(B^2c^5)
              +36kYw^4/(Bc^4) - 36kXw^2/(Bc^3).

Then the exact coefficient-frame identity is

    gamma = z^(-3) gamma_y(-1/z) - gamma_x.

This proves the stated vanishing in `H1(Wprime O_L(-3))`, before choosing a C5 test character. The parameter lambda cancels from this final cocycle, but it was retained in both source and trace-lift computations.

## 5. Comparison boundary and reproduction

ACTUAL-ENDPOINT-QUOTIENT-IS-LOWEST-VERTEX-COHOMOLOGY.md identifies the actual endpoint quotient with this lowest coefficient and specifies the needed actual operator comparison. The present calculation supplies its entire homogeneous secondary operation, including the required `K_i`. It does not replace that comparison with a dimension count, and it does not identify the full restriction to U with the lowest quotient.

Physical equation normalization is harmless for this zero identity but must not be silently reassigned: in fixed positive Gram coordinates `q0=nu q` with the actual constant `nu != 0`. Changing the normal generator by the resulting common factor rescales the source cocycle, its scalar splitting, its trace lifts, and its zero-cochain together.

Run `python verify_homogeneous_endpoint_secondary_square_cancellation.py`. It imports the exact apolar reconstruction, keeps all symbols unassigned, constructs and checks both regular trace lifts, verifies the operator/trace diagram and all target-frame factors, and verifies the displayed regular coboundary. Previously frozen artifacts are unchanged.

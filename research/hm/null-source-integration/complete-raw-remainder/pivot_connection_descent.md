# Pivot connections resolve the auxiliary-frame descent defect

## Result

The frame defect of the local connection rewrite has an explicit regular correction on the actual source cover. Each carrier's nonvanishing pivot section of N-squared defines a flat connection on N over that carrier. These vertex connections need not agree on different carriers. They suffice to replace the local scalar representative by a global, tensorial scalar cochain t-prime and to replace the local edge correction by a global regular edge cochain H:

    t'_r = s_raw,r + delta_S h_r,
    h_r,i = (1/4) contraction_r((gamma_i-a_i) wedge tau_i),
    H = B_p(h_q) + B_q(h_p),
    R(t') = R_raw + delta_S H.                              (1)

Here a_i is the pivot connection defined below. Formula (1) is a genuinely source-specific correction; it is not the choice t-prime = s_raw obtained by undoing the original rewrite. It resolves the auxiliary-frame anomaly. It does not prove that the resulting global obstruction is zero.

An entirely tensorial four-block formula for t-prime is given in (18). The original q-gerbe correction is retained. The projection correction from the preceding note is unchanged by this shift. All statements are algebraic differential identities; no physical source matrix, coefficient, jet, or overlap is evaluated.

## 1. Inputs and two different Cech directions

The source inputs are the [original first-order construction, sections 1, 2 and 4](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-residual-attribution/first-order-source.md), the [physical-frame theorem, sections 1, 2 and 4](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-geometric-dependencies/frames-and-poles.md), and [BI, equations (1), (2), (7) and (8)](https://github.com/Akilleez-QA/read-em-and-weep/blob/e93cf712f9da4926a8450cc870ed45a7bfc379ab/research/codex-swarm/source-boundary-analysis/PROOF.md). We use the complete-remainder reduction [published at 9f3c123](https://github.com/Akilleez-QA/read-em-and-weep/commit/9f3c1232806277ddf79785025fb56cf0fd4f796c) and the determinant/frame identities [published at 5afa438](https://github.com/Akilleez-QA/read-em-and-weep/commit/5afa4389419d9187104612b07e39558e9c4a7b92).

Write delta_S for the actual source-cover differential and delta_A for an auxiliary cover used to express all line-connection coefficients in one common frame. For row-End cochains delta_S includes the actual row transport. The rank-two transition frames are held fixed during an auxiliary line-frame comparison. A change of those rank-two frames additionally requires the usual conjugation and derivative transport.

For p=(a,b), q=(c,d), with four distinct coordinate indices, BI supplies

    B_ab(f)_ij = [(V_b f_i+V_b f_j)L_a,ij
                  -(V_a f_i+V_a f_j)L_b,ij]/2,
    E_ab(delta_S f) = delta_S B_ab(f).                       (2)

The V's are the physical derivations. Every displayed edge formula is used first on the fixed increasing source edges and then with the accepted alternating extension.

Use the four block signs sigma=(-,+,-,+), ranks n=(5,15,10,2), and line weights k=(-1,1,3,5). In a common line frame alpha,

    Omega_i^(r),alpha = B_i^(r) + k_r gamma_i^alpha I,
    tau_i = sum_r sigma_r k_r tr(B_i^(r)),
    gamma_j^alpha-gamma_i^alpha = -q_ij/2.                   (3)

The B_i are differences of connections; tau_i is tensorial and does not change with the auxiliary frame. The preceding local rewrite gives

    s_raw,r = t_r^alpha-delta_S f_r^alpha,
    f_r,i^alpha = (1/4) contraction_r(gamma_i^alpha wedge tau_i),
    K^alpha = B_p(f_q^alpha)+B_q(f_p^alpha).                  (4)

No block has been discarded in (3) or (4).

## 2. The frame defect and its actual source differential

Fix the sign convention by writing e_beta=e_alpha t_alpha,beta for the line frame. Then

    rho_alpha,beta = dlog(t_alpha,beta),
    gamma_i^beta = gamma_i^alpha+rho_alpha,beta,
    Delta f_r,i = (1/4) contraction_r(rho wedge tau_i),
    A_alpha,beta = K^beta-K^alpha
                = B_p(Delta f_q)+B_q(Delta f_p).             (5)

Thus delta_A A=0. This is an auxiliary Cech statement, not the assertion delta_S A=0.

For the actual separated physical line-frame changes, V_a rho_c=0 when a and c are distinct. Put

    P_i;ac = V_a V_c log(v_pivot(i)),  a != c.

The determinant reduction, with its accepted homogeneous regularity and complete-cover premises, gives V_a tau_i,c=-4 P_i;ac. Consequently

    B_ab(Delta f_cd)_ij
      = -rho_c/2 [(P_i;bd+P_j;bd)L_a-(P_i;ad+P_j;ad)L_b]
        +rho_d/2 [(P_i;bc+P_j;bc)L_a-(P_i;ac+P_j;ac)L_b].    (6)

Add the same expression with (a,b) and (c,d) exchanged to obtain A. For an arbitrary, nonseparated auxiliary frame change, retain also

    V_a Delta f_cd,i
       = [(V_a rho_c)tau_i,d-(V_a rho_d)tau_i,c]/4
         -rho_c P_i;ad+rho_d P_i;ac.                         (7)

The construction in sections 4-6 works in this general case too; separation is used only for the shorter expression (6).

There is also an explicit source differential of (6), rather than an assumed vanishing. For any scalar vertex cochain z, set

    M_r(z)_ij = (z_i+z_j)L_r,ij,
    Z_r(z)_ijk = (delta_S z)_ij U_r,ijk
                 -(delta_S z)_jk L_r,ij.

The current identity L_r,ik=L_r,ij+U_r,ijk gives

    delta_S M_r(z) = Z_r(z).                                (8)

In this notation (6) is

    -rho_c/2 [M_a(P_bd)-M_b(P_ad)]
    +rho_d/2 [M_a(P_bc)-M_b(P_ac)].

Its source differential is exactly the same expression with each M replaced by Z, plus the exchanged-pair expression. Here rho is common to the source vertices on the auxiliary patch, so delta_S rho=0. This exhibits the remaining endpoint Hessian differences and the transported currents explicitly. They need not vanish.

The original cocycle q is distinct from rho. On a finite one-factor comparison, after retaining the physical y factor,

    dlog(y/x)/dx = 1/(2x) + 1/[x(x^2-1)].

Equivalently, the refined line-frame change equals the old half-N-squared frame change plus the change between the prescribed old connection coefficients. In a common auxiliary frame the already transported coefficients instead obey (3). Mixing these two comparisons would replace rho by q/2 incorrectly.

## 3. Exact total descent before the correction

Keep the second-jet term Omega unless actual source symmetry has been established. Define

    N^alpha = Omega+Q2+Q4+E_p(t_q^alpha)+E_q(t_p^alpha)
            = R_raw+delta_S K^alpha.                        (9)

On the double cover use total differential

    D_tot = delta_A + (-1)^(auxiliary degree) delta_S.

The pair (N,A), of respective bidegrees (0,2) and (1,1), is a total degree-two cocycle:

    delta_S N = 0,
    delta_A N = delta_S A,
    delta_A A = 0.                                          (10)

It differs from (R_raw,0) by D_tot K. The first equation uses the admitted closedness of the complete raw source; the other two follow directly from (5) and (9). In particular A alone is not generally source-closed.

A total primitive would consist of P of bidegree (0,1) and Q_desc of bidegree (1,0), satisfying

    delta_S P = N,
    delta_A P-delta_S Q_desc = A,
    delta_A Q_desc = 0.                                    (11)

The stricter equation P^beta-P^alpha=A is merely the Q_desc=0 special case. Local flatness does not by itself supply any of these primitive equations.

The cocycle rho represents the line bundle's Atiyah class with the convention fixed in (5). Before a chain-compatible construction, the contraction in (6) is not a defined total cup-product obstruction class. Nonvanishing of the line bundle's first Chern class would not imply that the contracted A or the complete obstruction is nonzero. In fact the source-specific construction below explicitly makes A auxiliary-exact with source-edge coefficients.

## 4. The actual pivot section supplies regular vertex connections

On a primary carrier h_j=v_j(v_j^4-product_(k!=j) v_k) is nonzero, hence its pivot v_j is nonzero. On the auxiliary carrier v0 v1 v3 v4 is nonzero, and the source's chosen pivot is among these permitted nonzero coordinates. Thus each source vertex carries a specified nowhere-zero section of N-squared.

In its prescribed physical frame the coefficient of this section is

    w_i = v_pivot(i)/nu_i^2.

It is a regular unit on that carrier/legal open. The homogeneous source and physical-frame premises ensure this at infinity too: v_local=tau_chart v_affine and nu_B^2=tau_chart nu_A^2, so w is unchanged by that coordinate presentation. Define the connection on N whose induced connection makes this N-squared section parallel:

    a_i = -(1/2)dlog(w_i)
        = dlog(nu_i)-(1/2)dlog(v_pivot(i)).                  (12)

This definition uses only a logarithmic derivative of a regular unit and division by 2. It neither takes a square root nor chooses a logarithm branch. It is regular and flat on its own source vertex. No single global connection on N is claimed.

For clarity about signs, if lambda_i^alpha=dlog(w_i^alpha) denotes the coefficient logarithmic derivative in the auxiliary frame, then

    w_i^beta=t_alpha,beta^(-2)w_i^alpha,
    lambda_i^beta=lambda_i^alpha-2rho_alpha,beta,
    a_i^beta=a_i^alpha+rho_alpha,beta.                       (13)

Thus lambda_i+2gamma_i is intrinsic, not lambda_i-2gamma_i. Do not confuse this actual section coefficient with a fixed homogeneous reference expression for v_pivot.

The following are therefore intrinsic regular forms on their respective source vertices and edges:

    d_i = gamma_i^alpha-a_i^alpha,
    eta_ij = -2(a_j^alpha-a_i^alpha)
           = dlog(w_j^alpha/w_i^alpha)
           = q_ij+2(delta_S d)_ij.                          (14)

The symbol d_i denotes a one-form difference, not the exterior derivative. In a common line frame eta is the logarithmic derivative of the pivot-section ratio. Unlike q, it generally depends on all four coordinates.

## 5. An explicit correction removes the frame anomaly

Define the local scalar vertex cochains and local edge cochain

    g_r,i^alpha = (1/4) contraction_r(a_i^alpha wedge tau_i),
    C^alpha = B_p(g_q^alpha)+B_q(g_p^alpha).

Equations (5) and (13) give, without any separated-derivative assumption,

    Delta g_r = Delta f_r,
    delta_A C = A.                                        (15)

Consequently

    h_r = f_r^alpha-g_r^alpha
        = (1/4) contraction_r(d_i wedge tau_i),
    H = K^alpha-C^alpha = B_p(h_q)+B_q(h_p),
    t'_r = t_r^alpha-delta_S g_r^alpha
         = s_raw,r+delta_S h_r                             (16)

are regular tensorial cochains on the source cover, independent of alpha. The local family C removes the auxiliary anomaly; H is the resulting global regular source-edge comparison. This uses explicit source-vertex pivot connections, rather than an assumed global connection or the substitution g=f.

For a useful check confined to the source's prescribed physical vertex frames, the determinant identity gives

    tau_i = 8 a_i+30 gamma_i,
    h_r,i = (19/2) contraction_r(gamma_i wedge a_i).         (17)

Indeed (gamma-a) wedge (8a+30gamma)=38 gamma wedge a. The first equality in (17) must not be transported as an arbitrary common-frame coefficient identity: the extreme split bases change under an arbitrary auxiliary frame change. The globally valid definition is (16). The correction may vanish in particular prescribed mask-zero frames; that does not identify t-prime with s_raw as a cochain on the complete source cover.

## 6. Entirely tensorial formula, all four blocks retained

Set Btilde_i^(r)=B_i^(r)+k_r d_i I. These are the differences between the actual split connections and the pivot line connections, hence tensorial. Their weighted trace is tau_i-30d_i because sum sigma_r n_r k_r^2=-30. Direct expansion of (16) gives

    t'_cd,ij = (1/4) contraction_cd [
          sum_r sigma_r tr(Btilde_i^(r) wedge Btilde_j^(r))
          +(eta_ij/2) wedge(tau_i+tau_j)
          +30 d_i wedge d_j]
          -15 q_c,ij q_d,ij/8.                             (18)

One way to check every sign is to put W_ij=sum sigma tr(B_i wedge B_j). Then

    Wtilde_ij = W_ij-d_j wedge tau_i+d_i wedge tau_j
                       -30d_i wedge d_j.

Adding delta_S(d wedge tau) to W+(q/2) wedge(tau_i+tau_j), and using eta/2=q/2+delta_S d, gives precisely the bracket in (18).

The original edge gerbe term has not changed. Its complementary physical derivatives are still zero by the actual single-coordinate dependence of q_c and q_d. No such rule applies to eta: the terms V_a eta_c, V_a d_i,c, and derivatives of the shifted blocks must be retained when applying E to (18). This rewrite removes a descent anomaly, not necessarily symbolic cost.

It also preserves the exact first-order scalar equation:

    delta_S t'_r = delta_S s_raw,r = F_r,
    R(t') = Omega+Q2+Q4+E_p(t'_q)+E_q(t'_p)
          = R_raw+delta_S H.                               (19)

Equivalently (N,A)-D_tot C=(R(t'),0). Thus the frame descent part is explicitly resolved, while the complete global cohomology class is unchanged.

## 7. The projection correction survives unchanged

Let D be the actual complex differential, h_j its contraction, I_j and P_j the inclusion and projection, and C_ij=P_i I_j. Write T_j,a=[D,B_j,a]. The preceding exact projection identity was

    P_i B_j,a I_i-C_ij(P_j B_j,a I_j)C_ji
       = P_i h_j T_j,a I_i-C_ij P_j T_j,a h_j I_i.           (20)

Each component of D raises the source line weight by 2. Hence, for the block-diagonal weight operator k,

    [D,k]=-2D,
    [D,Btilde_j,a]=T_j,a-2d_j,a D.

Replacing B by Btilde in (20) leaves the right-hand side exactly unchanged: the added first term contains D I_i=0 and the added second term contains P_j D=0. Therefore the pivot normalization does not make the individual connection coefficients into chain maps and does not permit replacing the full four-block expression in (18) by its cohomology block alone.

## 8. The remaining global obligation and domain limit

The unresolved identity is now a global, regular source-cover boundary problem with no auxiliary-frame compatibility defect:

    Omega+Q2+Q4+E_p(t'_q)+E_q(t'_p) = delta_S P'.            (21)

If the actual J-transpose-S-H symmetry is later proved, remove Omega from (21), but retain all other terms. A regular total-resolution primitive would also suffice. When (21) holds, P'-H is a primitive for R_raw by (19). Conversely a primitive for R_raw yields one for R(t') by adding H. Neither direction establishes existence.

The new representative and comparison are regular on the full common cover. No claim is made that t-prime, H, or their resolution lifts satisfy the admitted 54/29 finite cutoff or any existing detector implementation's domain. Applying a finite projection to them would require new source-faithful bounds. The global identity (19) is valid without that unsupported promotion.

The precise progress is the constructive elimination (15)-(16) of the auxiliary frame defect, the all-tensorial four-block representative (18), and the unchanged projection correction (20). The complete global obstruction class has neither been evaluated nor proved to vanish.

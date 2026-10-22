# The actual cone diagonal is the canonical residue inverse

## Result

The diagonal entry of the corrected cone operator is determined by the actual quartic quotient and its canonical inverse. It is not an independent unknown scalar. This gives a fully normalized version of the harmonic transition cochain, while retaining the remaining global cohomology problem.

Normalize the negative vector field by D_a=a_s partial_t-a_t partial_s, and retain the fixed actual nonzero scalar k in zeta_a=k At_F(D_a). Let Q denote the actual quotient

    Q: D5 O_L -> V O_L(2),

identified by the actual socle pairing. Its induced map H0(D5 O_L(2))->H0(V O_L(4)) is an isomorphism. Define the GLOBAL scalar correction u by

    Q(u)=k a Lie_(D_a)(Qh).                         (1)

On z=t/s with normalized positive cover coordinates, write

    D_a=2a partial_z+(a_z/2)E,

where E is the positive-cover Euler field. For the tracefree cone connection A and the effective local scalar Lambda in O_ad(N)=Lambda N, the exact convention is

    Lambda=2k a a_z h-u,
    A11=Lambda/2-m,
    A12=-2k a^2 n_h,                                (2)

where H=k a h, H D_a f=m f+2k a^2 n_h g. In particular Lambda is LOCAL and includes a frame-action term. It must not be identified with the global mixed quartic u.

## 1. Derivation with fixed determinant

The rank-nine residue theorem uses the convention

    rho_(hD)=4 kappa h-tr(M),

where D=w partial_z+kappa E and hD(f,g)^T=M(f,g)^T. It proves that the image under the actual socle pairing is Lie_D(Qh). Here kappa=a_z/2. Multiplying the entire symbol and natural determinant action by k a proves (1).

For clarity, choose the corrected operator with the canonical subline action gamma=-u/2 supplied by the residue/Ext construction. Equivalently residue compatibility gives 2gamma+u in H0(I_Z(4))_+=0, so the same action is forced. Let A_full be its connection matrix on G before removing the determinant scalar, and now choose the OPERATOR-INDUCED relation matrix M=gamma I-A_full. This matrix satisfies H D(sigma)=M sigma exactly. An arbitrary relation matrix has its trace fixed only modulo(f,g), and must not be used for the following exact trace equation. The natural determinant action on det G=O(2) has local connection scalar -4 kappa H. Therefore

    tr(A_full)=-4 kappa H,
    2gamma-tr(M)=-4 kappa H.

For this induced matrix the exact scalar identity agrees with the prescribed action gamma=-u/2. Passing to the tracefree matrix adds 2 kappa H times the identity. Hence its action on sigma is (gamma+2 kappa H)sigma. Since N=sigma sigma^t J, its adjoint action on N has scalar

    Lambda=2gamma+4 kappa H=-u+2k a a_z h.

This proves (2), including its sign and factor two. Tensoring between G and F does not change the tracefree adjoint connection; the natural spinor/determinant line actions have already been included. This computation is compatible with the fixed determinant convention, not a replacement of it by zero determinant action.

The first row equation gives A12=-n and A11=Lambda/2-m. The actual upper-entry theorem gives n=2k a^2 n_h in the present Hamiltonian normalization.

## 2. A normalized formula for the pure-triangular cochain

Write tau(v,w)=v_uu w_vv-2v_uv w_uv+v_vv w_uu for the unnormalized second positive transvectant. All derivatives here are in the positive cover variables except explicitly indicated z derivatives.

On a pure g_j=g_i+p f overlap, p has positive degree2. Define the local quartic

    m_h,i=(h f_z-n_h g_i)/f.

This is the SOURCE i-frame coefficient used in A11,i. It is regular: h f_z-n_h g_i vanishes on the regular divisor f=0. The cone-chart Euler term gives

    m_i=2k a^2 m_h,i+(3/2)k a a_z h,
    D_a p=2a p_z+a_z p.

The established harmonic transition formula consequently becomes

    K11=-(k/3)a^2 tau(p,n_h),
    K21=k a^2 U + tau(p,Gamma)/30,                  (3)

where

    U=2 tau(p,m_h,i)/15-tau(p^2,n_h)/15
        -tau(p,p)n_h/3+tau(h,p_z)/15,
    Gamma=u+2k a a_z h.

The discrepancy K is in the target j-frame, but its displayed formula uses the SOURCE connection b=A11,i and hence m_h,i above. Only the trace below uses the target g_j=g_i+p f. In particular m_h,j=m_h,i-p n_h, so silently replacing m_h,i by m_h,j would omit a term. The actual square-ideal shadow is (2f g_j K11-f^2 K21)/nu in the physical equation frame q0=nu q. The later multiplication by a and the actual second-symbol quotient are unchanged.

Formula(3) follows with the degree-dependent harmonic constants retained: B(p,b)=tau(p,b)/30, B(p,c)=tau(p,c)/6, B(p^2,c)=tau(p^2,c)/30, B(p,p)=tau(p,p)/6, and B(H,Dp)=tau(H,Dp)/30. In particular the B(p,p)c term has not been omitted.

## 3. The exact remaining scalar-extension term

The natural action on the quotient coefficient Qh in O_L(2) is

    Lie_(D_a)(Qh)=2a (Qh)_z-2a_z Qh.

Thus (1) implies the local divisor identity

    Q(Gamma)=2k a^2 (Qh)_z.                         (4)

This means Gamma restricted to D is divisible by a^2. It does NOT say the ambient quartic Gamma is divisible by a^2. The derivative (Qh)_z is a local connection coefficient, not a global section with its formal twist. Its inverse under Q has formal bidegree(4,-2) and an inhomogeneous base-frame transformation; there is no asserted equivariant D5 map to H0(O_D(4,-2))=V. For local lifts ell_i of this divisor connection coefficient, the exact statement is

    Gamma-2k a^2 ell_i=f l_i,

with l_i a positive linear form carrying its actual base factor. These f-linear corrections contribute tau(p,f l_i)/30 to (3). They cannot be discarded as commutators or as global coboundaries without proof.

The first-normal cochain has therefore been reduced to its a^2-divisible part and an explicitly identified scalar-extension correction. Neither the value nor the cancellation of their global classes has been established. A nonzero upper multiplication map, or nonzero individual local residue, does not settle that question.

## Sources and verification

ACTUAL-POSITIVE-ATIYAH-MULTIPLICATION-SURJECTS-ONTO-NINE-SPACE.md Sections1-2 supplies the actual Q and rho convention, including the full determinant action. POSITIVE-SERRE-RESIDUE-AND-CANONICAL-CONE-OPERATOR-CORRECTION.md Section2 supplies the actual inverse in (1). ACTUAL-CONE-UPPER-CONNECTION-HAS-A-SQUARED-FACTOR.md supplies n_h. ACTUAL-NORMAL-OPERATOR-SQUARE-SHADOW-BY-HARMONIC-TRANSITION.md supplies the corrected actual transition comparison and its remaining scope.

The companion verifier checks the universal identity (3) using independent formal polynomial coefficients, as well as the determinant scalar and frame-weight cancellation. It does not select actual HM coefficients, construct an actual-instance matrix, or evaluate its rank.

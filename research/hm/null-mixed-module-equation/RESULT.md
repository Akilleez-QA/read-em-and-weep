# Explicit mixed module cocycle for the corrected external-product ambient

## Result

The identified external-product ambient and any representatives of the two existing pure lifts determine the mixed obstruction by the explicit formula (6) below. Every ambient mixed term is specified; no independent mixed ambient coefficient is left to choose. The remaining problem is the single linear equation

    δx = −C,    C = g_ik^−1 R_ijk.                         (1)

The formula includes the product mixed differential, overlap-composition differential, all overlap/pure-lift interactions, and the product of the two triple-unit coefficients. A pure change of frame changes C by an explicitly exhibited Čech coboundary (10). In the compact problem, the proved uniqueness of the pure lifts makes its class independent of every choice of pure representatives. This supplies a concrete, gauge-independent secondary operation, not a vanishing result.

The computation is formal algebra on unspecified transition cochains.

## 1. Inputs, conventions, and coefficient operators

Historical public context: https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6270678828. Dependencies include null-actual-pair-comparison/RESULT.md and AUDIT.md, null-corrected-pure-lift/corrected-relative-lift/RESULT.md, null-pure-lift-uniqueness/pure-lift-uniqueness/RESULT.md, null-simple-fiber-moduli/family-lift-torsor-0523/RESULT.md, null-module-boundary-audits/module-lifting/RESULT.md, null-actual-source-factorization/RESULT.md, and the pinned-source copy https://github.com/Akilleez-QA/read-em-and-weep/blob/c8aec970fd65a105f39f4e8aeb8a17f0f0053f89/research/hm/second-order-algebroid.md. The source's row convention is

    g_jk g_ij = g_ik,
    F_ij(G_jk) ⋆ G_ij = A_ijk ⋆ G_ik.

Let X=P²_z×P²_h, E=m*HM, K_z=pr_z*ω, K_h=pr_h*ω, J=K_z⊗K_h. The additive ambient is O⊕K_z⊕K_h⊕J. Bidegrees are (0,0),(1,0),(0,1),(1,1); any coefficient with either degree above one is zero. Symbols s,t are useful degree bookkeeping only: neither coefficient line is globally trivialized.

Start with product affine charts carrying the factor presentations and refine to an affine E-trivializing cover with affine intersections. Restrict the factor operators to this refinement. All coefficient identifications below are sheaf-theoretic; in line frames they include the usual transition factors.

Write

    μ_z(f,g) = (1/2)d_z f∧d_z g,
    μ_h(f,g) = (1/2)d_h f∧d_h g,
    v^z_ij(f) = (1/2)d_z f∧β^z_ij,
    v^h_ij(f) = (1/2)d_h f∧β^h_ij,
    b_ijk = −2((β^z)²)_ijk,
    c_ijk = −2((β^h)²)_ijk.

Here (β²)_ijk=−β_ij∧β_jk uses the stipulated total Čech–forms product. By contrast b_ijk c_ijk below is the coefficient-line tensor product on the SAME triple intersection, not a Čech cup product of degree-four.

Operators in the z direction extend canonically to K_h-valued arguments, and conversely, because each opposite coefficient line is pulled back from the other factor. For example, on decomposable coefficients μ_z(f,η_h)=μ_z(f,a)⊗η_h^0 if η_h=aη_h^0 and η_h^0 is a frame pulled back from h. This definition is independent of such transverse frames. Matrix arguments always mean the formal index-summed extension, preserving displayed order.

The two additional operators dictated by external product are

    w_ij = v^z_ij v^h_ij = v^h_ij v^z_ij,
    M(f_z f_h,g_z g_h) = μ_z(f_z,g_z)⊗μ_h(f_h,g_h).       (2)

Extend M bilinearly on product coordinate rings and by its differential-operator localization on refinements. In product coordinates it is the alternating z-contraction and alternating h-contraction of the two mixed derivatives, with coefficient 1/4. This definition is independent of coordinate choices; it is the tensor product of the two specified factor biderivations. The commuting statement in (2) is an identity on scalar entries and transverse coefficient lines, not an assertion that bundle transition matrices commute.

## 2. The entire ambient through mixed order

For a=f+u+v+r and a'=g+u'+v'+r', with u,u' in K_z, v,v' in K_h, r,r' in J, the mixed component of their product is

    (a⋆a')_J = f r' + r g + u v' + v u'
      + μ_z(f,v') + μ_z(v,g)
      + μ_h(f,u') + μ_h(u,g) + M(f,g).                  (3)

The pure components are f u'+u g+μ_z(f,g) and f v'+v g+μ_h(f,g). The complete overlap map is

    F_ij(a) = f
      + (u+v^z_ij(f)) + (v+v^h_ij(f))
      + (r+v^z_ij(v)+v^h_ij(u)+w_ij(f)),

and the complete triple unit is

    A_ijk = 1+b_ijk+c_ijk+b_ijk c_ijk.                  (4)

In particular, F_J is not zero in this corrected presentation. The two pure overlap maps themselves generate w.

A is central: a K_z-valued b is supported on the z factor, so μ_h(b,f)=μ_h(f,b)=0; its same-direction corrections have forbidden degree (2,0). The analogous facts hold for c. Mixed coefficients have no further corrections. Also v^h(b)=v^z(c)=0. These are factor-support facts, not a general claim about scalar coefficients in noncommutative algebras. Equations (3)–(4) are exactly the tensor product of the two genuine pair algebroids, so their algebra, overlap, and pentagon identities hold.

## 3. Pure lifts and the explicit mixed source

Choose pure module transition representatives

    G^z_ij=g_ij+u_ij,    G^h_ij=g_ij+v_ij.

Their exact pure equations are

    u_jk g_ij + g_jk u_ij − u_ik
      = b_ijk g_ik − μ_z(g_jk,g_ij) − v^z_ij(g_jk)g_ij,
    v_jk g_ij + g_jk v_ij − v_ik
      = c_ijk g_ik − μ_h(g_jk,g_ij) − v^h_ij(g_jk)g_ij.  (5)

Lift this boundary by initially taking G_ij=g_ij+u_ij+v_ij with zero mixed coefficient. Define U_jk=u_jk+v^z_ij(g_jk) and V_jk=v_jk+v^h_ij(g_jk); these auxiliary symbols depend also on ij. Direct use of (3)–(4) gives

    R_ijk = [v^z_ij(v_jk)+v^h_ij(u_jk)+w_ij(g_jk)]g_ij
      + U_jk v_ij + V_jk u_ij
      + μ_z(g_jk,v_ij) + μ_z(V_jk,g_ij)
      + μ_h(g_jk,u_ij) + μ_h(U_jk,g_ij)
      + M(g_jk,g_ij)
      − b_ijk v_ik − c_ijk u_ik − b_ijk c_ijk g_ik.      (6)

Thus in expanded form the often-missed mixed terms are

    v^z_ij(v_jk)g_ij, v^h_ij(u_jk)g_ij, w_ij(g_jk)g_ij,
    v^z_ij(g_jk)v_ij, v^h_ij(g_jk)u_ij,
    μ_z(v^h_ij(g_jk),g_ij), μ_h(v^z_ij(g_jk),g_ij),
    M(g_jk,g_ij), −b_ijk c_ijk g_ik,

in addition to the ordinary pure-lift cross products, their derivative terms, and −b v_ik−c u_ik. No derivatives of b or c occur on the right because of the proven complementary-factor support. Without that support one would additionally have −μ_h(b,g_ik)−μ_z(c,g_ik).

Formula (6) is a fully specified source once any solutions of (5) have been selected. It is separately affine-linear in u and v; its only terms bilinear in these two unknown pure representatives are u_jk v_ij+v_jk u_ij. The remaining terms are determined linear operators or the known ambient-only source. This is stronger data than an unspecified mixed small-extension defect.

## 4. Cocycle, correction, and exact gluing criterion

Put C_ijk=g_ik^−1 R_ijk, represented in the i row frame. Let τ_ij(x)=g_ij^−1 x g_ij, including coefficient-line restriction. The endomorphism-sheaf differential is

    (δx)_ijk = x_ij + τ_ij(x_jk) − x_ik.

Associativity, overlap identities, and the actual unit pentagon imply the four-index defect identity from module lifting report. Since all pure defects vanish by (5), the remaining defect is J-valued and products with positive-order coefficients vanish. Therefore the identity reduces to

    R_ikl + g_kl R_ijk − R_ijl − R_jkl g_ij = 0,

which is precisely δC=0 after normalization. This proves closure without any unproved characteristic-map computation or comparison with a frozen module two-jet.

A general mixed transition correction is G_ij→G_ij+g_ij x_ij, x_ij in End(E)⊗J. It changes C to C+δx. Hence on the acyclic cover

    a global mixed module exists ⇔ [C]=0 in H²(X,End(E)⊗J),

and its transitions are obtained by solving (1). No extra local module-action equation remains: local modules are the free modules over the already associative local algebras. The obstruction is for this fixed external-product ambient and boundary.

## 5. Explicit variation for arbitrary pure changes

If two solutions of (5) differ by Δu=p and Δv=q, the normalized cochains g_ij^−1p_ij and g_ij^−1q_ij are Čech one-cocycles in End(E)⊗K_z and End(E)⊗K_h. Keep the ambient fixed. Subtracting (6) gives the complete finite variation

    ΔR_ijk = [v^z_ij(q_jk)+v^h_ij(p_jk)]g_ij
      + U_jk q_ij + p_jk v_ij + p_jk q_ij
      + V_jk p_ij + q_jk u_ij + q_jk p_ij
      + μ_z(g_jk,q_ij)+μ_z(q_jk,g_ij)
      + μ_h(g_jk,p_ij)+μ_h(p_jk,g_ij)
      − b_ijk q_ik − c_ijk p_ik.                       (7)

Here U,V are computed from the OLD pure lifts. The polarized last quadratic interaction p_jk q_ij+q_jk p_ij is retained; variation is not merely the top-order ambient characteristic map. This matters on the open stable-family locus, where genuine non-gauge pure changes can exist.

## 6. Pure gauge: full mixed correction and coboundary primitive

Let a_i in End(E)⊗K_z and d_i in End(E)⊗K_h. Use the simultaneous reduction-identity frame units H_i=1+a_i+d_i and the gauge convention

    G'_ij = F_ij(H_j) ⋆ G_ij ⋆ H_i^−1.

Its pure coefficients are

    u'_ij = u_ij+a_j g_ij−g_ij a_i,
    v'_ij = v_ij+d_j g_ij−g_ij d_i.                    (8)

The inverse has mixed coefficient a_i d_i+d_i a_i; no derivative contribution occurs in that inverse because derivatives of its identity coefficient vanish and other eligible terms exceed a permitted bidegree. Even though G had mixed coefficient zero, the transformed transition has mixed coefficient

    Q_ij = [v^z_ij(d_j)+v^h_ij(a_j)]g_ij
      + a_j v_ij+d_j u_ij
      + μ_z(d_j,g_ij)+μ_h(a_j,g_ij)
      + g_ij(a_i d_i+d_i a_i)
      − (u_ij+a_j g_ij)d_i − (v_ij+d_j g_ij)a_i
      − μ_z(g_ij,d_i) − μ_h(g_ij,a_i).                 (9)

All frame coefficients from j are restricted to the common overlap; the notation follows the row convention. Formula (9) includes every cross contribution of the chosen simultaneous gauge. Taking successive pure gauges instead differs by an additional mixed frame coefficient and gives the equivalent coboundary formula.

The full defect transforms exactly as

    D'_ijk = F_ij F_jk(H_k) ⋆ D_ijk ⋆ H_i^−1.

To check, insert the gauge definition into the left module equation and use F_ij F_jk(H_k)=A_ijk F_ik(H_k) A_ijk^−1. Since D is J-valued and all H reduce to 1, D'=D. Thus retaining Q gives literally the original normalized defect. Resetting the mixed coefficient to zero, as required in definition (6), removes the correction Q and gives

    C(u',v') − C(u,v) = −δ(g_ij^−1 Q_ij).             (10)

This is the requested explicit primitive for variation under simultaneous pure gauge. It is stronger than only asserting abstract invariance under isomorphism.

An optional mixed coefficient e_i in H_i adds e_j g_ij−g_ij e_i to Q. Its normalized contribution is δe, so (10) is unchanged because δ²=0. The formula is therefore independent of this extra choice of gauge extension.

## 7. New reduction for the compact problem and its exact limit

The prior compact existence and vanishing results give nonempty pure lifting groupoids with H¹(End(E)⊗K_z)=H¹(End(E)⊗K_h)=0 and H⁰ likewise zero. Consequently any two pure representatives become related by (8) after a common refinement. Equation (10) now proves directly, at cochain level, that

    Secondary_ext(E) := [C(u,v)]

is a single well-defined class for the specified external-product ambient, independent of the choices made while solving the two pure equations. Thus optimizing over pure lifts cannot change the compact answer. It suffices to choose ANY solutions of (5), insert them into (6), and test the one linear Čech equation (1). This gives a concrete formal route to the remaining obstruction without selecting physical pure jets.

Also H²(X,J)=0, so the trace of this closed C is a scalar coboundary. Choose k with δk=tr C. Then

    C_0 = C − (1/2)δk·Id_E

is a tracefree representative of exactly the same class. This is a mixed module-cochain normalization, not a modification of the ambient gerbe. There is no compact scalar gerbe class to tune. Thus the criterion can equivalently be tested entirely in H²(X,End_0(E)⊗ω_X).

If the mixed class vanishes, the imported H¹ and H⁰ vanishings for End(E)⊗J make the resulting compact mixed lift unique up to unique reduction-preserving isomorphism. Those vanishings do not supply the missing primitive in (1).

On the stable-family open, inserting this C (or C_0) into the earlier double-Čech reduction produces its actual relative torsor representative: choose δ_z x^(0,1)=−C_0^(0,2), then take the vertical class of C_0^(1,1)+δ_h x^(0,1). The new content is that the input C is now explicitly (6), with all ambient cross terms fixed and pure-gauge changes controlled by (9)–(10). Restriction to the open still need not detect the global class.

No assertion follows that E is an external-product bundle, that the mixed class vanishes, that any prescribed frozen module two-jet has been aligned, or that any of the thirty retained physical values has been evaluated. In particular the ordinary rank-two pure Atiyah-square cancellation supplies solutions of (5), not a primitive of their secondary source (6).

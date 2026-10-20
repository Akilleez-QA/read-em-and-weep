# Background translation × first-star-order compatibility

## Result and inherited scope

For the genuine translated family, each inherited first-star sector r=(a,b) has a regular mixed background-parameter × first-star primitive on the actual refined carrier/legal cover. In fixed z,y coordinates its ordered scalar gerbe is parameter-independent. Consequently the full normalized cross term, and separately its tracefree projection, are regular Čech boundaries. The scalar edge variation must still be retained: parameter-independent gerbe does not mean parameter-independent scalar edge correction.

This conclusion is conditional on exactly the universal contraction, determinant normalization, covering and raw-transgression premises inherited by the compatible-family and source-domain proofs. It is not a new authentication of those premises. It concerns the coefficient η ε, where η is a background tangent and ε a single first-star parameter. It proves nothing about ε² or the mixed product of two star parameters, their detector, or source execution.

## 1. Actual first lift and regularity

Bundled mathematical dependencies:

- Compatible background-source translation family, ../structural-boundaries/translated-background-family/PROOF.md, §§1–4,7.
- Uniform owned domain for the translated raw source, ../structural-boundaries/translated-source-domain/PROOF.md, §§1–4.
- Structural closure of literal raw first and mixed second orders, https://github.com/Akilleez-QA/read-em-and-weep/blob/92ccceb1a023dd86bf4d17f4b86b779cc1b7c44f/research/hm/relative-models/relative-mixed-character-purity/dependencies/FIRST-LIFT-STRUCTURAL.md, §§5–6, only its first-order identities. Its second-star-order claims are not used here.
- Genuine background family, diagonal injectivity and ordinary Yoneda primitive, dependencies/BACKGROUND-FAMILY.md, DIAGONAL.md and ORDINARY-YONEDA.md.

Current prerequisite scope is recorded in DEPENDENCIES.md. These are inherited proof premises; the present argument does not depend on a physical computation receipt.

The two inherited Poisson branches are r=(0,1) and r=(2,3) in source zero-based physical labels; the geometric coordinates z_1,…,z_4 use one-based labels. Apply this proof separately to either branch (and, by linearity, their fixed linear combination at first star order). These two branches must not be confused with the four independent background directions. Write the background parameter as t to distinguish it from the scalar edge cochain S. In fixed z,y coordinates, V_d and the root frames are t-independent. For a single translated factor, x_1=z_1+t; for a tangent c in the four-parameter family, x_i=z_i+t c_i. Each V_d commutes with ∂_t. Let

  μ_r(H,G)=((V_a H)(V_b G)−(V_b H)(V_a G))/2.

Thus μ_r is t-independent as a relative bidifferential operator. This does not permit freezing g, its primitive ancestors, or its physical derivatives.

On the genuine family cover let g_jk g_ij=g_ik, det g_ij=1. The accepted transgression gives

  q_d,ij=(m_j,d−m_i,d)y_d/z_d,
  b_r,ijk=(15/4)q_a,ij q_b,jk,
  L_d,ij=g_ij^−1 V_d g_ij,
  k_r,ij=[L_a,ij,L_b,ij]/4,
  u_r,ij=S_r,ij I+k_r,ij,
  U_r,ij=g_ij u_r,ij.

The scalar S_r is the SAME raw transgression recipe given explicitly below. The inherited first-order identity is

  U_jk g_ij+g_jk U_ij+μ(g_jk,g_ij)=U_ik+b_ijk g_ik.       (1)

In particular U_ik is present. Sections 5–6 of the structural closure dependency prove this from the determinant-one rank-two identity and raw transgression. The compatible-family §4 proves that same transgression identity for the translated common split complex; its roots and connections are the fixed z roots, while all primitives are pulled back at v(x). The source-domain §§1–4 supply regularity of these actual family formulas on their carrier/legal opens. Thus (1) transfers as an identity over the parameter, not from equality at t=0 alone.

For a rigorous fixed-cover tangent statement, restrict the genuine family opens to X×Spec k[t]/(t²) and refine the central fiber by affine opens. An open containing a central affine piece contains its nilpotent thickening topologically. Every actual denominator is then a unit on its corresponding formal overlap. Taylor coefficients of regular family functions are regular there. Physical V derivatives and their parameter derivatives extend to these localizations by the quotient rule. No meromorphic global primitive or unjustified product neighborhood is used. The resulting affine cover computes End(E) cohomology.

The four-parameter conclusion uses no new scalar identity: repeat the compatible-family construction for every shifted factor. The same fixed z roots, common split arrows, homogeneous pullback and commuting V proof apply verbatim. Alternatively each tangent c gives the one-parameter substitution x_i=z_i+t c_i directly. Injectivity of the four-dimensional KS map is not needed for the boundary identity, only to identify four independent background directions.

## 2. Full unnormalized derivative

All undotted quantities below are evaluated at t=0, and dot means the actual family derivative. Differentiation of (1) gives the exact identity

  dot U_jk G_ij+U_jk dot g_ij
  +dot g_jk U_ij+G_jk dot U_ij
  +μ(dot g_jk,G_ij)+μ(G_jk,dot g_ij)
  =dot U_ik+dot b_ijk G_ik+b_ijk dot g_ik.             (2)

Here G=g(0). For a parameter-dependent operator there would additionally be dot μ(G_jk,G_ij) on the left. In the present fixed-z trivialization dot μ=0 is justified by [∂_t,V_d]=0. No differentiated transition term or b dot g term has been discarded.

Equation (2) is exactly the η ε coefficient of the genuine two-parameter gluing equation modulo η² and ε². First order in ε has no extra μ acting on b, since b is already multiplied by ε; the convention in (1) is ordinary scalar multiplication on its right.

## 3. Normalization and transport derivative

Use first-index End frames and define

  a_ij=G_ij^−1 dot g_ij,
  u_ij(t)=g_ij(t)^−1 U_ij(t),
  m_ijk(t)=g_ik(t)^−1 μ(g_jk(t),g_ij(t)),
  T_ij(t)(M)=g_ij(t)^−1 M g_ij(t).

For a 1-cochain v set (δ_t v)_ijk=T_ij(t)v_jk−v_ik+v_ij. Then (1) is precisely

  δ_t u(t)+m(t)=b(t) I.                             (3)

For any varying matrix M,

  ∂_t(T_ij(t)M(t))|₀=T_ij dot M+[T_ij M,a_ij].

Also

  dot u_ij=G_ij^−1 dot U_ij−a_ij u_ij,
  dot m_ijk=−a_ik m_ijk
     +G_ik^−1[μ(dot g_jk,G_ij)+μ(G_jk,dot g_ij)].     (4)

The −a_ik m term retains the variation of the output normalization. For variable μ add G_ik^−1 dot μ(G_jk,G_ij).

Differentiating (3) now yields

  δ dot u+C=dot b I,
  C_ijk=[T_ij u_jk,a_ij]+dot m_ijk.                 (5)

This is the complete normalized cross term for this convention. A formula containing only dot m, or differentiating μ while freezing the transports, is not (5). The commutator's scalar edge part vanishes, but that does not erase the scalar part of dot u.

For any regular parameterized first lift, regardless of the special gerbe formula,

  tf(C)=−δ tf(dot u).                              (6)

Trace and projection tf(M)=M−tr(M)I/2 commute with δ. Thus (6) is already a regular tracefree boundary theorem. It also proves closure, rather than assuming it.

## 4. Exact scalar variation and the stronger actual-family conclusion

In the fixed z,y family every q_d,ij is independent of t. Therefore

  dot b_r,ijk=0.                                   (7)

This is an equality of the actual ordered scalar gerbe, not merely its cohomology class. Infinity-x expressions for q may have moving coefficients and odd basis; their full horizontal derivatives still vanish. Freezing only their displayed inverse-chart coefficients would not implement (7).

Write ranks n_l=(5,15,10,2), weights w_l=(−1,1,3,5), signs e_l=(−,+,−,+), and B_i,d^l for the complete actual raw blocks. The precise scalar recipe is

  S_r,ij=(1/4)Σ_l e_l {tr(B_i,a^l B_j,b^l−B_i,b^l B_j,a^l)
      +(w_l/2)[q_a,ij tr(B_i,b^l+B_j,b^l)
                 −q_b,ij tr(B_i,a^l+B_j,a^l)]}
      −(15/8)q_a,ij q_b,ij.

Consequently its required derivative is

  dot S_r,ij=(1/4)Σ_l e_l {
      tr(dot B_i,a^l B_j,b^l+B_i,a^l dot B_j,b^l
           −dot B_i,b^l B_j,a^l−B_i,b^l dot B_j,a^l)
      +(w_l/2)[q_a,ij tr(dot B_i,b^l+dot B_j,b^l)
                 −q_b,ij tr(dot B_i,a^l+dot B_j,a^l)]}. (8)

There are no dot q terms in these fixed coordinates; the derivative of the final q_a q_b term is zero for that proved reason only. All four blocks and both endpoint-linear terms remain. In a convention where q varies, differentiate every q occurrence as well, including the final term; that is not the fixed-z family used here.

For an explicit ancestor rule, in a common reference B_i,d^l=−(V_d F_i^l)(F_i^l)^−1−A_old,i,d^l. With fixed z-root old connection, dot A_old=0, and

  dot B_i,d^l=−(V_d dot F_i^l)(F_i^l)^−1
       +(V_d F_i^l)(F_i^l)^−1 dot F_i^l(F_i^l)^−1.

Thus (8) differentiates the entire split-frame recipe. In moving target frames the connection/frame change terms must also be differentiated; this common-reference expression is not permission to erase them.

Since dot g=G a and [∂_t,V_d]=0,

  dot L_d=V_d a+[L_d,a],
  dot k_r=([dot L_a,L_b]+[L_a,dot L_b])/4,
  dot u_r=dot S_r I+dot k_r.                       (9)

Every k and dot k is traceless. Combining (5), (7), (9) gives explicit regular primitives

  C=−δ(dot S_r I+dot k_r),
  tf(C)=−δ dot k_r.                               (10)

Taking traces of (5) gives the indispensable scalar compatibility

  δ dot S_r=−(1/2)tr(dot m).                       (11)

The commutator has zero trace. Hence fixed gerbe is compatible precisely with the scalar edge variation (8), whose derivative identity (11) follows from the actual first lift. Setting dot S=0 without proving tr(dot m)=0 generally breaks compatibility. No vanishing or nonvanishing value of either side is computed here.

## 5. General changing-gerbe distinction and limits

For a general family with dot b≠0, (5) instead says C−dot b I=−δ dot u. Thus tracefree exactness remains valid, but full fixed-gerbe exactness requires the scalar class [dot b] to vanish (assuming dot b is a scalar Čech cocycle). If dot b=δh, the full primitive is h I−dot u. The trace identity is δ(tr dot u/2)+tr(dot m)/2=dot b. This general qualification is essential, although (7) removes it for the actual fixed-root translated family.

Regularity here means regular sections on the actual refined carrier/legal overlaps, yielding a genuine Čech boundary on X. It does not mean an unlocalized global matrix primitive on each standard chart, nor a new operational cutoff, owned bound or software-admission result. Ordinary polarized Yoneda products from the background family and the open mixed-Poisson ε² problem remain distinct.

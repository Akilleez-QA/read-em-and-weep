# Conditional fibers and differential failure of the resolved cubic map

Status: structural mathematical proof, conditional on the pinned predecessor below. Independent mathematical review is recorded in REVIEW.md; this is not formal proof-assistant verification. Work over C. The common intersection dimension r remains entirely unevaluated. No selected actual HM/source coefficients, matrices, points, numerical ranks, or computer-algebra calculations are used.

## 1. Pinned input and theorem

The sole mathematical dependency is PR604 at

    a4a0b5ed6e9dd0c18e3a263d1b3f8d9a49f2bf8d,
    research/hm/cubic-embedding-locus/PROOF.md.

Immutable source:

https://github.com/Akilleez-QA/read-em-and-weep/blob/a4a0b5ed6e9dd0c18e3a263d1b3f8d9a49f2bf8d/research/hm/cubic-embedding-locus/PROOF.md

Its dependencies, including the actual primary/modular dictionary, remain in force. We use the following proved facts from that source, not merely matching numerical data.

Let S be the actual primary surface in P4, Z its thirty reduced nodes, and

    pi:M=Bl_Z(P4)->P4,       Phi:M->V subset P9.

The map Phi is the finite birational normalization of its reduced image, induced by the ten cubic generators c of I_Z. Its source M is smooth of dimension four. The actual linear syzygy L(x) satisfies L(x)c(x)=0; the associated bilinear incidence is

    B(y)x=L(x)y,            B(Phi(m))pi(m)=0.

There are sixty pentagon-component lines ell in S, each containing exactly two nodes z,w. Their strict transforms ell_tilde are embedded by Phi as projective lines. Each exceptional divisor E_z is embedded as the linear P3

    Phi(E_z)=P(ker L(z)).

For every component line define

    K_ell=ker L(z) intersect ker L(w),
    Sigma_ell=P(K_ell),     Sigma=union_ell Sigma_ell.

Their common vector-space dimension is r in {0,1,2}. Nonempty Sigma_ell are pairwise disjoint. Phi is an isomorphism off Phi^(-1)(Sigma), and Sigma is exactly the reduced singular/nonnormal locus of V. For y in Sigma_ell,

    Lambda_y=P(ker B(y))=ell,
    |Phi^(-1)(y)| subset ell_tilde union E_z union E_w.       (1)

At a non-node x in ell, ker L(x) has dimension two. Finally, distinct exceptional divisors are disjoint.

Write p_z=ell_tilde intersect E_z and p_w=ell_tilde intersect E_w, and let

    alpha_ell=Phi(p_z),     beta_ell=Phi(p_w).

These are distinct, since Phi embeds ell_tilde. The notation depends on an ordering of the two endpoints, but the statements do not.

**Theorem.**

1. If r=1, each of the sixty points Sigma_ell has precisely two preimages, one in E_z and one in E_w. Both are unramified points of Phi. The scheme-theoretic fiber is two reduced C-points, of total length two. Phi is unramified everywhere on M, although it is not an isomorphism at these two-point fibers.

2. If r=2, Sigma_ell=Phi(ell_tilde). For every y in Sigma_ell other than alpha_ell,beta_ell, its fiber consists of three distinct unramified points: one on ell_tilde minus E, one on E_z, and one on E_w. The scheme-theoretic fiber is reduced of length three.

3. Still if r=2, over alpha_ell the fiber has exactly two geometric points: p_z and a point of E_w. The differential at p_z has rank exactly three and one-dimensional kernel; it is injective at the other point. Over beta_ell the analogous assertion holds with z and w reversed. These are all the differential failures on M. There are exactly 120 distinct such source points and exactly 120 distinct target values.

4. At each of the 120 ramified source points, the local fiber algebra has embedding dimension one and is isomorphic to C[t]/(t^e) for some finite e>=2. The other point in that fiber is reduced. No value of e is determined here; in particular no exact length of an endpoint fiber is claimed.

Here “unramified” has its usual morphism-theoretic meaning, Omega_(M/V)=0 locally. “Ramified point” means a point where this finite morphism is not unramified, equivalently here a point with a nonzero tangent kernel. No branch-divisor or smooth-target interpretation is intended. Differential ranks can be computed in the ambient tangent space of P9, since T_y V injects into T_y P9.

For r=0 the predecessor already proves that Phi is a closed immersion. This note does not select any of the three alternatives.

## 2. Universal restriction to an arbitrary component line

Fix an arbitrary component line ell=zw and choose homogeneous parameters x=sz+tw. Every cubic generator vanishes at [1:0] and [0:1], so its restriction is divisible by st. Consequently there are two vectors a,b in C^10 such that, identically on this abstract parameter line,

    c(sz+tw)=st(sa+tb).                                     (2)

These are unevaluated restriction vectors, defined uniformly for every component line. No actual endpoint representative, coordinate entry, or source instance is selected for calculation. Rescaling parameters changes their representatives but not the projective conclusions.

Removing the two simple base factors gives the resolved map

    Phi|ell_tilde : [s:t] |-> [sa+tb].                       (3)

The predecessor proves this is an O(1) embedding. Thus a,b are linearly independent, and

    C_ell=span(a,b),    Phi(ell_tilde)=P(C_ell),
    alpha_ell=[a],      beta_ell=[b].                        (4)

Set L_z=L(z) and L_w=L(w). Substituting (2) into L(x)c(x)=0, canceling the nonzero polynomial st, and comparing the three coefficients of the remaining quadratic identity gives

    L_z a=0,        L_w b=0,        L_z b=-L_w a.            (5)

Put d=L_z b=-L_w a. For any u=lambda a+mu b in C_ell,

    L_z u=mu d,       L_w u=-lambda d.                     (6)

If d is nonzero, these two equations force

    K_ell intersect C_ell=0.                               (7)

If d=0, they instead give C_ell subset K_ell. Since C_ell has dimension two and dim K_ell<=2, this means K_ell=C_ell and r=2. In particular,

    r=1  ==>  K_ell intersect C_ell=0.                      (8)

For the converse needed in the r=2 case, suppose dim K_ell=2. Linearity of L puts K_ell inside ker L(x) for all x in ell. At every non-node point of ell both dimensions are two, so

    K_ell=ker L(x).

For st nonzero, (2) and L(x)c(x)=0 then put sa+tb in K_ell. As [s:t] varies over the punctured line, these vectors span C_ell. Therefore C_ell subset K_ell, and equality follows. We have proved the full useful dichotomy

    r=1:  P(K_ell) is disjoint from P(C_ell);
    r=2:  K_ell=C_ell and Sigma_ell=Phi(ell_tilde).          (9)

This is a symbolic implication, not an evaluation of d or r for the actual construction.

## 3. All geometric fibers over Sigma

Every y in Sigma_ell lies in both Phi(E_z) and Phi(E_w). Since each exceptional restriction is an embedding, it has exactly one preimage e_z(y) in E_z and exactly one e_w(y) in E_w. They are distinct because E_z and E_w are disjoint.

If r=1, (9) says y is not in Phi(ell_tilde). By the exhaustive incidence restriction (1), there are no other preimages. Thus

    |Phi^(-1)(y)|={e_z(y),e_w(y)}.                          (10)

If r=2, (9) gives exactly one preimage h(y) on ell_tilde. For y different from alpha_ell,beta_ell, this point lies outside E_z union E_w, so the three points h(y),e_z(y),e_w(y) are distinct and exhaust the fiber.

At y=alpha_ell, h(y)=e_z(y)=p_z. The point e_w(y) remains distinct. At y=beta_ell, h(y)=e_w(y)=p_w, with e_z(y) distinct. There can be no contribution from another component line: (1) confines the pi-image to the single line ell, and the classification already includes all pi-fibers above its two nodes.

This argument establishes support only. Reducedness is proved below from the differential calculation, not inferred from the number of points.

## 4. Incidence controls every possible tangent kernel

We first record the projectively well-defined differential consequence of incidence. If m maps to y and pi(m)=x, then

    dPhi_m(v)=0  ==>  dpi_m(v) belongs to T_x Lambda_y.     (11)

Indeed choose local nonzero vector lifts of x and y. If the projective variation of y vanishes, its lifted variation is a scalar multiple of y. In the derivative of B(y)x=0, that scalar term vanishes because B(y)x=0. The remaining equation is B(y)dx=0. Modulo the line Cx, this is exactly tangency to the projective linear kernel P(ker B(y)). Thus (11) applies also at exceptional points; it does not assume pi is locally an isomorphism.

For y in Sigma_ell, Lambda_y=ell. If m is outside E, pi is locally an isomorphism. Then (11) says that any vector in ker dPhi lies in the tangent line to ell_tilde. Since the restriction (3) is immersive, that vector must be zero. This proves injectivity at the third, nonexceptional point of every three-point fiber in the r=2 case.

At m in E_z, the blowup differential has kernel T_m E_z and image the one-dimensional radial direction R_m in T_z P4 represented by m. For completeness, in a universal blowup chart

    x_1=t,       x_i=t u_i  (2<=i<=4),

its differential at t=0 sends (dt,du_2,du_3,du_4) to dt(1,u_2,u_3,u_4). Hence

    ker dpi_m=T_m E_z,      im dpi_m=R_m.                  (12)

There is exactly one m in E_z with R_m=T_z ell, namely p_z. Therefore, if m is in E_z but m is not p_z, (11) and (12) force dpi_m(v)=0 for every v in ker dPhi_m: two distinct one-dimensional subspaces R_m and T_z ell intersect only in zero. It follows that v is tangent to E_z. The linear embedding Phi|E_z is immersive, so v=0.

Consequently Phi is unramified at every exceptional preimage over Sigma_ell except possibly p_z and p_w. In the r=1 case neither of these points lies over Sigma_ell, by (9). In the r=2 case they map to alpha_ell,beta_ell, and all other exceptional preimages, including the opposite exceptional point at each endpoint target, have injective differential.

## 5. Exactly one tangent direction is lost at each endpoint when r=2

Assume r=2 and consider p_z. The strict transform ell_tilde meets E_z transversely. This is immediate in the chart of (12), choosing the first coordinate in the line direction: ell_tilde is u_2=u_3=u_4=0 and E_z is t=0. Hence

    T_(p_z)M = T_(p_z)E_z + T_(p_z)ell_tilde,

with the line T_(p_z)ell_tilde not contained in T_(p_z)E_z.

On the other hand, (9) gives

    Phi(ell_tilde)=Sigma_ell subset Phi(E_z).

Thus the image of the tangent line to ell_tilde is contained in the image of T_(p_z)E_z. The latter image is three-dimensional because Phi|E_z is a linear embedding. It follows that the image of all T_(p_z)M is exactly that same three-dimensional space:

    rank dPhi_(p_z)=3,       dim ker dPhi_(p_z)=1.          (13)

Equivalently, a nonzero tangent vector along ell_tilde has the same image as a unique vector tangent to E_z, and their difference is the nonzero kernel direction. This is a calculation of the ambient four-dimensional differential; it does not claim the kernel is tangent to ell_tilde itself. The identical argument applies at p_w.

All points outside Phi^(-1)(Sigma) have injective differential because Phi is an isomorphism there. Sections 4 and 5 therefore give the complete differential-failure locus.

For each ell its two endpoint target values are distinct by (3). For different ell they cannot coincide, since the Sigma_ell are pairwise disjoint. Hence the sixty lines contribute exactly 120 distinct target values, each with exactly one ramified source point. The source points are therefore distinct as well. No multiplicity or reducedness is asserted for the scheme defined by the differential failure.

## 6. Scheme-theoretic fibers and the remaining local integer

Let f:U->W be any finite morphism of complex varieties, let u map to a closed point w, and write

    B=O_(U,u),       F=B/m_w B.

The local fiber algebra F is Artinian with residue field C. Its maximal ideal n satisfies

    n/n^2 = m_u/(m_u^2+m_w B).                             (14)

The dual of (14) is exactly the kernel of the tangent map T_u U->T_w W. In particular an injective tangent map gives n/n^2=0. Nakayama applied to the finite F-module n yields n=0. Therefore

    d f_u injective  ==>  F=C.                             (15)

The same cotangent calculation identifies Omega_(U/W) tensor k(u) with (14); Nakayama over O_(U,u) makes its vanishing equivalent to f being unramified at u. Thus all uses of “unramified” in the theorem follow from the displayed tangent computations, with no smoothness assumption on W.

Apply (15) at every point of the fibers in (10) and at the three-point fibers of Section 3. A finite C-scheme is the disjoint union of its local Artinian pieces, so these fibers are respectively two and three reduced points, of lengths two and three. Over V minus Sigma the fibers are single reduced points by the isomorphism already proved in the predecessor.

At an endpoint in the r=2 case, (13) and (14) instead give dim_C(n/n^2)=1. Choose t in n spanning this quotient. Nakayama gives n=(t). Since n is nilpotent, some least e>=2 satisfies t^e=0. Every element of F can be expanded as a scalar plus a scalar times t and then iterated, so C[t]->F is surjective. Its kernel is precisely (t^e): an element of lower order cannot vanish, because its leading nonzero scalar factor is a unit. Consequently

    F is isomorphic to C[t]/(t^e),        e>=2.             (16)

The other point of the endpoint fiber is unramified and has local algebra C. Thus the complete endpoint fiber algebra is abstractly

    C[t]/(t^e) times C,

with e not determined. Formula (16) proves a curvilinear local fiber, not an analytic normal form for Phi or for its image. In particular the statement does not decide whether e=2, whether the whole fiber has length three, or how image branches intersect.

## 7. Reduced inverse image of a bad line

There is a further geometric consequence when r=2 that does not require the missing multiplicity. Define

    A_(ell,z)=(Phi|E_z)^(-1)(Sigma_ell),
    A_(ell,w)=(Phi|E_w)^(-1)(Sigma_ell).

Both are linear P1s in the corresponding exceptional P3, and each maps isomorphically to Sigma_ell. The fiber-support classification proves the equality of reduced closed subschemes

    (Phi^(-1)(Sigma_ell))_red
       = A_(ell,z) union ell_tilde union A_(ell,w).         (17)

The three smooth rational curves form a chain: the two exceptional curves are disjoint, and ell_tilde meets them at p_z,p_w respectively, with distinct tangent lines in M. Each component maps isomorphically to the target line. At the two chain junctions the component images have the same tangent direction in the target, which is compatible with, and explains, the lost ambient tangent direction in (13).

Equation (17) concerns the reduced inverse image. It does not assert that the scheme-theoretic inverse image has no nilpotents, nor that its finite map is flat. The local fiber result (16) is the precise retained boundary.

## 8. Contribution and scope

The unresolved number r is now tied to a complete conditional classification of the finite normalization fibers and the support of its differential failure. If r=1, the only bad target values have two reduced unramified preimages. If r=2, the sixty bad lines have reduced three-point fibers away from exactly 120 endpoint values; precisely one point over each endpoint value has a one-dimensional tangent kernel, and its finite local fiber is curvilinear of undetermined length.

These conclusions use universal cubic restriction identities, incidence differentiation, and elementary local algebra. They do not evaluate an actual kernel, choose a favorable instance, or substitute generic position for a proof. They do not determine r; establish a scheme structure for the singular or ramification loci; decide endpoint fiber lengths; determine transverse analytic branch types; classify the surface image T along T intersect Sigma; or resolve the separate full-adjoint, higher-lifting, and algebraicity goals.

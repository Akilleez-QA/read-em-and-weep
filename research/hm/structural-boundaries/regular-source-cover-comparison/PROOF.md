# A regular actual-source-cover comparison for the central scalar

## Result and exact scope

Let X=C^4, C:y^2=x^3-x, q:X→Y=(P1)^4, and retain the actual legal/carrier/standard-tag cover and the frozen raw rational denotation from the accepted dependency packets. Let M be the ACTUAL ten-term, left-normalized mixed defect, using U_r=g(s_raw,r I+k_r), and let c=tr(M)/2. The accepted central and structural-closure proofs give dc=0, full deck character, and

    M-R=c I-d_row W,       W=s_raw,q k_p+s_raw,p k_q.       (0.1)

After the branch-safe character identification, c is an L=O_Y(-2,-2,-2,-2)-valued cochain on the base refinement underlying the actual source cover. We construct a bounded source scalar complex S_D, the entire regular ALL-ORDERED ordinary sixteen-open complex O, and maps

    Pi:S_D→O,       B:O→S_D,       K:S_D^n→S_D^(n-1),
    Pi B=1,        dK+Kd=1-B Pi.                          (0.2)

The maps use polynomial Bezout witnesses chosen once from proved unit ideals. Their values are not calculated. The actual full c belongs to S_D. Every map is a genuine cochain operator in all degrees, with regularity on its specified target, rather than a selector on one component.

The ordinary/tensor comparison packet supplies a regular all-ordered ordinary operator H_O with dH_O+H_Od=1-P_O, where P_O is supported only in degree four. Consequently

    b=B H_O Pi(c)+K(c),             db=c.                (0.3)

This is a regular primitive on the ACTUAL source cover after the inverse character identification. If beta is that scalar function-valued primitive on X, then

    M-R=d_row(beta I-W).                                 (0.4)

No End-valued comparison is required for (0.4): scalar inclusion on the actual cover is canonical and commutes with d_row. This removes only the central difference between M and R. It does not prove R exact, assign an obstruction value, construct a higher-order lift, or evaluate beta, c, an actual source, a model, a physical matrix, or an actual polynomial instance.

This is an explicit operator formula parameterized by a CHOSEN collection of polynomial Bezout witnesses; existence of those witnesses is proved. It is not an expanded numerical primitive or a computation of the witnesses. No equality with separately prescribed witnesses or degree bound is asserted.

## 1. The actual principal refinement and polynomial witnesses

Work over k=Q; the argument and all chosen identities base-change to characteristic-zero fields. Write V_A for a standard product chart of Y, indexed by A∈{0,1}^4, with polynomial coordinate ring R_A. Let a=(A,h,m) be a source index, where h is one of the six actual carriers and m is a four-bit legal mask. Keep ALL such original indices and their tags A(a)=A, including repeated labels in cochain tuples. Distinct occurrences are always counted separately.

The primary homogeneous carriers are h_j=v_j^5-∏_r v_r, j=0,...,4, and the auxiliary is v_0v_1v_3v_4. Their local representatives on V_A are H_(A,h). The accepted product-root proof shows that their opens cover: if all h_j vanish and ∏v_r=0, all v_j vanish, impossible for the product of four nonzero binary forms; if ∏v_r≠0 the auxiliary is nonzero. This is a residue-field argument at every point, not merely a test of sampled rational points.

The legal homogeneous sections in one coordinate have representatives

    finite chart:    L_0=1,          L_1=x(x^2-1),
    infinity chart:  L_0=t,          L_1=1-t^2.             (1.1)

They are sections of degrees one and three, respectively; (1.1) includes their actual frame changes. The two legal opens cover in either chart, since 1 is a unit on the finite chart and t and 1-t^2 cannot vanish together on the infinity chart. The actual source owner open on X is

    U_a=q^(-1)(W_a),
    W_a=V_A ∩ D(H_(A,h) ∏_r L_(A,m_r,r)).               (1.2)

The root and legal proofs identify precisely these opens and the physical frames on them, including branch and infinity loci. Empty opens, if any, contribute nothing and may be retained.

Put

    C_a=H_(A,h)^54 ∏_r L_(A,m_r,r)^29 ∈ R_A.            (1.3)

All exponents are positive, so D(C_a)=W_a inside V_A. For a fixed A these principal opens cover V_A. Equivalently, their pullbacks cover Spec S_A, where

    S_A=R_A[z_0,...,z_3]/(z_r^2-f_r)

is free of rank 16 over R_A and hence faithfully flat. The source-cover theorem gives (C_a)S_A=S_A, and faithful flatness gives (C_a)=R_A. Directly, a proper ideal (C_a) would lie in a maximal ideal, producing an uncovered point. No effective Nullstellensatz estimate or calculation is used.

Thus choose, ONCE FOR EACH A and independently of any cochain, polynomials Q_(A,a)∈R_A with

    ∑_(a:A(a)=A) C_a Q_(A,a)=1.

Define rho_(A,a)=C_a Q_(A,a). Then

    ∑_a rho_(A,a)=1,        rho_(A,a)∈C_a R_A.           (1.4)

These are ordinary algebraic weights on an affine chart, not global regular functions on projective Y. Existence is over Q itself, since the ideal argument was over Q; no descent of unspecified complex coefficients is assumed. We make no degree bound on Q. Subsequent formulas involve only finite sums and these fixed chosen witnesses.

## 2. The exact scalar domain and line frames

For a tuple a=(a_0,...,a_n), let

    V_tag(a)=∩_j V_(A(a_j)),        W_a=∩_j W_(a_j).

The latter notation for a tuple is distinct from the single-index W_a of (1.2). All tuple complexes here are ALL-ORDERED: entries are not presumed alternating and repeats are allowed. The differential is the alternating sum of face restrictions, without antisymmetrizing a source formula. This includes the unsymmetrized actual raw scalar and gerbe conventions. This is a mathematical all-ordered cochain complex; its repeated tuples are retained.

Let

    D_a=H_(A(a),h(a))^16 ∏_r L_(A(a),m(a)_r,r)^10.       (2.1)

Each D_a is a regular function on its own standard chart, a unit on W_a. On V_tag(a), every D_(a_j) is defined by restricting from its own chart; its conversion from a homogeneous common-chart representative differs by a unit there. The chart tags are kept, so these changes never borrow an absent chart.

Define S_D^n to consist of families f_a∈Γ(W_a,L) such that

    N_a=(∏_(j=0)^n D_(a_j)) f_a                         (2.2)

extends to a regular L-section on the FULL V_tag(a). Extension is unique: Y is integral, L is locally free, and a nonempty W_a is dense in V_tag(a). Components on empty intersections and their chosen N extensions are zero by definition; no uniqueness from restriction to an empty set is asserted. Equivalently one may use rational L-sections satisfying the specified clearance. S_D is a k-vector space, with no affine-numerator degree bound.

For a face, multiplying its cleared extension by D of the deleted occurrence and restricting to V_tag(a) clears that face. Summing proves dS_D^n⊆S_D^(n+1). Thus S_D is a subcomplex; in particular the domain is not restricted to a closed degree-two input. Repeated equal divisors still contribute their occurrence multiplicities in (2.2).

Define O^n=∏_(A_0,...,A_n) Γ(V_(A_0)∩...∩V_(A_n),L), with the same all-ordered convention. It is the entire regular ordinary sixteen-open complex, not the four-factor tensor complex.

For character extraction, S_A=⊕_(E⊆{0,1,2,3}) R_A z_E, with z_r=y_r or u_r according to the chart. Localizing by the invariant carrier/legal functions preserves this decomposition. A full-character scalar is z_all f_A; extract f_A by this R_A-linear direct-summand projection, never by dividing by a branch coordinate in a regular ring. Its transition is

    f_B=(tau_B/tau_A)^(-2) f_A,

the coefficient law for L=O(-2,-2,-2,-2). Every invariant clearing bound survives projection. Conversely the local products z_all f_A glue to the full-character function-valued cochain on X. These inverse identifications commute with restriction and d. All formulas below are intrinsic L-section formulas; if stored in first-tag frames, the actual transition units must be used before addition.

## 3. Full M, rather than only its scalar-free baseline, is admitted

Use the accepted ownerwise theorem together with the later raw-block all-chart proof (discharging its retained B5/1 premise) and complementary-scalar-derivative proof (discharging its retained stripped-derivative premise), all separately snapshotted and pinned here. Their established bounds, at EACH of an edge's two actual occurrences, are

    g,g^-1:2/1,    Dg:3/2,    distinct D2g:4/3,
    k_r:6/4,       s_raw,r:5/2,
    Dk_r:7/5,      D s_raw,r:6/3.

The inverse is the actual rank-two adjugate, as justified by the accepted determinant/closure theorem. Bounds are powers of named owned factors, including actual homogeneous and physical-frame laws; no numerical valuation-one assumption at a ramified coordinate is made.

For the FULL first lift x_r=s_raw,r I+k_r, addition gives x_r≤6/4; therefore

    U_r=g x_r≤8/5,             D U_r≤9/6                (3.1)

at each endpoint. The scalar contribution g s has the smaller 7/3 bound. The two Leibniz terms in DU have respectively 3/2+6/4 and 2/1+7/5, both 9/6. Thus derivatives of the scalar part of U are retained.

Put A=g_ij, B=g_jk, G=g_ik. Keeping the actual left normalization G^-1 and all ten slots gives the following vectors on the ORIGINAL ordered occurrences (i,j,k):

| Family | Slots | Carrier vector | Legal vector |
|---|---:|---|---|
| G^-1 U_jk U_ij | 2 | (10,16,10) | (6,10,6) |
| G^-1 mu(U_jk,A) | 2 | (5,12,11) | (3,8,7) |
| G^-1 mu(B,U_ij) | 2 | (11,12,5) | (7,8,3) |
| G^-1 mu_pq(B,A) | 1 | (6,8,6) | (4,6,4) |
| G^-1 b U_ik | 2 | (10,0,10) | (7,2,7) |
| G^-1 b_p b_q G | 1 | (4,0,4) | (4,4,4) |

Here b has carrier zero and legal (1,2,1). Multiplication adds charges at shared occurrences; for example the middle U-U charge is 8+8=16. Addition takes coordinatewise maxima only after occurrence alignment. No cocycle simplification, inverse cancellation or trace cancellation is used. The maximum is

    M: carrier (11,16,11), legal (7,10,7).               (3.2)

Trace and multiplication by 1/2 preserve this bound. The accepted all-chart membership and homogeneous-clearing theorems give regularity of the cleared coefficients on every common standard target; projecting to the full-character coefficient preserves it. Uniform 16/10 padding in (2.1) therefore proves c∈S_D^2. Its differential also belongs by the subcomplex argument, and the accepted closure theorem gives dc=0. This uses full-M closure, rather than inferring it from trace-free closure.

No stronger statement about all arbitrary source regular cochains is needed: those with unbounded carrier/legal poles need not admit this one fixed partition.

## 4. The full source-to-standard cochain map

For f∈S_D^n set

    (Pi f)_(A_0,...,A_n)
      =∑_(a_j:A(a_j)=A_j) (∏_(j=0)^n rho_(A_j,a_j))
                                      f_(a_0,...,a_n).  (4.1)

The right side initially denotes sections on their source subintersections. Define each summand on the whole standard target using its unique cleared extension N_a from (2.2):

    (∏_j rho_(A_j,a_j)/D_(a_j)) N_a.                  (4.2)

Each quotient is the polynomial

    rho_(A,a)/D_a=H_a^38 ∏_r L_(a,r)^19 Q_(A,a)

on V_A, so (4.2) is regular on V_(A_0)∩...∩V_(A_n). No original suffix is present in (4.1); EVERY source occurrence has its own weight. Thus Pi lands in O, with no carrier/legal denominators left. No bound on the polynomial degrees of Q is necessary for regularity or for finite Laurent splitting on standard intersections.

To prove dPi=Pi d, restrict to a common source locus and expand. In the r-th face of Pi(df), the variable a_r is absent from f, and summing its weight gives 1 by (1.4). The remaining terms are exactly the r-th face of d(Pif), with sign (-1)^r. Restrictions and intrinsic L-frame changes commute with these scalar multiplications. Equality on the dense locus extends to equality of the regular sections just constructed. This proves the cochain identity in EVERY degree, including nonclosed inputs.

The reverse map is ordinary index restriction:

    (B F)_(a_0,...,a_n)
       =F_(A(a_0),...,A(a_n)) restricted to W_a.         (4.3)

It is a cochain map and lands in S_D, since multiplication by ∏D_a gives a regular section on V_tag(a). Summing all weights in (4.1) gives Pi B=1_O. Nothing in B changes the original source index set, removes a source open or substitutes a tag from outside the tuple.

## 5. The partition homotopy and its exact regular domain

Set K=0 on degree zero. For n≥1 define

    (K_n f)_(a_0,...,a_(n-1))
      =∑_(i=0)^(n-1) (-1)^i
         ∑_(b_j:A(b_j)=A(a_j), 0≤j≤i)
           (∏_(j=0)^i rho_(A(a_j),b_j))
                 f_(b_0,...,b_i,a_i,...,a_(n-1)).      (5.1)

The shared position a_i occurs after b_i; omitting it changes the degree and breaks the identity. All original target opens W_(a_0),...,W_(a_(n-1)) remain in the target, even though the displayed input component no longer includes the original prefix a_0,...,a_(i-1).

### Regularity, including the original suffix

For the input tuple in a fixed summand, (2.2) supplies the regular numerator

    N=(∏_(j=0)^i D_(b_j))(∏_(j=i)^(n-1) D_(a_j))
                        f_(b_0,...,b_i,a_i,...,a_(n-1)).

Its full standard target is EXACTLY V_tag(a), because each b_j has the tag of a_j and the shared tag at i is simply repeated. Multiplying this summand of (5.1) by ∏_(j=0)^(n-1) D_(a_j) gives

    (∏_(j<i)D_(a_j))
    (∏_(j≤i)rho_(A(a_j),b_j)/D_(b_j)) N.              (5.2)

Every factor in (5.2) is regular on V_tag(a). Hence K maps S_D^n to S_D^(n-1), with the SAME uniform 16/10 clearance. In particular it gives a regular source cochain on W_a, since every retained original D_(a_j) is a unit there.

Inserted weights clear inserted owners only. On an enlarged STANDARD target with no original source localizations, the original suffix factors in N need not be units. We do NOT claim that the uncleared expression (5.1) extends there. Formula (5.2), and the retention of every original target open/tag, are essential. Equal labels do not merge occurrence factors; if b_i happens to equal a_i, its two input occurrences are still charged twice, one cleared by rho and one by the target D.

### Universal sign identity

The identity is local on each full target, so work over a commutative coefficient ring containing the restricted weights and their relations ∑_b rho_(A(a),b)=1. On the free ALL-ORDERED tuple chains define the vertex average

    p[a]=∑_(b:A(b)=A(a))rho_(A(a),b)[b]

and extend it separately to every tuple position. Its augmentation is 1 at each vertex. Define the chain prism on a degree-m tuple by

    h[a_0,...,a_m]
      =∑_(i=0)^m(-1)^i
        [p a_0,...,p a_i,a_i,...,a_m],                (5.3)

with multilinear expansion of each p a_j. Boundary deletion before the repeated seam cancels the matching term of h∂; deletion after the seam cancels the other h∂ terms. The two seam deletions in consecutive i summands cancel each other. The only surviving end faces are [a_0,...,a_m] and -[p a_0,...,p a_m], because deleting an averaged vertex sums its coefficient to 1. Thus

    ∂h+h∂=1-p.                                        (5.4)

For degree zero this is directly ∂∑rho[b,a]=[a]-∑rho[b], fixing the sign. Here p on the right means its tuplewise extension, not only its vertex action. This calculation does not require cochains to be alternating or tuples to be distinct.

Dual evaluation gives exactly (5.1), and tuplewise p is exactly BPi. Therefore

    dK+Kd=1-BPi.                                      (5.5)

The local formal calculation is valid on every target because all weights and source restrictions used there have already been proved regular or uniquely extended by (5.2). The equality hence holds as an identity on the bounded source complex, not merely in a common function field.

## 6. Composition with the ordinary contraction

The companion ordinary/tensor proof supplies H_O on the ALL-ORDERED complex O. Its passage through the alternating ordinary complex is explicit, rather than an assumption about the present source. In that proof let A_T:T→C_alt and B_T:C_alt→T be the regular tensor comparison, with B_T A_T=1 and dJ+Jd=1-A_T P_top B_T, where J=A_T H B_T+K_T. Let r:O→C_alt be restriction to increasing lists, e:C_alt→O its alternating extension, and t the supplied all-ordered normalization homotopy. It proves

    re=1,     dt+td=1-er,
    H_O=e J r+t,
    dH_O+H_Od=1-e A_T P_top B_T r.                     (6.1)

All maps preserve their actual regular intersection domains, including any mixed box vertices in that companion construction. The final right-hand projector vanishes in degrees other than four. In particular, for dPi(c)=0 in degree two,

    dH_O Pi(c)=Pi(c).

Together with (5.5),

    d[B H_O Pi(c)+Kc]
      =B Pi(c)+(c-B Pi(c))=c.                          (6.2)

Both terms are regular on the original source cover. Indeed B H_O Pi(c) belongs to S_D^1 by (4.3), and Kc belongs to S_D^1 by (5.2). Formula (6.2) therefore proves (0.3) on that same source complex; it does not stop at a common refinement or infer a source boundary from Pi alone.

Under the inverse character identification of section 2 let beta correspond to b. Then d beta equals the original function-valued tr(M)/2. Scalar inclusion gives d_row(beta I)=(d beta)I even though End(E) is nontrivial. Substituting (0.1) proves (0.4), with the MINUS sign before W. No compatible matrix-valued averaging map is needed for this source identity.

## 7. Witness status, limits, and controls

The bound and finite-cover arguments discharge two separate obligations: 54/29 supplies enough vanishing for the full central scalar and the uniform bounded complex, while the unit-ideal proof supplies actual polynomial partition witnesses. They do not assert a particular degree bound, canonical choice, prescribed solver output, or equality with previously frozen witnesses. A fixed choice produces a k-linear cochain comparison and a primitive operator; without expanding that choice it is an existence-backed explicit formula, not a numerical evaluated certificate.

Standard intersection coordinates invert exactly the required standard chart equations, and all chart tags have been retained. This comparison asserts no additional cutoff bound. No source, model, actual matrix or actual polynomial instance is evaluated. Dependency files are retained and hashed only.

The small checker uses invented tag labels, formal two-variable partition weights, integer tuple chains, and integer pole-vector metadata. It checks partition chain-map/retraction identities and (5.4), plus the full-M ledger and occurrence-wise clearance arithmetic. Negative controls reject wrong prism sign, omission of a prefix weight, nonunit-sum weights, merged occurrence charges, and claiming an uncleared suffix is regular on a standard target. The universal proof is above; finite controls do not establish the accepted geometric hypotheses or compute an actual cochain.

The companion ordinary comparison, including its all-ordered appendix and review status, is an explicit separately pinned dependency. Independent audit of this new source comparison is required before treating this packet as accepted.

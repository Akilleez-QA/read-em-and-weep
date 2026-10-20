# A regular comparison between ordinary and tensor Čech complexes

## Result, assumptions, and scope

Let k be a field, Y=(P1_k)^4, and U_v=U_(v_0)×...×U_(v_3) for v in {0,1}^4, where U_0=Spec k[x] and U_1=Spec k[t], t=x^(-1), in each factor. Order the sixteen vertices lexicographically, with 0<1. Let C be the ordinary ordered alternating Čech cochain complex of these sixteen opens. Let T be the total tensor product of the four two-open Čech complexes. Coefficients are initially any exterior tensor product of line bundles L=L_0 ⊠ ... ⊠ L_3; the comparison itself works intrinsically for any sheaf whose cubical section complex is used in place of a literal tensor product.

We construct finite, signed, regular-domain-preserving cochain maps and a homotopy

    A:T -> C,       B:C -> T,       K*:C^n -> C^(n-1),
    BA=1,          dK*+K*d=1-AB.                         (0.1)

For L=O(-2,-2,-2,-2), we also specify the Laurent tensor contraction H and obtain

    J=A H B+K*,       dJ+Jd=1-A P_top B,                 (0.2)

where P_top is supported only in degree four. Hence every closed regular ordinary degree-two cochain c has the explicit regular ordinary primitive

    b=A H B(c)+K*(c),             db=c.                 (0.3)

In chain notation A=AW*, B=Sh*, so (0.3) is AW* H Sh*(c)+K*(c). The two different ordinary and tensor complexes are never identified termwise.

This supplies precisely the ordinary-sixteen-open/tensor comparison omitted in section 5 of ../central-scalar-contraction-20261018/PROOF.md. It does not supply a comparison from a different source/owner cover to these standard opens. No actual source cochain, physical matrix, model, polynomial instance, detector or guard is evaluated or changed. The formal tests use invented cube vertices, integer chains, and small Laurent monomials only.

## 1. The two incidence chain complexes

Write S_n for the free k-module on increasing (n+1)-tuples of distinct cube vertices. The symbol [w_0,...,w_n] for an arbitrary list means its alternating normalization into increasing order; it is zero when a vertex repeats. The boundary is

    ∂[v_0,...,v_n]=sum_(j=0)^n (-1)^j [v_0,...,omit v_j,...,v_n],

with the unaugmented convention ∂S_0=0. Thus S is the simplicial chain complex of the full simplex on sixteen vertices, not merely a chosen triangulation of the cube.

For each coordinate i let I_i have vertices [0],[1] in degree zero and e_i=[0,1] in degree one, with ∂e_i=[1]-[0]. Write [1,0]=-e_i and [a,a]=0. Put Q=I_0⊗...⊗I_3, with

    ∂(q_0⊗...⊗q_3)
      =sum_i (-1)^(sum_(j<i)|q_j|)
          q_0⊗...⊗∂q_i⊗...⊗q_3.                       (1.1)

A basis q of Q is a cubical cell: each coordinate is a fixed vertex or an active oriented interval e_i. Its dimension is the number of active coordinates. Denote its vertex box by Box(q), and put

    V_q = product_i U_(q_i),
    U_([0])=U_0, U_([1])=U_1, U_(e_i)=U_0∩U_1.         (1.2)

For a simplex σ, let Box(σ) be the Cartesian product of its coordinate-value sets. Thus a coordinate is fixed if all vertices of σ agree there, and is free otherwise. Let U_σ be the intersection of its vertex opens. Then

    U_σ = product_i intersection_(a occurs in coordinate i of σ) U_a.
                                                                    (1.3)

In particular, if every vertex of a simplex τ lies in Box(σ), then

    U_σ ⊆ U_τ.                                          (1.4)

If every vertex of a cubical cell q lies in Box(σ), similarly U_σ⊆V_q. These are inclusions of actual regular domains, not just relations of rational functions.

## 2. The explicit shuffle chain map Sh:Q -> S

For a cell q of dimension n, order its active coordinates as i_1<...<i_n. For a permutation π=(π_1,...,π_n) of these coordinates, begin at the coordinatewise minimum w_0 of Box(q), and change coordinate π_r from 0 to 1 to obtain w_r. Define

    Sh(q)=sum_π sgn(π) [w_0,w_1,...,w_n].               (2.1)

Here sgn(π) is relative to the ordered active list. For n=0 this is the corresponding single vertex. Every staircase list is increasing in the fixed lexicographic order. Every staircase has exactly the same coordinate-value sets as q, so its intersection equals V_q.

### Chain-map proof

Delete an interior vertex w_r, 0<r<n, in a staircase. The resulting face is also obtained from the staircase with the adjacent steps π_r and π_(r+1) exchanged. The deletion position and hence boundary sign are the same, while the permutation sign changes. All such interior faces cancel.

If the first step is i_s, deletion of w_0 leaves the upper face in coordinate i_s. Moving i_s to the first place contributes (-1)^(s-1), exactly the coefficient of that upper face in (1.1). If the last step is i_s, deletion of w_n leaves the lower face. Its coefficient is (-1)^n(-1)^(n-s)=(-1)^s, exactly the negative of (-1)^(s-1). The remaining permutation signs are precisely the lower-dimensional shuffle signs. Consequently

    ∂Sh=Sh∂.                                            (2.2)

## 3. The explicit Alexander–Whitney chain map AW:S -> Q

For an INCREASING simplex σ=[v_0,...,v_n], sum over (n_0,n_1,n_2,n_3)∈{0,1}^4 with sum n_i=n. Put r_i=sum_(j<i)n_j and define

    AW(σ)=sum_(n_0+...+n_3=n)
       [v_(r_0)^0,...,v_(r_0+n_0)^0] ⊗ ... ⊗
       [v_(r_3)^3,...,v_(r_3+n_3)^3].                   (3.1)

A length-zero segment is its coordinate vertex. A length-one segment is e_i, -e_i, or zero according as its endpoints are (0,1), (1,0), or equal. There are no extra signs in the cut sum; the reversed coordinate intervals contribute their own signs. For n>4 the sum is empty.

IMPORTANT: for a non-increasing input list, first normalize the WHOLE simplex alternatingly, then apply (3.1). Do not reapply the cut formula directly to the unsorted list. That latter operation is generally not alternating. Repeated original vertices give zero before the cut formula is used.

### Chain-map proof without assuming a comparison theorem

On S define the two-fold front/back diagonal

    Δ_2[v_0,...,v_n]=sum_(r=0)^n
                      [v_0,...,v_r]⊗[v_r,...,v_n].     (3.2)

Expand the tensor boundary. Deletions away from the shared cut vertex are exactly the terms of Δ_2∂. The remaining seam terms cancel between consecutive cuts: the front-factor last-face contribution at r and the back-factor first-face contribution at r-1 have opposite tensor-boundary signs and equal factors. Degree-zero factors have zero boundary, so there are no extra endpoint terms. Therefore ∂Δ_2=Δ_2∂. Iterating this identity gives the four-fold diagonal whose summands are the four consecutive segments of all weak cuts 0≤t_1≤t_2≤t_3≤n.

For each coordinate i define p_i:S->I_i by p_i[v]=[v^i], p_i[v,w]=[v^i,w^i], and p_i=0 in degrees ≥2. In degree one its boundary formula is immediate. In degree two,

    [v_1^i,v_2^i]-[v_0^i,v_2^i]+[v_0^i,v_1^i]=0,

because each oriented interval has coefficient equal to the difference of its endpoints, viewed as 0/1 integers. Higher boundaries are also killed. Hence p_i is a chain map. Applying p_0⊗...⊗p_3 to the four-fold diagonal kills precisely the segments of length ≥2 and gives (3.1). Thus

    ∂AW=AW∂.                                            (3.3)

All coordinates of each resulting cell come from coordinate values of σ. Therefore Box(q)⊆Box(σ) for every nonzero term q of AW(σ).

### Retraction identity

Apply AW to a staircase in Sh(q). Its n successive edges each change exactly one coordinate. A nonzero cut term of total degree n must use every edge, and must assign each edge to the coordinate it changes. Since the factors are visited in the fixed order 0,1,2,3, this is possible only for the staircase that visits active coordinates in increasing order. That staircase has positive shuffle sign, exactly one surviving cut term, and image q. Thus

    AW Sh=1_Q.                                          (3.4)

## 4. A finite box-supported homotopy K:S_n -> S_(n+1)

Set D=1_S-Sh AW; it is a chain map and D_0=0. For a fixed cube vertex b, define the normalized cone

    cone_b[w_0,...,w_n]=[b,w_0,...,w_n],                 (4.1)

with the alternating/repetition convention of section 1. Direct expansion gives

    ∂cone_b z+cone_b∂z=z                 in degree ≥1.  (4.2)

In degree zero the right side is z-ε(z)[b], where ε is the coefficient sum. We will apply the degree-zero formula only to the zero chain.

Set K_(-1)=0. Recursively, for each increasing n-simplex σ, let b(σ) be the coordinatewise minimum vertex of Box(σ), and set

    z_σ=Dσ-K_(n-1)(∂σ),
    K_n(σ)=cone_(b(σ)) z_σ.                             (4.3)

Extend K linearly from increasing simplices. At n=0, z_σ=Dσ=0 and K_0=0. For n≥1, suppose the homotopy identity is known one degree lower. Then

    ∂z_σ=D∂σ-∂K_(n-1)∂σ
          =D∂σ-(D-K_(n-2)∂)∂σ=0.                     (4.4)

Equation (4.2) gives ∂K_nσ=z_σ and therefore

    ∂K+K∂=D=1-Sh AW.                                   (4.5)

This is a literal recursive finite formula, not an appeal to the existence of an acyclic-carrier homotopy. Recursion terminates by decreasing simplex degree. S_n=0 for n>15, so no unbounded chain group appears.

### Support and the correct meaning of a mixed vertex

Each term of Dσ has vertices inside Box(σ): this is immediate for σ and follows from sections 2–3 for Sh AWσ. Every face has a box contained in Box(σ), so the inductive terms K∂σ stay in that box. The added cone vertex b(σ) also lies there. Hence every simplex τ appearing in Kσ satisfies

    Vertices(τ)⊆Box(σ),          U_σ⊆U_τ.               (4.6)

A mixed vertex need not be an original vertex of σ. The coordinatewise box inclusion, rather than membership in the original vertex set, is the fact that authorizes restriction of regular sections.

## 5. Dualization with regular sections and line transitions

Ordinary cochains are

    C^n=product_(σ increasing n-simplex) Γ(U_σ,L),

with δ given by the signed restrictions along faces. Let

    T^n=direct-sum_(q a degree-n cell) Γ(V_q,L),

with the differential dual to (1.1), again using restrictions. The finite direct sums/products are interchangeable. For an exterior tensor line bundle, sections on these affine product opens identify canonically with the tensor products of the one-factor section spaces. This is the usual total tensor Čech complex, including its Koszul signs.

For a chain map F that sends a generator a to sum_b m_b b, with its source domain contained in every target domain, define its transpose on sections by

    (F* f)_a=sum_b m_b (f_b restricted to the domain of a).   (5.1)

No evaluation or extension of a section to a larger domain occurs.

For Sh, all target simplex domains equal V_q. For AW, U_σ⊆V_q. For K, U_σ⊆U_τ. Thus all three transposes in (5.1) are defined on the entire indicated REGULAR section spaces. All composites of restrictions agree by functoriality. Transposing the proved incidence identities gives

    A=AW*:T->C,          B=Sh*:C->T,
    BA=1_T,              δK*+K*δ=1_C-AB.                (5.2)

For example, (K*c)_σ is obtained by evaluating c on the (n+1)-simplices occurring in Kσ and restricting each result to U_σ. The star on K includes this degree reversal; it is not a sign change. There is no extra Hom-complex sign in (5.2), because the Čech differential is defined as evaluation on the incidence boundary.

### Frames for O(-2)^4

On factor i use frames e_(i,0) and e_(i,1) with

    e_(i,1)=x_i^(-2)e_(i,0).

For a product vertex v use e_v=⊗_i e_(i,v_i). A component may be stored in the frame of its first vertex; a cubical component may be stored in the frame of its coordinatewise minimum. If a section is f_w e_w and is needed in frame e_v, its coefficient becomes

    f_v = product_i x_i^(-2(w_i-v_i)) f_w.              (5.3)

Whenever w_i≠v_i in the comparison formulas, both values 0 and 1 occur in coordinate i of the original input box. Its domain therefore has x_i invertible. Every frame ratio in (5.3) is a unit there. Thus coefficient conversion preserves regularity even if its expression in the single rational reference frame contains negative exponents. The same argument applies to any exterior tensor line bundle with its actual transition units. Intrinsic restrictions in (5.1) are the primary definition; omitting these frame ratios is not permitted.

## 6. The explicit tensor contraction and ordinary primitive

For each O(-2) factor, write its two-open cochains in their local frames as

    E^0=k[x]⊕k[t],       E^1=k[x,x^(-1)],
    d(a,b)=x^(-2)b(x^(-1))-a(x).

For f=sum_m a_m x^m set

    h(f)=(-sum_(m≥0) a_m x^m,
            sum_(m≤-2) a_m t^(-m-2)),
    P(f)=a_(-1)x^(-1),

and set h=P=0 on degree zero. These are finite Laurent sums of regular sections on their specified domains. Splitting exponents into m≥0, m=-1, and m≤-2 proves

    dh+hd=1-P,          dP=Pd=0.                        (6.1)

On T=E_0⊗...⊗E_3 define the graded operator

    H=h⊗1⊗1⊗1 + P⊗h⊗1⊗1
                  + P⊗P⊗h⊗1 + P⊗P⊗P⊗h.              (6.2)

On a homogeneous tensor, the i-th h term has sign (-1)^(sum_(j<i)|a_j|). Terms from other differential factors cancel in dH+Hd, and (6.1) telescopes to

    dH+Hd=1-P_top,          P_top=P⊗P⊗P⊗P.              (6.3)

Since P is supported only in degree one, P_top is supported only in total degree four. Using (5.2),

    δ(AHB+K*)+(AHB+K*)δ
       =A(1-P_top)B+(1-AB)=1-A P_top B.                 (6.4)

It follows that for every δ-closed c∈C^2,

    b=AHB(c)+K*(c)∈C^1,               δb=c.             (6.5)

Every operation is finite and defined on the full regular domain. In particular, K*c on an edge uses only c on triangles inside that edge's coordinate box; Bc uses the signed triangular staircases of the tensor two-cells; H performs the prescribed regular Laurent splittings; and A evaluates the cut sums on edges with restrictions and frame conversion.

The plus sign before K*c follows from ∂K+K∂=1-Sh AW. Reversing that homotopy convention would require reversing this sign. The degree-four harmonic cochain is not declared exact. Indeed BA=1 and (6.3) show that A P_top B is an actual degree-four projector. The assertion δJ(c)=c is also restricted to closed inputs; for a nonclosed input, the term Jδ(c) in (6.4) is essential.

## 7. Consequence and the remaining source-cover dependency

If the extracted scalar central cocycle has already been supplied as a regular cochain c on this ordinary sixteen-open cover, (6.5) is an unconditional explicit primitive there. If compatible ordinary End-valued data satisfy M-R=c I-δW, then

    M-R=δ(b I-W).                                       (7.1)

This is conditional only on that input identity and scalar inclusion; the comparison does not assume End is a trivial bundle.

For a DIFFERENT source complex S_src, an admitted degree-preserving cochain map F:S_src->C first gives the ordinary primitive JF(c) of F(c). The tensor comparison is now explicitly B F; no additional ordinary/tensor comparison remains missing. This alone does not give a source primitive. Such a primitive additionally needs a regular degree-preserving cochain map G:C->S_src (so dG=Gδ) and a regular degree-minus-one operator η with

    dη+ηd=1-GF,

in which case GJF(c)+η(c) is a source primitive. A corresponding common-refinement homotopy gives the weaker primitive on that refinement. Compatibility with scalar inclusion, and any End-valued transport, remains a separate source-comparison requirement.

Therefore the next unresolved dependency is a constructive regular-domain-preserving comparison from the actual source/owner cover, with the reverse/homotopy or common-refinement data appropriate to the claimed destination. Nothing here removes possible carrier denominators outside their original domains, evaluates the actual c, proves a noncentral obstruction vanishes, or establishes a higher-order physical lift.

## 8. Verification strength

The executable check_controls.py is standard-library-only and reads no input files. It checks the chain-map identities, AW Sh=1, alternating normalization, and box support on all cubical cells and on a bounded collection of invented simplices (exhaustively in two dimensions, plus selected four-dimensional inputs). It checks the recursive homotopy and small regular Laurent-cochain controls with all line-frame transitions. Negative controls distinguish an unsorted cut formula from alternating extension, reject a wrong shuffle sign and the opposite homotopy sign, detect omission of either primitive summand or the Jδ term on a nonclosed input, and exhibit why an outside-box section cannot be restricted to an original domain. Appendix A is also checked on ordered tuples with repeats, including a nonzero repeated-index cochain component.

The universal proofs are sections 2–6. Finite tests only verify the executable conventions and expose selected wrong alternatives; they do not replace those proofs or establish any property of actual source data.

## Appendix A. Explicit extension to all ordered tuples, including repeats

If a source comparison naturally lands in the unsymmetrized Čech complex, the alternating convention is not silently imposed. Let E_n be free on ALL (n+1)-tuples of cube vertices, including repeats, with the usual deletion boundary and ∂E_0=0. Its section-valued dual C_all is the ordinary all-ordered-tuple Čech complex; repeated-index components are retained.

Define p:E->S by alternating normalization (sorting sign, zero when a vertex repeats), and j:S->E by the inclusion of increasing lists. Both are chain maps and pj=1. For p, when an input contains no repeats this follows by comparing the deletion signs before and after sorting. If there is a repeated vertex, faces still contain repeats and vanish except possibly the two faces that delete its two occurrences; those two normalized faces cancel with their deletion and sorting signs. For j, every face of an increasing list is increasing.

The all-tuple cone c_b[w_0,...,w_n]=[b,w_0,...,w_n] now retains order and repeats, rather than normalizing. The same direct boundary identity holds. Put L_(-1)=0 and recursively

    L_n(σ)=c_(min Vertices(σ))((1-jp)σ-L_(n-1)∂σ).     (A.1)

Since (1-jp)_0=0, the degree-zero augmentation issue again disappears. Exactly the cycle argument (4.4) proves

    ∂L+L∂=1-jp.                                        (A.2)

Here the minimum is the lexicographically first ORIGINAL vertex, rather than the coordinatewise box minimum used in section 4. Inductively every output vertex is an original vertex of σ, including on repeated inputs. This gives even stronger support than box containment. Although E has terms in arbitrarily high degrees, each specified input has finite length and the recursion terminates; no infinite sum or limit is used.

Dualizing with the same regular restrictions gives

    p*:C->C_all,       j*:C_all->C,       j*p*=1,
    dL*+L*d=1-p*j*.                                    (A.3)

Here j* restricts a cochain to increasing tuples. Conversely p* is its alternating extension, with zero on repeated tuples. For the J of (0.2), set

    J_all=p* J j*+L*.

Then

    dJ_all+J_all d=1-p* A P_top B j*.                   (A.4)

Thus a closed regular degree-two cochain c in the unsymmetrized all-tuple complex has the explicit primitive J_all(c). This includes potentially nonzero repeated-index components through L*c; they are not discarded. The projection on the right of (A.4) still lives only in degree four. This appendix changes no source-cover requirement: it only supplies the convention bridge on the same sixteen standard product opens.

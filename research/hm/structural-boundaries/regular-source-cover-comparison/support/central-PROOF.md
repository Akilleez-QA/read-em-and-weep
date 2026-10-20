# Explicit central-scalar removal after a full cochain comparison

## Result and exact scope

Let M be the ACTUAL closed, left-normalized, ten-term mixed defect of the frozen raw route, using the first lifts U_r=g(s_raw,r I+k_r), rather than the scalar-free baseline M0. Put c=tr(M)/2 and W=s_raw,q k_p+s_raw,p k_q. The source-bound closure theorem gives

    d_row M=0,       R=tf(M)+d_row W=M-c I+d_row W.       (0.1)

Specifically, closure-PROOF sections 7-8 establish the unprojected associativity identity -g_il d_row M+A=0 and then show A=0 termwise by complementary gerbe support. Thus full-M closure precedes trace projection; it is not inferred from closure of R.

We first prove directly that all ten terms of this full M have full deck character. Consequently c is a regular scalar degree-two cocycle on the actual source cover, in the full-sign summand of O_X. Its branch-safe pushforward line on Y=(P1)^4 is L=O(-2,-2,-2,-2).

We give a fixed explicit degree-minus-one operator H on the standard TENSOR Cech complex T for L, with

    dH+Hd=1-P_top.                                      (0.2)

P_top is supported only in degree four. Thus, for any admitted degree-preserving scalar cochain map Pi from the entire relevant source complex to T,

    c_std=Pi(c),     b_std=H c_std,     d b_std=c_std.    (0.3)

This is an explicit finite Laurent-splitting operator formula, not evaluation of the actual c or its coefficients. If an accompanying End-valued comparison is a cochain map and respects scalar inclusion, then

    Pi_End(M)-Pi_End(R)
       =d[(H Pi(c)) I-Pi_End(W)].                      (0.4)

The sign before W is minus. Formula (0.4) is the explicit compared scalar-removal primitive; it is conditional on that FULL comparison, not supplied by a finite detector or a scalar selector on one lifted component.

No original-source-cover primitive is asserted from Pi alone. Sections 6-7 state exactly the additional homotopy data that produce one, or a primitive on a common refinement. No source/model/polynomial/actual-matrix evaluation, physical computation, detector value, obstruction vanishing, higher-order lift or guard change occurs.

## 1. Prior result and narrow novelty

The prior direct-scalar-free pairing proof, retained as inputs/prior-scalar-removal.md, already proves in section 5 that the central part of an actual closed full-sign M is exact in sheaf cohomology: H^2(Y,L)=0. It also already proves R=tf(M)+dW. Neither cohomology vanishing nor that class-equivalence identity is new here. Its section 6 describes a first-order scalar solver and its transpose; that is a different input cochain, degree and pair-character task.

The prior named-term restoration proof, inputs/prior-named-restoration.md, proves the cancellation 1+19-20=0 on a specified repeated-carrier quadruple and its S4 orbit. It explicitly does not supply an edge primitive, full-cover exactness or scalar-class removal. The older map-and-comparison note, inputs/prior-selector-comparison.md, concerns a degree-minus-two End selector and an O(-4)^4 scalar in Cech degree four, together with comparison of two lifts. It is not an explicit scalar contraction for tr(M)/2 in degree two and does not certify the full comparison required in (0.3)-(0.4).

The addition here is a fully signed constructive operator for this particular central scalar, a full-M character ledger using the actual first lifts, the compared primitive (0.4), and explicit formulas delineating source/refinement transport. The elementary one-factor and tensor contractions are standard algebra; no claim of novel abstract homological algebra is made. The two historical notes fetched for scope checking were read at commit 08b73637d4136f91606aad332c46cafd064417f8, at paths research/hm/current-scalar-proof/map-and-comparison.md and research/hm/current-scalar-residual-attribution/closure-and-characters.md. The newer frozen source identities are inherited only through the separately accepted local proofs in dependencies/.

## 2. Full M character, including all first-lift terms

Use p=(0,1), q=(2,3), with character masks p=3, q=12 and p XOR q=15. Let m_i be the legal mask of owner i and w_ij=m_i XOR m_j. The accepted character proof supplies the actual physical frames, their all-chart interpretation, and

    char(g_ij)=char(g_ij^-1)=w_ij,
    char(s_raw,r)=char(k_r)=char(b_r)=r,
    char(V_d f)=char(f) XOR e_d.

Inverse here is the actual inverse, justified by the source-bound determinant/closure theorem; the frozen entrywise adjugate has this same character. Scalar multiplication, ordered matrix composition and differentiation are in the fixed physical owner frames. In particular

    char(x_r)=r for x_r=s_raw,r I+k_r,
    char(U_r,ij)=w_ij XOR r for U_r,ij=g_ij x_r,ij.    (2.1)

This is the full first lift; replacing U by g k without retaining the scalar would not establish the present assertion. Each mu_r adds r to its two input characters; every mu_pq summand adds 15, since its four derivative directions occur once each. Put A=g_ij, B=g_jk, G=g_ik. The full ten unnormalized slots are

1. U_p,jk U_q,ij
2. U_q,jk U_p,ij
3. mu_p(U_q,jk,A)
4. mu_q(U_p,jk,A)
5. mu_p(B,U_q,ij)
6. mu_q(B,U_p,ij)
7. mu_pq(B,A)
8. -b_p U_q,ik
9. -b_q U_p,ik
10. -b_p b_q G.

Slots 1-7 have character w_jk XOR w_ij XOR 15=w_ik XOR 15. Slots 8-10 have character w_ik XOR p XOR q=w_ik XOR 15. Left multiplication of each by G^-1 yields 15. All ten terms therefore have the same character before any cancellation or trace projection. The derivative of the scalar part of U in slots 3-6 is included by the derivative character rule applied to the WHOLE U, not omitted.

The accepted all-chart interpretation of g, s_raw, k and the invariant V's shows these are the same meromorphic matrix cochains under a standard representation-chart change, while their physical owner frame stays fixed. The source-bound closure proof strengthens this to regularity on the actual common intersections for U, D and M. The physical cohomology frame has a common deck sign on both columns; conjugation cancels it. Hence full matrix character is the intrinsic End character of M, not an assertion that End(E) is a trivial bundle. Trace eliminates the owner-frame conjugation altogether. Thus c=tr(M)/2 is a genuine full-character regular scalar source cochain. Characteristic zero supplies 1/2.

Taking trace of d_row M=0 gives dc=0, since trace commutes with conjugation and the alternating face maps. This uses closure of the whole M, not closure of M0 or of individual central terms.

## 3. Scalar coefficient line and the actual input domain

On a standard base chart A, write its finite-flat curve algebra as

    S_A=R_A[z_0,z_1,z_2,z_3]/(z_d^2-f_d)
       =direct sum_(S subset {0,1,2,3}) R_A z_S,

with z_d=y_d on a finite factor and z_d=u_d=t_d^2 y_d at infinity. The full-character coefficient is obtained by the R_A-linear projection onto z_0 z_1 z_2 z_3. No division by a potentially vanishing branch coordinate is required. The source owner opens are deck-stable; restrictions and invariant localizations commute with this direct-summand projection.

If c_A=z_all,A a_A and tau_A is the product of the inverted coordinates, then z_all,A=tau_A^2 z_all,ref. Equality of the scalar c gives

    a_A=tau_A^-2 a_ref.

This is exactly the coefficient transition for L=O_Y(-2,-2,-2,-2), with the finite-chart trivialization convention used below. Thus c determines an L-valued source cochain after finite-flat character extraction. Denote this extracted scalar cochain again by c. Every subsequent scalar comparison must include this identification and its transition law.

The source c can have carrier/legal denominators outside its own owner intersections. It is not automatically an element of the standard Laurent tensor complex. The operator H below acts on regular sections on the standard tensor intersections, not arbitrary rational functions with extra interior poles. A full admitted source-to-standard cochain map must land there. Pole clearing, character purity, an abstract quasi-isomorphism, or a finite-coordinate projection alone is not this constructive input.

## 4. One-factor contraction with fixed signs

Let k be the characteristic-zero base field. For O_P1(-2), using U_0=Spec k[x], U_infty=Spec k[t] with t=x^-1, define

    C^0=k[x] direct-sum k[t],     C^1=k[x,x^-1],
    d(a,b)=x^-2 b(x^-1)-a(x),

and C^n=0 otherwise. If f=sum_n c_n x^n is a finite Laurent polynomial, put

    h(f)=(-sum_(n>=0) c_n x^n,
           sum_(n<=-2) c_n t^(-n-2)),
    P(f)=c_-1 x^-1.

Set h=0 on C^0 and P=0 on C^0. All sums are finite. Direct substitution gives

    d h(f)=f-P(f),           h d(a,b)=(a,b).

The first identity separates exponents >=0, <=-2 and -1. For the second, -a has only nonnegative x exponents and x^-2 b(x^-1) only exponents <=-2, so h recovers the two components separately. Hence

    dh+hd=1-P,     dP=Pd=0,
    P^2=P,         h^2=hP=Ph=0.                       (4.1)

In particular the harmonic x^-1 class is retained, not falsely declared a boundary. There is no degree-zero harmonic term.

## 5. Four-factor operator and proof

Let T=Tot(C_0 tensor C_1 tensor C_2 tensor C_3), the standard TENSOR Cech complex for L. For a homogeneous simple tensor a=a_0 tensor ... tensor a_3, set |a_j| in {0,1} and

    d(a)=sum_i (-1)^(sum_(j<i)|a_j|)
       a_0 tensor ... tensor d a_i tensor ... tensor a_3.

All tensor products of operators are graded. Define

    H=h tensor 1 tensor 1 tensor 1
      +P tensor h tensor 1 tensor 1
      +P tensor P tensor h tensor 1
      +P tensor P tensor P tensor h.                (5.1)

In the i-th term the sign on a is (-1)^(sum_(j<i)|a_j|), because h has degree -1. P has degree zero even though its nonzero image is in degree one. Equivalently, first apply P to the preceding factors, h to factor i, identity to the remaining factors, and multiply by that Koszul sign. This description is an explicit implementation prescription; no unseen sign convention is used.

Write H_i for the i-th summand. The graded Leibniz rule, Pd=dP and the factorwise degrees give

    d H_i+H_i d=P^(tensor i) tensor (dh+hd)
                                      tensor 1^(tensor(3-i)).

Terms with d acting on another factor cancel in pairs because both d and h are odd. Substituting (4.1) and telescoping yields

    dH+Hd=sum_i P^(tensor i) tensor (1-P)
                                      tensor 1^(tensor(3-i))
           =1-P^(tensor 4).                         (5.2)

Let P_top=P^(tensor 4). It vanishes in total degrees 0,1,2,3, and its degree-four image is spanned by x_0^-1 tensor x_1^-1 tensor x_2^-1 tensor x_3^-1. Thus for every closed degree-two c_std in T,

    d(H c_std)=c_std.                               (5.3)

This formula itself proves the degree-two vanishing; it does not invoke that vanishing as a black box. It does not say dH is the identity on nonclosed degree-two inputs: the term Hd remains essential. H also obeys H^2=0, P_top H=H P_top=0 by (4.1), though these side conditions are unnecessary for (5.3).

The ordinary ordered Cech complex of the sixteen product opens and this tensor Cech complex have different cochain groups. They are not identified literally. If a source comparison lands in the former, a specified cochain comparison from it to T is part of Pi; any required reverse map and homotopy must also be retained. One may use standard cubical/simplicial comparison data if supplied, but none is constructed or silently assumed by the elementary coefficient formula (5.1).

## 6. Compared central removal and the source-cover boundary

Let S be the scalar source complex after the character/line identification of section 3. Suppose Pi:S->T is a degree-preserving cochain map on a domain containing c and its differential, not merely a function on a selected degree-two coordinate array. Then d Pi(c)=Pi(dc)=0, and (5.3) gives (0.3).

For (0.4), additionally require an End-valued target complex V, scalar inclusion j_T:T->V, and cochain map Pi_End from the source row-End complex to V, satisfying

    Pi_End(f I)=j_T Pi(f).

It must be defined on M,R,W and the required differentials. Naturality for trace, if a trace map V->T is used to compute c_std, is the separate equality tr Pi_End=Pi tr; otherwise c_std is obtained directly by scalar Pi. Apply Pi_End to M-R=c I-dW to get

    Pi_End(M-R)=j_T Pi(c)-d Pi_End(W)
              =d(j_T H Pi(c)-Pi_End(W)).            (6.1)

The concise I notation in (0.4) means j_T, not an assumed trivialization of End(E). If both comparison maps induce the intended cohomology identifications, (6.1) recovers the already known equality of the full M and R classes with a specified compared primitive. A cochain map alone proves the boundary identity only in its target. It need not reflect exactness: the zero cochain map is a counterexample to any such inference.

For an explicit original-source primitive, suppose given cochain maps A:S->T and B:T->S and a degree-minus-one operator K:S->S with

    dK+Kd=1-BA.                                    (6.2)

For dc=0, the explicit formula

    b_source=B H A(c)+K(c)                          (6.3)

has db_source=BA(c)+(1-BA)c=c. If all these maps preserve the regular source-cochain domain, (6.3) is a regular source primitive. Then

    M-R=d_row[b_source I-W].                        (6.4)

The plus sign in front of K follows from the convention (6.2); reversing the homotopy convention reverses that sign. Merely knowing A is a quasi-isomorphism gives a cohomological existence statement, not the explicit source operator (6.3). Neither B nor K is supplied by this packet.

## 7. Common-refinement variant

Alternatively let Q be a common-refinement scalar complex with cochain maps rho:S->Q and r:T->Q, and suppose a supplied degree-minus-one eta satisfies

    d eta+eta d=rho-r Pi.                           (7.1)

Then

    b_Q=r H Pi(c)+eta(c),       db_Q=rho(c).         (7.2)

With compatible End refinement maps, rho(M)-rho(R)=d[b_Q I-rho(W)]. This is an explicit primitive on Q. It does not descend to the original source cover without further transport. Regularity and admitted domains for r,rho,eta are part of (7.1), not consequences of the formal equation alone.

## 8. Verification strength and remaining dependency

The checker uses only invented formal monomial basis states for the one-factor complexes and their fourfold tensor product, plus integer character masks. It checks (5.2), differential square zero, and H square zero on a finite selected basis in every degree, and constructs invented closed degree-two controls as boundaries. It checks the full ten-slot mask ledger for every legal-mask triple. Negative controls reject omitted Koszul signs, omitted prefix projections, the wrong finite-part sign in h, the missing normalization character, and an invalid extension of dH=1 to nonclosed inputs or to the top harmonic class. No actual source is imported, parsed or evaluated by this checker; dependency proofs are only hashed.

The exact universal identities are proved in sections 2-7; finite checks are convention controls, not substitutes for those proofs. The current unresolved constructive dependency is an admitted full source-to-standard scalar comparison with its regular domain, and compatible End comparison if (6.1) is required. An original-source primitive additionally needs the reverse/homotopy data (6.2), or an explicit common-refinement homotopy for the weaker result (7.2). This packet does not prove R exact, since only the central part of M is removed.

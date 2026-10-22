# Rational pole strata and the common-direction dichotomy

## Dependencies and scope

This argument uses the exact obstruction identity in [PR747 at 0a0ee30a5142477e54245b7c6f22d561abb4f5f1](https://github.com/Akilleez-QA/read-em-and-weep/blob/0a0ee30a5142477e54245b7c6f22d561abb4f5f1/research/hm/source-family-fourth-square-exclusion/PROOF.md), pencil rigidity in [PR752 at e0d0cb31fbef5c7d6f1148e2278fbce115239dcf](https://github.com/Akilleez-QA/read-em-and-weep/blob/e0d0cb31fbef5c7d6f1148e2278fbce115239dcf/research/hm/exceptional-direction-bounds/PROOF.md), and the projected Veronese parametrization in [PR759 at 8688c748e3a655a6db793c4b96504aaafb55cbc9](https://github.com/Akilleez-QA/read-em-and-weep/blob/8688c748e3a655a6db793c4b96504aaafb55cbc9/research/hm/exceptional-source-locus/PROOF.md).

Work over C. Put L=P1, k=C(L), A=H0(L,O(2)), and let B be its nondegenerate apolar symmetric form. The five-dimensional source space H is identified, by h↦S_h, with all trace-free B-self-adjoint endomorphisms of A. Fix a k-vector space V, a nonzero d∈V, a nonzero scalar γ∈C, and a C-linear map K:H→V. In one common rational trivialization of O(2), define

Φ_h(a)=aK_h−γS_h(a)d,   E_h=ker_C Φ_h.

For the imported HM identity, the actual modular class is a²Φ_h(a). Thus E_h records only its necessary vanishing gate. This does not identify the actual K, assert fourth-square sufficiency, resolve the separate β4 boundary, or prove algebraicity. All arguments below are structural and use indeterminate coordinates, not selected actual sources or coefficient evaluations.

## 1. A finite pole-stratified description

Let H0={h∈H:K_h∈kd}. This is a C-linear subspace. On H0 define the unique C-linear map r:H0→k by K_h=γr_h d. If h∉H0 then E_h=0. If h∈H0, then

E_h={a∈A:S_h(a)=r_h a}.

The finite-dimensional function space r(H0) has a maximal pole divisor D: at each point take the largest pole order among a finite basis. This is independent of that basis. A general h∈H0 realizes exactly D, since cancellation of the leading polar coefficient at each point is a proper linear condition. Set D=0 when r(H0)=0.

For each effective subdivisor F≤D with deg F≤2, define

H_F={h∈H0: div_infinity(r_h)≤F},
A_F=H0(L,O(2)(−F)),
M_F(h):A_F→A,   a↦S_h(a)−r_h a.

The principal-part conditions defining H_F are linear. Multiplication by r_h takes A_F to A, so M_F is a matrix of linear forms on H_F, of size 3 by (3−deg F). Let Y_F⊂P(H_F) be its rank-drop locus, defined by its maximal minors. Then the exceptional-source set is exactly

Y={ [h]∈P(H): E_h≠0 } = union_{F≤D, deg F≤2} Y_F.       (1)

Indeed any nonzero solution a has div_infinity(r_h)≤div(a), hence pole degree at most two. Taking F to be that pole divisor puts a in A_F and h in Y_F. Conversely a nonzero kernel vector of M_F gives an element of E_h. The union is finite. Consequently Y is closed. On its linear ambient subspaces it is described by cubic determinants for F=0, quadratic minors for deg F=1, and linear equations for deg F=2.

For exact pole divisor F of degree two the only possible direction is the fixed [a_F] with div(a_F)=F, and compatibility is linear in h. For exact pole degree one, PR752 implies dim E_h≤1 because r_h is nonconstant. The degree-zero stratum is precisely the ordinary eigenvalue problem S_h(a)=r_h a; only here is r_h necessarily a constant scalar.

## 2. Dense exceptions force a common direction

**Theorem.** Exactly one of the following holds:

1. Y is a proper closed subset of P(H), so a general nonzero source h has E_h=0.
2. There is a unique [a0]∈P(A) such that, for every h∈H,

   K_h=γ(S_h(a0)/a0)d.                              (2)

   In this case a0∈E_h for every h, hence Y=P(H).

The alternatives concern the unevaluated map K. They do not select which alternative holds for an actual source instance.

**Proof.** If Y is dense, H0=H. Let D be as above. Generic r_h has pole divisor D, so deg D≤2 by (1). If deg D=2, every exceptional generic h has the same direction a0 with div(a0)=D. The linear relation S_h(a0)=r_h a0 holds densely and therefore for all h, giving (2).

It remains to rule out deg D=0 and deg D=1 under density. These are universal polynomial contradictions, using arbitrary trace-free self-adjoint operators rather than evaluating selected actual sources.

If D=0, r is a linear functional H→C and density would force det(S−r(S)I) identically zero. Choose a B-orthonormal basis and write a general symmetric trace-free S with diagonal entries x,y,−x−y and independent off-diagonal indeterminates u,v,w. On the diagonal subspace the identity becomes

(x−r)(y−r)(−x−y−r)=0.

Since C[x,y] is a domain, the restriction of r equals one diagonal entry identically. Permuting the basis, take it to be x. Write r=x+αu+βv+δw. The coefficient of each off-diagonal variable in the determinant at u=v=w=0 is respectively −α,−β,−δ times the nonzero polynomial (y−x)(−2x−y). Thus α=β=δ=0. Now with v=w=0 the determinant equals u²(2x+y), which is not the zero polynomial. Contradiction.

If deg D=1, write D=(ell=0), choose a complementary m, and use the abstract basis U=ell², T=ell m, W=m², normalized by B(U,W)=1 and B(T,T)=−1/2. A general self-adjoint trace-free operator is

S = [[x,b,c],[e,−2x,−2b],[g,−e/2,x]],

with five independent indeterminates x,b,c,e,g. Write r=p(S)+q(S)m/ell with linear functionals p,q. A solution must lie in ell·H0(O(1))=span(U,T). Its equation is the kernel equation for the matrix

[[x−p,b],[e−q,−2x−p],[g,−e/2−q]].                 (3)

Density forces every 2 by 2 minor to vanish identically. Restrict these polynomial identities to x=b=e=0, retaining the independent indeterminates c,g. The three minors are p², pq, q²+pg. They force p=q=0 on this two-dimensional subspace. Hence p,q are independent of c and g. But the rows 1 and 3 minor of (3) has coefficient −b in g. This cannot vanish identically. Contradiction.

Thus only deg D=2 remains, proving existence of a common a0. Conversely (2) immediately gives Y=P(H). Uniqueness follows from PR759: two independent common directions would make dim E_h≥2 for every nonzero h, whereas that source locus has dimension at most one in P(H)=P4. ∎

The maximal pole divisor in case (2) is indeed div(a0): alternatively this follows already from the proof above and uniqueness. No extraction of its actual points is needed.

## 3. The remaining pencil sources in the common-direction branch

Assume (2). Use PR759's closed immersion

j:P(A)→P(H),   [v]↦[S^{-1}(Q(v))],
Q(v)=v⊗B(v,−)−B(v,v)I/3.

The sources with dim E_h=2 are exactly

X=j(P(a0^perp)).                                  (4)

To prove necessity, PR752 and PR759 identify any two-dimensional E_h with v^perp for its unique j([v]). Since a0∈E_h, B(v,a0)=0. Conversely if B(v,a0)=0, Q(v)a0=−B(v,v)a0/3. Formula (2) then gives K_h=γλd for the repeated eigenvalue λ=−B(v,v)/3. PR752 yields E_h=v^perp of dimension two. This includes isotropic v, where λ=0 and Q(v) is rank-one square-zero.

Because j is the projected Veronese embedding, its restriction to the projective line P(a0^perp) is a degree-two embedding. Therefore X is a smooth plane conic, not merely an unspecified curve of dimension at most one. For h outside this conic, E_h=C a0 exactly.

The isotropic boundary of this conic has scheme length two. If B(a0,a0)≠0, B restricted to a0^perp is nondegenerate of dimension two, giving two distinct isotropic points. If B(a0,a0)=0, the restriction has radical C a0 and rank one, giving the doubled point [a0]. This is a conditional refinement of PR759's general length-at-most-four bound, not an assertion that the common-direction branch occurs.

## 4. Contribution and unresolved dependency

The earlier pencil-source result controls sources having two exceptional negative directions. The present argument controls the remaining one-direction fibers: their source locus has the finite description (1), and density is possible only through one common negative direction valid for every source. In that branch the two-direction source locus is exactly the conic (4). Otherwise a general source has no exceptional direction at all.

The unresolved dependency is which side the actual, unevaluated K occupies. Neither side implies an actual first-order deformation is higher-order integrable. Vanishing of the modular gate is not sufficient for vanishing of ρ4, and neither gate decides the distinct β4 boundary. No algebraicity conclusion is drawn.

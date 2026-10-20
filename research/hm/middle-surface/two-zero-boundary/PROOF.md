# Two-zero boundary: exact relative cone and resolved rank-one directions

## Theorem and scope

Work over C with dim V=5 and dim J=20, and the canonical trilinear map f with outer symmetry and cyclic-zero identity. Import the locally split injection A_u:H -> J, A_u(v)=f(u,u,v), and the rank-ten hypothesis for Q_u(v)=[f(v,u,v)] on V/Cu. No antisymmetric residual map is assumed injective, surjective, or known.

Let S be a two-zero-input stratum, with its remaining input u nonzero. Shrink its base around a point whose common line has rank Q_u=10. Then:

1. A neighborhood of S is an exact relative homogeneous quadratic zero scheme in a rank-ten vector bundle over the five-dimensional u-base. Its normal cone along S is that very relative scheme, not merely a quadratic approximation.
2. Blow up the ambient space along S. The strict transform of X, equivalently the blowup of X along S, is the total tautological line bundle over the relative projective quadratic zero scheme. The exceptional divisor is exactly that projective scheme; it is an effective Cartier divisor on the strict transform.
3. The projective rank-one directions form a P¹-bundle L over S. Near every point of L, the strict transform is determined by the existing rank-ten normal forms. Away from its two endpoint sections it is a rank-four square-zero thickening of its smooth rank-one component. At either endpoint it has the exact algebraic local presentation

       O_B[e,q1,q2,q3,q4]/(e(q1,q2,q3,q4)^2),

   up to open localization, with B smooth of dimension six. One of the six base parameters is the exceptional line parameter r. The exceptional divisor is r=0.
4. In a neighborhood of L there are only the rank-one component and the two strict transforms of the zero-input coordinate components through S. The latter two are disjoint in the blowup. The rank-one component is locally the blowup of its original smooth rank-one locus along S; its exceptional locus is L. Its generic multiplicity is five. Each coordinate component is reduced at its generic point and has multiplicity one. Locally the nilradical is square-zero and free of rank four over the reduced rank-one component, including its intersections with the coordinate components and the exceptional divisor.

These are a complete description near the rank-one exceptional directions, not a classification of the whole two-zero germ. Other projective directions, and hence other components through the unblown vertex section, are not excluded. The full closed-point tangent cone in the fifteen-dimensional ambient space is not identified here with a product by the tangent space of S.

## 1. Separate formulas for the two permutation types

Choose ell with ell(u) nonzero and H=ker ell. For the nonzero outer input, write

    (x,y,z)=(a u+p,b u+q,u),       p,q in H.

These are exact independent algebraic coordinates on ell(z) nonzero. The variables u have dimension five; (a,b,p,q) have dimension ten. The identities give

    f(x,y,z)=b A_u(p)-2a A_u(q)+f(p,q,u).                 (1)

Indeed f(p,u,u)=A_u(p), f(u,q,u)=-2A_u(q), and f(u,u,u)=0. Here S is a=b=p=q=0. The case with nonzero first input follows by outer symmetry.

The nonzero middle input is a different permutation type. Use

    (x,y,z)=(a u+p,u,c u+q),       p,q in H.

Its independent coordinates give the different exact formula

    f(x,y,z)=c A_u(p)+a A_u(q)+f(p,u,q).                 (2)

We do not identify the mixed bilinear terms in (1) and (2). Each formula is homogeneous quadratic in its ten fiber coordinates, with algebraic coefficients in u. In each case the rank-one locus D is p=q=0, with its two scalar coordinates free. Thus D is a rank-two vector bundle over S in this chart.

The two coordinate components containing S are x=0 and y=0 in (1), and x=0 and z=0 in (2). Their fiber spaces are complementary five-dimensional linear subspaces of the ten-dimensional ambient fiber.

## 2. Normal cone exactness, and what it does not imply

Let R be the coordinate ring of the chosen smooth affine u-base, T=R[t1,...,t10] with the fiber grading deg(t_i)=1, and I the homogeneous quadratic ideal given by (1) or (2). Put A=T/I. The ideal K of S in X is the positive-degree ideal. Since A is standard graded,

    K^n = direct sum of A_d for d >= n,
    gr_K(A) = A

as graded R-algebras. This proves C_S X = X in these exact coordinates. It also proves that the relative normal cone embedding in N_(S/M) is cut out by precisely the displayed quadrics, scheme-theoretically.

For any fixed u, the scheme-theoretic fiber is a homogeneous quadratic cone, and its tangent cone at its fiber vertex is itself. Since I has no terms of total order one, the Zariski tangent space of X at a closed point of S is the entire fifteen-dimensional ambient tangent space.

We do not deduce that the full closed-point tangent cone equals T_u S times that fiber cone. The normal-cone grading above treats functions of u as degree zero, whereas the closed-point tangent cone also filters those functions by their maximal ideal. Flatness of the graded pieces over the u-base has not been proved or used.

## 3. Blowup of a standard graded cone

Write Z=Proj_R A. The blowup of Spec A in K is canonically the total space of O_Z(-1). Here this notation means Spec_Z Sym(O_Z(1)), and is valid even if Z is nonreduced or reducible.

For an explicit verification, on the projective chart indexed by t_i put

    B_i=(A[t_i^(-1)])_0.

The blowup chart is the subalgebra A[K/t_i] of A[t_i^(-1)]. The grading identifies the latter localization with B_i[r,r^(-1)], with r=t_i, and its blowup subalgebra is exactly B_i[r]. Relations and any t_i-torsion have already been handled by localization. These chart identifications glue with the transition functions of O_Z(-1). The exceptional ideal is (r); r is a nonzerodivisor in B_i[r], regardless of nilpotents or components in B_i. Consequently the exceptional divisor is Z, with its full scheme structure.

The ambient blowup gives the same answer. Its chart substitution is t_j=r v_j with v_i=1. Every defining equation becomes r² F(u,v). The strict-transform ideal is the saturation of this total-transform ideal by r. Since (R[v]/(F))[r] has no r-torsion, that saturation is exactly (F). Thus the ambient strict transform equals the intrinsic blowup just described. No division by a zero divisor in O_X is involved.

The rank-one directions inside Z are the closed P¹-bundle L defined by p=q=0. Its endpoints are the two projectivized coordinate directions. Projectivizing the two complementary five-dimensional coordinate subspaces yields disjoint P⁴-bundles; this proves disjointness of the coordinate strict transforms.

## 4. Why the old normal forms apply on the projective charts

A point of L represents two scalar multiples of u, with at least one scalar nonzero. Normalize that scalar to one in the corresponding projective chart. After removing the exceptional factor r² from the equations, the resulting triple has the original nonzero input u and one further nonzero input. Thus it is a scalar-normalized slice of an ordinary chart of the original zero scheme. This observation must be checked as an actual coordinate slice, rather than treated as an arbitrary hyperplane section of a known local ring.

Here are the checks for (1). On the projective chart a nonzero, normalize a=1. The direction triple is

    (u+p,b u+q,u).

In the exactly-one-zero chart of /research/hm/middle-surface/zero-input-rank-one-boundary/PROOF.md, Section 3, put v=u+p. The ratio of ell(z) to ell(x) is identically t=1; its residual displacement z/t-v is -p, and the scalar coefficient of y along v is exactly b. Therefore the normalized chart is exactly the independent-coordinate slice t=1 of that proof. Its four algebraic eliminations and factored Nakayama argument apply unchanged. The base originally denoted (v,t) becomes v alone; adjoining the independent exceptional parameter r restores a smooth six-dimensional base. At b=0 the answer is b(q_res)^2. The symbol q_res denotes the four residual coordinates from that proof, not necessarily the q in (1).

On the projective chart b nonzero, normalize b=1. The triple is

    (a u+p,u+q,u).

Use the outer-zero chart, Section 1 of the same source, with middle input v=u+q. Again t=ell(z)/ell(v)=1 identically; its zero-input scalar is a. The identical t=1 restriction gives a(q_res)^2 after elimination, with independent r adjoined.

For (2), normalizing a=1 gives the triple (u+p,u,c u+q). Near c=0 apply outer symmetry to obtain (c u+q,u,u+p). This is the outer-zero chart of Section 1 with t=ell(u+p)/ell(u)=1, zero-input scalar c, and nonzero middle input u. Normalizing c=1 gives (a u+p,u,u+q), directly the same outer-zero chart with t=1 and scalar a. Hence both endpoints again have e(q_res)^2.

The determinants inverted in the original eliminations equal one at L. The common-line rank-ten hypothesis holds at each point under consideration; surjectivity and coherence permit the necessary Zariski shrinking. This justifies the ideal equality, not merely an equality of quadratic leading terms. All added equations are independent of r, so r stays a free line parameter in every displayed presentation.

Away from the two endpoint sections both scalar coefficients are nonzero. The same projective charts are open portions of these presentations with e invertible, giving exactly (q_res)^2. Equivalently one may use the all-inputs-nonzero theorem, with one independent scalar ratio fixed to one. No additional hypothesis on the antisymmetric residual is needed.

## 5. Local components and infinitesimal structure

At either endpoint let P=(q1,...,q4). The ambient regular local ring after elimination is S'=O_B[e,q1,...,q4], localized as needed. The established ideal is eP². The exact identities

    eP²=(e) intersection P²,
    sqrt(eP²)=eP,
    N=eP/eP² ≅ P/P²

give the two local components and the square-zero nilradical. The module is locally free of rank four on the rank-one component P=0. The primary ideals (e) and P² have no embedded associated primes. The coordinate component has dimension ten, the rank-one component dimension seven, and their reduced intersection dimension six. The generic multiplicities are one and five, respectively. Off the endpoint sections e is invertible and only the rank-one square-zero component remains.

The nilradical statement is intrinsic and hence glues on an open neighborhood of L. It asserts local freeness, not a chosen global trivialization or splitting. The local descriptions also exclude any further irreducible component meeting L. Taking their union supplies a neighborhood in which precisely the indicated components occur. This does not rule out components elsewhere in the exceptional projective scheme.

Since D was the rank-two vector bundle p=q=0 over S, its strict transform is its blowup along the zero section S, namely the total tautological line over L=P_S^1. This identification concerns the reduced rank-one component. It does not assert that an unspecified primary component of the original two-zero germ has already been classified before blowing up.

Finally, r is part of the smooth base B. Restricting to the exceptional divisor simply deletes that parameter from every local presentation. In particular the projective quadratic scheme Z itself has rank-four square-zero structure near the open rank-one directions and the endpoint model eP² over a smooth five-dimensional base. This directly describes the normal cone near those directions, with nilpotents retained.

## 6. The blowup exposes, but does not resolve, these singularities

The exceptional line parameter is regular in every chart. Near an interior point of L the strict transform still has transverse square-zero algebra C plus C^4, of length five, rather than being reduced or smooth. At an endpoint it still has the mixed-dimensional eP² model and is not Cohen–Macaulay.

At closed points over L, the strict transform has tangent dimension eleven. At an interior direction its local dimension and depth are both seven. At an endpoint its local dimension is ten and its depth is seven. On the exceptional divisor the corresponding tangent dimension is ten; the interior dimension and depth are six, while the endpoint dimension is nine and depth six. These statements follow directly from the presentations: the interior algebra is free of rank five over a regular base; the endpoint depth follows from the exact sequence for (e) intersection P², as in Section 6 of the one-zero proof. Quotienting by the regular base parameter r lowers depth and local dimension by one.

Each coordinate component meets the exceptional divisor in its P⁴-bundle and meets L in the corresponding endpoint section. The rank-one component meets the exceptional divisor in the whole P¹-bundle L. This is compatible with the transverse reduced-component incidence in the eliminated eP² chart.

In particular this single blowup is not a resolution or a reduction operation near L. Conversely, its clean local primary decomposition cannot be pushed down to assert absence of embedded components in the original two-zero germ: blowing up can lose information supported solely on the center, and no such original decomposition was proved.

## Limits and provenance

The imports are /research/hm/middle-surface/zero-input-rank-one-boundary/PROOF.md and /research/hm/middle-surface/rank-one-open-thickening/PROOF.md, including the symbolic identities and repeated-input injection that they explicitly cite. Rank ten is a hypothesis at the common line, not a selected rank evaluation.

No claim is made about all projective directions, the antisymmetric residual, a complete primary decomposition at the original two-zero point, flatness over the u-base, the full closed-point tangent cone, the all-zero vertex, or constant rank ten. The two positions of the nonzero input were handled separately; outer symmetry alone was used only to exchange first and third inputs. All arguments are symbolic and algebraic.

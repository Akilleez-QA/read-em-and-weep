# Plane incidence exclusion and uniform lower Rao rank

Work over C. Let C be the twenty-five disjoint transverse HM evaluation-degeneracy lines in P(V), dim V=5. A hyperplane is proper if it contains no component of C. Write M_d=H^1(I_C(d)). All assertions below concern this line arrangement and its Rao module, not the original fixed-pair source or higher-order lifting problem.

## 1. Pinned inputs and statement

The Eagon–Northcott ideal-sheaf presentation of PR463 gives a surjection

Lambda^2 H^0(E) tensor O -> I_C(5).

Thus six quintics generate the ideal SHEAF after twisting; this does not say that the saturated homogeneous ideal has only quintic generators. PR464 and its successors explicitly retain ten additional sextic generators.

PR472 proves that for every proper hyperplane H, its section D=C intersect H is twenty-five reduced points with h_D(6)=25. PR473 proves that, for ell defining H and r=rank(ell:M_4 -> M_5),

h_D(5)=r-5 and r>=25.

Here h denotes the Hilbert function of the saturated homogeneous coordinate ring.

We prove:

1. Every plane P containing no component line of C meets at most nineteen component lines.
2. Every proper hyperplane section spans its ambient P^3.
3. For every proper ell, rank(ell:M_4 -> M_5)>=26, coker dimension<=4, and kernel dimension<=29.

Dependencies are PR463 for sheaf generation, PR472 for uniform sextic interpolation, and PR473 for the lower Rao rank/Hilbert-function relation. The proof of the nineteen-point bound also uses the classical complete-intersection residual identity stated below.

## 2. Restriction to a plane and a preliminary bound

Fix a plane P containing no component line, and let E=C intersect P. Each component either misses P or meets it in a single reduced point; the points from different components are distinct because the lines are disjoint. Thus E is reduced, of cardinality n equal to the number of lines met by P.

There is a proper hyperplane H through P. Indeed hyperplanes through P form a projective line. For any component line not contained in P, at most one such hyperplane contains that line. Avoid these finitely many members. The set E is a subset of D=C intersect H. Surjective sextic evaluation on D implies surjective sextic evaluation on E. Since restrictions of sextic forms on H to P are all plane sextic forms,

h_E(6)=n.

Restrict the six generating quintics to P, and call their span L. Their scheme-theoretic base locus is exactly E. To justify this despite possible Tor, tensor the sheaf surjection with O_P and then take its image in O_P(5): this image is I_C O_P(5)=I_(E,P)(5). Thus L generates the plane ideal sheaf. In particular L has no fixed curve.

Choose f,g in L with no common curve component. Such a choice exists: start with a nonzero f, and choose g outside the finitely many linear subspaces of L consisting of sections vanishing identically on a component of f. Their plane complete intersection Z has length twenty-five and contains E. Its Koszul resolution gives

h_Z(6)=dim C[x,y,z]_6 - 2 dim C[x,y,z]_1 = 28-6=22.

Consequently n=h_E(6)<=22. This already excludes a plane containing an entire proper hyperplane section of C.

## 3. Residual separation sharpens twenty-two to nineteen

We may choose the coprime pair f,g with independent linear terms at every point p of E. Indeed the germs of L generate the maximal ideal of the smooth plane local ring at p, so their linear terms span its two-dimensional cotangent space. Independence at each of the finitely many points is a nonempty open condition on L times L. Coprimeness is another nonempty open condition, established in section 2. These open sets intersect. The complete intersection Z consequently has local length one at every p of E.

Let R be the residual scheme to E in Z. Thus Z is the disjoint scheme union of E and R, and length(R)=m=25-n. The residual scheme may be nonreduced; no Bertini or reducedness assertion about R is needed.

For complementary residual subschemes of a plane complete intersection of degrees (5,5), the residual identity is

dim (I_E/I_Z)_a = h^1(I_R(7-a)).

This is the classical Cayley–Bacharach residual formula, with 7=5+5-3; a public statement is Gold–Little–Schenck, section 1.2 and Theorem 1.2. Applying it at a=6 gives

22-n = m-h_R(1).

Together with n=25-m, this forces h_R(1)=3: the residual scheme spans the plane.

Choose h in L nonzero at every support point of R. This is possible because the base locus of L is E and the support of R is finite. The restriction of h is therefore a unit after local trivialization of O_R(5). Multiplication by h defines a map

C[x,y,z]_1 -> (I_E/I_Z)_6.

If a linear form u maps to zero, then hu vanishes on Z. Since h is a unit on R, u vanishes scheme-theoretically on R. Since R spans P, u=0. The map is injective, so dim(I_E/I_Z)_6>=3. Therefore

22-n>=3, and n<=19.

The extra three conditions come from a third quintic separating the residual points, not from an assumed independent restriction of the six original quintics. This also shows precisely where the reducedness of E, sheaf generation, and uniform sextic interpolation enter; no reducedness of the residual scheme is assumed.

## 4. Excluding the minimal Rao rank

Suppose a proper ell had rank twenty-five. Then its section D has h_D(5)=20 and h_D(6)=25. The saturated coordinate ring of a finite reduced point set has dimension one and depth one: a linear form avoiding the points is a nonzerodivisor. Its Artinian reduction therefore has Hilbert function a_i=h_D(i)-h_D(i-1), with a_0=1 and a_6=5.

Macaulay growth backwards from a_6=5 implies

a_5>=5, a_4>=5, a_3>=4, a_2>=3, a_1>=2.

For clarity, values at most four in degree five or four cannot grow to five; values at most three in degree three cannot grow to five; a value at most two in degree two cannot grow to four; and a value at most one in degree one cannot grow to three. These are the corresponding Macaulay binomial expansions.

The lower bounds sum through degree five to 1+2+3+4+5+5=20. Since h_D(5)=20, every bound is equality. Since h_D(6)=25 equals the length, all later differences vanish. Thus the entire h-vector is

(1,2,3,4,5,5,5).

In particular h_D(1)=3, so D spans a plane P. This plane contains no component line because it lies in the proper H. It would meet all twenty-five lines, contradicting even the preliminary twenty-two bound, and a fortiori the nineteen bound. Hence rank is at least twenty-six. Since dim M_4=55 and dim M_5=30, the stated kernel and cokernel bounds follow.

Independently of the rank argument, any proper section contained in a plane would meet all twenty-five lines in that plane. Thus every proper section spans P^3.

## 5. Scope and next dependency

This excludes the entire rank-twenty-five stratum among proper linear forms, including special forms; it is not just a generic nonplanarity assertion. It does not prove that the rank is exactly twenty-six or that M_4 -> M_5 is surjective.

For U=ell M_4, the annihilator has vector-space dimension at most four. The rank-one incidence argument of PR473 therefore has ambient projective dimension at most three immediately. This simplifies its already established bound on bad second factors; it does NOT improve that bound to two without another argument. General quadratic surjectivity remains as in PR473. No assertion about the original fixed quadratic, original source membership, first-order pairing, higher-order lifting, or algebraicity is added.

No selected actual HM/source-instance evaluation, numerical rank, coefficient search, generator/checker, or large computation is used. These are authored and mathematically reviewed proofs, not formal proof-assistant verification.

## References and exact dependency pins

- PR463: https://github.com/Akilleez-QA/read-em-and-weep/pull/463, commit 8ec3631dcd6937e6cc7491d0200c1c78b5d21434, Eagon–Northcott sheaf presentation.
- PR472: https://github.com/Akilleez-QA/read-em-and-weep/pull/472, commit 306cd02e623881f3caeddaf17a286c33d3bec63f, uniform proper-hyperplane sextic interpolation.
- PR473: https://github.com/Akilleez-QA/read-em-and-weep/pull/473, commit 10e686c616512bec3f27b2bcb9d4749323d5aee2, lower Rao rank and quadratic incidence.
- Juan C. Migliore, The Geometry of Hilbert Functions, Definitions 2.3–2.5 and Theorem 2.6: https://academicweb.nd.edu/~jmiglior/Hilb.pdf.
- Leah Gold, John Little, Hal Schenck, Cayley–Bacharach and evaluation codes on complete intersections, section 1.2 and Theorem 1.2: https://arxiv.org/pdf/math/0311129.

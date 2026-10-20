> Publication scope: preserved mathematical proof/audit. Historical statements that rank eight remains open are superseded only after the final assembly and all its prerequisites. No source-instance evaluation or formal verification is claimed here.

# Two-sided Plücker obstructions for the global linear image

## Results

Retain the hypotheses and notation of `../rank-four-global-determinant/PROOF.md`. Let r be the generic rank of Q, let n=r+4, and let F be the saturated image of

    b: O(-1) tensor Sym^2 V -> J tensor O.

Write det F=O(-k), and let d be the degree of the common divisorial zero locus of its maximal minors, regarded as sections of O(n-k). Then

    k >= 2,     n-k-d >= 2,     d >= 0,     5 divides d,
    k = 3n modulo 5.

In particular generic rank r=8 forces

    det F=O(-6),     det I=O(1),     d=0.

Thus at generic rank eight, Q has no rank drop at the generic point of any divisor. The same conclusions at rank six are det F=O(-5), det I=O(2), d=0.

These are restrictions conditional on the actual generic rank, not a determination of that rank. No source matrices, operation products, values at inputs, rank instances, or polynomial instances are evaluated.

## 1. An elementary fact about linear spaces in a Grassmannian

Let S be a vector space and Z=P^s a projective linear space contained in the Plücker embedding of Gr(m,S), with s>=1. Then either all the represented m-planes contain a fixed (m-1)-plane, or they all lie in a fixed (m+1)-plane. Consequently their sum has dimension at most m+s.

Here is a proof. Two distinct m-planes whose entire Plücker line lies in the Grassmannian intersect in dimension m-1. To verify this standard line criterion directly, factor out their common intersection of dimension a. Their Plücker vectors become decomposable (m-a)-vectors on two disjoint spaces. If m-a>=2, the sum of those two vectors is not decomposable: the contraction span (the span of all contractions by (m-a-1)-forms) has dimension 2(m-a), whereas the contraction span of a nonzero decomposable (m-a)-vector has dimension m-a. Thus m-a=1.

Choose two distinct represented planes A,B, and put T=A intersect B and H=A+B. Every other represented plane C intersects both in codimension at most one. If C does not contain T, then C intersect A and C intersect B are distinct hyperplanes in C; their sum is C and lies in H. Thus each C either contains T or lies in H. If one C contains T but is not contained in H, then C intersect H=T. Any represented D contained in H but not containing T would meet C in dimension at most m-2, contradicting the line criterion. Therefore the family is entirely of one of the two asserted types.

For the family containing T, wedge with a fixed generator of det T identifies the Plücker linear space with a projective linear space of lines in S/T. Their span has dimension s+1, and the sum of the m-planes has dimension m+s. For the family contained in H, their sum has dimension at most m+1<=m+s.

## 2. The image-side obstruction k>=2

The determinant of the inclusion F into J tensor O yields a nonzero collection of sections of O(k), indexed by Plücker coordinates. On the dense locally free locus these give the Plücker image of the n-dimensional subspace F_u of J. The coordinate sections extend across codimension at least two.

The span of the subspaces F_u on any dense open set is all of J. Indeed a linear functional on J annihilating all these subspaces annihilates b(u,s) for every u in a dense open set and every s in S. Polynomiality then makes it annihilate b identically, hence all values of the trilinear operation. Those values span J by the established nonvanishing and irreducibility theorem.

If k=0, the image is a constant n-plane, contradicting that spanning property.

If k=1, the rational map given by the nonzero linear coordinate system has image a projective linear space P^s with s<=4. Its entire image lies in Gr(n,J), by closedness. If s=0 the previous contradiction applies; otherwise Section 1 bounds the sum of the represented n-planes by n+s<=n+4<=18<20. This again contradicts the spanning property. Thus k>=2.

This proof does not require irreducibility of the five-dimensional source representation or global definition of the Plucker map. The only representation-theoretic input here is the already established full span of the operation values in J.

## 3. The kernel-side obstruction n-k-d>=2

Put S=Sym^2 V, of dimension fifteen. Untwist b to obtain

    B: S tensor O -> F(1).

On its generic full-rank locus its kernel K_u has dimension

    m=15-n=11-r.

The maximal minors are global sections of O(n-k). Their common divisorial factor has degree d. After dividing by this factor, their remaining coordinates are homogeneous forms of degree

    e=n-k-d >=0.

They describe the kernel Plücker map into Gr(m,S), using the canonical duality between quotient and kernel Plücker coordinates.

The cyclic identity implies f(u,u,u)=0. Hence

    u^2 belongs to K_u

wherever the generic kernel is defined. The span of u^2 as [u] ranges over any dense open subset of P(V) is all of Sym^2 V: a linear functional vanishing on all such squares would give a quadratic form vanishing on a dense open set, and hence the zero form.

If e=0, the kernel is constant, which contradicts this spanning property because m<15.

If e=1, the rational map defined by its linear coordinate system is a linear projection with image a projective linear space P^s, where 1<=s<=4. Its entire image lies in the Grassmannian since the latter is closed and contains the image of the dense full-rank locus. Section 1 shows that the sum of these kernels has dimension at most

    m+s <= m+4 = 15-r <=11.

This again contradicts the spanning property. Thus e>=2.

This argument does not require the rational Plücker map to be defined at every point, nor does it assume that F is globally locally free.

## 4. Equivariance and the rank-eight consequence

As established in the determinant proof, the center of H5 gives k=3n modulo five. The common divisorial factor of the maximal minors is invariant under the normalizer; its defining polynomial is a semi-invariant, so its degree d is divisible by five, since the H5 center is contained in the commutator subgroup.

At r=8, n=12 and k=1 modulo five. The inequalities k>=2 and k<=n-2=10 force k=6. Then e=6-d>=2 and d is a nonnegative multiple of five, forcing d=0.

At r=6, n=10 and k=0 modulo five. The same bounds force k=5; then e=5-d>=2 forces d=0.

The exact sequence 0 -> O(-2) tensor U -> F -> I ->0 has determinant of its first term O(-7). Consequently det I=O(7-k), giving the stated values. Absence of a divisorial common minor factor means B, equivalently b, has full generic rank at every codimension-one point. Because its image contains the rank-four subbundle A, Q also has its full generic rank at every codimension-one point.

## 5. Complete determinant table allowed by these obstructions

The remaining possibilities are:

    r=4:  k=4,      d=0.
    r=5:  k=2 or 7; for k=2, d=0 or 5; for k=7, d=0.
    r=6:  k=5,      d=0.
    r=7:  k=3 or 8; for k=3, d=0 or 5; for k=8, d=0.
    r=8:  k=6,      d=0.
    r=9:  k=4 or 9; for k=4, d=0 or 5; for k=9, d=0.
    r=10: k=2, 7, or 12; see the exact refinement below.

At r=10, the generic kernel has rank one and contains u^2, so its Plücker map is exactly the quadratic Veronese map. The residual Plücker degree is therefore e=2. For completeness, this degree statement follows without assuming a chosen minimal representation: the square-coordinate Veronese vector is primitive, and any polynomial vector representing the same rational map is its common scalar multiple. Since all divisorial common factors have been removed, that scalar is constant. Thus

    d=12-k,

and the three allowed pairs are (k,d)=(2,10),(7,5),(12,0).

The table is a necessary-condition table only; no realization assertion is made.

## Sources and evidence boundary

The input bundle construction, generic basepoint-freeness, and r in {4,...,10} come from `../rank-one-quadratic-flag-nef/PROOF.md`. The determinant construction and central-character arguments are from `../rank-four-global-determinant/PROOF.md`; normalizer irreducibility is established in `../../full-hm-image-symmetry/PROOF.md` and the already imported cubic target identifications. The two-sided Plücker obstructions are proved here by universal linear algebra. Only local proof reading and writing were used.

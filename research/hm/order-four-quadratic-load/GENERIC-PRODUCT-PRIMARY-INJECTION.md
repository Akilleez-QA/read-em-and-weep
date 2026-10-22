# Generic products of two linear forms are primary-injective

## Theorem and scope

For the normalized HM bundle F, set A_d=H^1(F(d)). A general product q=ell1 ell2 of two linear forms induces an injective map

    q:A_0 -> A_2,  of dimensions 5 -> 10.

Moreover the generic corank of the middle linear map ell:A_1->A_2 is either one or two. No exact value is asserted. This concerns PRIMARY cohomology only. It does not prove Rao residual surjectivity, full adjoint invertibility, a good square, goodness of the original prescribed quadratic, or Q4 vanishing.

## 1. A good plane with no common degree-one annihilator

Boralevi's generic plane resolution gives a nonempty open subset of planes P with

    0 -> 3O_P(-3) -> 5O_P(-2) -> F_P -> 0.

Source: Ada Boralevi, The Horrocks–Mumford bundle restricted to planes, arXiv:math/0602002v2, Main Theorem and Corollary 2.2:
https://arxiv.org/pdf/math/0602002

The splitting of the degree-one and degree-two Koszul complexes, detailed in GOOD-PLANE-PRIMARY-TRACE.md, yields for U=H^0(I_P(1)), dim U=2,

    U tensor A_0 isomorphic to A_1,
    Sym^2 U tensor A_0 -> A_2 surjective.

These conclusions use F(-1) acyclic, H^2(F)=0, and the plane resolution, not a selected multiplication matrix. Put

    N=ker[Sym^2 U tensor A_0 -> A_2],  dim N=15-10=5.

We may also choose P so that H^0(I_P tensor F(3))=0. Here is a geometric proof. Every nonzero section of F(3) has no divisorial zeros: a divisorial factor of positive degree d would give a nonzero section of F(3-d), contrary to the known absence of sections in twists at most two. Its zero locus therefore has dimension at most two. Any plane contained in that locus is a two-dimensional irreducible component, so there are only finitely many such planes for each section. The closed incidence of planes contained in the zero locus with [s] in P(H^0(F(3)))=P3 has finite fibers over P3 and hence dimension at most three. Its image is a proper closed subset of the six-dimensional Grassmannian of planes. A general plane is not contained in the zero locus of any nonzero section, and can simultaneously belong to Boralevi's good open.

The degree-three Koszul splitting gives

    ker[A_1 -> U tensor A_2] = H^0(I_P tensor F(3)),

where the map has components multiplication by a basis of U. Indeed 0 -> F(1) -> F(2)^2 -> I_P tensor F(3) -> 0 and H^0(F(1))=H^0(F(2))=0 identify this kernel directly. Thus the chosen plane has no nonzero common degree-one annihilator:

    z in A_1,  U z=0  implies z=0.                      (2)

The nonzero group H^0(F(3)) is explicitly accounted for; no naive degeneration of the Koszul spectral sequence is assumed.

## 2. Evaluation of the five-dimensional quadratic relation space

Regard N as a space of A_0-valued binary quadratics on P(U*). Let

    N tensor O -> A_0 tensor O(2)

be evaluation. Its generic kernel dimension b is exactly the generic corank of multiplication ell:A_1->A_2 within this pencil. To see this, evaluation at p has kernel

    B_p=N intersect (ell U tensor A_0),

where ell spans the one-dimensional subspace of U vanishing at p. The identification U tensor A_0=A_1 turns this intersection into the kernel of multiplication by ell. No lower bound on b is needed for the product theorem. The separately verified section theorem will later supply b>=1.

Let E be the saturation of the evaluation image, a vector subbundle of A_0 tensor O(2) on P1, of rank r=5-b. The five independent vector-valued quadratics remain independent global sections of E, so h^0(E)>=5. Every summand O(e) in its splitting has e<=2, because a summand of larger degree could not map nontrivially into A_0 tensor O(2).

Suppose b>=3, so r<=2. Rank at most one is impossible since h^0(E)<=3 then. For rank two, the only splitting types with both degrees at most two and at least five sections are (2,1) and (2,2).

If E=O(2) direct-sum O(1), h^0(E)=5, so N=H^0(E). The O(2) summand maps into A_0 tensor O(2) by a nonzero constant vector a. Hence N contains Sym^2 U tensor a. Every element of U tensor a is then annihilated by U in A_2, contradicting (2).

If E=O(2)^2, its inclusion identifies E with E0 tensor O(2) for a fixed two-dimensional E0 in A_0. Now N is a hyperplane of Sym^2 U tensor E0. For z in U tensor E0, requiring xz and yz to belong to N, for a basis x,y of U, imposes at most two scalar linear conditions on a four-dimensional space. A nonzero such z exists and again contradicts (2).

Therefore 0<=b<=2. The product theorem below uses only this bound. The separate section theorem refines it to 1<=b<=2 for the HM bundle.

## 3. Two generic evaluation kernels are disjoint

Work on the nonempty open subset of P(U*) where dim B_p=b. For distinct p,q, with corresponding independent linear factors ell_p,ell_q,

    B_p intersect B_q
      = N intersect (ell_p ell_q tensor A_0).

Division by the nonzero product identifies this with ker(ell_p ell_q:A_0->A_2). It suffices to show that some pair has disjoint B_p,B_q.

If b=0, any two distinct points in this open set already have disjoint kernels, proving the claim.

If b=1 and every pair intersects, all the lines B_p are one fixed line. A nonzero quadratic in that line would vanish at every p in a dense open subset of P1, hence identically. This contradicts its nonzero membership in N.

Suppose b=2 and every pair intersects. If all B_p coincide, the same argument applies. Otherwise choose two distinct planes B_p,B_q, meeting in a line L and spanning a three-dimensional space S. Every two-plane meeting both either contains L or is contained in S: if its two intersection lines are different, they span it inside S; if equal, they equal L. The irreducible closure of the curve of planes B_p therefore lies wholly in one of these two closed families. The common-L alternative is impossible by the polynomial-vanishing argument.

Thus all generic B_p lie in S. Evaluation of S, a three-dimensional space of vector-valued quadratics, has generic rank at most one, because its kernel contains B_p of dimension two. The saturated image is a line subbundle O(d) of A_0 tensor O(2). Its degree satisfies d<=2, while the three independent sections in S imply h^0(O(d))>=3. Therefore d=2, and its inclusion is a constant vector a in A_0. We obtain

    S=Sym^2 U tensor a.

Since S is contained in N, this again creates a nonzero common degree-one annihilator, contradicting (2).

In every case, some pair has disjoint evaluation kernels. The corresponding product is primary-injective. Injectivity is open in the irreducible parameter space of pairs of linear forms, so a general product is primary-injective.

## 4. Additional consequences and boundaries

The same argument works for every plane in the intersection of the two established open sets: the generic-resolution locus and the locus with H^0(I_P F(3))=0. The primary-good product assertion does not depend on the Banica–Manolache lemma; only the positive lower bound on the middle corank uses that result. Thus a general good pencil has generic middle corank one or two and has primary-good products of two distinct members.

The symmetric five-dimensional trace description in GOOD-PLANE-PRIMARY-TRACE.md now has genuinely disjoint trace spaces for a general pair, rather than requiring an unproved transversality premise. This is a conclusion about the PRIMARY trace spaces H^0(F_H(2)) inside H^0(F_P(2)); it does not establish transversality of the Rao section-cubic trace spaces in a ten-dimensional plane-cubic space.

The theorem proves neither that a square ell^2 is good nor that every product is good. No passage to the diagonal, selected coefficient evaluation, or experiment is used. The original source membership, residual condition, lift boundary, and full Q4 remain open.

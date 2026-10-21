# Identifying the primary line-bearing surface with the degree-fifteen modular surface

Status: authored structural proof; independently mathematically reviewed in REVIEW.md; not formally checked. Work over C. All formulas below hold universally in indeterminate coordinates. No selected actual source point, coefficient matrix, or rank is evaluated.

## Dependencies and distinct ambient spaces

Use PR562 at 86b643fe2adecbd321d1c8f98be84fe2082bcd10 for the actual universal intertwiner phi: Lambda^2 A -> V tensor W and its evaluation-annihilator dictionary. Use PR567 at e0f15a5c6a49d2101dae450dae4d26171a259331 for an integral normalizer-invariant surface component S of D=D9(e), containing all twenty-five distinguished lines. Here e:3Q(-1)->10O on P(A), and dim A=dim V=5, dim W=2.

PR562 identifies an incidence surface in P(V*) times P(W*) with BHM S25. Its first-projection S15 is NOT initially a subscheme of P(A). The construction here defines a separate coordinate-copy T of the BHM degree-fifteen surface in P(A), then proves S=T. No equivariant identification of A with V* is asserted or needed.

In Schrodinger coordinates indexed by Z/5, PR562 gives

F1(p)=sum_i p_(2i) e_(i+2)* wedge e_(i+3)*,
F2(p)=-sum_i p_(2i) e_(i+1)* wedge e_(i+4)*.

Write f+(u)=sum_i u_i e_(i+2)* wedge e_(i+3)* and f-(u)=sum_i u_i e_(i+1)* wedge e_(i+4)*. After the invertible coefficient reindexing u_i=p_(2i), these are F1=f+ and F2=-f-. The GL(W) multiplicity change in PR562 preserves the traceless orbit construction, so these coordinate formulas apply to the actual primary locus.

For k=p tensor epsilon1+q tensor epsilon2, its traceless orbit net has span F1(q), F2(p), F1(p)-F2(q). Consequently, with P_i=p_(2i) and Q_i=q_(2i), the equation e_x*(k)=0 is exactly

 i_x f+(Q)=0,   i_x f-(P)=0,   i_x f+(P)+i_x f-(Q)=0.                 (1)

This equation applies to every k, including tensor rank one. Nonzero k is equivalent to (P,Q) not both zero.

## Universal cyclic kernels on the coordinate torus

Let U={x_0 x_1 x_2 x_3 x_4 !=0} in P(A). For x in U define cubic coefficient vectors

 r_i=x_i x_(i+1) x_(i+4),
 s_i=x_i x_(i+2) x_(i+3).

The coefficient of e_a* in i_x f+(u) is

 u_(a-3) x_(a-1)-u_(a-2) x_(a+1),

up to the harmless simultaneous choice of contraction sign. Thus the kernel equation is u_(i+1)/u_i=x_(i+2)/x_(i+4). Since every x_i is invertible, these equations recursively determine u from one entry; their cyclic product is 1. The displayed r satisfies them. Therefore ker(i_x f+)=C r.

Similarly the coefficient of e_a* in i_x f-(u) is

 u_(a-4) x_(a-3)-u_(a-1) x_(a+3).

The equations link indices by step three, which generates Z/5, so their kernel has dimension one. Direct substitution gives ker(i_x f-)=C s. These statements hold as split rank-four maps over the Laurent coordinate ring, not merely pointwise.

It follows that the first two equations of (1) force Q=a r and P=b s, with scalars a,b. The remaining equation is

 b i_x f+(s)+a i_x f-(r)=0.                                      (2)

## Diagonal pullback and the BHM cubics

Let Delta_x act diagonally on A by Delta_x(e_i)=x_i e_i. Pullback on covectors multiplies e_i* by x_i. Then the definitions give the universal identities

 f+(s)=Delta_x* f+(x),   f-(r)=Delta_x* f-(x).

Here f+(x) and f-(x) mean the same coefficient formulas with coefficient tuple (x_i), not evaluation of phi on a selected source. Naturality of contraction gives

 i_x f+(s)=Delta_x* i_(x^2) f+(x),
 i_x f-(r)=Delta_x* i_(x^2) f-(x),

where x^2 denotes the vector with entries x_i^2.

BHM Section 2.2, displayed definitions on printed page 37, defines h0(x) with entries x_i^2 and cubic vectors v+(x)=-<h0(x),f+(x)>, v-(x)=-<h0(x),f-(x)>. BHM uses bivectors rather than our two-forms. To apply its polynomial identities, use an auxiliary coordinate vector space B with basis b_i, identify b_i with e_i* and b_i* with e_i. Under this coordinate identification, their contraction by h0(x) is exactly our contraction by x^2. Thus the two vectors in (2) are -Delta_x* v+(x) and -Delta_x* v-(x), in the copied coordinate notation.

Delta_x is invertible on U. Therefore a nonzero pair (a,b) satisfying (2) exists if and only if

 v+(x) wedge v-(x)=0.                                           (3)

BHM Section 2.4 Proposition 2 equates (3) to decomposability of a member of its pencil. Section 4.5 Proposition 9 proves that its zero locus T is an integral degree-fifteen surface, the image of S(5) under |I+2F|. Proposition 11 identifies its scheme ideal with the ten components of v+ wedge v-. Hence

 support(D) intersect U = T intersect U.                         (4)

The support equality alone suffices below. One can also eliminate the first two rank-four systems of (1), using invertible monomial pivots, to reduce the dual evaluation matrix to an identity block of size eight, the five-by-two matrix with columns -Delta_x* v+, -Delta_x* v-, and two additional zero rows (fifteen rows in total). Thus the maximal-minor ideal restricts to the ideal of two-by-two minors of (v+,v-), giving scheme equality on U. This does not assert scheme equality on the coordinate boundary.

## Closing the surface identification

The projective linear span of S is invariant under the Heisenberg group, since S is invariant by PR567. Its action on A is irreducible. Consequently S spans P(A), so S is not contained in any coordinate hyperplane. Since S is integral, S intersect U is nonempty and dense in S.

By (4), S intersect U is contained in T. Taking closures gives S subset T. Both S and T are integral surfaces, so S=T. In particular

 degree S = 15.

This proves the exact degree of the line-bearing primary surface. It does not claim the full degeneracy scheme D equals S globally: additional components or scheme structure on the coordinate boundary have not been excluded here. Nor does it establish the original generic section Q4 claim.

## Further geometric consequences with the identification in place

BHM Proposition 9 identifies the normalization with S(5), and Proposition 10 proves that T is smooth away from thirty ordinary transverse double points, each with two smooth surface branches. These statements now apply to S through the coordinate-copy dictionary, rather than by matching numerical invariants. The torus calculation also gives the rank formula dim ker e_x*=2-rank(v+(x),v-(x)) on U; no boundary rank assertion is inferred from it.

Public source: W. Barth, K. Hulek and R. Moore, Shioda's Modular Surface S(5) and the Horrocks-Mumford Bundle, in Vector Bundles on Algebraic Varieties, Sections 2.2, 2.4 Proposition 2, 4.5 Propositions 9-11. https://mathweb.tifr.res.in/Documents/Publications/Studies/Vector-Bundles-On-Algebraic-Varieties.pdf

## Identifying the distinguished lines with the torsion sections

This further consequence uses PR566 at 11642c25ba1b3046e8bc97e3f0e95f077e010375: S is smooth along all twenty-five distinguished lines L, and each has intrinsic normal bundle O(-5). The normalization nu:S(5)->S is therefore an isomorphism near each L. Its strict transform, again denoted L, is a smooth rational curve of self-intersection -5. Adjunction gives K_S(5).L=3.

BHM Section 4.3, printed page 58, explicitly records K_S(5)=3F. Thus F.L=1. Write H=nu*O_S(1)=I+2F using Proposition 9. Since H.L=1, it follows that I.L=-1. By BHM Section 4.3 Lemma 9, 5I is the sum of the twenty-five torsion sections. If L were distinct from each torsion section, intersection positivity on the smooth normalization would imply 5I.L>=0, contradicting -5. Hence L is one of them. Since all twenty-five distinguished lines are distinct, they are exactly the twenty-five torsion sections under normalization.

In particular, on S(5), if C is their sum then

 C=5I,   5H-C=10F.

This last equality is a statement of divisor classes on the normalization. It is not an assertion that every normalized section descends to the nonnormal surface or that an ambient quintic restriction map is surjective.

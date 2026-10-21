# Quadric-freeness of Gamma and the remaining two-torsion gate

## 1. The actual smooth A5 sextic lies on no quadric

Use KAPPA-RATIONAL-SEXTIC.md (3edb50b13b8a5ce876f52a2085ecc8d16b3181c0): Gamma is a smooth nondegenerate rational sextic, with faithful A5 action induced by the irreducible four-dimensional representation on its ambient projective space.

There is at most one quadric containing Gamma. Two independent quadrics either form a degree-four complete intersection, impossible for a sextic, or have a common plane, in which case their intersection is supported on that plane and a line, impossible for an integral nondegenerate curve. Thus any containing quadric is A5-invariant and irreducible.

If it is smooth, Gamma has bidegree (1,5) or (5,1), because its degree is six and its genus is zero. A5 cannot interchange the two rulings, since it has no nontrivial quotient of order two. The degree-one projection identifies Gamma with one ruling base. The other projection is an equivariant map of degree five between projective lines, and the action on its target is faithful: a trivial target action would make the degree-five map factor through the degree-sixty quotient of the faithful source action, impossible; any nontrivial target action is faithful because A5 is simple. Riemann-Hurwitz gives a ramification divisor of degree eight, invariant under the faithful A5 action on the source. But every orbit of this action has size at least twelve. Indeed a point stabilizer in a finite subgroup of PGL2(C) is cyclic, and cyclic subgroups of A5 have order at most five. No invariant effective divisor of degree eight exists.

If the quadric is a cone, its vertex is A5-fixed. It cannot lie on Gamma, since a faithful finite A5 action on P1 has no fixed point. Resolve the cone by the Hirzebruch surface F2, with negative section S and fiber F. The hyperplane pullback is S+2F. The strict transform of Gamma avoids S, so its class aS+bF satisfies b-2a=0; its degree is b=6. It therefore has class 3S+6F. With K_F2=-2S-4F, adjunction gives arithmetic genus four. Because the resolution is an isomorphism along Gamma, its strict transform is a smooth rational curve, a contradiction.

Therefore H0(I_Gamma(2))=0.

## 2. Exact two-torsion obstruction for quartics double at eight marks

Let eight distinct noncoplanar points Z on Gamma admit quadrics Q0,Q1 whose intersection C is integral of arithmetic genus one and smooth at Z, with Q0 smooth. Assume the quadrics through Z form exactly their two-dimensional span. Set

    A=O_C(2)(-Z),

an invertible degree-zero sheaf. It is nontrivial: H0(A) would supply an additional quadric restriction vanishing at Z. Surjectivity H0(P3,O(2))->H0(C,O_C(2)) follows from the complete-intersection resolution, and any such nonzero restriction would be an additional quadric through Z.

Suppose further A^2 is nontrivial. Then no integral quartic surface D can have multiplicity at least two at every point of Z.

Indeed D|C is a section of A^2 and must be zero, since a nontrivial degree-zero invertible sheaf on an integral projective curve has no nonzero section. Thus D contains C. Its conormal class in (I_C/I_C^2)(4) is a pair of sections of O_C(2). At each smooth marked point, multiplicity at least two forces both sections to vanish, so they lie in H0(A)=0. Hence D belongs to I_C^2 scheme-theoretically. The complete-intersection square has resolution 0->O(-6)^2->O(-4)^3->I_C^2->0, so its degree-four global sections are precisely the span of Q0^2,Q0Q1,Q1^2. Every binary quadratic over C factors, so the quartic is reducible or nonreduced, contradicting integrality.

Thus the remaining degree-four image would force A to be a nontrivial two-torsion line bundle for each suitable eight-subset of its ten double marks. This is stronger than merely requiring an elliptic pencil, but the required generic avoidance of this torsion condition has NOT been established here.

## 3. Precise unresolved issue

Fixing seven general Gamma points gives a net of quadrics whose complete-intersection base is a Cayley octad when it is reduced. For an eighth moving point p, the elliptic fiber C_p contains the fixed seven plus the additional fixed basepoint b, and A_p=O_Cp(b-p). The exceptional condition is that p-b is a nonzero two-torsion point in its elliptic fiber. This interpretation alone does not show that Gamma avoids the resulting surface. It would be invalid to invoke interpolation for eight general points of P3 in place of the actual points on Gamma.

The new checked deduction is quadric-freeness and the exact two-torsion criterion. No generic torsion avoidance, degree-four exclusion, selected coefficient evaluation, or complete repair is claimed.

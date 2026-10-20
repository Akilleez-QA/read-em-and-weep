# Binary-quartic normalization prerequisite

Work over C. Identify Y=P⁴ with the projective space of binary quartics, and let N be the reduced image of f:P¹×P¹→Y, (l,m)↦l³m. Here l and m are binary linear forms up to scale. The coefficient sections have bidegree (3,1) and no common zero, so f*O_Y(1)=O(3,1). The following local normalization argument supplies the finiteness needed for the inverse-image affine Čech cover. It does not import any conductor, Gysin, or source-obstruction assertion.

## 1. An exact local ring at every collision

Choose an affine root coordinate x on P¹ such that neither root is at infinity. This is possible near every point of S after a common projective change of coordinate. The corresponding quartic can be uniquely normalized to be monic:

    (x-a)³(x-b).

Put s=(3a+b)/4 and d=b-a, so a=s-d/4 and b=s+3d/4. For z=x-s, the polynomial identity is

    (z+d/4)³(z-3d/4)
      = z⁴ -(3/8)d²z² -(1/8)d³z -(3/256)d⁴.

The x³ coefficient recovers s. The centered x² and x coefficients recover nonzero scalar multiples of d² and d³. Conversely all four monic coefficients are in C[s,d²,d³]. Since N is the reduced image, its coordinate algebra on this chart is exactly

    A=C[s,d²,d³] ≅ C[s,u,v]/(v²-u³),
    R=C[s,d],  u=d², v=d³.                        (5)

This is an equality of coordinate algebras, not only of formal or generic local models. Indeed the parametrization of this affine chart is surjective on geometric points; the kernel of the coefficient map defines its reduced closed image, and that image is N in the monic chart.

R is finite over A, generated as an A-module by 1,d. The fraction fields agree, because d=v/u away from u=0. R is normal, so it is the normalization of A. These affine charts cover N, proving the global normalization claim.

If d≠0, A localized at u equals R localized at d; N is smooth there. At every quadruple root d=0, the transverse singularity is an ordinary cusp, with the free coordinate s along C. In particular there is no exceptional higher cusp at a special quadruple root. All such points admit the same exact product model. This differs from the several triple-diagonal components upstairs in (P¹)⁴: N itself is unibranch along C.

For precision, the reduced singular locus is C=(u,v). The Jacobian singular subscheme in the cusp chart has ideal (u²,v), since the equation is v²-u³. Its nonreduced structure is not the conductor ideal. The conductor is computed next.


# Independent derivation of the finite-dual presentation

This checks the proposed abstract-module calculation directly from the previously reviewed candidate, with λ≠0, λ⁴≠1 and ε²=1. It does not assume an isolated reflexive realization.

## Socle and dual generators

The candidate has graded pieces (4,6,4,2). Its degree-two basis is F_j and x_i F_j is zero unless i=j, when the result is G_j≠0. Thus there is no degree-two socle. The six degree-one B-weight lines consist of four nonzero-clock lines represented by x_jt_j and an opposite clock pair represented by x_it_(−i). Multiplication by x_(−j) sends the former to −εF_(−j)≠0, and multiplication by x_i sends the latter to F_(−i)≠0. Their B-weights are distinct, so the kernel of all parameters cannot contain any nonzero degree-one vector. Similarly each top weight line has a nonzero linear product. The socle is graded; it is therefore exactly the two-dimensional degree-three piece, spanned by G1,G2 with G4=−εG1 and G3=−εG2.

The finite dual is the vector-space dual with the canonical determinant-line factor, not the uncorrected equivariant vector-space dual. Normalize its grading so functionals dual to G1,G2 have degree zero. Denote them q1,q2, suppressing but retaining their common determinant-line factor. Nakayama's lemma, or the perfect pairing between its top and soc(P), proves these two elements generate the finite dual.

Since only x_jF_j is nonzero, the four linear relations are x2q1=x3q1=x1q2=x4q2=0.

## Cubic relations and signs

Cubic functionals are determined by their values on the four top vectors t_j. From the original normal forms, the only nonzero cubic monomials on t_j are x_jx_(−j)²t_j=G_j and x_(3j)³t_j=−(ε/λ)G_(3j). Therefore:

- x1³q1 and x2x3²q2 are supported only on t2, with values −ε/λ and 1.
- x1²x4q1 and x2³q2 are supported only on t4, with values −ε and −ε/λ.
- x1x4²q1 and x3³q2 are supported only on t1, with values 1 and 1/λ.
- x4³q1 and x2²x3q2 are supported only on t3, with values 1/λ and −ε.

These verify exactly the four proposed relations:

    x1³q1+(ε/λ)x2x3²q2=0,
    x1²x4q1−λx2³q2=0,
    x1x4²q1−λx3³q2=0,
    x4³q1+(ε/λ)x2²x3q2=0.

After the linear relations, the presentation is the direct sum of two polynomial planes, C[x1,x4]q1 and C[x2,x3]q2. The four cubic relations pair their complete cubic monomial bases by invertible coefficients. They are independent and leave a four-dimensional cubic quotient. Multiplication by a variable from one plane kills the term from the other plane, and consequently kills all quartic monomials in both planes. All higher pieces vanish. The resulting Hilbert function is (2,4,6,4), hence the quotient has length sixteen. Its surjection onto the normalized finite dual of the same length is an isomorphism. This proves the full presentation, not only necessary relations.

The four linear and four cubic relations are minimal: they are independent in their respective degrees after dividing by lower-degree relations, and no quadratic relation remains in the direct sum of polynomial planes.

## Betti table

Use standard graded S with four variables, or its completion with the associated grading. The candidate P has F0=S⁴ and F1=S(−1)^10 by its exact minimal presentation. Finite graded duality, retaining the equivariant canonical line, reverses the resolution. The normalized dual's two degree-zero generators and four linear/four cubic minimal relations imply

    F4(P)=S(−7)^2,
    F3(P)=S(−4)^4 ⊕ S(−6)^4.

The shift seven is four plus the socle degree three. The Hilbert numerator is

    (4+6t+4t²+2t³)(1−t)^4
      =4−10t+4t²+6t³−4t⁴+2t⁵−4t⁶+2t⁷.

Subtracting the already determined even/odd free terms determines

    F2(P)=S(−2)^4 ⊕ S(−3)^6 ⊕ S(−5)^2.

Thus the total Betti numbers are (4,10,12,8,2). This is a structural symbolic calculation of the abstract family. It asserts neither an actual geometric defect nor a new first-order, higher-order, or algebraicity statement.

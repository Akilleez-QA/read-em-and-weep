# Ten-root dominance for the 25 Heisenberg lines

## Result and conventions

For the actual 25 Heisenberg lines in P^4, every ten-mark pattern with at most two marks on each line is independently dominant onto Gamma^10 EXCEPT the thirty patterns consisting of both roots on each of the five lines in one configuration hyperplane. Each exceptional pattern has a nine-dimensional image, of codimension one in Gamma^10. This is a symbolic configuration result, not a selected-quadric evaluation.

Use indices in F_5, a primitive fifth root zeta, the coordinate shift and diagonal Heisenberg operators, and L_00=span(e_1-e_4,e_2-e_3). Write L_ab as the shift by a of the diagonal-by-b translate of L_00. These are the source lines already identified with the evaluation configuration. Coordinate-copy or dual conventions replace signs and primitive powers and do not change the assertions.

## 1. All hyperplanes containing two configuration lines

A hyperplane sum c_i x_i=0 contains L_ab precisely when

    c_(a+1)=zeta^(-2b)c_(a-1),
    c_(a+2)=zeta^(-4b)c_(a-2).

If it contains two lines with the same a and different b, all coefficients except c_a vanish. Thus it is the coordinate hyperplane x_a=0, containing exactly the five L_ab for that a.

Suppose it contains lines with two different centers a,a'. The support of (c_i) is invariant under the reflections i -> 2a-i and i -> 2a'-i, by the displayed equations. Their composition is a nonzero translation of F_5, hence acts transitively. The nonempty support is therefore all five indices. The coefficient ratios along those reflection edges are fifth roots of unity; the graph is connected, so after rescaling c_i=zeta^(r(i)) for a function r:F_5 -> F_5.

Write r uniquely as a polynomial r_0+r_1 i+r_2 i^2+r_3 i^3+r_4 i^4 over F_5. Eliminating b from the displayed conditions gives

    r(a+2)-r(a-2)=2(r(a+1)-r(a-1)).

Expanding gives 2(r_3+4a r_4)=0 in F_5. Two different centers therefore force r_3=r_4=0. Conversely every coefficient vector c_i=zeta^(A i^2+B i), up to scale, contains exactly one L_ab for each a, with b determined by the first relation. There are 25 such hyperplanes.

Thus the only hyperplanes containing two or more configuration lines are the five coordinate hyperplanes and these 25 quadratic-phase hyperplanes. Each contains exactly five lines. Every pair of lines determines its unique P^3 span, so this is also the complete block classification.

## 2. None of the five-line blocks lies on a quadric surface

The five lines in x_0=0 are parametrized, with r running through the fifth roots of unity, by

    (x_1,x_2,x_3,x_4)=(u,v,-r^2 v,-r u).

If a quadratic form vanishes on all five, its u^2 coefficient is a polynomial in r with exponents 0,1,2; its v^2 coefficient has exponents 0,2,4; its uv coefficient has exponents 0,1,2,3. Each has degree at most four and vanishes at all five fifth roots. Each is zero, and their ten coefficients are exactly the ten coefficients of the quadratic form. Hence there is no nonzero quadric through the block.

The same assertion holds for every quadratic-phase block by an explicit configuration-preserving coordinate change. Diagonal chirps e_i -> zeta^(A i^2)e_i conjugate a shifted Heisenberg reflection to another such reflection and commute with the central reflection e_i -> e_-i. The discrete Fourier transform exchanges the shift and diagonal generators and also commutes with that central reflection. They therefore preserve the orbit of its two-dimensional negative eigenspace L_00, namely the 25 lines. On dual hyperplane coefficients, a suitable chirp removes the quadratic phase, and a suitable Fourier transform sends the remaining vector (zeta^(B i))_i to a coordinate vector. Thus every block is transported to a coordinate block. Signs depend only on whether the coordinate change is applied on vectors or covectors, and both inverse changes preserve the same configuration.

## 3. The universal rank-nine exception for skew lines

Recall that any three skew lines impose nine independent conditions on quadrics. If those three lie in a P^3 H, their common ambient quadratic base locus is the smooth quadric surface in H containing them: the ambient ideal includes ell_H times every linear form, and the unique quadric in H containing the three skew lines. Any further line whose Veronese span adds no dimension must lie on that surface.

If the three lines span P^4, their common quadratic base locus is the three lines plus their unique common transversal. Here is a direct verification. Let H span the first two lines, let p=L_3 intersect H, and use complementary coordinates u,v on H. Quadrics ell_H times linear forms vanishing on L_3 force the base locus into H union L_3. Restrictions to H of the remaining quadrics are exactly the bilinear forms u_a v_b vanishing at p. Their common zeros are L_1 union L_2 and the line joining [u(p),0] to [0,v(p)], the unique transversal through p. No fourth line skew to the first three is contained in this base locus.

It follows that a collection of at least four skew lines has quadratic evaluation rank nine exactly when all its lines lie in one ruling of a smooth quadric surface in a P^3. Otherwise its rank is at least ten.

For five or more HM lines that exception is impossible: all would lie in one hyperplane, so Section 1 places them in one five-line block, and Section 2 excludes a quadric through the block. Therefore every collection of at least five HM lines has quadratic evaluation rank at least ten.

## 4. The rank-eleven refinement

Four skew lines spanning P^4 impose at least eleven independent conditions on quadrics. Choose three among them spanning P^4 (otherwise every triple lies in the P^3 spanned by the first two, hence all four lie there). Their common quadratic base locus was described above. Along the transversal away from its intersections with the original lines, this base locus is scheme-theoretically reduced: a generator ell_H times a linear form nonzero there supplies the transverse equation ell_H, while the bilinear forms vanishing at p cut out the transversal reducedly inside H. Indeed the Segre map [u,v] -> [u tensor v] has exactly this line as its fiber and is a submersion away from the two coordinate lines.

The fourth line avoids all three original lines, and can meet the transversal in at most one point. At such a point its intersection with that reduced linear base locus has length one. Thus the base scheme of the restricted quadratic system on the fourth line has length at most one. That system cannot have dimension one: a one-dimensional nonzero space of degree-two sections on P^1 has base divisor of length two. It therefore has dimension at least two, increasing the previous rank nine to at least eleven.

Consequently a set of at least five HM lines has quadratic rank at least eleven unless it consists exactly of one five-line hyperplane block. Indeed a set not contained in a hyperplane contains four spanning P^4; a set in a hyperplane is contained in a five-line block. The exceptional block has quadratic rank exactly ten by Section 2.

## 5. All nonexceptional ten-mark patterns dominate

First assign at most two slots to each line, total ten. The linear Hall inequalities hold: one line has span dimension three, two have six, three or four have at least nine (and contribute at most six or eight slots), and five or more have at least ten. The independent-transversal proof and multilinear specialization from EIGHT-ROOT-POSITION-DOMINANCE.md show that generic selected points impose ten independent conditions.

Now append an eleventh slot on any specified source line. There is at most one line with three slots. For any subset supported on at most four lines its slot count is at most nine, and the preceding dimensions suffice (one line has at most three slots; two at most five; three at most seven). A subset with ten slots supported on a hyperplane block still satisfies rank ten. The only potential failure is all eleven slots supported on a five-line hyperplane block. That occurs precisely when the original ten slots were both slots on all five lines of that block. For any other original pattern, all eleven slots satisfy Hall, by the rank-eleven refinement.

Thus, for a nonexceptional pattern, generic quadrics through the ten points do not contain any source line: use independence after adjoining a generic additional point on that line. Simultaneously avoiding the finitely many line-containment conditions is a nonempty open condition in the projective P^4 of quadrics through the ten points. The independent-point incidence therefore has dimension ten plus four, and its projection to source P^14 is generically finite and dominant. As in the eight-root proof, distinct irreducible discriminant divisors give an irreducible ordered-root cover. Hence the actual cover dominates the full tenfold product of line parameters, and therefore Gamma^10. No extra generic component with special positions is ignored.

## 6. The thirty exceptional patterns have image dimension nine

Let H be a configuration hyperplane containing its five-line block, and select both roots on each line. Every source quadric not containing H restricts to a nonzero quadric in H through all ten points. Independently general ten positions on the block impose ten independent conditions on H-quadrics, by Section 2 and Hall. Therefore actual root positions cannot be independently general: they belong to the proper determinant locus for the ten-point evaluation map on the ten-dimensional space H^0(H,O_H(2)).

Their image has dimension exactly nine. To see this, select nine independent generic positions with multiplicities (2,2,2,2,1). They impose nine independent conditions on H-quadrics by Hall, leaving a unique projective quadric. It does not contain any block line generically: adjoining a tenth point on any line satisfies Hall, with at most one triple slot and at most five distinct lines, and full-block rank ten. The nine-point incidence is thus nine-dimensional and maps generically finitely and dominantly to the P^9 of H-quadrics. For general H-quadric, those nine positions are independent, so its ten roots determine that H-quadric uniquely. The full ten-root image consequently has dimension nine.

Restriction of source quadrics to H is onto, so no further source restriction changes this image. The same dimension and codimension conclusions hold after the fixed kappa identifications with Gamma.

## Scope

This classifies the exact failure of ten-root independence, not the existence of a quartic surface double at those ten kappa images. For nonexceptional patterns, one may test a nonempty open condition on Gamma^10 independently. The thirty exceptional codimension-one root-position families require a separate argument. In particular the exceptional pattern is a five-line hyperplane block, NOT five lines contained in a quadric ruling: the block itself lies on no quadric, while its actual ten root points necessarily do.

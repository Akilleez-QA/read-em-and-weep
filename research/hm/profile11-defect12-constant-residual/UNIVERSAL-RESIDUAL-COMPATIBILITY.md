# An abstract equivariant family realizes the surviving residual data

This is an abstract universal construction, not an actual HM or source-instance realization. It selects no actual coefficients, parameter values, points, derivative values, matrices or ranks. It explains why the residual conclusion in Section7 of PROOF.md is not itself a contradiction.

Let Hbar=A+V+P+D. The universal binary-icosahedral identities are

    Sym10 W=A+V+D,       Sym8 W=P+D.

Consider all equivariant coefficient maps

    a:Sym10 W -> Hbar,
    b:Sym8 W -> Hbar

whose A,V channels in a and P channel in b are nonzero, and for which at least one of the two D channels is nonzero. These conditions define the family; no member is selected. Let f:O(-10)->Hbar O and g:O(-8)->Hbar O be the corresponding line systems. Put

    Z=image(first-polar map of f) + image(g).

Then every member of this family has

    Z=W O(-9)+O(-8),
    Z^-=O(-10),
    Z/Z^-=2 O(-8),

and its derivative image is saturated. Moreover Z is saturated in Hbar O and spans Hbar.

## Universal jet bounds

A G-stable dimension-(r+1) linear system in H0(O(d)) has invariant Wronskian divisor of degree

    (r+1)(d-r).

Indeed the Wronskian is the determinant of the jet-evaluation map to the rank-(r+1) principal-parts bundle. That bundle has the jet-filtration factors O(d),O(d-2),...,O(d-2r), so its determinant has the stated degree. The determinant is nonzero in characteristic zero: for independent polynomials, choose a basis with distinct leading degrees; the highest-degree coefficient of their derivative determinant is a nonzero Vandermonde factor. At a point with vanishing sequence a0<...<ar the vanishing order is sum_i(a_i-i).

The A+V subsystem of H0(O(10)) has dimension six. It is basepoint-free, because a common invariant zero divisor would have degree at least twelve, exceeding ten. Its Wronskian degree is6(10-5)=30. Failure of full second jets means a2>=3, hence a_i-i>=1 for i=2,3,4,5 and weight at least four. Failure at any point would occur on a projective orbit of at least twelve points, contributing at least48 to a degree30 divisor. Therefore its second jets have rank three everywhere.

The P subsystem of H0(O(8)) has dimension four and is likewise basepoint-free. Its Wronskian degree is4(8-3)=20. Failure of full first jets means a1>=2 and weight at least three. Its invariant orbit would contribute at least36, impossible. Therefore its first jets have rank two everywhere.

These are universal linear-system arguments, not rank tests on a selected coefficient map or point.

## Actual subbundles of the abstract family

The projection of the first-polar map W O(-9)->Hbar O to A+V has rank two everywhere by the first jet bound. Hence it is a saturated embedding, with image F1=W O(-9). The original line f is its tautological subline O(-10), and F1/f=O(-8).

The g line has everywhere nonzero P projection, whereas F1 has zero P projection. Consequently their sum is a saturated direct-sum embedding

    Z=F1 direct-sum O(-8)g.

The derivative of Z kills the f line. Modulo Z, the derivative of F1/f is everywhere nonzero by the second-jet bound in A+V, while the derivative of g is independent of it by the first-jet bound in P. Thus the induced derivative

    Z/f=O(-8)+O(-8) -> (Hbar O/Z)(-2)

has rank two at every point. Its image is saturated, proving all the kernel and quotient statements.

Finally the constant span is G-invariant. It contains A and V through the f channels, P through the g channel, and D through at least one of the two D channels. The four irreducibles are pairwise nonisomorphic and occur with multiplicity one in Hbar, so the span is Hbar.

This construction does not extend Z to the original rank17 E, prove its compatibility with the actual multiplication pencil, or realize the whole Gauss label. It establishes only that the precise residual data alone admit universal abstract realizations and cannot support a contradiction without an additional actual-source constraint.

# A one-dimensional beta image forces nonnormal general surfaces

## Statement

Assume the residual beta assignment f:dual P4⇢P(U*) has one-dimensional image. Then its general fixed-beta surface X_B cannot be normal. After the residual degree-five exclusion, X_B is already known to be reduced integral of degree fifteen; the conclusion here removes the normal case for this one-dimensional-image alternative.

No canonical-singularity assumption is needed. The proof uses the previously established negative adjunction degree on a smooth neighborhood of D, the algebraic beta family, H5 invariance of f, and irreducibility of the five-dimensional coordinate representation.

## 1. General fixed-B fibers must be hyperplanes if X_B is normal

Suppose X_B is normal for general B in the image curve. A normal surface over C has a finite singular locus. A general irreducible component T of an f-fiber has dimension three. It parametrizes distinct sextics D_H on the fixed X_B: each integral nonplanar sextic spans and determines H. Shrinking T gives a flat algebraic family.

A general D_H cannot avoid Sing(X_B). Otherwise it lies entirely in the smooth locus; as a Cartier curve there, the established adjunction computation gives deg N_{D_H/X_B}=4−25=−21, so H0(N)=0. Its Hilbert point would be isolated, contradicting the positive-dimensional family through a general member. Notice that this uses smoothness only near D_H, not global smoothness of X_B.

For each general H∈T, therefore, D_H contains some p∈Sing(X_B). Since D_H⊂H, such H belongs to the hyperplane p^⊥ in dual P4. The finite singular set gives finitely many such hyperplanes covering a dense subset of T. Irreducibility forces the closure of T into one of them. Both have dimension three, so the closure of T is that hyperplane.

Thus all general fiber components of f have hyperplane closures.

## 2. Passing to the connected-fiber curve gives a linear pencil

Normalize the image curve, resolve the rational map f, and take its Stein factorization. Equivalently, take the relative algebraic closure K of the image curve's function field in C(dual P4). It is the function field of a smooth projective curve Γ, and produces a rational map g:dual P4⇢Γ with geometrically integral generic fiber in characteristic zero, followed by a finite map Γ→normalization(image f).

The curve Γ is rational. Indeed a general line in dual P4 on which g is nonconstant gives a dominant rational map P1⇢Γ; a complex curve dominated by P1 has genus zero. Therefore identify Γ with P1.

Write g=[F:G] with coprime homogeneous polynomials F,G of the same positive degree m. Its general fiber is the hypersurface F−tG=0 away from the base locus. There are no fixed divisorial base components because F and G are coprime. The geometrically integral generic fiber is reduced, and by Section 1 its closure is a hyperplane. Therefore m=1. In particular g is a linear pencil and W=span(F,G) is a two-dimensional subspace of the space of linear coordinate forms on dual P4.

## 3. Heisenberg symmetry excludes that pencil

The beta assignment f is H5-invariant because H5 acts trivially on U and the assignment is intrinsic. Thus the H5 action on C(dual P4) fixes the image function field and preserves its relative algebraic closure K. Consequently it induces an action on Γ and permutes the fibers of g. The pencil of hyperplanes is therefore invariant, so W is an H5-stable two-dimensional subspace of the five-dimensional linear coordinate representation (or its dual, depending on convention).

Both versions are irreducible Schrödinger representations. Such a subspace cannot exist. This contradiction proves that a one-dimensional beta image cannot have general normal X_B.

## 4. The image is not a point

If B were constant for general H, all D_H would lie in one fixed reduced integral degree-fifteen surface X_B. Bertini gives an integral degree-fifteen general hyperplane section X_B intersect H. It cannot contain the integral degree-six D_H: an integral curve has no proper closed subcurve of the same dimension. Thus the constant-image case is impossible. Combined with the earlier dimension drop, the remaining image dimensions are exactly one or two; this does not assert that either occurs.

## Boundary

This does not exclude a one-dimensional image whose general integral degree-fifteen surfaces are nonnormal, nor the two-dimensional-image alternative. Finite singular locus is essential to Section 1 and must not be asserted for a nonnormal surface. The zero-dimensional-image case is excluded in Section 4. No selected coefficients, matrix ranks, scans, or prohibited experiments were used.

Public input pins in PR543: integral-surface conclusion3714d276821366f9b1230abb6cc60b81861bb878; negative-adjunction and dimension-drop f5b50172bd65d1772d1af3d4a511decc8363183e; beta active-point filtration d755d22d3bf460fe314dd846bda1e893d682b71c.


# Why the codimension bound does not imply rank-nine transversality

## Scope and dependencies

This is an abstract counterexample to a proposed inference, not a counterexample about the Horrocks–Mumford representation. The relevant established results are PR555 at ff5a3164337016e96e3a29a9ad37891130a66e29 and PR556 at 0fbd687207401fe715aa6aff2e22ee8a8de4081b. They do not assert that the rank-nine locus is reduced. Nothing here evaluates selected HM/source coefficients or matrices.

## Linear determinantal example

Over R=C[x,y,u,v], consider the 5-by-3 matrix

    T = [1 0 x]
        [0 1 y]
        [x 0 0]
        [y 0 0]
        [0 y 0].

Subtract x times row 1 from row 3, y times row 1 from row 4, and y times row 2 from row 5. Next subtract x times column 1 and y times column 2 from column 3. These invertible operations give

    T ~ [1 0 0]
        [0 1 0]
        [0 0 -x^2]
        [0 0 -xy]
        [0 0 -y^2].

Consequently its maximal-minor ideal is exactly (x^2,xy,y^2)=(x,y)^2. In particular:

- T has generic rank three, rank two precisely on the reduced surface x=y=0, and no smaller rank.
- The maximal minors have no nonconstant common divisor.
- The determinantal scheme is nonreduced along this entire surface.
- At every point of the surface, the intrinsic first-order derivative from the kernel to the cokernel is zero: in the pivot normal form its entries are the derivatives of x^2,xy,y^2, all zero there.

Adding a 7-by-7 identity block gives a 12-by-10 matrix with generic rank ten, rank nine along the same surface, no smaller ranks, no maximal-minor common divisor, and identically zero residual derivative along the rank-nine surface. All entries before row operations have degree at most one. For a projective version replace every constant 1 in the original matrix and identity block by z; the affine chart z=1 has precisely the behavior above. No global claim about the hyperplane z=0 is needed.

## Consequence for the research route

Linearity of the original matrix, a codimension-at-least-two rank-drop locus, and absence of a maximal-minor gcd do not imply generic nonvanishing of the residual derivative. A proof for the HM incidence must use additional special structure, or independently establish generic reducedness/transversality of its rank-nine locus. This example does not contradict normality of that incidence and does not determine its rank-nine locus.

## Verification

The displayed elementary operations are an exact symbolic verification. In normal form every nonzero maximal minor is one of the three last-column entries, and each entry occurs as such a minor. The kernel on x=y=0 is the third coordinate line; the quotient by the first two rows identifies the cokernel with the last three coordinates. These identifications directly give the zero derivative. No numerical computation or formal proof assistant was used.

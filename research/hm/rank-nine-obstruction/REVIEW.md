# Independent review of the abstract rank-nine obstruction

Verdict: the displayed mathematical construction and its stated local consequence are sound.

Reviewed file: `OBSTRUCTION.md`, SHA-256
`8d20269ba30d3a1b3359897133ecc9ea6924422949e2360db82a44ab820dd195`.

## Exact operations and ideal

After the three indicated row operations, rows 3, 4, and 5 are respectively
`(0,0,-x^2)`, `(0,0,-xy)`, and `(0,0,-y^2)`. The first two rows remain
`(1,0,x)` and `(0,1,y)`. The stated operation on column 3 removes their last
entries and leaves the other rows unchanged. Each operation is elementary
and invertible over C[x,y,u,v], so it preserves the ideal of maximal minors.

In the resulting matrix, a nonzero three-row minor must select rows 1 and 2
and one of rows 3, 4, 5. These three choices give exactly -x^2, -xy, and -y^2.
Thus the maximal-minor ideal is exactly (x,y)^2, not merely an ideal with the
same radical.

The fixed identity pivot gives rank at least two everywhere. The rank is
three away from x=y=0 and two on that plane. Its reduced support is a
codimension-two surface in affine four-space. The ideal is nonradical at
every point of the surface: the local class of x is nonzero, while its square
is zero. Since x^2 and y^2 are relatively prime in the polynomial UFD, the
maximal minors have no nonconstant common divisor.

## Intrinsic derivative

At a point of the surface the kernel is the third coordinate line and the
cokernel is represented by the last three coordinates. The induced derivative
is therefore the derivative of (-x^2,-xy,-y^2), which is zero in every tangent
direction, including the u and v directions. This computation is invariant
under the variable-dependent invertible row and column operations: terms
arising from differentiating those operations either annihilate the kernel
or lie in the image and vanish on passage to the cokernel. Thus it is the
intrinsic kernel-to-cokernel derivative that vanishes, not merely a chosen
coordinate artifact.

## Identity stabilization and projective scope

For diag(I7,T), every nonzero ten-row maximal minor must use all seven identity
rows; its remaining factor is one of the three-row minors of T. The ideal
remains (x,y)^2. Ranks increase by seven, giving generic rank ten, rank nine
exactly on the surface, and no smaller rank. Kernel, cokernel, and their
induced derivative retain the preceding descriptions.

Replacing the constant ones by z gives a homogeneous linear 12-by-10 matrix
on projective four-space with coordinates [x:y:u:v:z]. In the standard chart
z≠0, trivializing and dividing the coordinates by z yields exactly the
affine construction. The file correctly confines its claim to that chart.
It does not establish a globally gcd-free projective example: the zI7 block
in fact forces a common z^7 factor in every potentially nonzero global
maximal minor. This does not affect the stated chart-local obstruction.

## Scope of the verdict

The example disproves the universal inference from affine linear entries,
codimension-two rank drop, and gcd-free maximal minors to a generically
nonzero residual derivative. It is not an actual Horrocks–Mumford example,
does not settle the HM rank-nine locus, and makes no claim about normality of
the HM incidence. The cited repository dependencies were not independently
re-audited in this review. Verification here is an independent exact
mathematical calculation, not a proof-assistant check or an evaluation of
selected actual HM/source instances.

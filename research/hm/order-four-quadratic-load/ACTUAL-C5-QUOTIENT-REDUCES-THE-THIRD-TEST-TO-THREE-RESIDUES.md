# The actual C5 quotient reduces the third test to three residues

## Exact result and companion status

Fix an ARBITRARY order-five stabilizer and its two fixed points x,y on the negative line L. Use the detectable square/h channel of ACTUAL-C5-SQUARE-CORRECTION-HAS-A-SIMPLE-ROOT.md. The actual genus-four cubic support D has rational quotient by this C5. The induced degree-three map

    D/C5 -> L/C5

has four simple branch values. Two are the images of x,y. The other two correspond precisely to the two free C5 orbits of the remaining ten polar points.

There are abstract quotient coordinates z,V, obtained by rescaling eigenlines without assigning any actual source coefficient, in which the degree-three map is

    V=(z+1)/(z^2(z-1)).                                  (1)

Its two ordinary critical points satisfy z^2+z-1=0 and their distinct critical values satisfy

    V^2+11V-1=0.                                        (2)

These are universal identities for the entire symplectic C5 tensor geometry, not an actual-instance coefficient model or a rank computation.

Pair the actual polar representative with its actual final Serre test. Let b_y be the full resulting scalar residue at y, proved nonzero in the C5 correction theorem. Let b_+,b_- be the scalar residues at any representative of the other two C5 orbits. Then the EXACT remaining square-third criterion is

    b_y+5b_++5b_- != 0.                                 (3)

No separate value of b_+ or b_- is asserted here. The quotient argument alone does not settle(3). The companion ACTUAL-THIRD-BOCKSTEIN-VANISHES-ON-SQUARE-DIRECTIONS.md now proves, using the exact meromorphic-source comparison and complete two-chart cochain, that b_y+5b_++5b_-=0. Thus the two unknown orbit contributions cancel the known opposite residue. This does not license an advance use of the global residue theorem on unglued local data. The discriminant-divisible cubic channel remains open at this package cutoff.

## 1. The rational quotient is actual

Use arbitrary stabilizer eigenvectors with the conventions of the C5 correction theorem. The actual cubic is a nonzero intertwiner of the two irreducible cubic four-spaces, so all four allowed eigenspace maps are nonzero. In formal tensor notation it is

    f=A X^2Y s^3+B Y^3 s^2t+C X^3 st^2+D XY^2 t^3,
    AD+BC=0.

The letters denote arbitrary nonzero maps between eigenspace lines. The relation is forced by the invariant alternating cubic apolar forms. No one of these maps is given a chosen actual value.

On the open torus put w=t/s and v=Y/X. A generator of C5 acts with weights1,2 on w,v. Hence

    u=v/w^2,    w^5

are invariant. Dividing the cubic equation by X^3 s^3 and substituting v=u w^2 gives

    A u+C+w^5 u^2(Bu+D)=0.

Thus

    w^5=-(A u+C)/(u^2(Bu+D)).                           (4)

The function field extension over C(u) has degree five: its right-hand side has zeros or poles of orders1 and2, so it is not a fifth power. Therefore C(D)^C5=C(u). This proves that the quotient is P1, not just that a rational invariant function exists.

Equivalently, the four fixed corners on D have full cyclic stabilizer, and Riemann--Hurwitz gives 6=5(-2)+4*4. Both arguments refer to the actual smooth integral D.

Set z=A u/C and rescale the target quotient coordinate by

    V=-(B C^2/A^3) w^5.

Equation(4), together with AD+BC=0, becomes(1). These are isomorphisms of the abstract quotient lines; they do not normalize a numerical HM instance.

The cyclic-five cover D->D/C5 has its four branch points at z=-1,infinity,0,1, with orders1,2,-2,-1 in(4). The branch set is therefore harmonic. The normalization has genus four, in agreement with the established actual support theorem.

## 2. Identify the two remaining polar orbits

The derivative of(1) is

    dV/dz=-2(z^2+z-1)/(z^3(z-1)^2).

The points z=0 and infinity have local degree two and map to V=infinity and0 respectively. The other two critical points are the distinct roots of z^2+z-1. At such a root,

    V=(z+1)/(3z-2),

and elimination gives(2). Neither critical value is0 or infinity, and the two values are distinct.

The actual degree-three projection D->L has a reduced twelve-point ramification orbit which maps bijectively to the polar orbit E. Passing to the cyclic quotients preserves its two free C5 orbits. At the four corners the degree-five quotient ramification on D and L cancels in the ramification-index formula; the double corners give the two exceptional critical values0,infinity. Hence the other critical values in(2) are exactly the images in L/C5 of the remaining two polar orbits. There is no selected point evaluation in this identification.

## 3. Descend principal parts, not an unproved global differential

Let c_a be a nonzero covector annihilating the actual second-symbol image. For the square a rooted at x this line is one-dimensional. The final scalar test is the Serre pairing with

    zeta=a i^t c_a in H0(V O_L(4)).

At each polar point pair the actual physical vector principal part R/nu with zeta. This yields a principal part of a meromorphic DIFFERENTIAL. The derivative correction from double poles and the physical nu factor is exactly the one in the published polar residue theorem.

These scalar differential principal parts are C5-invariant in the detectable channel: the cubic a factor contributes weight6, h contributes weight2, and c_a contributes weight2, totaling zero modulo ten. Thus the residues at the five points of either free orbit agree. The full R is regular at x, so its scalar differential principal part there is zero. At y its simple residue b_y is nonzero by the oriented C5 theorem and the nonzero final local pairing.

Invariant local differential principal parts descend to the quotient curve L/C5. At a free orbit the residue is unchanged. At a fixed branch point the quotient parameter is a fifth power: dw/w=(1/5)d(w^5)/(w^5). Thus the descended residue at the image of y is b_y/5. At x regular invariant differentials descend regularly. The descended data have precisely three possible residue locations, and their residue sum is

    b_y/5+b_++b_-.

The upstairs Serre sum is five times this number, proving(3). Higher principal-part orders at the two free orbits do not change this residue identity; their contribution has already been included in pairing with zeta.

Crucially, these are DESCENDED LOCAL PRINCIPAL PARTS. No single global meromorphic differential with these principal parts has been constructed. On P1 such a differential exists exactly when their residue sum is zero. Applying the global residue theorem before proving that gluing would assume the very vanishing under investigation.

## Scope and verification

The proof identifies the actual global quotient geometry and the exact two-orbit cancellation condition after the nonzero opposite residue; the companion square-vanishing theorem establishes that condition by a different global source calculation. It does not evaluate either unknown orbit contribution, infer nonzero cohomology from a nonzero local residue, or claim the original proof repair is complete.

Dependencies: ACTUAL-CUBIC-SUPPORT-IS-GENUS-FOUR-WITH-EXACT-FIVE-TORSION.md; ACTUAL-C5-SQUARE-CORRECTION-HAS-A-SIMPLE-ROOT.md; ACTUAL-VECTOR-SHADOW-HAS-A-TWELVE-POINT-POLAR-NORMAL-FORM.md. The companion verifier checks only universal rational-function, polynomial-elimination, ramification-degree, and residue-scaling identities, with no actual HM coefficient assignment, matrix, rank, or scan.

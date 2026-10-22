# The actual square third gate has forced icosahedral osculation

## New result and exact limit

Let Delta=P(W) be the discriminant conic of square negative directions, with its quadratic Veronese map to P(A). The actual third Bockstein restricts to an equivariant map

    b: D5 tensor O_Delta -> O_Delta(18).

Here O_Delta(1) means O_(P(W))(1), not the hyperplane restriction from P(A). The actual second symbol has rank three everywhere on Delta. The established two-channel theorem says that b is either zero or belongs to a single nonzero equivariant line; in the nonzero case its five sections are independent and basepoint-free.

The following additional facts hold if b is nonzero:

1. Its ramification divisor is exactly B_2+2B_3, where B_2 is the reduced orbit of thirty points with order-two projective stabilizer and B_3 is the reduced orbit of twenty points with order-three stabilizer.
2. Its vanishing sequences are (0,1,2,3,5) on B_2, (0,1,2,4,5) on B_3, and (0,1,2,3,4) everywhere else, including the twelve-point order-five orbit.
3. The associated morphism P(W)->P(D5*) is everywhere immersive and birational to its image, a nondegenerate rational curve of degree eighteen.
4. The fifth-jet evaluation is an everywhere-injective bundle map. In ordinary line-bundle notation it fits into

       0 -> D5 O -> J^5(O(18)) -> O(78) -> 0.

These are conditional constraints on the ACTUAL restriction, not an evaluation of it. In particular any independently proved extra basepoint, excess osculation, or ramification of the associated parametrization would force b=0. The rank-four node geometry alone does not supply such an extra condition: the precise local/global distinction is proved below.

## 1. From the actual Bockstein to a linear series

The actual global gate on P(A) is

    D5 O(-3) -> I_Z(6),

where the length-twenty-four second-symbol degeneracy scheme Z is disjoint from Delta. Pullback along the quadratic Veronese gives D5 O(-6)->O(12); twisting by six gives b above.

The source D5 is irreducible. Thus a nonzero b induces an injective map D5->H0(O(18)). Its basepoint-freeness was proved in THIRD-BOCKSTEIN-POLARIZATION-AND-SQUARE-DIRECTION-GATE.md: a common zero divisor would be an invariant divisor of degree at most eighteen, necessarily the twelve-point orbit, and division by its equation would put D5 in Sym^6 W=V+P4, which is impossible.

Consequently b is a five-dimensional basepoint-free linear series of degree eighteen. No local value of b is used in what follows.

## 2. Its Wronskian has only one possible invariant divisor

For a five-dimensional linear series in H0(P1,O(d)), its Wronskian is a nonzero section of

    O(d)^5 tensor (Omega^1)^(0+1+2+3+4)=O(5d-20).

It is nonzero in characteristic zero because the five sections are linearly independent. For d=18 its zero divisor has degree seventy. Its local multiplicity at a point with increasing vanishing sequence a_0,...,a_4 is

    sum_i(a_i-i).

The divisor is A5-invariant. A point stabilizer in a finite subgroup of PGL2 is cyclic: its derivative on the tangent line is faithful in characteristic zero. The nontrivial cyclic stabilizers in A5 have orders two, three and five. There is exactly one exceptional orbit of each type, of sizes thirty, twenty and twelve. Indeed the fifteen, ten and six cyclic subgroups respectively each fix two points, and distinct subgroups cannot share a point unless they lie in its cyclic stabilizer. All remaining orbits have size sixty.

Write the invariant Wronskian divisor as aB_5+bB_3+cB_2 plus ordinary orbits of total multiplicity d. Its degree gives

    12a+20b+30c+60d=70,
    a,b,c,d >= 0 integers.

Modulo ten, a is divisible by five. The only positive possibility a=5 leaves degree ten, which cannot occur. Thus a=0. Dividing by ten gives 2b+3c+6d=7, whose sole nonnegative solution is (b,c,d)=(2,1,0). This proves

    Ram(b)=B_2+2B_3.

Equivalently, let H_20 and T_30 denote invariant binary forms with reduced zero divisors B_3 and B_2, defined up to nonzero constants without choosing their coefficients. Then the Wronskian has the exact universal form

    Wr(b)=c T_30 H_20^2,    c!=0.

These orbit equations are invariant rather than merely semi-invariant because the binary icosahedral group has no nontrivial characters. The equality is an identity of binary forms, not just an equality of zero sets. It does not determine the actual scalar multiplying b.

No selected point or coefficient has been evaluated.

## 3. Exact vanishing sequences and global consequences

Basepoint-freeness gives a_0=0. Weight zero forces the ordinary sequence (0,1,2,3,4). Weight one forces (0,1,2,3,5), so the order-two orbit has the asserted sequence.

At a point of B_3, weight two leaves only two increasing possibilities:

    (0,1,2,3,6), or (0,1,2,4,5).

The projective order-three stabilizer acts on D5=Sym^4 W with eigenvalue multiplicities (1,2,2). This follows directly by restricting the five weights 4,2,0,-2,-4 to a binary lift of order six. The fiber of O(18) has trivial character under that lift. Equivariance identifies section vanishing orders modulo three with the three eigenspaces, up to reversing the generator. The first possible sequence has residue multiplicities (3,1,1), which is incompatible. The second has multiplicities (1,2,2), so it is forced.

In particular a_1=1 everywhere. The morphism defined by the series is therefore immersive everywhere. Factor it through the normalization of its image. That normalization is P1: a nonconstant morphism from P1 onto a smooth projective curve forces genus zero by Riemann--Hurwitz. If the finite map to that normalization had degree greater than one, it would have a ramification point, where the original morphism could not be immersive. It follows that the normalization map has degree one. The image has degree eighteen because b pulls the ambient hyperplane line back to O(18).

The series is nondegenerate because its five sections are independent. Birational and immersive does not imply that the image is smooth or embedded; distinct points could still have the same image. No embedding assertion is made.

Every vanishing order a_i is at most five. Therefore evaluation to fifth principal parts is injective on fibers everywhere. Its cokernel is a line bundle. The principal-parts filtration has graded lines O(18-2j), for 0<=j<=5, whose degrees sum to

    18+16+14+12+10+8=78.

This proves the exact bundle sequence in the result. Its ordinary cokernel is O(78); the finite-group linearization is inherited from the map.

## 4. What the rank-four geometry actually contributes

Write the ambient five-space as the positive three-space V plus the negative two-space W. The invariant q0 is nondegenerate on V and zero on W. For a nonzero square a=ell^2 and t!=0,

    Q_(ell,t)=(q0+t ell^2=0)

has rank four and is integral, with its sole vertex p=P(ker ell) on L=P(W). Its intersection with L is scheme-theoretically 2p, not two distinct points and not a component L.

Near p choose an affine negative coordinate that is nonzero. In the resulting coordinates (x_1,x_2,x_3,z), with z representing ell, the local equation is q0(x)+t z^2. Inversion acts by x_i->-x_i and z->z. In the three-dimensional Cohen--Macaulay local ring of Q, the ideal of the actual line intersection is

    (x_1,x_2,x_3), with quotient C[z]/(z^2).

Since the quotient has dimension zero, these three elements form a regular sequence. Thus the double point is a regular codimension-three immersion in the singular quadric. There is no additional Tor or local Koszul-homology term merely because its support is the vertex.

This applies to the actual evaluation resolution, not a substitute bundle model. Near an evaluation-degeneracy line the actual evaluation matrix can be reduced, after canceling a unit, to the three transverse generators of its ideal. Restriction to Q leaves their Koszul resolution exact by the preceding regular-sequence argument. Equivalently multiplication by q0+t ell^2 is injective on the line-supported evaluation cokernel, because its restriction t ell^2 is a nonzero function on that line.

For a proper intersection with all twenty-five lines, the actual fifty-point resolution and its dual cubic-restriction map therefore remain valid. At the distinguished vertex they use the length-two scheme 2p and its dualizing line, not a nonexistent pair of reduced marks. On 2p the involution acts trivially on the scheme and hence on its intrinsic dualizing line. The evaluation tail ell_eval^2(-1)|_(2p) has character minus one, so this length-two contribution has trace minus two, exactly the same trace as the two reduced fixed marks in the smooth even-quadric calculation.

The ambient primary cohomology and hypersurface ACM/Gorenstein calculations are unchanged by this rank-four singularity. The actual equivariant Euler calculation consequently still gives

    h0(B_Q(4))_+ - h1(B_Q(4))_+ = 4.

This is not a new proof of a fifth section or of its absence. It shows precisely why a putative extra local contribution from the node or colliding marks cannot decide the remaining one-dimensional positive obstruction: the exact local duality complex has no missing term. A further constraint would have to concern the actual GLOBAL lift boundary, or the osculation of b, not rank four or the double point alone.

## 5. Why the general-cone ruling argument does not settle this family

The quotient four-space at the vertex is V plus the one-dimensional negative quotient W/ker ell. Inversion has determinant minus one on it. On a smooth quadric surface, an orthogonal transformation with determinant minus one interchanges the two components of the space of maximal isotropic two-planes, hence exchanges the two plane rulings of the cone. One way to see the component distinction is to use the two eigenspaces of the Hodge involution on the middle exterior power; an orientation-reversing orthogonal transformation exchanges them.

Thus inversion exchanges the two small resolutions rather than acting on either fixed ruling resolution. A pushforward on one ruling does not by itself produce a positive-parity bundle governing the desired 41-to-37 block. Moreover the vertex is constrained to the distinguished HM jumping line, so the generic-translate avoidance of bad plane strata used in RANK-FOUR-CONE-RULING-GATE.md has not been established on this square family.

There is a still simpler incompatibility with borrowing the full-adjoint balancedness conclusion from general cones: every present cone is inversion-even, so the exact index above already forces at least four positive sections. Full-adjoint vanishing is not the target here. The remaining target is h1(B_Q(4))_+=0, or equivalently exactly four positive sections, and that is the actual global obstruction still under examination.

## Boundary of the result

This note determines the complete possible ramification and parametrization geometry of a nonzero actual square third channel, and identifies the precise failure of a node-only or generic-ruling shortcut. It neither proves b nonzero nor proves b zero. The discriminant-divisible third channel is invisible on this conic, and even b=0 does not rule out that channel or a later Bockstein.

Dependencies are the actual Hilbert--Burch third-gate presentation, THIRD-BOCKSTEIN-POLARIZATION-AND-SQUARE-DIRECTION-GATE.md, FULL-ADJOINT-PENCIL-INVOLUTION-BLOCKS.md, INVERSION-EVEN-QUADRICS-ARE-ADJOINT-BAD.md, and the actual QUADRIC-FIFTY-POINT-BOUNDARY.md. The Wronskian, regular-sequence, duality, and ruling arguments above are global geometric or universal representation proofs. No selected actual HM/source coefficient, actual map value, matrix, rank test, parameter scan, model experiment, or external write is used.

## Reproduction

Run `python3 verify_square_third_osculation.py` from this directory. The standalone standard-library verifier checks the unique degree-seventy orbit partition, all candidate vanishing sequences of weights zero through two, their cyclic-stabilizer residues in Sym^4 W, and the fifth-principal-parts degree seventy-eight. These are universal integer and representation-weight calculations, not evaluations of an actual map. The proof above supplies the geometric inputs. Passing the verifier leaves both the actual square value and the final full repair explicitly open.

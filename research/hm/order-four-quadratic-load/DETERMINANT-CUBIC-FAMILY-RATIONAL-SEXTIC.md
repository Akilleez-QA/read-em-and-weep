# The actual determinant cubics form a rational normal sextic

## Theorem

Retain the actual invariant-hyperplane determinant family c_lambda in H0(R,O_R(3)), parameterized by lambda in P(W*). Let q0 be the invariant nondegenerate quadratic on the positive three-space V, and let Z6 be the six nonisotropic axis points in R=P(V), one for each cyclic subgroup of order five in A5.

The following statements hold without selecting HM coefficients:

1. The determinant cubics form a rational normal sextic in

       P(q0 V* directsum H0(I_Z6(3))) = P6.

   Both irreducible channels V and 4 occur nontrivially.
2. H0(I_Z6(3)) is the unique four-dimensional cubic constituent, and its scheme-theoretic base locus is exactly the reduced six-point scheme Z6. The full actual determinant family has no common plane base point.
3. Neither channel vanishes at any parameter. No member contains the invariant conic (q0=0) as a component.
4. For an axis point p, the parameter divisor of cubics containing p is

       3 lambda_(p,+) + 3 lambda_(p,-),

   where the two parameters are the fixed points of its order-five subgroup on P(W*). The six pairs are disjoint. Thus precisely twelve parameters give cubics meeting Z6; each such cubic contains exactly its one associated axis point.

This sextic is in the seven-dimensional linear system of plane cubics, not the earlier rational sextic Gamma in P3. Nothing here asserts that an individual cubic is smooth, irreducible, or reduced. Triple parameter incidence is not a claim of a singularity of the plane cubic.

## 1. The actual determinant intertwiner

Put E=F_R(2). Its actual Steiner presentation is

    0 -> A O_R(-1) -> D O_R -> E -> 0,
    A=Sym^2 W,  D=Sym^4 W,
    det E=O_R(3).

In particular D globally generates E. Wedge of the actual evaluation gives an equivariant map

    d:Lambda^2 D -> H0(O_R(3))=Sym^3 V*.

The hyperplane-section theorem identifies the section two-plane with ell_lambda^3 W in D, where ell_lambda is the annihilator of lambda. Its determinant therefore gives

    c_lambda=d(Lambda^2(ell_lambda^3 W)).              (1)

The universal Clebsch–Gordan decomposition is

    Lambda^2 Sym^4 W = Sym^6 W directsum Sym^2 W.

The Plucker curve ell |-> Lambda^2(ell^3 W) is the degree-six Veronese in the Sym^6 W summand. For example its highest-weight line has weight six; equivariance and irreducibility then identify the entire summand and its Veronese orbit. This is a universal representation statement, not an actual coefficient calculation.

On restricting to A5, the source and target decompose as

    Sym^6 W=V directsum 4,
    Sym^3 V*=V directsum A directsum 4.                (2)

Thus the actual family is obtained from the Veronese by the actual intertwiner

    alpha:V directsum 4 -> V directsum A directsum 4.

There is no A-channel. The remaining task is to prove that neither of the two allowed scalars is zero.

## 2. The actual family has no common plane base point

Suppose p in R lay on every c_lambda. Since the Veronese spans Sym^6 W, the nonzero determinant of evaluation at p would annihilate that entire summand. Evaluation D->E_p is onto, so its determinant is a nonzero decomposable element of Lambda^2 D*, up to the one-dimensional determinant fiber. Such an alternating form has rank two.

The annihilator of Sym^6 W is the remaining Sym^2 W summand in Lambda^2 D*. It contains no nonzero alternating form of rank two. To see this intrinsically, use the invariant symmetric form on D=Sym^4 W. It identifies this summand with the image of sl_2 acting on Sym^4 W, through

    X |-> ((v,w) |-> (Xv,w)).

Every nonzero element of sl_2 is conjugate either to a nonzero semisimple element or to a nonzero nilpotent element. In the semisimple case its five weights are proportional to 4,2,0,-2,-4, hence the rank is four. In the nilpotent case its action is one Jordan block of length five, again of rank four. The associated alternating form has the same rank because the invariant symmetric form is nondegenerate.

Thus the decomposable evaluation determinant cannot belong to the annihilator. This contradiction proves that the actual cubic family is base-point-free on R.

## 3. The six axis points and the four-dimensional cubic system

Each cyclic subgroup C5 of A5 has a unique eigenvalue-one line in V. The six-subgroup conjugation action is doubly transitive: a C5 in one normalizer permutes the other five subgroups freely. Coincidence of two axes would therefore force all six axes to coincide, contradicting irreducibility of V. Thus there are six distinct axis points, and their stabilizer is exactly the dihedral normalizer of order ten. Its rotations act trivially on the axis, while its involutions act by minus one: they exchange the two nontrivial eigenspaces in the orthogonal complement, and the three-dimensional representation has determinant one. The axis is nonisotropic for q0, since it is orthogonal to that complement and q0 is nondegenerate.

The cubic fiber O_R(3)|p therefore has the normalizer sign character. The multiplicity of that character in the irreducible four-space is

    (4 + 4(-1) - 5(0))/10 = 0.

Here the four nonidentity rotations have four-space character -1, and the five involutions have character zero. Hence evaluation of the four-dimensional cubic constituent at p is zero. The same holds at all six axis points.

These six points are in general position. Their degree-six A5 action is doubly transitive: the order-five subgroup in one point stabilizer acts freely, hence transitively, on the other five. If a line through a pair contained k of the six points, double transitivity would make k the same for every pair. The five other points through one point partition into groups of size k-1. Thus k-1 divides five, so either k=2 or all six points are collinear. The latter contradicts irreducibility of V. Therefore no three are collinear.

There is no conic through all six. Such a conic would be unique up to scalar: two distinct conics through six points have a common component by Bezout, incompatible with no three collinear. Its equation would consequently span an invariant line in Sym^2 V*, hence would be q0. But none of the axis points lies on q0.

It follows that quadratic evaluation on Z6 is an isomorphism between two six-dimensional spaces. Thus H1(I_Z6(2))=0; also H2(I_Z6(1))=0. The ideal is therefore 3-regular. In particular I_Z6(3) is globally generated, has four sections, and has base scheme exactly Z6. The four-dimensional cubic constituent, already shown to vanish there, is consequently

    H0(I_Z6(3)).                                      (3)

## 4. Both actual channels are forced nonzero

The unique V-constituent in Sym^3 V* is q0 V*, since multiplication by the invariant quadratic gives a nonzero equivariant inclusion. Its common base is the invariant conic.

If the four-dimensional channel of alpha were zero, all determinant cubics would belong to q0 V* and would share that conic. If the V-channel were zero, all would belong to (3) and would share Z6. Both alternatives contradict Section 2. Thus both channels are nonzero.

Schur's lemma now makes alpha injective on V directsum 4, with image exactly

    q0 V* directsum H0(I_Z6(3)).                       (4)

Equation (1) is therefore a linear isomorphism of its spanning seven-space applied to the degree-six Veronese. This proves that the actual family is a rational normal sextic in the P6 of (4). In particular distinct parameters give distinct cubic equations, and any at most seven distinct members are linearly independent.

This determines the allowed channels, their nonvanishing, the exact span, and the projective type of the actual curve. It does not compute the relative nonzero scalar of its two equivariant channels.

## 5. Neither projected channel has parameter base points

The projections of the degree-six Veronese to V and to 4 give two nonzero invariant subsystems of H0(P(W*),O(6)). A common zero divisor of either subsystem would be an A5-invariant effective divisor of degree at most six. But an icosahedral orbit on P1 has size at least twelve. Therefore both subsystems are base-point-free.

Consequently each individual cubic has nonzero components in both summands of (4). In particular no member is divisible by q0: the entire space of cubics divisible by q0 is precisely q0 V*.

This argument does not apply Bertini to the seven-dimensional span in order to claim smoothness of the one-dimensional family. The sextic parameter curve could meet or even lie in a cubic discriminant locus without contradicting its base-point-freeness.

## 6. Exact parameter incidence at the six axes

Fix p in Z6 and evaluate the actual family at p. It gives a section of O_P(W*)(6), with values in the fixed cubic fiber O_R(3)|p. It is nonzero by Section 2.

The cyclic order-five subgroup fixing p acts trivially on that fiber. In eigen-coordinates x,y for its action on W, the only invariant weight in degree six is the weight-zero line spanned by x^3 y^3. Indeed the weights 6,4,2,0,-2,-4,-6 have only zero divisible by five. Choosing an order-ten rather than an order-five lift gives the same conclusion because degree six is center-even.

The normalizer reflection interchanges x and y with product of the two interchange scalars equal to -1, since it belongs to SL2. It acts on x^3 y^3 by -1, exactly the sign on O_R(3)|p. Thus the nonzero evaluation section is a scalar multiple of this universal weight-zero form, and its divisor is

    3 lambda_(p,+) + 3 lambda_(p,-).                   (5)

The two points in (5) are the fixed points of that C5 on the parameter line. Different order-five subgroups have disjoint fixed-point pairs: point stabilizers in a finite subgroup of PGL2 are cyclic, and the stabilizer here has order five. There are therefore twelve distinct special parameters.

For each special parameter, precisely one axis evaluation vanishes; for every other parameter none vanishes. This proves the stated incidence conclusion scheme-theoretically in the parameter direction. It gives no plane-cubic multiplicity or singularity conclusion at the axis point.

## Scope and dependencies

INVARIANT-HYPERPLANE-DETERMINANT-CUBIC-CONES.md supplies the actual two-space ell_lambda^3 W and the everywhere nonzero determinant family. The actual Steiner presentation supplies global generation used in Section 2. All remaining arguments are universal representation theory and the geometry of the six-axis orbit.

The companion verify_binary_determinant_channels.py checks only the universal sl2 alternating ranks, the Sym^8 character, the dihedral sign multiplicity, and the invariant sextic weight. No selected HM/source coefficients, evaluated actual matrices or ranks, scans, or experiments are used. The result does not establish mixed-root section compatibility, smoothness of individual cubics, or the remaining full-adjoint vanishing gates.

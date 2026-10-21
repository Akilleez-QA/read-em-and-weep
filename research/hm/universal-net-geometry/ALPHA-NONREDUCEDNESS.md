# The wedge-minor scheme is nonreduced at alpha nets

## Scope and dependency

Work over C. Let A have dimension five and let G=Gr(3, exterior^2 A*) with tautological rank-three bundle N. Let D be the closed subscheme defined by the 2-by-2 minors of the wedge map

    w: Sym^2 N -> exterior^4 A*.

The universal common-radical theorem in PR560, commit b9ee9b3b105967ee4d9e423d30cfa961ce0824d7, proves equality of closed-point supports between D and nets with a nonzero common radical. It also classifies zero-wedge nets into alpha and beta types. The present result concerns this universal Grassmannian scheme, not an assertion that a selected HM net belongs to either type.

## The contraction scheme and its smooth incidence

Define the contraction map

    c: A tensor O_G -> N* tensor A*,
    x |-> (omega |-> contraction_x omega),

and let C be the closed subscheme defined by its 5-by-5 minors, equivalently by rank(c)<=4. Let J in G times P(A) be the incidence defined by contraction_x(N)=0.

For fixed [x], the allowed forms constitute exterior^2(x^perp), a six-dimensional vector space. Hence J is the relative Grassmannian Gr(3, exterior^2 Q*) over P(A), where Q=A/O(-1). In particular J is smooth, irreducible, projective, and has dimension

    4 + 3(6-3) = 13.

On the open locus where c has rank at least four, projection J->C is a scheme isomorphism. Indeed, after choosing an invertible 4-by-4 pivot, invertible row and column operations put c into a block consisting of I_4 and one residual column. The 5-by-5 minors generate the entries of that residual column. The kernel-line incidence equations determine the first four kernel coordinates from the fifth, and then impose exactly the same residual-column equations. The fifth coordinate is a unit on the kernel line in this pivot chart. This proves the assertion over arbitrary C-algebras, not merely on closed points.

It follows that C is smooth of dimension thirteen on its rank-four locus.

## Alpha points: strict scheme discrepancy

At an alpha net choose independent covectors a,b,c,d and write

    N_alpha=span(a wedge b, a wedge c, a wedge d).

Its common radical is ann(span(a,b,c,d)), a line. Thus contraction has rank four, and C is smooth of dimension thirteen near this point.

Every pairwise wedge product in N_alpha is zero. Consequently every entry of the local matrix of w vanishes at N_alpha. Every 2-by-2 minor therefore belongs to the square of the maximal ideal of the smooth ambient Grassmannian. Its linearization is zero. Thus

    T_(N_alpha) D = T_(N_alpha) G,
    dim T_(N_alpha) D = 3(10-3)=21.

By PR560, D and C have exactly the same closed points. In a rank-four contraction neighborhood of N_alpha, C is smooth and therefore reduced, so the Nullstellensatz gives

    D_red = C

as schemes on that neighborhood. But their Zariski tangent dimensions are twenty-one and thirteen. Therefore D is nonreduced at every alpha net. Equivalently the reduction map has an eight-dimensional kernel on Zariski cotangent spaces at each alpha point. This last assertion measures first-order nilpotent directions only; it is not a claim that the nilradical has length eight or square zero.

There is also a direct ideal comparison on this neighborhood. The universal radical line on C is a subbundle of A. Every form lies in its rank-four annihilator, so every wedge product lands in a line bundle. Hence all wedge 2-by-2 minors vanish scheme-theoretically on C. Their ideal is contained in the contraction-minor ideal, and the tangent calculation proves strict containment in the local ring at an alpha point.

## Global support and fiber geometry

The reduced support D_red is the image of the proper irreducible variety J. It is therefore irreducible. There are nets with a unique common radical and containing a rank-four form: on a four-dimensional covector subspace, take a three-dimensional net containing a symplectic form. The rank-four contraction open is thus nonempty, and the preceding isomorphism gives dim D_red=13. Therefore J->D_red is a proper birational morphism from a smooth variety, a resolution of this reduced support.

A three-dimensional net cannot have a common radical of dimension at least three: all its forms would then lie in the one-dimensional exterior square of a two-dimensional annihilator. By PR560, nets with a two-dimensional common radical are precisely beta nets

    N_beta=exterior^2 B,  dim B=3,

and have zero wedge map. Their parameter space is Gr(3,A*), of dimension six, and their incidence fibers are P(Rad(N_beta))=P^1. All other nets in D_red have a unique common radical. Thus J->D_red is an isomorphism away from the beta locus, and its positive-dimensional fibers occur exactly there. The inverse image of the beta locus has dimension seven, hence codimension six in J.

The alpha locus is the flag variety of pairs ell subset B subset A* with dimensions one and four, via N=ell wedge B. It has dimension 4+3=7. The common factor ell and support B recover the flag uniquely. In particular the nonreducedness proved above occurs along an entire seven-dimensional locus, even though the reduced support is smooth there.

No assertion is made here about reducedness of the contraction scheme at beta nets, normality of D_red, or a scheme identification of D and C across the zero-wedge locus.

## Consequence for the actual-family approach

The restriction in PR560 to nets containing a rank-four form is essential for its stated wedge-minor scheme bridge. Merely proving existence and uniqueness of a common radical does not extend that bridge: alpha nets already have unique radicals, while the wedge-minor scheme has eight extra tangent dimensions there.

Pulling the schemes back to the actual traceless-orbit family does not automatically preserve this nonreducedness: special pullbacks can remove nilpotents. Conversely, no set-theoretic identification permits dropping those nilpotents without proof. To use wedge equations for actual rank-nine transversality, one must either stay on the rank-four-form open, establish the relevant scheme comparison after pullback, or work directly with the contraction incidence. The intersection of the actual family with the alpha and beta loci is not determined here.

All arguments are universal linear algebra, Grassmannian geometry and exact local elimination. No selected actual HM/source coefficient, matrix, rank, or numerical experiment is evaluated. This is a mathematical proof, not a proof-assistant certificate.

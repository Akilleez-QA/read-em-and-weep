> Historical mathematical record, 16 October 2026. Statements of PASS and check counts below refer to the original recorded verification, not a new execution. See PUBLICATION-SCOPE.md at the common series root for current scope, imported premises, and source/public hash bindings.

# Twelve literal constant-row evaluations suffice on the positive target

This is a symbolic corollary of the existing quotient maps and the four witnesses independently verified in `AUDIT.md`. No new coefficient products or rank computation are used.

## Exact selected evaluations

Use K30 free-coordinate indexing r=15c+i for E13[c,i], corresponding to the original scalar row L_(i,c). Use the authenticated harmonic index

    k=27(kappa1+3)+9(kappa2+3)+3(kappa3+3)+(kappa4+3).

At kappa=(-1,-1,-3,-3), index72, select the eight literal rows

    r=0,1,5,6,10,11,15,16,
    L_(0,0), L_(1,0), L_(5,0), L_(6,0),
    L_(10,0), L_(11,0), L_(0,1), L_(1,1),       (1)

in that order. At kappa'=(-2,-1,-2,-1), index50, select

    r=9,4,5,12,
    L_(9,0), L_(4,0), L_(5,0), L_(12,0).       (2)

These are12 row-position pairs. Rows with the same matrix identifier at two different harmonic positions are distinct evaluations. They are genuine original constant rows, not unspecified linear combinations or positive-block p-coordinate functionals.

## Old eight, including the two boundary-sensitive choices

The complete d5 quotient retains e0,...,e19, with

    e_(25+a)=-e_a,
    e_(20+a)=-e_(10+a), a=0,...,4.

Thus e10 and e11 are independent retained coordinates. The relations with e20 and e21 do not set them to zero. On this quotient inversion is four copies of -J5:

    I(e_(5b+s))=-e_(5b+4-s).

The established positive basis is

    P_(b,s)=e_(5b+s)-e_(5b+4-s),
    b=0,...,3, s=0,1.

Consequently the plus classes of the eight literal graph cycles(1) are exactly P0/2,...,P7/2 in lexicographic(b,s) order. This follows directly from the saved quotient and involution; it is not an inference from a dimension count.

Multiplication by v2 is inversion equivariant and descends through the complete d5 boundaries. Therefore replacing the plus class of E_(5b+s) by P_(b,s)/2 is legitimate in both the first and second components of the single-position dual graph. The positive third primal component is zero. With the original factor4 trace normalization, the old eight evaluation values are

    y_i=2z_i+2 <G1,v2 P_i>, i=0,...,7.          (3)

The bracket is the existing genuine Serre supertrace pairing. Its actual8-by4 coefficient matrix need not be computed to prove the following implication.

## Block-triangular certificate

The four new evaluations(2) are independently verified to be

    t=(-w0,w1,-2w2,-w3).

Relative to the specified coordinates (z0,...,z7,w0,...,w3), the12 evaluation map has block form

    [ 2 I8   M ]
    [  0     D ],
    D=diag(-1,1,-2,-1),                         (4)

where M is the well-defined matrix of the second term of(3). Its entries are unnecessary for the determinant: det(4)=2^8 det(D)=−512≠0. Equivalently t=0 forces w=0 and hence G1=0, after which y=0 forces all z_i=0.

Therefore these12 literal evaluations constitute a complete linear detector system on the full positive12-dimensional space. Their cardinality is minimal among scalar linear tests separating all vectors of that space. This minimum says nothing about an independently established smaller source-specific subspace, and no actual evaluation or obstruction vanishing is supplied.

The source's membership in this target, its complete representative, and the required source/cover/trace acquisition remain separate premises. This does not claim an81-position computation or actual source values.

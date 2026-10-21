# The determinant-cubic family has no distinguished line factor

## Theorem

Let c:P(W*) -> P(Sym^3 V*) be the actual determinant-cubic family on the positive HM plane R=P(V). The binary icosahedral two-space W satisfies Sym^2 W=A, where A and V are the two distinct irreducible A5 three-spaces. The actual family is the rational normal sextic established in DETERMINANT-CUBIC-FAMILY-RATIONAL-SEXTIC.md.

Exactly one of the following alternatives holds:

1. A general member is an irreducible plane cubic. Only finitely many parameter values give reducible cubics.
2. A general member is a product of three distinct lines, and its three line factors form an irreducible degree-three cover of the parameter line. The normalization of this cover has genus at least four.

In particular, a general member is reduced. The family cannot generically be a line times an irreducible conic, a triple line, or a doubled line times a different line. In the three-distinct-line alternative the factor monodromy must be transitive. This theorem does not exclude that alternative and therefore does not assert that a general determinant cubic is irreducible or smooth.

## 1. Degree of an equivariant line map

Write G=2.A5 for the binary icosahedral group. It acts on W and on the parameter line P(W*). Its center acts trivially on V. If

    f:P(W*) -> P(V*)

is A5-equivariant, let d be the degree of f*O(1). Pullback of the standard linearization on O_P(V*)(1) gives a G-linearization on O(d), with trivial central action. Since G is perfect, its characters are trivial, so linearizations on O(d) are unique up to isomorphism. The standard one has central action (-1)^d. Consequently d is even.

Pullback of linear sections is a nonzero equivariant map

    V -> H0(P(W*),O(d)) = Sym^d W,

with the harmless self-dual identification of W understood. It is injective because V is irreducible. A constant map is impossible: its image would be an invariant point in P(V*).

The relevant even symmetric powers are

    Sym^0 W=1,
    Sym^2 W=A,
    Sym^4 W=5,
    Sym^6 W=V directsum 4.

Thus every such line map has d at least six. This is a statement about the actual two inequivalent three-dimensional representations, not merely the existence of an abstract icosahedral action.

## 2. No equivariantly distinguished line factor

Suppose a line factor of the generic cubic is defined over C(P(W*)) and is preserved by the A5 action on the family. It determines an equivariant rational map f to P(V*). The residual quadratic factor determines an equivariant rational map g to P(Sym^2 V*).

Both maps extend uniquely over the entire smooth parameter line, because their targets are projective. The multiplication map of polynomial equations has no base points:

    P(V*) x P(Sym^2 V*) -> P(Sym^3 V*).

The identity c=f g on the generic point therefore extends everywhere. Multiplication pulls O(1) back to O(1,1). If d and e are the pullback degrees for f and g, then

    d+e=6.

Here d,e are nonnegative because they are degrees of globally generated line bundles. Section 1 gives d at least six, so d=6 and e=0. Hence g is constant. Equivariance makes its equation an invariant line in Sym^2 V*. Since A5 has no nontrivial characters and

    Sym^2 V*=1 directsum 5,

this constant conic is the invariant nondegenerate conic q0.

But the actual family theorem proves that no c_lambda is divisible by q0: each member has nonzero components in both q0 V* and the four-dimensional cubic constituent. This contradiction excludes every equivariantly distinguished generic line factor, whether or not its residual conic is irreducible.

## 3. The generic factorization types

Factorization types may be considered over an algebraic closure of the parameter function field.

If the generic cubic is a line times an irreducible conic, its line is unique. It is consequently defined over the parameter function field and preserved by A5. Section 2 excludes it.

If the generic cubic is a triple line, its line is again unique. If it is a doubled line times a different line, the multiplicities distinguish both factors. These cases are likewise excluded by Section 2. Equivalently, their degree formulas are 3d=6 and 2d+e=6, incompatible with the minimum degree six for each equivariant line map.

It follows that a geometrically reducible generic cubic must be three distinct lines.

Consider the incidence of line factors in P(W*) x P(V*). It is closed: it is obtained by projecting the closed factorization correspondence with the projective residual-conic space. Its fibers are finite, since a nonzero cubic has at most three distinct line factors. Take the reduced closure of the three generic factors and normalize it. This gives a possibly disconnected smooth projective curve B with a finite, generically etale degree-three map

    pi:B -> P(W*).

The A5 action preserves the incidence and lifts canonically to its normalization.

If this cover is not irreducible, its component degrees are either 1+2 or 1+1+1. In the first case the degree-one component is unique and A5-stable, yielding the forbidden equivariant line factor. In the second case A5 permutes the three components through a homomorphism A5 -> S3. Such a homomorphism is trivial, so each degree-one component is stable and again gives a forbidden equivariant line factor. Therefore B is irreducible, or equivalently its generic factor monodromy is transitive.

Finally, the locus of reducible ternary cubics is closed, as the image of the projective multiplication map of a line and a quadratic. If the family is not contained in this locus, its inverse image on P1 is finite. This proves the stated dichotomy.

## 4. Genus forced by equivariant branching

In the three-line alternative the map pi has degree three and the connected curve B is smooth. Its ramification divisor is nonzero: Riemann-Hurwitz would otherwise give 2g(B)-2=-6, which is impossible.

The pushforward of this ramification divisor is a nonzero effective A5-invariant divisor on the parameter line. Every icosahedral orbit on that line has size at least twelve. Its degree is therefore at least twelve. Riemann-Hurwitz now gives

    2g(B)-2=-6+deg Ram(pi) >= 6,

so g(B) is at least four.

If equality holds, the branch divisor is exactly the twelve-point orbit with multiplicity one. Every branch point is simple, hence its local monodromy is a transposition. Transitivity then forces full S3 monodromy, not cyclic degree-three monodromy. This additional conclusion is conditional on the three-line alternative and genus four; it is not an existence claim.

## Limits

A transitive degree-three factor cover is a genuine remaining possibility. In particular, a correspondence between the two inequivalent icosahedral parameter lines can have bidegree (3,3), since the two binary cubic representations are isomorphic four-spaces. One cannot label the three line factors globally without justifying the covering monodromy, and one cannot use the preceding argument to infer generic irreducibility.

Only the actual representation distinction, the established polarization degree six, and exclusion of a q0 component are used. No selected HM coefficients, actual matrix ranks, scans, or experiments are involved. No claim concerning mixed-root square compatibility or remaining adjoint gates follows from this factorization theorem.

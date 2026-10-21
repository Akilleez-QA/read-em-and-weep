# Universal second Bockstein symbols and the remaining rank-three channel

## Status and actual scope

The positive first Bockstein is zero, as proved in POSITIVE-FIRST-BOCKSTEIN-VANISHES-BY-CYCLIC-RAO.md. Its former scalar gamma is therefore zero, not an open nonvanishing problem. Write A=Sym^2 W and D=Sym^4 W, and P for the genuine four-dimensional representation.

This note classifies the universal possible second-order symbol. It does not evaluate its actual coefficients. The independent square-shadow argument, if established, annihilates the D-input summand entirely; under that input, the conclusion here is that the actual second Bockstein is either zero or generically rank exactly three. It cannot itself give the four missing positive ranks.

Current application: POSITIVE-SECOND-BOCKSTEIN-SQUARE-FILTRATION.md now proves the actual D input is zero, and ACTUAL-SECOND-BOCKSTEIN-NONZERO-BY-ATIYAH-QUINTIC.md proves the actual A scalar is nonzero. Thus the rank-three universal geometry below applies to the actual second Bockstein. The conditional and archival channel classification remains valid as a universal statement.

## 1. The cyclic constraint on the A-input

Let xi be the invariant cyclic class and let zeta:A -> H1(B)_A satisfy q0 zeta_a=a xi. The established original kernel is K=(A+D)xi, and multiplication by every negative quadratic kills K after passage to the q0-cokernel P, because the first Bockstein is zero.

For a,b in A, associativity gives

    q0(a zeta_b-b zeta_a)=0.

Consequently a zeta_b-b zeta_a belongs to K. Multiplication by any c in A has zero class in P. Thus [ca zeta_b]=[cb zeta_a]. Together with commutativity of polynomial multiplication, the trilinear expression [ab zeta_c] is fully symmetric. The A-input second symbol therefore factors through Sym^3 A, not merely Sym^2 A tensor A.

Now Sym^3 A = Sym^6 W + Sym^2 W = P+V+A. Hence exactly one scalar remains on this input. There is no representation-theoretic vanishing of that scalar.

## 2. An explicit universal model and its generic rank

Use a=p X^2+q XY+t Y^2, and identify the P quotient of Sym^6 W with W tensor W'. In the monomial basis X^6,X^5Y,...,Y^6, an exact equivariant projection is

    [ sqrt(5), 0, 1, 0, -sqrt(5)/3, 0, 5 ]
    [ 0, sqrt(5)/3, 0, -1, 0, -sqrt(5), 0 ]
    [ 0, -sqrt(5), 0, -1, 0, sqrt(5)/3, 0 ]
    [ 5, 0, -sqrt(5)/3, 0, 1, 0, sqrt(5) ].

The unique channel is h -> projection(a^2 h), for h in Sym^2 W. This is the polarization of a -> projection(a^3), up to a nonzero normalization. Its 4 by 3 matrix has rank three, for example at the universal direction a=X^2+XY+Y^2. Therefore it has generic rank three. This evaluates only a universal representation symbol, not any actual HM coefficient or cohomology map.

In fact the universal map has rank three on every square direction a=ell^2. The kernel would be a nonzero sextic in the three-dimensional V summand divisible by ell^4. For the V-linear series in H0(P1,O(6)), such a point has vanishing sequence at least (0,1,4), hence Wronskian weight at least two. Its G-orbit has at least twelve points. But the nonzero Wronskian has total degree 3(6-2)=12, incompatible with weight at least 24. Thus V intersects ell^4 Sym^2 W trivially. This coefficient-free strengthening was supplied by the square-filtration worker and checked here. It does not claim rank three at every nonsquare direction.

If the actual scalar is nonzero, the second Bockstein has generic rank three when its D-input is zero. If that scalar is zero, the entire second Bockstein is zero. Higher-order obstructions remain necessary for a possible fourth rank gain.

## 3. The exact universal rank-drop scheme

The four maximal minors of the surviving 4 by 3 matrix have no common polynomial factor, as checked exactly over Q(sqrt(5)). Therefore the projective rank-drop scheme in P(A)=P2 is zero-dimensional. Hilbert--Burch gives its ideal resolution

    0 -> O(-8)^3 -> O(-6)^4 -> I_Delta -> 0.

Its length is 24, from the second derivative at 1 of 1-4z^6+3z^8 divided by two. The preceding Wronskian argument shows this entire scheme is disjoint from the discriminant conic of square directions. No claim of reducedness is made. This is a universal degeneracy scheme of the nonzero channel, not an evaluation of the actual remaining scalar.

## 4. Archival classification before the geometric D-input annihilation

Since Sym^2 A=1+D, the unrestricted space

    Hom_G(Sym^2 A tensor (A+D),P)

has dimension 1+2=3. The two D-input channels are projection to P of a^2 h in Sym^8 W, and projection to P of the first transvectant (a^2,h)_1 in Sym^6 W. The scalar part of Sym^2 A contributes neither channel.

For the exact normalizations in the companion verifier, denote their coefficients by v,w. There is one exceptional line 3v+160w=0. Off this line the D-input channel is generically rank four. A nonzero channel on this line is generically rank three. A nonzero A-input coefficient together with a nonzero exceptional D-input channel is generically rank four. The A-input-only channel is generically rank three; all coefficients zero gives rank zero. These facts are universal and must not be read as evidence that any actual coefficient is nonzero.

The proof is exact: using both universal directions a=X^2+XY+Y^2 and a=X^2+2XY+3Y^2, the greatest common divisor of the ten maximal minors of the D-input pencil is v+160w/3. On the exceptional line all maximal minors vanish identically as polynomials in p,q,t, while a 3 by 3 minor is nonzero. The combined A-input/exceptional-D-input matrix has a nonzero 4 by 4 minor. The verifier checks the projections against generators of the binary icosahedral group and performs all these identities over Q(sqrt(5),i).

## Evidence and limitations

Run verify_positive_second_bockstein_symbols.py. No actual coefficients or ranks are selected or computed. The actual D-input annihilation is a separate geometric theorem, not inferred from this character calculation. Neither the actual A-input scalar nor any higher Bockstein is determined here.

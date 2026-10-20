# Ordered-root coefficient geometry: prerequisite extracts

These existing geometric arguments are included to close the ordinary-ideal hypotheses of the power-contraction unit. They are supporting lemmas, not new counted manuscripts or an actual-source comparison. Work on Z=(P1)^4, with A=O(1,1,1,1) and its natural permutation linearization. The three pairing weights have sum zero and the explicit differences below; equivalently the first two differences and the zero sum define all three weights. Fix harmless binary determinant lines throughout. Put Y=Sym^4(P1)=P4 and q:Z→Y. For the alternant coefficient statement let B0 be any locally free bundle on Y and E=q*B0⊗A^(-2). The weight ideal has the exact sequence 0→det(U)⊗A^(-1)→U⊗O_Z→I_D⊗A→0.

## Weight-difference ideal


Choose a common affine coordinate in which the four roots are finite. Every configuration admits such a coordinate: choose the omitted point of P1 away from its finite set of roots. Thus these charts cover Z, including infinity and all collisions.

Use the displayed normalization of the weight differences. Its differences are

    sigma_1-sigma_2 = 3(x1-x4)(x3-x2),
    sigma_1-sigma_3 = 3(x1-x3)(x4-x2),
    sigma_2-sigma_3 = 3(x1-x2)(x4-x3).

The third is a linear combination of the first two. Set a=x1-x4, b=x2-x4, c=x3-x4. Since 3 is invertible, the local ideal is

    I = (a(c-b), b(c-a)) in C[x4,a,b,c].

The equations say a=0 or c=b, and b=0 or c=a. Their four possibilities give

    (a,b), (a,c), (b,c), (a-b,b-c).

These are respectively the four triple-root diagonals, with the free translation coordinate x4. There is no fifth component supported on the quadruple-root diagonal.

## 2. Scheme-theoretic reducedness

The two quadratic polynomials a(c-b) and b(c-a) have no common irreducible factor in C[a,b,c]. Their ideal has height two, and they form a regular sequence. Its quotient is a one-dimensional complete-intersection Cohen-Macaulay ring, hence has no embedded associated primes.

For explicit generic reducedness, the gradients are

    grad(a(c-b)) = (c-b,-a,a),
    grad(b(c-a)) = (-b,c-a,b).

At a nonzero point of each coordinate axis these are independent. At (t,t,t), t nonzero, they become (0,-t,t) and (-t,0,t), also independent. Thus the scheme is reduced at the generic point of each of its four components. A Noetherian ring with no embedded associated primes and reduced localizations at every minimal prime is reduced. Therefore

    I = (a,b) intersect (a,c) intersect (b,c)
                         intersect (a-b,b-c).

Adding the free coordinate x4 preserves this equality. Changes of common affine coordinate and coefficient-line frame multiply the global section equations by units and identify the same global ideal. The local calculations on the covering charts prove the global reduced complete-intersection assertion.

## 3. Koszul resolution and character

The differences span U because sum sigma_i=0 and characteristic zero. The evaluation U tensor O_Z -> A has zero scheme D and is a regular sequence locally. Its rank-two Koszul resolution, twisted by A, gives the displayed exact sequence.

The action on U is the standard two-dimensional representation of S3 inflated through the action of S4 on the three pair partitions. Its determinant is the sign of that S3 permutation. An S4 transposition swaps two pair partitions, so the pullback of this determinant is precisely sign of S4. This identifies the permutation character of the first Koszul term without introducing an erroneous sign into A itself.

Tensoring the resolution by a locally free E preserves exactness. No S4 action on the fixed paired ambient is used; the coefficient bundle upstairs uses its actual geometric linearization.


## Regular alternant division and cubic ideal order


In fact any sign cochain in EA on the quotient-adapted affine cover vanishes on every pair diagonal, not just D. Let

    v = product over i<j of [l_i,l_j].

This is a global section of A³ carrying S4 sign. Its divisor is the sum of the six pair diagonals, each with multiplicity one. A sign-equivariant EA section vanishes on each pair diagonal because its transposition fixes that diagonal and acts trivially on EA there. On the smooth variety Z the six distinct prime divisors therefore divide that section jointly. Equivalently, multiplication by v identifies the invariant coefficient q*B0 A^(-4) with the sign coefficient EA after taking finite pushforward. Locally this is the familiar statement that an alternating regular function is divisible by the Vandermonde; smoothness and the effective Cartier divisor description prove that the quotient is regular globally. This is not a meromorphic prescription or an inversion of the ramification discriminant.

Along the small quadruple diagonal each of the six bracket factors lies in its ideal J, so every such sign cochain belongs to J^6 EA. Thus the weighted remainder's total sign projection has at least order six there, although the weight ideal alone only proves order two before using the full source action. This extra vanishing is universal for the sign coefficient and still imposes no restriction on its descended B0(-4) class. No equality of a chosen Vandermonde normalization with a chosen finite-duality trace normalization is asserted or needed.

### Sharp triple-diagonal ideal-power corollary

The three weight differences obey, in the source normalization,

    (sigma1-sigma2)(sigma1-sigma3)(sigma2-sigma3) = c v,

where c=±27, with its sign determined by the ordering of brackets. Indeed the three displayed root-product identities together use each of the six unordered root pairs exactly once. Both sides are global sections of A³, so their equality on common affine root charts is global. Consequently v belongs to I_D³ A³.

Every sign EA cochain is v times a regular invariant q*B0 A^(-4) cochain. It therefore belongs to I_D³ EA. For each k=1,2,3, inclusion gives a sheaf isomorphism

    (q_*(I_D^k EA))_sign ≅ (q_*EA)_sign,

and hence an isomorphism in every cohomological degree. This follows directly from equality of sign sections on quotient-adapted opens and does not assume that D's higher infinitesimal neighborhoods are reduced. Thus even cubic ideal membership is automatic in the full sign target; quadratic coefficient vanishing cannot by itself add a constraint.

The exponent three is sharp as a universal coefficient statement. Near a generic point of, say, Delta123, the fourth root is distinct, D has only that one component, and I_D is the smooth codimension-two diagonal ideal. Choose transverse coordinates a=x1-x3 and b=x2-x3. The three brackets among the equal roots give, up to units and sign,

    v = unit times a b (a-b).

The other three brackets are units there. The displayed degree-three polynomial is nonzero in Sym³(I_D/I_D²), so v belongs to I_D³ but not I_D⁴ at that generic point. Choosing a regular descended coefficient with nonzero value gives a sign EA section with exactly this order. Therefore automatic membership in I_D⁴ fails at the sheaf/cochain level. No assertion about the induced global H² map for I_D⁴ is made, and no claim is made about the order of the particular physical source.


## Trace normalization and cubic identity

Let t₂=Tr_F(σ²) and t₃=Tr_F(σ³), sections of O_Y(2) and O_Y(3) after fixing σ. On a generic fiber the values a,b,c sum to zero, so

  ab+ac+bc=−(a²+b²+c²)/2=−t₂/4,
  abc=(a³+b³+c³)/3=t₃/6.

Their cubic gives, for each of the three pairing sections σ_i on Z, the global relation

  σ_i³ − (q*t₂/4)σ_i − q*t₃/6 = 0.

It holds everywhere because both sides are regular sections of a locally free sheaf on the integral base and agree on a dense open. Equivalently this is Newton’s identity for the three pairing values, with full trace normalized to twice their sum.


Here full rank-six trace means twice the sum of the three regular pairing values; t2 and t3 are invariant sections and descend. The argument uses the polynomial identities, not an identification of a physical coefficient complex or an action of SL2 on HM.

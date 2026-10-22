# Independent review of the fourth-channel geometry

Reviewed: `FOURTH-GATE-SIX-AXIS-INVISIBLE-CHANNEL.md`.

## Verdict

**Pass, conditional on the stated reviewed inputs. No mathematical blocker found.**

The residual-conic calculation, the fifteen-product spanning construction added in Section 1a, the equivariant character calculation, the exact one-dimensional invisible kernel, and the one-axis first-ideal-sheaf-jet injectivity assertion all hold. The proof uses no selected Horrocks–Mumford coefficient, point coordinates, matrix, or actual gate rank. Its numerical statements concern universal linear series and representation multiplicities only.

I treat the supplied scheme description, the six-axis orbit, discriminant disjointness and invariance, and the stated fourth-family/square-kernel description as inputs. I have not independently revalidated the cited PRs or asserted anything about the actual corrected fourth class.

## 1. Residual sequences and the triple-octic dimension

The general-position assumptions suffice, without a stronger genericity hypothesis.

- Five of the points impose independent conditions on conics: to separate one of five points from the other four, use the union of the two lines through two disjoint pairs of the other four. No three collinear ensures the separating point is on neither line. Thus the conic through those five is unique up to scalar.
- That conic is irreducible, since a reducible or double conic containing five distinct points would contain three of them on one line. Over C an irreducible plane conic is smooth.
- It does not contain the omitted sixth point, by the no-six-on-a-conic assumption. Hence the six conics are distinct and each contains exactly its specified five points.

At a point of a smooth conic, choose its local equation as one regular parameter, say x. Then

    m^r : (x) = m^(r-1),
    (m^r + (x))/(x) = (y^r).

Consequently the displayed residual exact sequence and its restriction twist are correct. The multiplicities and restriction degrees independently check as follows:

| Step | Ambient degree and multiplicities before restriction | Conic | Restriction degree |
| --- | --- | --- | --- |
| 1 | (8; 3,3,3,3,3,3) | C6 | 16 - 15 = 1 |
| 2 | (6; 2,2,2,2,2,3) | C5 | 12 - (2+2+2+2+3) = 1 |
| 3 | (4; 1,1,1,1,2,2) | C4 | 8 - (1+1+1+2+2) = 1 |

The terminal residual is `(2; 0,0,0,1,1,1)`. Three distinct points impose independent conditions on conics, giving h0 = 3 and H1 = 0. Each restriction line bundle is O_P1(1), with h0 = 2 and H1 = 0. The long exact sequences, read backwards, give h0 = 9 and H1 = 0 for the initial triple-octic ideal sheaf. There is no unjustified surjectivity of global restriction: it follows at each stage from the H1 vanishing already established for its residual term.

## 2. Additional audit: the fifteen-product construction

The normalization `c_i(p_i) = delta(p_i)` is a valid equality in the common line-bundle fiber. Both sides are nonzero. It makes the chosen equations an actual permutation family, rather than a monomial representation with unknown scalar factors: applying g carries the equality to the normalization at gp_i, since delta is invariant, and uniqueness then gives `g c_i = c_(gi)`. The product P is consequently invariant.

Every F_ij contains four smooth conic factors through p_i and p_j, and precisely three conic factors through each other axis. Thus it has the claimed multiplicities and belongs to the triple-octic series.

The spanning argument covers all fifteen generators in successive groups of sizes 5, 4, 3, 3:

- The forms F_6i do not contain C6, so their restrictions there are nonzero. After the prescribed triple zeros are removed, the resulting degree-one section has an additional zero at p_i. Nonzero degree-one sections with different zeros span H0(O_P1(1)).
- The forms F_5i, for i = 1,...,4, contain c6; after dividing by it their C5 restrictions have the required residual zeros plus the extra zero at p_i. They likewise span the next degree-one quotient.
- The forms F_4i, for i = 1,2,3, contain c6 c5, and the identical argument applies to the third quotient on C4.
- The remaining three forms, divided by c6 c5 c4, are c3, c2, c1. Evaluation at p1, p2, p3 proves their linear independence, and the terminal residual space has dimension three.

No unstated transversality assumption is required. At each stage the restricted polynomial is nonzero, the prescribed zeros plus the specified extra zero already have the full available degree, and hence all those multiplicities are exact. Alternatively, any two distinct C_i and C_j meet at four different marked points, forcing transverse intersections by Bezout.

The residual kernels at each stage are ordinary polynomial divisibility by the relevant c_i. Thus backwards induction from the terminal basis genuinely proves that the products span the whole series, not merely that they span each quotient without controlling its kernel.

The induced permutation types on six axes are `(1)(1)(2)(2)`, `(3)(3)`, and `(1)(5)` for elements of orders 2, 3, and 5. Their numbers of fixed unordered pairs are 3, 0, and 0. The fifteen-generator character is therefore `(15,3,0,0,0) = 1 + P4 + 2 D5`. Subtracting the proved image `P4 + D5` gives relation module `1 + D5`. This is an equivariant construction of the image and its unique D5 isotypic summand; it does not normalize an isomorphism from an externally chosen model of D5 or determine the scalar of an actual fourth family.

## 3. Characters, stabilizers, and the line-bundle twist

The computation is valid for either of the two three-dimensional A5 representations: interchanging the two order-five classes changes none of the displayed characters.

The projective six-axis orbit is A5/D10. An involution fixes two axes, a nontrivial element of order five fixes one, and an element of order three fixes none. At an involution-fixed axis the line itself has eigenvalue -1, while the tangent and cotangent eigenvalue multisets are `{1,-1}`. At an order-five-fixed axis the line eigenvalue is 1 and the tangent/cotangent multisets are `{zeta,zeta^-1}`, with the choice of primitive zeta depending on the class and on A.

With the standard convention that P(A) parameterizes lines, the O(8) fiber character at an eigenline with eigenvalue lambda is lambda^(-8), not lambda^8. **This convention causes no correction here:** lambda is -1 or 1, so the twist character is 1 in every fixed-point calculation. The proof's even-power reasoning is therefore sound.

The length-six triple-point local algebra has filtration with associated graded pieces of degrees 0, 1, 2. Character traces can be computed on those pieces even without choosing equivariantly linear local coordinates.

- At an involution-fixed axis the trace is `1 + 0 + 1 = 2`.
- At an order-five-fixed axis the trace is `2 + zeta + zeta^-1 + zeta^2 + zeta^-2 = 1`.

Thus the triple-jet character is `(36,4,0,1,1)`.

The ambient character is `(45,5,0,0,0)`. In particular, for either order-five class the generating function can be written

    1/((1-t)(1-zeta t)(1-zeta^-1 t))
      = (1-zeta^2 t)(1-zeta^-2 t)/(1-t^5),

so its degree-eight coefficient is zero. The order-two generating function gives degree-eight coefficient 5, and the order-three generating function `1/(1-t^3)` gives zero.

The exact jet-evaluation sequence is valid because of the H1 vanishing in Section 1. Subtraction gives `(9,1,0,-1,-1)`, exactly the sum of the irreducible characters of P4 and D5. Semisimplicity over C gives the claimed module decomposition, with D5 multiplicity exactly one. Formally H0(O(8)) is Sym^8(A*); A is self-dual, so writing Sym^8 A does not affect this calculation.

## 4. The invisible kernel is an equality

Both required local identities are exact:

    m (x^2,y^2) = m^3,
    m^2 (x^2,y^2) = m^4.

The first follows because all four cubic monomials are products of x or y with x^2 or y^2. The second contains every degree-four monomial, including x^2 y^2. These are identities of ideals, not merely statements about initial forms. They are consequently independent of which allowed regular coordinate system expresses I_Sigma in the given normal form.

If square restriction vanishes, the input kernel description uniquely writes the family as delta times a degree-eight family. Delta is a unit at each axis, so multiplication by delta preserves, and induces isomorphisms on, the relevant local ideal-sheaf fiber/jet quotients, with the O(8) to O(10) twist included.

At every axis, zero ideal-sheaf fiber is exactly membership in m I_Sigma = m^3. Away from the axes both ideals are the unit ideal. Thus the global kernel is precisely the triple-point octic space, not a potentially larger or smaller subspace. Since Hom_G(D5, P4 + D5) has dimension one, the invisible equivariant channel has dimension one. The combined rank-three statement follows only for the universal test on Q, as claimed; it is not a statement about the actual gate's rank or value.

## 5. One-axis first ideal-sheaf jet

The one-axis datum must be the **entire linear map**

    D5 -> (I_Sigma,p / m_p^2 I_Sigma,p) tensor O(10)_p,

not the jet of one selected source vector. Zero of that map propagates to all six axes by equivariance and transitivity. A test on a selected source vector would not justify this propagation and is not proved here.

After dividing by delta, the residual octic belongs to m_p^4 at every axis. If an octic component did not contain C_i, its intersection multiplicity with C_i at the five smooth marked points would be at least 5 times 4 = 20, contradicting the total intersection number 16. Hence every C_i divides every nonzero residual component. The six conics are distinct irreducible polynomials; their degree-twelve product cannot divide a nonzero octic. All residual components therefore vanish.

This proves injectivity of square restriction together with that one-axis jet. It also proves that the unique invisible line has a nonzero cubic associated-graded jet at each axis. It does not prove that every nonzero source vector has nonzero jet there, and the note correctly does not make that stronger claim.

## Precision edits checked in the final revision

The author incorporated all three suggested clarifications, and I checked them in the final revision:

1. The convention `H0(O(8)) = Sym^8(A*)`, self-duality, and the inverse eighth-power fiber action are explicit. All computed traces remain unchanged.
2. The final paragraph of Section 4 now says “linear map with source D5” and explicitly distinguishes the entire family from a single source vector. The fiber at a single axis is naturally a stabilizer representation, not a representation of all G by itself.
3. The closing contrast with triple septics now includes the one-line justification: a septic triple at all six points meets each C_i with multiplicity at least 15 > 14, forcing all six conics as components and hence zero.

No additional coefficient computation, stronger position assumption, higher jet, or extra vanishing theorem is needed for the stated universal conclusions.

Publication context: this retained proof or audit may describe an intermediate bound or then-open branch. Read the unit overview for the current scope and later implications. Historical mathematical review is not a new formal verification.

# The canonical cyclic finite-dual defect has length at least 31

## Statement and hypotheses

Under all hypotheses of `../cyclic-dual-defect-constraint/PROOF.md`, including the canonical stabilizer and cotangent representation, one has

    length(Q) = length(P) >= 31.

Thus cyclic finite-dual lengths 1 through 30 are excluded. If the canonical thirty-point orbit occurs with cyclic finite-dual stalks, its contribution is at least 930. This is conditional on cyclicity; it does not improve an unrestricted global bound or establish existence at length 31.

More specifically, write P=(R/I) tensor chi and A=R/I. The earlier proof establishes that I is a complete intersection of four elements, I is contained in m², and its quadratic image has precisely the following possibilities:

- rank 0: length(A) >= 31;
- rank 2, opposite products: the final bound here is length(A) >= 32 (Section 6);
- rank 4, nonopposite mixed products: the final bound here is length(A) >= 38 (Section 7).

Sections 1–5 retain the intermediate bound 28 and its derivation. Sections 6–7 give the final bounds stated above.

Higher-order terms of the four equations are unrestricted. In particular this proof does not assume a homogeneous complete intersection, symmetric Hilbert function, or that the quadratic initial forms generate the whole initial ideal.

## 1. Equivariant Frobenius pairing

Let B=C5² be the canonical normal subgroup. Every character of H restricts trivially to B. Put W=m/m² and L=I/mI. Both determinant representations det(W) and det(L), being characters of H, are consequently trivial on B.

The top Tor of A computed from the complete-intersection resolution is det(L). Computed instead with the regular-parameter Koszul resolution of the residue field, it is Soc(A) tensor det(W). Hence

    Soc(A) = det(L) tensor det(W)^(-1)

as representations. In particular Soc(A) is one-dimensional and B acts trivially on it.

Choose a complex-linear functional lambda on A that is nonzero on Soc(A), and average it over B. The average remains nonzero on the socle and is B-invariant. The pairing

    (a,b) -> lambda(ab)

is nondegenerate: every nonzero principal ideal Aa contains a nonzero socle element. Indeed choose the largest n for which m^n Aa is nonzero; this nonzero space is killed by m and lies in the one-dimensional socle. Thus for a nonzero a some b satisfies lambda(ab) != 0. The pairing is B-invariant, so A is self-dual as a B-representation.

For any B-stable quotient U of A, let c_u denote its multiplicity at the B-weight u in F5². If K is the kernel, self-duality of A forces

    dim K >= sum_u max(c_u - c_(-u),0).                 (1)

To see this, for each pair {u,-u} the representation K must supply at least the multiplicity difference at the deficient member; sum over all pairs. Equivalently the right side in (1) counts each deficient pair once. The zero weight contributes zero. Additional zero-weight vectors known to lie in K give additive lower bounds beyond (1).

## 2. Notation for weight orbits

Write C for the four-weight multiset of W,

    C = {(i,3i²): i != 0}.

Write S for the square orbit and T for the opposite-product orbit:

    S = {(a,4a²): a != 0},
    T = {(0,1),(0,4)}.

Also write U0={(a,0):a != 0}. A minus sign on an orbit denotes weight negation. The six sets C, -C, S, -S, T, U0 are pairwise disjoint. Both T and U0 are fixed by negation; C and S are disjoint from their negatives.

The variables x_i have weights (i,3i²), for i=1,2,3,4. These definitions concern abstract character multisets, not actual model data.

## 3. Rank-four quadratic image: length at least 28

In this case the independent quadratic initial forms are

    x1*x2, x1*x3, x4*x2, x4*x3.

The existing filtered calculation proves that the associated graded algebra through degree three is exactly the polynomial quotient by (x1,x4)(x2,x3). Thus its pieces have the following B-weight multisets:

    degree 0: {0},
    degree 1: C,
    degree 2: S + T,
    degree 3: S + (-S).

For explicit verification of the last line, the pure cubic monomials in x1,x4 give weights

    (3,4), (1,4), (4,4), (2,4),

and the pure cubics in x2,x3 give weights

    (1,1), (2,1), (3,1), (4,1).

Their union is S plus -S. Consequently A/m⁴A, of dimension 19, has multiset

    {0} + C + 2S + (-S) + T.                           (2)

By (1), m⁴A must contain at least four dimensions at the weights -C and at least four at -S. These weight sets are disjoint and nonzero. Thus at least eight nontrivial-weight dimensions lie in m⁴A.

There is also a zero-weight socle dimension in m⁴A. To justify its location rather than just its existence, let s be the greatest index with m^s A nonzero. Since h3=8, s>=3. If s=3, the eight-dimensional m³A lies in Soc(A), a contradiction. Therefore s>=4; m^s A is the one-dimensional socle and lies in m⁴A. By Section 1 its weight is zero.

These nine necessary dimensions are independent, proving

    dim m⁴A >= 9,
    length(A) = 19 + dim m⁴A >= 28.

## 4. Rank-two quadratic image: length at least 31

Here the quadratic initial ideal is generated by x1*x4 and x2*x3. Set

    F = C[x1,x2,x3,x4]/(x1*x4,x2*x3).

Through degree two the associated graded algebra of A agrees with F. In degree three it is a quotient of F3 by a B-stable space E of dimension at most two. This includes all cancellations: choose the first two minimal generators with independent quadratic initials, and the remaining two in m³. A relation with order at least three must have vanishing constant coefficients on the first two generators. Modulo W times the quadratic image, its cubic part is therefore in the span of the cubic initials of the remaining two generators. This proves the dimension assertion even with arbitrary higher terms.

Direct monomial weights give

    F0 = {0},
    F1 = C,
    F2 = S + U0,
    F3 = C + (-S) + 2T',

where T'={(0,2),(0,3)}. For F3: the four cubes have weights -S; the eight surviving monomials of type x_i²*x_j, with j neither i nor -i, have weights C once and T' twice.

The space E is in fact H-stable, as the degree-three initial ideal and the quadratic-generated ideal are H-stable. The C4 subgroup permutes each of C and -S transitively, so an H-subrepresentation of F3 that meets either of these four-weight orbits has dimension at least four. Since dim E<=2, E contains neither C nor -S. Thus the quotient F3/E still contains the entire C orbit. None of F0,F1,F2,F3 has a weight in -C.

It follows that A/m⁴A contains two copies of every weight in C and no weight in -C. Its dimension is at least

    1 + 4 + 8 + (12-2) = 23.

Self-duality of A requires m⁴A to supply at least two copies of every weight in -C, hence at least eight dimensions. Therefore

    length(A) >= 23 + 8 = 31.

No exact classification of E or of its higher-degree consequences is needed.

## 5. Rank-zero case and conclusion

When the quadratic image is zero, the existing estimate gives Hilbert prefix at least (1,4,10,16) and length at least 31. Combining the three cases proves the stated lower bound 28, strictly improving 22.

All operations in this proof are abstract finite-group character arithmetic, finite-dimensional linear algebra, and local-algebra arguments. No source-model evaluation, actual input, physical matrix, rank instance, jet or residue calculation, external write, installation, or large computation was used. The only imported algebraic conclusions are those explicitly proved in the two supplied local-defect proofs; the new Frobenius and character arguments are proved here.

## 6. Refinement: the opposite-product case has length at least 32

In Section 4, h3>=10. Therefore the socle cannot be m³A: the last nonzero maximal-ideal power has degree at least four. The B-trivial socle lies in m⁴A, independently of the eight forced dimensions at the nonzero weights -C. Hence dim(m⁴A)>=9 and length(A)>=32. This refinement does not yet change the global bound of Sections 1–5.

## 7. A cubic weight gap improves the global bound to 31

The rank-four case can be sharpened further to length(A)>=38. Combined with rank-zero >=31 and rank-two >=32, this proves the stronger global statement

    length(Q) = length(P) >= 31.

The conditional thirty-point contribution is consequently at least 930. This supersedes the intermediate bound 28; all scope qualifications remain in force.

Here is the extra argument, including the filtered issue. We may complete R without changing lengths, generator representations, the associated graded algebra, or the socle. Average a lift of W into the maximal ideal to obtain B-equivariant formal coordinates. The resulting map from the power-series algebra on W to the completed regular local ring is an equivariant isomorphism: its induced graded map is the isomorphism Sym(W) -> gr(R). Thus homogeneous monomial weights can be used for every Taylor component in these coordinates.

In the rank-four case, L maps isomorphically to the quadratic initial space, whose weights are S0={(a,0):a!=0}. Choose B-eigenvector generators f_a lifting this basis. A variable has second weight coordinate either 2 or 3=-2. A cubic monomial therefore has second coordinate in {1,2,3,4}, never zero: the possible integer sums of three numbers ±2 are ±6 and ±2. Accordingly each f_a has zero cubic Taylor component. Write

    f_a = q_a + terms of order at least four,

where the q_a are the four mixed-edge monomials.

This implies that there are no additional degree-four initial relations. Indeed write an element g of I∩m⁴ as sum a_a f_a. Vanishing of its degree-two part and independence of q_a force every coefficient a_a to have zero constant term. The degree-three part is then sum of the linear coefficient components times q_a and must vanish. Because the f_a have no cubic terms and the coefficient constants are zero, the degree-four part of g is just sum of the quadratic coefficient components times q_a. It belongs to Sym²(W)J2. The reverse containment follows by multiplying the f_a by quadratics. Thus the degree-four initial ideal is exactly Sym²(W)J2.

The surviving degree-four monomials are the five in x1,x4 and the five in x2,x3. Their weights are respectively

    {(a,2):a∈F5},  {(a,3):a∈F5}.

This weight multiset equals C + (-C) + T', where T'={(0,2),(0,3)}. In particular h4=10 and dim(A/m⁵A)=29. Combining with (2), the prefix through degree four is

    {0} + 2C + (-C) + 2S + (-S) + T + T'.

Both T and T' are self-dual. Formula (1), now applied to the quotient A/m⁵A, forces at least four additional dimensions at -C and four at -S in m⁵A. Also h4=10 ensures that the last nonzero maximal-ideal power has degree at least five; otherwise the socle would have dimension at least ten. The B-trivial socle therefore lies in m⁵A and supplies an independent ninth dimension. Hence

    length(A) >= 29 + 8 + 1 = 38.

Together with the other two cases this proves the final universal cyclic bound 31.

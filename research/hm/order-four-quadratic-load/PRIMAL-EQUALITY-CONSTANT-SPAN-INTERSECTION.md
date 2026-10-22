# The surviving primal equality residuals are genuine constant-quotient subbundles

## Result and scope

For either surviving primal equality label

    G3.11.942927348917,   G3.12.8e9af2d08af9,

let V0=Sym10 W be the invariant constant span forced by equality and let C8=Sym8 W O(-2) be its eighth osculating bundle in E. Then

    E intersect (V0 O) = C8.                             (1)

The actual restriction of the annihilator Q* onto C8^perp=W O(-9) is surjective. Its kernel Qprime has rank11 and degree -36, and projection gives an exact bundle sequence

    0 -> Z=E/C8 -> (H/V0) O -> Qprime* -> 0.              (2)

Thus Z, of rank8 and degree -36 in a constant rank19 bundle, really has the inherited constant-connection Gauss filtration. The known ordinary residual kernel N=K/C7 has rank6, degree -30, and is contained in Z^-. Equality N=Z^- is not asserted.

This result applies to all retained scalar strata of these two labels. It excludes no further label and asserts no realization. The primal profile21 equality label was already excluded in the preceding annihilator theorem. The proof does not assume H0(Q*(1))=0 for profiles11/12.

## 1. The exceptional unrestricted channel

The preceding theorem PR750, commit4c6b0ab0eccb2d2df524f7f529e26f2771a91111 (PRIMAL-EQUALITY-ANNIHILATOR-FORCES-DUAL-DEGREE-ONE-SECTIONS.md), proves the following complete actual-source bound. For the actual negative Q* of rank13 and degree -54, the only eligible irreducible blocks with nonzero equivariant Hom into W O(-9) are

    W O(-9),   O(-10),   O(-28),                         (3)

and each Hom space is one-dimensional. This comes from the complete degree window[-42,-1], the two actual identities

    H1(Q*(-1))=M3=3Wp+3S+6T,
    H1(Q*)=M2=A+2V+3P+4D,

and center parity. It is not a selected formal splitting or a map-instance calculation.

The same theorem establishes that actual restriction p:Q*->V0* O takes values in C8^perp=W O(-9). A nonzero W O(-9) block is already enough to make p surjective. The issue is to exclude the O(-28) alternative before using the O(-10) argument.

For both labels the actual quotient is

    B=Q*/L=O6 + O(-4) + O(-8).

In particular there is an everywhere surjective equivariant bundle map Q*->O(-8).

## 2. The O(-28) block cannot coexist with this quotient

Suppose Q* contains a block O(-28). Subtracting its two H1 characters from M3 and M2 gives the remaining budgets

    H1 at twist -1: 2Wp+S+3T,
    H1 at twist  0: P+2D.

Every other block of Q* must satisfy both remaining componentwise bounds. Checking the previous complete26-block overlist leaves exactly these nine possible co-blocks:

    O(-10), O(-6), V O(-4), Wp O(-3),
    P O(-2), D O(-2), Wp O(-1), S O(-1), T O(-1).        (4)

This is a necessary overlist of individual co-blocks; we need not solve their multiplicities. In particular a second O(-28) is impossible.

None of (4) admits an equivariant map to O(-8). All but O(-10) have too high ordinary degree, and

    Hom_G(O(-10),O(-8)) = (Sym2 W)^G = 0.

Consequently the required surjection Q*->O(-8) would factor through the single O(-28) block. Any such line-bundle map is a section of O20 and cannot be everywhere nonzero: a nonzero section has a zero divisor of degree20, and the zero section is also not surjective. This contradicts the actual quotient. Hence

    Q* contains no O(-28) block.                         (5)

The accompanying exact verifier checks all nine co-blocks and their vanishing Hom spaces, including the multiplicity-one bound for O(-28). No orbit calculation or selected degree20 invariant is needed.

## 3. The remaining projection must be surjective

By (3) and (5), p is supported only on W O(-9) and O(-10). Suppose all W O(-9) components map to zero. If p=0, the full constant V0 O lies in E, contradicting H0(E)=0.

Otherwise all nonzero components of p are scalar multiples of the canonical inclusion

    O(-10) -> W O(-9) -> V0* O.

At a parameter line l in W this image has fiber l^10 in Sym10 W. Its apolar annihilator is l Sym9 W. Thus the ninth osculating bundle

    C9=Sym9 W O(-1)

would lie in the actual annihilator E of Q*. This contradicts H0(E(1))=0. Therefore some W O(-9) component of p is nonzero. Its map to W O(-9) is a nonzero scalar isomorphism, so p is surjective everywhere.

There is exactly one such source block: subtracting the H1 contributions of W O(-9) from the two actual budgets forbids a second copy, as the verifier checks. The projection kernel Qprime is locally free, has rank11 and degree -36, and Q*=W O(-9) plus Qprime as equivariant bundles. This splitting is a bundle splitting using a right inverse to p, not a splitting of any ambient connection; maps from other blocks can be absorbed into the graph defining Qprime.

## 4. Exact intersection and saturation

The image of Q* in V0* O is now exactly C8^perp. Taking fiberwise annihilators proves (1). Dualizing the surjective restriction sequence gives

    0 -> (C8^perp)* -> Q -> Qprime* -> 0,

where Q=(H O)/E. The image of V0 O in Q is precisely (C8^perp)*=V0 O/C8. Hence

    (H O)/(E+V0 O)=Qprime*

is locally free. Together with (1), this proves (2), including the saturated, locally free inclusion of Z in the genuine constant quotient. The connection used on that quotient is the ordinary constant connection, which descends because V0 is a fixed constant subspace.

## 5. What is established for the projected Gauss kernel

The earlier equality and residual quotient theorems give

    C8 intersect K=C7=Sym7 W O(-3),
    0 -> N=K/C7 -> Z -> O2+O(-8) -> 0.

Since E intersect V0=C8, the actual projection of K to H/V0 has kernel C7 and image N. Every local section of K has derivative in E. Constant projection commutes with differentiation, so the derivative of every projected local section of K lies in Z. Local lifts exist because K->N is a bundle surjection. Therefore N is contained in the actual projected Gauss kernel Z^-.

This proves a containment, not equality: additional sections of E could have derivatives lying in E+V0 without lying in E. No identification of the quotient O2+O(-8) with the actual projected Gauss quotient is made. The distinction must be retained in any subsequent argument.

## Reproduction

Run `python3 verify_primal_equality_constant_span_intersection.py`. It pins the preceding exhaustive annihilator theorem and certificate, the equality theorem and the ordinary residual quotient theorem. It independently rechecks their26 block contributions with exact Q(sqrt5) characters, lists the nine co-blocks permitted alongside O(-28), verifies their zero Hom spaces to O(-8), and checks the multiplicity and rank-degree assertions. It writes `primal-equality-constant-span-intersection.json`.

No frozen files, actual coefficients or actual-instance matrices are changed or evaluated. No further quotient label is excluded.

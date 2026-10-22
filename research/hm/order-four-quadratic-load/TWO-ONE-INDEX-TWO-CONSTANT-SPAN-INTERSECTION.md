# Source2: the constant-span intersection is exactly the forced osculating bundle

## Statement and scope

For stable ID **G3.21.d610e381ed75**, source index2, write the actual dual inclusion as

    Q* subset H* tensor O,    (H* tensor O)/Q*=E*.

The equality theorem PR733 (commit3349988b5c3fc82dbca0741fc1b5fe70af1c7d0d) forces an invariant constant subspace V0=Sym10 W and its eighth osculating bundle U=Sym8 W O(-2) inside Q*. Then

    Q* intersect (V0 tensor O) = U.                         (1)

The actual E contains exactly one W O(-9) block, and its restriction to U's annihilator is an isomorphism. Its complementary kernel E' has rank15, degree -36 and degrees in [-8,-2]. Consequently projection to the genuine constant quotient induces a saturated inclusion

    R=Q*/U subset (H*/V0) tensor O,                        (2)

of rank4 and degree -36, with quotient E'^*. Thus R legitimately has the constant-connection Gauss filtration of a subbundle of a constant bundle. This proves a new intersection and geometric realization of the abstract residual as an actual projected subbundle. It does not prove existence of the original quotient label and excludes no label.

## 1. An exhaustive actual-source Hom bound

The actual presentation and negativity give

    rank E=17, deg E=-54, top E<=-2,
    H1(E(-1))=M3=3Wp+3S+6T,
    H1(E)=M4=2V+4P+3D.

Every ordinary splitting degree therefore lies in [-22,-2], since the other sixteen degrees are at most -2. For any irreducible block rho O(e), its contributions to the two H1 characters are respectively rho Sym^(-e-1) W and rho Sym^(-e-2) W. They must be bounded componentwise by M3 and M4. The center fixes the parity of e.

The standalone checker lists every block satisfying these necessary bounds throughout the complete degree window. Among all such blocks, the only ones with nonzero equivariant Hom to W O(-9) are

    Hom_G(O(-10),W O(-9)) = C,
    Hom_G(W O(-9),W O(-9)) = C.                            (3)

The first is the canonical degree-one inclusion O(-10)->W O(-9); the second consists of scalar isomorphisms when nonzero. This support statement is proved from the actual H1 identities, not from a selected formal E splitting. The exhaustive block overlist suffices: every block of every actual E must appear in it.

## 2. The annihilator and the forbidden alternative

Use the invariant self-duality of Sym10 W. For a parameter line l in W, the eighth osculating fiber is l^2 Sym8 W. Under the invariant apolar pairing its annihilator is l^9 W. Hence inside V0* tensor O,

    U^perp = W O(-9).

Because E annihilates Q*, the actual projection E->V0* tensor O factors through U^perp. Suppose every W O(-9) component in (3) maps to zero. If the entire projection is zero, V0 tensor O lies in Q*, contradicting top Q*<=-2. Otherwise (3) says all its nonzero components are scalar multiples of the same canonical image O(-10)->W O(-9). The annihilator of this image in V0 is the ninth osculating bundle

    U9=Sym9 W O(-1).

Indeed the canonical image has fiber l^10, whose apolar annihilator is l Sym9 W. Therefore U9 lies in Q*. But Hom(O(-1),Q*)=0 from top Q*<=-2, again impossible.

Thus a W O(-9) block maps nontrivially and therefore isomorphically onto U^perp. In particular E->U^perp is surjective everywhere. Subtracting this block from E leaves rank15 and degree -36, still with top at most -2, so every remaining degree is at least

    -36-14(-2)=-8.

There is exactly one W O(-9) block, and all remaining blocks map to W O(-9) by zero, for ordinary degree reasons. The actual projection kernel E' is their equivariant direct sum. Taking annihilators now proves (1).

## 3. Saturation in the constant quotient

Dualize the surjective restriction sequence:

    0 -> E' -> E -> U^perp -> 0,
    0 -> (U^perp)* -> E* -> E'^* -> 0.

The image of V0 tensor O in E*=(H* tensor O)/Q* is exactly (U^perp)*. Therefore

    (H* tensor O)/(Q*+V0 tensor O) = E'^*

is locally free. Together with the exact intersection (1), this proves the exact bundle sequence

    0 -> Q*/U -> (H*/V0) tensor O -> E'^* -> 0.

This is the saturation assertion in (2). The constant quotient has rank19, and the residual has rank4 and degree -36. Its negativity also follows from the four possible residual types proved in PR738 (commit92c1580998dd5476458e32d8d6c2ca14a9c55edb).

## 4. What the projected Gauss kernel does and does not give

PR738 proves that the actual quotient Q*->B restricts on U to the top O6 evaluation, with kernel U7=Sym7 W O(-3). Consequently it induces a surjection

    R -> B/O6=O(-18)+O(-4)

with kernel S=L/U7, one of O(-8)+O(-6) or W O(-7). Projection to the constant quotient commutes with the constant connection. Every local section of L has derivative in Q*, so its image in R has derivative in R. Thus S is contained in the actual projected kernel R^-.

We do NOT identify S with R^-. Extra kernel could arise if the image of B meets the additional constant-subspace directions. Although (V0/U)(-2)=W O7 and quotienting its canonical O6 line gives O8, there is no automatic projection of all B/O6 to that line. No such projection or scalar description is assumed here. The next open step is to control this actual intersection, rather than assign a connection to an arbitrary bundle complement.

## Reproduction

Run `python3 verify_two_one_index_two_constant_span_intersection.py` to generate `two-one-index-two-constant-span-intersection.json`. The verifier pins the baseline row, actual-source theorem, equality theorem and dual residual theorem; lists the complete eligible E-block overlist; verifies (3), the symmetric-power identities, and the finite degree bounds. The geometric argument above supplies the actual intersection and saturation, rather than inferring them from characters alone.

No selected actual coefficients or points, matrices, actual-instance ranks, scans, spikes or consumed experiments are used. No prior frozen files are edited, and no quotient-label count changes.

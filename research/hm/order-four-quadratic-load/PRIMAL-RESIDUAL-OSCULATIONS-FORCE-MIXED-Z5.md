# Actual projected osculations force the mixed Z5 residual

## Result and scope

For both remaining primal equality labels

    G3.11.942927348917 (profile11),
    G3.12.8e9af2d08af9 (profile12),

the residual in the genuine constant quotient is necessarily

    Z=(V+P) O(-4) + O(-8),
    N=K/C7=T O(-5).                                      (1)

Thus only residual type Z5 remains, with its lower coefficient a nonzero and both upper coefficients alpha,beta nonzero. Types Z1,Z2,Z3,Z4 are excluded for these two labels. The corresponding actual E bundle is forced to be

    E=(P+D) O(-2) + (V+P) O(-4) + O(-8).                 (2)

These are necessary conditions, not realization. No quotient label is excluded here. The proof uses the actual projected derivative and its actual induced symbols; it never assumes N=Z^-.

## 1. The genuine constant quotient and actual projected flag

The preceding exact-intersection theorem supplies

    V0=Sym10 W subset H,
    E intersect (V0 O)=C8=Sym8 W O(-2),
    0 -> Z=E/C8 -> U O -> Qprime* -> 0,   U=H/V0.         (3)

Here dim U=19, Z is saturated of rank8 and degree -36, and Qprime is its actual annihilator. The restriction Q*->W O(-9) is split surjective as a bundle map, so Qprime is isomorphic to the complement of the unique W O(-9) block. The top-block splitting of C8 out of E proves top Z<=-2, in particular H0(Z)=0.

Write F0=K and F_j=F_(j-1)^- for the original actual flag, and C_k=Sym^k W O(k-10) for the first rational-normal chain. The honest-filtration theorem gives

    F_j intersect (V0 O)=C_(7-j),
    N_j=F_j/C_(7-j) subset Z,
    0 -> N_j -> N_(j-1) -> O(2-2j) -> 0,
    j=1,...,6,     N0=N,     N6=0.                      (4)

These are the heights(8,6,0) cases for both profiles11 and12. No profile21 height or vanishing condition is imported.

All inclusions in (4) are saturated in Z. The quotient constant connection is available because V0 is a fixed constant subspace. Since the original derivative sends F_j into F_(j-1) tensor Omega, constant projection gives

    derivative of N_j lies in N_(j-1) tensor Omega.       (5)

This can be checked on local lifts to F_j. A change of lift lies in C_(7-j), whose derivative lies in C_(8-j), and both are killed by the constant projection. Thus (5) is a statement about the actual embedded subbundles, not a chosen connection on their abstract bundle complements.

## 2. The actual induced symbols remain isomorphisms

Equality in the original envelope identifies

    Q_j=F_(j-1)/F_j=O(6-2j)+O(2-2j),   j=1,...,6.

For j=1,...,5, the actual symbol Q_(j+1)->Q_j tensor Omega is an isomorphism: under the equality identifications both are the same highest two HN lines. The C-chain supplies the first line and maps isomorphically onto that line. Quotienting that commutative symbol diagram by the first line therefore gives the actual isomorphisms

    N_j/N_(j+1) -> (N_(j-1)/N_j) tensor Omega,
    O(2-2(j+1)) -> O(2-2j) tensor O(-2),  j=1,...,5.     (6)

At the final step toward Z, the actual symbol Q1->A tensor Omega has image the two highest HN lines, where A=O6+O2+O(-8). Removing the first C-chain line yields

    N0/N1=O0 -> (Z/N0) tensor Omega
                    =(O2+O(-8)) tensor Omega,

isomorphically onto its highest O0 summand. This again follows from the original actual symbol, not from the containment N0 subset Z^- alone.

Let Y be the inverse image of O2 in Z/N0=O2+O(-8). Then

    0 -> N0 -> Y -> O2 -> 0,
    Z/Y=O(-8),      rank Y=7,      deg Y=-28.             (7)

## 3. The bottom line generates the actual osculating chain

By (4), N5=O(-10). Take a local nonvanishing generator v of this line in the constant bundle U O. Equation(5) places its derivatives in the successive bundles of (4). The everywhere-isomorphic symbols(6) show inductively that

    v, v', ..., v^(i)

span N_(5-i) for i=0,...,5, at every point. Indeed each new derivative has a nonzero leading class in the next line quotient; its leading class is obtained from the preceding one by an isomorphism in (6). The last symbol from Section2 gives the same assertion for Y at i=6. Changes of local parameter or generator are triangular changes of these spans and preserve them.

Consequently the actual order-i osculating bundles of N5 are exactly

    N5,N4,N3,N2,N1,N0,Y,                                (8)

with ranks i+1 and degrees (i+1)(i-10), for i=0,...,6. In particular there is no unproved saturation or generic-only rank assertion here: the symbols are isomorphisms everywhere, and every bundle in (8) is already saturated in Z and hence in U O.

## 4. A proper constant span is impossible

The inclusion N5=O(-10)->U O is determined by an equivariant coefficient map

    Sym10 W -> U.

Let V1 be its image, the constant polynomial span. Since Sym10 W=A+V+D is multiplicity-free and the sixth osculating bundle has rank7, the only possible nonzero span representations are

    A+D (dimension8),   V+D (dimension8),
    A+V+D (dimension11).                                (9)

Suppose dim V1=8. The saturated Y of rank7 lies in V1 O. It is also saturated there: V1 O/Y is the kernel of the bundle surjection (U O)/Y -> (U/V1) O. Thus the annihilator of Y inside V1* O is a line bundle of degree -28. Its equivariant coefficient is trivial because G has no nontrivial one-dimensional characters, though only its ordinary degree is needed below.

The actual Qprime annihilates Z and hence Y. Therefore restriction gives

    Qprime -> Y^perp inside V1* O,     Y^perp=O(-28).     (10)

The complete actual-source block bound, after subtracting the forced W O(-9) block, gives every splitting degree of Qprime at least -18. Explicitly its two H1 budgets are M3-W Sym8 and M2-W Sym7. Exhausting the original safe window[-42,-1] gives21 eligible individual blocks, none below -18. The standalone verifier checks this complete bound without choosing a formal Qprime splitting.

Thus (10) vanishes even as an ordinary bundle morphism. Taking actual annihilators forces the whole constant V1 O into Z, contradicting H0(Z)=0. Both dimension8 alternatives in (9) are impossible.

Therefore V1=Sym10 W and the coefficient map is an isomorphism onto this constant subspace.

## 5. Full span identifies the bundle, not just its characters

For the complete degree-ten system, the order-i osculating fiber at a line l in W is l^(10-i) Sym^i W. Multiplication therefore identifies its osculating bundle with

    Sym^i W O(i-10).

Applying this to the actual full coefficient span and (8) proves

    Y=Sym6 W O(-4)=(V+P) O(-4),
    N0=Sym5 W O(-5)=T O(-5).                            (11)

This is an explicit rational-normal osculating identification, not an assumed jet-bundle identity. From (7), the remaining extension splits because

    Ext1(O(-8),Y)=H1(Sym6 W O4)=0.

Averaging makes the splitting equivariant. This gives (1), exactly residual type Z5. Its quotient onto O2+O(-8) has a nonzero lower coefficient a, and the honest-filtration boundary cuts already require alpha*beta nonzero. Equivalently, the classified mixed kernel is precisely T O(-5). No scalar normalization is claimed to realize the actual map.

Finally C8 splits from the top degree -2 block of E, so E=C8 plus Z as bundles, giving (2). The derivatives used in the proof remain those of the genuine constant quotients, not those of these bundle splittings.

## Reproduction and remaining issue

Run `python3 verify_primal_residual_osculations_force_z5.py`. It pins the exact-intersection package and the actual equality, source, residual and honest-filtration theorems. It checks the complete21-block Qprime overlist by exact Q(sqrt5) character arithmetic, every projected rank/degree and symbol degree, all possible constant span dimensions, the annihilator degree obstruction, the resulting symmetric-power identifications and the extension vanishing. It writes `primal-residual-osculations-force-mixed-z5.json`.

The proof, rather than the finite arithmetic, establishes the actual symbol and saturation assertions. No actual-instance coefficients or matrix evaluations are used, no prior frozen files are changed, and N0=Z^- is not assumed or concluded. The next unresolved intersection is Z intersect (V1 O), not the already established Y subset Z intersect (V1 O).

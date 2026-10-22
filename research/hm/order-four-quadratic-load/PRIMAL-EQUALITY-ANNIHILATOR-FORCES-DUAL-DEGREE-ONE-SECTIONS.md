# Primal equality forces a dual degree-one section and excludes the profile21 equality label

## Result and scope

For each primal equality label

- G3.11.942927348917 (profile11, source70),
- G3.12.8e9af2d08af9 (profile12, source8),
- G3.21.45ca6278cbfc (profile21, source1),

the actual annihilator Q* necessarily satisfies

    Wp is a constituent of H0(Q*(1)).                       (1)

Consequently **G3.21.45ca6278cbfc is excluded**: its plateau index k=2 implies H0(Q*(1))=0. No exclusion of the other two labels is claimed. In particular, we do not impose that vanishing on profiles11 or12.

This is a universal constant-span obstruction using the actual source presentation. It requires neither actual coefficients nor a connection on an abstract residual quotient. It applies to every retained scalar stratum of the excluded label at once. Earlier ordinary filtered witnesses therefore do not assert realization by the actual connection.

## 1. Actual inputs and the forced constant span

Use the conventions of ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md: G is the binary icosahedral group, W its standard two-space, and the irreducibles in order are

    one, W, Wp, A, V, P, S, D, T,

of dimensions 1,2,2,3,3,4,4,5,6. They are self-dual. The actual sequence is

    0 -> Q* -> M3* O(-1) -> M2* O -> 0,
    M3=3Wp+3S+6T,     M2=A+2V+3P+4D.

In particular Q* has rank13, degree -54 and top degree at most -1, with

    H1(Q*(-1))=M3,   H1(Q*)=M2,
    chi_G(Q*(1))=M3-M2 W=-W-2S-3T.                       (2)

The equality theorem PR733, commit3349988b5c3fc82dbca0741fc1b5fe70af1c7d0d, proves for all three labels an actual invariant constant subspace V0=Sym10 W of H and the inclusion

    C8=Sym8 W O(-2) subset E intersect (V0 O).             (3)

It also eliminates the height(7,6,1) alternative for profile21, so (3) applies there without an additional choice. The bundle C8 is the eighth osculating bundle of the complete degree-ten rational normal curve. At a parameter line l in W its fiber is l^2 Sym8 W. Under the invariant apolar pairing on Sym10 W, its annihilator is l^9 W. Therefore inside V0* O,

    C8^perp = W O(-9).                                   (4)

Here Q* is the actual annihilator of E in H* O. Restriction to V0 thus gives an actual equivariant bundle morphism

    p: Q* -> V0* O

whose image lies in (4). This uses no identification of a residual connection and no equality assertion for E intersect V0.

## 2. Exhaustive dual block support

Equivariant splitting is legitimate by the splitting and averaging proof in the actual-source theorem. Every line summand of Q* has degree at least -42, since its other twelve degrees are at most -1 and the total degree is -54. Thus every irreducible block rho O(-j) has 1<=j<=42, parity fixed by the center, and satisfies

    j dim(rho)+(13-dim(rho)) <=54,
    rho Sym^(j-1) W <= M3,
    rho Sym^(j-2) W <= M2.                               (5)

The second contribution is zero for j=1. The inequalities are componentwise inequalities of genuine representations, so no cancellation between blocks is possible.

Exact character decomposition over this complete finite window leaves the following26 eligible blocks, expressed as j: rho:

    1: Wp,S,T;  2: V,P,D;  3: Wp,T;  4: one,V,P;
    5: W,Wp;    6: one,A;  7: W,S;   8: one,A;
    9: W;      10: one;   11: Wp;   16: one;
    17: W;     18: one;   28: one.

This is an overlist of possible individual blocks, not a realization claim. It includes every block of every actual Q*. Among these26, the only nonzero equivariant Hom spaces into W O(-9) are

    Hom_G(W O(-9), W O(-9)) = C,
    Hom_G(O(-10), W O(-9)) = C,
    Hom_G(O(-28), W O(-9)) = C.                          (6)

All three are essential in the unrestricted calculation; ignoring the O(-28) channel would not justify an exact constant-span intersection for profiles11/12.

Their twist-one H1 characters are respectively

    W Sym6 W = Wp+2T,
    Sym7 W = Wp+T,
    Sym25 W = W+Wp+S+3T.                                (7)

In particular each has a Wp constituent. Equations (5)-(7) are checked exhaustively by the accompanying standalone exact Q(sqrt5) verifier. They are finite universal character calculations, not empirical map tests.

## 3. The obstruction and the profile distinction

Suppose Wp does not occur in H0(Q*(1)). Equation (2), whose Wp coefficient is zero, implies that Wp also does not occur in H1(Q*(1)). By the genuine direct-sum decomposition and (7), none of the three supported blocks (6) can occur in Q*. Completeness of (6) then gives

    Hom_G(Q*, W O(-9))=0.

The actual restriction morphism p from Section1 therefore vanishes. Every vector in V0 is annihilated by every fiber of Q*. Taking the actual fiberwise annihilator shows

    V0 O subset E.

This contradicts H0(E)=0, which follows already from H0(E(1))=0. Hence (1) is necessary for all three labels.

The actual Gauss-persistence theorem, Section4 equation(12), gives

    H0(Q*(d)) nonzero implies k<=d.

For profile21, k=2, so H0(Q*(1))=0 and (1) is impossible. For profiles11 and12, k=1 and this implication provides no such vanishing. Those two labels are not excluded by this argument; they acquire the necessary constituent (1). We neither assert an exact intersection E intersect V0=C8 nor install a constant quotient connection for either surviving label.

## Reproduction and limits

Run `python3 verify_primal_equality_annihilator_degree_one.py`. It pins the original frontier row, actual-source theorem, equality theorem and equality certificate; exhausts all parity-compatible blocks in degrees[-42,-1]; verifies the26-block overlist, all Hom support and the twist-one characters; and writes `primal-equality-annihilator-forces-dual-degree-one-sections.json` with the single excluded stable ID.

The geometric proof supplies the actual annihilator implication. No actual-instance coefficients, evaluation matrices, ranks, scans or local experiments are computed. No frozen file is changed, no quotient connection is invented, and no other label or scalar stratum is excluded.

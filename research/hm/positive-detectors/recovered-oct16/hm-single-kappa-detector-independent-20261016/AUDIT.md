> Historical mathematical record, 16 October 2026. Statements of PASS and check counts below refer to the original recorded verification, not a new execution. See PUBLICATION-SCOPE.md at the common series root for current scope, imported premises, and source/public hash bindings.

# Independent proof: all constant rows at one harmonic position are incomplete

## Accepted result and exact scope

**PASS.** On the authenticated characteristic-zero full-deck-sign, D8-epsilon cohomology space of dimension32, all30 constant scalar maps evaluated at the **single** harmonic position

    kappa=(-1,-1,-3,-3)

have joint rank20 and common kernel dimension12. On its inversion-positive12-dimensional subspace, their joint rank is8 and their common kernel has dimension4.

An exact positive counterexample family is

    (G0,G1,G2)=(-v2 eta, eta, 0),
    eta in H^2(B(-4))^+,

equivalently the class `a(U-v2)eta` under the specified global epsilon splitting. Every nonzero eta gives a nonzero class annihilated by every one of these30 detectors. This is a statement about an entire four-dimensional cohomological subspace. It is not an evaluation, nonvanishing claim, or location assertion for the actual obstruction.

This proof does not test the family obtained by varying the harmonic position, nor determine its completeness. In particular a result requiring **all positions** cannot be weakened to this one position. The older full352-dimensional-sector kernel and its pure-positive description are different domain statements and are not substituted for the epsilon32 calculation here.

Here “constant scalar maps” means the original rows on the internal-degree−2 negative harmonic block. A functional on the finite model's separate positive80 block, such as a functional using its p[7] or p[25] coordinates, is not one of these30 rows and must not be identified with this family.

## 1. Authenticating all30 rows and the dual signs

The original classification is Section3 of [structural-relations.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-proof/structural-relations.md), commit `08b73637d4136f91606aad332c46cafd064417f8`, Git blob `d48c88141e80f0005cf598d4796d6f358d45f07a`. A fresh read-only retrieval was byte-authenticated against that blob; its local snapshot is included. We use the linear classification in Section3, not its source-evaluation claims elsewhere.

The constant row has coefficients alpha_(a,j) on the internal-degree−2 F20 block and beta_(i,c) on F31. Annihilation of the incoming degree−3 map is equivalent to

    alpha_(a,5c+k) + sum_i beta_(i,c) gamma_(i,a,k)=0.

There are30 arbitrary beta entries. Each alpha is independently determined, since ev contains two ordered copies of (v0,...,v4). This is a graph identity over the integers, not a numerical rank inference.

The genuine complex degrees are −1,0,1,2. The authenticated duality is

    Str(FE)=-tr(F20 E02)+tr(F31 E13).

Consequently E13[c,i]=beta_(i,c), while E02[j,a]=−alpha_(a,j). The above equations become exactly

    E02[5c+k,a]=sum_i E13[c,i] gamma[i,a,k].       (1)

These are the closed-degree+2 graph cycles K30 of the first-component certificate. Thus the original30 row parameters give all K30 cycles with the correct supertrace signs, not merely a subset or a dimension-matched unrelated space.

Let A=H²(B(-2)). The complete-Cech certificate identifies

    A = K30 / im(d5),
    im(d5)=span(e_a+e_(25+a), e_(10+a)+e_(20+a)), a=0,...,4.

The explicitly given quotient map Q and section onto coordinates0,...,19 prove that every class of A is represented by one of these constant cycles, and dim A=20. The omitted last10 coordinates are exactly the displayed boundary span. This uses the complete-domain d5 result; ordinary global-section closure alone would not suffice.

## 2. The fixed harmonic position and source weights

For the full-sign internal-degree−2 scalar target on Y=(P1)^4, the line is O(-4,-4,-4,-4). The harmonic exponent kappa has Serre-dual homogeneous monomial

    q=X3² X4² Y1² Y2².

This is the actual q in the independently authenticated global trace bridge. Put

    a=(X1Y2-X2Y1)(X3Y4-X4Y3),
    U=X1X2Y3Y4+Y1Y2X3X4,
    beta2=v2²-v1v3+2v0v4.

The specified splitting, including the full-sign O(-2) line, is

    V = H²(B(-3)) direct_sum H²(B(-4)) direct_sum H²(B(-5)),
    (G0,G1,G2) -> aG0+aUG1+aU²G2.                (2)

Its dimensions are20,10,2. The polynomial identity

    Alt(q a U^j)/Delta = 4 beta_j,
    (beta0,beta1,beta2)=(1,v2,beta2),             (3)

uses the canonical unnormalized trace. It is independent of which closed constant matrix E is paired with the source. Therefore its derivation applies to every E in K30, not only h,j,p,r.

For the row corresponding to E, the exact functional on (2) is

    D_E(G)=4 Tr_P4 Str((G0+v2 G1+beta2 G2)E).   (4)

All summands inside the parentheses belong to B(-3). Pairing with E in B(-2) lands in O(-5). Equivalently the dual tuple lies in B(-2), B(-1), B(0). The scalar multipliers have homogeneous degrees0,1,2, respectively. Thus (4) is global, preserves the complete complex, and has no affine-denominator or hidden source-weight change. The fixed genuine supertrace and total-Cech sign from the bridge are retained. No ordinary unsigned transpose is substituted.

## 3. Descent through complete boundaries and exact rank

Global polynomial multiplication commutes with both the End differential and the Cech differential. It is of cohomological degree0 and introduces no totalization sign. If E is a d5 boundary, its status means that E=d_tot H for a **complete** total primitive H, which may have nonzero lower Cech components. Then

    v2 E=d_tot(v2 H),
    beta2 E=d_tot(beta2 H).

It would be insufficient to multiply only a clipped/global-section witness. Complete-complex multiplication proves that both maps descend on hypercohomology:

    m1:A -> H²(B(-1)), e -> v2 e,
    m2:A -> H²(B),    e -> beta2 e.

Hence the dual family is precisely

    Phi:A -> V*, e -> 4(e,m1(e),m2(e)).          (5)

Its first component is4 times the identity. Therefore Phi is injective, and its image has dimension20, without computing either multiplication matrix or reranking a source matrix. The surjection K30→A ensures that all20 image dimensions really occur in the original30-row family. Perfect Serre duality then gives joint detector rank20 on V.

Equivalently define the surjective primal map

    F:V -> H²(B(-3)),
    F(G0,G1,G2)=G0+v2 G1+beta2 G2.              (6)

Surjectivity follows from G0 alone. Every class of A pairs perfectly with its target, so vanishing of all30 single-position detectors is equivalent to F(G)=0. Thus its entire kernel is

    {(-v2 eta-beta2 zeta, eta, zeta):
        eta in H²(B(-4)), zeta in H²(B(-5))},   (7)

which has dimension10+2=12. This also proves directly that the dual of multiplication is the same central multiplication on the primal twists; no unknown transpose coefficients are needed.

## 4. Inversion, the positive kernel, and the explicit counterexample

Inversion acts componentwise on (2), fixes a,U and all beta_j, and preserves the canonical Serre trace. The last assertion uses the even reversal of the five projective coordinates; there is no hidden character from the full-sign line or the four Cech factors. The established positive dimensions are8,4,0 on the three summands.

The same equivariance holds for (5) and (6). On A, the literal quotient action is four copies of −J5, with positive dimension8. Hence Phi(A)^+=Phi(A^+) has dimension8. Restricting all30 functionals to V^+ keeps exactly these positive dual components, proving rank8 and kernel dimension12−8=4.

Since H²(B(-5))^+=0, (7) specializes to

    ker(F|V^+)={(-v2 eta,eta,0): eta in H²(B(-4))^+}. (8)

Every eta≠0 is nonzero in the direct-sum second component, regardless of whether v2 eta vanishes. Under (2), equation(8) is exactly `a(U-v2)eta`. Its annihilation is also visible directly from (3):

    Alt(q a(U-v2))/Delta=4(v2-v2)=0.

The exterior/supertrace conventions matter for identifying E and the target, but they introduce no ambiguity into this scalar cancellation. One does not need to select a source representative, acquire eta's actual coefficients, or presume a nonzero multiplication rank.

For example, taking eta to be any one of the four Serre-dual basis classes to the specified C0,...,C3 gives four independent cohomological counterexamples. This defines their classes exactly; it does not assert that separate complete-Cech lifts or their source values have been produced here.

## 5. Verification and stopping boundary

`check.py` passes263 bounded checks. It authenticates the original classification's Git blob, independently reconstructs the explicit K30 quotient, verifies its section and full d5 reconstruction on all30 basis vectors, checks inversion compatibility and the complete positive8 projection/basis identities, and matches the saved quotient metadata. It checks multiplier degrees and reversal, plus the graph-pairing normalization for a wholly manufactured multiplication matrix.

No elimination, new rank run, actual multiplication matrix, source value, primitive coefficient, nonlinear source evaluation, or large solve is used. The factorization and rank proof are structural. The check does not treat a manufactured matrix as the actual multiplication action.

The input proofs are:

- `../hm-epsilon-projective-generator-bridge-20261016/THEOREM.md`, particularly Sections2–5;
- `../hm-detector-plus-first-component-20261016/THEOREM.md` and `positive-eight-maps.json`, including the complete incoming d5;
- `../hm-positive-twelve-detector-interface-20261016/THEOREM.md`, particularly Sections1–2;
- `../hm-projective-detector-dual-audit-20261016/AUDIT.md`, the prior independent sign/trace/quotient audit;
- the freshly authenticated original `structural-relations.md`, Section3 only.

The result corroborates the separately saved `../hm-pr80-scalar-completeness-independent-20261016/AUDIT.md`. It sharpens the single-position boundary; it does not replace the historical review of PR80's all-position completeness claim.

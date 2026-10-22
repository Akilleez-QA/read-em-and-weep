# Vanishing of the twist-two invariant classical equation term

## Result

Let X=P_stack(1,1,2,2), physical O(1)=O_wt(2), Gamma=SL_2(F_5), G the actual rank-two Serre bundle with det G=O(2), sigma its regular section, I=I_Z, and 2Z=V(I^2). Then

    H^i(O_(2Z)(2))^Gamma=0 for every i.

Consequently PR646's classical linearized equation complex

    F_eq=[B(-2) --ad_N--> B --tr(N·)--> O(2)]

in degrees 0,1,2 is invariantly acyclic. Here B=End_0(G) and N=J(sigma^2). Neither complex is claimed to be the full derived deformation theory, nor does this theorem evaluate the positive cubic obstruction.

## Pinned inputs and distinct contribution

The new result evaluates the twist-two residual groups left open by the classical equation-complex comparison. The different positive operator residue and frame-comparison problems remain separate.

1. [PR646 classical equation-complex comparison](https://github.com/Akilleez-QA/read-em-and-weep/blob/9945accf7172732a6fe1754c95187e97ce6f2845/research/hm/tangent-complex-comparison/PROOF.md) gives HyperH^n(F_eq)^Gamma=H^(n-2)(O_(2Z)(2))^Gamma and explicitly leaves the right-hand groups unevaluated.
2. [Actual square filtration](https://github.com/Akilleez-QA/read-em-and-weep/blob/fda26320ad77f6806916616048df7af09d21c768/research/hm/order-four-quadratic-load/POSITIVE-SECOND-BOCKSTEIN-SQUARE-FILTRATION.md), Section 1, establishes the globally uniform actual vertex filtration and relation bundle used below. It imports the constant actual Loewy layers and fiberwise regular initial-pair theorem. This geometric premise is retained as a dependency, not reproved here.
3. [Weighted-stack square sequence](https://github.com/Akilleez-QA/read-em-and-weep/blob/fda26320ad77f6806916616048df7af09d21c768/research/hm/order-four-quadratic-load/WEIGHTED-STACK-SQUARE-SHADOW-AND-PRIMARY-SCALAR.md) proves regularity, the ordinary-square sequence, and exact tame pushforward. The ordinary square must not be replaced by the square of a coarse annihilator.
4. [Actual midpoint bracket theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/fda26320ad77f6806916616048df7af09d21c768/research/hm/order-four-quadratic-load/MIDPOINT-NORMAL-EXTENSION-HAS-UNIQUE-SQUARE-ZERO-ADJOINT.md) proves the actual bracket H1(B(-2))^Gamma→H1(B)^Gamma nonzero between invariant lines, and H0(B)^Gamma=H0(O(2))^Gamma=0.
5. [PR645 invariant evaluation isomorphism](https://github.com/Akilleez-QA/read-em-and-weep/blob/9bbdc4582a75f6a3b36f84b071972dd8c5313d5e/research/hm/invariant-normal-defect-vanishing/PROOF.md) proves actual evaluation H1(B(-2))^Gamma→H1(G*)^Gamma is an isomorphism. Its pinned primary calculation gives H0(G*)=0, H1(G*)=1+V, H2(G*)=0.

## 1. The actual nonreduced filtration

Put R_2=pi_*O_(2Z)(2). Exact tame coarse pushforward preserves cohomology and equivariance. Its disjoint support components are the reduced conic C and vertex line L=P(W). This gives an actual decomposition into supported sheaves, not a splitting of vertex graded pieces.

Write + for physical inversion-even. At even physical twist two, source 2's positive vertex graded pieces are

    O_L(2), D5 tensor O_L, V8(2),

where V8 is defined by the exact sequence

    0 -> P4 O_L(-8) -> Sym^8 W' O_L(-4) -> V8 -> 0.       (1)

Intervening odd filtration pieces have negative physical inversion character. On the ambient coordinates V+W, the central involution of Gamma acts by +1 on V=Sym^2 W' and -1 on W, which is physical inversion. Thus these negative pieces have no Gamma-invariant cohomology. Local stack mu2 parity is different and has already been taken by pi_*.

On C, the positive part is O_C(2)=O_P1(4); the conormal part of the full first thickening is inversion-odd. This is the full filtered quotient, not a replacement of 2Z by its reduced support.

## 2. Invariant cohomology of every layer

The actual representation identities are

    H0(O_L(2))=Sym^2 W=A,
    Sym^4 W=D5,
    Sym^8 W'=P4+D5,
    H0(O_C(2))=Sym^4 W'=D5.

Here A,P4,D5 are nontrivial irreducibles of dimensions 3,4,5, and D5 is self-dual. Therefore O_L(2), D5 O_L, and O_C(2) have no invariant H0 and no H1.

Twist (1) by two:

    0 -> P4 O_L(-6) -> (P4+D5) O_L(-2) -> V8(2) -> 0.    (2)

Both left-hand terms have no H0. Equivariant Serre duality on P(W), with trivial det W, gives

    H1(P4 O_L(-6))=P4 tensor (Sym^4 W)*,
    H1((P4+D5) O_L(-2))=P4+D5.

Neither contains a trivial representation. For the first, its invariants identify with Hom(P4*,D5*), which is zero because the irreducible dimensions differ. Hence the invariant long exact sequence of (2) proves

    H0(V8(2))^Gamma=H1(V8(2))^Gamma=0.                    (3)

No rank or nonzero scalar of the actual arrow in (2) was required. In particular (3) does not assert nonequivariant acyclicity.

Invariants are exact over C. Successively apply invariant cohomology to the actual finite filtration. Every positive graded piece is invariantly acyclic, and every negative piece has no invariant cohomology by the central action. Therefore the whole vertex sheaf is invariantly acyclic, regardless of its extensions. The conic contribution is likewise invariantly acyclic. The disjoint-support decomposition proves the result. Dimension-one support supplies vanishing in degrees at least two.

## 3. Actual-map cross-check in degree zero

The square sequence is

    0 -> G*=G(-2) --m--> B -> I^2(2) -> 0.               (4)

The universal rank-two identity

    [T,J(sigma^2)]=J(2 sigma(T sigma))

makes the actual bracket the composite of evaluation e_sigma and 2m. PR645 proves H1(e_sigma)^Gamma is an isomorphism, while source 4 proves the composite bracket nonzero between invariant lines. Thus H1(m)^Gamma:H1(G*)^Gamma→H1(B)^Gamma is an isomorphism by the actual nonzero composite, not by dimensions alone.

Since H2(G*)=0, (4) gives H1(I^2(2))^Gamma=0. Since H0(G*)^Gamma=H0(B)^Gamma=0, and H1(m)^Gamma is injective, it also gives H0(I^2(2))^Gamma=0. The ideal sequence

    0 -> I^2(2) -> O(2) -> O_(2Z)(2) -> 0

with H0(O(2))^Gamma=0 and H1(O(2))=0 independently proves H0(O_(2Z)(2))^Gamma=0. The filtration proof supplies degree one without silently assuming vanishings of unknown higher terms in (4).

Conversely the theorem and positive-line-bundle cohomology imply H^i(I^2(2))^Gamma=0 for every i. Thus (4) identifies H^i(G*)^Gamma with H^i(B)^Gamma canonically through m in every degree.

## 4. Consequence and scope

PR646 now gives HyperH^n(F_eq)^Gamma=0 in every degree. In particular no invariant residual hypercohomology remains in degrees two or three of this specified classical linearized equation complex.

This does not make the local cokernel sheaf O_(2Z)(2) zero. Nor does it construct compatible inhomogeneous local lifts, supply omitted higher syzygies, identify a full derived deformation theory, or evaluate the distinct positive operator residue in omega_(2Z)(5). The midpoint's proved non-extension to the next thickening is compatible with this result. Full nonequivariant cohomology has not been computed.

No selected actual HM/source coefficient, point evaluation, matrix, rank test, numerical experiment, or large computation was used. This is a structural deduction from pinned geometric inputs, not a formal proof-assistant certificate. Independent review is recorded separately.

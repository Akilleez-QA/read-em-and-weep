# Independent mathematical review

## Verdict

PASS, relative to the stated pinned geometric and cohomological inputs. The deduction proves H^i(O_(2Z)(2))^Gamma=0 in every degree for the actual regular Serre zero ideal. No gap was found in the new deduction, its actual-map cross-check, or its restricted consequence for the classical three-term equation complex. This is a mathematical review, not a formal proof-assistant certificate or an independent reconstruction of the full HM foundation.

Reviewed on 2026-10-22. The review read PROOF.md and the preceding tangent-complex-comparison/PROOF.md in full. It also independently fetched, through the read-only GitHub connector:

- At fda26320ad77f6806916616048df7af09d21c768, the files POSITIVE-SECOND-BOCKSTEIN-SQUARE-FILTRATION.md, VERTEX-QUINTIC-RELATION-EXTENSION-AND-SQUARE-P4.md, WEIGHTED-STACK-SQUARE-SHADOW-AND-PRIMARY-SCALAR.md, and MIDPOINT-NORMAL-EXTENSION-HAS-UNIQUE-SQUARE-ZERO-ADJOINT.md under research/hm/order-four-quadratic-load/.
- PR645's research/hm/invariant-normal-defect-vanishing/PROOF.md at 9bbdc4582a75f6a3b36f84b071972dd8c5313d5e.

## 1. Actual thickening and filtration

The source filtration is explicitly the ordinary square of the actual regular ideal on the smooth weighted stack, followed by exact tame coarse pushforward. It is not the square of the coarse Ext-annihilator and is not the reduced support. At even physical twist d its positive vertex grades are O_L(d), D5 O_L(d-2), and Q4(d). Thus substitution d=2 gives precisely the draft's three terms. The draft's V8 is merely a renaming of source Q4; its definition by the exact relation sequence makes this unambiguous.

The source states uniformity at every vertex point and zero later positive grades, using the constant actual Loewy filtration and fiberwise regular initial pair. The second fetched source spells out the rank-four square relation bundle and its twist. Consequently no exceptional-fiber correction or unmentioned higher positive grade is needed, assuming those upstream theorems. This review does not independently reprove their deeper unique-module and initial-pair premises.

The conic and vertex supports are disjoint, so their supported sheaf summands separate. Within the vertex summand the argument uses finite exact filtrations, not a direct-sum splitting. In particular it never splits the explicitly nonsplit cubic/quintic relation extension.

## 2. The three parity notions

For the binary icosahedral representations, the center acts as minus identity on W and W', and hence plus identity on V=Sym^2 W'. On the ordinary cone coordinate space V+W its action is therefore exactly physical inversion. On O_(2Z)(2), which is induced from the structure sheaf and the canonical physical hyperplane linearization, this identification applies without a free choice of linearization. Gamma has no nontrivial one-dimensional character that could introduce a hidden twist.

The local stabilizer mu2 instead acts on the weight-one cover coordinates and has already been removed by the exact coarse pushforward. It must not be identified with physical inversion. The draft keeps this distinction correctly. Once the source's physical parity of each coarse graded piece is fixed, a negative piece has central eigenvalue -1 on all its cohomology and therefore zero Gamma-invariants. Even twist two is important here.

## 3. Independent line-cohomology check

Twisting the relation bundle by two gives

    0 -> P4 O_L(-6) -> (P4+D5) O_L(-2) -> V8(2) -> 0.

Both left terms have zero H0. On L=P(W), the canonical line is O_L(-2) with no determinant-character correction because det W is trivial. Equivariant Serre duality gives

    H1(P4 O_L(-6)) = P4 tensor (Sym^4 W)*,
    H1((P4+D5) O_L(-2)) = P4+D5.

The invariant part of the first is Hom(P4*,D5*), hence zero, since P4 and D5 are irreducible of different dimensions. The invariant part of the second is also zero. The invariant long exact sequence therefore gives both H0(V8(2))^Gamma=0 and H1(V8(2))^Gamma=0, independent of the rank of the map on the full cohomology groups. Dual conventions for P(W) do not affect this conclusion; W is self-dual.

The other positive pieces have H0 representations Sym^2 W=A, D5, and Sym^4 W'=D5, respectively, and no H1. None has a trivial constituent. Exactness of finite-group invariants over C and induction along the finite filtration give the claimed invariant acyclicity of the entire actual thickening. Its one-dimensional support supplies all higher-degree vanishings, also on the tame stack by exact pushforward.

## 4. Actual-map check

Twisting the regular square sequence yields exactly

    0 -> G(-2)=G* --m--> B -> I^2(2) -> 0.

The universal bracket factorization is ad_N=2m composed with evaluation, when m uses multiplication by sigma without the factor two. The earlier tangent-complex paper absorbs that factor into m instead. This harmless convention change is explicit and does not affect any induced isomorphism.

The midpoint source establishes a genuinely nonzero actual bracket between the invariant H1 lines. PR645 proves the actual evaluation map is an isomorphism onto H1(G*)^Gamma. Their composition therefore forces H1(m)^Gamma to be an isomorphism, rather than merely identifying equal dimensions. Combined with the stated H2(G*)=0, the exact sequence gives H1(I^2(2))^Gamma=0, and injectivity of H1(m)^Gamma gives H0(I^2(2))^Gamma=0. The ideal sequence then independently recovers H0(O_(2Z)(2))^Gamma=0. No unknown H2(B) vanishing is used to infer the degree-one quotient result; that result comes from the filtration.

For the converse all-degree ideal acyclicity, H0(O_X(2))^Gamma=0 is the source's quadric-ring assertion: the only ambient invariant quadratic is the defining quadric and is removed on Q. Higher cohomology vanishes by the positive line-bundle hypersurface sequence. Thus the converse deduction and the canonical all-degree isomorphisms through m are valid.

## 5. Comparison and scope

The earlier comparison has a correctly shifted triangle C -> F_eq -> O_(2Z)(2)[-2], with C invariantly acyclic. The present vanishing consequently makes precisely F_eq invariantly acyclic. This does not annihilate its nonzero local cokernel sheaf, establish compatible inhomogeneous local lifts, replace a prescribed bundle by a variable one, supply missing higher syzygies, or compute a full derived obstruction theory.

In particular there is no implication for the distinct positive residue in omega_(2Z)(5), and no contradiction with the midpoint bundle's failure to extend to the next thickening. The draft expressly preserves these limits.

No external writes, selected HM evaluations or matrices, actual rank tests, or numerical/large computations were performed during this review.

## Reviewed proof identity

SHA-256 of the final reviewed PROOF.md:

    8c8932d292db139b7ce21c72eee293f3e29aa7a6ec6303a4cd8fc6b94dd1e3cc

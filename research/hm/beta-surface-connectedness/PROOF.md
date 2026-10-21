# Fixed-beta surfaces: cohomology and mandatory residual intersection curves

## Inputs and distinction from the primary evaluation surface

Work over C on P4. Let E=F(3) be the rank-two Horrocks–Mumford bundle, with det(E)=O(5), and U=H0(E), dim U=4. Fix a three-dimensional subspace B of U and let X=X_B be the rank-at-most-one degeneracy scheme of B tensor O -> E.

The inputs from null's fixed-beta surface construction are that X has pure dimension two, is locally Cohen–Macaulay, and has the determinantal resolution

0 -> E(-10) -> 3O(-5) -> I_X -> 0.                         (1)

This follows for every B in that construction, independently of whether a beta sextic family exists. The standard HM cohomology used here is

h0(E)=4, h1(E)=2, H2(E)=0.                                 (2)

In the conditional beta-family application, an invariant integral component S of X has degree ten or fifteen. If its degree is ten, the other components have total degree five and are either one invariant integral surface or one transitive orbit of five distinct planes; all generic multiplicities are one. These classification inputs are not reproved here.

This X_B is the degree-fifteen fixed-three-section degeneracy surface, not the distinct primary evaluation rank-drop surface of PR564.

## 1. Structure-sheaf cohomology

**Proposition.** Every X satisfying these inputs has

h0(O_X)=1, h1(O_X)=2, h2(O_X)=1.

In particular X is connected and is not arithmetically Cohen–Macaulay.

**Proof.** Rank-two duality gives E*=E(-5), hence

(E(-10))* tensor omega_P4 = E.

Serre duality and (2) therefore give

H2(E(-10))=0, h3(E(-10))=2, h4(E(-10))=4.

The only nonzero cohomology of O(-5) is H4(O(-5))=C. The long exact sequence of (1) gives

H1(I_X)=0,
H2(I_X) = H3(E(-10)),
0 -> H3(I_X) -> H4(E(-10)) --a--> C3 -> H4(I_X) -> 0.       (3)

The map a is surjective. One can see its precise meaning without a rank experiment: retain the constant determinant factors in Hilbert–Burch. Before choosing a basis of B, its first map is

E* tensor det(E)^(-1) tensor det(B)
  -> (Lambda2 B) tensor det(E)^(-1).

After dualizing and tensoring by omega_P4=O(-5), this becomes

(Lambda2 B)* tensor O -> E tensor det(B)*.

The canonical identification (Lambda2 B)* = B tensor det(B)* identifies it with the evaluation map for B, tensored by det(B)*. On H0 it is consequently the inclusion B -> U, up to the same one-dimensional factor. Serre duality identifies a with the dual of this injective map. Thus a has rank three, and its kernel has dimension one. Equivalently, a must be surjective because H4(I_X)=H3(O_X)=0 for a surface; this supplies an independent consistency check.

Finally 0 -> I_X -> O_P4 -> O_X -> 0, together with the vanishing of positive cohomology of O_P4, yields

H0(O_X)=C, H1(O_X)=H2(I_X)=C2, H2(O_X)=H3(I_X)=C.

Here H0(I_X)=0 since X is nonempty. The alternating sum is zero, agreeing with the previously computed chi(O_X)=0. Absence of nontrivial idempotents in H0(O_X)=C gives connectedness.

An arithmetically Cohen–Macaulay projective surface has H1(O_X(n))=0 for every integer n: the sheaf/local-cohomology correspondence identifies this group with the degree-n part of H2 of its homogeneous coordinate ring supported at the irrelevant ideal, and a Cohen–Macaulay coordinate ring of dimension three has that local cohomology equal to zero. The nonzero group at n=0 therefore proves that X is not ACM. This is stronger than merely declining to assert ACM, and does not conflict with local Cohen–Macaulayness. QED.

## 2. Connectedness after deleting finitely many points

**Proposition.** If Z is any finite closed subset of X, then X minus Z is connected. Consequently every partition of the irreducible components of X into two nonempty unions has an intersection containing a curve.

**Proof.** Local Cohen–Macaulayness and pure dimension two imply depth O_{X,z}=2 at each closed point z. For j:X minus Z -> X, the local-cohomology characterization of depth gives sheaf local cohomology H_Z^0(O_X)=H_Z^1(O_X)=0. The localization exact sequence therefore identifies

O_X = j_* O_{X minus Z}.

Taking global sections yields H0(X minus Z,O)=C. A decomposition into two nonempty open-and-closed pieces would give a nontrivial idempotent, which is impossible.

If two nonempty unions Y1,Y2 partition the components and met only in a finite closed set Z (including the empty case), then after removing Z they would be disjoint nonempty closed subsets covering X minus Z. Each would also be open. They remain nonempty because every component is two-dimensional. This contradicts the preceding connectedness. Their intersection therefore has dimension at least one. Since they have no component in common, its dimension is at most one. QED.

The depth/local-cohomology implication is the one in Stacks Project, Lemma 47.11.1. The local connectedness mechanism is also explicitly proved in Lemma 51.3.1. No normality is assumed. The conclusion is connectedness in codimension one, expressed here by its precise finite-removal property.

## 3. Application to the degree-ten beta component

Recall first the reducedness consequence of the component classification. In either the degree-ten or degree-fifteen case every generic multiplicity of X is one. Thus X is generically reduced. Local Cohen–Macaulayness excludes embedded associated primes, so X is reduced.

In the degree-ten case define the canonical residual R by I_R=(I_X:I_S). Locally the radical ideal I_X is P_S intersected with the other minimal primes P_i. These primes are incomparable, so (P_i:P_S)=P_i for i distinct from S, while (P_S:P_S) is the whole ring. Hence

I_R = intersection of the P_i for the other components.

Thus R is exactly their reduced union. In particular X=S union R, both are nonempty, and they share no surface component. Proposition 2 gives

dim(S intersection R)=1.                                  (4)

This excludes both a disjoint residual and a residual meeting S only at finitely many points. It is a constraint on the actual canonical residual, not an inference about an arbitrary scheme with the same fundamental cycle.

If R is the orbit of five planes Pi_1,...,Pi_5, then S intersection R is the finite union of S intersection Pi_i. Equation (4) forces one of these intersections to contain a curve. For any i and j, choose a Heisenberg element taking Pi_i to Pi_j. Since it preserves S, it carries S intersection Pi_i isomorphically to S intersection Pi_j. Therefore

dim(S intersection Pi_i)=1 for every i=1,...,5.             (5)

This argument does not assume that different residual planes are disjoint or that their own incidence graph is connected. It only uses the invariant S, transitivity on planes, and the already established curve intersection with their union.

## Dependencies and limits

- Fixed-beta determinantal resolution and component alternatives: [PR543 surface proof at 26240e70230aef0de1f1b8714a06bd644adeec69](https://github.com/Akilleez-QA/read-em-and-weep/blob/26240e70230aef0de1f1b8714a06bd644adeec69/research/hm/order-four-quadratic-load/BETA-DEGENERACY-SURFACE.md).
- HM cohomology (2): [primary-image proof at d5d9bd997145b0ecf7d7bd659a19fb7845afb75f](https://github.com/Akilleez-QA/read-em-and-weep/blob/d5d9bd997145b0ecf7d7bd659a19fb7845afb75f/research/hm/actual-primary-image-extension/PROOF.md); also explicitly restated in [the ambient secondary-map proof at 4697da676f49f13eb74c2cc73d09db1406b71b37](https://github.com/Akilleez-QA/read-em-and-weep/blob/4697da676f49f13eb74c2cc73d09db1406b71b37/research/hm/order-four-quadratic-load/AMBIENT-BETA-SECONDARY-MAP.md).
- Depth and local cohomology: [Stacks Project, Section 47.11, Lemma 47.11.1](https://stacks.math.columbia.edu/tag/0AVY).
- Punctured-local connectedness: [Stacks Project, Section 51.3, Lemma 51.3.1](https://stacks.math.columbia.edu/tag/0FIV).

The new contribution is the exact cohomology triple, explicit non-ACM conclusion, and mandatory one-dimensional residual intersections. Reducedness and the radical colon description are recalled to make the precise scheme application self-contained; they are not presented as newly discovered here.

Beyond the reducedness stated above, no normality, smoothness, or Cohen–Macaulayness of S or R is asserted. Their scheme-theoretic intersection is not asserted reduced or pure-dimensional, and its degree is not computed. In particular the cohomology triple (1,2,1) does not identify X with an abelian surface. This does not exclude either beta degree alternative, classify ambient realization, establish Q4, give higher-order lifting, or prove algebraicity. The argument uses no selected HM/source-instance evaluation and no computational experiment. It is an ordinary mathematical proof, not a proof-assistant-certified result.

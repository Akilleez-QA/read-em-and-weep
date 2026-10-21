# Reduced determinant implies a reduced three-conic general section

Checked deduction from the Bănică–Manolache classification, 2026-10-21.
This is not a generic-moduli assertion; the argument uses no selected coefficient or rank evaluation.

## Result

Let E be a stable rank-two vector bundle on complex P3 satisfying

    c1(E)=-1, c2(E)=4, h0(E(1))=0, h0(E(2))=2.

Let s,t be a basis of H0(E(2)) and let S=V(s wedge t) be its determinant cubic. If S is reduced, then:

1. S is the union of three distinct planes.
2. A general nonzero section of E(2) has reduced zero scheme, a disjoint union of three reduced plane conics, one on each plane of S.

The conics are allowed to be pairs of intersecting lines. This note does not assert their smoothness.

In particular, an irreducible reduced cubic cone, including a cone over a nodal or cuspidal irreducible plane cubic, cannot be the determinant under these hypotheses. For an actual cone family whose generic base is known to be either irreducible or three distinct lines, the latter alternative is forced.

## Primary source and exact scope

C. Bănică and N. Manolache, *Moduli space M_P3(-1,4): minimal spectrum*, INCREST Preprint 19/1983.

Public source: https://imar.ro/~increst/1983/19_1983.pdf

The classification is stated on printed page 1, PDF page 7. It begins with bundles for which H0(E(1))=0 and treats the zero sets of sections of E(2), not merely the general bundle of a moduli component. It lists:

- Ferrand doubles of degree-three Cohen–Macaulay curves of Hilbert polynomial 3t+1;
- Ferrand doubles of certain degree-three Cohen–Macaulay curves of Hilbert polynomial 3t+2;
- a disjoint union of a conic and a suitable double structure on another conic;
- three disjoint conics;
- certain triple structures on conics.

The conics may degenerate, including to plane double lines. The exhaustive body summary occurs on printed pages 24–29, PDF pages 30–35. The additional doubled-plane-cubic case in that summary has h0(E(1))>0 and is expressly excluded by the hypotheses. The conic-plus-double-conic case is also described in Section 3, printed page 5/PDF page 11, including a degree-four structure supported on a line as a double of a degenerate plane conic.

Section 4, Lemma 1(ii), printed page 5/PDF page 11, gives the essential containment for a Ferrand double Y of X:

    I_X² subset I_Y subset I_X.

The source constructs such a double from a surjection I_X -> omega_X tensor L, where X is Cohen–Macaulay and L is invertible. The corresponding exact sequence is

    0 -> omega_X tensor L -> O_Y -> O_X -> 0.

The published 1985 Math. Z. paper's full text was not accessed; numbering here refers to this primary preprint.

## Proof

### 1. Every section is regular and has the same unique containing cubic

Put V=E(2). A divisorial zero of a nonzero section would give a section of E(2-d) for some d>=1, contrary to h0(E(1))=0. Its zero curve C is therefore a pure locally complete intersection of degree six, with omega_C=O_C(-1). There are no embedded components.

The regular-section sequence is

    0 -> O -> V -> I_C(3) -> 0.

Thus h0(I_C(3))=1. For any section in the pencil its unique cubic is the same S, since changing the basis of H0(V) only rescales its wedge. In particular, s wedge t is nonzero.

### 2. On reduced S, a general section has a multiplicity-one component on every surface component

On the smooth locus U=S_sm, the evaluation map H0(V) tensor O -> V has rank exactly one. Rank-zero points are singular determinant points. The kernel gives a morphism

    k: U -> P(H0(V)) = P1.

On each irreducible component of U this morphism is nonconstant: a constant kernel would give a section vanishing along an entire surface component, contradicting regularity. It is therefore dominant on every such component. In characteristic zero, generic smoothness gives an open set of P1 over which its fibers are smooth. Dominance and constructibility also permit this open set to be chosen with nonempty fibers on every component. There are finitely many components, so a common nonempty open set works for all of them.

These fibers are exactly C intersect U scheme-theoretically. Locally an invertible evaluation entry reduces the zero-section equations to the determinant equation and the kernel-ratio equation. Consequently a general C has, on every component of S, a curve component of multiplicity one meeting its smooth locus.

This statement does not assert reducedness along Sing(S); that is why classification is needed.

### 3. Exclude the wholly multiple types without overlooking embedded or non-Gorenstein bases

For a Ferrand double of a Cohen–Macaulay degree-three curve, localize its extension sequence at any generic point of its support. If the local Artinian ring of the underlying curve has length m, its canonical module has length m as well. The doubled curve consequently has length 2m at that generic point. Every curve-component multiplicity is therefore at least two, even when the underlying degree-three curve is itself nonreduced or non-Gorenstein.

For the triple-conic type, there is no ambiguity about multiplicities on a reducible base. Section 6, printed page 9/PDF page 15, defines tripling a locally complete intersection curve X by an invertible sheaf L using an intermediate double X' and the exact sequences

    0 -> L -> O_X' -> O_X -> 0,
    0 -> L² -> O_Y -> O_X' -> 0.

At each generic point eta of X, the two invertible modules have the same length as O_X,eta. Thus length(O_Y,eta)=3*length(O_X,eta). A smooth conic has multiplicity three; a reduced pair of meeting lines has multiplicity three on EACH line, not (1,5); a plane double line gives multiplicity six on its supporting line. These sequences were visually verified in the scan. Section 7, printed page 10/PDF page 16, independently lists the connected two-support-component cases as degrees (2,4) or (3,3). Lemma 4, printed pages 14–15/PDF pages 20–21, identifies the latter case, explicitly requiring multiplicity three along both meeting lines, with tripling their union by L=O_X. The final summary, printed page 29/PDF page 35, explicitly treats a double-line conic as giving a multiplicity-six line.

Thus type 5 has no multiplicity-one component. All these zero curves remain locally complete intersection, hence Cohen–Macaulay and unmixed; no embedded components can evade this generic-length argument.

Step 2 excludes the two Ferrand-double types and the triple-conic type for a general member of a pencil with reduced S.

### 4. Exclude the conic-plus-double-conic type using its cubic

Suppose C=Q disjoint union Y, where Q is a plane conic and Y is a Ferrand double of a plane conic Q'. This includes degenerate plane conics. Let h and h' be their respective plane equations. Since h belongs to I_Q and (h')² belongs to I_Q'² subset I_Y,

    h*(h')² belongs to H0(I_C(3)).

This is a nonzero cubic with a repeated plane factor. The one-dimensionality of H0(I_C(3)) forces it to be the determinant cubic up to scalar, contrary to reducedness of S. This type is impossible.

### 5. The remaining type forces three distinct planes and reduced conics

The classification leaves C=Q1 disjoint union Q2 disjoint union Q3, with each Qi a plane conic, initially possibly a double line. Let hi be its plane equation. The product h1*h2*h3 belongs to H0(I_C(3)), so equals the determinant equation up to scalar. Since S is reduced, the three planes Pi=V(hi) are distinct.

Take C in the open set from Step 2. For each i, its intersection with Pi minus the other planes is nonempty and smooth. The other two conics lie in the other two planes, so this intersection comes from Qi alone. If Qi were a double line, that intersection would be nonreduced wherever nonempty. Therefore no Qi is a double line. Each Qi is a reduced conic, and C is reduced as their disjoint union.

This proves both conclusions. This reasoning also handles a hypothetical double-line conic supported inside Sing(S): in that case its corresponding plane would have no contribution to C in its smooth locus, contradicting Step 2. One does not need any unproved assertion about the intersection length of a line with a nonreduced curve, nor any transfer from a generic bundle in moduli.

## Consequence for the actual cubic-base family

The following application uses the actual results in INVARIANT-HYPERPLANE-DETERMINANT-CUBIC-CONES.md, DETERMINANT-CUBIC-FAMILY-RATIONAL-SEXTIC.md, and DETERMINANT-CUBIC-FACTORIZATION-DICHOTOMY.md: the actual determinant surfaces are cones; the nonzero plane-cubic bases form the stated rational-normal-curve family in the projective space of plane cubics; the general base is reduced; and the corresponding bundles satisfy the hypotheses above.

For every parameter in that dense open locus, the theorem forces the base cubic to be a product of three distinct line equations. In particular, the irreducible reduced-base alternative is impossible, including singular irreducible cubics.

Let W be the three-dimensional space of plane coordinates. The multiplication morphism

    (P(W*))³ -> P(Sym³ W*),  ([l1],[l2],[l3]) |-> [l1*l2*l3]

has projective source, hence closed image. Its image is the Chow locus of completely reducible plane cubics, allowing repeated factors. Since the actual rational normal curve has a dense open subset in this closed locus, its ENTIRE projective image lies in that locus. Thus every member of the actual cubic-base curve is a product of three lines over the algebraic closure, and the factors are distinct for general parameter. Special parameters may have repeated line factors; no distinctness assertion at every parameter follows here.

This closure argument does not select or order the three factors, and does not assert that the factor cover splits rationally. It is compatible with an irreducible degree-three factor cover. Any further vertex-evaluation or rational-selection argument requires its own proof.

## What remains unproved here

- Generic smoothness of all three conics, rather than their reducedness.
- Product-generation of H0(Sym²E(4)) or its exact dimension.
- Any assertion about the distinct odd quadratic/quadric target.

The conclusion applies to a specific HM hyperplane restriction once its stated cohomology hypotheses and the reducedness of its actual determinant have been established. No moduli-density or genericity transfer is used.

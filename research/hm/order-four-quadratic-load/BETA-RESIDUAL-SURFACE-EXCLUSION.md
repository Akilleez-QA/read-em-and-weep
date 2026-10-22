# A normalization splitting obstruction eliminates the residual degree-five cycle

## Statement

In the residual beta setup, the degree-ten sextic-containing component alternative is impossible. Consequently the fixed-beta degeneracy surface supporting a general positive-dimensional sextic family must be reduced integral of degree fifteen.

This is not an exclusion of that integral degree-fifteen alternative and is not a complete proof repair.

The argument uses the established evaluation description, c2(E)=10H², the fixed-beta degree dichotomy, and an elementary quartic-section bound for an integral quintic surface. It does not assume that a residual component is normal, smooth, or Cohen–Macaulay.

## 1. General splitting obstruction

Let T⊂X_B be any integral projective surface, where X_B is the rank-at-most-one degeneracy scheme of B⊗O→E for a three-space B⊂U=H0(E), dim U=4. Suppose T∩C is finite, where C is the actual rank-at-most-one locus of full evaluation U⊗O→E. Choose a complementary section t so that U=B⊕⟨t⟩.

On T\C, full evaluation has rank two. The B evaluation has rank at most one by membership in X_B and cannot have rank zero: the kernel of full evaluation has dimension two, smaller than B. Thus it has constant rank one and its image A is a line subbundle of E|_{T\C}. The quotient Q=E/A is a line bundle. The image of t is nonzero at every point and hence trivializes Q. This produces a regular bundle map

p:E|_{T\C}→O_{T\C},    p(t)=1.

Let ν:T^ν→T be the finite normalization. It is projective, integral, and normal. The inverse image of T∩C is finite. Pulling p back gives a section of the vector bundle (ν*E)* on the complement of that finite set. A normal surface is S2; the Hartogs extension property applies to each local coordinate of a vector bundle section. Therefore this section extends uniquely to a global map

p^ν:ν*E→O_{T^ν}.

The equality p^ν(ν*t)=1 holds on the dense open and thus everywhere. Hence the map splits, and its kernel is a line bundle. Taking determinants gives

ν*E ≅ O_{T^ν} ⊕ ν*O_T(5).

The second Chern class of this split bundle is zero. On the other hand, Chern-class functoriality and the projection formula give

0 = deg(c2(ν*E)∩[T^ν])
  = deg(c2(E)∩[T])
  = 10 deg(T),

a contradiction. Here ν is birational, so ν_*[T^ν]=[T]. Chern classes of vector bundles and this projection formula are valid on singular projective varieties; alternatively one may pull the splitting to a smooth projective resolution of T^ν and use the same degree-one projection formula there.

Thus every integral surface T⊂X_B must meet C in positive dimension. Because C is a finite union of lines, T must contain at least one component line of C.

## 2. The invariant integral quintic residual is impossible

Suppose the residual degree-five fundamental cycle consists of one invariant integral quintic R. By Section 1 it contains a line L_i of C. Heisenberg invariance and transitivity on the 25 lines then imply C⊂R.

A general hyperplane section Γ of R is an integral curve of degree five. For i≥1, h0(O_Γ(i))≤5i+1: iteratively remove smooth points from a line bundle of degree 5i until its degree is negative, when it has no section. The hyperplane exact sequences then give h0(O_R(4))≤h0(O_R)+Σ_{i=1}^4 h0(O_Γ(i))≤1+Σ_{i=1}^4(5i+1)=55. Since h0(P4,O(4))=70, a nonzero quartic vanishes on R. As C⊂R, it vanishes on C, contradicting the established H0(I_C(4))=0. This bound does not require R to be normal or Cohen–Macaulay. For hyperplane integrality one may avoid its finite non-Cohen–Macaulay locus and apply Bertini.

Consequently no invariant integral quintic can occur as that residual cycle.

## 3. The orbit of five planes is impossible

The other residual degree-five alternative is an orbit of five distinct planes P_1,...,P_5 under the projective Heisenberg action. Each is an integral surface contained in X_B, so Section 1 makes it contain at least one line of C.

The union of the five planes is invariant. Once it contains one component line of C, transitivity forces it to contain all 25. An irreducible line contained in a finite union of planes lies in at least one individual plane. But a plane contains at most one of the component lines of C: two distinct lines in a plane meet, whereas the 25 lines are pairwise skew. Therefore the union can contain at most five of them, a contradiction.

## 4. Consequence for the beta branch

The fixed-beta surface theorem leaves either a degree-ten invariant integral component with residual cycle of degree five, or X_B itself reduced integral of degree fifteen. Sections 2 and 3 eliminate both possible residual degree-five cycles. The degree-ten alternative therefore disappears entirely.

Every surviving general fixed-beta surface in the sextic-family argument is consequently reduced integral of degree fifteen. Earlier results still force it into the exceptional singular locus; the normal-canonical exclusion and non-Cartier defect bound remain additional necessary conditions. No conclusion excluding singular nonnormal or normal noncanonical integral degree-fifteen surfaces is made here.

## Dependencies and boundaries

- The full evaluation degeneracy scheme is the reduced union C of 25 skew lines; evaluation has rank two away from C.
- c2(E)=10H² and det E=O(5).
- Fixed-beta surface resolution, purity, and the degree-ten/fifteen dichotomy: BETA-DEGENERACY-SURFACE.md, commit 26240e70230aef0de1f1b8714a06bd644adeec69.
- The elementary bound h0(O_R(4))≤55 for an integral quintic is proved directly in Section 2; no new quintic cohomology or resolution theorem is needed.
- H0(I_C(4))=0 and transitivity on the 25 component lines.

The general splitting obstruction does not assert that every component contains all C: that stronger conclusion requires invariance. No external writes, selected coefficient evaluations, matrix ranks, parameter scans, or prohibited experiments were used.

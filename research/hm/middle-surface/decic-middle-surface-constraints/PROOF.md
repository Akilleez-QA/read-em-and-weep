# The rank-at-most-five middle surface, if present, is a unique invariant integral decic

## Result and precise scope

Work over C, under the full conditional trilinear, bundle, generic-rank-ten, and normalizer hypotheses of /research/hm/rank-four/quintic-surface-classification/RANK_AT_MOST_THREE_COROLLARY.md. Write Z_s={rank Q<=s}, where Q has source rank ten, and let W be the reduced union of the two-dimensional irreducible components of Z_5.

If W is nonempty, then:

1. W is one integral N-invariant nondegenerate surface of degree ten. In particular there is at most one surface component of Z_5. This is uniqueness inside this rank locus, not uniqueness among all invariant decics in P4.
2. Its generic residual rank is either four or five. Its multiplicity m in the codimension-two singularity cycle of S=Ext^1(R,O) is in {5,6,7}; if its generic rank is four then m is in {6,7}.
3. A general scheme-theoretic hyperplane section C is an integral nondegenerate degree-ten curve in P3. Its arithmetic genus g is in {6,11,16}.
4. The Hilbert polynomial is

       P_W(t)=10 binom(t,2)+(11-g)t+chi(O_W),
       chi(O_W)=0 modulo 5.

No smoothness, normality, projective normality, or Cohen–Macaulay property of W is assumed or concluded. Existence is not asserted. Curves or isolated points of Z_5 outside W are not excluded.

## 1. Imported inputs

The following established results are used:

- Z_9 has dimension at most two.
- R is torsion-free of rank six and has the established locally free presentation; the total degree delta of the effective codimension-two cycle [S]_2 is at most seventy, and is divisible by five. See /research/hm/middle-surface/rank-ten-fitting-strata/ADDENDUM.md.
- At a generic point of a surface component of residual rank r, set j=10-r. Its coefficient lambda in [S]_2 satisfies

       lambda >= max(j,2j-6).

  This follows from the rank-six generator budget for (R**/R)_eta and local duality, and applies at every residual rank; see /research/hm/middle-surface/rank-one-middle-quintic-reduction/PROOF.md, Section 1.
- Every H5-equivariant coherent sheaf of proper support of dimension at most three has every integral-binomial Hilbert coefficient divisible by five. In particular each reduced H5-invariant union of surface components has degree divisible by five; see /research/hm/local-defect/heisenberg-defect-hilbert-congruence/PROOF.md.
- Every integral N-invariant quintic surface is excluded by /research/hm/middle-surface/rank-one-middle-quintic-reduction/SECTIONAL_GENUS.md together with /research/hm/rank-four/quintic-surface-classification/PROOF.md. The former proves sectional genus one without normality and the latter supplies the birational exclusion.
- dim Z_3<=1, by /research/hm/rank-four/quintic-surface-classification/RANK_AT_MOST_THREE_COROLLARY.md.

Here A=H5/Z(H5) is F5^2, and the projective normalizer is Gamma=A semidirect SL2(F5), with its standard conjugation action. Its SL2(F5) factor is perfect and acts transitively on the six one-dimensional subspaces of A. The representation V defining P4 is irreducible under H5.

## 2. Total reduced degree at most fourteen

At every generic point of W, r<=5, so j>=5 and lambda>=5. Additivity and positivity of degrees of effective cycles give

       5 deg(W) <= sum_(Y component of W) lambda_Y deg(Y)
                  <= delta <=70.

Thus deg(W)<=14. Since W is N-invariant, O_W is naturally H5-equivariant, and its degree is divisible by five. Therefore the positive possibilities are five or ten. We next prove irreducibility without assuming either possibility in advance.

## 3. An orbit argument eliminates all nontrivial component orbits

Consider the action of A on the finite set of irreducible components of W. Each orbit has size one, five, or twenty-five. Size twenty-five is impossible: every component has positive integer degree and deg(W)<=14.

Suppose there is an A-orbit O of size five. For a component Y in O its stabilizer L in A has order five, hence is a line in A. Because A is abelian, all components of O have precisely the same stabilizer L. For n in N, the translated orbit nO is another A-orbit of components of W, and its stabilizer is nLn^(-1). The standard SL2(F5) action carries L through all six lines in A. Orbits associated to distinct stabilizer lines must be distinct, and distinct A-orbits are disjoint. Consequently W would have at least six disjoint size-five orbits, hence at least thirty distinct components and degree at least thirty. This contradicts deg(W)<=14.

It follows that every component of W is individually A-stable and therefore H5-stable. Each such component has positive degree divisible by five. There can thus be at most two components.

The permutation action of N on this at-most-two-element set factors through N/H5=SL2(F5), since H5 fixes every component. The target is a subgroup of S2 and is abelian. Perfectness of SL2(F5) makes this homomorphism trivial. Hence each component is individually N-invariant.

If a component has degree five, the imported invariant-quintic theorem excludes it. Every component therefore has degree at least ten. The total degree bound fourteen allows exactly one component, and divisibility by five forces its degree to be ten. Since W is reduced, this proves that W is integral, N-invariant, and degree ten.

Its linear span is a nonzero H5-invariant subspace of V; irreducibility of V implies that it spans all P4.

## 4. Generic ranks and multiplicity

Rank is constant on a dense open subset of the integral surface W. Its generic rank is at most five and cannot be at most three because dim Z_3<=1. Thus r=4 or r=5.

Let m be its coefficient in [S]_2. Since 10m<=delta<=70, m<=7. When r=5, j=5 gives m>=5. When r=4, j=6 gives m>=6. This proves the asserted multiplicity lists. The contribution 10m to delta is consequently 50, 60, or 70, with 50 possible only at rank five. The remainder delta-10m is a nonnegative multiple of five bounded by 70-10m; no vanishing of that remainder is assumed. If m=7, the remaining codimension-two cycle vanishes, though lower-dimensional rank-drop support can still occur.

## 5. General hyperplane sections are integral and nondegenerate

The argument in /research/hm/middle-surface/rank-one-middle-quintic-reduction/SECTIONAL_GENUS.md, Sections 1–3, is degree-independent. Here are its essential details for this surface.

An integral surface is Cohen–Macaulay at every codimension-one point: a one-dimensional local domain has depth one. The non-Cohen–Macaulay locus is closed and therefore finite. A general hyperplane H avoids that finite set. Its equation is a nonzerodivisor on O_W; hence C=W intersect H is a Cohen–Macaulay curve, with no embedded associated points. Bertini irreducibility makes C irreducible; smooth Bertini on the smooth open subset of W makes it generically reduced. Thus C is integral. These are assertions about the scheme-theoretic section, not just its underlying set.

For references to the Bertini inputs see Stacks Project Lemmas 37.32.3 and 33.47.3:

https://stacks.math.columbia.edu/tag/0G4C
https://stacks.math.columbia.edu/tag/0FD4

To check nondegeneracy, if a linear form ell vanishes on C, the sequence

       0 -> O_W --h--> O_W(1) -> O_C(1) ->0

and H^0(O_W)=C imply ell|_W=a h|_W for a scalar a. Since W spans P4, ell=a h as ambient linear forms. Thus C spans H=P3. Its degree is ten. In particular its arithmetic genus g=h^1(O_C) is nonnegative.

Writing P_C(t)=10t+1-g and taking the difference P_W(t)-P_W(t-1) gives

       P_W(t)=10 binom(t,2)+(11-g)t+chi(O_W).

The H5 Hilbert congruence gives g=1 modulo5 and chi(O_W)=0 modulo5. The general hyperplane need not itself be invariant; the congruence is applied to O_W, not to O_C.

## 6. Arithmetic Castelnuovo bound and elimination of genus one

The arithmetic version of Castelnuovo's bound for an integral nondegenerate curve of degree d in P^r is

       p_a(C) <= (r-1) binom(q,2)+q epsilon,
       d-1=q(r-1)+epsilon, 0<=epsilon<=r-2.

A verified explicit statement, covering integral curves and arithmetic genus, is Rosa M. Miro-Roig, "Complete intersection liaison and Gorenstein liaison: new results and open problems", Le Matematiche 55, fasc. II, 319–337, Theorem/Definition 4.13 on printed page 331:

https://lematematiche.dmi.unict.it/index.php/lematematiche/article/download/275/252/1043

For d=10 and r=3, q=4 and epsilon=1, so g<=2*6+4=16. Combining with nonnegativity and g=1 modulo5 leaves g in {1,6,11,16}.

To exclude g=1, the proof in /research/hm/rank-four/quintic-surface-classification/PROOF.md applies in every positive degree, not only degree five. Explicitly, take a smooth projective resolution f:S->W of its normalization, and L=f*O_W(1). Then L is nef and globally generated, L^2=10, and a general pullback hyperplane D is smooth and integral and maps birationally to C. It is the normalization of C: the exceptional curves map to finitely many points of W, avoided by a general hyperplane, so D->C is finite birational. Therefore g(D)<=p_a(C)=1. Adjunction yields

       K_S.L=2g(D)-2-10 <0.

Nefness excludes any effective positive multiple of K_S. All plurigenera vanish, so the ruledness theorem makes S birationally ruled. Its ruled base has genus at most g(D)<=1: for a positive-genus base the ruling map extends across resolution, and D dominates the base because its intersection with a moving general ruling fiber is positive. Riemann–Hurwitz supplies the inequality.

The Gamma action on W is faithful on its function field, because an integral spanning surface cannot be fixed pointwise by a nonidentity finite-order projective transformation. A rational surface is impossible: Gamma contains the nonabelian subgroup A semidirect <u> of order 125, where u is an order-five unipotent in SL2(F5), whereas finite 5-subgroups of Cr2(C) are abelian (Serre's theorem cited and verified in the imported proof). An elliptic-ruled surface is impossible as well: Gamma acts on its elliptic base; perfectness kills SL2(F5) in the solvable group Aut(E), and [SL2(F5),A]=A kills A on the base. Faithfulness would then embed A=C5 x C5 into PGL2(C(E)), which is impossible over an algebraic closure since a finite abelian subgroup centralizing an element of order five lies in a one-dimensional torus and is cyclic. These arguments use no degree-specific classification.

Thus g=1 is impossible, and the final list is {6,11,16}.

## Boundaries

The conclusions are necessary constraints on a hypothetical surface component. They do not eliminate invariant decics, prove their existence, exclude dimension-seven independent-zero components, or classify the normalization. In particular neither chi(O_W) nor sectional arithmetic genus may be silently transferred to a resolution.

All statements remain conditional on the imported source/equivariance/bundle inputs.

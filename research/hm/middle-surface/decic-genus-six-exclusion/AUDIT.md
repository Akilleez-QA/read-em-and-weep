# Independent audit of the degree-ten, sectional-genus-six exclusion

## Verdict

PASS. I read the complete PROOF.md and independently checked each mathematical implication. The exclusion is valid over C, conditional only on the standard surface-theory results explicitly identified in that proof and the stated faithful action of G=(F_5)^2 semidirect SL_2(F_5). No counterexample or missing mathematical case was found.

The degree must be measured by the chosen polarization: explicitly writing O_Y(1)^2=10 in the generalized statement removes any possible ambiguity. This is automatic in the intended embedded-decic application.

## Detailed checks

1. **Group theory.** The commutator calculation with diag(2,3) correctly proves SL_2(F_5) perfect, since its upper and lower unipotents generate it. Commutators with -I fill A. Thus G is perfect. The standard two-dimensional module is irreducible; the centralizer C_G(A)=A; and A semidirect a unipotent subgroup is a nonabelian Sylow five subgroup of order125. These are the precise properties subsequently needed.

2. **Non-normal and singular Y.** Normalization is finite over C. A resolution of a normal surface has exceptional curves mapping to finitely many points. A general hyperplane avoids their images, though it need not avoid the non-normal locus of Y. Consequently the smooth pulled-back general curve D maps finite birationally to the integral section C, so it is its normalization. Bertini applies to the pulled-back basepoint-free hyperplane system; irreducibility follows because the morphism is birational onto a surface. Therefore g(D)<=p_a(C), without normality or Cohen–Macaulay assumptions on Y. Adjunction gives K_S.L=2g(D)-12<=0. None of the proof transfers arithmetic genus or Euler characteristic from Y to S.

3. **Faithfulness.** A faithful automorphism action on an integral variety is faithful on its function field. Passing through normalization, resolution, and birational models therefore preserves faithfulness as a birational action. In the nonruled case birational automorphisms of the smooth minimal model are regular. No equivariant contraction argument is needed. A group trivial on a fibration base injects into the automorphisms of the generic fiber; base change to the algebraic closure of its function field preserves injectivity.

4. **Ruled base and genus bound.** For positive-genus B, the ruling is intrinsic, since rational curves have constant image in B. A rational map from the smooth surface to B extends: resolve its indeterminacy and descend, because every exceptional rational curve maps constantly. A vertical irreducible curve has square<=0, whereas D^2=10; hence D is horizontal and Riemann–Hurwitz gives b<=g(D)<=6. This works equally when S is a blowup of a ruled surface.

5. **Rational and positive-genus ruled exclusions.** Serre's theorem excludes the nonabelian Sylow five subgroup in Cr_2(C). For b=1, Aut(B) is solvable, so G acts trivially on B and A would embed into PGL_2 of the geometric generic field. Such an embedding is impossible: the centralizer of an element of order5 is a one-dimensional torus, whose finite subgroups are cyclic. For b>=2, normality and irreducibility give K intersect A equal to 0 or A. The latter is impossible by the same fiber argument. The former implies [K,A]=1, hence K subset C_G(A)=A and K=1. Hurwitz then gives 3000<=420, a contradiction.

6. **Nonruled minimal model.** The standard ruledness theorem gives kappa>=0, and the smooth minimal model has nef K. The effective blowup discrepancy E has nonnegative intersection with the nef L. Thus q^*K is orthogonal to L. Since L^2>0, Hodge index makes its orthogonal complement negative definite; the nef q^*K has nonnegative square, forcing numerical triviality. A positive plurigenus is already supplied by kappa>=0. Any effective divisor of a numerically trivial pluricanonical section has zero intersection with an ample class and is therefore zero. Thus a positive multiple of K is trivial and kappa=0. This avoids any unmentioned abundance theorem. The four minimal projective complex types are precisely K3, Enriques, abelian, and bielliptic.

7. **K3.** The symplectic order5 fixed set has four points. Its commuting A-action on that set is trivial since 5 does not divide |S_4|. Faithful finite actions fixing a smooth point have faithful tangent representations, by analytic linearization. Symplecticness puts that representation in SL_2(C). An abelian finite subgroup there is simultaneously diagonalizable and its subgroup of exponent5 has order at most5. Hence no faithful symplectic A-action exists. Perfectness makes the G-action on the one-dimensional holomorphic two-form space trivial.

8. **Enriques.** The canonical double-cover lifts form a finite central extension by C_2. Because its quotient G is perfect, the extension's abelianization is a quotient of C_2. Thus its two-form character is trivial on every five-subgroup. A Sylow five subgroup maps isomorphically to a Sylow five subgroup of G; that subgroup contains the normal A. Its corresponding subgroup upstairs is therefore a faithful symplectic A-action on the K3 cover. The contradiction does not assume that the full lift extension splits.

9. **Abelian.** An automorphism has a well-defined linear part, and these parts form a representation rho. Its determinant is trivial by perfectness. A nonidentity order5 linear part would have eigenvalues zeta^a,zeta^-a, and real trace 4cos(2pi a/5)=sqrt(5)-1 or -sqrt(5)-1. This contradicts integrality of the trace on the preserved rank-four lattice. Thus all order5 elements have trivial linear parts. They generate G, so G acts by translations; that action is trivial because G is perfect. This reasoning does not incorrectly exclude ordinary abelian-surface automorphisms of order5, which can have a nontrivial determinant character.

10. **Bielliptic.** The intrinsic Albanese morphism has elliptic base and geometric generic genus-one fiber. G acts trivially on its base because Aut(B) is solvable. Over the algebraic closure of the generic field, choosing an origin identifies the full genus-one automorphism group as translations extended by a finite cyclic group. It is solvable; the perfect G therefore has trivial image, contradicting the already justified faithfulness.

## Source checks and limits

Independently opened the primary Serre paper at https://arxiv.org/pdf/0903.0514. Theorem5.1(i), PDF page13 (zero-based page12), states the required finite l-subgroup result for l>3. This is a structural theorem, not merely a bound on elementary-abelian rank.

Independently opened Huybrechts' author-hosted manuscript at https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf. Chapter15, Corollary1.5, printed p.309, gives the fixed-point formula; the table on printed p.310 explicitly gives four fixed points for order5. Its proof also derives the result from holomorphic Lefschetz. This is an authoritative independent check, not a claim to have opened Nikulin's original paper. The primary-paper citations supplied in PROOF.md for Nikulin's consequence and the Enriques/bielliptic structure remain appropriate.

The surface classification/minimal-model inputs are standard background theorems, not reproved in this audit. PROOF.md expressly discloses that dependency; it does not pretend that the linked lecture exposition is original classification research.

## Scope of conclusion

This audit verifies exclusion of sectional arithmetic genus at most6 under the stated group action and degree assumptions. It does not independently verify the earlier source establishing the candidate set {6,11,16}, nor prove existence of either remaining case. Applying the exclusion to that separately established candidate set leaves {11,16}.

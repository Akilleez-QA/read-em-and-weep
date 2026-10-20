# Independent audit: the genus-eleven deficiency closure

## Verdict

PASS over C. I independently reconstructed the argument and then reviewed the completed `decic-hyperplane-deficiency/PROOF.md`. Every substantive step is valid for the stated integral surface and integral scheme-theoretic general hyperplane curve. No smoothness, normality, local Cohen–Macaulayness of the surface, or Gorenstein hypothesis on the curve has been smuggled into the proof.

The result is genuinely stronger than a restriction on a possible deficiency module: every such H5-invariant decic with sectional arithmetic genus eleven is ACM. Combining this with the already audited full-normalizer ACM-decic exclusion rules out the full-normalizer genus-eleven case. This audit does not separately re-audit the original rank-locus reduction or the genus-six and genus-sixteen exclusions.

## Checks

1. **Low-degree equations.** I read Section 2 of the ACM-decic exclusion. Its prime-ideal and Bézout argument is independent of the ACM assumption and of full-normalizer invariance. H5 invariance alone gives dimensions divisible by five in degrees two and three. Two independent minimal-degree equations are coprime by primeness. A degree-ten surface cannot be a component of their complete intersection of degree at most nine.

2. **Linear normality.** The arithmetic Castelnuovo bound applies to integral singular curves, not only their normalizations. At degree ten in P4 it is nine. If five independent sections of O_C(1) exist, choosing them to include the four given embedding sections defines a closed immersion in P4: on every chart where one of the original sections is nonzero this map is the graph of the additional regular coordinate over the original embedded curve. Its image is nondegenerate, giving the contradiction.

   A small exposition addition is recommended: before using the four independent embedding sections, state explicitly that C is nondegenerate in its P3. Indeed H^1(I_Y)=0 because Y is integral projective and has only constant global functions, while H^0(I_Y(1))=0. The t=1 hyperplane ideal sequence then gives H^0(I_C(1))=0. This is an automatic consequence of the existing hypotheses, not a missing assumption or a substantive gap.

3. **Singular-curve duality.** An integral curve is Cohen–Macaulay. Its dualizing sheaf has rank one and is torsion-free, of Euler-characteristic degree twenty. A nonzero section of a rank-one torsion-free sheaf gives O_C -> F injective with zero-dimensional cokernel; its degree is the cokernel length. Thus negative degree permits no section, and degree zero permits at most one section, with equality forcing F=O_C. Applying this to omega_C(-2) and omega_C(-n), n>=3, proves exactly h^0(O_C(2))=10+epsilon, epsilon in {0,1}, and h^0(O_C(n))=10n-10 for n>=3. In particular no invertibility of omega_C is assumed; invertibility follows only in the epsilon=1 alternative.

4. **Surface representation squeeze.** Restriction gives 15 <= h^0(O_Y(2)) <=16. Its central character is the nontrivial square of the character on linear forms, so its dimension is divisible by five. Hence it equals fifteen, proving H^1(I_Y(2))=0. The preceding linear-normality argument similarly gives H^1(I_Y(1))=0. These two vanishings, not an unjustified restriction of equations, give I_C(2)=I_C(3)=0. The extra cubic section count and H^1(I_Y(3))=0 in the written proof are also correct, though not essential.

5. **Uniform position and quartics.** The characteristic-zero uniform position theorem applies to the general plane section of an integral curve even when the curve is singular. Its general plane avoids the finite singular set and meets the smooth locus transversely. Since I_C(2)=0 and H^1(I_C(1))=0, the ten plane points lie on no conic. Evaluation on conics has rank six; uniform position upgrades some independent six-point subset to every such subset. For any selected point, partitioning the other nine into five and four and multiplying the two separating conics gives a quartic separating that point. Thus h_Gamma(n)=10 for every n>=4.

6. **No saturation assumption.** For R=R_C and the plane equation ell, R is a domain, so ell is regular. The quotient R/ell R surjects onto the saturated coordinate ring of Gamma, whether or not it has saturation torsion. Therefore its degree-n dimension is at least h_Gamma(n), the direction of the inequality used in the proof. Starting with R_3=20 gives R_n>=10n-10 for n>=3, while restriction into global sections gives the matching upper bound. Consequently the complete Rao module is confined to degree two and has dimension epsilon<=1. Nonpositive degrees and degree one vanish as claimed.

7. **The crucial cohomology shift.** From the hyperplane ideal sequence, H^1(I_C(t))=0 for t>=3 makes E_(t-1) -> E_t injective, where E_t=H^2(I_Y(t)). Serre vanishing consequently gives E_2=0. At t=2, H^1(I_Y(2))=0 identifies H^1(I_C(2)) with E_1. This is only a vector-space identification, and the proof correctly does not claim that the chosen general hyperplane is H5-stable. The surface group E_1 independently has the primitive central character, so its dimension is divisible by five. Its dimension is at most one; therefore both groups vanish. This closes the purported non-ACM alternative.

8. **All twists and ACM.** With C ACM, the ideal sequence makes H^1(I_Y(t-1)) -> H^1(I_Y(t)) surjective for every integer t, and E_(t-1) -> E_t injective for every t. The second family vanishes by Serre vanishing. The first vanishes in negative twists since an inverse ample twist on an integral projective variety has no sections, and at degree zero since global functions are constants; surjectivity propagates it to all positive twists. Vanishing of both families in all twists is precisely the cohomological ACM criterion for a surface. It does not require local Cohen–Macaulayness as a prerequisite.

## Source verification

I opened Joe Harris, *Interpolation*, https://library.slmath.org/books/Book59/files/60harris.pdf . Printed page 168 states the equal-cardinality-subset Hilbert-function formulation of uniform position and its applicability to the general hyperplane section of any irreducible curve. The characteristic-zero scope is additionally explicitly confirmed by the research-paper abstract at https://arxiv.org/abs/1009.4021 . The former theorem is sufficient for the six-point conic-evaluation argument used here.

The arithmetic Castelnuovo source is recorded in Section 6 of the imported decic-middle-surface constraints. Independently, the numerical evaluation is 10-1=3(4-1)+0 and pi(10,4)=3*binom(3,2)=9. The existing independently audited ACM-decic exclusion establishes the final normalizer contradiction.

 No chosen source instance, external application, or source evaluation was used.

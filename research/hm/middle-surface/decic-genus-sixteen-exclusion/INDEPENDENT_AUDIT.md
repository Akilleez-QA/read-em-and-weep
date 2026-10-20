# Independent audit: the integral decic, sectional-genus 16 branch

## Verdict

The proposed argument is valid over an algebraically closed field of characteristic zero, for integral nondegenerate surfaces in P4, without normality or arithmetically Cohen–Macaulay hypotheses. At this stage this audits the proof strategy and its individual steps; a final draft check is recorded below when available.

The group-theoretic conclusion assumes the stated standard Heisenberg subgroup H5 acts on the ambient five-dimensional vector space, with primitive fifth-root scalar center, and preserves Y. Stability under its normalizer is more than sufficient.

## Detailed checks

1. A general hyperplane section C of integral Y is integral and nondegenerate of degree 10. Bertini applies to the very ample embedding. Nondegeneracy can also be seen from 0 → IY → IY(1) → IC,H(1) → 0 and H1(IY)=0, the latter following from H0(OY)=k. No normality is used.

2. If h0(OC(1)) ≥ 5, extend the four embedding sections by one independent section. These five sections give a closed immersion into P4, not merely a birational map. Indeed, on the chart where one of the original four sections is nonzero, the new map is the graph of the regular function given by the extra section divided by that section, over the original closed immersion. The image is nondegenerate, has degree 10, and retains arithmetic genus 16. The arithmetic Castelnuovo bound in P4 is 9: write 9 = 3·3 + 0, obtaining 3·binom(3,2)=9. Thus h0(OC(1))=4 and H1(IC,P3(1))=0.

3. The non-ACM genus inequality is particularly important. Let A be the saturated homogeneous coordinate ring of C and ℓ a nonzero linear form defining a general plane section Γ. Since A is a domain, multiplication by ℓ is injective. Put a(n)=dim(A/ℓA)n=hA(n)−hA(n−1). Saturating A/ℓA gives the homogeneous coordinate ring B of Γ, so a(n)≥hΓ(n). Both functions are eventually 10. For N sufficiently large, hA(N)=10N+1−pa(C), while hA(0)=1. Telescoping gives

   pa(C)=Σ[n≥1](10−a(n))≤Σ[n≥1](10−hΓ(n)).

   The summands 10−a(n) need not be nonnegative; this causes no problem. All sums terminate. Replacing this inequality by an equality before proving ACM would be an error; the stated strategy does not do that.

4. General linear position of Γ follows from the uniform position principle in characteristic zero. For ten points in P2 with no three collinear, products of n lines interpolate arbitrary values on any selected min(10,2n+1) points: for each selected target, partition the other points into pairs and possibly one singleton, choose lines avoiding the target, and multiply. Extra factors avoiding the target raise to exact degree when needed. Consequently hΓ(n)≥min(10,2n+1). The genus upper bound is 7+5+3+1=16. Equality of genus with 16 forces hΓ(2)=5, hence precisely one independent conic contains Γ.

5. The ideal restriction sequence 0 → IC,P3(1) → IC,P3(2) → IΓ,P2(2) → 0 is exact: the hyperplane equation is a nonzero divisor on OC. Vanishing H1(IC(1)) lifts the conic to a quadric containing C.

6. The sequence 0 → OY → OY(1) → OC(1) → 0 gives h0(OY(1))≤1+4=5. Ambient nondegeneracy gives the reverse bound. Thus Y is linearly normal and H1(IY,P4(1))=0. The analogous ideal restriction sequence lifts the quadric containing C to a quadric containing Y. This argument neither assumes nor concludes normality.

7. Every nonzero quadric in IY is irreducible: if it factors into linear forms, primeness of IY forces a linear equation of Y, contradicting nondegeneracy. Two independent quadrics in IY would therefore be coprime. Their complete intersection is a pure degree-four surface and cannot contain the integral degree-ten surface Y as a component. Hence 1≤h0(IY(2))≤1.

8. The space IY(2) is H5-stable. Its one-dimensionality already contradicts the central action: every one-dimensional representation is trivial on commutators, whereas the central commutator acts on degree-two forms by ζ^2 or ζ^(−2), according to the dual-action convention. Either is nontrivial. Equivalently, the nontrivial central character forces every such representation to have dimension a multiple of five. The latter can be proved using the five eigenvalue orbits of the standard two Heisenberg generators.

## Independently checked sources

- Joe Harris, *Interpolation*, MSRI Publications 59 (2011), pp.167–168: Theorem 2.1 gives hΓ(n)≥min(rn+1,d); the next page states the uniform-position fact for general hyperplane sections and the Castelnuovo bound. https://library.slmath.org/books/Book59/files/60harris.pdf
- Joe Harris's 2011 algebraic-curves lectures, notes by Akhil Mathew, Lecture 12, Proposition 12.1, p.59: a general hyperplane section of an irreducible nondegenerate curve is in linear general position. https://staff.math.su.se/shapiro/UIUC/curvesHarris.pdf
- Paola Bonacini, *On the plane section of an integral curve in positive characteristic*, arXiv:1009.4021, introduction and Definition 2.1: explicitly states the characteristic-zero theorem for integral (not necessarily smooth) space curves, with the truncated Hilbert-function formulation. https://arxiv.org/abs/1009.4021

Source caution: Harris's *Interpolation* p.168 prints an intermediate Hilbert-difference inequality with the opposite sign from the coordinate-ring argument. The final genus inequality is correct. Use the independent telescoping derivation above rather than copying that intermediate sign.

## Final-draft audit (2026-10-19)

Reviewed PROOF.md in full, including its imported integral-hyperplane argument from /research/hm/middle-surface/decic-middle-surface-constraints/PROOF.md, Sections 5–6. **PASS, with no mathematical correction required.**

The final draft improves on the initial outline: equality in the non-ACM Hilbert-function estimate directly yields dim(B2)=5 and dim(R2)=9, hence h0(IC(2))=1. It therefore avoids a separate plane-conic lifting argument. Surface linear normality then makes restriction on quadratic ideals an isomorphism, giving h0(IY(2))=1 directly. The independent degree-four complete-intersection argument is correctly labeled optional. The Heisenberg invariant-line contradiction is sufficient.

Also checked the downloaded source text: Bonacini Theorem 2.4 explicitly covers integral space curves in characteristic zero; Miro-Roig Theorem/Definition 4.13 explicitly bounds the arithmetic genus of integral nondegenerate curves. Thus there is no smoothness/geometric-genus substitution in the source use. The proof correctly excludes only genus sixteen, leaving the conditional possibilities six and eleven; it does not exclude all invariant decics.

# Independent mathematical review

Verdict: PASS for the stated target reduction, relative to the explicitly pinned actual-frame and factorization inputs. This review does not claim a value of the scalar or the fourth Bockstein, or reprove the cited geometric dependencies.

## Checks

1. In the actual weighted frame, a matrix with diagonal degree d has off-diagonal degrees d-2 and d+2. Multiplication respects weighted degree: the off-diagonal shifts cancel in a trace or a diagonal product. The minimum regular matrix degree is -2. Thus the use of a potentially negative weighted order for K is necessary and correct.

2. The harmonic coefficient B_r has binary degree equal to the sum of its input degrees minus 4r, since the fixed equation q has binary degree four. This is a homogeneity statement, valid without an explicit third-product formula. Entrywise extension to a completed series retains the bounds. The proof does not identify the actual filtered regular pair with its homogeneous leading pair.

3. From F0=a^2 h and the regular scalar F1, the three terms in L1 have lower bounds 8,8,8. The non-L2 terms in the q^2 square equation have lower bound sixteen. At a hypothetical lowest L2 degree d<4, only a^2 h tr(n8 (L2)_d) can enter degree 12+d. The graded coefficient ring over C(L) is a domain, so cancellation is legitimate. With n8 represented by a regular pair f3,g5, reduction of 2 f3 g5 x+g5^2 y-f3^2 z=0 modulo f3 and g5 gives y=f3 y1 and z=g5 z1. The resulting degrees d-5,d-3 are negative for d=-2,0,2. This proves the claimed lower bound four. Higher terms of n do not affect the lowest-degree argument.

4. There are eight ordered contributions to the cubic harmonic square coefficient with indices i,j in {0,1,2} and i+j+r=3. Each has lower bound twelve. The arbitrary fourth correction contributes a^3 h tr(nK), with only lower bound ten. Its inclusion prevents the unsupported stronger estimate S4>=12. The actual factorization from PR691 and nonzero leading h then imply rho4 has generic vertex order at least six, without treating h as a local unit.

5. The polynomial decomposition of physical-positive sextics has binary degrees 0,4,8,12. Generic order six kills the first two coefficient polynomials identically on the integral vertex line. This is a statement about locally free polynomial coefficient bundles, not extension of a section of the nonreflexive square ideal. Thus zeros of the chosen source a create no exceptional low-degree coefficients. The conic restriction is injective on the pure-positive degree-twelve block and zero on the other three blocks. Smooth-locus square-ideal membership therefore eliminates precisely that last block.

6. The remaining ambient polynomial block has dimension 9 times 3, namely 27. It need not belong to the vertex square ideal. The proof correctly distinguishes this reduction from proving square-zero for J4, computing beta4, or establishing algebraicity.

## Verification status

The bounded universal bookkeeping verifier was independently executed and passed. It checks the eight cubic product indices and their degree bounds, the retained fourth-correction bound, the three low kernel degrees, and the polynomial-block dimension. It is not a proof-assistant formalization or a substitute for the cited actual-frame geometry. No selected HM/source coefficients, points, derivatives, matrix ranks, or large computation were evaluated. No external repository changes were made during this review.

Reviewed final PROOF.md SHA-256: `aafb8a9c44d538ba99ff67ad184a439b239bed478234818642bcbfd62a1a02a4`. This version includes the explicit A and D5 source domains and the immutable harmonic-decomposition reference.

# Independent mathematical review

## Reviewed artifact and verdict

Reviewed `PROOF.md`, SHA-256 `dcbfb09e295658ed37152178119c9ab352bc7206fcb97429cfafbff5ffcc4f22`.

Verdict: passes independent structural review, conditional on the explicitly pinned inputs. No mathematical correction is required. This is mathematical review, not formal proof-assistant verification or a numerical test of an HM/source instance.

## Checks

1. **Exact intersections.** For two independent linear forms in a two-dimensional space, divisibility in the auxiliary binary polynomial ring gives intersection of their quadratic multiples equal to the line spanned by their product. The sum has dimension three and is all binary quadratics. Tensoring with the five-dimensional E preserves these calculations. The independent input that every column ideal contains m^3 upgrades the quadratic-space calculation to the asserted exact homogeneous ideals. Three distinct linear divisors cannot divide a nonzero quadratic, so the three-fold intersection is exactly m^3. The proof correctly avoids confusing binary multiplication with multiplication in S.

2. **Fiber products.** The two-factor difference-map sequence has cokernel S/(J_1+J_2)=S/m^2, as stated. For three factors, the compatible constant and linear components contribute dimensions one and five, and the three independent quadratic quotients contribute fifteen. The map from S/m^3 has zero kernel and is surjective in every degree, hence is an algebra isomorphism. The stated warning for four or more factors is essential and correct: their unrestricted degree-two fiber-product space has dimension 5r, greater than fifteen when r>3.

3. **Projective geometry and flatness.** With P parametrizing covector lines, evaluation of a binary quadratic on the tautological line takes values in O_P(2). Its kernel is the quadratic multiples of the line annihilated by the covector. After the stated determinant trivialization this kernel is the image of U tensor O_P(-1). The ranks and twists are consistent: the kernel has rank ten and degree minus ten, and the quotient E tensor O_P(2) has rank five and degree ten. Constant fiber rank yields the exact bundle sequence. The uniform cubic-surjectivity input, followed by Nakayama on the coherent cokernel, makes every degree at least three vanish. The resulting algebra has underlying locally free module O_P direct sum (T tensor O_P) direct sum (E tensor O_P(2)), so its relative spectrum is finite flat of degree eleven. Positive twists do not obstruct this relative algebra construction.

4. **Information-loss dimensions.** The pinned Hilbert functions imply I,D are contained in m^3. Quotienting the exact intersection m^3 by I or D therefore gives the simultaneous kernels. Their lengths are 25+15+3=43 and 35+35+3=73. Subtracting from lengths 64 and 94 leaves the common image length21. These are exact consequences of the intersection theorem; they do not assert an impossibility for all conceivable reconstructions from the full presentation.

5. **Origin-jet recovery.** The nonnegative binary grading makes n^2 M_d have zero components in degrees zero and one. Thus the first binary infinitesimal neighborhood retains S_d, H_d and their W-action. An element f of S_d is annihilated by both binary generators precisely when it kills the generating space W of H, hence precisely when f belongs to Ann_S(H)_d. This is a common kernel of two operators on S_d, not the full kernel on W tensor S_d. The proof explicitly preserves that distinction. Its projective-specialization explanation agrees with the origin-supported modules in the cited binary theorem.

## Verification boundary

The review checked the new derivations and inspected the local binary-module proof's uniform nonzero specialization statement. It uses, rather than re-proves, the pinned universal tensor description and scalar/determinantal Hilbert functions. No selected actual evaluation, coefficient search, numerical multiplication-rank computation, generator/checker, or large computation was used. Neither first-order fixed-source vanishing, higher-order lifting nor algebraicity is established by this result.

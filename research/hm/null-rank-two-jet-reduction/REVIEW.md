# Independent audit: accepted with explicit scope

The proposed identity R_alg=Q4+S2 is correct for the supplied rank-two baseline. Q4 is exactly the existing R22+R31, not a new quartic cancellation. S2 collects the complete second-jet family, not an isolated sector. No actual source, model, jet, detector, owner value, or physical matrix-polynomial product was evaluated. No production module was imported. The independent checker uses only universal scalar indeterminates and rational arithmetic.

## Contract and scope

Work over a commutative Q-algebra (or a characteristic-zero field); rational fractions must exist. Merely saying a commutative ring has characteristic zero is insufficient to justify division by 2. The physical source inputs have determinant-one transitions, traceless first currents, commuting specified physical derivative slots, and exact row composition G=BA. The normalized second jets H,J are tracefree. For arbitrary independently supplied traceless H,J the resulting universal identity still holds, but identifying it with the physical baseline requires those normalization premises. In particular tr(A^-1 A_ab)=tr(L_a L_b), and the transported B analogue, are used in the mixed block.

The supplied complete normal form defines R_alg=tf(G^-1 N)+F_Q k_P,ik+F_P k_Q,ik. This is precisely the R_alg in the candidate, with indices shifted by one. It is not all of B_p or all of Rsharp. The current-curl, test/selector, overlap/cohomology insertion, and K Delta Z families remain unchanged.

## Independent source-to-formula audit

1. The full raw baseline has two quadratic terms, four mu terms, one mixed block, and three negative gerbe terms. Expanding product derivatives gives 17 raw signed terms. Each mu factor is 1/2; the mixed block factor is 1/4.
2. Normalizing G=BA moves every B-edge current and second jet by A^-1(...)A to the first endpoint. Thus quadratic products normalize to X_P K_Q+X_Q K_P. Tracefree projection gives half their commutator sum. No moving conjugation is differentiated as if frozen.
3. The independently audited original Q equation (3), before the preferred cancellation, retains Y=YH-[U,X]/2 and Z=ZH-[L,K]/2. The checker starts here, not by assuming the candidate's collected jet inventory. Both Q pairs agree identically with equation (3′).
4. Expanding the four derivative brackets per Q gives exactly the candidate's eight displayed jet coefficients. Outer Q factor 1/4 times inner YH/ZH factor 1/4 is 1/16. Rank-two contraction contributes 2, giving 1/8. The four complementary signs are +,-,-,+ in the order 13|24,14|23,23|14,24|13.
5. Rank-two polarization gives XY+YX=tr(XY)I; direct expansion gives both nested-bracket identities (B). No basis independence assumption, Gram inverse, or nondegenerate trace Gram matrix is required.
6. The original mixed 1/4 block becomes (1/8) sum epsilon([J,H]+tr(U_a U_b)H+tr(L_c L_d)J). Adding the two Q jet portions supplies exactly the cross traces in a_ab and b_cd and all four negative trace-vector terms. Hence no H/J contribution is discarded.
7. Central gerbe normalization gives -b_P b_Q I, removed only by exact tracefree projection. The two noncentral terms remain -b_P K^G_Q-b_Q K^G_P. Both F=b-c branches cancel these b terms, leaving -c_P K^G_Q-c_Q K^G_P. Together with all first-current terms this is the previously proved Q4. The checker retains independent formal b symbols until this cancellation.
8. Cyclicity gives tr(V[J,H])=tr(H[V,J]); this verifies the dual commutator sign. All other dual terms follow by symmetry of tr(XY). The bilinear H/J term occurs only once in the displayed dual expression, inside W_H. It would be double-counted if also inserted into W_J. This is a contraction identity, not the full gradient in both jet sets.

## Regression and limits

check.py implements sparse exact polynomials in the 48 universal current/jet scalar coordinates, three dual coordinates, and two independent gerbe symbols. It uses scalar trace/bracket structure constants, never constructs a matrix or evaluates a physical polynomial. Equality is coefficientwise, not random sampling or a finite basis spot check. It verifies complete R_alg against existing R22+R31+S2, both original-to-preferred Q identities, the dual formula, and the nested identity. Five mutations are rejected: omitted Fk branches, doubled mixed Moyal coefficient, missing complement, flipped complement sign, reversed dual commutator. Explicit exceptions preserve all checks under python -O. Normal, optimized, and alternate-working-directory outputs agree.

The checker's normalized baseline relies on the supplied source audit for normalization, physical transport, determinant trace relations, and raw product differentiation; it does not independently derive geometric source premises. Source snapshots and exact excerpts are bundled and hashed. The current remote PR/head was not independently authenticated in this audit.

## Novelty boundary

The Fierz contraction, preferred-Q nested-current cancellation, Q4 decomposition, and corrected full-S4-sign primitive are prior results. The new bounded contribution is their organization of the entire unalternated H/J family into four complementary-pair expressions, with the corresponding direct dual contraction. It avoids the eight named YH/ZH intermediates in this representation; it does not establish a smaller physical circuit or runtime bound. It does not provide cancellation of S2 or Q4, cancellation against scalar dependence, a new boundary, a rational divergence, or a value of the obstruction. No local rank-two dimension argument reduces the thirty global residual tests.

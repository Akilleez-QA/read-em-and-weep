# Independent review

Verdict: PASS. The proof establishes a genuine actual-source-family nonvanishing result, conditional on the explicitly pinned actual-frame/source theorems. It does not evaluate a chosen source or establish a Bockstein value.

## Independently checked sources

Fetched and read directly from GitHub, independently of the author's summaries:

- PR739, actual-scalar-compatibility/PROOF.md, commit 9b67dae4d91e81b9e514f4072bfc3774ffd0028f. Confirmed the cited repository path and the exact sign and powers in K_actual=K0-a^2 L_can(a,h)d.
- PR729, firstnormal-scalar-slope/PROOF.md, commit c384ae419983a5031af19c37674df020de1aa5da. Confirmed existence, exact divisibility, independence of the local R, the scalar slope, and nonzero d for every regular pair (including nonsquarefree f).
- PR725, modular-vertex-elimination/PROOF.md, commit 397c7473691a08a839ccf7e9abeed06002b48bab. Its two modular inverses, exact divisions and fixed linear section genuinely give a k-linear right inverse; no dependence on the varying source is hidden in the construction.
- PR713, leading-vertex-obstruction/PROOF.md, commit 5b3943980ecaef78ee7f56fbc015d40955fb24f0. Confirmed the eight-term quadratic expression and the implication from nonzero immutable quotient to nonzero actual global scalar.
- PR692, vertex-scalar-filtration/PROOF.md, commit 858f96ba1539afb1293f31239b8761af08e46f60. Its hypotheses and result explicitly apply to every nonzero a,h; the full actual filtered pair, rather than a selected homogeneous replacement, supplies n,T.
- PR724, canonical-trace-isomorphism/PROOF.md, commit 2061379fe77ec4c82b5f05c7a11d3b7454b97a04. Confirmed the quotient to (S/(f))_8 and the distinction between that necessary immutable gate and full scalar vanishing.
- At commit 8d8b5be4ce62c3055bb53be9e16d29cc63072f04, read the complete source files ACTUAL-MULTIPLIED-NILPOTENT-COHERENCE-FIXES-ENDPOINT-SCALE.md, ACTUAL-CANONICAL-RAW-CUBIC-HAS-A-NONZERO-LINEAR-LIFTING-CORRECTION.md, and ACTUAL-FOURTH-BOCKSTEIN-AS-A-FIFTH-NEIGHBORHOOD-ADJOINT-BOUNDARY.md. These establish the common chart generator, global canonical correction, injective trace-free endomorphism identification, existence of actual primitives, and separate fifth-neighborhood boundary target.

## Checks of the new argument

1. The negative chart is fixed before varying a. Its generator is N_r=U_(r^2)/r^2, independent of a and h. The exact shifted-coordinate formula expresses every U_a using that generator. The change of negative chart modifies T_full only by a multiple of n_full of order eight, not T4. Thus a-dependent reframing does not undermine comparison in one V.
2. Negative rational functions belong to k=C(L); the positive harmonic products are k-linear. This is different from claiming that L_can is k-linear on all rational functions: it is used only as a C-linear endomorphism of the complete global section space A_-.
3. The identity -E_A/A=tr(nW_A)-A d2 proves polynomial divisibility and linearity of the right-hand side before applying the right inverse. Therefore R_A is linear in A, each cubic-square term is quadratic in A, and division by a h gives precisely K0=a^3 K_h, not a^2 or a^4 times K_h.
4. PR729's factored expression proves linearity of K_h in h separately; exact division of a quadratic expression alone would not have sufficed. Nonzero h remains a nonzero quartic in the fixed binary frame. No inverse of h is asserted regular.
5. The canonical correction has its actual normalization gamma retained. Trace-freeness holds for the endomorphism a -> L_can(a,h), and injectivity h -> S_h follows from the stated representation isomorphism. Nonzero gamma is required and supplied by the pinned theorem, not guessed from equivariance alone.
6. Unknown actual second-normal primitives cause no gap: the immutable class is independent of every regular local solution R with the prescribed P,M. Using a linear formal representative computes the same quotient without asserting that it is the actual global primitive or a permitted global change.
7. For a nonzero global section, its generic rational coefficient is nonzero. Cancelling a^2 over k is legitimate even though a has zeros on L. Assuming vanishing for all such sections forces one common rational multiplier on A_-, since d is nonzero in the k-vector space V.
8. A rational multiplier preserving all of H0(P1,O(2)) has no pole: the complete linear system is basepoint-free. It is consequently a constant global function. Trace zero then forces that constant to vanish, and injectivity forces h=0. This is a structural argument about divisors and sections, not an actual point evaluation.
9. Although V is infinite-dimensional over C, the image of the finite-dimensional C-space A_- is finite-dimensional. The kernel is an ordinary proper linear subspace and its projectivized complement is a nonempty Zariski-open set. No numerical rank test is needed.
10. The square-direction refinement is valid: the Veronese conic in P(A_-) is nondegenerate, hence not contained in a proper linear subspace. A line intersects it in at most two geometric points; a point or empty subspace cannot give more. Thus at most two square directions can have zero immutable class, with no assertion that either exceptional point exists.

## Scope and restrictions

Nonzero K implies nonzero rho4. Zero K is only necessary, not sufficient, for rho4=0. The proof does not identify any particular exceptional or nonexceptional actual direction. A nonzero rho4 is not a nonzero beta4: the latter belongs to the separately retained fifth-neighborhood adjoint boundary modulo the second-symbol image. No algebraicity conclusion follows.

No actual source coefficients, source values, derivatives, points or matrix ranks were evaluated. No model substitution, executable computation or GitHub write was performed in this review. Reading older source derivations imports their stated theorems; it does not rerun their calculations.

The only requested improvements were disambiguating the local cubic numerator from the actual monad primitive, replacing process-only bookkeeping with immutable source links, and adding the valid square-conic corollary. No mathematical correction to the core argument was required.

## Reviewed final artifact

PROOF.md SHA-256: 3612cb72dfb8b65c819a3aa094e3ddaa7587a8193861ed0b1670d17333d7ffdc

This hash includes the source-link revisions, disambiguated local numerator and square-direction corollary. The final text and hash were read and checked after those changes.

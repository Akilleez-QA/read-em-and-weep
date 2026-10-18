# Independent exceptional-carrier audit

## Verdict and scope correction

The literal-column proof is correct. The claimed 152096 tuples are precisely the fresh-source-ordered slice with **ordered standard sequence (3,11,15)**, not the entire seed-4 outer-label sum. They split into 45760 prior primary tuples and 106336 exceptional tuples. Within the exceptional slice, 101962 tuples have an outer factor structurally zero and 4374 are not excluded by that outer test. All 106336 have identically zero selected contraction.

The full seed-4 outer sum assigns each of 96 carrier/mask pairs independently to each of three distinct staircase standard tags before source sorting. It therefore has 96^3 = 884736 assignments. Sorting can change the standard sequence. There are 96^3 - 64^3 = **622592 exceptional-containing assignments**, and 262144 primary-only assignments. The exceptional zero-column proof covers every one of those 622592, across all six source-sorted standard permutations. This extension was independently enumerated and checked against the authenticated selector binding. It does not establish complete seed-4 E12 vanishing: the prior primary proof covers only the 45760-tuple ordered-standard slice, leaving 216384 primary assignments outside that reviewed coverage. Some may have zero outer weights; no unresolved tuple is asserted nonzero.

Concrete missing-slice witness: assign (carrier,mask,standard) = (2,0,3), (1,0,11), (4,0,15). All three outer owners pass the structural activity test. Source sorting gives ordered standards (11,3,15), outside the present primary lowering. This prevents silently treating the fixed staircase as a fixed source-sorted standard sequence.

## Source-order provenance

The order is the existing fresh-consistent-source-definition contract: auxiliary/star first, then carriers 0 through 4, numeric low-bit legal mask, then standard tag. Historical intra-carrier mask enumeration is not newly authenticated. The source-mask-order witness explicitly distinguishes a fresh construction from historical value import; its derivative-index list is not a cover-mask enumeration.

The domain is a genuine summand of the declared fresh ordered-cover construction under that construction's stated source-identity hypotheses, rather than a certificate comparing historical nonlinear source values. Authenticated refined detector composition section 2 explicitly requires Pi_out to assign labels and then source-sort, preserving alternating sign. The zero-column argument itself is insensitive to the within-carrier mask order and to the sorting sign.

## Exact algebra and provenance

The raw pinned model SHA256 is 635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926. Its compact canonical JSON SHA256 matches the existing homogeneous identity certificate's modelSha256. Both the certificate and checker file byte hashes, and their pinned Git blob hashes, authenticate successfully. The historical checker was not executed.

For physical carrier 0 and star 5, the pivot is 0 and both entries P[0][6], P[1][6] are literal empty polynomial lists. I[12] need not be zero. The authenticated selector for seed 4 is coefficient -2 and zero-based entry [12,6]. The transposed contraction is

    -2 sum_(u,w) I_a[12,u] tf(R)[w,u] P_a[w,6].

Each of its four coefficients vanishes by the right column. No trace-free shortcut is needed; the statement holds for arbitrary R. The independent test replaces current construction by four free syntactic entries and obtains a literal zero numerator without physical polynomial evaluation. Full owner labels and the actual first sorted owner remain in the selector binding. All six standard permutations were tested with both exceptional anchors.

Star's actual stored denominators di, dp, dh are -v1*a = -v1^2*v3*v4 on v0=1, not -a. On D(a), v1 is already a unit, with inverse v0*v3*v4/a. More importantly, the column-zero proof does not need speculative outer denominator cancellation or a new scalar edge clearance certificate. Candidate cancel, quotient, and edge_inverse overrides reject that route.

## Prior primary incorporation

All seven hashes in primary-carrier-full-domain-partition.json match the current artifacts. Its separately recorded four-test independent audit log hash also matches. Its domain decomposition is 43584 outer-literal-zero + 832 selected-contraction-zero + 512 earlier support-excluded + 832 new support-excluded = 45760. The original primary audit explicitly incorporates the separately checked 512-tuple legal-mask artifact.

The public release regenerates the support artifacts and replays the independent checks. The public hash bridge authenticates those regenerated artifacts; see verification-results.txt.

## Verification and resource boundary

`test_exceptional_carrier_independent.py`: seven tests; see exceptional-independent-test.log for the public replay. Tests independently enumerate Cartesian label products, verify counts and owners, authenticate model/certificate bytes, inspect selector orientation, exercise arbitrary-entry zero, forbid rational lowering during partition(), check release flags, verify prior hashes, and preserve the missing-permutation counterexample.

The candidate test file was inspected: its current checks construct rational syntax DAGs and formal derivatives only. Neither candidate nor independent tests execute the polynomial checker, expand a physical polynomial, evaluate a physical polynomial, enumerate physical multinomial terms, or extract coefficients. No public writes were made. Physical products spent remain zero; execution release and actual factorization acceptance remain false. No complete M0/E34/78-seed/global-obstruction conclusion is made.

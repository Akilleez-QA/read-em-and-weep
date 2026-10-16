> Worker proposal/review record. Acceptance and supersession are tracked in `../STATUS.md`.

# Independent reusable q2 family exclusion

Claim: for the fixed parameterized outer carrier partition, both q2 selector entries [9,3] and [10,4] vanish termwise on both CCBB staircases, for arbitrary admissible residual R. Hence cloud seeds0,1,2,3 vanish in both E12/E34 channels:8 ownership cells. No claim about seed4/5, detector value or class.

## Independent check

Ran Codex-V01-family-zero.py, which imports no C-worker code and performs NO polynomial arithmetic. It authenticates the literal model bytes against Git blob fcd48a9a22d40d55ce7a08b8aefcb4eaa2fdf761 at08b73637d4136f91606aad332c46cafd064417f8, then reads all six I rows and P columns. A nonempty term list is treated only as potential support; no polynomial nonzero assumption is needed.

| selector | carriers with nonempty I row | carriers with nonempty P column | intersection enclosure |
|---|---|---|---|
| [9,3] | 0,3,4 | 2,3,4 | 3,4 |
| [10,4] | 1,2,3,4 | *,0,3,4 | 3,4 |

Every other carrier has an ENTIRE literal-zero I row or P column. For arbitrary2x2 R, (I_a R^t P_a)[r,c] = sum_(u,v) I_a[r,u] R[v,u] P_a[v,c]. The zero row/column therefore kills all four matrix-entry paths without invoking source identities or cancellation. Diagonal frame factors preserve these literal zeros.

## Partition and ordering premise

PR1 comment6141322825 section5 explicitly constructs the carrier partition for ANY positive N. At standard chart e, s is its number of infinity coordinates. Its unit identity uses only j=0,...,s; raising and splitting that identity defines R_j=B_j C_j for j<=s and R_j=0 for j>s, with R_*=sum_(j<=s)B_jD_j. This conclusion is a syntactic definition, independent of exponent N. In particular it holds at N54. Multiplication by separately chosen legal29 weights preserves a literal zero carrier weight.

Comment6205249609 chooses the fixed outer carrier54/legal29 partition, same common-cover projection r and corresponding standard tag at every sampled slot, building on6141322825. Thus this proves the premise for THAT published fixed family, not an arbitrary alternative partition. No executable outer lowering is claimed supplied. A future implementation must authenticate these same weights; choosing unrelated Bezout weights would invalidate this exclusion.

Both reconstructed CCBB staircases begin at coordinate tuple(0,0,1,1), standard tag3 under the now authenticated bit dictionary, so s=2. Any nonzero-weight sample at that slot has carrier in{*,0,1,2}. Sorting common vertices carrier/mask first, standard last, auxiliary first (6205660472; canonical*=5, sorting key-1), ensures the leading carrier is no greater than this sampled carrier. Therefore its leading carrier cannot be3 or4. It is killed by the literal selector supports above.

This argument applies to EVERY legal mask, every other sampled carrier, all source-sorting permutations/signs, both staircase orientations, and arbitrary admissible R. Repeated tail carriers are allowed. Alternating extension is used; the proof never recomputes a nonlinear R after permutation. Zero weights and repeated full vertices vanish separately.

## Disposition

C03's zero-family mechanism is corroborated and extends to the complementary permutation in C04 and both channels in C01/C02: cloud seeds0..3, total8 cells. This does not touch incumbent seed4E12. It is a symbolic rule proof, not a physical source scan or full-label enumeration. Acceptance is conditional only on retaining the explicitly published fixed partition family in the actual lowering; the family formula itself supplies its j>s premise for N54. Next: bind the concrete lowering when transferred and apply this certificate as a pruning rule.

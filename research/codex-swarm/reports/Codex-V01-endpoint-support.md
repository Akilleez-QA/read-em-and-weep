> Reviewed metadata record; scope in [PR80 STATUS](https://github.com/Akilleez-QA/read-em-and-weep/blob/b5224465774932b25b03d74af5dbe087ba291ac2/research/codex-swarm/STATUS.md).

# Endpoint partition rule on unchanged carrier domains

Source pinned to PR79 commit6e28c6b59f8245779f6c03a20798e4de6842ae19. Independent script check_endpoint_support.py authenticates outer_partition_source_binding.py Git blob1dcb9d5e0def4fba2268f4c54de6409b137ed05e and owned_scalar_denominator_binding.py blobb1fee3ac562bce5f561adb5b6ab03103f148efa6 before classifying. It DOES NOT import/execute either package module. It reuses our independently authored Boolean model parser/checker with model blob authentication. Complete per-tuple records: certificates/endpoint-support.json. No q2/seed4 work, physical polynomials or coefficients.

## Hand rule, exact inspected source

For standard15 all four coordinates are infinity, hence s=4 and the finite-variable set is empty. The source formula H_k sums monomials over nonnegative exponents of FINITE variables whose sum is k. Thus H0=1 and Hk=0 for k>0, with the empty sum/product conventions explicitly specified.

The source defines N54, M107, T535, L=(s+1)(T-1)+1=2671. In every B_j summand, the chosen index satisfies n_j>=T. If j<4, its factor [(-1)^(4-j) H_(4-j)]^n_j is zero with strictly positive exponent. The other factor v_j^(n_j-T) has nonnegative exponent and cannot cancel this zero. Hence B_j=0 for j<4. For j=4 only n0=n1=n2=n3=0 can survive, n4=L; H0=v4=1, so B4=1. This step uses finite defining identities, not source expansion.

Therefore Q_b=B_b*Cbar_b is zero for primary b<4; Q_5=sum_j B_j*Dbar_j may remain, as may Q4. Multiplication by H_b^54 and legal29 factors does not resurrect a zero. Every staircase's last sampled vertex is standard15, so its carrier is4 or5 whenever its weight is nonzero. This is stronger than j>s at s4 and belongs to the newly pinned source, not an arbitrary partition.

## Same domains, disjoint ordered classification

Keep exactly the prior q3 raw360 and q4 raw720 sampled-carrier tuples PER staircase/row. Slot j has declared flag superdomain{*,0,...,4-q+j}. Never replace its denominator with a smaller survivor set. Classify each tuple exactly once in order: (1) last carrier not4/5 => endpoint weight zero; (2) source-sorted prefix carriers fail strictness => split-identity zero; (3) selector AND/OR matrix path absent => literal selector zero; (4) UNKNOWN. These are carrier-domain counts, not occupied source-support counts. Mask uniformity and repeated-tail ownership remain as in the prior proof.

| q,row | raw | endpoint zero | prefix zero after endpoint | selector zero after both | UNKNOWN |
|---|---:|---:|---:|---:|---:|
|3,3 M10[0,3]|360|240|57|57|6|
|3,4 M10[2,6]|360|240|57|39|24|
|3,5 M21[10,1]|360|240|57|63|0|
|3,6 M21[12,5]|360|240|57|61|2|
|4,7 M20[0,0]|720|480|208|28|4|
|4,8 M31[10,0]|720|480|208|32|0|

Every row sums to its unchanged raw domain. Same results apply separately to each lexicographic staircase permutation, both channels, without physically evaluating either. Prefix and selector ordering signs are preserved but irrelevant to a literal zero.

## Remaining anchor demands

q3row3: anchors(*,2),(0,2),(1,2), two sampled tuples each; all4 Boolean residual paths.
q3row4: anchors(*,1):15 tuples, (0,1):9; residual paths R[1,0],R[1,1].
q3row6: anchor(1,2),2 tuples; all4 paths.
q4row7: anchors(*,1,2),(0,1,2),2 tuples each; all4 paths.

Per-staircase UNKNOWN sampled tuples improve18->6,88->24,6->2,12->4 for the respective nonzero rows, within the SAME prior raw360/720 domains. Whole-row zeros remain unchanged: this proves no additional whole seed zero beyond the prior68 E-channel cells. It reduces exact unresolved carrier-demand records, not obstruction dimension. All full owner/mask/frame/inner partition dependencies remain; Boolean true still means UNKNOWN.

Next: independent review of source binding and hand zero rule, then propagate demands only from the explicit remaining records. No resource gate or actual source/Laurent admission follows from this source-formula binding.

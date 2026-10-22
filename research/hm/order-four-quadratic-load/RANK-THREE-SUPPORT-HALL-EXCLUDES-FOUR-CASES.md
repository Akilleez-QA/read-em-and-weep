# Weighted Hom-support Hall excludes four more rank-three quotient labels

## Result and scope

Starting with the frozen `rank-three-quotient-frontier-148.json`, the universal zero-pattern argument below excludes exactly four further labels, all maximal profile (1,1). The remaining counts are **144 = 122 + 10 + 12** for profiles (1,1), (1,2), (2,1). Against the unchanged 182-label baseline there are now 38 excluded and 144 not excluded. The surviving original determinant lengths have distribution **{0:80, 12:50, 20:2, 24:12}**. These numbers count profile-labelled ordered quotient splitting types, not realizations, proof tasks, or completion percentages.

The source theorem `ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md` provides the original injection A -> B*(-2), and its transpose B -> A*(-2). Both maps are injective as sheaf maps, but need not be subbundle injections at torsion points. Only generic injectivity is used below. All irreducibles are self-dual.

## Weighted Hall necessity

Write X = direct sum_i R_i O(e_i), Y = direct sum_j S_j O(f_j). Make an edge i--j precisely when the universal equivariant Hom space is nonzero. Its dimension is the multiplicity of R_i in S_j tensor Sym^(f_j-e_i) W, interpreted as zero for f_j<e_i.

For any subset I of source summand occurrences, let N(I) be the set of target occurrences adjacent to at least one element of I. Every equivariant map X -> Y sends the subbundle X_I into Y_N(I): all other component Hom spaces vanish identically. If the map is generically injective, its restriction to X_I is injective over the function field, so necessarily

    sum_{i in I} dim R_i <= sum_{j in N(I)} dim S_j.

This is an ordinary dimension necessity imposed by a universal zero pattern. It does not choose map coefficients or points and does not compute any instance matrix rank. Repeated summands are separate occurrences. Nonzero Hom entries and even satisfaction of every inequality do not imply that any generically injective equivariant map exists.

## Four explicit contradiction certificates

All certificates below use A -> B*(-2). The listed target neighborhood is complete, not merely a convenient subset. Every source neighborhood has ordinary rank two and every reachable target neighborhood has rank one.

1. `G3.11.ef6c4c677f42`, original source index 19, original defect 24:
   A = O(-8) + W' O(3); B = O(-28) + O(-6) + O(6).
   B*(-2) = O(26) + O(4) + O(-8).
   Source subset W' O(3) can reach only O(26). It cannot reach O(4) because Hom(W',Sym^1 W)=0, nor O(-8) by degree. Contradiction: 2 <= 1.

2. `G3.11.63299e2ae6ab`, source index 27, defect 12:
   A = O(-10) + O(-8) + O(16); B = O(-18) + W' O(1).
   B*(-2) = O(16) + W' O(-3).
   Source subset O(-8) + O(16) can reach only O(16). The first has no map to W' O(-3) because W' does not occur in Sym^5 W = T; the second has no map there by degree. Contradiction: 2 <= 1.

3. `G3.11.581de282a9e9`, source index 64, defect 12:
   A = W' O(-1) + O(2); B = O(-8) + W O(-5).
   B*(-2) = O(6) + W O(3).
   Source subset W' O(-1) can reach only O(6). It has no map to W O(3) because W tensor Sym^4 W = W tensor D = S + T, with no W'. Contradiction: 2 <= 1.

4. `G3.11.6cb986f38b24`, source index 86, defect 12:
   A = W' O(-1) + O(4); B = O(-8) + 2O(-6).
   B*(-2) = O(6) + 2O(4).
   Source subset W' O(-1) can reach only O(6). Neither O(4) receives a map because Sym^5 W = T contains no W'. Contradiction: 2 <= 1.

The verifier also supplies transpose certificates. The exact character-ring operations verify the full neighborhoods including their positive edges, rather than relying on these prose identities alone.

## Same-witness Q refinement, kept separate from label exclusions

For each existing pair/Q* witness in `unrestricted-dual-splittings-and-pairs.json`, retain one and the same Q* only if it passes the support inequalities for both

    A -> Q(-2), and B*(-2) -> Q(-2).

The second is the dual-twisted injection from the quotient Q* -> B. Original witness conditions remain in force because the new list is strictly a subset of the old witness list. No relation between a primal E witness and a dual Q* witness is inferred.

There are initially 2734 witness edges (2140 for (1,1), 594 for (1,2)). Hall retains 2392. Exactly one pair loses all Q* witnesses, and that pair is already among the four direct exclusions. Witness edges are not additional quotient labels.

A complementary analytic condition is useful when a source subset and its neighborhood have equal rank. The restricted injection has nonzero determinant, which is an invariant global section of det(Y_N) tensor det(X_I)^(-1). The complete binary-icosahedral character table has exactly one one-dimensional character, the trivial one; this is checked by orthonormality and sum of squared dimensions =120. Thus every representation determinant is trivial, and if d is the target neighborhood degree minus source subset degree, Sym^d W must contain the trivial character (and d>=0). This tight-neighborhood determinant test is still necessary only. It reduces the same-Q witness edges further to 2284, but excludes no further pair. It creates no extra direct pair exclusions either.

## Reproduction, bounds, and audit

Run `python3 verify_rank_three_support_hall.py`. It SHA-256 pins the 148-case predecessor, dual witness dataset, and exact character implementation; no predecessor files are regenerated. It writes `rank-three-quotient-frontier-144.json`, preserving all 182 stable IDs and prior exclusion statuses, and records the precise source and target occurrence indices for every new exclusion. All indices are zero-based in the stored splitting lists. Its output is saved in `rank-three-support-hall-verification.log`.

For direct tests and dual-witness tests the source is always rank three, hence has at most three irreducible summand occurrences and at most seven nonempty subsets. Each Q* has rank 13, hence at most thirteen target occurrences. The 2734 witness edges and these small subsets give an explicitly bounded finite test. Character products and invariant multiplicities use exact rational arithmetic in Q(sqrt(5)); no actual coefficients, source correlation, selected points, instance matrices, rank calculations, model spikes, or consumed experiments occur.

This proves exclusions, not realizability or generic rank of any surviving case. All three maximal profiles remain open, as do original-source realization and the separate original proof obligations.

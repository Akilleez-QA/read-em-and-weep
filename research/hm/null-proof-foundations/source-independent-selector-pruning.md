# Source-independent pruning:4038 formal kernel paths to78 selectors

## Proved reduction

For every row-End2-cochain R on the source-first common cover, the local split identities give

    J1_abcd=h_a j_b(R_bcd),
    J2_abcde=-h_a h_b j_c(R_cde).

No source locality or closure is needed for these linear-map equalities. Closure is needed only to interpret the complete lift as an obstruction cocycle. All deleted prefix owners and their outer weights remain in the resulting expression.

This is not a four-carrier-tail reduction. The residual tails still range over common vertices, potentially with repeated carrier labels and different standard tags or masks.

## Why only the first face survives

The split contraction has H I=0, P H=0, H^2=0, E=IP. Hence h_a j_a=0. Also H E=E H=0, so h_a^2=0 with its prescribed degree-dependent sign.

In h_a delta j, every face except deletion of a starts with j_a and is killed by h_a j_a. In -h_a delta(h_first j_second), every face except deletion of a starts with h_a and is killed by h_a^2. This proves both equations above. The same argument extends to the next lift component, though it has no terminal tensor row here.

It does not justify killing h_a j_b or h_a h_b for unrelated owners. The formal implementation uses only equal-owner identities. Any later identification of physical splittings across different labels requires its own frame/source proof.

## Graded block and terminal pruning

The inclusion j_c(R) occupies only the K1->K1 block. Each h has a left-H branch and a right-H branch preceded by E. A single homotopy therefore gives:

    M10: H_a I_b R^t P_b,
    M21: E_a I_b R^t P_b H_a.

The lambda3 M10 and M21 entries each select exactly their respective branch.

For two homotopies, the inner left-H branch has target K0. Both possible outer branches then vanish: another left H would require K0->K(-1), and an outer E acts only in K1. The remaining two branches of h_a h_b j_c are

    M20: H_a E_b I_c R^t P_c H_b,
    M31: -E_a E_b I_c R^t P_c H_b H_a.

J2 adds its overall minus. Lambda4 is -M20[0,0]+M31[10,0]. Consequently its two final scalar contractions BOTH have a plus sign before the staircase orientation:

    row0(H_a E_b I_c) R^t col0(P_c H_b),
    row10(E_a E_b I_c) R^t col0(P_c H_b H_a).

The graded H blocks within these words are fixed by their source/target indices; the implementation does not multiply physical matrices.

Lambda2 already selects its inclusion entries without any H. Thus every one of the78 terminal staircase entry seeds has exactly one factored selector path.

## Exact formal accounting

The unpruned seed expansion has

    6 +24*2*4 +48*2*5*2*4 =4038

H/face paths. Enumerating just those small formal paths gives:

-3792 vanish by same-owner split identities;
-96 vanish by graded block incompatibility;
-72 miss the requested terminal block;
-78 survive, one per terminal staircase entry seed.

The counts sum to4038. They are not polynomial-product counts. Source label sums, selector factor entries, coefficient demand and exact arithmetic remain unexpanded and unpriced.

## Reproducible formal implementation

`prune_refined_selector_paths.py` produces schema `hm-refined-detector-pruned-v2`. It imports only the earlier metadata specification generator, whose exact canonical certificate hash is recorded in the new JSON. No physical source model or polynomial code is imported.

`test_refined_selector_pruning.py` contains9 tests checking counts, one selector per seed, cross-owner noncancellation, prefix weight retention, all surviving word shapes, lambda4 signs, metadata bounds and mutation rejection. Run with Python -B and PYTHONDONTWRITEBYTECODE=1.

`refined-selector-pruning.json` records each selector's left/right owner words, residual tail, terminal entry, sign, all weighted owners, and deleted prefix owners. It uses ordinary row(left) R^t col(right), preserving the source transpose convention. The exact canonical serializer rejects sign, tail, prefix-owner and old-four-tail flag mutations.

Serialized metadata size is not a runtime-memory bound. The actual obstruction value remains unknown.

## Certified conditional carrier-prefix filter

The pinned `source-identity.md` section2, blob `7e12e8c7479427db87cd496763f5f003005af9c5`, explicitly proves that repeated prefix carriers vanish even across different legal masks: their common-original-frame homotopies coincide. The frame-conjugated arbitrary middle R remains inside the same carrier inclusion. This is additional source-map evidence beyond the equal-symbol formal word rules.

Accordingly the executable conditional predicate `prefix_allowed` requires carrier(first)<carrier(second) for J1 and strictly increasing first THREE carrier labels for J2. It rejects application without the common-original-frame certificate or source-first tuple ordering. J0 has no such prefix restriction. The final two tail carriers may repeat the third carrier; distinct standard tags are still distinct common vertices, including when physical carrier/mask labels agree.

The label domains remain unenumerated. The78 universal selector paths are therefore unchanged, with this additional filter attached. Tests include equal carrier with different masks (rejected prefix), repeated tail carriers/physical labels with different standard tags (allowed), and wrong-frame/order controls. The suite now has12 tests.

No claim that repeated tail labels kill Rsharp is made. Its partition-dependent scalar solution can contribute on an edge with identical physical source labels and different standard tags. Thus the old four-tail or781-feature argument still cannot be substituted.

## Exact prefix-mask merger, without a tail merger

On the strict-carrier prefix domain, the prefix common-frame H/E/eta factors depend on their carrier and standard-frame restriction but not their legal mask. The new Rsharp is evaluated only on the final residual triple. Source-first sorting and its sign cannot change as a prefix mask changes: every prefix carrier is strictly below the next prefix carrier and below the tail leader. The matching outer standard row remains fixed.

For each prefix vertex with outer weight R_(e,b) times the four legal weights, one may therefore sum its mask exactly:

    sum_(m in {0,1}^4) product_i L_(e,i,m_i)
       = product_i (L_(e,i,0)+L_(e,i,1)) =1.

The outer carrier weight R_(e,b) and the standard/carrier owner remain. This removes one16-valued prefix mask sum for J1 and two for J2, symbolically16 or256 combinations. It does not sum any tail mask or any inner scalar-T mask. It gives no polynomial-product count.

The implementation records this exact merger on each selector and tests it using only the abstract two-chart identity w0+w1=1. No actual partition polynomial is expanded. It rejects missing strict-carrier or common-frame certification, a proposed tail merger, or an incomplete two-chart sum. The suite now has14 tests.

## Dependency scope

Companion references are identified by basename. A referenced file not supplied with this collection is an external prerequisite, not an embedded proof or a verified relative link. The reading order and unresolved conditions are listed in `proof-notes-index.md`. Reported test results describe the source audit; this proof copy does not by itself constitute a new test run.

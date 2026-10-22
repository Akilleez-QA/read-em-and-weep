# Both torsion alternatives exclude the index-2 second-defect-20 branch

## Claim and distinction from the earlier result

For stable ID **G3.21.d610e381ed75**, source pair index 2,

    A=O(-8)+O(2)+O(16),   B=O(-18)+O(-4)+O(6),

the profile (2,1) second defect s=20 is impossible. This is a new whole-defect exclusion, separate from the already proved s=24 exclusion for this same quotient pair. Combining the two results leaves second defects **{0,12}**.

The quotient case itself remains in the frontier; no realization of either retained defect is asserted. The frontier143 case count is unchanged.

## Common geometric identities

Write K=E^-, M=K^-, J=K/M and C=A(-2). The published profile (2,1) exact sequences are

    0 -> K -> E -> A -> 0,
    0 -> M -> K -> J -> 0,
    0 -> J -> C -> T_def -> 0.

Here C=O(-10)+O(0)+O(14). At s=20, the published rank-eleven endpoint theorem leaves exactly two alternatives:

    T_def=O(0)|D20 or O(2)|D20.

The actual-source identities and strict top-slope bounds give

    rank K=14, deg K=-64, maxdeg K<=-3;
    rank M=11, deg M=-48, maxdeg M^-<=-5.

Since every ordinary summand of K has degree at most -3, its minimum degree is at least

    -64-13(-3)=-25.

The quotient J inherits this minimum bound: K(25) is globally generated, hence J(25) is globally generated. Thus mindeg J>=-25.

The derivative M->J(-2), with kernel M^-, requires an injection H0(M(4))->H0(J(2)). Independently, the second exact sequence requires a surjection H1(K(2))->H1(J(2)), since H2(M(2))=0.

## Alternative 1: the weight-zero torsion quotient

Choose O(1) fiber weight1 at the binary stabilizer C6 of D20. The three source fibers of C have weights {2,0,2}. Therefore only the middle O(0) summand can supply O(0)|D20. Its nonzero equivariant component is a nonzero constant on the transitive orbit and is everywhere surjective. Consequently

    J=O(-10)+O(-20)+O(14).

There are no hidden cross-components: the other summands have incompatible stabilizer weights and the target is reduced.

The source slope bound gives H0(K(2))=0, so Riemann--Roch yields

    h1(K(2)) = -(14*3-64) = 22.

But the forced image gives

    J(2)=O(-8)+O(-18)+O(16),
    h1(J(2))=7+17=24.

The required surjection from dimension22 onto dimension24 is impossible.

## Alternative 2: the weight-two torsion quotient

Now the middle O(0) component cannot supply O(2)|D20. If the high O(14) component also vanished, the low O(-10) summand would supply the quotient alone. Its kernel O(-30) would split off in J, contradicting mindeg J>=-25.

Hence the high component is nonzero. Equivariance makes it fiberwise invertible on the reduced transitive orbit. After twisting by two, its section map from H0(O(16)) is injective: its kernel is H0(O(16-20))=H0(O(-4))=0.

The low summand has no twist-two sections, while the middle O(2) after twisting has three and maps to zero in the torsion target. Thus

    h0(J(2)) <= 3.

On the other hand, Riemann--Roch for M gives

    h0(M(4)) >= chi(M(4)) = 11*5-48 = 7.

The required injection from at least seven sections into at most three is impossible. This excludes the second and last s=20 alternative, proving the whole-defect claim.

## Reproduction and limits

Run `python3 verify_two_one_index_two_second_defect_twenty_exclusion.py`.

The standalone verifier pins the published frontier144, rank-eleven endpoint JSON and primal-interior proof. It checks the exact stable ID and A/B, the exhaustive two-alternative list, the C6 weights, the inherited minimum-degree bound, and both numerical contradictions. It writes `two-one-index-two-second-defect-twenty-exclusion.json`.

The certificate records the result relative to its endpoint input as {0,12,24}; the independent earlier s=24 exclusion yields the combined list {0,12}. This avoids counting that earlier result again.

No splitting enumeration or unpublished witness tables are used. There are no selected actual coefficients or points, instance matrices or rank tests, scans, spikes or consumed experiments. The argument uses the same actual image J and universal exact sequences throughout. No global realization, quotient-case exclusion, smoothing or SF claim is made.

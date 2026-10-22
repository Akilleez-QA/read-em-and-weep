# Orbit restrictions exclude the second-defect-32 branch

## Claim and scope

For stable ID **G3.21.1c43993b4f83**, source pair index 9,

    A=O(-8)+O(6)+O(16),   B=O(-18)+O(-8)+O(6),

the profile (2,1) second defect s=32 is impossible. Its published list {0,12,20,24,32} sharpens to **{0,12,20,24}**. This removes one whole defect branch that survives the local module criteria. It does not exclude the quotient case or change the frontier143 case count.

## Published exact sequences and endpoint bounds

Write K=E^-, M=K^-, J=K/M, and C=A(-2). The interior-flag relations are

    0 -> K -> E -> A -> 0,
    0 -> M -> K -> J -> 0,
    0 -> J -> C -> T_def -> 0.

The published rank-eleven endpoint theorem leaves exactly one torsion possibility at s=32:

    T_def=O(4)|D12 + O(2)|D20.

The two supports are disjoint, and C=O(-10)+O(4)+O(14). The established numerical and strict top-slope bounds give

    rank K=14, deg K=-68, maxdeg K<=-3;
    rank M=11, deg M=-44, maxdeg M<=-4;
    maxdeg M^-<=-5.

Every ordinary summand of M therefore has degree -4, so h0(M(4))=11. The actual next derivative M->J(-2), with kernel M^-, requires an injection

    H0(M(4)) -> H0(J(2)).                         (1)

We prove h0(J(2))<=7 for the same image J.

## The high summand must supply the D20 quotient

The bounds on K imply

    mindeg K >= -68-13(-3) = -29.

Thus K(29) is globally generated, and so is its quotient J(29). Consequently mindeg J>=-29.

Choose O(1) fiber weight1 at each stabilizer. The C10 fiber weights of the three summands of C at D12 are {0,4,4}; its C6 weights at D20 are {2,4,2}. Therefore:

- O(-10)->O(4)|D12 is zero, because weights0 and4 differ;
- O(4)->O(2)|D20 is zero, because weights4 and2 differ.

A component to a reduced transitive orbit is either zero or nonzero at every point, by equivariance.

Suppose the O(14)->O(2)|D20 component were zero as well. Surjectivity would then force the O(-10) summand to supply the entire D20 quotient. Since that summand maps to zero at D12, the full quotient splits into the low summand supplying D20 and the two higher summands supplying D12. Its kernel J would split off

    O(-10)(-D20)=O(-30).

This contradicts mindeg J>=-29. Hence the O(14)->O(2)|D20 component is nonzero, and is fiberwise invertible along D20.

## The section bound

After twisting by two, the high-summand component induces

    H0(O(16)) -> H0(O(4)|D20).

It factors as restriction to D20 followed by a fiberwise invertible map of the restricted line bundles. Its kernel consists of sections vanishing along D20, namely H0(O(16-20))=H0(O(-4))=0. Thus this section map is injective.

The low summand contributes H0(O(-8))=0. The middle summand has no map to the D20 target, as proved above. Consequently the kernel on H0(C(2)) of the D20 quotient is exactly the middle summand's H0(O(6)), of dimension seven. Imposing the additional D12 quotient can only shrink this kernel. Hence

    h0(J(2)) <= 7.

This contradicts the eleven-dimensional injection (1), excluding s=32.

The argument uses the actual common image J throughout. Local quotient existence alone did not give this bound; the quotient K->J rules out the alternative with a degree-minus-thirty summand, after which the global restriction to D20 controls sections.

## Reproduction and limits

Run `python3 verify_two_one_second_defect_thirty_two_section_exclusion.py`.

The small independent checker pins the published frontier144, endpoint JSON and primal-interior proof, verifies the stable ID and exact A/B, the unique torsion alternative, both stabilizer weight comparisons, the minimum-degree contradiction and 11>7. It writes `two-one-second-defect-thirty-two-section-exclusion.json`.

No splitting enumeration or unpublished coupling tables are inputs. There are no selected actual coefficients or points, actual matrices or rank tests, scans, spikes or consumed experiments. These are universal orbit restrictions, exact sequences and integer section dimensions. No global realization, additional quotient-case exclusion, smoothing or SF claim is made.

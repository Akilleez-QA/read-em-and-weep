# Index9 cannot have the semisimple second-defect24 torsion alternative

## Exact claim

For stable ID **G3.21.1c43993b4f83**, source index9,

    A=O(-8)+O6+O16,   B=O(-18)+O(-8)+O6,

the profile (2,1) alternative T_def=O4|D12 + O4|D12 is impossible. This does **not** exclude the whole second-defect24 branch: cyclic O4|2D12 remains untouched. It does not exclude the quotient case or change frontier143.

## Forced image kernel

Put C=A(-2)=O(-10)+O4+O14 and use the actual image exact sequence

    0 -> J -> C -> (O4|D12)^2 -> 0.

At the C10 stabilizer, with O1 fiber weight1, the source weights are {0,4,4}. Thus the low summand has zero component. Each of the other two summands has a one-dimensional space of equivariant maps to O4|D12: equivariant maps on a transitive reduced orbit are determined by their stabilizer-invariant fiber.

Consequently each of these two source components is a fixed nonzero equivariant line-restriction map multiplied by a constant vector in the two-dimensional target multiplicity space. Surjectivity forces those two constant vectors to be independent. A constant target GL2 change of basis makes the middle summand supply the first target and the high summand supply the second. Both restrictions are everywhere invertible. Taking their kernels gives the equivariant splitting

    J=O(-10)+O(-8)+O2.

This uses only reduced torsion. There are no nilpotent or socle components to discard, and no assumption about a lift between the two source line bundles.

## Endpoint contradiction

It follows that H0(J(2))=H0(O4)=Sym^4 W=D, an irreducible of dimension5. The published rank-eleven endpoint list has exactly four M splittings for this semisimple torsion alternative, and each contains P O(-4). Thus each H0(M(4)) contains P, an irreducible distinct from D.

The actual derivative M->J(-2) has kernel M^- with maximum degree at most -5, so it induces an injection H0(M(4))->H0(J(2)). Such an equivariant injection cannot send the P constituent into D. This contradiction excludes precisely the stated semisimple alternative.

## Reproduction and scope

Run `python3 verify_two_one_index_nine_semisimple_twenty_four_exclusion.py` to produce `two-one-index-nine-semisimple-twenty-four-exclusion.json`. The short standalone checker pins the published frontier144, endpoint JSON and primal-interior proof; it checks the exact stable ID, A/B, all four endpoints, stabilizer weights, forced J degrees and section degree4. The representation convention D=Sym^4 W is the same as in the published character table, and P and D are distinct irreducibles.

No broad splitting enumeration, unpublished witness tables, selected actual coefficients or points, matrices or actual rank tests, scans, spikes or consumed experiments enter. This is a necessary-condition pruning of one torsion-structure alternative, not a global realization or whole-branch claim.

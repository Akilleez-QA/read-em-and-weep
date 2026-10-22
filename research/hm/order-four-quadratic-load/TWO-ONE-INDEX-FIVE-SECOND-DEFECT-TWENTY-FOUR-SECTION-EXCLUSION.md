# A seven-to-five section obstruction removes index-5 second defect 24

## Claim

For stable ID **G3.21.ed1df480d8d2**, source pair index 5,

    A=O(-8)+O(4)+O(16),   B=O(-18)+O(-6)+O(6),

the profile (2,1) second defect s=24 is impossible. Its published defect list {0,12,20,24} sharpens to **{0,12,20}**. This is a whole-defect exclusion, not a quotient-case exclusion; the frontier143 count is unchanged.

## Actual-image and endpoint requirements

Write K=E^-, M=K^-, J=K/M, and C=A(-2)=O(-10)+O(2)+O(14). The actual image sequence is

    0 -> J -> C -> T_def -> 0.

The published rank-eleven endpoint theorem leaves exactly two s=24 possibilities:

    cyclic O(4)|2D12,
    semisimple O(2)|D12 + O(4)|D12.

These are different sheaves and are treated separately below. The established endpoint formulas give rank M=11 and

    deg M=-48-2 deg A+s=-48-24+24=-48.

Riemann--Roch implies

    h0(M(4)) >= chi(M(4)) = 11*5-48 = 7.          (1)

The actual derivative M->J(-2) has kernel M^- with maxdeg M^-<=-5, so it induces an injection H0(M(4))->H0(J(2)). We show that each torsion structure forces h0(J(2))<=5 for this same J.

## Cyclic alternative

Choose O(1) fiber weight1 at C10. The source fibers of C have weights {0,2,4}. The cyclic module O(4)|2D12 has top/generator weight4 and socle weight4-12=2 modulo10.

Only the high O(14) summand can supply the top. Surjectivity of the full quotient forces this component to be nonzero on the top at every orbit point. By Nakayama its restriction from O(14)|2D12 onto the cyclic target is an isomorphism of the local length-two modules. The middle summand may map to the socle; this possibility is not discarded.

After twisting by two, the high-summand section map has kernel

    H0(O(16-24))=H0(O(-8))=0.

The low summand has H0(O(-8))=0 as well. Therefore projection of the full section kernel H0(J(2)) to the middle summand H0(O(4)) is injective: any kernel element with zero middle component would lie in the injective high-component map. Consequently

    h0(J(2))<=h0(O(4))=5.

This bound remains valid with every permitted middle-to-socle component and does not choose a quotient map.

## Semisimple alternative

The two tops have weights2 and4. Source weights {0,2,4} force the middle O(2) summand to supply the weight-two target and the high O(14) summand to supply the weight-four target separately. Both components must be nonzero and are fiberwise invertible on the reduced orbit. All cross-components have incompatible stabilizer weights, and the low summand contributes to neither target.

At twist two, the middle restriction has kernel H0(O(4-12))=0. The high restriction has kernel H0(O(16-12))=H0(O(4)), of dimension5. The low summand has no sections. Hence h0(J(2))=5 here.

Both alternatives contradict the injection from at least seven sections in (1), proving the whole s=24 exclusion.

## Reproduction and limits

Run `python3 verify_two_one_index_five_second_defect_twenty_four_section_exclusion.py`.

The standalone verifier pins the published frontier144, rank-eleven endpoint JSON and primal-interior proof. It checks the stable ID, exact A/B, exhaustive torsion list, top/socle weights, both section bounds and 7>5. It writes `two-one-index-five-second-defect-twenty-four-section-exclusion.json`.

No splitting enumeration or unpublished witness tables are inputs. There are no selected actual coefficients or points, actual matrices or rank tests, scans, spikes or consumed experiments. This is a universal exact-sequence obstruction, with no global realization, quotient-case exclusion, smoothing or SF claim.

# The remaining source2 weight-zero torsion has three image strata

## Result and scope

Fix stable ID **G3.21.d610e381ed75**, source index2, with

    A=O(-8)+O2+O16,  B=O(-18)+O(-4)+O6,

and second defect12 with T_def=O0|D12. The actual image kernel J has exactly the following three possible splitting types, according to the scalar components of its quotient map:

| Low component a | Middle component b | Actual J |
|---|---|---|
| nonzero | zero | O(-22)+O0+O14 |
| zero | nonzero | O(-12)+O(-10)+O14 |
| nonzero | nonzero | W O(-11)+O14 |

These are three strata in a projective scalar parameter space for **one torsion alternative**, not three quotient labels. The mixed case is a genuinely non-split extension before passing to its ordinary splitting type.

Moreover, four of the eight published M endpoints contain O(-6). Each of these four forces the first, low-only stratum. Thus eight of the24 formal stratum/endpoint combinations are impossible, leaving at most16 under these particular tests. This is not an exclusion of the torsion alternative, entire second defect, or stable quotient label. No remaining combination is asserted realized.

## 1. The complete scalar parameterization

Write K=E^-, M=K^-, J=K/M. Its actual image sequence is

    0 -> J -> C=O(-10)+O0+O14 -> O0|D12 -> 0.

The C10 source weights are0,0,4 and the reduced target has weight0. Hence the high component vanishes identically. Each lower summand has a one-dimensional equivariant restriction-map space to the target, since an equivariant map on the transitive reduced orbit is determined by its invariant fiber. Denote its scalar by a or b. Surjectivity is equivalent to (a,b) not both zero: a nonzero equivariant component is nonzero at every point of this orbit. Modulo target scaling these pairs form P1; the two coordinate points and their complement give the three displayed strata.

If b=0, only O(-10) supplies the target, giving J=O(-22)+O0+O14. If b is nonzero, normalize its scalar. The kernel N of the two lower summands then fits into

    0 -> O(-12) -> N -> O(-10) -> 0.                (1)

When a=0 this extension splits, giving the second row.

For a nonzero a it does not split. Indeed, apply Hom_G(O(-10),-) to

    0 -> O(-12) -> O0 -> O0|D12 -> 0.

The global lifting space is H0(O10)^G=(Sym10 W)^G=0. The target restriction space is one-dimensional, and the connecting extension space is

    Ext1_G(O(-10),O(-12))=H1(O(-2))^G=C.

The connecting map is an isomorphism: it is injective by the zero lifting space and surjective since H1(O10)=0. Thus a nonzero low component gives the unique nonzero extension class up to scalar. The equivariant Euler sequence, twisted by -11,

    0 -> O(-12) -> W O(-11) -> O(-10) -> 0,

represents that nonzero class. Therefore N=W O(-11), proving the mixed row. In particular the low component cannot be removed by an invariant global lift into the middle summand. All three rows refer to actual image kernels, without selecting source coefficients or orbit points.

## 2. Same-endpoint section pruning

The published rank-eleven theorem lists eight M types for this torsion alternative, all with rank11, degree -56 and top degree at most -4. Let N1=M^-, N2=N1^-, N3=N2^-. Successive kernels are saturated in the same constant ambient bundle. Strict slope gives top N3<=-7, hence H0(N3(6))=0. Their successive images inject into J(-2), J(-4), J(-6). Taking sections and telescoping therefore requires, irreducible by irreducible,

    H0(M(6)) <= H0(J(4))+H0(J(2))+H0(J).           (2)

This does not assign ranks to the later derivatives.

In both strata with b nonzero, the negative summands of J contribute no sections at twists0,2,4. The right side of (2) is

    Sym18 W+Sym16 W+Sym14 W,

which has no trivial constituent. Every endpoint containing O(-6), however, has a trivial constituent in H0(M(6)). Exactly four of the eight published endpoints do so, namely the zero-based endpoint indices3,4,5,7 in the pinned alternative list. They cannot occur with b nonzero. For b=0 the O0 summand supplies a trivial target constituent, and this obstruction disappears.

This uses **H0(M(6))**, calculated from the published endpoint splitting, rather than only chi_G(M(6)). A negative-summand H1 term can cancel that trivial constituent in Euler characteristic, so the weaker Euler envelope need not detect these eight incompatibilities. The stronger section inequality (2) is justified for the same actual J and M.

## 3. Degree-capacity comparison and reproduction

For completeness, maximality makes M an endpoint with first derivative rank at most2. The degree-envelope height vectors therefore have h3=0 and h1+h2=11. Their capacities are30 for the low-only J and22 for each other J, all above the actual degree -56. Thus those degree tests alone exclude none of the three strata; the eight exclusions above are genuinely additional section information.

Run `python3 verify_two_one_index_two_defect_twelve_weight_zero_strata.py` to generate `two-one-index-two-defect-twelve-weight-zero-strata.json`. The standalone exact-character checker pins the published baseline144, endpoint list, primal constraints, strict-slope theorem and finite degree-envelope theorem. It verifies the scalar support, zero invariant lift space, one-dimensional extension space, each J's rank/degree, all eight M endpoint degrees, the three-step character differences, and the stated capacities. The output records the eight removed combinations with full endpoint splittings and character certificates.

The three strata and16 retained combinations are necessary abstract possibilities, not actual-instance constructions or realizations. There are no selected coefficients, points, matrices, actual-instance rank tests, scans, spikes or consumed experiments. No quotient-frontier count or SF conclusion changes.

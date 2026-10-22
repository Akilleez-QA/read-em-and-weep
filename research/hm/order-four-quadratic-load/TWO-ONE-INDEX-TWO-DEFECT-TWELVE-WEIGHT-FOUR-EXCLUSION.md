# Source2 second defect12 cannot have torsion O4 restricted to D12

## Exact claim

For stable ID **G3.21.d610e381ed75**, source pair index2,

    A=O(-8)+O2+O16,  B=O(-18)+O(-4)+O6,

the profile(2,1) alternative s=12 with T_def=O4|D12 is impossible. This removes one torsion-structure alternative only. It does not exclude the whole s=12 branch or the quotient label, and does not change a quotient-frontier count.

## The same actual image is forced

Write K=E^-, M=K^-, J=K/M. The actual equal-rank image sequence is

    0 -> J -> C=A(-2)=O(-10)+O0+O14 -> O4|D12 -> 0.

The published rank-eleven endpoint data include precisely this s=12 torsion alternative for the stated A/B. At a point of the reduced transitive orbit D12 the stabilizer is C10. Naming O1 fiber weight1, the three source fibers have weights0,0,4 and the target has weight4.

Consequently the low and middle components vanish: there is no equivariant map from a weight-zero fiber to a weight-four fiber, and the target is reduced. Surjectivity of the full map forces the high O14 component to be nonzero, hence invertible on the fiber at every orbit point. Its kernel is O14(-D12)=O2. The invariant divisor D12 carries the standard equivariant linearization, with no character ambiguity because the binary icosahedral group has no nontrivial one-dimensional characters. Thus the actual kernel, not merely a separately feasible splitting candidate, is

    J=O(-10)+O0+O2.                               (1)

No lift between source summands or selected quotient map is assumed.

## Apply the finite degree envelope to M

The published actual-stage formulas give rank M=11 and

    deg M=-48-2 deg A+s=-48-20+12=-56.

M is saturated in the original constant ambient bundle and top M<=-4. Its actual derivative factors through J(-2), since M is the Gauss kernel of K. Moreover J=K/M naturally injects into the ambient quotient by M, so this factorization has exactly the actual Gauss kernel. These verify every hypothesis of the finite degree-envelope theorem of PR715, commit8ddbcedc7e01f33ae9aacff56df8da0a33503b57. No rank-three assertion about the endpoint M is needed.

For the decreasing ordinary degrees (2,0,-10) of (1), that theorem requires

    deg M <= max sum_(i=1)^3 [h_i lambda_i-h_i(h_i+1)],

where h1>=h2>=h3>=0 and h1+h2+h3=11. There are exactly16 such height vectors, equivalent to all nonincreasing positive derivative-rank partitions with parts at most3. Their maximum is -60, uniquely attained at (6,5,0). Therefore the actual degree -56 exceeds the necessary upper bound -60 by four, a contradiction.

All permitted endpoint derivative ranks and subsequent ranks are retained. The contradiction arises from coupling the actual image (1) to the actual M, not from pruning an unrelated witness edge.

## Reproduction and scope

Run `python3 verify_two_one_index_two_defect_twelve_weight_four_exclusion.py` to generate `two-one-index-two-defect-twelve-weight-four-exclusion.json`. The short standalone verifier pins the published baseline144, rank-eleven endpoint JSON, primal-interior constraints and finite degree-envelope theorem. It checks the stable ID, exact A/B, torsion alternative, stabilizer weights, forced J degrees, all16 height vectors and the degree gap.

No unpublished witness tables, selected actual coefficients or points, matrices or actual-instance rank evaluations, scans, spikes or consumed experiments enter. The s=12 alternative with a different torsion character is not excluded by this proof. There is no realization, whole-case, profile-closure or SF claim.

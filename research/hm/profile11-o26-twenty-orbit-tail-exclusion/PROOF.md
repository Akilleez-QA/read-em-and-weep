# The twenty-orbit forces an impossible rank drop in the negative tail

## Theorem and scope

The two zero-original-defect maximal profile-(1,1) labels

    G3.11.dc58cc54f352:
      A_q=O(-10)+O(-8)+O(26), B_q=O(-28)+O(6)+O(8),
    G3.11.4b6dad66f329:
      A_q=W O(-9)+O(26), B_q=O(-28)+W O(7)

are impossible.

After the pinned source exclusions, their only possible sources are respectively

    E6 =(P+D) O(-2)+T O(-3)+O(-8)+O(-10),
    E13=(P+D) O(-2)+T O(-3)+W O(-9),

in the degree20 top-divisor stratum. The new argument excludes that final stratum: its degree-twenty divisor forces a generically rank-two negative tail of determinant O(-18) to drop rank on twenty points. Its exterior-square map would have to vanish identically, a contradiction.

The proof does not exclude G3.11.8ae96830fd21, source2, any other retained label, or the global rank possibility. It requires neither the separate defect12 stabilizer corollary nor the essential constant-coupling theorem. It preserves the possible degree12 saturation defect of the projected cubic plane and only uses its absence along the disjoint degree20 orbit.

No selected actual HM/source coefficient, parameter, point, derivative value, matrix, source-instance rank, selected model, scan or large computation is used. All pointwise statements hold at an arbitrary point of a whole invariant divisor. There is no numerical envelope or source-instance calculation.

## 1. Exact immutable source exhaustion

The repository is Akilleez-QA/read-em-and-weep. Original source, stable-label and actual-bundle inputs are at

    db51525015bb7c5e825833d550d08dedf6f6ea96,
    research/hm/order-four-quadratic-load/.

The exact files are ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md, one-one-endpoint-necessary-pairs.json, rank-three-quotient-frontier-144.json, POSITIVE-DOUBLE-HYPERPLANE-GAUSS-GATE.md, and UNIFORM-TWIST-FOUR-FIVE-HYPERPLANE-COHOMOLOGY.md. The two source indices are112 and115. The first of these files explicitly states that the actual E spans the whole constant ambient H.

The full source overlists, restated at PR813 below, are

    index112: E0,U6,E3,E6;
    index115: E0,U6,E3,E6,E10,U13,E12,E13.

Here

    E0 =(P+2D) O(-2)+2 O(-8)+O(-10),
    U6 =(2P+D) O(-2)+Wp O(-5)+O(-8)+O(-10),
    E3 =(V+P+D) O(-2)+V O(-4)+O(-8)+O(-10),
    E10=(P+2D) O(-2)+O(-8)+W O(-9),
    U13=(2P+D) O(-2)+Wp O(-5)+W O(-9),
    E12=(V+P+D) O(-2)+V O(-4)+W O(-9),

and E6,E13 are as in the theorem. U6,U13 are the names for these displayed types, not additional catalog indices.

The exact source-exclusion dependencies are:

- PR813, 3f99ecf539a3a3da61743df0dff409e54270c865, research/hm/profile11-o26-divisor-reduction/PROOF.md. Section1 gives the complete displayed overlists. Its theorem gives top-divisor alternatives0,12,20, eliminates12 for every source, and permits20 only for matching E6/E13.
- PR817, a0b7cbd7a53c1603f284cf0e1a29fff106d02cb3, research/hm/profile11-o26-basepoint-free-top/PROOF.md. Section7 excludes E0 for index112 and E10 for index115 in the basepoint-free stratum, and also records the immediate E0 mismatch for index115. These are all the E0/E10 entries here; their other divisor strata were already removed by PR813.
- PR829, 5e713ff925335b7fb08b5a5768fb558e81fc3575, research/hm/profile11-o26-two-p-polar-exclusion/PROOF.md. It excludes every displayed U6/U13 entry.
- PR834, 71e3d3671474e2990c55ee67fec6d2c65e288649, research/hm/profile11-o26-vpd-polar-exclusion/PROOF.md. It excludes every displayed E3/E12 entry.
- PR840, a69b5a8b9a7c4cb673a89c6465e152fcf699840a, research/hm/profile11-o26-basepoint-free-pd-exclusion/PROOF.md. It excludes the basepoint-free matching E6/E13 cases. The mismatched E6 for index115 cannot surject onto W O(-9): only its single O(-10) summand could contribute, giving rank at most one. This is recorded in Section1 there and in PR813.

Thus all source entries have been addressed except E6 for index112 and E13 for index115 with top divisor20. No source entry is discarded by a count or by an assumed realization status.

The exact remaining geometric inputs are:

- PR825, ea94799a3b1e1c18a4d83061b92d7e7e2f1c631e, research/hm/profile11-o26-degree10-endpoint/PROOF.md: the actual degree-ten constant block and exact endpoint intersections.
- PR845, 3078ec876065f772aa10ef9d8478505035f71db8, research/hm/profile11-o26-cubic-residual/PROOF.md: the six necessary saturated cubic-plane templates, with their saturation defect0 or12.

Every path denotes https://github.com/Akilleez-QA/read-em-and-weep/blob/COMMIT/PATH at its displayed immutable commit and path.

## 2. The actual constant quotient and the tail map

Use W defining, A=Sym2 W, D=Sym4 W, T=Sym5 W, and the usual Wp,V,P. All representations are self-dual. The actual exact presentations imply

    H=M3 tensor W-M2-M4=2A+2V+2P+2D,

using M2=A+2V+3P+4D, M3=3Wp+3S+6T, M4=2V+4P+3D. This is the cohomology character of the actual constant thirty-space, not an imposed model.

Let

    F=(P+D) O(-2)=U_8^10,
    F^+=U_9^10,
    C=Sym10 W=A+V+D,
    L=O(-8)+O(-10) or W O(-9).

PR813 and PR825 give actual saturated subbundles and sheaf intersections

    E intersect C O=F,
    E^+ intersect C O=F^+,
    R=E/F=T O(-3)+L,
    E^+/E=O(28)+L(2).                                (1)

Consequently the constant projection induces an injective sheaf map

    i:R -> Hbar O,   Hbar=H/C=A+V+2P+D.              (2)

No saturation or fiberwise injectivity of all of (2) is assumed. Its full constant span is Hbar, since E spans H.

Let G0 be the saturation of i(T O(-3)), and C1 its full constant span. The six templates of PR845 give

    7<=dim C1<=9,
    C1 in {A+P, A+D, P+D, V+P},                      (3)

and the only possible torsion in G0/i(T O(-3)) has degree12 and is supported on the invariant orbit D12. In particular i on T O(-3) is fiberwise injective at every point outside D12, including every point of the distinct orbit D20.

Set B=Hbar/C1. Equation (3) shows

    dim B>=10, and B contains P.                     (4)

Indeed Hbar has two copies of P, whereas every C1 has at most one. Constant projection kills the T summand in (2), so the induced actual map

    q:L -> B O                                      (5)

spans all of B. This is a full-span assertion for a genuine constant quotient, not a claim that (5) is saturated.

## 3. The tail map has generic rank two

It cannot have generic rank zero by (4)-(5). Suppose its generic rank is one. Its saturation in B O is an equivariant line O(-d), with d>=0. Since q(L) spans B, this line also spans B. The corresponding coefficient map B*->H0(O(d)) is injective, so

    d+1>=dim B>=10, hence d>=9.                      (6)

For E13, a nonzero map W O(-9)->O(-d) is impossible when d>9 by ordinary degree, and when d9 its coefficient map would be W->1, also zero. This contradicts (6).

For E6, a nonzero map O(-8)+O(-10)->O(-d) requires d<=10. The line is center-even, so d is even; the group has no nontrivial one-dimensional character to alter this parity. Equations (6) force d10. Its O(-8) component is then zero, and the O(-10) component is a scalar isomorphism. Therefore the saturated line would have to span B through a coefficient inclusion

    B* -> Sym10 W=A+V+D.

This is impossible because B contains P by (4), and P is absent from Sym10 W.

Thus in both cases

    generic rank q=2.                               (7)

In particular its exterior-square map is nonzero.

## 4. The degree-twenty orbit forces its exterior square to vanish

Let f20 define the reduced invariant orbit D20. The actual map F^+->E^+/E has image

    f20 O(8) subset O(28),                           (8)

and zero component in L(2). This is the top-divisor statement of PR813/825, with F^+/F=O(8). Thus at every point x of D20 its entire fiber map is zero. Since F^+ and E are actual subbundles of E^+, one has

    F^+_x subset E_x.

Both F^+ and F are saturated in the constant bundle. Therefore F^+_x/F_x is a nonzero one-dimensional subspace of R_x=E_x/F_x. It lies in the kernel of the projection i_x in (2), because F^+ lies in C O.

The restriction of i_x to (T O(-3))_x is injective by Section2: its possible defect lies on D12, not D20. Every nonzero vector in this kernel of i_x therefore has a nonzero L component. Writing its two components abstractly as (t,l), one has

    i_x(l)=-i_x(t) in (C1)_x.

Thus q_x(l)=0 with l nonzero. It follows that q drops rank at every point of D20.

But both possibilities for L have determinant O(-18). The global exterior-square map

    wedge2 q: O(-18) -> (wedge2 B) O                 (9)

vanishes on the reduced divisor D20. Hence it factors through

    (wedge2 B) O(-20).

There is no such nonzero map, because H0(O(-2))=0. Therefore wedge2 q is zero identically, contradicting (7).

This excludes the degree20 matching E6/E13 sources. Combined with the complete source exhaustion in Section1, it excludes both labels in the theorem. The conclusion does not use a saturation upgrade for R, an identification of the length-twenty backward image with T O(-3), a selected point calculation, or an assumption that a constant-shear restriction is invertible.

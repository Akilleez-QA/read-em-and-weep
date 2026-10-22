# Independent structural review

Status: PASS. The complete PROOF.md was independently read after the candidate review; the standalone verify.py passed.

The review independently checked the local invariant-ring argument for vertex vanishing, the restriction image of exterior-Euler generators, the ideal-twisted cohomology sequence, the representation dimensions, the homogeneous mixed-functional vanishing, and the independent vertex/class adjustment argument.

On a vertex chart let A=C[a,b,t] with the involution changing signs of a,b, R=A^even, and M=A^odd. For any map M -> R, the images p,q of a,b satisfy (ab)p=a²q by an R-linear relation, hence a q=b p after passing to the domain A and cancelling a. Coprimality makes p=a h,q=b h with h regular odd. The symmetric-square extension therefore has entries h_i h_j in (a²,ab,b²)R. Even weighted twists trivialize on the chart by a nonzero degree-two coordinate; this changes the argument only by units. Thus the published canonical nilpotent restricts to zero on the reduced vertex, without assuming a complete zero-scheme classification.

For E(1), the exterior-Euler generators U Lambda³(V+W) restrict with kernel U Lambda³V. The two remaining summands U Lambda²V W and U V Lambda²W fill H0(E_Z(1)); multiplication by negative cubics fills E_Z(4). Higher acyclicity then gives H1(E_Q(4) I_Z)=0 and H2(I_Z(3))=0; the locally split rank50 resolution gives H1(Ncal_Q(4) I_Z)=0.

The actual mixed-value source at PR543 commit 8d8b5be4ce62c3055bb53be9e16d29cc63072f04, ACTUAL-RAMIFICATION-DETECTS-A-NONZERO-MIXED-FORM-MIDDLE-VALUE.md Section3, explicitly kills every source-end term by the Cartan functional. Its homogeneous form therefore vanishes identically on the joining lines. This proves containment in the mixed-functional kernel, rather than guessing an intersection by subtraction.

The combined vertex/adjoint map is onto: lift the adjoint first, then correct its vertex by a global section of Ncal, which does not change the adjoint. Consequently dimensions684 and680 follow from actual exact maps. The95 source-lift directions remain when only the divided cohomology class is fixed, giving779 and775 full families. No arbitrary-vertex or arbitrary-class reachability follows.

A minor wording refinement was requested in Section1 to derive its odd-coefficient relation from the genuine R-linear relation explicitly; this does not change the proof or result. A direct immutable reference to the mixed-value source was also supplied.

The bounded abstract-character verifier was run independently and passed, including230 ordinary,108 even and54 parameter-family vertex dimensions. These tests check character algebra, not formal proof certification or selected actual HM/source evaluations.

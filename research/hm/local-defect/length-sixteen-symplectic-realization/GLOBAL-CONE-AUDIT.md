# Independent audit of the projective cone

Verdict: PASS after the algebraic-stalk/completion clarification, now verified. Reviewed GLOBAL-CONE.md at SHA256 `ad1e77531d8dd6b90cc07b4440435595d87a488010c503caf124446a6b241e51`.

The polynomial presentation has finite-length cokernel at the origin, so homogenizing in an additional fixed coordinate has rank drop only at the vertex. Its algebraic local stalk is defined over the polynomial local ring; its completion is the formal module of the local construction. The corrected text distinguishes these rings and correctly uses the same algebraic depth/Ext arguments or faithful flatness. Finite-length defects and nonfreeness are preserved. No extra singular point appears.

Every hyperplane missing the vertex identifies with P3 through its four x-coordinates. The restricted complex is everywhere endpoint-exact and yields the stated rank-two bundle. The degree-one independence of the ten relation columns gives H0(ker L)=0; the vanishing of H1(O(−d−1)) on P3 and P4 then gives H0 of the middle cohomology twisted by −d equal to zero for all d≥0. A saturated rank-one subsheaf of a reflexive sheaf has torsion-free quotient and is reflexive by the depth lemma, hence is O(d) on these projective spaces. The section vanishing excludes every nonnegative-degree destabilizer. Stability follows for both the P3 bundle and P4 reflexive sheaf. The stated instanton-type H1(E(−2)) vanishing follows from acyclicity of O(−3), O(−2), O(−1) on P3.

The Euler class of the complex has the sign [F]−[Ptilde]=10[O]−4[O(−1)]−4[O(1)]. The length16 correction contributes +16H⁴, so ch(F)=2−4H²+(47/3)H⁴. Thus c1=c3=0, c2=4H² and c4=−86H⁴. Direct Euler characteristic gives χ(F)=6. The independent minimal-resolution calculation reproduces this K-class. Negative c4 is not discarded by the vector-bundle rank-two formula: F is reflexive and singular, not a vector bundle at the vertex.

The c2 mismatch with the prescribed c2=5 kernel cannot be removed by a twist preserving c1=0. The singleton singular support also cannot support the full irreducible projective Heisenberg action, since it would force an invariant projective point. The construction therefore establishes an abstract algebraic cone with the stated local data while preserving the distinction from the HM problem's global inputs.

This audit covers the corrected cone theorem and its restrictions, stability and Chern calculation. It does not establish a parameter-flat family unless separately proved, nor evaluate an actual source instance.

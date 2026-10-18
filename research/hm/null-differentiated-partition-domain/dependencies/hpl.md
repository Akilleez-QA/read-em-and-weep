## 4. Recurrence, degrees, faces and top closure

With D=delta_Cech+(−1)^q d_End, a component J_s of bidegree (2+s,−s) must satisfy

    delta J_(s−1)+(−1)^(s+2) d_End J_s=0.

Thus the exact solution is

    J0=jR,
    J_s=(−1)^(s+1) H_(1−s) delta J_(s−1), s=1,2,3.

The shared schema's signs +,+,−,+ and homotopy input degrees 0,−1,−2 match this formula. The compiler uses precisely these fields. In `at(s,t)`, h belongs to t[0], selected before evaluating the next face deletion. Recursive face calls select their own new leading owner, retaining any outer H owners already selected. The tuple arities are s+3; face deletion preserves the input order. Expanding signed face words yields 1,4,20,120 words for J0...J3. This matches the accepted JC owner program. No sorting, directional-source reconstruction, or loss of deleted prefix owners occurs in these methods.

For a source-increasing input tuple the methods therefore denote exactly the accepted construction. `Lift.at` checks distinctness and length but does NOT enforce source-increasing order: that is a caller/domain premise. Unsorted nonlinear source reconstruction is not certified by this theorem. Formal agreement on an arbitrary ordered tuple is not permission to identify it with the alternating extension of a differently constructed source.

Now d_End J0=0 by the chain-map identities. Put F1=delta J0. Then d_End F1=0 by commutation with restrictions, and its cohomology projection is zero by §2 and complete raw cocycle closure. The homotopy identity yields d_End J1=delta J0. Inductively d_End delta J_(s−1)=0 because delta²=0; negative degree removes the projection term. Hence

    delta J0−d_End J1=0,
    delta J1+d_End J2=0,
    delta J2−d_End J3=0.

Finally W=delta J3 has internal degree −3. It has only block K3→K0; d_End W has blocks W ev and gamma W, with positive signs since degree −3 is odd. Commutation and delta² give d_End W=0. The K0 contraction identity gives H0 gamma=1, so gamma W=0 implies W=0. Thus delta J3=0. Equivalently, degree −4 is absent and the End contraction implies injectivity in degree −3. This is a universal seven-owner proof: J3 has six inputs, its Cech boundary seven. It is not a claim that a six-owner circuit evaluated that boundary.

## 5. Stage two terminal versus stage three mathematics

Frozen `source_and_lift(model,owners,stage=2)` constructs the shared Lift and calls `at(stage,tuple(owners))`. Its default computes J2 and its predecessors only; it does not compute J3 or validate any closure equation. This is correct for a terminal scalar selector L on internal degree −2. It is not a self-contained closure certificate.

The schema and compiler template retain J3; `compile_template` explicitly describes stages 0...3. Mathematical correctness of the terminal reduction uses the independently defined J3 and the theorem delta J2=d_End J3. If L d_End=0, then delta L(J2)=0. The terminal formula contains the single J2 minus sign:

    −lambda L S Pi_outer H_-1 delta H_0 delta j(R).

The full outer regular comparison still requires the accepted common domain through J3 and the seven-owner boundary. Its corrected prism statement clears only inserted owners with weights and retains suffix divisors in the allowed common-cover domain. Stage-two evaluation alone proves none of this.

JC's original-frame/full-sign identification gives conversion tau^(r−2), so J2 is in the deck-removed tau^-4 frame before L; J3 has tau^-5. These are imported geometric identifications, not extra Laurent factors to append to the already interpreted original-resolution products. This audit finds no omitted transport or face-order defect in the literal Lift methods. It does identify the exact premises that cannot be silently inferred from their code: common ambient/line-frame transport, correct source-increasing input, same-source raw cocycle, contraction identities, scalar chain-map property, and admitted outer regular comparison.


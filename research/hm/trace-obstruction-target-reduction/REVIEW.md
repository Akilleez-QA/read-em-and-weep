# Independent review of the target-reduction lemma

Verdict: PASS. The target-reduction argument is correct in the fixed harmonic frame. The final proof includes the required determinant-one coordinate choice. It does not determine the residual map's rank or value.

## Frozen material and evidence

Final PROOF.md SHA256: ceaf166f8814365e24d9f7264b813836f0262cde760eac1a4fc236f2ad07cb70.
Final verify.py SHA256: bb160827401243ad1235be2b0b83f0b20e0b09e19fea77bd3e65ad1256ef505e.
I reread the complete final proof and verifier and directly retrieved its immutable [PR717 dependency](https://github.com/Akilleez-QA/read-em-and-weep/blob/7362df9da60a3b87b3200078a0145a376cc3056b/research/hm/nilpotent-trace-lift-invariance/PROOF.md), Git blob a41c18fda3f34e4357d9854b9c0afe7d34399bde. The final changes are the immutable dependency, standalone wording, and explicit SL2 coordinate choice; the mathematical calculations are unchanged.

I independently retrieved the full [PR716 proof at its pinned commit](https://github.com/Akilleez-QA/read-em-and-weep/blob/2a602d811b904def02bd56518fb0549e2911ff3e/research/hm/firstnormal-trace-variation/PROOF.md), Git blob e9b51b438105f9c9577da5eb9fedc812de6131e6, and the full [pinned universal harmonic-product theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/UNIVERSAL-SECOND-NORMAL-HARMONIC-PRODUCT-AND-OPERATOR-DEFECT.md), Git blob acab5fcac801d0843306d4afb74228191a00b2a4. I also retrieved sections 1–2 of [the frame dependency PR692](https://github.com/Akilleez-QA/read-em-and-weep/blob/858f96ba1539afb1293f31239b8761af08e46f60/research/hm/vertex-scalar-filtration/PROOF.md), Git blob bc9a9a2aa1b4d7343de5c4168d93bb8017e155bb.

The script was read before execution. Only its fixed four formal-jet identities and elementary arithmetic checks were run. It printed PASS and exited zero. No actual HM/source coefficients, points, derivative values, or matrix ranks were evaluated. No large computation or GitHub write occurred.

## Independent checks

1. The universal theorem uses ordinary derivatives and gives B1=tau2/[2(d-1)(e-1)(d+e-1)] for positive even binary degrees. The entry pairs (8,8), (6,10), (8,4), (6,6) therefore have denominators 1470, 1350, 462, 550. All entries being multiplied have even degrees; odd f, g, and ell are merely polynomial factors, not separately lifted harmonic inputs.

2. Entrywise ordered multiplication gives c=u²(B1(fg,fg)-B1(f²,g²)) and b_ell=u(B1(fg,ell f)-B1(f²,ell g)). In the latter expression the diagonal factor 1/2 in A and the scalar trace factor 1/2 are canceled by the two diagonals and two product orders. Ordinary tr(T ell A)=ell(fx+gy). Thus there is no missing factor two or sign in (3)–(6). The common coefficient u is retained throughout and inverted only as an element of k×.

3. Formula (7) follows from the chain rule for p=X^d P(Y/X). Modulo F, the formal product jets are (FG)'=F'G, (F²)'=0, (F²)''=2(F')², and (LF)'=LF'. These give exactly the four coefficients -98, 180, -42, 60 in (8), without assuming F square-free. The rational combinations are -98/1470-180/1350=-1/5 and -42/462-60/550=-1/5.

4. The final proof explicitly makes an SL2(k) coordinate change. One can choose X avoiding the finitely many linear factors of f and complete it to a determinant-one pair over the infinite field k. This preserves tau2 and the fixed quadric normalization, so the displayed constants remain valid. No actual roots need be computed or selected. The earlier coordinate-choice ambiguity is fully resolved.

5. Homogeneous regularity gives gcd(F,G)=1, so the class of G, and hence G², is a unit in k[t]/(F), even when this quotient has nilpotents. Reducing (5) gives uG² y-u²G²(F')²/5=0 and hence (10). Its substitution in (6) cancels modulo F. This uses ideal membership, not a rootwise test. On the chart X≠0 it proves Psi lies in (f)S[X^-1]. Consequently X^m Psi lies in (f) for some m. Since gcd(X,f)=1 in the UFD S, every irreducible factor of f with its full multiplicity divides Psi. Thus f divides Psi globally, including for nonsquarefree f.

6. Multiplication by the fixed nonzero cubic f identifies fS5/(f²S2+kfg) with S5/(fS2+kg)=(S/(f,g))5. Regularity implies g is not in fS2, so the denominator has dimension 3+1 and the quotient has dimension 6-4=2. The inclusion into Q8 is injective because its denominator is the same subspace. The complementary quotient is S8/fS5, of dimension 9-6=3. The source K is identified with S1 by ell↦ell A, also of dimension two. None of these dimensions is a numerical rank evaluation of the obstruction.

7. Replacing T by T+eta A changes Psi/f by f eta ell/2, which belongs to fS2. Thus the reduced class is independent of the nilpotent lift, as asserted. 'Canonical' here is relative to the fixed frame and fixed f,g,u and harmonic convention, not a new assertion of invariance under arbitrary changes of those inputs.

## Equation units and limitations

The fixed-q convention agrees with the pinned frame dependency. The universal product theorem also explicitly treats q0=nu q: then B1, T, and Psi scale by 1/nu. Hence divisibility by f and the reduced target survive this unit transport; the map itself scales by 1/nu. There is no authorization to drop the physical equation unit while comparing numerical representatives in different frames. The coefficient unit u in the present formulas is distinct and has already been retained.

This review proves the new reduction assuming the first-normal square-zero equation and the cited regular-pair/frame inputs. The pinned PR717 dependency includes a separate actual-nonemptiness paragraph, using the exact chart definition N_s=U_(s²)/s². Its three global lift/coherence premises are cited inputs, not independently recertified by the four-identity computation in this review. This limitation does not leave a new assumption in the target-reduction argument beyond its expressly retained dependencies.

The verifier confirms formal universal polynomial identities, not the cited harmonic construction, regularity, actual nonemptiness, global realizability, the residual rank/value, a Bockstein identification, or the base fourth-square obstruction. The result removes the entire three-dimensional quotient projection and leaves a two-dimensional-to-two-dimensional local obstruction. It does not assert that this remaining map vanishes. This is an independent mathematical review with a tiny symbolic check, not proof-assistant certification.

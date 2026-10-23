# Independent review: source127 h-b-f exclusion

## Verdict

**PASS. No mathematical correction is required.**

This review verifies the new closure and its exact interface to the already reviewed, pinned PR885 reduction. Together they exclude the displayed source127 h-b-f edge, including its remaining nonzero negative scalar row. This is not an exclusion of every compatible E type at source index 127, an exclusion of the stable label, or a global frontier-count update.

Review date: 2026-10-23. The reviewed files were left unchanged:

- `PROOF.md`, SHA256 `1740dd7bb504cb49c726952373f74700e3396b7a8a94a1f89e7e3f6121775e38`.
- `verify.py`, SHA256 `27d003e5c19599ab1c7cc12ceea60b0b5658779dd49659a1cdec4fde55d71e92`.

The fixed verifier ran successfully. I also performed a separate small representation-ring calculation using the affine-E8 tensor-by-W graph, not the verifier's quadratic-field character table or its implementation.

## Immutable inputs and scope

I read the entire PR885 proof, the original actual-presentation note, and the original strict-top proof. All five supplied input bytes match their manifest Git blob hashes. Their SHA256 hashes are:

- `ACTUAL.md`: `a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256`.
- `STRICT-TOP.md`: `53ff5daf7e656bb1ec2dcf5feebd2813e2dbfbd6489a3a65117960f492b4cc08`.
- `pairs.json`: `6002ad138a41d98c351130a29703722979f31b8da90d7c75a120f28bf89480eb`.
- `frontier.json`: `a6fc9ec680d1866782e0233c234c5d80d398e9fc77734b59e61040ffc92021ad`.
- `PR885.md`: `3e3a994defbeea2cefff4b0a64a93f70e0059417f8850a79d85069c1d45ab169`.

The reduction is exactly commit `53939364de5459822be1a32be08f2b12dbbb4280`, proof Git blob `3d473e81c158e45c923a1177e71701c40ac477c5`. The other four inputs are pinned at `db51525015bb7c5e825833d550d08dedf6f6ea96`. The catalog check identifies the original defect-zero A and B endpoints and the specific compatible tuple `(0,1,0,0,0,1,0,1)`.

This review relies on PR885 and its previously established dependencies as the prior reduction; it does not claim to re-prove every lemma imported by PR885 from earlier publications. It checks the full reduction's surviving interface rather than treating PR885 as a whole-edge exclusion.

## Coverage of the prior reduction

PR885 Section 2 gives the five high-P kernel alternatives and their complete internal-image alternatives. Sections 3-4 exclude the zero low-D row and the constant first-span alternative. Section 5 excludes the nine-dimensional constant span, eliminates case I, and treats both values of the negative scalar row in case II. Section 6 excludes case IV; cases III and V were already eliminated in Section 2. Section 8 supplies the degree-38 obstruction used for the eliminated alternatives, including case II with zero negative scalar row.

Consequently the sole remaining case is precisely the one used here: actual first span M=(Wp+T)O(-1), full constant span C=V+P+D, Y/M=W O(-3)+O(-6), C/Y=O(20), E^+ intersect C=Y, zero O(4) row, high row onto O(18) already on M, and a nonzero scalar negative row. The optional internal T component remains unrestricted. Nothing in the new argument restricts that component or silently removes the negative row. Eliminating this interface therefore closes the entire specified h-b-f edge.

## Actual intersections and the rank-two quotient

The negative map Y -> O(-6) is onto: it factors through Y/M, kills W O(-3), and is an isomorphism on the equal-degree scalar quotient. Its kernel Y0 contains M and has Y0/M=W O(-3). It is saturated in C because both Y/Y0 and C/Y are locally free. Thus rank(Y0)=10 and degree(Y0)=-14.

The actual intersection X=E intersect C is the kernel of Y -> E^+/E, since E^+ intersect C=Y. The middle row vanishes, and taking the negative-row kernel first leaves exactly the high row Y0 -> O(18). This map remains onto because M is contained in Y0. Therefore X has rank 9 and degree -32. These are actual intersections and kernels, not identities inferred from abstract splitting types.

V0=C/Y0 is globally generated and has rank 2 and degree 14. A section of V0* would be a constant functional on C annihilating Y0, hence annihilating F, whose full constant span is C. Thus H0(V0*)=0, so every ordinary splitting degree of V0 is positive. Equivariant splitting and central parity leave exactly W O(7), Wp O(7), and the three scalar pairs of positive even degrees summing to 14. The five Euler characters in the proof are correct and distinguish Wp O(7) uniquely.

The quotient sequence C/X -> C/Y0 has kernel Y0/X=O(18). Its extension class vanishes because H1(Wp O(11))=0; equivariant splitting follows by averaging. Hence U0=C/X is exactly O(18)+Wp O(7). This does not yet assume U0 saturated in Q.

## Saturation and the strict-top endpoint

Both Q/U0 and (H/C)/(E/X) identify with H/(E+C). Their torsion therefore has the same length delta. The projected E/X has rank 8 and degree -22. Its saturation Z still has full constant span H/C, because E spans H. The injection (H/C)* -> H0(Z*) gives

    18 <= h0(Z*) = 8+22-delta.

Here the equality is justified by Z being a subbundle of a constant bundle, so every degree of Z* is nonnegative. Thus delta<=12. The torsion divisor is G-invariant; its minimum positive possible degree is 12. Only delta=0 or delta=12 remains. No projected derivative-rank assertion is used.

At delta=12 the saturation U has rank 3 and degree 44. Its dual quotient R=(Q/U)* has rank 10 and degree -10. Since R is a subbundle of Q* and H0(Q*)=0, every degree of R is at most -1; hence R=R10 O(-1) and h0(R(1))=10. The exact original dual endpoint, together with strict-top for Q*, injects H0(Q*(1)) into H0(B_q(1))=Sym7 W=Wp+T, of dimension 8. This contradicts R subset Q*. The use of B_q is the original source127 endpoint, not a substituted endpoint. Therefore delta=0 and dualizing the quotient by U0 is legitimate as a short exact sequence of vector bundles.

## Cohomology and complete support obstruction

The original presentation gives H1(Q*)=M2 and chi_G(Q*(1))=M3-M2 W. In the exact sequence

    0 -> R -> Q* -> O(-18)+Wp O(-7) -> 0,

both right-hand and middle H0 vanish. The resulting H1 sequence is short exact because H2 on P1 vanishes. Thus the subtraction in the proof is valid, not merely an unsupported virtual identity. It gives H1(R)=V+P+D. Independently, twisting the original presentation by one and using Euler additivity gives exactly chi_G(R(1))=-W. The ordinary dimensions also agree: rank(R)=10, degree(R)=-22, h1(R)=12, and chi(R(1))=-2.

R is center-even. For an atom B O(-j), its coefficient therefore has center sign (-1)^j. Each j>=2 atom contributes a genuine subcharacter B Sym^(j-2)W of V+P+D, with dimension (j-1)dim(B)<=12. Checking this finite bound and parity gives exactly the twelve listed atoms. In particular, odd j>=9 exceed the budget; the only scalar candidate at j=12 contains A and fails; larger j exceed the budget. Degree -1 atoms are not incorrectly discarded: after twisting by one, they contribute only to H0 and hence cannot make the W Euler coefficient negative.

For an independent calculation I used the tensor-by-W identities

    1 -> W; W -> 1+A; Wp -> P; A -> W+S;
    V -> T; P -> Wp+T; S -> A+D; D -> S+T;
    T -> V+P+D,

and the recurrence B Sym^n W = W(B Sym^(n-1)W)-B Sym^(n-2)W. This reproduces all five rank-two characters, both original-presentation subtractions, all twelve admissible H1 atoms, and their displayed twist-one H1 characters. Every such twisted H1 character is W-free. Nonnegative W multiplicity in H0 then contradicts the coefficient -1 in chi_G(R(1)).

## Computation and conclusion boundary

Only the frozen abstract verifier, immutable-input hashes and fixed catalog identity, and the independent small universal representation recurrence were evaluated. No selected actual HM/source coefficient, parameter, point, derivative value, matrix, instance rank, model, scan, or large computation was used. No files were published.

The geometric arguments and the original presentation together supply the proof; the checks certify the finite arithmetic and support list. Under the stated pinned actual inputs and prior reduction, the new contradiction is rigorous and closes the exact source127 h-b-f edge.

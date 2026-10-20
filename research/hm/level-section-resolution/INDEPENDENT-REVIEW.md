# Independent review: exact adjoint section resolution

## Verdict and reviewed artifact

Accepted. The reviewed `PROOF.md` has SHA256

    0e7df08243d9cd60c812d29f57a88edd8bd87880670f640f7e6ac4562d740e41

This review independently checks the new deductions against the stated pinned inputs. In particular, the compact evaluation complex and its local regular-sequence verification, the section-module shifts, and the depth/regularity bounds were checked against the PR485 proof. No change is requested.

## Exactness in all integer degrees

On P^4 the first three intermediate cohomology groups of every line bundle vanish. Applying this to the first short exact sequence in (8) gives both H^1(A_t)=0 and H^2(A_t)=0 for every integer t, not merely for nonnegative t. It also gives the displayed full section-module resolution of mathcal A. Taking sections of the second sequence is therefore right exact, and its next cohomology segment identifies H^1(J_t) with V_s tensor H^1(E(t)).

The indexing is consistent: t=j-6, E=F(3), and hence H^1(E(t))=H_(j-3). Its possible degrees are j=3,4,5,6. The line-residue module is a direct sum of 25 coordinate rings shifted by 8, since ell squared has degree -2. It begins in degree 8. Thus the connecting homomorphism from the residue sections to H^1(J_t) is zero in every degree, proving the actual exact module sequence (12). This step does not assume that a sheaf-surjection automatically induces a section-surjection. All identifications respect the polynomial action.

## Mapping cone and the decisive Tor sequence

For an injection A into Q, a cone resolving its cokernel has terms Q_0, Q_1 plus A_0, Q_2 plus A_1, Q_3 in this case. Substituting (9) and the shifted primary section resolution gives precisely the terms used in Section 5 before cancellation. The degree-six component of A_0 to Q_0 is the alternating inclusion from Lambda^2(V_s) to V_s tensor V_s. It has dimension six and is injective over C. Canceling these six scalar pairs removes six S(-6) summands in homological degrees zero and one and leaves exactly (13).

No minimality of the remaining resolution is needed. After tensoring with C its chain groups in internal degree nine are zero in homological degrees zero and one. Consequently both Tor_0(mathcal J,C)_9 and Tor_1(mathcal J,C)_9 vanish. Each line coordinate ring has three linear first relations, giving 25 times 3 equals 75 for Tor_1(R,C)_9. The exact Tor segment in the proof then supplies an isomorphism, not only an inequality, between Tor_1(G,C)_9 and this 75-dimensional space. Thus a=75 is rigorously forced. The adjacent degree-nine summands of the final minimal resolution cannot be canceled merely because their shifts agree.

## Level endpoint, duality, and full resolution

The Rao module is the cokernel of the restriction map from S to the direct sum of the line coordinate rings in every degree; it is therefore generated in degree zero. Its shifted graded dual has no socle below degree six, and the same is true for its submodule N. For the primary cohomology module, the proof correctly uses the kernel of the adjoint map H_d to Hom(T,H_(d+1)), rather than the kernel of aggregate multiplication. Generation and irreducibility of the stated primary pieces imply this adjoint map has zero kernel below degree three. The extension argument then excludes every lower-degree socle element of K without assuming a splitting.

Given these pinned primary representation inputs, Soc(K)=K_6 has dimension 32. Local duality with the five-variable canonical shift S(-5) correctly identifies Ext^3(G,S(-5)) with K dual. In a minimal length-three resolution its minimal generators read off the final free module. A generator of Hom(S(-b),S(-5)) has degree 5-b, so the 32 degree-minus-six generators force 32S(-11).

The Hilbert numerator and the shift windows yield F1=140S(-8)+aS(-9) and F2=(a+5)S(-9)+75S(-10). Setting a=75 gives the asserted complete resolution. Its alternating numerator is 10t^6+60t^7-115t^8+5t^9+75t^10-32t^11, consistent with rank three and the stated Hilbert values. The high-tail Tor consequences follow with the two-step homological index shift already established in PR485. The proof correctly leaves the separate lower-degree cubic ambiguity unresolved.

## Verification boundary

This is an independent mathematical review of the derivation and its explicitly pinned dependencies, not a formal proof-assistant verification. It neither evaluates a selected HM/source instance nor computes a numerical multiplication matrix or rank. No coefficient search, generator/checker execution, or large computation was performed. No conclusion about fixed-source membership, the original polynomial pair, higher-order lifting, or algebraicity follows from this review. No public repository action was performed by this reviewer.

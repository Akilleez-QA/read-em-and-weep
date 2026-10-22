# Independent mathematical review

## Verdict

The smooth-locus containment and global factorization proved in PROOF.md are correct under their explicitly pinned actual first-normal, third-square, and Serre-locus inputs. Reviewed the final extension sections as well as the conic calculation. The argument correctly leaves vertex square-ideal membership unresolved. This is independent mathematical review, not proof-assistant certification or an actual-instance evaluation.

## Checks

- Read the pinned corrected third-neighborhood theorem at commit 8d8b5be4ce62c3055bb53be9e16d29cc63072f04, especially its conic coherence/tangent formula. Read the fourth-square invariance proof underlying PR687.
- On a positive affine chart at a closed conic point, the physical negative coordinates and the actual quadratic equation can be retained in formal regular parameters. The coefficient-ring splitting makes the actual negative quadratic source independent of q. The unit determinant factor u remains present.
- Lifting the nilpotent matrix through that coefficient ring preserves its square-zero identity. The first-normal tangent formula then gives N,T in Mat_2(I^2), without computing any actual coefficient.
- The first derivative of the positive source is correctly included as beta=b-a h_1. No assumption that h is independent of q is made.
- For trace-free two-by-two matrices, the polarized identity is AB+BA=tr(AB)Id. Accordingly the q^2 relation is a^2h(hc+tr(NL_2))=0, with no missing factor of two.
- Cancellation is in a regular complete local domain by the nonzero elements a,h, not inversion on a source-unit open. It therefore retains the source-zero locus.
- The chosen lift L has zero q^3 coefficient. Its cubic scalar is tr(L_1L_2); an arbitrary fourth lift differs from aL by q^3K. The resulting sign and factor are S_4=a^3h[tr(TL_2)+beta c+tr(NK)].
- The bracket is in the full I^2: the two trace terms use N,T in Mat_2(I^2), while c belongs to I^4. Faithful flatness of completion descends this exact principal-times-ideal membership.
- Executed the bounded universal verifier successfully. It checks symbolic rank-two polynomial identities and I-adic lower bounds only. It does not instantiate selected HM/source data.

## Smooth-locus and Hartogs extension

The same scalar algebra proves a^3h divisibility on every other smooth chart where the actual Serre ideal is the unit ideal. Indeed choose the formal splitting retaining physical s,t and a. In any extended local bundle frame, lift N|Q entrywise through the coefficient ring, preserving N^2=0. Writing U_a=aN+qT, its square-zero identity modulo q^2 gives a tr(NT)=0 and hence tr(NT)=0. The remaining calculation does not use the special conic tangent formula, and I^2=O makes bracket membership automatic.

Using the pinned support assertion identifying the smooth Serre locus with the conic, the quotient extends regularly throughout the smooth locus. Normality and codimension-two singular locus then permit Hartogs extension as a section of O_Q(6). These observations do not establish membership in the full square ideal at the vertex. They do not prove global square-zero, compute a fourth Bockstein, or imply algebraicity.

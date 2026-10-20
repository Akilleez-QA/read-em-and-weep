# Independent source audit: explicit third-order ambient representative

PASS, reviewed 2026-10-19.

Source: https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6260064519 (05:03:11 UTC). The pinned PR16 regular identities and conventions were previously read and audited in SOURCE_AUDIT.md. Only universal symbolic consequences of these identities are checked here.

The total degree-one cochain eta_i=a_i omega_i+q_i is closed: its Cech derivative cancels the negative de Rham derivative of its Cech-degree-one part. Expanding the Alexander–Whitney product gives exactly the stated endpoint-dependent alpha. Contraction of the displayed T with omega has the same signs. Total closedness then gives d zeta=0, delta zeta=d alpha, delta alpha=-db, and delta b=0.

Since delta zeta=L_T omega and the inverse-bivector correction is rho=-P Z P in the stated matrix convention, delta rho=-L_T pi. On each two-dimensional pair, -P(zP)P=zP, giving the stated scalar multiples of the pair bivectors. Thus the added third product coefficient has the correct sign.

At third order a biderivation is a Hochschild cocycle, so the local associativity equation remains satisfied. The overlap equation from the earlier third-order audit becomes delta mu3+L_T mu1=0 with S=F3=0, and the stated rho satisfies it. The third-order inner automorphism term vanishes by the symmetric second Moyal coefficient and the cancellation involving b²/2. The new mu3 does not enter that inner calculation before order four. The already audited scalar equation for c supplies the remaining unit identity. Hence this is a complete ambient extension modulo h4, with explicit product and overlap coefficients but only existence of the third unit correction.

The two-parameter specialization also checks: factor separation kills every mixed Lie derivative, mixed Hamiltonian bracket and cross action of T on the other b. The cubic unit defect therefore consists only of the s³ and t³ pair terms.

Finally, the ordinary-nerve product c_ij=q_i*q_j obeys delta c_ij=-(q_i cup q_j+q_j cup q_i). The Cech-degree-one part of eta_i eta_j+eta_j eta_i is d c_ij, while its degree-two part is -delta c_ij and its degree-zero part vanishes. Thus the full anticommutator is -D c_ij. Subtraction of the two displayed Pi representatives gives exactly -delta(c12+c34)/8.

The result supplies an explicit solution to the variable-product third-order equation left open by the fixed-Moyal criterion. It does not prove the original T to be Poisson for frozen products. The period/central-curvature identification, explicit c, higher explicit coefficients, module extension and retained detector values remain open as stated. No outstanding correction.

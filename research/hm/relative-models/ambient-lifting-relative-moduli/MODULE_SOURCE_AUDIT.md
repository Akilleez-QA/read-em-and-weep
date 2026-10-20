# Independent source audit: two-parameter ambient and module lifting

PASS, reviewed 2026-10-19.

Source: https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6259871686 (04:46:23 UTC). The preceding literal-lifting lemma and the pinned PR16 conventions were independently audited in SOURCE_AUDIT.md.

The two-parameter two-jet has the correct coefficients: expansion of the commuting pair operators gives the mixed product coefficient DP DQ/4, and the exponential unit gives bP bQ. Factor separation removes mixed inner-gluing contributions. The diagonal recovers the fixed two-jet. The small-extension proof works with the finite-dimensional kernel (s,t)^N/(s,t)^(N+1). Its deck characters are all even, whereas HH3 characters are odd; invariant obstructions therefore vanish. The formal full-deck ambient-family conclusion follows with higher products allowed to vary.

The module four-index identity has consistent row order g_jk*g_ij=g_ik. Expanding the two bracketings, then using inner gluing and the ambient pentagon, gives the four displayed terms. On the square-zero kernel, multiplication and transport reduce to classical ones. Multiplication by g_il inverse turns them into C_ikl+C_ijk-C_ijl-tau_ij(C_jkl), which is minus the standard Cech differential. Thus delta C=0. The correction G_ij+g_ij*x_ij adds exactly delta x to C.

The ambient-change map retains precisely u_i(g_jk,g_ij), v_ij(g_jk)g_ij, and -a_ijk*g_ik. Terms with positive-order old coefficients vanish on the small-extension kernel, and normalization removes u_i(1,g_ik). For a total boundary, expansion of bt cancels the t_i(g_jk) term against delta t; what remains is delta of g_ij inverse times [t_i(g_ij)-s_ij*g_ij]. This verifies descent to the stated characteristic map with the negative gerbe sign.

Consequently a fixed ambient extension has obstruction in Ext2, while freely choosing the new ambient extension gives the cokernel of the permitted characteristic map. The full-sign conclusion is conditional on the classical deck linearization/equivariance, exactly as stated: HH2 has only weights zero and two, and diagonal inversion does not remove the even full-sign component. Changes of older coefficients can still enter future equations nonlinearly. The two-parameter first-order module existence is likewise conditional on the accepted first-order cancellation and does not provide a second-order module lift.

No detector values, full module quantization, all-order frozen Moyal extension, or higher-choice independence are established. The delivered relative 28-dimensional one-parameter ambient torsor remains compatible and distinct. No outstanding correction.

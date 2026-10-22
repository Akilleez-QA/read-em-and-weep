# Independent mathematical review

Reviewed `PROOF.md`, SHA-256:

`83e9508b23cd427a6a1afa04033e53869ec446d968b54bb4d375d8c01b378516`

Verdict: **PASS for the stated conditional structural theorem.** This is an independent deductive review, not proof-assistant verification. No selected actual HM/source instance, coefficient, point, derivative, matrix, or rank was evaluated; no numerical scan or large computation was performed.

## Dependency and field checks

The pinned PR747 identity supplies C-linearity of K, the full five-dimensional trace-free self-adjoint source space, nonzero d, and the distinction between the immutable modular gate and the actual fourth-square scalar. PR752 supplies the exceptional-pencil criterion. PR759 supplies the projected Veronese embedding and the dimension bound for two-dimensional exceptional kernels. These inputs were checked against their pinned public proof files. In particular, linearity is over C, whereas d spans a line over k=C(P1); the proof does not confuse these two fields.

## Checks of the new argument

1. H0 is a linear subspace: it is the inverse image of the C-linear subspace kd under K. Outside it no nonzero a can solve the identity. The finite-dimensional rational-function image of H0 has finitely many poles and a coefficientwise maximal pole divisor. The leading polar coefficients are linear functionals, so all maximal orders occur simultaneously on a nonempty Zariski-open subset.

2. The pole condition for a nonzero solution is exactly containment of the polar divisor in its degree-two zero divisor. Each H_F is linear, multiplication maps A_F into A, and the displayed maximal minors detect a nonzero kernel. There are only finitely many effective subdivisors of D. Thus the finite union is closed in projective H, including empty strata and the case H0=0.

3. Density forces H0=H and pole degree at most two. In degree two, the space of sections vanishing on D is one-dimensional even when D is a doubled point. Its fixed generator works densely; C-linearity then extends its compatibility identity to every source.

4. In degree zero, restriction to the diagonal forces the linear functional r to equal one diagonal entry. Each first off-diagonal coefficient of the characteristic determinant forces the corresponding remaining coefficient of r to vanish. The resulting second-order term u^2(2x+y) is nonzero. This is an identity in free indeterminates, not a source-instance evaluation.

5. The degree-one self-adjoint matrix has the correct signs and factors for B(U,W)=1 and B(T,T)=-1/2. Its restricted minors are exactly p^2, pq, and q^2+pg. These remove the c and g coefficients of p and q. The remaining rows-1-and-3 minor has unavoidable g coefficient -b. Hence this case cannot be dense.

6. The converse common-direction implication is immediate. Uniqueness follows from the cited dimension bound, which prevents two independent directions from being exceptional for every source. Thus the two alternatives are exhaustive and exclusive without choosing the actual alternative.

7. In the common-direction branch, the repeated eigenspace v-perp contains a0 exactly when B(v,a0)=0. The converse compatibility also holds for isotropic v and eigenvalue zero. Restricting the projected Veronese embedding to this projective line gives a smooth plane conic; away from it the kernel is exactly C a0.

8. The boundary length is two: B restricts to a nondegenerate binary quadratic when a0 is nonisotropic, and to rank one with radical C a0 when a0 is isotropic. Thus the latter intersection is the doubled point, not two distinct points.

An additional scheme check supports the conic geometry. Substituting the common-direction identity into PR759's coefficient equation gives Psi(v)=gamma B(v,a0)(v/a0)d. The coefficient linear forms of v span A* and have no common projective zero. Its ideal sheaf is therefore the reduced linear ideal B(v,a0)=0. No stronger scheme claim about arbitrary pole strata is needed.

## Limits retained

The result does not determine the actual map K or select either branch. It proves no modular-gate sufficiency for rho4, no value or vanishing of beta4, and no algebraicity or source-realization statement. No group invariance of the chosen mod-(f3) gate is assumed. Publication and any later source-specific evaluation are separate actions.

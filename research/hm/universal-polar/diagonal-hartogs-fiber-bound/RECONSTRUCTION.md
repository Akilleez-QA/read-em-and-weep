# Repeated-input independence and exact residual reconstruction

Work over C. Let f:V^3 → J be outer symmetric and cyclic zero, and assume A_a:V/Ca → J, b ↦ f(a,a,b), is injective for every a≠0. For independent a,b, the vectors A_a(b), A_b(a) are linearly independent. Each is nonzero. A dependence A_a(b)=t A_b(a) would imply

A_(a+tb)(b)=A_a(b)−t A_b(a)=0,

by expanding the left side and using f(b,a,b)=−2A_b(a) and f(a,b,b)=A_b(a). But a+tb and b remain independent, contradiction.

Consequently a nonzero zero triple is either linearly independent or all three projective lines coincide. If outer lines agree, cyclic zero gives f(x,y,x)=−2A_x(y), forcing y∈Cx. If the outer lines differ and y=αx+βz, then f(x,y,z)=αA_x(z)+βA_z(x), which cannot vanish for nonzero y.

Fix a middle u and split V=Cu⊕E. Let Q:Sym²E→J/im A_u be the residual map and K=ker Q. The restriction of f(-,u,-) to K lies in im A_u, so there is a unique v:K→E with f(a,u,b)=A_u(v(ab)). For independent a,b and ab∈K,

f(a+αu,u,b+βu)=A_u(v(ab)+βa+αb).

It vanishes exactly when v(ab)∈span(a,b), with a unique pair of coefficients α,β. No extra lift parameter occurs. If e²∈K and v(e²)∈Ce, then f(e,u,e)=−2A_e(u) makes A_e(u) proportional to A_u(e), contradicting the independence already proved. Hence v is square avoiding. Reconstruction is algebraic on independent-pair charts by solving an injective rank-two subbundle equation.

This lemma is universal. It does not impose a group representation, derive a global rank-drop dimension bound, or identify an actual source operation.

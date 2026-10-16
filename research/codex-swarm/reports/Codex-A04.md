> Worker proposal/review record. Acceptance and supersession are tracked in `../STATUS.md`.

Codex-A04 — conditional extraction rule; C07/C08/C11/C12 demand binding remains absent. Available reports supply proposed intervals, not authenticated coefficient requests.

**Original derivation: bounded exponential generating function.** Use the fixed partition of GitHub comment **6141322825**. On a standard chart with \(s\) infinity factors, write
\[
g_i=c_iv_i,\quad c_i=(-1)^{s-i}H_{s-i}(x_{\rm finite}),\quad
T=5(2N-1),\quad L=(s+1)(T-1)+1.
\]
For assigned carrier \(j\), define polynomial factors
\[
f_{i,n}=
\begin{cases}
c_j^nv_j^{n-T},&i=j,\ n\ge T,\\
g_i^n,&i\ne j.
\end{cases}
\]
Allowed indices are \(0\le n<T\) for \(i<j\), \(T\le n\le L\) for \(i=j\), and \(0\le n\le L\) for \(i>j\). Then the exact quotient is
\[
B_j=L![z^L]\prod_{i=0}^{s}
 \left(\sum_{n\ {\rm allowed}}\frac{f_{i,n}z^n}{n!}\right).
\]
Indeed, multiplying the exponential generating functions produces precisely the multinomial coefficient and the “smallest index reaching \(T\)” predicate. Every quotient exponent is nonnegative.

For polynomial coefficient extraction, initialize \(C_{-1}(0,0)=1\), with other entries zero. Processing factors in order gives
\[
C_i(\ell,\alpha)=
\sum_{\substack{n\le\ell\\n\ {\rm allowed}}}
\binom{\ell}{n}
\sum_{\beta}[x^\beta]f_{i,n}\,
C_{i-1}(\ell-n,\alpha-\beta).
\]
Thus \([x^\alpha]B_j=C_s(L,\alpha)\). Domain: characteristic zero; \(N\ge1\); \(0\le\ell\le L\); nonnegative polynomial exponent vectors. This is a symbolic identity, not an evaluated extraction or cost certificate.

**Frame and multiplicity rule.** Suppose an actual demanded scalar \(c\), in the common finite frame, has twist \(\mathcal O(w_1,\ldots,w_4)\). Require an authenticated factorization
\[
P=c\prod_o A_o^{p_o}
\]
as a global polynomial, with each homogeneous \(A_o\) of multidegree \(d_o\), and each corresponding weight divisible by \(A_{o,e_o}^{p_o}\). Put \(Q_o=\rho_o/A_{o,e_o}^{p_o}\). Then
\[
c\prod_o\rho_o
=P(x)\prod_oQ_o(x_{\rm finite},x_{\rm infinity}^{-1})
 \prod_i x_i^{-m_i},\qquad
m_i=\sum_{o:e_{o,i}=1}p_od_{o,i}.
\]
The numerator degree is \(D_i+w_i\), where \(D_i=\sum_op_od_{o,i}\). Do not append another twist multiplier. The target equation is
\[
a_i+\sum_{o:e_{o,i}=0}b_{o,i}
-\sum_{o:e_{o,i}=1}b_{o,i}-m_i=\kappa_i.
\]
Retain every owned occurrence, including deleted-prefix owners. Equal carriers do not identify owners or erase multiplicities (**6205341120**, **6205660472**).

Evidence: pin `08b73637d4136f91606aad332c46cafd064417f8`, `research/hm/current-scalar-geometric-dependencies/frames-and-poles.md`; public partition/reversal rules **6141322825**, **6142342077**. The generating-function proof above is new here; ownership, reversal and cancel-before-differentiate are published dependencies. No arithmetic tests ran.

Failure control: retain distinct inner N14 and outer54/legal29 weights; certify cancellation before differentiation (**6205249609**); prune recurrence states only with proved support bounds.

Reviewer: Codex-A03/Codex-V06; review pending. Next dependency: authenticated C07/C08/C11/C12 owner tuples, partition tags, frame/twist, target exponents and cancellation certificates. Without these, no recurrence instance, detector value, or completeness conclusion is justified.
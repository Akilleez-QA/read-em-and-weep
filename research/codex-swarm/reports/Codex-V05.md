> Worker proposal/review record. Acceptance and supersession are tracked in `../STATUS.md`.

Codex-V05 — support-certificate contract. Reviewer: Codex-V06, pending. Original contribution: the exact coefficient-weight and separation rules below; no obstruction value computed.

Sources: pin `08b73637d4136f91606aad332c46cafd064417f8`, `research/hm/current-scalar-geometric-dependencies/data/{source-formulas.js,model.json}` (both supplied blob IDs verified); `research/hm/current-scalar-residual-attribution/{ambient-second-jet.md,closure-and-characters.md}`; comments #6205127744, #6205249609, #6205341120, #6205455951, #6205660472.

**1. Exact coefficient functional.** Work over Q, in fixed authenticated local coordinates/frame, with full common-vertex owners retained. After normal ordering an owned linear demand as
\[
L(f)=\sum_{\beta,\kappa}\lambda_\kappa[x^\kappa]
                 (A_\beta(x)\partial^\beta f),
\]
its weight on the Laurent monomial \(x^e\), \(e\in\mathbb Z^4\), is exactly
\[
L(x^e)=\sum_{\beta,\kappa}\lambda_\kappa
 (e)_\beta[x^{\kappa-e+\beta}]A_\beta,\qquad
(e)_\beta=\prod_i\prod_{j=0}^{\beta_i-1}(e_i-j).
\]
Thus derivatives shift demand by **+β** in the multiplier coefficient; negative exponents use the same falling factorial. Matrix entries, orientations, terminal row coefficients and owner sums remain additional indices. Rational-series interchange requires finite demand sums or a proved formal topology.

For \(p=(a,b)\), #6205127744 fixes the four current multipliers:
\[
2E_p(s)=(V_as_{jk})L_b-(V_bs_{jk})L_a
       +(V_bs_{ij})U_a-(V_as_{ij})U_b,
\]
where \(L_d=A^{-1}V_dA\), \(U_d=A^{-1}B^{-1}(V_dB)A\).
Conversion to \(\partial^\beta\) must retain the coefficients of \(V\), frame conversion, and partition weights.

**2. Rational support/separation certificate.** After the required owned cancellations, write a scalar contribution
\[
G=N/\prod_jD_j^{m_j},\quad
D_j=c_jx^{d_j}(1+\sum_a u_{ja}x^{a}),\quad m_j>0.
\]
Require a common rational weight \(w_0\) with \(w_0\!\cdot a>0\) for every denominator increment. This specifies a locally finite formal expansion. Its inverse-factor coefficient for multiplicities \(n_a\ge0\) is
\[
c_j^{-m_j}(-1)^{|n|}
 \frac{(m_j)^{\overline{|n|}}}{\prod_a n_a!}
 \prod_a u_{ja}^{n_a},
\]
at exponent \(-m_jd_j+\sum_an_aa\).

Let \(B=\operatorname{supp}N-\sum_jm_jd_j\), and let \(\mathcal A\) contain all denominator increments. A sufficient exact zero certificate for demand κ is a rational vector \(w\) satisfying
\[
w\cdot a\ge0\ (\forall a\in\mathcal A),\qquad
w\cdot\kappa<\min_{b\in B}w\cdot b.
\]
Such a separator exists exactly when κ lies outside
\(\operatorname{conv}(B)+\operatorname{cone}(\mathcal A)\).
Failure to separate leaves UNKNOWN: convex support does not detect holes or coefficient cancellation.

**3. Failure control.** Cancel inserted-owner denominators before differentiation (#6205249609). Use
\(\partial(N/D)=((\partial N)D-N\partial D)/D^2\);
retain both terms and combine equal exponents. Common-multiplier cancellation requires an exact identity and regularity on the claimed domain. Different owners cannot be merged by carrier alone. Any outer multiplier requires its own convolution support.

Audit: no C-series reports were available at inspection. V01/V03/I01 agree with these prerequisites but supply no instantiated support certificate. No tests or source arithmetic ran.

Next: supply one unreserved, authenticated owned quotient/demand record for V06 review. The unpublished gaps 29/101/100, mask increments 57/58, seed4 and 704 reserved tuples remain unused. All 78 seeds still constitute one detector; these rules do not decide its complete pairing or prove boundary completeness.
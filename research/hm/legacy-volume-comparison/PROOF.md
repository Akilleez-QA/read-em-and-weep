# Identify the legacy stripped coefficient with natural root descent

## Result and scope

For the exact complete mixed source specified below, the legacy operation
“divide by \(y_1y_2y_3y_4\)” is **natural degree-sixteen deck descent**, once
its local matrix frames are interpreted correctly and its coefficient line is
converted to canonical forms. It contains no additional divisor four:

\[
  \mathcal L^\omega(M)
  =\frac1{16}\operatorname{Tr}_\rho^\omega(\Omega M)
  =D_\rho(M).
  \tag{1}
\]

Here \(\Omega=\bigwedge_{r=1}^4dx_r/y_r\), with the exact source normalization
proved in §2. The legacy generator returns the full mixed \(M\), not the
corrected trace-free source

\[
  R_{\rm raw}=\operatorname{tf}(M)+\delta W.
  \tag{2}
\]

Consequently, under the same complete-source class comparison as PR434,

\[
 [\operatorname{tf}\mathcal L^\omega(M)]
   =[D_\rho(R_{\rm raw})]=4j_4(C).
 \tag{3}
\]

Thus the trace-free legacy class is the naturally descended class, not its
quarter-normalized version. A representative of the naturally descended
corrected source includes the boundary \(D_\rho(\delta W)\); dividing that
representative by four gives the normalization used in PR434.

Equation (1) is an absolute statement in canonical-form coefficients under
the pinned source hypotheses. In ordinary \(\mathcal O(-2,-2,-2,-2)\)
coefficients, an absolute numerical identification with PR387 additionally
requires its binary-volume choice to be specified. We give the exact
coordinate-volume isomorphism and record the remaining scalar in §5.
Neither a literal equality with a separately chosen Čech representative nor
any high-collision-order claim is made.

## 1. Pinned source and what the legacy output means

All references and exact commits are in [SOURCES.md](SOURCES.md).
Let

\[
 T=C_{\rm ell}^{\,4}\xrightarrow{\rho}Z=(\mathbf P^1)^4
 \xrightarrow{p}X=\mathbf P^2\times\mathbf P^2
 \xrightarrow{m}Y=\mathbf P^4,\qquad q=mp,
\]

where \(C_{\rm ell}\) is the smooth completion of \(y^2=x^3-x\);
\(\deg\rho=16\) and \(\deg p=4\). Put
\(B=\operatorname{End}(\mathrm{HM})\), \(B_0=\operatorname{End}_0(\mathrm{HM})\).
The genuine root line cancels in these endomorphism coefficients.

Use the PR35 reduced generator at commit `6032b64d3f748c7ac37cb283db4a527e49d06ac8`,
with its mathematical source dictionary at
`08b73637d4136f91606aad332c46cafd064417f8`.
The latter's `closure-and-characters.md`, §2, identifies:

* `crossResidual` with the seven mixed kinetic terms;
* `globalCross` with those seven terms plus all three negative gerbe terms;
* the final left adjugate multiplication with the left-normalized full-sign
  source \(M=g_{ik}^{-1}D_{ijk}\), after removal of
  \(Y_{\rm odd}=y_1y_2y_3y_4\) and the stated pointwise frame normalization.

The final source line is \(C=GI\cdot\mathrm{globalCross}\).
There is no subsequent common factor \(1/4\), \(1/16\), or \(1/64\).
The factors already inside the mixed bidifferential and the scalar gerbe
remain part of \(D\); they are not descent normalizations.
The group-multilinear mask expansion expresses that same function and is not
a further cochain projection or a new representative.

This statement concerns the full-sign mixed component. The unprojected
ambient second-order defect also has unary and noncentral-gerbe terms;
the cited character/support argument, rather than omission by definition,
removes their full-sign components. No identification with an unspecified
alternative ambient is assumed.

The corrected source edition PR351, §7, uses the same ten-term \(D\), left
normalization, vector fields, unsymmetrized scalar \(s_{\rm raw,r}\), and
first lift \(U_r=g(s_{\rm raw,r}I+k_r)\). It proves (2) with

\[
 W=s_{\rm raw,q}k_p+s_{\rm raw,p}k_q,\qquad
 k_r=-\mu_r(g^{-1},g)/2.
 \tag{4}
\]

The two pairs are \(p=(1,2)\), \(q=(3,4)\) here. Its complementary-support
proof makes \(M\) closed. Its trace-free projection and (2) are therefore
closed as well. We use those structural source identities, not any
execution or selected-source value.

## 2. Fix the elliptic volume from the actual vector fields

The source fixes, without a free scalar,

\[
 V=y\partial_x+\frac{3x^2-1}{2}\partial_y,\qquad
 \pi_{12}=V_1\wedge V_2,\quad \pi_{34}=V_3\wedge V_4.
 \tag{5}
\]

The contraction convention is
\(\iota_{V_r\wedge V_s}=\iota_{V_s}\iota_{V_r}\).
PR131 fixes \(\Omega_{\rm pair}(\pi_{\rm pair})=1\).
Since \((dx/y)(V)=1\), it follows that

\[
 \Omega_{12}=\frac{dx_1}{y_1}\wedge\frac{dx_2}{y_2},
 \qquad
 \Omega_{34}=\frac{dx_3}{y_3}\wedge\frac{dx_4}{y_4},
 \qquad
 \Omega=\Omega_{12}\wedge\Omega_{34}.
 \tag{6}
\]

These are identities of the actual invariant forms, not a declaration that
equal-looking symbols have the same normalization. Each pair has
one-dimensional canonical fibers, and (5) is nowhere zero; evaluation on
that bivector determines its dual form uniquely.

For regularity, near a finite branch point the curve relation gives
\(dx/y=2\,dy/(3x^2-1)\), whose denominator is nonzero at each branch point.
At infinity put \(t=1/x\), \(u=y/x^2\). Then \(u^2=t-t^3\) and
\(dx/y=-dt/u\), regular and nonzero there. These formulas also verify
directly that (6) uses the same global vector fields as the source.
No ramification factor is inverted in defining the global forms.
Exchanging the two degree-two volume factors has sign \(+1\); no extra
mixed factorial arises.

## 3. The pointwise frame normalization is not a volume constant

The source dictionary, §4, specifies that `nu[0]=1` normalizes only the
zeroth jet at the point at which the jet is represented. Its nonzero
square-free derivative slots retain products of
\(\mathrm{mask}[r](x_r^2+1)/(2x_r(x_r^2-1))\).
It is not the substitution \(\nu\equiv1\) before differentiation.

PR351, §3, gives the physical row transitions

\[
 D_i=\operatorname{diag}(\nu_i,\nu_i^{-1}),\qquad
 g_{ij}=D_j(P_iI_j)^tD_i^{-1}.
 \tag{7}
\]

At any point of the dense common frame locus, let \(S_i\) denote the
constant matrix \(D_i\) at that point. A constant change at every endpoint
gives \(g'_{ij}=S_j^{-1}g_{ij}S_i\). All derivatives retain the derivatives
of \(g\), because \(S_i\) is constant for this jet calculation.
The complete defect transforms by
\(D'_{ijk}=S_k^{-1}D_{ijk}S_i\), so its left normalization gives

\[
 M'_{ijk}=S_i^{-1}M_{ijk}S_i.
 \tag{8}
\]

Thus the emitted array \(L_{ijk}\) represents
\(M'_{ijk}/Y_{\rm odd}\); the same intrinsic coefficient in physical row
coordinates is

\[
 \widehat L_{ijk}=D_iL_{ijk}D_i^{-1}
                 =M_{ijk}/Y_{\rm odd}.
 \tag{9}
\]

Equation (9) is an identity of rational sections on the dense comparison
locus. It does not instruct one to differentiate the right-hand side after
setting nonconstant frames to one. Deck changes multiply each \(D_i\) by a
scalar sign, so its conjugation is deck invariant. In a descended frame
one can instead use the emitted arrays directly with their corresponding
frame identification. The intrinsic section is what matters.

The public physical-frame proof checks the transpose/inclusion cancellation
\(S^t(SCS^{-1})^t(S^t)^{-1}=C^t\). It does not say that the two bare
two-by-two arrays are identical before conjugation. In particular this
pointwise diagonal normalization supplies no common scalar that could
silently convert natural deck descent to its quarter-normalization.

## 4. Division by the four y factors is canonical-form descent

Let \(\chi\) be the product of the four deck signs. The source character
proof gives the intrinsic full-sign \(M\) character \(\chi\).
The form \(\Omega\) has the same character. Hence \(\Omega M\) is invariant
under the degree-sixteen root deck group.

On the finite chart, (6) and (9) give the rational identity

\[
 \Omega M
   =\rho^*\!\left(\widehat L\,dx_1\wedge dx_2\wedge dx_3\wedge dx_4\right).
 \tag{10}
\]

Here the notation \(\widehat L\) means the intrinsic descended coefficient,
with (9) used if physical row coordinates are displayed.
Ordinary pullback of top forms has canonical trace
\(\operatorname{Tr}_\rho^\omega\rho^*=16\).
Applying its normalized trace to (10) proves (1).

The sheaf statement is regular, not a prescription to divide arbitrary
regular functions by a ramification equation. For a single curve cover,
the odd function summand on the finite chart is \(y\,\mathcal O\);
on the infinity chart its generator is \(u=y/x^2\).
Multiplication by \(dx/y\) sends these generators to \(dx\) and \(-dt\).
These are exactly the pullbacks of regular canonical frames.
Thus the odd summand is isomorphic to the downstairs canonical line.
Four external products, with the locally free endomorphism coefficient,
prove the regular sheaf isomorphism and (1) across every branch
intersection. Equivalently this is the degree-sixteen finite-duality
trace/Reynolds isomorphism proved in PR434.

There is an important cochain qualification. An entrywise finite trace is
literal only on full inverse-image opens, not arbitrary physical-chart
intersections. For this stated legacy cover that qualification can be
verified directly. Its one-factor legal opens are

\[
 C_{\rm ell}\setminus\{\infty\}
   =h^{-1}(\mathbf P^1\setminus\{\infty\}),\qquad
 C_{\rm ell}\setminus\{(0,0),(1,0),(-1,0)\}
   =h^{-1}(\mathbf P^1\setminus\{0,1,-1\}),
 \tag{11a}
\]

where \(h:C_{\rm ell}\to\mathbf P^1\) is the root cover. The carrier opens
are also pulled back from \(Y\). Hence their intersections with products of
these legal opens are exactly \(\rho^{-1}(V_i)\) for opens \(V_i\subset Z\).
The \(V_i\) are affine: carrier preimages are affine because \(q\) is
finite, the legal product opens are affine, and intersections of affine
opens in the separated variety \(Z\) are affine. The same holds for finite
intersections. Thus the source's stated carrier/line cover is already
adapted to \(\rho\); it need not first be replaced to take this trace.
The finite-chart expressions in nonregular reference frames are interpreted
as the intrinsic regular sections supplied by the physical-frame proof.

A further arbitrary non-deck-stable refinement would not retain this
entrywise interpretation. To compare with PR434's independently chosen
quotient cover, use a common regular affine refinement, finite pushforward,
affine acyclicity, and exact deck invariants as in PR434 §5. These identify
the cohomologies; representatives of the same class differ by boundaries
after comparison. No surjectivity of a cochain refinement map is assumed.

On the stated carrier/line cover the regular map \(D_\rho\) commutes with \(\delta\), with
frame transport, and with the rank-two trace-free projection. Consequently
(2) yields the cochain identity, for compatible representatives,

\[
 D_\rho(R_{\rm raw})
    =\operatorname{tf}\mathcal L^\omega(M)
       +\delta D_\rho(W).
 \tag{11}
\]

If \(M\) and \(R_{\rm raw}\) have already been transferred independently,
include their regular comparison boundaries in (11). The class identity
is independent of those choices. Applying PR434's exact identities
\([R_{\rm raw}]=j_{64}(C)\) and \(D_\rho j_{64}=4j_4\)
proves (3). This invocation retains all the complete-source, ambient,
boundary, equivariance, and localization hypotheses of PR134/426/434.
The raw array \(L\) itself also has a scalar endomorphism component; it is
not a \(B_0\)-valued candidate until trace removal is performed.

## 5. Exact binary-volume convention and the remaining scalar

The public geometric package fixes homogeneous coordinates \((X_r:Y_r)\),
with \(x_r=X_r/Y_r\) on \(Y_r=1\), and binary factors \(Y_r+X_rz\).
Define an explicit underlying-line isomorphism

\[
 a_{\rm std}:\mathcal O_Z(-2,-2,-2,-2)\longrightarrow\omega_Z
 \tag{12}
\]

by the ordered product of the binary forms
\(\alpha_r=Y_r\,dX_r-X_r\,dY_r\). More precisely, \(\alpha_r\) is the
homogeneous representative of a section of
\(\omega_{\mathbf P^1}(2)\); contracting it with the local
\(\mathcal O(-2)\) frame defines the isomorphism.
On the standard finite product frame \(e_{\rm fin}\),

\[
 a_{\rm std}(e_{\rm fin})=dx_1\wedge dx_2\wedge dx_3\wedge dx_4.
 \tag{13}
\]

If a subset \(S\) of coordinates is changed to \(t_r=Y_r/X_r=1/x_r\)
and \(\tau=\prod_{r\in S}t_r\), the corresponding line frame is
\(e_S=\tau^2e_{\rm fin}\). On that chart \(\alpha_r=-dt_r\) for
\(r\in S\), and \(\alpha_r=dx_r\) otherwise, in the original ordered
factor positions. Hence

\[
 a_{\rm std}(e_S)=(-1)^{|S|}\,dz_1\wedge dz_2\wedge dz_3\wedge dz_4,
 \quad z_r=t_r\ (r\in S),\quad z_r=x_r\ (r\notin S).
 \tag{14}
\]

This matches precisely the legacy internal-degree-zero coefficient
transition \(c_S=\tau^{-2}c_{\rm fin}\) proved in the physical-frame
package. In particular the minus signs on partial infinity charts must not
be suppressed. They reside in the canonical frame (14), not in an invented
source scalar. The internal-degree-minus-two HPL scalar in that package
has a different \(\mathcal O(-4)^4\) line and is not the present coefficient.

Let \(E=q^*B_0\otimes\mathcal O_Z(-2,-2,-2,-2)\), and extend \(a_{\rm std}\)
by the identity on \(q^*B_0\). In this expressly defined convention the
intrinsic trace-free legacy coefficient \(L^0\) satisfies

\[
 a_{\rm std}L^0=\operatorname{tf}\mathcal L^\omega(M),
 \qquad [L^0]=4j_{0,{\rm std}}(C),
 \quad j_{0,{\rm std}}=a_{\rm std}^{-1}j_4.
 \tag{15}
\]

PR387 §5 fixes an underlying canonical-line identification only by the
phrase “usual binary-coordinate volume convention” and explicitly allows
a fixed determinant-of-coordinate-space factor to be carried or fixed.
It states no numerical equation (13) for its \(a\).
Therefore the source readings do not prove that its chosen \(a\) is
literally \(a_{\rm std}\). If \(a\) is a fixed global isomorphism for the
same line, the ratio is a nonzero constant on connected projective \(Z\):

\[
 a=c\,a_{\rm std},\qquad c\in\mathbf C^\times.
 \tag{16}
\]

Its ordinary-coefficient inclusion is
\(j_0^a=a^{-1}j_4=c^{-1}j_{0,{\rm std}}\).
Accordingly the exact formulas in that convention are

\[
 [L^0]=4c\,j_0^a(C),\qquad
 [c^{-1}L^0]=[R_{\rm nat}^a],\qquad
 [(4c)^{-1}L^0]=[R_0^a].
 \tag{17}
\]

To make representative rather than class comparisons, add the correspondingly
transported \(D_\rho(W)\) boundary from (11) and any cover-comparison
boundary. If (13) is adopted for PR387's \(a\), then \(c=1\).
Otherwise (16) is the exact remaining normalization datum.
It is unrelated to the generator's pointwise matrix-frame normalization,
the rank-two trace subtraction, the degree-six constant inclusion, or
any later scalar residue prefactor.

## 6. Contribution and limitations

The coefficient-map question has a concrete answer: the restored legacy
division operation is \(D_\rho\), not \(D_\rho/4\), in canonical-form
coefficients. The trace-free legacy class equals the natural descended
complete class; the corrected source representative differs by the
explicit descended boundary dictated by (4). The binary-volume ambiguity
is isolated to the single missing equation (13) for the previously chosen
ordinary-line identification, not concealed in a claimed equality of
notations.

No individual coefficient, carrier tuple, mask value, detector, or
obstruction value was evaluated. No generator, model, checker, or
parameter search was run. No high-ideal representative, weighted
primitive, module lift, new vanishing, or later scalar-extraction identity
is deduced. In particular a historical supplier's high-order assertion
cannot be transferred to this class without a separate representative
and class comparison. This note resolves the normalization of the
specified legacy map, not every output historically called \(R_0\).

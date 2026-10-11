# Arithmetic review of the τ=1 central matrices

Pinned head: `fcfa65a24455e6c5aff3b8d42ec1f75c2b374735`.

This note rebuilds the two stated central-compatibility matrices from presentation (A) in `central-criterion.md` and reads both focused proofs. It does not import the package checkers. It makes no carrier-classification claim. The quotient-image direction is outside the theorem, as that note already says.

## Reproduce

From the repository root:

```sh
python3 research/hsd-review/53/run_review.py
```

The script uses Python `int` and `fractions.Fraction` only. It exits nonzero unless every asserted identity holds. A passing run writes `transcript.txt` beside the script.

## Matrix definition

Presentation (A), on \(X=\mathbb{P}^1\times\mathbb{P}^3\):

\[
\begin{CD}
\mathcal{O}(-12,2)\oplus\mathcal{O}(-8,1)
@>{\begin{pmatrix}\ell&h^2\\0&a\end{pmatrix}}>>
\mathcal{O}(-8,3)\oplus\mathcal{O}(-7,1).
\end{CD}
\]

The finite-chart coordinate is \(u=t/s\). A class in \(H^1(\mathcal{O}(b,d))\) is \(u^e\) times a degree-\(d\) monomial in \(x_0,x_1,x_2,x_3\), with \(e\) running from \(b+1\) through \(-1\). Monomials are ordered with the exponent of \(x_0\) slowest. Source block order is \((-12,2)\) then \((-8,1)\). Target block order is \((-8,3)\) then \((-7,1)\). Output exponents outside the target range are Čech coboundaries and are omitted.

The stated specializations are

\[
\ell=s^4 x_0+s^3 t x_1+s t^3 x_2+t^4 x_3,\qquad a=t,
\]

with \(h=x_1\) and, separately, \(h=2x_0+3x_1+5x_2+7x_3\). In the finite chart, \(\ell=x_0+u x_1+u^3 x_2+u^4 x_3\) and \(a=u\).

The torsion kernel vector is the class of \((-h^2/a,\ell/a)\) reduced to negative Laurent degree. For this \(\ell\), that class is \((-u^{-1}h^2,\,u^{-1}x_0)\). It is the image of the relation \(a(0,\ell)=P(-h^2,\ell)\) from §3.

## Reproduced

- Both matrices are \(164\times 138\). For each stated \(h\), the torsion vector is nonzero and lies in the kernel, and a \(137\times 137\) minor is a nonzero integer. Rank over \(\mathbb{Q}\) is exactly 137.
- Basis counts \(11\cdot 10+7\cdot 4=138\) and \(7\cdot 20+6\cdot 4=164\).
- \(\operatorname{Sym}^3 U(-7)\) has degrees \(-1,-2,-2,-3,-3,-3,-4,-4,-4,-4\), so \(h^1(\mathcal{O}_Y(-7,3))=20\). The doubled line contributes 7 and the radical line would contribute 4, giving 27 against 24.
- Presentation identities: \(P(-h^2,\ell)=(0,a\ell)\); the column \((s,hk)\) produces \((\ell s+h^2 k,ak)\); clearing \(a\) shows that \((0,\ell)\) is a symmetric splitting change on \(a\neq 0\).
- Half correction \(d(QV+LB(V))=f_j-f_i\), and the corrected cocycle changes by \(L\) times a symmetric matrix under the stated first-stage gauge.
- \(g(V,S)^\top\Omega g=\Omega\), and \(\beta\Omega^{-1}\beta^\top=RL^\top-LR^\top-QJQ^\top\).
- On the chart \(a=1\), the ideal of \(2\times 2\) minors is \((\ell,q_1,q_2,\rho)\).
- The stated \(\ell\) has syzygy columns \((t,-s,0,0)\), \((0,t^2,-s^2,0)\), \((0,0,t,-s)\). With the sign \((-1)^i\) on the deleted row, the maximal minors are the negatives of the four coefficients, so they generate the same ideal. The coefficient vector is nonzero at \((s:t)=(1:0)\) and at \((0:1)\).
- The binary identity \(W_Y=Z\Delta\), \(W_Z=-Y\Delta\), with middle coefficient \(2(Ac-Ca)\).
- The stated \(r=0\) isotropy substitution. Its discrepancy is exactly \(XW+tH_1-(F_1G_2-F_2G_1)\), which is the primary divisibility hypothesis of that substitution.

## Defect

None in the identities above.

The prose says the maximal minors are equal to the coefficients. The signed minors are the negatives. That is a global sign in the deletion convention. It does not change the ideal or the splitting type \(U\simeq\mathcal{O}(2)\oplus\mathcal{O}(1)^2\).

## Missing hypothesis

None beyond inputs the notes already mark as inputs.

Those stated inputs are: algebraically closed of characteristic zero; the bidegrees and \(J\); \(a\) has one simple zero; the coefficients of \(\ell\) have no common base zero; \(\ell_0\) and \(h\) are independent; the actual primitive presentation \(0\to\mathcal{O}(-4)\to\mathcal{O}^4\to U\to 0\) with the projective-bundle convention \(p_*\mathcal{O}_Y(0,1)=U\); \(W=\mathcal{O}^2\); local data \(Q_j=Q_i+LV^\top J\) with symmetric \(S\); and, for the second note only, \(0\neq h_0\in\mathcal{O}(2)_0\). The normal-form reduction from a general charge-three family is an input, not a theorem of the package.

The sentence that restriction to the exceptional line imposes three independent conditions on \(\operatorname{Sym}^2 U(-1)\) is not derived in `central-criterion.md`. It is not used for the gluing criterion or for rank 137.

## Hypotheses as stated or justified

Stated, and used as inputs: the list in the previous section.

Justified in `central-criterion.md` from those inputs:

- Koszul shape of the syzygies of \((a,-\ell,-h)\), using that \((a,\ell,h)\) is regular because \(\Lambda\) is a line. Chartwise vanishing of \(H^{>0}(M)\) because every bundle in the resolution has nonnegative relative degree.
- Exactness of (A): \(h\) is a nonzerodivisor modulo \(a\), \((a,h^2)\) is regular on \(Y\), and \((a,\ell)\) is regular. Injectivity because \(\det P=a\ell\).
- The doubled line \(D=V(a,h^2)\) is not the radical line. The torsion summand is \(i_*\mathcal{O}_{\mathbb{P}^3}\), with \(h^0=1\) and no higher cohomology. Thus \(h^0(N)=1\) and \(h^1(N)=27\).
- Two-chart Čech cohomology computes \(H^1(N)\). Vanishing of the corrected class is necessary and sufficient for a central gluing. The class is unchanged by first-stage lifts.
- The residue on \(V_Y(q_1,q_2)\) is regular, including on the exceptional fiber. The torsion generator has zero image in that residue.
- After localizing at \(a\), ordinary rank is the condition that \(\rho\) be a unit on the length-four scheme \(V(q_+,q_-)\). Exceptional rank is saturation by the full irrelevant ideal of \(\mathbb{P}^3\).

Justified in `maximal-direction.md` from the same inputs plus \(h_0\in\mathcal{O}(2)_0\):

- The maximal summand is unique because \(\operatorname{Hom}(\mathcal{O}(2),\mathcal{O}(1))=0\). The subscroll is the quotient, not a chosen complement. The finite-chart shape \(h_Y=-X+tk\) follows from the degrees \((2,1,1)\) and from \(h_0\) being pure of maximal degree.
- The extension splits on each affine base chart. The normalized Čech windows are \(t^{-1},\ldots,t^{-5}\) and \(t^{-1},\ldots,t^{-4}\).
- Twisting the actual presentation by \(\mathcal{O}(-1)\) makes \(\delta:H^0(U(-1))\to H^1(\mathcal{O}(-5))\) an isomorphism. In the basis \((X,tX,Y,Z)\) the columns are \((d_1,\ldots,d_4)\), \((d_2,\ldots,d_5)\), \((y_1,\ldots,y_4)\), \((z_1,\ldots,z_4)\).
- The projected image of \(I_{(t,h_Y^2)}\) is \(t\mathcal{O}_\Sigma(-7,3)\). The retained Laurent window is \(t^{-3},t^{-2},t^{-1},t^0\). Exponent \(-4\) is an infinity boundary. From the displayed overlap formula, those four coefficients are \(M(B_1,B_2,W_Y,W_Z)^\top\).
- Invertibility of \(M\) forces the three binary minors to vanish in characteristic zero, hence the two quadrics are proportional. A constant section of \(\Sigma\) then lies in \(V(q_1,q_2)\), and the pulled-back residue is a section of \(\mathcal{O}_{\mathbb{P}^1}(-4)\), so it is zero. On \(t\neq 0\) the minor ideal is \((q_1,q_2,\rho)\), so those ordinary points are rank failures.

The overlap formula \(T|_\Sigma\) in §4 of the second note is a direct calculation. This review did not expand it from the monad matrices. The Laurent matrix \(M\) was read off from that displayed formula. The sample connecting determinant 1282 was not recomputed. Neither omission is an input to the \(164\times 138\) rank.

## Scope

Rank 137 is the rank of these two rational specializations of \(H^1(P)\). The sheaf argument for every \(\ell\) and \(h\) in the stated family is the cohomology sequence in §5, which this arithmetic check corroborates and does not replace. No statement is made about a globally surjective monad, a carrier, stability, or mixed Atiyah vanishing.

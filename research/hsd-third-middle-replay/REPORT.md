# Third-middle raw-equation replay

## Scope

This replay checks the 40 third-middle raw equations of order \(h^3\) for the proposed third cochain at commit `fa685b9dd33e1c8a4336f6a8086c56f3ceb3bc3b`. The transitions retain the form \(\exp(-h A_\eta - h^2 A_\kappa - h^3 A_\nu)\, g\), with the order-zero completion, form, line \(P\) and pairing held fixed. Arithmetic is exact over \(\mathbb{Q}\). The replay stops at these 40 equations: it builds no new gauge, treats no order-four equation, and asserts no carrier and no formal existence.

## Pins

The following digests were checked before the corresponding bytes were used.

| Object | SHA-256 | Bytes |
| --- | --- | --- |
| First jet \(\eta\) | `2be28aebeb2ff40754f17ca94f76b68eb40043f6492a1794bd91436bc27e1f10` | 12297 |
| Second-middle \(\kappa\) | `c03a36fca19b7a73b8c483c7dc9e2a17f4a1ea422e9a61972966b734cd5597e4` | 152410 |
| Third cochain | `011ba80d06f7b47a077845f377e9b22a5a9e51d808804e88e2ba4bf66c2306cd` | 23833465 |

The \(\kappa\) bytes are the certificate carried at commit `22b800836385cf4c869c200bfc6715e07613aad6`. The complementary mixed lambda input is the closed tensor \(z^{-1} E_0^2\) on each mixed vertex, with empty finite and infinity parts. Frame slot \((1,1)\) is \(E_0^2\), as fixed by the first-jet legend \(c = z^{-2} X E_0^2\).

## Method

`replay.py` rebuilds every cubic right-hand side from \(\eta\) and \(\kappa\) before it opens the third cochain. On a plane chart,

\[
\delta\nu = \tfrac12\bigl([\eta_{01},\kappa_{12}] + [\kappa_{01},\eta_{12}]\bigr) - \tfrac1{12} N(\eta_{01},\eta_{12}),
\]

where \(N(u,v) = [u,[u,v]] + [v,[v,u]]\) and \([\,{,}\,]\) is the tensor Poisson bracket. On a mixed edge,

\[
T\nu_I - \nu_F - \delta\nu_H
  = \tfrac12\bigl([h_i,K_I] + [k_i,I] - [F,k_j] - [K_F,h_j]\bigr)
    + \tfrac1{12}\bigl(N(h_j,F) - N(I,h_i)\bigr),
\]

with \(I\) and \(K_I\) transported from the infinity chart. Each defect is reduced modulo the line relation: the linear cofactor is fixed by the \(XY\) row, and every slot must match. Grading checks plane degree, secondary character, plane poles and base regularity on every exported \(W\) term.

The rebuilt right-hand sides contain 4081 finite monomials, 2985 infinity monomials and 25966 mixed monomials.

## Results

All 40 equations pass. Each equation has six components, and every component passes: finite, infinity, mixed edges \(01\), \(02\) and \(12\), and grading/regularity. The graded \(W\) terms number 13547.

Passing parameters: `1`, `a`, `b`, `c`, `d`, `a*a`, `a*b`, `a*c`, `a*d`, `b*b`, `b*c`, `b*d`, `c*c`, `c*d`, `d*d`, `a*a*a`, `a*a*b`, `a*a*c`, `a*a*d`, `a*b*b`, `a*b*c`, `a*b*d`, `a*c*c`, `a*c*d`, `a*d*d`, `b*b*b`, `b*b*c`, `b*b*d`, `b*c*c`, `b*c*d`, `b*d*d`, `c*c*c`, `c*c*d`, `c*d*d`, `d*d*d`, `lambda`, `a*lambda`, `b*lambda`, `c*lambda`, `d*lambda`.

`RECEIPT.json` records the pass/fail row for each equation.

The five previously supplied lambda-slice coefficients were compared separately. `lambda`, `a*lambda`, `b*lambda`, `c*lambda` and `d*lambda` each match the supplied lambda-order-three primitive. That comparison is 5/5 pass. Those supplied primitives are read and compared; they are not recomputed.

In this gauge the exported \(W\)-valued third primitive has the stated support: the 28 listed monomials are nonzero and the 12 listed monomials are zero. Support pass.

## Controls

1. Known-sensitive control, pass. Adding \(X^{-1} Y^{-1} W E_0^2\) to the origin finite edge \((0,1)\) makes the finite triple-overlap \((0,1,2)\) quotient remainder exactly that monomial. The unmutated origin equation passes.

2. Wrong-sign BCH control, pass. With the published signs fixed, the finite nested summand \(-\frac1{12} N\) at parameter `1` has a nonzero relation remainder of 406 monomials. Ten parameters have a nonzero remainder for this summand; the control uses label `1`. Replacing \(-\frac1{12}\) by \(+\frac1{12}\) makes that finite raw equation fail, and its quotient remainder equals twice the identified remainder. \(\eta\) and \(\kappa\) were left unchanged.

## Dependencies

Shared with the published verifiers:

- the literal first jet \(\eta\)
- the literal second-middle primitives \(\kappa\), including the mixed term \(z^{-1} E_0^2\)
- the plane geometry: coordinates \((z,X,Y,W)\), frame, bivector, line relation, transport and the three-chart Čech cover

Independent in this replay:

- the polynomial and symmetric-tensor arithmetic
- the cubic BCH assembly, run before the third cochain is read
- the relation quotient, grading and regularity checks
- both controls

`replay.py` does not import the generator, the contraction or the published checkers. Primitive equality was not required and was not tested.

## Reproduce

From the repository root, with the Python standard library only:

```sh
python3 research/hsd-third-middle-replay/replay.py
python3 -m unittest discover -s research/hsd-third-middle-replay -v
```

# Physical frames and completed-scalar pole bounds

## 1. Homogeneous primitive denominators

Set `F_j=v_j^4-product_(k!=j) v_k`, so `h_j=v_j F_j`. The primary divisor
channels are the two factors `(v_j,F_j)`, owned by carrier `j`; the auxiliary
channels are `(v0,v1,v3,v4)`, owned by `*`. Factors with the same polynomial
value but different carrier owners are not identified in the bound graph.

The affine primitive entries are numerator/denominator pairs `p/d` in
`v1,...,v4`, with assigned homogeneous degree `w`. Put

\[
D=\deg d,\qquad e=\max(0,\deg p-D-w).
\]

Their homogeneous expression is
`hom_(D+e+w)(p)/(v0^e hom_D(d))`. The weights are `+1` for `gamma,delta,ev`,
`-1` for `H0,H1,eta`, `0,1` for the two columns of `I`, and `0,-1` for the
two rows of `P`; `W,L` have weight zero. These degrees are part of the
specified bundle model, and the checker performs the actual homogenization.

For every nonzero `I,P,H0,H1` entry, the seed checker multiplies this homogeneous
rational expression by its supplied product of owned divisor factors, cancels
exactly, and verifies that the result is a polynomial over Q. There are 451
such checks. All remaining zero entries have null seeds. The auxiliary seed
can require `v0^2`; the checker does not silently invert `v0` on another chart.
The elementary `eta,W,L` entries are defined explicitly from a pivot:
`eta` has entries `1/v_pivot`, and each nonconstant `W` entry is a coordinate
ratio with the same denominator. Their bounds follow directly.

For a square-free derivative of order `d`, a positive denominator exponent
`e` can increase to `e+d`; an absent factor stays absent. This follows by
iterating the quotient rule in the local coordinate ring. Polynomial entries
remain polynomial. The graph includes order-zero, order-one, and distinct
order-two derivatives, including conservative nonzero derivative bounds
when the finite chart's specialized expression happens to be constant.

## 2. Why these are the same expressions at infinity

Choose an infinity-coordinate subset `S`, put `t_i=1/x_i`, and let
`tau=product_(i in S) t_i`. The local homogeneous coefficient vector satisfies
`v_local=tau v_affine`; the chart checker verifies this coefficientwise on all
16 charts. The physical line frame satisfies `nu_B=tau^(1/2) nu_A`.

Every physical splitting block has a homogeneous degree `d` and a power `p`
of the line frame with `2d+p=0`:

- `U0`: `gamma (1,-2)`, first `I` column `(0,0)`, second `I` column `(1,-2)`,
  `H1 W (-1,2)`
- `U1`: `W (0,0)`, `eta (-1,2)`
- `Q0`: `H0 (-1,2)`, first `P` row `(0,0)`, second `P` row `(-1,2)`,
  `L delta (1,-2)`
- `Q1`: `L (0,0)`, `ev (1,-2)`

Therefore each physical block is multiplied by `tau^(d+p/2)=1`: the physical
splitting matrices agree as rational matrices **before differentiation**.
The homogenized primitive identities and the source's displayed `U/Q`
construction give this conclusion. A list of assigned exponent sums alone
would not establish agreement with an arbitrary program.

Retain the same legal frames and transport the same old connections. On an
infinity factor set `s=1-t^2`; the squared normalized line ratios are `t` and
`s`, with logarithmic derivatives `1/(2t)` and `-t/s`. The finite connection
`dx/[x(x^2-1)]` becomes `-t dt/s`, while `dlog x` becomes `-dt/t`.
The invariant vector field is `-z partial_t`, where `y=z/t^2`. Its sign and
the sign of transported `dlog x` must both be included.

In the mixed full-sign residual, coordinate groups `(1,2)` and `(3,4)` each
occur once. The first corrections contain one occurrence of each coordinate
in their pair; their products, first-derivative cross terms, and mixed second
derivative terms consequently use every one of the four coordinates exactly
once. All mixed second derivatives use distinct coordinates. Thus there is
no missing same-coordinate second derivative of a coordinate change. Taking
the common-frame normalized residual and its transpose preserves this exact
covariance, rather than replacing it by a cohomologous expression.

Physical inclusion and projection have opposite factors `tau^(1/2)` and
`tau^(-1/2)` in internal degree zero, which cancel. Each undifferentiated HPL
homotopy contributes `tau^-1`. Removing the common full-sign product of the
four invariant `y` factors contributes `tau^-2`. Consequently an internal
degree `r` coefficient transforms as

\[
c_S=\tau^{r-2}c(x_i=1/t_i\text{ for }i\in S).
\]

The scalar has `r=-2`, giving `tau^-4` and the common line bundle
`F=O(-4,-4,-4,-4)`. The scalar bound graph is interpreted in these transformed
local frames, using the homogenized seeds above. It is not an affine bound
with an unsupported Laurent multiplier appended afterwards.

The 901 transported-frame identities check these elementary seed transforms
and exponent cancellations. The reasoning above, the homogeneous primitive
checks, and the source-formula tie supply the implication to the actual
expression. This is not a claim that 901 full nonlinear chart expressions
were separately expanded or replayed.


# Closure, full-sign source, and choice independence

## 1. Closure before coefficient extraction

The ambient second jet satisfies both descent identities, and the explicit
first lift solves its full order-one module equation. Associating the
three semilinear module maps on a quadruple overlap in the two ways, and
taking the first unsolved coefficient, gives
\[
R_{ikl}+g_{kl}R_{ijk}-R_{ijl}-R_{jkl}g_{ij}=0.
\]
Terms involving a lower defect vanish because order one was solved;
the ambient associator terms cancel by the two descent identities.
Multiplication by `gil^-1` identifies this with minus the ordinary row-End
Čech differential of `C2=gik^-1R`. Thus `δC2=0` before evaluating at any
point, extracting a coefficient, applying a Laurent cutoff, or projecting
to a finite complex.

The second-order obstruction of the declared first lift is therefore
`[C2] in H²(X,End E)=Ext²(E,E)`. The exact formula for its full-sign
component is the source used by the scalar calculation.

## 2. Why the mixed formula is exactly the full-sign component

The deck group is `(Z/2)^4`, acting by independent `y_i -> -y_i`.
The bundle's End complex has its natural pullback deck linearization;
characters below are intrinsic, after transporting to a common frame.
`q_i` and `V_i` have character `chi_i`, while `a_i` is invariant.
Accordingly `b12,pi12,u12` have character `chi12`, and the `(3,4)`
terms have character `chi34`. This applies to the actual source choice:
a deck element sends each local `nu_i` to `epsilon_i nu_i`, with
`epsilon_i` equal to `+1` or `-1`. All split `U/Q` column powers of `nu`
are even, and the physical E basis `I diag(nu_i,nu_i^-1)` changes by the
scalar `epsilon_i`. These scalar frame signs cancel in normalized End
cochains transported to a common frame. The old connection is deck
invariant. Contracting the exact transgression or the logarithmic matrix
derivatives with `pi12` or `pi34` therefore gives exactly the corresponding
pair character for this first lift, not merely for a hypothetical averaged
replacement. Arbitrary unnormalized transition entries need not be invariant.

`T` has character zero. Also
`pi12(db34,dg)=pi34(db12,dg)=0`, since the indicated coordinate sets are
disjoint. Thus the normalized `T(g)g` and `μ1(b,g)` terms have no
full-sign (`chi1234`) component. They are still required in the complete
unprojected closure proof.

Write `A=u12`, `B=u34`, `b=b12+b34`. The surviving unnormalized terms are
\[
\begin{aligned}
R_{1234}={}&A_{jk}B_{ij}+B_{jk}A_{ij}\\
&+\mu_{1,12}(B_{jk},g_{ij})+\mu_{1,34}(A_{jk},g_{ij})\\
&+\mu_{1,12}(g_{jk},B_{ij})+\mu_{1,34}(g_{jk},A_{ij})\\
&+\mu_{2,1234}(g_{jk},g_{ij})
-b_{12}B_{ik}-b_{34}A_{ik}-b_{12}b_{34}g_{ik},
\end{aligned}
\]
where
\[
\mu_{2,1234}(f,g)=\tfrac14[(V_1V_3f)(V_2V_4g)
 -(V_1V_4f)(V_2V_3g)
 -(V_2V_3f)(V_1V_4g)
 +(V_2V_4f)(V_1V_3g)].
\]
The coefficient is `1/4`, not `1/8`: both orders of the two disjoint
bivector factors occur in the Moyal square. Similarly the mixed part of
`-(1/2)b²g` is `-b12 b34 g`.

`crossResidual` in PR #35 implements the first seven displayed terms;
`globalCross` adds the last three gerbe terms, using `bcoef=15q_a q_b/4`.
The complete-generator tail multiplies by the left adjugate inverse of
`g[0][2]`. This gives precisely `C2_1234`, after division by the common
`y1 y2 y3 y4` factor and the stated constant frame normalization. The exact
source check verifies that final normalization line too, rather than only
the two residual functions. The source's group-multilinear mask extraction
does not change the cochain; it expresses this same function in its finite
mask basis.

Character projection commutes with the Čech differential over characteristic
zero. Consequently this unsigned normalized mixed source is itself closed.

## 3. Passage to the original scalar

Column-coordinate contractions receive `C2_row^t`. Form the nonlinear row
defect first and transpose afterward; transposition reverses products.
For `e=IP`, the induced End contraction is
\[
j(f)=IfP,\qquad h(F)=HF+(-1)^{|F|}eFH,
\quad [d,-]h+h[d,-]=1-jp_{End}.
\]
In Čech degree `q` set `D0=(-1)^q[d,-]`, `h0=(-1)^q h`.
Perturbation by `δ` gives the finite chain inclusion
\[
J=(1+h_0\delta)^{-1}j.
\]
The sum is finite because each term lowers internal degree; the transferred
differential on End E is its ordinary Čech differential, since End E has
only internal degree zero. Therefore `DJ(C2^t)=0`, including its top
Čech-degree-five component. This is a chain-map proof, not a top-face
regression extrapolated to a theorem.

With the declared total differential the components obey
`J1=h δJ0`, `J2=-h δJ1`, `J3=h δJ2`. Hence the scalar's one `J2` minus
is geometric. The auxiliary-first contraction, carrier merger, scalar map,
physical frame transport, and completed scalar pole bounds are provided by
PR #34 and the geometric package. Combining those results with the closed
source here fulfills their ambient-source hypothesis for this particular
second jet. This does not assert that every denominator-cleared cochain has
an arbitrary finite cutoff comparison; only the stated scalar comparison
with its checked regularity domain is used.

## 4. The exact Ext¹ character dependency

Choice independence needs more than formal character counting. The actual
finite-model implementation is pinned in
[PR #34](https://github.com/Akilleez-QA/read-em-and-weep/blob/a100f4e0be453d6e182320b792359f8a04e32b4d/research/hm/current-scalar-proof/finite-model/pinned-verify-hm-ext.js),
SHA-256 `1fe4608ed77f3767691e7ef4de375fc55b052ccf26159a4aae3ec6d35fe96414`.
This package executes it afresh and checks the classical `gamma,delta,ev`
coefficients against the geometric model, so a rank table for a different
complex is not silently substituted.

For a character subset `S`, the deck eigensheaf on `(P1)^4` twists by `-2`
in each factor of `S`. Thus an internal-degree-`r` End summand has factor
degree `r-2*1_(i in S)`. The source's parameter `weight` is `|S|`, with
representative `S={1,...,weight}`. It constructs the finite transferred
differential using the line-bundle Čech contractions in that eigensheaf,
checks exact integer kernels, and computes rational ranks, using BigInt
elimination for nonunit tails. The finite-model construction and its
comparison are the existing mathematical dependency, not newly reconstructed
by the rank wrapper here.

The fresh ranks are:

- initial `d1`: `(50,150,450,1250,2550)`;
- weight-two length-three rank: `100`;
- remaining maps: `(3598,522,90,30,10)`;
- trivial-character boundary rank: `353`;
- per-character `dim Ext¹_S`: `(79,2,0,0,0)` for weights 0 through 4.

These are per-character dimensions, not aggregate dimensions by weight.
Permuting the four curve factors permutes character subsets and preserves
the elementary-symmetric coefficient map defining the complex. Signed
tensor-factor permutation therefore gives chain isomorphisms for subsets
of equal size; the chosen ordered contraction need not itself be symmetric.
The multiplicities are `(1,4,6,4,1)`, giving total Ext¹ dimension `87`.
In particular `Ext¹_S=0` for `|S|>=2` over characteristic zero.

## 5. What choices can and cannot change

For the fixed first-order ambient class, a different first-order object
lift differs, modulo first-order gauge, by Ext¹. The preceding actual ranks
allow a representative with only weights zero and one. Its quadratic term
has weight at most two. Its bilinear terms with either the baseline
weight-two first lift or the weight-two ambient class have weight at most
three. They cannot change the full-sign second-order obstruction class.
For completeness, an exact first-order difference is harmless for a direct
reason. A local change `H_i=1+h z_i` sends the transitions to
`Fij(H_j^-1) star Gij star H_i`. The first-order correction changes by
`-gij (delta z)_ij`, where `(delta z)_ij=gij^-1 z_j gij-z_i`.
The full module defect transforms covariantly under this change. Retaining
the induced order-two correction preserves its normalized obstruction;
discarding that correction changes `C2` by its ordinary End Čech boundary.
Thus the character bound is needed only for Ext¹ classes, not for every
possible cochain representative of an exact difference.

After first-order identification, two valid ambient second jets differ by
a total Hochschild two-cocycle. Their module obstructions differ by its
characteristic evaluation. Here
\[
HH^2(X)=H^0(\Lambda^2T_X)\oplus H^1(T_X)\oplus H^2(\mathcal O_X)
\]
has only weights zero and two: each `V_i` and each factor's `H¹(O)`
has weight `chi_i`. The evaluation is equivariant for the natural deck
linearization of E. It therefore cannot change the full-sign class.

The qualification “after first-order identification” is essential. This
argument does not construct an equivalence between the entire current
algebroid and a different central/harmonic presentation, nor does it prove
that two unspecified first-order presentations agree. It proves independence
of the full-sign class within the explicitly identified first-order
deformation problem. It proves neither equality of all weight components
nor vanishing of the full Ext² obstruction.

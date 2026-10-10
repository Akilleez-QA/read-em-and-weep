# Structural relations and the detection boundary

## 1. The finite complex and current scalar vector

Use the full-sign harmonic finite-model basis
`hm-pr5-full-sign-harmonic-v1`. In total degrees 1, 2, 3 its dimensions
are 2560, 6560, 4080. Write a degree-two element as `(n,p)`, with
negative block `n` of length 6480 and positive block `p` of length 80.
The differentials have form

\[
D_1x=(Ax,Tx),\qquad D_2(n,p)=(Bn,Un+Cp).
\]

Here `T` and `U` include the length-five transferred differential. Ignoring
them would change the cohomology problem. The current scalar vector is

\[
c[k]=n[k]-n[5670+k],\qquad 0\le k\le80.
\]

The coefficient index is
`k=27(e_1+3)+9(e_2+3)+3(e_3+3)+(e_4+3)` for `e_i in {-3,-2,-1}`.
The selected matrix slots are 0 minus 70. Each scalar coordinate kills
incoming boundaries over the integers.

## 2. Forty-seven integral relations

The following 35 coordinates vanish on every cycle:

```text
0,1,3,4,9,10,12,13,26,27,28,30,31,36,37,39,40,41,
43,44,49,50,52,53,62,67,68,70,71,74,76,77,78,79,80.
```

The twelve remaining independent relations have all coefficients `+1`:

```text
c[17] + c[35] = 0
c[14] + c[32] + c[38] = 0
c[16] + c[34] + c[42] = 0
c[23] + c[47] = 0
c[22] + c[46] + c[48] = 0
c[25] + c[51] = 0
c[2] + c[6] + c[18] + c[54] = 0
c[59] + c[65] = 0
c[58] + c[64] + c[66] = 0
c[61] + c[69] = 0
c[8] + c[20] + c[24] + c[56] + c[60] + c[72] = 0
c[73] + c[75] = 0
```

For each relation with coefficients `a_k`, the compact certificate supplies
an explicit integer row vector `w` with

\[
\sum_k a_k(e_k^t-e_{5670+k}^t)=wB. \tag{1}
\]

All 221 witness terms involve original uneliminated pure-negative rows;
no positive-block cancellation is hidden in (1). The checker rebuilds
`B` from the pinned finite-model code, compares its complete outgoing
matrix hash, and checks every equality over the integers. It also checks
an explicit 47-by-47 identity minor in the scalar relation matrix.
Hence the relations have rank 47 over every field and hold over every
field, without a characteristic-stability assumption.

The exact rational outgoing rank is 3648, and the exact augmented rank
of `[D_2; L]` is 3682, where `L` denotes the 81-row scalar matrix. Thus

\[
\operatorname{rank}_{\mathbf Q}(L|_{\ker D_2})=3682-3648=34.
\]

The 47 equations therefore characterize the complete possible scalar
image over `Q`. The checker separately obtains rank 34 over `F_13`,
including both higher and positive blocks; they also characterize the
image in that field. Their validity in every field alone does not assert
image dimension 34 in every characteristic.

The 35 single-coordinate equations provide theorem-derived zeros for the
actual rational scalar once its source is identified with this closed
finite-model class. They are not numerical evaluations of omitted source
windows. Satisfying all 47 relations is a consistency condition, not proof
of source identification or correctness of coefficient extraction.

## 3. All constant scalar maps

Write a constant functional on internal degree `-2` as

\[
\ell(X)=\sum_{a,j}\alpha_{a,j}X_{02}[a,j]
       +\sum_{i,b}\beta_{i,b}X_{13}[i,b].
\]

Let `gamma[i,a]=sum_k gamma[i,a,k]v_k` and
`ev[b,5b+k]=v_k`. The coefficient of `W[a,b]v_k` in
`ell(W ev,gamma W)` is

\[
\alpha_{a,5b+k}+\sum_i\beta_{i,b}\gamma[i,a,k]. \tag{2}
\]

These 50 equations independently determine all 50 `alpha` entries from
the 30 freely chosen `beta` entries. Their first 50 columns are a
permutation matrix, so the space of constant scalar maps is exactly
30-dimensional over every field. A basis is

\[
L_{i,b}(X)=X_{13}[i,b]-\sum_{a,k}\gamma[i,a,k]X_{02}[a,5b+k].
\tag{3}
\]

The current `L` is `-L_(10,0)`. The same homogeneous transition puts each
map in the scalar target already specified. This classification does not
supply the special first-carrier merger, pole bounds, or a low-cost
geometric numerator for the other 29 maps.

## 4. What all constant maps still miss

Applying the 30 maps at all 81 Laurent positions gives a 2430-row
operator `S`, supported on `n` alone. The executable checks verify every
integer identity in `SA=0`. They compute

\[
\operatorname{rank}_{\mathbf Q}D_2=3648,\qquad
\operatorname{rank}_{\mathbf Q}\begin{bmatrix}D_2\\S\end{bmatrix}=3980.
\]

The combined cohomological rank is consequently 332. Independently,
`rank A=2550` and the transferred image `T ker A` has rank 10, so the
full incoming rank is 2560. Therefore

\[
\dim H^2=6560-3648-2560=352.
\]

The common kernel of all constant scalar maps has dimension 20 over `Q`.
A separate modular elimination verifies combined rank 332 over `F_29`;
it is an additional check, not the proof of the rational statement.

The positive differential `C` has size 160-by-80 and rational rank 50,
so `dim ker C=30`. A boundary has negative part zero exactly when its
preimage lies in `ker A`; the pure-positive boundaries are `T ker A`,
of dimension 10. Thus

\[
\ker C/(T\ker A)
\]

injects into `H^2` as a 20-dimensional subspace. Every constant scalar
map kills it, and its dimension equals their common kernel dimension.
This identifies the entire common kernel over `Q`.

An explicit integer nonboundary in that kernel is

```text
n = 0
p[7] = p[23] = p[50] = 1
all other p entries = 0.
```

Its positive basis keys are
`[0,2,1,2,0,0,0,0]`, `[0,2,4,3,0,0,0,0]`, and
`[1,3,0,0,0,0,0,0]`. The full rational oracle verifies that it is closed,
then produces the positive separating functional `-p[7]+p[25]`, which
kills `T ker A` and takes value `-1` on this cycle. Since `n=0`, all
2430 scalar outputs vanish. This is a synthetic finite-model control;
it is not asserted to be the actual geometric obstruction.

For the current map alone the rational kernel dimension is
`352-34=318`. Vanishing of its 81 coordinates therefore cannot imply
that the original class is zero. Even vanishing of every constant scalar
map would leave the 20-dimensional pure-positive ambiguity.

## 5. Completed result and stopping boundary

The separate exact-rational result package establishes zero at all 46
coordinates outside the 35 forced-zero positions. Combining those
computed zeros with (1) gives the full zero 81-vector for the current
scalar image. Exact rational coefficients and the integer kernels are
used; earlier modular zeros are not lifted by choosing integer
representatives.

This is the completed current-scalar result. It supplies neither a full
boundary preimage nor a nonzero full obstruction witness. No geometric
construction or evaluation of another scalar map is part of this package.

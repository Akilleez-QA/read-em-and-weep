# Correction: include the ambient frame in the cohomology comparison

## Result

The actual source comparison is

\[
A^E_{ij}=-dG_{ij}G_{ij}^{-1}=-L_{ij}^t,
\]

with no extra scalar one-form. The earlier equation (4) in this review and the corresponding author-proof paragraph compared prescribed column arrays before applying the ambient line-frame transport. That was an incorrect description of the actual induced connection difference. The primitive and the full alternating boundary theorem are unchanged.

The independent common-frame challenge is correct. This note supplies the direct source derivation and updates the review rather than defending the earlier formula by cubic scalar-shift invariance.

## 1. Prescribed and common ambient matrices

The pinned [first-order source, sections 1, 2, and 4](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-residual-attribution/first-order-source.md) specifies:

- The ambient line weights are `k=(-1,1,3,5)`.
- The prescribed frame of `N` at vertex i is `nu_i` times the reference frame.
- The differential in that prescribed frame is `D_i,pres=nu_i^-2 D_ref`.
- The middle split columns have factors `(nu_i^-2 I5, 1, nu_i^-2, nu_i^2 I8)`.
- The next split block has factors `(I8,nu_i^2 I2)`; the extreme prescribed split bases are identities.

Consequently an ambient vector in a block of weight k is transported from prescribed coordinates to common coordinates by multiplication by `nu_i^k`. The common-ambient split matrices are

\[
\widetilde U_i^{(r)}=\nu_i^{k_r}U_{i,\mathrm{pres}}^{(r)}.
\]

Every differential raises the line weight by two, so

\[
D_{i,\mathrm{common}}
 =\nu_i^{k_r+2}D_{i,\mathrm{pres}}\nu_i^{-k_r}
 =D_{\mathrm{ref}}.
\]

The paired common split-column exponents agree: `-1` for the first contractible pair, `3` for the next, and `5` for the last. This is also why the extreme common-frame split matrices are generally scalar powers, even though the extreme prescribed matrices are identities.

## 2. Exact cohomology transition

The cohomology lies in the ambient middle block of weight one. Write `I_i` and `P_i` for the reference carrier inclusion and projection. Its prescribed column array and projection array are

\[
f_i=I_i\operatorname{diag}(1,\nu_i^{-2}),
\qquad p_i=\operatorname{diag}(1,\nu_i^2)P_i.
\]

Multiplying the inclusion by the ambient factor and the projection by its inverse gives

\[
e_i=\nu_i f_i=I_i\operatorname{diag}(\nu_i,\nu_i^{-1}),
\qquad
\bar p_i=\nu_i^{-1}p_i=\operatorname{diag}(\nu_i^{-1},\nu_i)P_i.
\]

These are precisely the determinant-normalized physical cohomology inclusion and projection. Thus the actual common-frame transition is

\[
G_{ij}=\bar p_i e_j
 =\operatorname{diag}(\nu_i^{-1},\nu_i)(P_iI_j)
                  \operatorname{diag}(\nu_j,\nu_j^{-1}).
\]

This agrees exactly with the source dictionary `G_ij=g_ij^t`.

The earlier array comparison was

\[
C_{ij}^{\mathrm{arrays}}=p_i f_j=(\nu_i/\nu_j)G_{ij}.
\]

That equality is an algebraic equality of the displayed arrays, but it is not yet a transition between bases in one ambient frame. Applying the required middle ambient factor gives

\[
(\nu_j/\nu_i)C_{ij}^{\mathrm{arrays}}=G_{ij}.
\]

Differentiating only `C_arrays` and calling the result the induced connection difference omitted this factor.

Each split connection is flat in its own transported split basis. Its induced cohomology connection is therefore flat in `e_i`. Expressing the j connection in frame i yields `-dG_ij G_ij^-1`, while the i coefficient is zero. Thus

\[
A^E_{ij}=-dG_{ij}G_{ij}^{-1}=-L_{ij}^t.
\]

## 3. Ambient connection difference and theorem stability

The same transport preserves the tensorial B used in the raw scalar. In weight k,

\[
\Omega_{i,\mathrm{common}}
=-d\widetilde U_i\widetilde U_i^{-1}
=-dU_{i,\mathrm{pres}}U_{i,\mathrm{pres}}^{-1}-k\,d\log\nu_i,
\]

while the old connection coefficient is

\[
k\gamma_{i,\mathrm{common}}
=k\gamma_{i,\mathrm{pres}}-k\,d\log\nu_i.
\]

This transport also preserves the source's connection-difference relation. In one finite coordinate the prescribed old coefficient is `ga=1/[x(x^2-1)]` and the line-ratio logarithmic derivative is `rf=(x^2+1)/[2x(x^2-1)]`. Hence `ga-rf=-1/(2x)`. Summing over the mask bits gives

\[
\gamma_{j,\mathrm{common}}-\gamma_{i,\mathrm{common}}
=-\frac12\sum_a(m_{j,a}-m_{i,a})\frac{dx_a}{x_a}
=-\theta_{ij}.
\]

Thus the old common-frame block difference is exactly `-k theta_ij`. This is the same transported form at infinity; no connection is reset there.

Subtracting gives exactly the source's

\[
B_i=-dU_{i,\mathrm{pres}}U_{i,\mathrm{pres}}^{-1}-k\gamma_{i,\mathrm{pres}}.
\]

Therefore no raw scalar, `Z_i=str(B_i^3)`, or candidate primitive changes. The chain map remains

\[
A'_{ij}=B_j-B_i-k\theta_{ij}I.
\]

The legitimate scalar-shift invariance still proves

\[
\operatorname{str}((B_j-B_i)^3)
=\operatorname{str}((A'_{ij})^3)
=\operatorname{tr}((A^E_{ij})^3)
=\operatorname{tr}(L_{ij}^3).
\]

The last equality follows from the row/column cubic transpose sign and the now-exact `A^E=-L^t`. All remaining transgression algebra, the coefficient `-1/72`, the regularity argument with fixed source connections, and the two-dimensional-projection scope are unchanged.

No physical source was evaluated for this correction. It is derived from the published line weights, frame ratios, split-column factors, and connection transformation law.

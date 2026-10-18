# Independent review of the full-alternation primitive

## Verdict

**Accepted, with the common-ambient-frame normalization stated explicitly below.** Under the pinned physical source premises already used by the ordered-nerve and complete-remainder proofs, the genuine full `S4` alternating projection of the complete raw representative is a regular global boundary. In the prescribed first-row frame, the primitive is

\[
P_{ij}=-\frac1{72}\,\iota_{V_1\wedge V_2\wedge V_3\wedge V_4}
       \left((Z_i+Z_j)\wedge L_{ij}\right),
\qquad Z_i=\operatorname{str}(B_i^3),\quad L_{ij}=g_{ij}^{-1}dg_{ij}.
\]

Thus `e_sign R_raw = delta P` on the full ordered nerve, and its restriction has the same identity on the increasing source cover. The normalized projector is the signed sum over all 24 permutations divided by 24. Four-forms in this review are evaluated on the displayed ordered vector fields without an additional factorial.

This proves vanishing of the previously isolated two-dimensional full-sign projection of the obstruction class. It does not prove that the full obstruction class or its complementary thirty-dimensional target vanishes. It supplies a regular mathematical primitive, not a finite-cutoff coefficient implementation or a new pole/resource certificate.

No actual source polynomial, physical matrix, jet, residual, fiber, owner list, or consumed source experiment was evaluated. The executable checks below use invented matrices only.

## 1. Inputs and source premises

The corrected proof reviewed has SHA-256 `e43de2abc2838f2d5e31c3fd45fc9517c963e3ad9c8a605f00ec62b50263bab9`. The initial proof had SHA-256 `0f380a52c52cf482d9c160e9f386a41520d625b7ac3eddccfa60e05ebfd8c18b`. The common-ambient-frame correction below replaces this review's earlier scalar-shift equation (4); the theorem and primitive are unchanged. See `ERRATUM.md` for the correction and `COMMON_FRAME_CORRECTION.md` for the detailed source derivation.

I independently read the complete-remainder proof and the ordered-source review, then checked the proposed exterior-transgression proof. The relevant frozen source descriptions are:

- [First-order source, sections 1–4](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-residual-attribution/first-order-source.md).
- [Physical frames and poles, sections 1–2 and 4](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-geometric-dependencies/frames-and-poles.md).
- [RS full-source application](https://github.com/Akilleez-QA/read-em-and-weep/blob/e93cf712f9da4926a8450cc870ed45a7bfc379ab/research/codex-swarm/full-source-application/PROOF.md).
- [BI source-boundary comparison](https://github.com/Akilleez-QA/read-em-and-weep/blob/e93cf712f9da4926a8450cc870ed45a7bfc379ab/research/codex-swarm/source-boundary-analysis/PROOF.md).

Their admitted premises include regular inverse split matrices on each carrier/legal open; the correct transported old connections; compatibility of split connections with the actual complex differential; determinant-one normalized rank-two transitions; and the physical coordinate transport. The existing ordered-nerve review establishes that the genuine full permutation action agrees with same-array full alternation of the complete physical formulas, without sorting cover vertices or imposing an invented antisymmetry on the raw scalar.

The already verified reduction is

\[
R_{\rm raw}=\Omega+Q_2+Q_4+E_{12}(s_{{\rm raw},34})+E_{34}(s_{{\rm raw},12}),
\qquad \operatorname{Alt}\Omega=\operatorname{Alt}Q_2=0.
\]

The present audit checks what happens to all the surviving terms. It does not replace these source premises with numerical examples.

## 2. The relevant flatness is valid for the actual four ambient blocks

The raw scalar uses the four connection differences

\[
B_i^{(r)}=-(dU_i^{(r)})(U_i^{(r)})^{-1}-k_r\gamma_i I,
\]

with signs `(-,+,-,+)`, ranks `(5,15,10,2)`, and weights `(-1,1,3,5)`. These are not the projected rank-two connection matrices.

Both connections being subtracted are regular on the same vertex open. Their difference is an endomorphism-valued one-form. In the physical block frame, the old connection coefficient is the scalar one-form `k_r gamma_i`, and it is closed. The split connection coefficient is `B_i+k_r gamma_i` and is flat. Expanding its curvature gives

\[
dB_i+B_i^2=0,
\]

because the scalar cross terms cancel, the scalar one-form squares to zero, and `d gamma_i=0`. The differing weights cause no extra term: they are scalar within each differential-degree block.

This calculation is compatible with the physical scalar line-frame changes. Under a general auxiliary matrix frame it is expressed using the corresponding covariant derivative. No new flatness assertion about a projected connection is required.

For any matrix-valued one-form `X`, ordinary graded trace cyclicity gives `tr(X^2)=0`. Therefore

\[
d\tau_i=0,\qquad \tau_i=\operatorname{str}(kB_i).
\]

## 3. Full raw scalar, differentiation, and the factor 1/24

Set `theta_ij=q_ij/2`. The entire raw scalar is

\[
s_{{\rm raw},ab,ij}=(S_{ij})_{ab}-\frac{15}{8}q_{a,ij}q_{b,ij},
\quad
S_{ij}=\frac14\left\{\operatorname{str}(B_iB_j)
                     +\theta_{ij}(\tau_i+\tau_j)\right\}.
\]

Products here and below are ordinary exterior products. The gerbe correction remains in this equation. It is symmetric in its two scalar indices, so its contribution to full four-slot alternation vanishes. This argument would remain valid with arbitrary derivatives of that symmetric pair correction. For the physical source the complementary derivatives vanish even before alternation by coordinate separation.

Because `d theta=0` and `d tau=0`, the full theta-linear term in `S` is closed. The four-block flatness identity then gives

\[
dS_{ij}=\frac14 T_{ij},
\qquad T_{ij}=\operatorname{str}(B_iB_j^2-B_i^2B_j).
\]

On a triple let `L=L_ij` and let `U` denote the `jk` current transported into the first row frame. Direct expansion of the source's two `E` terms gives

\[
\operatorname{Alt}\big(E_{12}(s_{{\rm raw},34})+E_{34}(s_{{\rm raw},12})\big)
 =\frac16\{dS_{jk}L-dS_{ij}U\}
 =\frac1{24}\{T_{jk}L-T_{ij}U\}.                 \tag{1}
\]

The normalization can be checked without conventions about antisymmetrization operators: for antisymmetric `S_cd`, the coefficient of `dS wedge L` is the sum of twelve signed terms, so `Alt((V_a S_cd)L_b)=(dS wedge L)_1234/12`. The two antisymmetric terms inside each `E`, its prefactor `1/2`, and the second pair-exchanged `E` produce the factor `1/6`.

## 4. Independent universal quartic calculation

Put `t=tr(U L)`, a scalar two-form. Alternating the displayed complete `Q4`, with both curvature corrections retained, gives

\[
\operatorname{Alt}Q_4
=\frac{U^2L^2-L^2U^2}{96}
 +\frac{\operatorname{tr}(U^3)L-\operatorname{tr}(L^3)U}{48}
 -\frac{t(L+U)^2}{48}.                              \tag{2}
\]

I derived these coefficients independently from the source's rank-two formula:

- The two commutator terms give `(U^2L^2-L^2U^2)/96`.
- The two differentiated-`k` quartic terms give the middle numerator divided by 48.
- The two `-c K` terms give the last term divided by 48.

For traceless two-by-two matrix-valued one-forms,

\[
UL-LU=tI,\qquad X^3=\frac12\operatorname{tr}(X^3)I.
\]

The first is the polarized rank-two anticommutator identity with the exterior signs included. For the second, `X^2` is traceless because `tr(X^2)=0`; applying the same rank-two identity to the even form `X^2` and the odd form `X` gives `2X^3=tr(X^3)I`.

Successively commuting with the first identity gives

\[
U^2L^2-L^2U^2=2t(UL+LU),
\quad \operatorname{tr}(U^3)L=3tU^2,
\quad \operatorname{tr}(L^3)U=-3tL^2.
\]

Substitution in (2) yields

\[
\operatorname{Alt}Q_4
=\frac{\operatorname{tr}(U^3)L-\operatorname{tr}(L^3)U}{72}. \tag{3}
\]

In particular the previously observed nonzero quartic control is consistent with the proof: `L=(h,e,f,0)`, `U=(0,0,0,h)` gives `-h/12`. The quartic term is canceled by the corresponding cubic-current terms in the actual scalar transgression, not declared zero on its own.

## 5. Chain-map cubic trace and the normalization correction

The chain map is

\[
A'_{ij}=B_j-B_i-k\theta_{ij}I,
\]

not `B_j-B_i` and not an individual `B_i`. Each split connection makes the same differential horizontal, so its difference is a degree-zero chain endomorphism with one-form coefficients. Products of coefficient chain maps remain chain maps. The paired contractible blocks cancel in the supertrace of their product, leaving the cohomology trace with positive sign, since the cohomology lies in the positive degree-zero block. Thus

\[
\operatorname{str}((A'_{ij})^3)=\operatorname{tr}((A^E_{ij})^3).
\]

For a scalar one-form `a` and matrix-valued one-form `X`,

\[
(X+aI)^2=X^2,\qquad
\operatorname{tr}((X+aI)^3)=\operatorname{tr}(X^3)+a\operatorname{tr}(X^2)
=\operatorname{tr}(X^3).
\]

This removes the `k theta` shift from the cubic trace block by block. It does not assert the shift is a chain map or erase commutators with the differential.

The cohomology comparison must include the ambient line-frame transport. Let `U_i,pres^(r)` denote the source split matrix in the prescribed vertex frame of the block of weight `k_r`. Since that line frame is `nu_i` times the reference line frame, its split matrix in the common ambient frame is

\[
\widetilde U_i^{(r)}=\nu_i^{k_r}U_{i,\mathrm{pres}}^{(r)}.
\]

Every differential raises the weight by two. The source's prescribed differential is `nu_i^-2 D_ref`, so its common-frame matrix is

\[
\nu_i^{k_r+2}(\nu_i^{-2}D_{\mathrm{ref}})\nu_i^{-k_r}=D_{\mathrm{ref}}.
\]

In particular the ambient middle block has weight one. The prescribed cohomology column array is `(I_0,I_1 nu_i^-2)`, but its common-ambient column array is

\[
\nu_i(I_0,I_1\nu_i^{-2})
=I_i^{\mathrm{ref}}\operatorname{diag}(\nu_i,\nu_i^{-1}),
\]

which is exactly the determinant-normalized physical cohomology frame. With its corresponding left inverse, the actual common-frame transition is

\[
G_{ij}=\operatorname{diag}(\nu_i^{-1},\nu_i)(P_iI_j)
                  \operatorname{diag}(\nu_j,\nu_j^{-1})=g_{ij}^t.
\]

Therefore the induced split-connection difference, in the first cohomology frame, is precisely

\[
A^E_{ij}=-dG_{ij}G_{ij}^{-1}=-L_{ij}^t.             \tag{4}
\]

An earlier revision of this review instead differentiated `(nu_i/nu_j)G_ij` and attributed an extra scalar one-form to the actual induced difference. That expression compares the prescribed column arrays before applying their different ambient frame factors. Multiplying by the required ambient comparison factor `nu_j/nu_i` gives `G_ij`; the extra scalar term is absent from the actual source comparison. The scalar-shift invariance proved above is still needed for the ambient `k theta` shift, but it is not needed to repair the cohomology normalization.

Transposing three one-form factors reverses three pairs and changes the trace sign; the three explicit minus signs supply the other minus. Hence

\[
\operatorname{tr}((A^E_{ij})^3)=\operatorname{tr}(L_{ij}^3).
\]

Finally, for odd matrix forms, cyclically moving one factor across the other two has positive sign. Expanding the cube gives

\[
\operatorname{str}((B_j-B_i)^3)=Z_j-Z_i-3T_{ij}.
\]

Combining the preceding identities establishes the required exact source relation

\[
3T_{ij}=Z_j-Z_i-\operatorname{tr}(L_{ij}^3).          \tag{5}
\]

Only ordinary graded cyclicity of forms in one common frame is used. There is no cyclic rearrangement of Alexander–Whitney endpoints.

## 6. Cancellation, row transport, and global regularity

Equations (1), (3), and (5) cancel the two cubic-current terms and give

\[
\operatorname{Alt}R_{\rm raw}
=\frac{(Z_k-Z_j)L-(Z_j-Z_i)U}{72}.                  \tag{6}
\]

The row current cocycle identity is `L_ik=L_ij+U`. Thus the row-End Cech differential of the proposed primitive is

\[
\delta P=\frac{-(Z_j+Z_k)U+(Z_i+Z_k)(L+U)-(Z_i+Z_j)L}{72},
\]

which equals (6), including both signs. This algebra holds on every ordered tuple, including repeated labels.

Each `B_i` is a regular tensorial difference of two fixed connections on its own vertex open. Thus `Z_i=str(B_i^3)` is a regular scalar three-form there. A Cech zero-cochain requires no agreement of the separate `Z_i` on distinct vertices. The accepted homogeneous inverse-splitting identities and the physical-frame theorem provide regularity on legal infinity charts as well as finite ones; the old infinity connection is transported, not reset to zero.

The expression `g_ij^-1 dg_ij` is used in the prescribed physical source frames. Its intrinsic interpretation is the negative row transpose of the induced split-connection difference in (4), which is already tracefree. This explains its compatible physical transport. Under an arbitrary nonconstant change of endpoint bases, one transports the already fixed connections as well; re-flattening the changed frames would define different source data. The proof does not claim that a bare logarithmic derivative is tensorial under that different operation.

With these fixed frames and transports, `P` is a regular row-End edge cochain valued in four-forms. The four product vector fields are global and regular, so evaluating the four-form gives a regular coefficient cochain. Its matrix trace is zero because `tr L=0`. The genuine ordered-nerve permutation covariance identifies (6) with the full geometric sign projection. Restriction to increasing tuples is a chain map and supplies the asserted global class conclusion.

This argument needs no global old flat connection, no local `gamma wedge tau` primitive, no determinant-logarithm constancy argument, and no replacement of the four ambient blocks by rank-two blocks. The ambient contractible contributions remain in the explicit `Z_i` used by the primitive.

## 7. Independent controls and limits

`check_independent.py` is standalone Python using only the standard library and invented rational matrices. It checks:

1. Equation (3) on all `6^4=1,296` basis tensors of four copies of `sl2_L direct-sum sl2_U`. Since both sides are multilinear in the four coordinate slots, this is exhaustive for that quartic tensor identity.
2. The positive column-to-row cubic sign and cubic scalar-shift invariance, with a nonzero cubic negative control for ordinary transpose alone.
3. The full `Alt(Q4+E+E)=delta P` identity on sixteen invented triples of flat rank-two connection germs. Their derivatives obey the Maurer–Cartan equation; these are not arbitrary scalar derivative choices. The differential is also calculated directly from all three edges. Nonzero cases are required.
4. Cancellation of arbitrary symmetric-pair raw scalar correction derivatives under the complete alternation.

All four tests pass under both `python` and `python -O`. No test imports a production source or evaluates the physical model. These controls supplement the universal algebraic proof and do not independently certify its geometric source premises.

The conclusion is a source-bound global boundary theorem for the full alternating projection only. The accepted raw/N14 comparison identifies its cohomology class with the corresponding accepted projection. It does not identify the full raw and N14 cochains, supply a comparison primitive within any finite cutoff, or determine the remaining obstruction component.

# Independent review: regular source-divisor normalization

## Verdict

**PASS. No blocking mathematical findings.**

Reviewed `PROOF.md` with exact SHA-256:

`822607dedbc50765cb46172bbb8f98b1fc1e8845b75f689651f67f73dd173538`

The hash was verified before and after reading the proof. This is an independent deductive audit of the new all-class extraction and its application of the named prior results, not a proof-assistant certification or a new proof of the prior cone geometry.

## Pinned dependencies checked

The following exact files were fetched through the read-only GitHub connector and compared with the claims made in the proof:

1. [PR769 norm construction](https://github.com/Akilleez-QA/read-em-and-weep/blob/1599ab33ec5392433da49fcfbd0bddd5ba1482d3/research/hm/ideal-valued-fifth-norm/PROOF.md), commit `1599ab33ec5392433da49fcfbd0bddd5ba1482d3`, returned blob `a421d2dfbc2aafba50684620ef5d13ac6b561a83`. It gives the positive overlap formula `w_j-w_i=f tau(c_ij)`, the exact stack-square trace image, and the norm quotient with its second-symbol indeterminacy.
2. [PR770 faithfulness theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/b242300110c33627eb77ee5ab36cc81fffa359e4/research/hm/faithful-fifth-norm/PROOF.md), commit `b242300110c33627eb77ee5ab36cc81fffa359e4`, returned blob `dd0489148189fdc8dfd8d9c18dd8f2d8ea32761f`. It proves the actual trace-induced cohomology isomorphism, its quotient by the transported actual second-symbol image, and the fixed-fourth-lift extension criterion.
3. [Square-filtration normalization, sections 1--2](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/POSITIVE-SECOND-BOCKSTEIN-SQUARE-FILTRATION.md), commit `8d8b5be4ce62c3055bb53be9e16d29cc63072f04`, returned blob `7fe07b9b6971e089abf74b4526fe8adb07d242be`. It supplies the exact stack-square quotient, conic/vertex decomposition, physical-positive filtered pieces, `F^6=0`, actual polynomial normalization, relation-bundle sequence, and natural twist-six quotient identification.

## 1. All-class source-divisor lemma

The two exact sequences in section 1 are correct. Locally, if `f l` belongs to `f A`, write `f l=f a` with `a` in `A`; regularity of `f` on the ambient line bundle gives `l=a`. Thus `R -> C` is injective even if `R` has nonzero `f`-torsion. This is not the generally false assertion that `f:R -> R tensor M` is injective.

The cokernel is precisely `(L tensor M)|D`: after quotienting `L tensor M` by `f A`, the kernel of restriction to the full Cartier divisor is `f L/f A`, canonically identified with `L/A`. No reducedness or transversality assumption is used.

The long exact sequence of `0 -> L -> L tensor M -> (L tensor M)|D -> 0` and `H1(L)=0` gives a global lift `r` of every residue `d`. Exactness of the second sequence then produces a unique global `t` with `f t=chi-r`. If `r'-r=f s`, then `t'=t-s`; the section `s` is global and unique. Replacing `chi` by an ambient section changes neither its quotient class nor the extracted class. Conversely, if `f t` is ambient, its ambient representative restricts to zero on `D`, hence equals `f s` for a global `s`; injectivity gives `t=s`. These arguments establish surjectivity, injectivity, and canonicity for all classes, not only the zero class.

The isomorphism is canonical for the specified multiplication section `f`. It requires only the displayed `H1(L)` vanishing, not an additional vanishing for `L tensor M`.

## 2. Actual cone, signs, and source-divisor safety

For the actual integral `Q` and nonzero `f=a^4h`, multiplication is injective on every ambient invertible sheaf. The hypersurface sequence with twists `4,6` gives `H1(O_Q(6))=0` using `H1(O_P4(6))=H2(O_P4(4))=0`; singularity of the cone causes no problem.

The local errors have matching restrictions to the entire, potentially nonreduced divisor `D`. After lifting that residue, `w_i-r=f v_i` is a regular image equation. Subtracting it on overlaps gives

`f(v_j-v_i)=f tau(c_ij)`, hence `v_j-v_i=tau(c_ij)`.

With the positive Čech convention used by PR769, the connecting class is therefore `tau_*(delta_5 K)`, not its negative. Changing the local adjoint lifts adds a section of `Qsq` to each `v_i`; changing the scalar lift can be absorbed by the same change in `r`; changing `r` alone gives exactly an ambient-sextic ambiguity. These are all the stated representative choices.

The argument remains valid on the singular locus, on source zeros, and when `D` contains the support of `R6`. It never assumes torsion-freeness of `R6`, inverts `f` away from `D`, or infers extension from a complement calculation. Identically zero sources are explicitly outside the stated nonzero-source hypotheses; the proof does not silently extend the lemma to `f=0`.

The physical-even restriction is valid because the data and exact sequences are equivariant, `f` is even, and taking invariants is exact in characteristic zero. The proof correctly keeps physical inversion separate from stack-stabilizer parity.

## 3. Existing finite vertex normalization

The claimed normalization agrees with the pinned filtration theorem and does not introduce a homogeneous splitting:

- The conic component is removed by its unique cover-degree-twelve polynomial, a 13-dimensional space. Its vertex restriction is zero because its filtration order is six and `F^6=0`.
- Cover degrees zero and four remove the low vertex quotient. Their actual restrictions are filtered isomorphisms on the two graded pieces, of dimensions `h0(O_L(6))=7` and `dim(Sym4(W')) h0(O_L(4))=5*5=25`. Their conic restrictions vanish.
- Cover degree eight already vanishes on the conic and low vertex grades, so after normalization its contribution is exactly the image of `Sym8(W') tensor H0(O_L(2))` in the top piece. Conversely every element of that image is realized by such an ambient sextic. This checks the full remaining ambiguity, not just a dimension count.

Twisting the pinned relation sequence gives exactly

`0 -> P4 tensor O_L(-2) -> Sym8(W') tensor O_L(2) -> Q4(6) -> 0`.

Its long exact sequence, with `H0(O_L(-2))=0` and `H1(O_L(2))=0`, identifies the quotient with `H1(P4 tensor O_L(-2))`. The middle global polynomial space has dimension `9*3=27`; the boundary target has dimension `4*1=4`; consequently `h0(Q4(6))=31`. The dimensions corroborate the exact-sequence identification, rather than replace it. Local lifting on the two standard affine charts defines precisely this boundary and requires no global splitting or source-dependent matrix inverse.

Composing normalization with the inverse of the sextic connecting isomorphism gives the stated fixed identification `T`. The extracted `eta(K)` is therefore `T(tau_*(delta_5 K))` with the same connecting convention.

## 4. Second-symbol image and limits of the conclusion

Defining `W_a=T(tau_*(V_a))` retains the actual second-symbol image through both exact identifications. PR770's isomorphism yields the stated criterion `beta4_a(h)=0` if and only if `eta(K)` lies in `W_a`. Before quotienting completion changes, `eta(K)=0` is equivalent to vanishing of the actual fifth boundary and hence to extension of the fixed fourth lift. Completion changes alter the class only by the transported image. None of these steps assumes that image vanishes or that its rank is constant.

The genuinely supplied step is a regular representative-level extraction for arbitrary norm cosets. The conic/vertex normalization and trace faithfulness remain explicitly cited dependencies. The proof correctly makes no evaluation of the actual class, no membership decision, no inference from the older `q^3` norm coefficient, and no algebraicity claim.

## Review scope

Only the candidate proof and the three pinned source files were read. No actual-source coefficient, point, derivative, matrix, rank, or source-instance evaluation was performed; no large computation or external write was used. The sole deliverable write is this local review.

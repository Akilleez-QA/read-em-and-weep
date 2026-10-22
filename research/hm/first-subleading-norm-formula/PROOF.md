# The fifth norm class is a leading–first-subleading bilinear pairing

## Scope and pinned inputs

Keep the actual marked rank-two bundle, physical inversion, cone equation q, positive/negative coordinate decomposition, and nonzero sources a and h. Put f=a^4h and K=aJ4, a section of B_(4Q)(12) with K|Q=fN. The conclusion is a formula for the surviving local scalar norm representatives and their global quotient class, not an evaluation of that class.

The inputs are:

- [PR713 at 5b3943980ecaef78ee7f56fbc015d40955fb24f0](https://github.com/Akilleez-QA/read-em-and-weep/commit/5b3943980ecaef78ee7f56fbc015d40955fb24f0), research/hm/leading-vertex-obstruction/PROOF.md: the actual generic harmonic-frame bounds and the vanishing of the weight-minus-two fourth coefficient.
- [PR692 at 858f96ba1539afb1293f31239b8761af08e46f60](https://github.com/Akilleez-QA/read-em-and-weep/commit/858f96ba1539afb1293f31239b8761af08e46f60), research/hm/vertex-scalar-filtration/PROOF.md, and its pinned actual third-neighborhood theorem at [8d8b5be4ce62c3055bb53be9e16d29cc63072f04](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-CORRECTED-THIRD-NEIGHBORHOOD-LIFT-IS-SQUARE-ZERO.md): the regular actual pair and harmonic convention underlying PR713.
- [PR774 at eec909bef4a7e6998737773d5eadd0ad562e79d9](https://github.com/Akilleez-QA/read-em-and-weep/commit/eec909bef4a7e6998737773d5eadd0ad562e79d9): the intrinsic adapted vertex matrix filtration, physical eigenframes, and saturation of its graded coefficients along the entire vertex line L.
- [PR773 at 53209eb6d4e45883ce0f31dd6d9b1c191bd6c4a3](https://github.com/Akilleez-QA/read-em-and-weep/commit/53209eb6d4e45883ce0f31dd6d9b1c191bd6c4a3): only the cover-degree-twelve scalar norm block can contribute; all smaller blocks and all tails of cover degree at least sixteen are ambient-removable in the stated global quotient.
- [PR769 at 1599ab33ec5392433da49fcfbd0bddd5ba1482d3](https://github.com/Akilleez-QA/read-em-and-weep/commit/1599ab33ec5392433da49fcfbd0bddd5ba1482d3) and [PR770 at b242300110c33627eb77ee5ab36cc81fffa359e4](https://github.com/Akilleez-QA/read-em-and-weep/commit/b242300110c33627eb77ee5ab36cc81fffa359e4): the faithful norm-class construction and its second-symbol quotient. [PR772 at 9cfcea876a88cfdaf774e3b02e7cd05739dbfcc4](https://github.com/Akilleez-QA/read-em-and-weep/commit/9cfcea876a88cfdaf774e3b02e7cd05739dbfcc4): full source-divisor normalization.

All harmonic operators below use the fixed equation and convention of these inputs. They are not arbitrary splittings of the q-adic filtration. All scalar twists and the local equation are trivialized on the standard negative-coordinate charts; their overlap units depend only on L, so the displayed cover-weight blocks and harmonic coefficients do not mix under scalar-trivialization changes.

## 1. The actual matrix bound holds everywhere along L

In the regular actual generic frame, PR713 gives J4 as the sum of three harmonic terms with coefficient bounds 12,8,4, multiplied respectively by 1,q,q^2, and a fourth term q^3 times a coefficient of weight at least zero. Thus J4, and therefore K=aJ4, have total weight at least twelve. The source a has transverse weight zero.

This frame is the actual regular-pair frame of PR692 and its cited third-neighborhood theorem, not a frame obtained by a meromorphic diagonalization. Its first section component has initial cubic and its second initial quintic. The cubic-first line is precisely the intrinsic line identified in PR774. Indeed, in comparing two such regular frames, a nonzero constant lower-left entry would introduce a cubic term into the second section component; its quintic initial order excludes that entry. Thus the comparison is adapted, without requiring a homogeneous full pair. Consequently its comparison with a physical eigenframe is an adapted regular invertible change over the completed transverse algebra over C(L). PR774 permits transfer through this change and then saturation to all of L: every forbidden lower coefficient is a section of a locally free graded coefficient module on the integral line and vanishes if its generic restriction vanishes. No zero of a is inverted in this step.

In physical eigenframes every even endomorphism weight is a multiple of four, and a regular even endomorphism has weight at least zero. Here a homogeneous matrix of weight d has diagonal entries of cover degree d, upper entry of degree d-2, and lower entry of degree d+2; q has weight four.

Choose local even trace-free fifth lifts K_i. Their additional terms are q^4 times regular even matrices and thus have weight at least sixteen. Every such lift consequently has the local expansion

    K_i = K_i,[12] + K_i,[16] + terms of total weight at least twenty,

modulo q^5. This is a local homogeneous expansion in a chosen regular eigenframe, not a claimed global splitting of matrix jets.

## 2. Fixed harmonic coefficient operators

Let H be the fixed homogeneous harmonic lift from the cone binary algebra to the ambient positive-coordinate algebra. Define scalar bilinear operators H_r uniquely by

    H(u) H(v) = sum_(r>=0) q^r H(H_r(u,v)).

For homogeneous binary inputs of cover degrees d and e, H_r(u,v) has degree d+e-4r, and is zero if that degree is impossible. Extend coefficientwise over regular functions of L and termwise to completions. For matrices define

    (H_r(A,B))_ab = sum_c H_r(A_ac,B_cb).

In particular these are ordered matrix products. Scalar operator degree parameters refer to the individual entry degrees, not blindly to the total matrix weights. Opposite off-diagonal shifts cancel in a trace. Cyclicity of scalar multiplication gives tr H_r(A,B)=tr H_r(B,A).

Write, on each chart and suppressing the chart index,

    K_[12] = sum_(i=0..3) q^i H(A_i),   wt(A_i)=12-4i,
    K_[16] = sum_(j=0..4) q^j H(B_j),   wt(B_j)=16-4j.

The absence of an i=4 term follows from regular physical-even weight at least zero. The coefficient B_4 is the freely chosen weight-zero part of the fifth-layer correction. The other B_j are first-subleading jets of the fixed four-neighborhood section. One may choose the local extension with B_4=0, but this choice is neither global nor gauge-canonical.

## 3. The fourteen-term formula

Set n(X)=tr(X^2)/2. Since there are no matrix weights between twelve and sixteen, the scalar total-weight-twenty-eight block is exactly

    n(K_i)_[28] = tr(K_i,[12] K_i,[16]).

The factor one-half has disappeared by cyclicity of trace; no additional factor two is present. Therefore its q^4 harmonic coefficient, of cover degree twelve, is

    F_i = sum_(0<=i'<=3, 0<=j<=4, i'+j<=4)
              tr H_(4-i'-j)(A_i', B_j).                         (1)

There are fourteen ordered index pairs: five for i'=0, four for i'=1, three for i'=2, and two for i'=3. Every summand has degree

    (12-4i') + (16-4j) - 4(4-i'-j) = 12.

If B_4=0, its sole term (i',j)=(0,4) is absent, leaving thirteen. This count is universal bookkeeping, not a dimension or rank assertion for actual data. Some summands can vanish for entry-degree reasons.

To identify the norm error rather than merely the norm, choose a GLOBAL scalar reference P extending n(K) from 4Q to 5Q. Such a reference exists by H1(O_Q(16))=0. On each chart write

    n(K_i)-P=q^4 w_i.

If p_12 is the q^4 harmonic coefficient of the scalar total-weight-twenty-eight block P_[28], the exact local equality is

    (w_i)_12 = F_i - p_12.                                  (2)

Thus omitting P from a literal equality for w_i would be incorrect. Its p_12 is, however, an ambient global polynomial block of O_Q(16), so disappears in the quotient by ambient global sections. To see this with no local-choice ambiguity, a global scalar section on 5Q of twist twenty-four lifts to an ambient degree-twenty-four polynomial because H1(O_P4(14))=0; apply the fixed global harmonic decomposition to that polynomial. Terms divisible by q^5 cannot affect p_12. One may choose any convenient global scalar reference, but reference-independence is a quotient statement.

Only the leading matrix jet and its first subleading jet occur in (1). Leading self-products have total weight twenty-four and contribute at q^4 only in scalar cover degree eight. Terms involving matrix weight at least twenty have total weight at least thirty-two and contribute at q^4 only in cover degree at least sixteen. PR773 removes exactly these scalar ranges, globally and without assuming homogeneous square-ideal generators.

## 4. Fifth-layer and frame changes

A local fifth-lift change q^4 D changes w_i exactly by

    tr(K|Q D)=f tr(ND).

The q^8 square term is zero modulo q^5. Its degree-twelve part is f tr(n8 D_0), where n8 is the leading N matrix and D_0 the weight-zero part of D. Formula (1) reproduces this exactly through its B_4 term, since A_0=f n8. This is in the actual leading relation image and hence has zero quotient class. It is not a license to discard an arbitrary first-subleading B_j for j<4.

Gauge independence can be checked before harmonic extraction. A physical adapted transition has nonnegative weights in 4Z. Factor its leading invertible weight-zero part T_0, and write its next part as 1+X_4 modulo weight eight. Conjugation preserves the leading jet up to T_0 conjugation and changes the first subleading jet, after that conjugation, by [K_[12],X_4] (or its negative under the opposite frame convention). The cross pairing changes by

    tr(K_[12] [K_[12],X_4])=0.

Conjugation by T_0 also preserves trace. These equalities are in the ambient algebra before q extraction, and hence prove invariance of the full harmonic sum (1), even though individual A_i and B_j need not be invariant. Local trivializations of scalar twists transform in the usual manner. No flat or globally split eigenframe on a thickening is asserted.

## 5. Global interpretation and the unresolved actual value

Let Qsq=pi_*(I_Z^2(6)) be the actual ordinary STACK square image of tau, and let A_L=ker(O_Q(6)->R_L) be its vertex counterpart. The surviving relation image is

    a^4h times the degree-eight actual square relation
       inside Sym12 U tensor O_L(10).

Equivalently its source is the established P4 O_L(-2), mapped first to Sym8 U tensor O_L(2), then multiplied by a^4h. Keep this image unsaturated at zeros of a. The local family (F_i-p_12) modulo this sheaf image is the degree-twelve representative supplied by PR773. Its class modulo ambient polynomial sections is the faithful raw fifth norm class. A single computation over C(L) does not supply this global class, and generic division by a or h does not decide it.

For comparison with the full source normalization, retain the whole divisor D=div(a^4h), including multiplicities. As in PR772, remove a global scalar lifting the common norm error on D and solve the regular image equation w_i-r=f v_i. Normalize the resulting square-quotient section by its globally liftable conic and lower vertex blocks. This gives the same P4 boundary as the degree-twelve construction. No inversion on D, replacement of the stack square by a coarse square, or deletion of source-zero torsion is allowed.

Finally quotient this boundary by the transported image of beta2_a. At fixed classified lower data, [PR685 at 449a8df60662bd7a1d93e318ea4f7e6dab28e5ad](https://github.com/Akilleez-QA/read-em-and-weep/commit/449a8df60662bd7a1d93e318ea4f7e6dab28e5ad) describes the changes of raw boundary by precisely that second-symbol image. Formula (1) is not a claim of completion-choice independence before this quotient.

The contribution is a finite bilinear input formula for the already faithful scalar criterion: leading total-weight-twelve and first-subleading total-weight-sixteen matrix jets suffice, with the fifth-layer correction killed by the actual relation image. The actual value and its membership in the beta2 image remain unevaluated. No assertion about beta4 vanishing or nonvanishing, further lifting, or algebraicity follows here. The argument is deductive and uses no selected actual coefficients, points, derivatives, matrices, ranks, or large computation; it is not proof-assistant verification.

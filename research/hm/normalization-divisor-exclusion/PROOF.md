# Regular source divisibility excludes globally glued mixed-normalization errors

Conditional written theorem, 2026-10-23. No actual source, parameter, base
point, coefficient, matrix, derivative or instance rank is selected or
evaluated. No physical row or primitive is constructed. This is not Lean
certification or a complete repair of the original geometric theorem.

## 1. Exact inputs and the additional issue being resolved

Use the exact PR866 mixed-contraction formula at
`25b1d2927294fffbc393e6ac2285f5a58cfd6c60`:
https://github.com/Akilleez-QA/read-em-and-weep/blob/25b1d2927294fffbc393e6ac2285f5a58cfd6c60/research/hm/physical-source-normalization/PROOF.md
Its SHA-256 is
`a7f6afe41fe569cb9a061a047b1d0a140fd198950cda6fe3bace6978f3cf0b14`.
In particular retain its regular actual contractions, common ambient frames,
compatible tensor twists, corrected full source, and full-source row domains.

The physical coefficient conventions are those of PR815 at
`0eaeca734b9e17142da2f1bdfd9a1721d0bb1d42`:
https://github.com/Akilleez-QA/read-em-and-weep/blob/0eaeca734b9e17142da2f1bdfd9a1721d0bb1d42/research/hm/affine-square-source-response/PROOF.md
Its SHA-256 is
`78a0f462ffd0710d248658aaf95926f926297b0bae43aade85eb4c7fc934d236`.
It explicitly assigns a transverse cover weight zero to the negative
quadratic a, and retains all physical-twist and marking factors in extraction.

PR889 at `72ac7ecc5447415fa8452f12ed6ec16921a600f4` distinguishes the
negative base line L=P(W) from the positive binary coefficient variables U.
Its exact proof SHA-256 is
`cf85d577d57f3b08369045b99599738498f0caf1fc0e45009a6d2bf227c95b22`.
No equivariance, character decomposition, or source-parameter calibration
theorem from that note is needed below.

PR904 at `b5999dfd50f8469a5d686f331fdf653cbb3be785` is contextual, not a
new premise: its compatible-W invariance and actual-cone/graded distinction
remain valid. The present proof does NOT represent eta as an actual global
cone adjoint, and does not apply the actual cone coefficient-vanishing
theorem to eta. It uses a different restriction imposed by the source factor a.

## 2. Fixed-input hypotheses

Work over C. Fix an arbitrary NONZERO global negative quadratic

    a in H0(L,O_L(2)),    L=P(W)=P1,

and, for the mixed norm comparison, a nonzero positive quartic h in Sym^4 U.
These are universally quantified inputs, not selected actual instances.
Let Z,V,b,W_h,E,X,J3 be the certified full data of PR866, with

    Y=V-bZ,             S=aY,
    T=S-qW_h=dE,        X=aJ3,       dX=q^3 S.

Y has physical twist two, S and T twist four, and X twist ten. The complete
corrected source T remains the argument of every response row Lambda.
The preceding division, canonical or compared correction, and actual
source-membership requirements are not removed by this note.

Take a cover inducing a cover of the ENTIRE L, including the zero divisor
of a. On each chart use two regular contractions of the same actual full
monad, expressed in the common physical frame as in PR866. Require:

1. Their maps and homotopies, and the required inverse frame comparisons,
   are regular on that cover, including over the zeros of a. No inversion
   of a or removal of its zero divisor is allowed.
2. All physical twists are the compatible tensor twists of those SAME
   contractions. Supplying unrelated operators at twists two and four,
   or certifying only one q-multiplication identity, is not enough.
3. The marked cone/weight extraction is the regular one from PR815, with
   a of cover weight zero and all equation, determinant and line factors
   transported before extraction.

These are actual realization requirements, not conclusions inferred from
finite symmetry, an abstract trace row, or a successful arithmetic check.
The full lower projection y and its prescribed maps remain prerequisites
for authenticating this packet; they are not supplied by the theorem.
They make explicit the regular full-cover and tensorial content used below.

Let the local PR866 comparison operators be

    R_t(B)=(g_t^-1 p_B^(t)(B h_B+h_A^(t) B)i_A)_0.

They are defined on ALL local degree-one maps of twist t. Define the local
trace defect by the already proved cone-source formula

    eta_i=tr(n8_i [R_4(S)|Q]_[4]).                              (D1)

The trace coefficient bundle is

    T_trace=Sym^12(U) tensor O_L.

No gluing of eta is inferred from (D1). Gluing over all of L is the separate
hypothesis in the theorem below.

## 3. The local defect is divisible by the base quadratic

Tensor compatibility and O-linearity give, for every local degree-one
twist-two input B and every local expression of the section a,

    R_4(a B)=a R_2(B).                                         (D2)

This is the same naturality used for q in PR866, but applies to a as well.
It follows directly by substituting aB in the displayed operator formula:
the contractions and homotopies are O-linear; the twist-four versions are
the twist-two versions tensored with O(2); scalar multiplication commutes
with frame conjugation and trace-free projection. There is no derivative
of a. This step would fail as a deduction from isolated q-compatibility
alone if unrelated operators had been supplied at different twists.

Restrict (D2) to Q and take marked cover weight four. Since a has cover
weight zero, regular coefficient extraction preserves its factor. Therefore

    eta_i=a_i xi_i,
    xi_i=tr(n8_i [R_2(Y)|Q]_[4]),                              (D3)

where xi_i is a regular local coefficient section of T_trace tensor O_L(-2).
The physical twist drops by two while the positive binary degree stays
twelve. Equivalently, (D3) says eta_i lies in the image of the sheaf map

    a:T_trace(-2) -> T_trace.                                  (D4)

Regularity of xi_i holds also at the zeros of a: it is constructed using
the regular operator R_2 and Y, not obtained by numerically dividing eta_i
by a_i. Thus (D3) is divisibility in a locally free sheaf, not cancellation
inside a zero fiber and not a statement only on L minus div(a).

## 4. Gluing forces the whole defect to vanish

Theorem. Under Section 2, if the local eta_i glue to a global section of
T_trace on all of L, then eta=0. No group-equivariance or polynomial
dependence on the source parameters is required for this fixed-input result.

Proof. The nonzero section a has an effective Cartier zero divisor of
degree two on the integral smooth curve L. Multiplication in (D4) is
injective as a sheaf map. Since the eta_i glue and each is locally in its
image, they define a global section of that image subsheaf.

Explicitly, on an overlap write a_i=t_ij a_j for the O(2) transition and
eta_i=theta_ij eta_j for the trace transition. Formula (D3) gives

    a_i (xi_i-theta_ij t_ij^-1 xi_j)=0.

The local ring has no a-torsion and the coefficient sheaf is locally free.
Thus the parenthesized difference is zero even across div(a), and the xi_i
glue to a global section xi of T_trace(-2). Their gluing is a CONCLUSION
from the gluing of eta, not an assumption about R_2(Y). Nothing here asserts
that the full local operators R_2(Y), or their uncontracted weight-four
coefficients, glue. This is sheaf-level cancellation, not division by the
value of a at a root. Repeated roots cause no change.

Finally

    H0(L,T_trace(-2))=Sym^12(U) tensor H0(P1,O(-2))=0.

Hence xi=0 and eta=a xi=0. Conversely zero eta of course glues.

This proof neither constructs a global cone adjoint nor identifies an
associated-graded section with such an adjoint.

## 5. Consequence for actual mixed normalization

PR866 proves, on the same authenticated data,

    rho_AB-rho_AA=-a^3 h eta,                                   (D5)

and, if the paired rho_AA is global, proves that rho_AB glues if and only
if eta glues. Its argument uses sheaf injectivity of multiplication by
the nonzero a^3 h, including at its divisor; the positive binary vector
is never replaced by one scalar evaluation.

This comparison applies to two globally authenticated responses only when
their difference actually realizes this eta through the pinned packet
formula (D5), with the same full source and lower data. Globality of two
arbitrary candidate responses does not establish such a realization.

Combining that result with Section 4, and assuming the paired rho_AA is
global, gives the sharper fixed-input criterion under the regular all-twist
realization gates:

    rho_AB glues on the full cover
      iff eta=0
      iff rho_AB=rho_AA.                                       (D6)

Thus a nonzero normalization mismatch realized by such a regular mixed
contraction packet must fail global overlap somewhere. A separate eligible
base-fiber calibration is not needed to eliminate a globally glued defect
ON THIS REALIZED SUBCLASS. This does not compute the common scalar, construct
the actual rows or lower projection y, or authenticate a claimed packet.

The proof never evaluates Lambda(S). Formula (D1) legitimately uses the
full-domain R_4 on S; the physical response rows remain evaluated only on
T=S-qW_h in im(d). Compatible-W changes and fifth-order norm data are not
being used to repair a normalization mismatch.

## 6. Scope and failure modes

- PR866's thirteen-dimensional global associated-graded trace space remains
  nonzero. Arbitrary affine coefficient shifts can occupy it. The present
  result says that its intersection with the globally glued defects realized
  by the regular a-divisible comparison construction is zero.
- PR889/891's abstract equivariant family spaces and observation theorems
  remain valid. The present actual source-divisibility gate is stronger
  than their unrestricted abstract family assumptions; it does not prove
  that any pending packet satisfies all realization requirements.
- Divisibility does not establish gluing. The argument requires equality
  of the prescribed trace transitions on a cover of the whole base.
- On the punctured line L minus div(a), a nonzero constant eta can be
  written as a times eta/a. The quotient then has poles at the omitted
  divisor. Punctured-cover regularity or meromorphic homotopies therefore
  cannot support (D6).
- A q-compatible collection of unrelated twist operators need not obey
  (D2). Such data need an independent a-linearity/tensorial certificate.
- The theorem fixes an arbitrary nonzero global a before using its divisor.
  It does not confuse that base-line section with the tautological section
  over the parameter plane, choose a generic parameter, or infer gluing
  of a parameter family from a single specialization.

Consequently this resolves a conditional dependency in normalization:
full regular tensorial realization plus full-cover gluing excludes the
realized global error without a further numerical calibration. It does not
replace actual source membership, physical authentication, or the unknown
full lower projection, and does not decide rho16, beta4 or theorem repair.

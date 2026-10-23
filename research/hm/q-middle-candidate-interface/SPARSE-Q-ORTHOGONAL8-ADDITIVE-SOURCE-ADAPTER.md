# Sparse additive q-orthogonal8 source adapter

## Scope and immutable prerequisites

This package adds a sparse translation of the frozen raw-eight-leg q source
interface. It does not modify the frozen source constructor, the old supported
216/234 data, the equivariant quotient labeling, or any coefficient family.
It performs no source solve, rank test, point test, selected actual coefficient
test, 260-family generation, or claim of source solvability or independence.
The preconditions remain the fresh source and coefficient audits and parent
review before any enlarged-family computation.

Pinned input manifest:
`Q-ORTHOGONAL-A-PLUS-D5-COMPLETION.sha256`, digest
`b67501a8cedb8c81a47826eb90b2f9091b2d15ecaa8a206769e3b229b17deee7`.
Pinned q constructor:
`universal_q_orthogonal_leg_completion.py`, digest
`3864e8a3c291c0ac8e918fb88604fa5033524d999043cf35cc71fec3c71d1ecd`.
The new implementation is `universal_sparse_q_orthogonal_c_source_adapter.py`.

## 1. Domain and literal reduction

Work over the same exact rational Laurent polynomial ring as the frozen sparse
source map. Its public variables are x,y,z,u,w,ha,hb,hc,hd,hf,h,k,l,FB,FC,FD,theta;
only FB,FC,FD,theta are inverted. The binary S,T variables remain internal.
The raw leg order is D5[0:5], raw q-lifts[5:8]. A split-equivariant coefficient
must first undergo the separately verified nontrivial raw-frame congruence.
This module neither assumes nor substitutes an identity section.

For any symmetric positive-linear raw8 tensor K, let Y,Z,rC,R0 be the frozen
raw leg matrices. The sparse interface computes, without any source solve,

    D3_j = -Y K rC_j,       G5 = GZ K rC,
    QY_j = Y K R0_j,        QZ = GZ K R0.

Here Y denotes the complete contracted VVW form, while GZ is the VWW primitive
coefficient matrix. In particular, ZKR0 means the complete contracted VWW
form, not just its WW component.

The existing `OrthogonalSourceMap.source_map_new(D3,G5)` alone reconstructs
Pc,y,Vnorm and all26 existing error sectors. The old supported
`SourceMap.source_map` is never called on the new middle. The checker installs
a tripwire that raises if that forbidden route is taken. The ten old U/VV
sectors remain present as structural exact zeros. None of the off-image C
sectors is screened, including LC, low_literal, high_spin, sigma_harmonic,
high_full_remainder and Lharm.

## 2. All physical scales and source endpoints

Write kappa=bm/am, q0=(xy+z²)/theta. Channel scales are stored separately and
exactly as Laurent exponent tuples in the order (kAt,am,bm,cm), never assigned
values. All five columns U0,U1,C0,C1,C2 remain explicit.

The actual raw C residual is

    kAt cm [D3 + kappa p(G5) + q0(kappa^-1 QY - p(QZ))].

The full source increment is

    source_left = kAt [[0, (cm/am) Pc], [0, -y]],
    source_right = -source_left^T.

Subtracting alpha source_left therefore restores both A(Pc) and B(Pc)
companions, as well as C(y). The actual normalized divided C arrow is

    Vactual = Vnorm - kappa^-1 QY + p(QZ),
    divided_left_C = kAt cm Vactual.

This is the **actual** additive arrow to combine once with the frozen old
arrow. Vnorm by itself is not the q8 divided arrow. Both U divided columns
are exact zero, but remain in the record.

If Ehigh is high_full_remainder plus the Lharm wedge term, the exact full
physical residual identity is

    actual_corrected_left_residual + q0 divided_left
      = kAt cm [Ehigh + kappa low_literal].

The new adapter verifies this equality coefficientwise for every call. The
checker additionally constructs the actual middle action on every alpha
column with the independent SymPy q middle API and compares it with the
sparse raw and corrected residuals at every physical scale.

## 3. Off-image exterior and monad defects are data, not assumptions

Let i_x be exterior contraction and let the fixed alternating source dual
convention give

    d(V)_(i,j) = b(alpha_i,V_j) - b(alpha_j,V_i), i<j.

The adapter retains all five i_x(V_j) defects and all ten d(V)_(i,j) defects,
together with their corresponding error defects, and checks

    q0 i_x(V) = i_x(E),     q0 d(V) = d(E).

These defects are generally nonzero before the joint source errors vanish.
The verifier explicitly checks that both kinds of off-image defects are
nonzero on the universal input, ruling out an accidental closure filter.
Only when the **joint** error cochain is zero does q0 regularity imply the
required closure. No separate closure of the subtracted q0N cochain is
assumed or asserted.

`divided_right_pairing(record,eta)` returns the complete alternating
four-form pairing for all five columns and all channel scales, on arbitrary
eta. It deliberately performs no scalar determinant division. The verifier
compares this right endpoint against the frozen SymPy companion on all20
formal coefficients of an arbitrary spinor-valued two-form, not merely on
already closed eta. Any scalar right-arrow use remains conditional on the
necessary exterior-closure error vanishing.

## 4. Whole-cochain external harmonicity and trace

The frozen reduced sparse adapter accepts externally harmonic data. The new
adapter does not extend it by silently discarding trace. For nonharmonic
inputs, it extracts the h,k,l monomial coefficients, applies the existing
adapter to those coefficient-free pieces, and reinserts **every** monomial
in all reduced candidates, errors and residuals. Literal q restoration then
acts on the full cochain. This is a finite coefficientwise translation, not
a source solve and not a selection of actual source coefficients.

Every operation in the construction is linear over the external parameter
ring and differentiates only x,y,z,u,w,S,T. The raw legs, channel scales and
alpha are independent of h,k,l. Consequently the entire output, including
raw K/middle data, both source endpoints, actual divided arrows, quotient
companions, all26 errors and both kinds of defects, commutes with

    Delta_D = d_h² + 4 d_k d_l.

For quadratic external degree, rho=h²+kl satisfies Delta_D rho=6, and the
whole-cochain harmonic projector is 1-rho Delta_D/6. It must never be applied
only to a middle coefficient while leaving the source/quotient unchanged.
The API exposes `tensor_payload` and `transform_tensors` for precisely this
coefficientwise, whole-record operation. The report's harmonicity flag is
computed from **every** stored mathematical coefficient, not from K alone.

## 5. Universal reproducible comparison

Run:

    python -u verify_sparse_q_orthogonal_c_source_adapter.py

The checker embeds all108 independent coefficients of Sym²(raw8) tensor V
as distinct powers of a formal tag ha. Every K entry has all three positive
coordinates; all36 symmetric positions are included. All operations being
linear over the tag ring, equality of the resulting polynomial is exactly
equality of all108 coefficient-basis maps. This is not evaluation at chosen
values, a rank experiment, or a chosen HM instance. All marking units and
positive/negative source coordinates remain symbolic.

It compares against an independently executed `extend_q_C_source(K)`, then
checks actual all-scale restoration against `restore_q_companion` and
`q_completed_middle_action` on the five source columns. All source-image
and off-image cochain data are retained. A further tensor product uses six
distinct hb powers for the entire external quadratic basis
(h²,hk,hl,k²,kl,l²). It checks the full108-by6 coefficient identity, full-cochain
Delta_D commutation, retained nonzero trace, and whole-cochain harmonic
projection. Twenty distinct hc powers label every right-pairing input.

The receipt, complete log and immutable manifest accompany this note.
The certificate is a sparse-translation result only. It does not authorize
or establish new260 columns, a source solve, operator independence, descent,
a new Bockstein value, or the eventual fourth value.

A second checker, `verify_sparse_q_full_cochain_external_duality.py`, tests
the divided right endpoint on the larger unrestricted cochain domain. It
uses all200 coefficients of five spinor-valued two-form columns at both
physical divided-arrow scales, all20 eta coefficients, and all6 external
quadratic coefficients. It executes the production pairing routine without
any geometric/source constructor, proving its coefficientwise compatibility
with Delta_D and the full Fischer projector, with a nonzero retained trace.
Thus the right endpoint is checked explicitly too, not merely inferred from
the stored left arrow or a middle-only harmonicity calculation.

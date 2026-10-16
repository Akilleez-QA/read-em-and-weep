# A surviving second-jet symbol in the full-gerbe M0 baseline

## Result and limits

There is an exact determinant-one reduction of the mixed second-derivative block: its scalar second jets can be replaced by first-jet traces. Its remaining second-jet-bilinear trace-free symbol is a sum of four Lie brackets, with coefficient 1/8. That symbol is nonzero and cannot be removed by any universal transition-local boundary correction depending only on the transition's two-jet.

This is a formal differential-algebra result. It does not evaluate the pinned HM transitions, their coefficients, or the obstruction; it does not prove the symbol survives a particular source-specific relation, detector, or cover contraction. It gives no new arithmetic complexity certificate.

## 1. Conventions and exact reduction

Use row composition G=BA, p=(1,2), q=(3,4), and the complete baseline from `m0-baseline-independent-audit.md`. All derivatives below are physical derivatives, including the actual frame contributions. The distinct coordinate derivations commute as in the pinned mixed Moyal formula. Write g_ij for D_i D_j g in this note only; these subscripts are derivative indices, not cover endpoints.

Define normalized second jets and first currents

    H_ij = A^(-1) A_ij,
    J_ij = A^(-1) B^(-1) B_ij A,
    L_i  = A^(-1) A_i,
    U_i  = A^(-1) B^(-1) B_i A.

The four signed index pairs are

    (ij,kl,epsilon) = (13,24,+1), (14,23,-1),
                      (23,14,-1), (24,13,+1).

The normalized mixed Moyal block is exactly

    C = (1/4) sum epsilon J_ij H_kl.

Determinant one gives the exact identities

    tr(H_ij)=tr(L_i L_j),
    tr(J_ij)=tr(U_i U_j).

Indeed D_j tr(g^(-1)D_i g)=0 implies
tr(g^(-1)D_jD_i g)=tr((g^(-1)D_jg)(g^(-1)D_i g)).
No derivative of a physical frame is suppressed in this argument.

For arbitrary 2 by 2 matrices X,Y,

    (XY)^0 = [X,Y]/2 + tr(X)Y^0/2 + tr(Y)X^0/2.

This follows from the polarized Cayley-Hamilton identity for traceless matrices. Consequently

    C^0 = (1/8) sum epsilon (
              [J_ij,H_kl]
            + tr(U_i U_j) H_kl^0
            + tr(L_k L_l) J_ij^0 ).                 (A)

Equation (A) eliminates scalar second-jet traces exactly. It retains the 1/4 mixed Moyal factor, yielding 1/8 in the Lie-bracket expression. It is not a claim that evaluating this expression costs fewer products for the selected source circuit.

Every other baseline term contains at most one second jet: k=[L_a,L_b]/4 depends only on first jets; D_c k is linear in second jets; D_c(gk)=(D_c g)k+gD_c k; and each of the four mu terms pairs such a derivative with a first derivative. The quadratic and all three gerbe terms have no second jets. Thus the second-jet-bilinear symbol of M0^0 is precisely the bracket part of (A).

## 2. Exact formal slice exposing the surviving symbol

Consider determinant-one formal transition germs at a point with

    A=B=I,  D_i A=D_i B=0 for every i.

Let a_ij=A_ij and b_ij=B_ij there. Determinant one makes these second jets traceless. All k values on A,B,G vanish. Every differentiated k also vanishes, since each term in its derivative contains a first current. Therefore all quadratic terms and four mu terms vanish. The two noncentral gerbe terms vanish, and the central gerbe term remains -b_p b_q I and is annihilated by exact trace-free projection. No gerbe term was omitted beforehand.

On this slice the entire baseline is therefore

    M0^0 = Omega(b,a)
          = ( [b_13,a_24] - [b_14,a_23]
              - [b_23,a_14] + [b_24,a_13] )/8.    (B)

In particular Omega(a,b)=-Omega(b,a), using the symmetry of the four-pair index tensor and the antisymmetry of the Lie bracket.

This symbol is not identically zero. For abstract noncommuting nilpotent sl2 elements X,Y with X^2=Y^2=0, take formal germs

    A(x)=I+t x_1 x_3 X,
    B(x)=I+s x_2 x_4 Y.

They have determinant one. At the origin their only relevant nonzero second jets are a_13=tX and b_24=sY. Formula (B) becomes

    M0^0 = st [Y,X]/8.

Swapping the two transition germs changes this to st[X,Y]/8. This is a formal Lie-algebra witness, not a numerical or polynomial evaluation of the HM source.

## 3. No universal transition-local two-jet boundary removes it

Here “transition-local two-jet correction” means an edge cochain h_e obtained from that edge's transition value, its first and second physical derivatives, and fixed edge labels. There is no additional vertex-connection or independently varying geometric input. The rule may differ between the three labeled edges; it need not be polynomial or invariant. It cannot depend on another edge's independently chosen jets. Its boundary is

    (delta h)(A,B)=A^(-1)h_bc(B)A-h_ac(BA)+h_ab(A).

On the slice above A has value I, and the two-jet of BA is the sum of the second-jet arrays a+b, with value I and zero first jets. Denote the restricted edge functions by f_ab(a), f_bc(b), f_ac(a+b). Then

    delta h(a,b)=f_bc(b)-f_ac(a+b)+f_ab(a).

Take its mixed interaction

    I_h(a,b)=delta h(a,b)-delta h(a,0)
                         -delta h(0,b)+delta h(0,0).

The single-edge functions cancel, giving

    I_h(a,b)=-f_ac(a+b)+f_ac(a)+f_ac(b)-f_ac(0).

This is symmetric under a,b exchange, even when the three edge rules differ. In contrast, the mixed interaction of M0^0 is the antisymmetric Omega(b,a). Over characteristic zero, a nonzero antisymmetric interaction cannot be canceled by a symmetric one. A residual expression depending only on transition values and first jets has zero mixed interaction on this slice.

Hence neither M0^0+delta h nor M0^0-delta h can be made independent of all second jets by a universal correction of this type. The argument also rules out removing the particular cross-edge interaction b_24 with a_13 together with its exchanged counterpart throughout the universal two-jet algebra.

## 4. What remains open

This is not a nonvanishing proof for the actual obstruction and not a resource lower bound. It does not exclude source-specific second-jet identities, a cancellation after an authenticated detector, corrections using vertex connections or other additional geometric data, or higher-jet corrections. Fourth jets of BA and AB can differ even on the displayed slice; the two-jet boundary argument intentionally makes no claim about such corrections.

The concrete analytic reduction available now is (A). A source-specific circuit may exploit it to replace the trace components of second jets by first-jet contractions. The bracket symbol (B) identifies exactly what still needs source geometry or detector-level cancellation; determinant one, row composition, the canonical k lift, and the complete gerbe alone do not eliminate it.

## Sources and scope

Inputs: `direct-scalar-free-pairing-reduction.md`, `selected-new-m0-circuit.md`, `m0-baseline-independent-audit.md`, and the pinned `crossResidual` / `globalCross` [source formulas](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-geometric-dependencies/data/source-formulas.js). The argument uses formal differential algebra and Lie-algebra identities; no physical source polynomial arithmetic or coefficient extraction was performed.

## Dependency scope

Companion references are identified by basename. A referenced file not supplied with this collection is an external prerequisite, not an embedded proof or a verified relative link. The reading order and unresolved conditions are listed in `proof-notes-index.md`. Reported test results describe the source audit; this proof copy does not by itself constitute a new test run.

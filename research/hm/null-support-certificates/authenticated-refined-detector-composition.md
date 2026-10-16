# Authenticated refined detector and its unexpanded adjoint composition

## Result

The new pole-domain certificate now authenticates an explicit detector Phi on the refined trace-free residual. Its terminal requests are the same three UNIVERSAL tensor slots, with nine matrix-entry coefficient rows, proved from the End differential independently of the old source. Their staircase expansion has78 signed entry seeds before outer carrier/legal labels are summed.

No four-tail, old mask-feature, or old residual sparsity claim is used. All outer and inner label/exponent sums remain symbolic. This is a fully specified coefficient-demand composition, not a priced arithmetic implementation or an evaluated obstruction.

Use `refined-tracefree-pole-domain.md` for the new carrier54/legal29 domain and `transposed-scalar-demand-grammar.md` for the scalar solver's exact adjoints.

## 1. Fixed comparison and terminal rows

Work on the SOURCE-FIRST common cover B with r:B->U its actual standard tag. Use the fresh outer carrier54/legal29 partition Pi_out. Standard coordinate denominators stay units on target standard intersections, as certified by the new domain proof.

Let j map a normalized row-End residual R into the local resolution by

    (jR)_ijk=I_i R_ijk^t P_i.

Let H_r be the local End homotopy on internal-degree-r inputs, applied at the FIRST vertex of the current cochain tuple:

    H_r(F)=H_K F+(-1)^r (IP)F H_K.

Set

    J0=jR,
    J1=H_0 delta J0,
    J2=-H_-1 delta J1,
    J3=H_-2 delta J2.

These signs follow from D=delta+(-1)^q d_End. At Cech degrees3,4,5 the equations are respectively dJ1=delta J0, dJ2=-delta J1, dJ3=delta J2. For closed R the pinned contraction identities make J0+...+J3 a closed total lift. There are no internal-degree-positive components, so the tensor representative has z0=z1=0.

Define the three terminal scalar coefficient functionals on the tensor complex:

    lambda2: chart CCBB, exponent (-1,-2,-2,-2),
      M11[9,3]+M11[10,4]-2 M11[12,6];

    lambda3: chart CCCB, exponent (-1,-2,-3,-3),
      M10[0,3]+2 M10[2,6]+M21[10,1]+2 M21[12,5];

    lambda4: chart CCCC, exponent (-1,-2,-3,-4),
      -M20[0,0]+M31[10,0].

Matrix indices are zero-based. These are the source-independent dual rows proved in `hm-dual-row-anticommutation-proof.md` from the pinned linear differential and tensor contraction. Using them here does not reuse the source-specific four-tail contraction. In particular the minus already present in lambda4 must not erase the separate minus in J2 by an informal sign convention.

Put L_s=lambda_(2+s) S Pi_out, s=0,1,2. Then the actual refined detector is

    Phi(R)=L0(jR)+L1(H_0 delta jR)
                         -L2(H_-1 delta H_0 delta jR).       (1)

This is the expansion of ell P_A S Pi_out J on the new closed source. S has no degree5 tensor target, so J3 contributes no terminal row, while its existence remains part of the closure/comparison proof.

Equation (1) defines a linear formula even on nonclosed cochains. Its cohomological interpretation is asserted on closed R. Therefore one may distribute it across the nonclosed summands of Rsharp without declaring those summands individually cocycles.

## 2. The78 terminal staircase seeds

S^* turns the3 lambda2 entry rows into3*2!=6 signed standard-triple seeds. It turns the4 lambda3 rows into4*3!=24 signed standard-quadruple seeds. It turns the2 lambda4 rows into2*4!=48 signed standard-quintuple seeds.

Each seed records:

- q=2,3,4 and the exact ordered staircase of standard vertices;
- the fixed exponent of its terminal row;
- its matrix entry selector, integer coefficient and staircase permutation sign;
- the future outer weight product over all q+1 vertices.

Thus there are78 unmerged signed entry seeds. This is a seed count, not a nonconstant-product count. Opposite terms may later cancel, and rational matrix kernels may have many entries if expanded; neither possibility is inferred from78.

Pi_out^* attaches the bounded symbolic sum over q+1 carrier/legal labels and multiplies the kernel by the product of their fixed outer weights. It sorts each common tuple source-first with its exact alternating sign. Structural zero weights may be removed; no new source sparsity is assumed.

## 3. Exact adjoints of the local resolution maps

Use the ordinary matrix trace pairing tr(W F), not a supertrace. An entry request on F[a,b] corresponds to a matrix unit in W[b,a]. All tensor/totalization signs have already been stated explicitly.

For H_r,

    H_r^*(W)=W H_K+(-1)^r H_K W(IP).                (2)

This is obtained by ordinary trace cyclicity. Consequently the first homotopy adjoint has a plus between its two terms (r=0), and the second a minus (r=-1). Matrix dimensions and degrees restrict the actual blocks. The factors may remain unexpanded.

For the row-normalized inclusion,

    j^*(W)=(P W I)^t.                              (3)

Indeed tr(W I R^t P)=tr((P W I)^t R). The transpose is essential because the source residual uses the row convention.

For an ordered q+2 tuple, delta^* emits its q+2 faces with sign(-1)^l for deletion of vertex l, retaining the exact restriction/frame map. Resolution End entries are already in their fixed original frames; no new row-transition conjugation is inserted into this delta.

Ownership rule: H_r^* uses the first vertex of the tuple BEFORE its following delta^* deletion. If that vertex is then deleted from the residual's face, its homotopy factor and its outer weight remain in the kernel ledger. Do not replace it by the first vertex of the shorter face or discard its weight. This is how all prefix owners remain accounted for without assuming the old four-tail formula.

The complete residual-dual kernel is therefore

    Phi = j^* [ L0
              + delta^* H_0^* L1
              - delta^* H_0^* delta^* H_-1^* L2 ]. (4)

Read compositions from right to left. This is an explicit finite expression on common-cover residual triples, with all prefix labels and their weights retained.

## 4. Compose the primitive-free residual formula

For p=(1,2), q=(3,4), the closed trace-free representative is

    Rsharp=M0^0+B_q(F_p)+B_p(F_q)
                     +E_q(T_p F_p)+E_p(T_q F_q),

where B_q(f)_ijk=f_ijk k_q,ik and similarly for B_p.

Substituting (4) yields exactly

    Phi(Rsharp)=Phi(M0^0)
       + < B_q^*Phi+T_p^*E_q^*Phi, F_p >
       + < B_p^*Phi+T_q^*E_p^*Phi, F_q >.          (5)

All instances of Phi in (5) are now the authenticated finite formula (4), not an unspecified future detector. There is no quadratic scalar-primitive demand.

For a kernel W on a residual triple,

    B_q^*W = tr(W k_q,ik)

as a scalar kernel on that same F triple. E_p^* emits the four differentiated scalar edge demands stated in the scalar grammar, with currents L,U and signs +,-,+,- divided by2.

Use the exact scalar transpose

    T_a^*=H_rho,a^*+Pi_a^* K_cov^* R^*
                        +Pi_a^* S^* h_a^* A^* R^*.

Here the inner rho and Pi use N14 and the relevant pair character; the outer Pi_out remains carrier54/legal29. These are distinct partitions and must never be merged by pretending they use the same weights.

The remaining h_a^* branches are precisely the grammar's chart/exponent filters. The optional complementary derivative identity changes n_i=0 to-2 and may be used only after the exact frame conversion; it does not commute a derivative through inner or outer weights.

## 5. Minimal abstract nodes

A coefficient-only symbolic implementation needs the following node types; none requires constructing a source polynomial merely to represent the node.

1. TERMINAL(q,cell,kappa,entry,integer): one of the nine rows above.
2. STAIRCASE(permutation): adds the standard tuple and orientation sign.
3. OUTER_LABEL_SUM: q+1 bounded common labels with the fixed carrier54/legal29 weight factors.
4. END_H_ADJOINT(r,owner): the two factored matrix-kernel terms in (2).
5. CECH_FACE(delete_index): the signed face map with restrictions, keeping existing kernel owners.
6. INCLUDE_ADJOINT(owner): formula (3) at the actual residual-triple first vertex.
7. BASELINE or MULTIPLY_K or CURRENT_DERIVATIVE: the three branches of (5); the last emits four scalar edge requests.
8. INNER_PRISM or INNER_K or INNER_AHS: the three bounded branches of T^* from the scalar grammar.
9. REGULARIZED_PRODUCT: combine the exact owned denominators with their specified partition quotients BEFORE differentiating.
10. DERIVATIVE_DEMAND and FINITE_CONVOLUTION: emit shifted exponent equations with scalar derivative factors and finite support predicates.
11. SOURCE_NUMERATOR(pair,sorted_original_triple): the cleared physical F numerator with its authenticated degree box and source-first alternating extension.

A frame-conversion record accompanies every node where coordinates/character change. A pending rational record is not converted into a coefficient atom until node9 supplies its exact cancellation witness. Matrix products remain symbolic factors until a prospective product ledger is explicitly built.

## 6. Derivative cancellation sequencing is mandatory

The new outer-domain certificate clears all carrier/legal poles owned by its tuple; inner scalar weights clear inserted vertices. However after raw Leibniz expansion the two expressions (V rho)F and rho V(F) can each have an apparent inserted-carrier pole of order1 beyond N14.

The valid sequence is:

1. Use the established exact N14 quotient identity to cancel each inserted vertex in rho F, including its legal factors.
2. Differentiate that exact regularized expression, using polynomial derivative nodes and the remaining suffix denominator rule.
3. Compose its suffix/current owners with the outer54/legal29 weight ledger.

This retains derivatives of the weights implicitly and exactly through the differentiated quotient. It neither discards a Leibniz term nor assumes N14 separately clears the uncancelled derivative pieces.

For Pi branches every source vertex is inserted and the input regularizes to a Laurent polynomial before h. For the inner prism, the unchanged suffix retains its owned denominator and receives the proven one-derivative increase. The outer certificate clears those suffix/current poles. Standard-tag factors remain allowed Laurent units throughout the same r projection.

## 7. Terminal finite-demand closure

Once (4)-(6) are represented with exact quotient nodes, every requested coefficient has a bounded label sum and a finite exponent predicate. The outer predicate and uniform envelope are those in the fresh domain note. Inner predicates use the scalar N14 numerator and quotient bounds, and h^* only filters/redirects finite-frame coefficient atoms without adding exponents.

The derivative node shifts a request by e_i and multiplies by its exact integer exponent; convolution subtracts a multiplier exponent within its certified finite support. These operations preserve finite demand. Sorting and all maps in sections2-3 are finite signed sums. Thus (5) now has an authenticated finite coefficient-demand closure at formula level, with no complete scalar primitive as an intermediate object.

This does not make support rectangles occupied, does not make exact cancellations free in an implementation, and does not certify the resulting DAG's multiplication count. The next execution gate is concrete: price these nodes after actual syntactic reuse, specify a live-value schedule and exact coefficient widths, and refuse before arithmetic if either held limit fails.

The obstruction value remains unknown. No polynomial evaluation or budget release is part of this deliverable.

# Source-order comparison: an exact directional curvature defect

## Result and scope

This note advances null's source-comparison work. It does not change ownership of any other scalar or seed work.

There is an exact distinction between (a) reindexing an already defined alternating cochain, which is a chain isomorphism, and (b) rebuilding the ordered cup formula for E12 in a new cover order. The second operation has an explicit curvature defect. Therefore the fresh-order seed-4 E12 zero theorem alone does not prove a historical-order E12 zero theorem.

For orders differing only within the fixed carrier blocks, a conditional seed-4 comparison reduces the missing historical value to a particular curvature-defect contraction. This is more specific than a general request for order invariance. Neither that contraction nor any physical source polynomial is evaluated here. The abstract counterexample below is not a counterexample to the HM zero theorem.

## 1. Sources read and conventions

The public reference is [PR79 snapshot ea2d1a1d2b5774984d0ad48bc15df5fa4d2e0f18](https://github.com/Akilleez-QA/read-em-and-weep/tree/ea2d1a1d2b5774984d0ad48bc15df5fa4d2e0f18). At this ref the following were read directly:

- `research/hm/null-support-certificates/combined-seed4-e12-coverage-audit.md`, Git blob `8deadf7ec3e2bbc4fda4f86bb4563605fd71d85a`: 884736 assignments, six standard permutations, explicitly fresh-order only.
- `research/hm/null-proof-foundations/direct-dual-scalar-fill-contract.md`, Git blob `7073ed6652e31daac56213b4fd014da8dc7c717c`: E, A, and their two differential identities; its reading-order qualification points to the later finite-domain theorem.

The available source copies of the alternating reindexing note, fresh-order contract, physical current binding, carrier-1 selector, generic frame cancellation, authenticated refined detector, and owned-denominator finite-domain certificate were also read. In particular, the later finite-domain theorem already proves bounded gauge annihilation for the full detector. This note does not reinstate the earlier finite-domain gap.

The fresh order is exactly (auxiliary-first carrier rank, numeric low-bit legal-mask integer, standard tag), with carrier 5 assigned sorting rank -1 and other carriers their numeric ranks. Numeric masks run 0 through 15. The competing coordinate-1-first lex order would be 0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15; this is an example, NOT an identified historical order. No inspected historical source supplies the missing intra-carrier enumeration, so O remains an authenticated-order parameter in this note.

The inert historical bridge source was read, not executed. Its checked SHA256 is `731fa3f8e3d9ae49f57f595c34220ef9b6a2bedc9cc6f3875c643978f5f01ab4`. The historical source itself has caller-supplied carrier/mask vertices; its eleven derivative masks do not establish an order of sixteen legal cover masks.

Use the row-End transition convention g_ik=g_jk g_ij. Transport all matrices in one calculation into the same reference frame. Write ell_d,ij=g_ij^(-1)D_d g_ij. Transported currents obey ell_d,ik=ell_d,ij+ell_d,jk. Scalar derivations commute with restriction and the scalar Cech differential, with the actual character/frame conversion retained.

For p=(a,b), t a scalar edge cochain, and F=delta t, set

    E_p(t)_012 = 1/2 [ell_b,01 D_a t_12 - D_a t_01 ell_b,12
                     -ell_a,01 D_b t_12 + D_b t_01 ell_a,12].

This is exactly the four-term directional operator in the source reduction. In the application p=(1,2), t=s_34 and F=F_34. It is not assumed that F or its derivatives vanish.

## 2. The chain map that is genuinely order independent

For authenticated cover orders O and N, let R_q take an O-cochain to an N-cochain by sorting each requested tuple into O order, multiplying by the sorting sign, and restricting/transporting the same section on the same intersection. Then

    delta_N R_q = R_(q+1) delta_O.

Proof: deletion of a vertex changes the sorting parity by the difference between its positions in the two tuples. After the deletion signs are included, corresponding faces agree. Internal sheaf differentials commute with R as well. R is invertible. Repeated full vertices give zero; distinct common vertices with the same physical label must not be identified for a newly constructed common-cover edge cochain.

This same signed permutation identifies the full owned-denominator finite complexes: the product of vertex-owned divisors is unchanged under a tuple permutation, and the signed multiplication differential conjugates by R. Every owner occurrence and its multiplicity remains. This is an exact domain statement, not a coefficient computation.

Consequently R_2 E_O(t) is always well defined. It is the old alternating cochain in new indexing. It is generally NOT E_N(R_1 t), where the subscript indicates that the ordered cup formula was defined on the increasing tuples of that order.

## 3. Exact adjacent-swap and six-permutation formulas

Initially use the oriented tuple (0,1,2). For a permutation pi let eps(pi) be its sign. Evaluate the edge inputs of E using the same alternating t and transported ell, but use the new tuple order for the cup prescription. Define

    C_pi(t) = eps(pi) E_p(t)_(pi(0),pi(1),pi(2)) - E_p(t)_012.

The first expression is transported back to the same frame before subtracting. Put

    B_ij(F) = ell_b,ij D_a F_012 - ell_a,ij D_b F_012.

Then the complete table is

    pi = 012 or 210: C_pi = 0;
    pi = 102 or 201: C_pi = -B_01(F)/2;
    pi = 021 or 120: C_pi = +B_12(F)/2.

In particular these are explicit formulas for both generating adjacent swaps. The table uses the original orientation of F, not a freshly reevaluated scalar curvature.

Proof reduces by linearity to e(l,r)= (l_01 r_12-r_01 l_12)/2, with l_02=l_01+l_12 and f=r_12-r_02+r_01. For swapping the first two vertices,

    -e_102-e_012
       = [l_01(r_02-r_12)-r_01(l_02-l_12)]/2
       = -l_01 f/2.

For swapping the last two vertices,

    -e_021-e_012
       = [(l_02-l_01)r_12+(r_01-r_02)l_12]/2
       = +l_12 f/2.

The remaining entries follow directly or by composing swaps with their orientation signs. Apply this twice, to (ell_b,D_a t) and (ell_a,D_b t), and subtract. No matrix-matrix commutation is used: each differentiated scalar commutes with the matrix current.

Thus, as operators on the new complex, define the exact comparison remainder

    C_ON = E_N R_1 - R_2 E_O.

The table computes R_2^(-1) C_ON locally. It does not redefine R, or claim that a consistently alternating cochain fails alternation. It isolates precisely the difference between the two ordered prescriptions.

## 4. A regular artificial SL2 example and closedness warning

Take N to be the 2-by-2 matrix with N_12=1 and all other entries zero, so N^2=0. Use independent coordinates x,y and constants h=(0,1,1). Define

    g_ij = I + (h_j-h_i)y N,
    D_a = partial_x, D_b = partial_y,
    t_01=t_12=0, t_02=x,

and extend t alternatingly. These transitions have determinant one, polynomial inverses, and g_jk g_ij=g_ik. The currents are ell_a=0 and ell_b,ij=(h_j-h_i)N. Then F_012=-x,

    E_012=0, but -E_102=N/2.

Both sides are regular polynomial sections. This disproves a universal assertion E_N R=R E_O even with genuine SL2 transitions. It is not physical source data, and it says nothing about whether the actual seed-4 sum of defects vanishes.

The differential identity from the pinned foundations is also decisive:

    delta E_p(t) = -A_p(F),
    A_p(F)=1/2(ell_b cup D_a F + D_a F cup ell_b
                       -ell_a cup D_b F - D_b F cup ell_a).

E_p(t) is generally not closed. A fourth artificial vertex with h=(0,1,1,1), D_a t_13=1 and all other differentiated edges zero gives delta E=N/2. Therefore cohomological invariance of a FULL CLOSED obstruction cannot be applied to this directional summand without further proof. A single seed is additionally not known to annihilate boundaries; the dual-cocycle theorem applies to the assembled detector, not each one of its 78 summands.

## 5. A smaller conditional comparison for the actual seed 4

Assume the two authenticated orders preserve the same auxiliary-first carrier blocks and differ only inside a carrier block. This assumption covers a change of legal-mask enumeration, but is not a substitute for obtaining the missing historical witness.

Here L4,O means the SAME refined seed-4 construction written in O order, not the historical scalar-41 detector or an asserted identification with that different construction. The fixed pre-sort standard staircase stays (3,11,15), the coefficient target stays (-1,-2,-2,-2), and the same full owner assignments and weights are summed. A source-sorted permutation of these tags is only a request reindexing, not a change of staircase or terminal row.

For seed 4, the terminal q=2 contribution has no prefix End homotopies. Its inclusion is j_a(R)=I_a R^t P_a and its fixed selector is -2 times entry [12,6]. The outer weight is the product over the same three full owners.

Under an intra-carrier change, the first owner can change but the first carrier cannot. For two owners a,b with the same carrier, the normalized transition is K_ab=(P_a I_b)^t=I; the physical transition is D_b D_a^(-1). Transporting the residual to b changes D_a Rbar D_a^(-1) into D_b Rbar D_b^(-1), and matching physical inclusion/projection cancels those diagonal factors. The bare I and P are identical. The outer scalar product is unchanged, and the staircase sorting sign is exactly the sign already in R. Hence, for the same underlying alternating residual,

    L4,N R_2 = L4,O.                                      (S)

This proves conditional naturality of this q=2 seed functional. It does not establish corresponding seedwise statements for the homotopy-prefix terms in other degrees, or compare nonlinear source definitions.

Suppose further that the historical scalar solution t_O, after reindexing, belongs to the complete per-edge numerator domain already covered by the fresh seed-4 support certificates. Those certificates separate from the entire numerator domain, rather than using particular scalar coefficients. Therefore

    L4,N E_N(R_1 t_O)=0.

Combining this with (S) and the exact operator definition of C_ON yields

    L4,O E_O(t_O) = - L4,N C_ON(t_O).                     (T)

This is the precise residual historical comparison target. It is not yet a zero theorem: the right side consists of the explicit current times D(F_O) defects from section 3, with the actual owned weights, selector, and sorting signs.

There is no automatic diagonal annihilation shortcut. For the possible active first carrier 1, the authenticated selector is

    [2v1(v1^2 v4+v3^2)/h1] Rbar_10
      + [2v1(v1^2+v2^2 v3)/h1] Rbar_00.

Although same-carrier currents are diagonal, this selector retains Rbar_00. A new cancellation or support proof is needed. For such a proof, expanding D F as D t_12-D t_02+D t_01 introduces cross-edge products absent from the original four adjacent-edge terms. Existing separator associations cannot simply be relabeled onto them.

## 6. Complete comparison requirements, without assuming equality of sources

Let the fresh solution satisfy delta_N t_N=F_N, and the historical one satisfy delta_O t_O=F_O. Put Delta t=t_N-R_1 t_O. Then exactly

    delta_N Delta t=F_N-R_2 F_O,
    E_N(t_N)-R_2 E_O(t_O)=C_ON(t_O)+E_N(Delta t).       (U)

Even if F_N=R_2 F_O and the finite-domain theorem supplies Delta t=delta f, only the full admissible detector is entitled to use

    E_N(delta f)=-delta A_p(f).

For seed 4 one may instead use the stronger direct support vanishing, if both edges lie in its certified complete domain. One must not invoke the full detector's boundary annihilation for this isolated seed.

For the full source write

    Rsharp_O=B_O+E_p,O(t_q,O)+E_q,O(t_p,O),

where B includes M0^0 and both Fk corrections, and similarly in N order. A sufficient source comparison is an explicit admitted End edge cochain Q such that

    (B_N-R_2 B_O)
      + C_p,ON(t_q,O)+C_q,ON(t_p,O)
      + E_p,N(Delta t_q)+E_q,N(Delta t_p)
      = delta_N Q.                                   (V)

All terms must be sourced from the same intended geometric deformation problem. Historical nonlinear first corrections, gerbe, and mixed-source formulas cannot be imported merely by sorting their arguments. If the geometric construction itself changes, its equivalence must first be supplied.

Finally compare the FULL detector. It is sufficient to prove on the admitted domain

    Phi_N R_2 - Phi_O = Xi delta_O,
    Phi_N delta_N Q=0,

with an actual admitted comparison/homotopy and source-closure proof. Then (V) proves equality of the full closed-source values. A cohomological comparison on closed inputs can replace this explicit Xi identity, but neither version identifies a single nonclosed E12 component. Existing within-order bounded-primitive results help check the Q domain; they do not themselves construct the cross-order Q or Xi.

A complete historical seed-4 directional zero proof thus needs either (T) plus a zero certificate for its curvature contraction, or a direct historical-order support proof. A full obstruction-value comparison needs the combined equation (V), its domains, historical order/source witnesses, and full detector comparison. The fresh zero theorem remains valid at its existing scope.

## 7. Independent verification and boundaries

`test_order_defect.py` uses only exact rational numbers and abstract cochain symbols. Eight tests pass. All six permutation identities are checked on every basis monomial of the bilinear current/scalar-edge identity; the tetrahedron closedness identity is tested on its complete bilinear basis. Additional controls check nonzero defects, the opposite-sign failure, closed scalar inputs, the genuine reindexing chain map, a generic triangle-evaluation functional's failure to annihilate a boundary, and all six orientations of the same-carrier q=2 inclusion with independent artificial diagonal frames.

No support scan was rerun. No source model was imported into the tests. No physical polynomial was expanded, multiplied, or evaluated. No external posting, source edit, arithmetic admission, or global obstruction conclusion is made. This note and its tests are public-safe; resource admission remains outside their scope.

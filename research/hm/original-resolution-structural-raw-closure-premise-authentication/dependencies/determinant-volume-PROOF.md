Editorial scope: This is a mathematical source edition. Historical review and check statements describe the original artifact, not a fresh run. Supporting snapshots are dependencies, not additional new results. Later PR145 mixed-class vanishing supersedes historical unknown mixed-class status; it does not resolve the six pure diagonal conditions.

Supporting dependency only: this complete source text is not a fresh result of this packet.

# Structural determinant normalization of the six pinned HM frames

## Result and exact dependency boundary

For the six rational carrier frames in the pinned HM model, the primitive contraction identities imply

    det(P_i I_j) = 1   for every ordered carrier pair (i,j).

The additional determinant-normalization premise is proved here by sparse determinant-line geometry. No historical determinant execution receipt is used. The proof still assumes the primitive identity A, `gamma H0_i + I_i P_i + H1_i delta = Id15`, on the six carriers. The already structural literal identity B (`H1_i eta_i=0`) and the structural complex identity C (`ev delta=0`) combine with A via the pinned three-family contraction theorem. This note does not replace the A premise, certify its historical execution, establish legal-owner regularity, evaluate a physical source or detector, or decide the global obstruction.

All computations below are handwritten determinant identities and exact sparse support reasoning. Companion checks inspect inert literal records, coordinate order, support matchings, signs and exponent-shift equality; they perform no actual polynomial or physical matrix multiplication, source specialization, source jets. Tiny invented rational controls are separate from the actual source.

Pinned intake: PR79 head `48b4ae6d9ccf4a8f12ef54f7514f0ec8f4a1d4ba`, read 2026-10-18. The model is `research/hm/null-operator-compiler/hm-pinned-model.json`, Git blob `fcd48a9a22d40d55ce7a08b8aefcb4eaa2fdf761`, SHA256 `635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926`. The relevant source formulas have Git blob `3dfed53a28b53b3c912a097971d89fc547330a5f`. See `source-pins.json` for immutable links.

## 1. Ordered split volumes and the determinant cocycle

Work over `F=Q(v1,v2,v3,v4)`, with `v0=1`; all statements also hold on localizations where their stated denominators are units. The common complex is

    F^5 --gamma--> F^15 --delta--> F^10 --ev--> F^2.

For carrier i, the pivot is p_i=i for i=0,...,4, and p_5=0. The pinned pivot splitting is

    eta_i[:,h] = e_(5h+p_i)/v_(p_i),   h=0,1,
    W_i[:,4h+k-1] = e_(5h+r) - (v_r/v_(p_i)) e_(5h+p_i),
    r=(p_i+k) mod5, k=1,...,4,
    L_i selects those same nonpivot coordinates in that order.

Its literal identities are `L_iW_i=Id8`, `ev W_i=0`, `L_i eta_i=0`, `ev eta_i=Id2`, and `W_iL_i+eta_i ev=Id10`. Define square matrices in the EXACT pinned column orders

    U_i = [gamma | I_i | H1_i W_i],
    V_i = [W_i | eta_i],
    Q_i = [H0_i ; P_i ; L_i delta].

The three-family theorem gives `Q_i=U_i^-1` and `[L_i;ev]=V_i^-1`, together with the full contraction equations. Set

    lambda_i = det(U_i)/det(V_i).

For `T_ij=P_i I_j`, the change of split basis has block upper triangular form

    U_i^-1 U_j =
      [ Id5   *       *       ]
      [  0    T_ij    *       ]
      [  0     0    L_i W_j   ],

whereas

    V_i^-1 V_j = [ L_i W_j   * ; 0  Id2 ].

For the lower-right first block use `delta H1_j=Id10-eta_j ev` and `ev W_j=0`. Dividing the two determinant equalities yields

    det(T_ij) = lambda_j/lambda_i.                    (1)

No determinant sign is hidden in (1): the cohomology block is between the 5-column image block and the 8-column lift block on every carrier. This is the explicit determinant-line invariant left undetermined by an abstract contraction argument.

## 2. Eliminate every homotopy and large split determinant

Let S be any ordered eight-element subset of the 15 ambient coordinates and let E_S be its coordinate inclusion. Put

    N_i(S)=[gamma | I_i | E_S],
    Y_i(S)=[delta E_S | eta_i],
    M_i(S)=L_i delta E_S.

The contraction identity and C imply

    E_S = gamma(H0_i E_S)+I_i(P_i E_S)+(H1_i W_i)M_i(S),
    delta E_S = W_i M_i(S).

Consequently, by block column operations,

    det N_i(S) = det U_i det M_i(S),
    det Y_i(S) = det V_i det M_i(S).

Whenever the chosen sparse minor is nonzero,

    lambda_i = det N_i(S)/det Y_i(S).                (2)

Thus no entry of H0, H1 or P needs to be multiplied. Only the fixed linear differential, seven selected rows of gamma and I, and an eight-coordinate lift remain. Our chosen actual minors below are nonzero, so no rank assumption has been smuggled into (2).

This formula is invariant under changing the complement lifts or the basis of ker(ev): matching contractible-pair determinants cancel. It is strictly stronger than merely restating that the quotient bases need equal volume.

## 3. Five primary carriers: the same two-matchings cancellation

Use zero-based indices. For c=0,...,4 let

    Z_c = sort{ (c+1) mod5, (c+4) mod5,
                5+(c+2) mod5, 5+(c+3) mod5, 10+c },
    D_c = (c,c+5),
    S_c = increasing complement of Z_c union D_c in {0,...,14},
    d_c = product_(r=0..4) v_r - v_c^5.

These d_c are exactly the stored primary denominator records. Literal sparse inspection proves

    (I_c)_(Z_c,:)=0,
    (I_c)_(D_c,:)=diag(1,v_c).                       (3)

The second diagonal assertion is an exponent-shift equality of stored numerator/denominator records, not a computed rational simplification. No other I entries enter the selected wedge determinant.

The following sparse identities, including their signs, are proved immediately below:

    det gamma_(Z_c,:) = (-1)^(c+1) d_c,
    det M_c(S_c) = -v_c^3 d_c.                      (4)

The permutation putting the 15 ambient rows in the order `(Z_c,D_c,S_c)` has sign `(-1)^c`. In this order N is block lower triangular with diagonal blocks `gamma_Z`, `diag(1,v_c)`, and `Id8`. Hence

    det N_c(S_c)=(-1)^c (-1)^(c+1) d_c v_c
                =-v_c d_c.                         (5)

For Y, put its 10 rows in the nonpivot order selected by L_c followed by `(c,c+5)`. This permutation is even. Its top-right block is zero and its bottom-right block is `diag(1/v_c,1/v_c)`. Therefore

    det Y_c(S_c)=det M_c(S_c)/v_c^2=-v_c d_c.       (6)

Equations (2), (5), (6) prove `lambda_c=1` for all five primary carriers.

### Explicit source graph for (4)

Here is the c=0 pattern with v0 temporarily denoted t. This is a presentation of the source's linear 5-cyclic pattern, not a substitution into the physical source. Write `a=v1,b=v2,c=v3,d=v4` within this paragraph only. With `Z_0=(1,4,7,8,10)`, its gamma minor is

    [ 0   0   0   b   t ]
    [ 0   t   c   0   0 ]
    [ 0  -d   0  -t   0 ]
    [ 0   0  -t   0  -a ]
    [ t   0   0   0   0 ].

Its last row forces the first column. The remaining 4-cycle has precisely two perfect matchings, giving `t*(t^4-abcd)=-d_0`. For the actual finite carrier0, t=1.

For `S_0=(2,3,6,9,11,12,13,14)`, the first four columns of `M_0` each have a single nonzero entry. Their Laplace contribution is `-t^4`. The remaining four-by-four matrix, in its retained row and column orders, is

    [ -t   0   d   0 ]
    [  0  -a   0   t ]
    [  0   0   t  -b ]
    [  c  -t   0   0 ].

It has just two perfect matchings and determinant `abcd-t^4`. Thus `det M_0=-t^4(abcd-t^4)=-t^3 d_0`.

The actual gamma and delta literal arrays have the cyclic pattern obtained by simultaneously increasing by one each variable label modulo5, each coordinate within every five-row/five-column block, and the five gamma-domain coordinates. Every complete five-cycle permutation is even. The primary selected I data (3), rather than a guessed equivariance of the full I arrays, supply the required normalized cohomology columns. Transporting the pattern and sorting Z_c gives exactly the first sign in (4); the paired nonpivot orders contribute even parity to the second. The metadata certificate independently lists every selected row/column order, both support matchings and its sign. No homogeneous formula for the unselected stored I entries is assumed.

## 4. Auxiliary carrier: a unique-matchings cancellation

For carrier5 choose

    Z_5=(4,7,8,10,11), D_5=(5,14),
    S_5=(0,1,2,3,6,9,12,13), p_5=0.

The stored I records give

    (I_5)_(Z_5,:)=0,
    (I_5)_(D_5,:)=diag(1,-v4/v1^2).                (7)

With `a=v1,b=v2,c=v3,d=v4`, the gamma minor is

    [ 0   1   c   0   0 ]
    [ 0  -d   0  -1   0 ]
    [ 0   0  -1   0  -a ]
    [ 1   0   0   0   0 ]
    [ 0   a   0   0   0 ].

It has one perfect matching, with column sequence `(2,3,4,0,1)`, positive permutation sign, and product `a^2 c`. The row order `(Z_5,D_5,S_5)` is even, so (7) gives

    det N_5(S_5)=(a^2 c)(-d/a^2)=-cd.              (8)

The sparse M_5 has block upper triangular shape in the displayed S_5 order. Its diagonal blocks are

    A = [  0   0   0   1 ]     B = [  0   0   0   1 ]
        [ -c   0   0   0 ]         [ -1   0   0   0 ]
        [  b  -d   0   0 ]         [  0   1   0   0 ]
        [  0   c  -1   0 ]         [  0   0  -1   0 ].

Both have the unique column sequence `(3,0,1,2)`, of negative permutation sign. Thus `det A=cd`, `det B=-1` and `det M_5=-cd`. As `v_(p_5)=1`, the same even row permutation used for Y above gives

    det Y_5(S_5)=-cd.                              (9)

The denominator record is `d_5=-v1^2 v3 v4`; consequently the needed nonzero factors are already nonzero on its generic localization. Equations (2), (8), (9) prove `lambda_5=1`.

## 5. Consequences for the exact frozen physical transitions

All six lambda values are equal to one. Equation (1) therefore gives the full 36 ordered carrier identities `det(P_i I_j)=1` without constructing any of those products. The pivot determinant also follows directly:

    det V_i=v_(p_i)^(-2),
    det U_i=v_(p_i)^(-2).

For V, moving the first eta column across the second four-column W block is even; each five-dimensional block has determinant `1/v_p`, since its cyclic coordinate permutation is even. This proves the individual split determinant formula rather than importing it.

The pinned common-ambient root-line normalization is `C_i=diag(nu_i,nu_i^-1)`, and the physical column transition is `G_ij=C_i^-1(P_ci I_cj)C_j`, with row transition `g_ij=G_ij^t`. Since det C_i=1 and transpose preserves determinant, the same conclusion is

    det g_ij=1.

This removes the historical determinant-normalization premise from the frozen adjugate-as-inverse interpretation, conditional on the remaining contraction and physical-frame premises. It also supplies the previously conditional rational split determinants used in weighted-trace formulas. It does not prove regularity of rational expressions on the full geometric cover, or independently establish the ambient line-frame identification.

In particular, for the exact frozen two-by-two transition and any correctly interpreted derivation D,

    adj(g_ij)=g_ij^-1,
    tr(g_ij^-1 D(g_ij))=D(det g_ij)/det g_ij=0.

Thus the determinant assumptions in the frozen denominator-free inverse, the traceless logarithmic-current identity, the raw first-order transgression, the mixed-order raw-closure theorem, and the conditional ID0 correctness chain can now be supplied by this structural proof. The other premises in those results remain in force: primitive A, geometric frame/localization, exact derivation/arithmetic semantics, same-source residual identification, and the relevant higher regularity/closure requirements. No downstream conclusion is unconditional merely because this one dependency has been removed.

### Conditional extension to all legal physical overlaps

Assume the accepted physical-frame interpretation identifies the stored finite formula with the prescribed regular transition on every legal overlap, with the stated homogeneous/line transport at infinity. On an integral overlap, the inclusion of regular functions into its function field is injective. The rational identity `det g_ij-1=0` therefore proves the same identity everywhere that this transition is defined, including infinity portions. If the geometric base has several integral components, use this argument on each component meeting the finite comparison locus; any other component needs its own comparison. For the stated irreducible product-of-curves setting, every nonempty open meets the dense finite locus.

This is an extension of an equality of already-defined regular transitions. It is not an argument that an arbitrary rational frame extends regularly, and it cannot supply the separate J3/prism or pole-bound premises. The ambient determinant-line weight is consistent with this conclusion: `-5*(-1)+15*1-10*3+2*5=0`. That weight count is not used as a replacement for the actual sparse normalization or the accepted geometric identification.

## 6. Advancement and remaining work

Previously the determinant cocycle followed from contractions, but agreement of the six specific quotient volumes was only an imported 36-pair historical computation claim. Here a new oriented determinant-line reduction removes H0/H1/P, and the actual pinned sparse gamma/delta/I patterns identify every volume as one. The source-specific content is essential: arbitrary GL2 regauging changes the selected I data (3) or (7) and therefore changes the volume.

The proof needs no unprovided B/C/T construction of the stored primitives. It uses their literal zero rows and normalized entries plus the contraction theorem. The complete remaining nontrivial primitive A premise remains exactly where the earlier bridge left it. No broader obstruction, detector follows.

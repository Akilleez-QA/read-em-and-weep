## 1. Exact premises and geometric distinctions

Use characteristic zero and a localization supporting all frames. Work on the SAME ambient four-term complex K, in degrees −1,0,1,2 of ranks 5,15,10,2. Its ambient summands have root-line weights −1,1,3,5. All restrictions and changes of ambient frame are the actual ones; on a triple intersection all endomorphisms below are transported into one chosen ambient frame before multiplication.

Import the primitive bridge's pivot identities and model identities A: γH0+IP+H1δ_K=1, B: H1η=0, C: ev δ_K=0. These imply the full contraction and complex identities by that bridge; A is imported from the separately scoped historical exact-computation evidence, not independently replayed here; actual-model B is covered by the earlier literal-column proof, and C by the later structural proof linked below. Equivalently one may assume the full contraction plus complex identities directly. They give the physical split frames U and inverse Q, with the precise two distinct cohomology column weights, as established by the moving-frame bridge. In these frames the differential is a constant direct sum of identity pairs and a zero rank-two cohomology summand E in degree zero.

The root-line bridge supplies the external-product identification and tensor old connections as premises for its four-factor consequence. Write θ_ij=(1/2)Σ_r(m_jr−m_ir)dlog x_r. The LOCAL old connections satisfy A_ij=∇_j−∇_i=−kθ_ij Id on the weight-k block. They are flat individually, but do not glue to a global flat connection and need not commute with the complex differential. No supertrace-to-cohomology assertion is applied to A or B.

The split connection ∇'_i is flat in its actual split frame, and

    B_i=∇'_i−∇_i=−(dU_i)U_i^−1−kγ_i Id.

Since its split differential is constant, [∇'_i,D_K]=0. Thus A'_ij=∇'_j−∇'_i is a degree-zero chain-map-valued one-form. Both differences obey A'=A+δB, and δA=0, by subtraction of connections after common ambient transport. Flatness is not needed for the ensuing Čech algebra; compatibility of ∇' with D_K is essential for the cohomological trace step.

The cohomology frames induced by these SAME split connections have column transitions G_ij=g_ij^t and G_ij G_jk=G_ik. This is an identification premise, not something inferred from an unrelated transition cocycle. In the finite root reference, the rank-15 ambient line contributes ν_i while the two split cohomology columns carry (1,ν_i^−2); their actual reference-frame columns are therefore I_i diag(ν_i,ν_i^−1), exactly the transition bridge's quotient frames. Their overlap transition is G_ij=diag(ν_i^−1,ν_i)P_i I_j diag(ν_j,ν_j^−1). The geometric physical-frame agreement is retained on other charts; the old connection must be transported at infinity, never reset to zero.

For the geometric scalar theorem g need only be invertible. To identify F with the frozen raw implementation, import det(P_iI_j)=1: its implemented inverse is an adjugate without determinant division. Contraction alone does not imply this premise, as the transition bridge's volume-rescaling countermodel shows.

## 2. Čech/exterior algebra without a cyclic-cochain shortcut

Let juxtaposition mean ordinary wedge of matrix-valued forms and Alexander–Whitney composition, in that order, with no extra Čech/forms sign. Thus (BA)_ij=B_i∧A_ij and (AB)_ij=A_ij∧B_j. The total product for bidegrees (p,q),(r,s) is (−1)^(qr) times this product. B has (0,1), A and δB have (1,1). Consequently the total transgression is, literally,

    T_ij = str(−B_i A_ij + A_ij B_j − B_i(B_j−B_i)).       (1)

This fixes every sign and endpoint without presupposing a total differential convention. On a triple write X=A_ij, Y=A_jk, B=B_i, C=B_j, D=B_k, all in the same frame. A_ik=X+Y. Expanding (1) in the free noncommutative algebra gives

    δT = str(BY−CY−XD+XC+BD−BC−CD+CC)
        = str(XY−(X+C−B)(Y+D−C))
        = str(A∧A−A'∧A').                                (2)

No letters have been commuted or cyclically rotated. This also proves the claimed total-product formula since A star_tot A=−A∧A for bidegree (1,1). Replacing the two endpoint terms in (1) by twice either one is not valid Alexander–Whitney trace cyclicity and generally changes (2).

On each internal block A_ij=−kθ_ij Id, where θ is an ordinary scalar one-form. Therefore B_i θ=−θ B_i by exterior skew symmetry, and

    T_ij = −str(B_i∧B_j + kθ_ij∧(B_i+B_j)).                (3)

The discarded term is only str(B_i∧B_i). Its contraction in directions a,b is tr(B_i,a B_i,b−B_i,b B_i,a)=0 by the ordinary matrix trace at this SAME endpoint. This is legitimate coefficient trace cyclicity. It is not an interchange of cochains or endpoints. Formula (3) retains B_i∧B_j in its original order and both linear endpoints.

## 3. Why the chain-map supertrace cancellation applies

For any coefficient chain endomorphism M of the split complex, choose one of the fixed splittings on the intersection. Each identity differential pairs a summand in degree n with an isomorphic summand in degree n+1. The relation D_K M=M D_K equates the diagonal blocks of M on the two members of each pair. Their traces occur with opposite signs and cancel. Only the degree-zero E block remains, so str(M)=tr(H(M)). Off-diagonal blocks do not affect trace. This is a direct block proof, valid whether or not M preserves the chosen contractible subspaces individually.

Each directional coefficient of A'_ij and A'_jk is a chain endomorphism because each split connection commutes with the SAME D_K. Their products and the difference of their two wedge coefficients are chain endomorphisms as well. Taking induced maps on cohomology preserves composition. Hence, as actual cochains,

    str(A'∧A') = tr(A^E∧A^E),
    A^E_ij = −dG_ij G_ij^−1.

Neither local old flatness nor a pointwise contraction unrelated to the global differential suffices for this step. In particular, one cannot replace A' by A, or cancel arbitrary B products between adjacent internal degrees.

For the old square, the scalar weight acts on every coordinate of its internal block, so

    str(A∧A) = [−5·(−1)^2+15·1^2−10·3^2+2·5^2] θ∧θ
              = −30 θ∧θ.                                (4)

Here θ is a Čech one-cochain of one-forms: (θ∧θ)_ijk=θ_ij∧θ_jk need not vanish. A scalar one-form wedged with itself at ONE endpoint would vanish, but these endpoints are different.

## 4. Ordered gerbe correction and raw formula

Fix the ordered bivector π_ab=V_a∧V_b, with contraction i_π=i_Vb i_Va, and q_r,ij=2θ_ij(V_r). The q_r are scalar Čech cocycles. Set Q_ab=q_a,ij q_b,jk and r_ij=q_a,ij q_b,ij. Exact scalar expansion yields

    i_π(θ∧θ)=(Q_ab−Q_ba)/4,
    δr=−(Q_ab+Q_ba).

Define, without alternation or endpoint replacement,

    s_raw = −(1/4)i_π T − (15/8)r.                        (5)

Global vector fields and restriction make contraction commute with scalar δ. Using (2)–(4),

    δs_raw = (30/4)i_π(θ∧θ)
               +(1/4)i_π tr(A^E∧A^E)−(15/8)δr
            = (15/8)(Q_ab−Q_ba)+(15/8)(Q_ab+Q_ba)
               +(1/4)i_π tr(A^E∧A^E)
            = (15/4)Q_ab+(1/4)i_π tr(A^E∧A^E).           (6)

Thus the correction is exactly the ordered gerbe b; reversing or dropping its sign would not give b. The same argument adds for the two disjoint ordered pairs (1,2),(3,4).

Contracting (3), (5) gives the literal source recipe

    s_raw,ij = (1/4) Σ_l ε_l {
       tr(B_i,a B_j,b−B_i,b B_j,a)
       + k_l [ (q_a,ij/2)tr(B_i,b+B_j,b)
                 −(q_b,ij/2)tr(B_i,a+B_j,a) ] }
       −(15/8)q_a,ij q_b,ij,

with (ε_l)=(-,+,-,+), (k_l)=(-1,1,3,5), and ranks (5,15,10,2). This is raw_engine.py:76–83 read as text. Its same-ambient block semantics are supplied by the moving-frame bridge. No symmetrized substitute is used. The quadratic edge correction is in general nonalternating; arbitrary antisymmetrization would change the cochain representative and is not part of this proof.

## 5. Row/column reversal, explicitly at coefficient level

Use the row transition convention g_ik=g_jk g_ij and define

    P_r=g_ij^−1 V_r(g_ij),
    Q_r=g_ij^−1 g_jk^−1 V_r(g_jk) g_ij.

The two column connection differences transported to the i frame have coefficients −P_r^t and −Q_r^t. Ordinary coefficient multiplication and tr(M^t)=tr(M) give

    i_π tr(A^E∧A^E)
       =tr(P_a^t Q_b^t−P_b^t Q_a^t)
       =tr(Q_b P_a−Q_a P_b).

The ordered bidifferential μ1(h,g)=(V_a(h)V_b(g)−V_b(h)V_a(g))/2 yields

    C=g_ik^−1 μ1(g_jk,g_ij)=(Q_a P_b−Q_b P_a)/2.

Therefore i_π tr(A^E∧A^E)=−2tr C. No cochain cyclic rotation occurs: transpose reverses ordinary coefficient matrix multiplication. Substitution in (6) proves δs_raw=b−tr C/2=F.

## 6. What this closes and what it does not

This closes the universal same-raw-scalar closure implication required by BI01 once the declared geometric/actual-model premises hold. It does not upgrade BI01's existing import into a proof of those premises. In particular the imported historical primitive A evidence and the separately proved B/C identities, source-specific determinant-one certificate, exact coefficient arithmetic/derivative denotation, legal localization and full physical-frame correspondence remain separate. The proof needs no compatible quantization of separate line summands, no finite RHom projection, no outer cutoff, no second-jet cancellation, no residual/test evaluation, and no production execution.


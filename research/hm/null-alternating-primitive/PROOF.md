# Exterior transgression of the fully alternating raw remainder

## Status and result

This is a symbolic proof candidate, pending independent audit. It uses the genuine full ordered-nerve source and the pinned physical connection/transgression premises. It does not evaluate the source, repeat a source experiment, or construct a coefficient provider.

Let `Alt` be normalized full alternation in four derivative slots, with the full geometric action on all source data. Write `L=g_ij^-1 d g_ij` and `U=g_ij^-1(g_jk^-1 d g_jk)g_ij` on an ordered triple, in its first row frame. Products below are ordinary exterior products with matrix composition, not the totalized Cech/forms product. A displayed four-form means its value on `(V_1,V_2,V_3,V_4)`, with no extra factorial.

For the exact four ambient split-connection differences of the raw scalar, put

    Z_i = str(B_i ∧ B_i ∧ B_i).

Under the regularity, flatness, chain-compatibility, and row/column transport premises verified below, the alternating representative is

    Alt(R_raw)_ijk
      = [(Z_k−Z_j) ∧ L − (Z_j−Z_i) ∧ U] / 72
      = (delta P)_ijk,

where the candidate global row-End edge cochain is

    P_ij = −(Z_i+Z_j) ∧ (g_ij^-1 d g_ij) / 72.

The conclusion is only for the full S4-sign projection. It makes no claim that the unprojected raw remainder, or its other thirty previously isolated dimensions, vanishes. No finite-cutoff or source-compiler admissibility follows from a regular mathematical primitive.

## 1. The precise source connections

Use the four block degrees with supertrace signs `(-,+,-,+)`, ranks `(5,15,10,2)`, and line weights `k=(-1,1,3,5)`. These are the ambient complex blocks from the pinned [first-order source, sections 1, 2, and 4](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-residual-attribution/first-order-source.md), not an arbitrary collection of rank-two cohomology connection matrices.

On vertex open U_i the exact scalar source uses

    B_i^(r) = −(d U_i^(r))(U_i^(r))^-1 − k_r gamma_i I.

The extreme split matrices are identities. Equivalently, B_i is the difference between the flat split connection and the old connection on the same block. Each B_i is therefore an endomorphism-valued one-form on U_i, transforming tensorially. Products involving two vertices are taken after transporting both factors to a common physical ambient frame.

The old block connection is scalar and flat. In the prescribed line frames its coefficient is k_r gamma_i, and d gamma_i=0. The two split matrices are genuine invertible local bases and the split connection is flat. Thus in a common physical block frame

    d B_i^(r) = −B_i^(r) ∧ B_i^(r).                    (1)

Indeed the split coefficient is B_i+k gamma_i, its curvature is zero, the cross terms B_i∧gamma_i+gamma_i∧B_i vanish, gamma_i²=0, and d gamma_i=0. This is the actual connection appearing in the raw scalar. Flatness of unrelated cohomology connections would not establish (1).

The same argument can be stated covariantly: the old covariant exterior derivative on End of each block is ordinary d because the old connection is scalar. The physical block transitions are scalar line-frame changes, so conjugation is trivial within that block, and the equation is compatible with those common-frame changes. Arbitrary non-scalar auxiliary frame changes require covariant differentiation; none are silently substituted here.

Regularity uses the accepted physical-frame theorem: the split matrices and their inverses are regular on their own carrier/legal opens, and the old scalar connections are regular there, including the transported infinity expressions. Hence B_i and its invariant trace Z_i are regular on the vertex open. This does not require a globally flat old connection or a single global old connection at all; the old connections may differ between vertices. A Cech zero-cochain consists of separate regular sections on its vertex opens.

## 2. Keep the full unsymmetrized scalar before alternating

Put theta_ij=q_ij/2 and tau_i=str(k B_i). The exact source formula on every supplied ordered edge is

    s_raw,ab,ij = (S_ij)_ab − 15 q_a,ij q_b,ij / 8,

    S_ij = [str(B_i ∧ B_j)
             + theta_ij ∧ (tau_i+tau_j)] / 4.          (2)

In particular the raw scalar is not replaced by a pair-antisymmetric cochain before applying the action. The last term is symmetric in a,b. Its contribution to full four-slot alternation of either complementary E operator is zero by the odd transposition of those two scalar slots. For the actual product source its complementary derivative is also identically zero, since q_a depends only on coordinate a. Either explanation retains the correction in the original scalar identity.

Let ds_ij denote exterior differentiation of the two-form S_ij, not of a fictitious antisymmetric version of the entire raw scalar. Expanding the exact E operator and its pair-exchanged partner gives

    Alt(E_12(s_raw,34)+E_34(s_raw,12))
      = [dS_jk ∧ L − dS_ij ∧ U] / 6.                 (3)

The scalar dS_jk needs no row conjugation. Its companion U is the transported current displayed at the start, not the untransported g_jk^-1 d g_jk. All source scalar and connection data are transformed before taking Alt.

For the coefficient in (3), with S antisymmetric in c,d,

    Alt((V_a S_cd)L_b) = (dS ∧ L)_1234 / 12.

The two antisymmetric terms in E double this, its prefactor 1/2 cancels that doubling, and the pair-exchanged E doubles it once more. This yields 1/6.

Now d theta_ij=0 and

    d tau_i = −str(k B_i²)=0,

because the trace of the square of any matrix-valued one-form is zero in characteristic zero. Thus the entire theta-linear term in (2) is closed. Applying (1) gives

    dS_ij = T_ij / 4,
    T_ij = str(B_i ∧ B_j² − B_i² ∧ B_j).              (4)

All second derivatives in the alternating scalar contribution have disappeared. This uses flatness of the four actual ambient split connections and the full antisymmetrization; it does not assert that individual complementary derivatives vanish.

## 3. Full exterior simplification of Q4

For traceless two-by-two matrix-valued one-forms L,U put

    t = tr(U∧L),       K(L)=L²/4,       K(U)=U²/4.

Direct alternation of the verified Q4 formula gives the four-form

    Alt(Q4)
      = [U²,L²]/96
        + [tr(U³)∧L − tr(L³)∧U − t∧(L+U)²]/48.     (5)

Here the first bracket is the graded commutator of two even forms, so it is simply U²L²−L²U². The rank-two identities give

    U L − L U = t I,
    X³ = tr(X³) I / 2,
    [U²,L²] = 2t(UL+LU),
    tr(U³)L = 3t U²,
    tr(L³)U = −3t L².                                (6)

The first identity follows coefficientwise from the traceless two-by-two anticommutator identity. The second follows because the alternating product of three traceless two-by-two matrices is scalar. Alternatively it follows by writing X in the three-dimensional basis h,e,f and expanding its only possible triple wedge. For the fourth identity, move L successively across three U factors using the first identity and then use that U³ is a scalar three-form, hence anticommutes with L. The fifth is the analogous identity with L,U exchanged. Substitution in (5) proves

    Alt(Q4) = t ∧ (L²+U²) / 24.                       (7)

The invented negative control L=(h,e,f,0), U=(0,0,0,h) has t∧L²=−2h times the ordered volume form, and U²=0. Formula (7) therefore gives exactly −h/12, as required.

Combining (3), (4), and (7) already gives a usable exterior expression containing only first connection data:

    Alt(R_raw)
      = [t(L²+U²)+T_jk L−T_ij U]/24.                 (8)

The previously verified Alt(Omega)=Alt(Q2)=0 is used here.

## 4. Cubic transgression and the chain-map trace

Let A'_ij be the difference of the two flat split connections on an edge, in the common ambient frame. The exact source identity is

    A'_ij = A_ij+B_j−B_i,
    A_ij^(r)=−k_r theta_ij I.

Each split connection makes the actual complex differential horizontal. Their difference A'_ij is therefore a degree-zero chain endomorphism with one-form coefficients. Every coefficient product of A'_ij is again a chain endomorphism. The usual supertrace identity for a split complex consequently applies to its cubic exterior product:

    str((A'_ij)³) = tr((A^E_ij)³).                   (9)

This does not treat B_i itself as a chain map, and does not erase any [D,B_i] term. Only the genuine difference A'_ij is used in (9).

In each block B_j−B_i=A'_ij+k_r theta_ij I. For any scalar one-form a and matrix-valued one-form X,

    tr((X+aI)³)=tr(X³)+a∧tr(X²)=tr(X³).

Thus the scalar shift has no cubic-trace effect, block by block, irrespective of the differing weights k_r. Hence

    str((B_j−B_i)³)=tr((A^E_ij)³).                   (10)

The actual split cohomology columns are f_i=(I_0,I_1 nu_i^−2), whereas the determinant-normalized physical columns are e_i=nu_i f_i. For G_ij=e_i^−1 e_j=g_ij^t, the split transition is Csplit_ij=(nu_i/nu_j)G_ij. Consequently the induced connection difference is precisely

    A^E_ij = −L_ij^t + (dlog nu_j−dlog nu_i)I.

The scalar term cannot be omitted from the connection itself. It has zero effect on its cubic trace by the same scalar-shift identity. Transposing three one-form factors reverses three pairs, and the three minus signs contribute the other minus. Therefore

    tr((A^E_ij)³)=tr(L_ij³).                        (11)

In particular L_ij is intrinsically the negative transpose of the tracefree induced connection difference. This also supplies its tensorial common-frame covariance. The physical current L_ij is traceless, as required in section 3.

Ordinary graded cyclicity is legitimate for these single-edge differential-form products. It is not an assumed cyclicity of different Alexander–Whitney cochain endpoints. Expanding the cube gives

    str((B_j−B_i)³)=Z_j−Z_i−3T_ij.

Combining with (10)–(11) yields

    3T_ij = Z_j−Z_i−tr(L_ij³).                      (12)

On the next edge, the invariant cubic trace is tr(U³), since U is its first-row-frame conjugate.

## 5. Cancellation and the global primitive

Substitute (12) into (8). The cubic current contribution is

    [−tr(U³)L+tr(L³)U]/3 = −t(L²+U²)

by (6). It cancels all of (7), leaving

    Alt(R_raw)_ijk
      = [(Z_k−Z_j)L−(Z_j−Z_i)U]/72.                 (13)

The Cech current cocycle identity is

    L_ik=L_ij+U_jk,

with U_jk transported to the first row frame. For

    P_ij=−(Z_i+Z_j)L_ij/72,

the row-End differential is

    (delta P)_ijk
      = −[(Z_j+Z_k)U−(Z_i+Z_k)(L+U)
                         +(Z_i+Z_j)L]/72,

which is exactly (13). This works on every ordered tuple, with repetitions allowed; no tuple sorting or guessed alternating extension occurs.

Z_i is a scalar, regular, invariant three-form on U_i because it is the trace of a tensorial connection difference. L_ij is a regular End-valued one-form on U_i∩U_j: intrinsically it is the negative transpose of the tracefree induced connection difference, as explained in section 4, so it transforms in the prescribed first row frame. This statement keeps the fixed source connections under coordinate/frame transport; it does not reset them after arbitrary independent changes of endpoint basis. Therefore P is a regular row-End edge cochain with values in four-forms, and evaluating on the ordered four global product vector fields gives the required scalar-coefficient edge cochain. The tracefree condition is automatic from tr L_ij=0.

No local gamma∧tau primitive was used. Such a primitive has the previously computed common-frame defect; Z_i instead is invariant under physical frame transport from the outset. There is no need to replace four ambient B blocks by six cohomology connection matrices. Their contractible contributions remain inside Z and hence inside the exhibited primitive.

## 6. Evidence boundary

The argument depends on the pinned source's ordinary-wedge formula (2), physical regularity of its splittings, local scalar old connections, flatness and differential-compatibility of its split connections, determinant-one rank-two physical transitions, and the already reviewed geometric ordered-nerve action. Those are mathematical source identities. The algebra is independent of the entries of any physical source polynomial or point.

The candidate proves a global boundary only if these premises apply with exactly the transported source conventions used above. Independent audit should particularly check (1), (9), (11), and the regularity of Z. It does not justify a finite-cutoff executable use of P, additional source evaluations, or elimination of the complementary thirty-dimensional sector.

## 7. Exact invented controls

`check_exterior.py` uses Python's standard library and rational two-by-two matrices only. It independently expands the 24 signed derivative-slot permutations rather than assuming the exterior formulas. It checks 24 quartic inputs, 16 scalar-alternation inputs with arbitrary symmetric scalar corrections retained, and 20 flat scalar-transgression inputs. Every one of those twenty full boundary controls is pointwise nonzero. It also checks the required sparse quartic value −h/12 and rejects the wrong primitive sign.

`check_chain_blocks.py` supplements this with sixteen invented graded block examples having rank-two degree-zero cohomology and one contractible pair. The individual B_i deliberately fail to commute with the differential, while their differences are chain maps. It verifies the cubic supertrace reduction and the complete Q4+E alternating boundary with all block contributions retained in Z. All sixteen resulting boundaries are pointwise nonzero. This tests precisely the distinction that would be lost by treating each B_i as its cohomology block.

Both scripts pass normally and with Python optimization enabled. Their finite examples are controls for signs, coefficients, and algebraic regressions; the universal proof is the displayed exterior identities. Neither imports a physical source, evaluates a source point or polynomial, scans an owner list, or performs any physical-source computation.

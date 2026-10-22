# Complete traceless-W operators have exactly twenty-four presentation relations

## Statement and scope

The complete traceless-W coefficient family of PR746 has dimension162+33=195. Its supported full exterior presentation has kernel dimension24 and image dimension171. Combined with the identity-W family of PR735, the259-dimensional coefficient space has kernel dimension33 and image dimension226. There are no additional cross-relations between the scalar and traceless W families.

These are universal presentation statements, not a source solve, a statement about unrestricted middle cochains, or an obstruction value. The deliberately redundant generator lists607+71 are not independent coefficient coordinates. The theorem concerns the intrinsic195-dimensional coefficient space, not the number of relations in those lists.

Dependencies are the full arbitrary-input exterior assembly in `SUPPORTED-W-ACTIONS-HAVE-A-UNIFIED-FULL-EXTERIOR-ASSEMBLY.md` (PR741), the complete coefficient space in `COMPLETE-TRACELESS-W-COEFFICIENTS-HAVE-AN-EXPLICIT-MARKED-GENERATING-SET.md` (PR746), and the orthogonal tensor calculation in `COMPLETE-IDENTITY-W-OPERATORS-HAVE-EXACTLY-NINE-PRESENTATION-RELATIONS.md` (PR735). A new explicit contraction inverse below proves that no final-contraction relations are missed, including when coefficients depend on the negative coordinates.

Pinned public sources: [full assembly, PR741](https://github.com/Akilleez-QA/read-em-and-weep/blob/eace951d98b0c5adb0462cb2d93c09eac5b08b8b/research/hm/order-four-quadratic-load/SUPPORTED-W-ACTIONS-HAVE-A-UNIFIED-FULL-EXTERIOR-ASSEMBLY.md), [complete coefficients, PR746](https://github.com/Akilleez-QA/read-em-and-weep/blob/b02baa8ef2a8b488d6ef24713933d38aa8a0d2f7/research/hm/order-four-quadratic-load/COMPLETE-TRACELESS-W-COEFFICIENTS-HAVE-AN-EXPLICIT-MARKED-GENERATING-SET.md), and [identity-W kernel, PR735](https://github.com/Akilleez-QA/read-em-and-weep/blob/c727e9d15b8a5ea0509875c174c80e99fc1cbb33/research/hm/order-four-quadratic-load/COMPLETE-IDENTITY-W-OPERATORS-HAVE-EXACTLY-NINE-PRESENTATION-RELATIONS.md).

## 1. Exact traceless-W primitive kernel

Use the constant orthogonal V frame of PR735. Write B(r)_ij=epsilon_ijk r_k and let dagger be the tensor adjoint on V tensor U. For a traceless W factor the primitive presentation is

    Q(H) B(r) + B(r) Q(H)^dagger
      + K B(Hr) + B(Hr) K^dagger.                         (1)

The nonzero common wedge normalization has no effect on its kernel. Q is linear in the arbitrary symmetric trace-free H; K is independent of H. Coefficients are independent of positive base coordinates. Negative variables are permitted throughout.

Split End(U)=1+sl(U). Its symplectic adjoint has signs+1 and−1. Thus (1) has the opposite parity from the identity-W calculation.

On scalar U coefficients, put

    L(K)=tr(K)I−K^t,     L_inverse(Z)=(tr(Z)/2)I−Z^t.

The identity K B(r)+B(r)K^t=B(L(K)r) implies that the kernel is exactly

    Q(H)=−L_inverse(L(K)H),   K arbitrary in End(V).        (2)

This supplies nine explicit free parameters and is an exact inverse, not a rank assertion.

On each sl(U) coefficient, define

    Rec(X)_il=(1/3) sum_jk epsilon_ljk partial_k X_ij.

The identity Rec(QB−BQ^t)=Q−tr(Q)I/3 determines Q modulo its scalar part. Apply it to X=−(KB(Hr)−B(Hr)K^t). The eight literal residual coefficients listed in PR735, and checked again in the standalone verifier, force K=sI. Conversely this gives X=0. Thus this kernel is exactly

    Q(H)=lambda(H)I,     K=sI,                            (3)

where lambda is any linear functional on D5 and s is arbitrary. There are six parameters for each of the three sl(U) factors.

Consequently the primitive kernel before tensoring with sl(W)=A is

    End(V) + (D5+1) tensor sl(U),                         (4)

of dimension27. Equations(2) and(3), tensored with arbitrary W-traceless factors, are a complete parametrization of the universal kernel81 inside the coefficient space648.

### Concrete cross-polar specialization

Taking K=−I/2 in(2) gives Q(H)=−H. In the physical frame this is the six-space coefficient K_H=−H3^t tensor I2. Thus for every traceless W coefficient T,

    primitive(K_H,r,T) = (1/2) primitive(I6,H3 r,T).

This is an equality on all mixed inputs before contraction. Equivalently, the wedge identity −H3^t E_r−E_r H3=E_(H3 r) proves it directly. The two copies of A in N supply two marked specializations of this relation. They are already contained in the24-dimensional kernel and are not two additional relations.

## 2. New explicit inverse for final positive contraction

A primitive kernel need not automatically equal a full exterior kernel. Here they coincide for a structural reason, with an explicit inverse.

Let p be the positive Euler coordinate in an orthogonal frame. The q-polar r is a fixed nonzero scalar multiple of p. Absorb this scalar into the presentation; H r remains an arbitrary linear function of p. Positive contraction on a positive two-form, identified with a three-vector by the volume form, is B(p), up to an irrelevant common sign. Right multiplication by the fixed raising map is invertible and simply identifies the input columns. Therefore the mixed VW output reads B(p) times each primitive matrix block.

Consider any matrix linear in p with fixed transpose parity sigma=+1 or−1:

    M_ij(p)=sum_k C_ijk p_k,     C_ijk=sigma C_jik.

From its contracted matrix F(p)=B(p)M(p), compute

    D_ijk=sum_tl epsilon_til partial_l partial_k F_tj,
    t_j=(sum_a D_jaa)/(3 sigma−1),
    C_ijk=(D_ijk+delta_ik t_j)/3.                          (5)

These are exact formulas over any characteristic-zero coefficient algebra independent of p. Indeed epsilon contraction gives

    D_ijk=3 C_ijk−delta_ik sum_a C_aja.

Transpose parity then gives sum_a D_jaa=(3 sigma−1)sum_a C_aja. Both denominators are nonzero. Thus (5) recovers every coefficient of M from its contracted output. In particular F=0 forces M=0. The verifier checks this inverse with every coefficient of a completely arbitrary symmetric, respectively skew, linear matrix free.

Apply this to the supported primitive. In each U factor, QB+BQ^t is skew and QB−BQ^t is symmetric, including the H-polar summand. For traceless W these parities are respectively skew on scalar U and symmetric on sl(U); identity W has the reverse parities. The mixed output retains both input and output W indices. Hence first projecting these blocks onto scalar W and traceless W, and then splitting U, commutes with positive contraction and isolates exactly the fixed-parity matrices covered by (5).

It follows that a full supported operator that vanishes on arbitrary two-form inputs has zero primitive in every W/U sector. Conversely a zero primitive obviously gives a zero operator. This proves injectivity of the final contraction on the entire joint primitive image. It does not divide by a negative coordinate, assume negative coefficients are constant, or infer injectivity from the VV shadow. Possible negative-coordinate syzygies are eliminated by the mixed output and (5).

This argument is specific to the prescribed coefficient degree: the primitive is linear in positive coordinates and the coefficients Q,K have no positive-coordinate dependence. It is not an injectivity assertion for unrestricted coordinate-dependent middle cochains or for evaluation only on closed/source inputs.

## 3. Marked representation kernel and joint splitting

Use sl(U)=V, End(V)=1+V+D5, and V tensor D5=A+V+P4+D5. Formula(4) becomes

    K_plus = 1+A+3V+P4+2D5.

Tensoring with the inequivalent negative A gives

    K_traceless = K_plus tensor A
                = 1+4A+3V+6P4+7D5.                      (6)

The dimensions are27 and81 respectively. Taking equivariant Hom from N=2A+V+P4+D5 is exact in characteristic zero. Thus

    dim Hom_G(N,K_traceless)=2·4+3+6+7=24.

PR746 supplies the195-dimensional coefficient domain, giving image171. The formulas(2),(3) are G-equivariant kernel parametrizations, so this is a deduction from an explicit kernel, not merely a dimension subtraction conjecture.

The W trace projection separates scalar and traceless primitives. Section2 proves it still separates full-operator relations. Therefore the identity-W kernel9 and traceless-W kernel24 sum directly: joint kernel33, joint image259−33=226. No additional scalar/traceless interaction relation survives on arbitrary mixed input.

## Verification

Run `python verify_complete_traceless_w_presentation_kernel.py`.

The standalone verifier imports only SymPy. It checks the L inverse and complete arbitrary-K relation, the Rec inverse and eight unit residual consequences, the free-tensor final-contraction inverse for both parities, and exact character arithmetic retaining the inequivalent A and V. The log is `verify_complete_traceless_w_presentation_kernel.log`. No actual-instance coefficients, points, numerical scans, source data, matrix-rank computations, source completion, or consumed experiments enter this proof or verifier.

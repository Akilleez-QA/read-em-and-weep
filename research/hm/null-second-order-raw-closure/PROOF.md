# Same-raw mixed second-order closure, with the noncentral gerbe anomaly

## Result

For the SAME rank-two determinant-one physical row transitions, commuting product-factor derivations, raw first lifts, and ordered gerbe used by the pinned source, the literal complete representative satisfies

    δ_row R_raw = 0.

This proves mixed p=(0,1), q=(2,3) closure. It neither proves obstruction vanishing nor asserts closure at the repeated-pair orders p² or q². The crucial additional input beyond first-order exactness is **complementary-coordinate support of the actual ordered gerbe**. It is verified from the inspected leaf formula below. Neither b_p nor b_q is asserted to be central for the whole star product.

For arbitrary ordinary scalar gerbe cocycles, the precise corrected identity is

    δ_row R = tf(g_il^-1 A_ijkl),                         (A)

where

    A_ijkl = μ_p(g_kl,b_q,ijk) g_ik
            +μ_q(g_kl,b_p,ijk) g_ik
            -g_jl μ_p(b_q,jkl,g_ij)
            -g_jl μ_q(b_p,jkl,g_ij).                     (B)

Here a scalar in a μ slot means that scalar times the identity. With determinant-one transitions the normalized anomaly is already traceless. Ordinary δb=0 alone does not set (B) to zero.

## 1. Inspected conventions and dependencies

The local inputs read before this argument were:

- `inputs/raw-first-order-proof.md`, especially §§4–5, together with its `inputs/first-order-source.md` §§3–4 and `inputs/raw_engine.py.txt`.
- `inputs/complete-residual-proof.md`, especially its ten baseline terms, both currents, trace projection, and raw dispatch.
- The input `inputs/direct-scalar-free-pairing-reduction.md` at commit 10810ee877fdaf291399198ad60d7dd0c316a42d, §§1–5.
- The input `inputs/BI01-proof.md` at commit e93cf712f9da4926a8450cc870ed45a7bfc379ab, §§1–3.

The prior closure assertion in direct scalar-free reduction §5 is NOT used as a premise here. Instead it is derived below with its missing noncentral-gerbe qualification made explicit. The first-order raw theorem and literal residual-lowering theorem remain conditional on their declared geometric, determinant, inverse, derivative and implementation premises. This proof does not replay those premises.

Write g_ik=g_jk g_ij, μ_(a,b)(H,G)=((D_aH)(D_bG)−(D_bH)(D_aG))/2. The mixed coefficient μ_pq is exactly

    [(D0D2H)(D1D3G)−(D0D3H)(D1D2G)
     −(D1D2H)(D0D3G)+(D1D3H)(D0D2G)]/4.

Commuting derivations give an associative formal Moyal product. We may work in the quotient by t²=u²=0, with

    H*G = HG+t μ_p(H,G)+u μ_q(H,G)+tu μ_pq(H,G).

This quotient isolates the mixed coefficient and does not assume anything about same-pair second-order lifts.

For an End-valued triple cochain normalized in its first vertex frame,

    (δ_row M)_ijkl = g_ij^-1 M_jkl g_ij−M_ikl+M_ijl−M_ijk.

Conjugation gives δ_row²=0 and preserves ordinary trace. No star inverse, transpose, or right normalization is introduced.

## 2. The first lifts solve exactly the required equation

For r=p,q set

    C_r=g_ik^-1 μ_r(g_jk,g_ij), c_r=tr(C_r)/2,
    F_r=b_r−c_r, k_r=−μ_r(g^-1,g)/2,
    x_r=s_raw,r I+k_r, U_r=g x_r.

Import the already proved raw equation δs_raw,r=F_r and the rank-two transition identity δ_row k_r=−C_r+c_r I. Thus

    δ_row x_r=b_r I−C_r.

Consequently, with T_ij=g_ij+t U_p,ij+u U_q,ij, its degree-zero and degree-one defect against the prescribed ordinary scalar twist vanish:

    T_jk*T_ij−h_ijk T_ik = tu D_ijk,
    h_ijk=1+t b_p,ijk+u b_q,ijk+tu b_p,ijk b_q,ijk.   (1)

The multiplication `h T` in (1) is ORDINARY scalar multiplication, precisely as in the frozen implementation. Writing `h*T` instead changes the second-order source by derivative terms and is not allowed in this proof.

## 3. Every baseline and scalar term is accounted for

The coefficient D is the seven kinetic terms

    U_p,jk U_q,ij + U_q,jk U_p,ij
    +μ_p(U_q,jk,g_ij)+μ_q(U_p,jk,g_ij)
    +μ_p(g_jk,U_q,ij)+μ_q(g_jk,U_p,ij)
    +μ_pq(g_jk,g_ij)

followed by the three negative gerbe terms

    −b_p U_q,ik−b_q U_p,ik−b_p b_q g_ik.

This is the full raw-lift expression; put M=g_ik^-1 D. Replacing U_r by g k_r in these same ten terms defines M0, exactly as in the inspected source. In particular the last scalar gerbe term is present BEFORE projection.

The proved scalar-elimination identity, using δs_r=F_r, gives

    R_raw = tf(M)+δ_row W,
    W=s_q k_p+s_p k_q,

    R_raw = tf(M0)+F_q k_p,ik+F_p k_q,ik
                     +E_p(s_q)+E_q(s_p).                 (2)

The E terms retain both differentiated endpoints and transported currents:

    E_(a,b)(s)=1/2[(D_a s_jk)L_b−(D_b s_jk)L_a
                           +(D_b s_ij)U_a−(D_a s_ij)U_b],
    L_d=g_ij^-1 D_d g_ij,
    U_d=g_ij^-1 g_jk^-1(D_d g_jk)g_ij.

Thus δ_row R_raw=tf(δ_row M), with no assumption that M0 or any separate Fk/E summand is closed. Removal of the boundary δW is legitimate because δ_row²=0. Removal of the trace is legitimate because conjugation commutes with tf. Neither operation presupposes star-centrality of b.

## 4. Ordinary scalar cocycle versus star noncentrality

The actual q_r are scalar Čech cocycles; their ordered cup products obey

    b_r,ijk+b_r,ikl=b_r,jkl+b_r,ijl.

For example this follows by substituting q_r,ik=q_r,ij+q_r,jk into the four ordered products, with no antisymmetrization. Therefore, in the quotient t²=u²=0,

    h_ijk h_ikl = h_jkl h_ijl.                            (3)

These products are ordinary. Formula (3) does not say h can pass through a star product.

To see exactly what remains, apply associativity to

    T_kl*(T_jk*T_ij)−(T_kl*T_jk)*T_ij=0.

Insert (1). Commuting the scalar h only through ordinary products, and retaining the product-rule errors in first star coefficients, gives at tu:

    0 = g_kl D_ijk−D_jkl g_ij+D_ikl−D_ijl+A_ijkl.        (4)

The ordinary scalar term is zero by (3). The two remaining errors are, for each complementary (r,s),

    μ_r(g_kl,b_s,ijk g_ik)−b_s,ijk μ_r(g_kl,g_ik)
         = μ_r(g_kl,b_s,ijk) g_ik,

    −μ_r(b_s,jkl g_jl,g_ij)+b_s,jkl μ_r(g_jl,g_ij)
         = −g_jl μ_r(b_s,jkl,g_ij).

These are precisely (B). Terms with μ_pq and a nonconstant part of h have parameter degree above tu, so no additional gerbe derivative term is omitted. First-lift terms multiplying an h derivative likewise have higher parameter degree.

Using g_il=g_kl g_ik=g_jl g_ij, the first four terms in (4) equal −g_il δ_row M. This proves (A), including its sign and normalization side.

For determinant-one g, tr(g^-1 D_d g)=0. The normalized first anomaly summand is a conjugate of g_kl^-1 μ_r(g_kl,b); the normalized second is −g_ij^-1 μ_r(b,g_ij). Each is a scalar linear combination of traceless logarithmic currents. Thus tr(g_il^-1 A)=0. In particular projecting to tf generally does NOT eliminate the anomaly.

## 5. Actual support kills exactly the required anomaly

The frozen raw leaf at `raw_engine.py.txt:138` reads literally

    def q(self,a,b,d):return self.ex.scalar(((b.legal_mask>>d)&1)-((a.legal_mask>>d)&1))*(self.y[d]/self.x[d])

This is inert source text, not executed here. It agrees with the first-order source dictionary: after removing the invariant y_d factor, q_d is the mask difference divided by x_d. Under the physical product-factor derivative premise, D_e x_d=D_e y_d=0 for e≠d, and cover masks are constant. Hence

    D_2 b_p=D_3 b_p=0,
    D_0 b_q=D_1 b_q=0.                                  (5)

These are global product-factor statements, retained on infinity charts and legal localizations; differentiating in an unrelated product factor still vanishes. They are statements about the physical q leaf, not about frame-stripped derivatives of arbitrary matrix leaves.

Every μ in (B) differentiates b_q with p directions or b_p with q directions. Therefore (5) makes A=0. Equation (4) proves δ_row M=0, and (2) proves δ_row R_raw=0.

This is mixed-sector compatibility, not full star-centrality. Same-pair derivatives of b_p or b_q need not vanish. If the product-factor leaf denotation is unavailable, the honest result remains the conditional defect identity (A), with (5) as a sufficient additional hypothesis. More generally the exact necessary and sufficient condition for this representative's closure is tf(g_il^-1 A)=0 on every quadruple.

## 6. Scalar removal and class scope

Closure needs no scalar cohomology vanishing: tf is a Čech chain projection, so tf(M) is closed once M is closed. The stronger claim that R_raw represents the same FULL End-valued obstruction class as M additionally uses the independently supplied full-sign scalar H²=0. That character/cohomology result is not reproved here. The exact identity R_raw=tf(M)+δW and the derived full M closure place that use on the actual closed cochain, never on isolated central terms of the nonclosed baseline.

## 7. Formal verification and restrictions

`check.py` uses invented free noncommutative matrix words, commuting scalar jet symbols, rational coefficients, and commuting formal Leibniz derivatives. It constructs arbitrary free edge transitions a,b,c with g_02=ba, g_13=cb, g_03=cba; defines first lifts recursively using the first-order equation; and enforces only the ordinary b cocycle. It independently verifies the other first-lift route around the tetrahedron, constructs all ten second-order terms, and proves (4) exactly. Without the complementary-support rule the anomaly has eight free words; imposing that rule makes both the anomaly and the Čech defect zero. An omitted negative gerbe term is rejected as a mutation.

The checker imports no production module, executes no frozen source, and computes no actual source/model/owner/jet values or physical matrix-polynomial products. It does not verify rank-two trace identities by a concrete matrix computation; those are the symbolic arguments stated above. It is a proof control for the universal ordered algebra, not a physical detector or an execution-admission certificate.


## 8. Independent audit clarification and traceless negative control

The first-order equation supplies degree-one defect cancellation only. The full degree-tu coefficient D is then computed from those first lifts, with no second-order lift supplied or assumed. Associativity relates its boundary to A; it does not assert D is a boundary. The scalar-elimination identity in section 3 follows by the elementary expansion in inputs/direct-scalar-free-pairing-reduction.md section 4. That expansion does not use section 5's prior closure assertion.

All derivations are the same globally defined product-factor derivations restricted to each intersection. Their restrictions commute with localization by the quotient rule. They commute with each other because they act on separate factors. Pullbacks of functions from factor d remain annihilated by a derivation from factor e != d, including on infinity charts. No claim is made that entrywise differentiation commutes with arbitrary moving-frame conjugation; derivatives of those frames remain present throughout. The actual leaf denotation and invertibility on legal intersections remain imported premises.

Ordinary scalar cocycle closure cannot in general be repaired by taking trace-free parts. For a formal example let N^2=0, tr(N)=0, tr(1)=2, and set g01=g12=1, g23=1+z0 N. These are the symbolic unipotent determinant-one relations. Set bq,012=bq,013=z1, bq,023=bq,123=0 and bp=0. The ordinary scalar cocycle holds. With D0(z0)=D1(z1)=1 and all cross derivatives zero, A=N/2 and g03^-1 A=(1-z0 N)N/2=N/2. This is nonzero and traceless. The checker specializes only invented formal words into this nilpotent algebra; it performs no physical matrix or model evaluation.

The portable checker additionally rejects anomaly-sign, missing mixed coefficient, reversed word order, and omitted-gerbe mutations, and verifies the nilpotent countercontrol. Input hashes and the exact inert q AST are checked before the formal algebra. All checks use explicit exceptions and remain active with Python optimization enabled.

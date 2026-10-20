# Publication scope

This is a preserved theorem manuscript, with the exact hypotheses and held identifications listed in unit 04 INPUTS.md. Abstract geometry and formal conditional implications are distinct from identification with the actual HM module or retained source. Historical words such as “new,” “remaining,” or “previously verified” describe the source manuscript, not a claim about the current research frontier.

# Structural bounds on the quadruple-root conductor correction

## Result

Let F be the normalized Horrocks–Mumford bundle on Y=P⁴, B=End₀(F), and C≅P¹ the rational normal quartic of quadruple roots. Let ν:S=P¹×P¹→N be the normalization of the reduced triple-root (2,3) complete intersection, with diagonal Δ mapping isomorphically onto C. All degrees on C below refer to O_P¹(1), not O_Y(1)|C=O_P¹(4).

Without evaluating the monad maps, there is an integer a with −2≤a≤8 such that

    F|C ≅ O(a) ⊕ O(−4−a),
    B|C ≅ O ⊕ O(d) ⊕ O(−d),  d=2a+4∈{0,2,…,20}.

Put G_t=ν*(B(t)|N)=ν*B⊗O_S(3t,t), and Q_t=B|C⊗O_P¹(4t−2). For t≥1,

    h¹(Q_t)=max(d−4t+1,0) ≤ max(21−4t,0).

The canonical normalization pullback on H² is surjective, and

    ker[H²(N,B(t)|N)→H²(S,G_t)]
      ≅ coker[H¹(S,G_t)→H¹(C,Q_t)].

Thus this kernel has dimension at most 5 for t=4, at most 1 for t=5, and is zero for every t≥6. No splitting type or map rank has been evaluated.

The fourth-power boundary domain is still ker D₄, where

    D₄:H⁰(S,G₄)→H⁰(C,Q₄),
    dim H⁰(C,Q₄)=45+h¹(Q₄)∈{45,46,48,50}.

Consequently descent cuts out a subspace of codimension at most 50 in the normalized section space. This is not a claim of surjectivity of D₄ or of the fourth-power boundary.

IMPORTANT: the bound 5 is a positive-twist (+4) H² comparison bound. The fourth-power obstruction restriction is at twist −4. Its conductor H¹ has dimension 51, 52, or 54. No bound 5 on the fourth-power image follows.

## 1. Restricting the monad is exact

The normalized HM monad is

    5O_Y(−1) → 2Ω²_Y(2) → 5O_Y.

The verified primary source and normalization are recorded in ../effective-collision-bound/PROOF.md, §1 (Boralevi, equation (1.1), https://arxiv.org/pdf/math/0602002).

Write K_Y for the kernel of its right arrow. There are exact sequences of vector bundles

    0→K_Y→2Ω²_Y(2)→5O_Y→0,
    0→5O_Y(−1)→K_Y→F→0.

Each sequence is locally split, because its quotient is locally free. Tensoring with O_C is therefore exact; equivalently the relevant Tor₁ groups vanish. In particular the restricted middle cohomology is precisely F|C. Merely restricting an arbitrary three-term complex would not justify this claim; the two locally free quotients do.

The Euler sequence restricts to

    0→Ω¹_Y(1)|C→5O_C→O_C(4)→0.

The five sections are the complete degree-four linear system defining the rational normal curve. The induced map on H⁰ is an isomorphism. Its kernel bundle E has rank four, degree −4, and H⁰(E)=0. By splitting on P¹, every summand has degree at most −1; their sum −4 forces E=O(−1)^4. Taking exterior squares gives

    Ω²_Y(2)|C=Λ²E=O(−2)^6.

Thus, writing K=K_Y|C, the restricted monad sequences are

    0→K→O(−2)^12→O^5→0,
    0→O(−4)^5→K→F|C→0.                 (1)

No matrices of the HM monad are chosen or inspected.

## 2. Splitting bounds from subbundle, quotient, and determinant

The first sequence gives rk K=7 and deg K=−24. Write K=⊕_{i=1}^7 O(b_i). Each b_i≤−2: otherwise the restriction of the injection K→O(−2)^12 to that summand would be zero, since Hom(O(b_i),O(−2))=0. For each i,

    b_i=−24−Σ_{j≠i}b_j ≥−24+12=−12.

Hence K(12) is globally generated. The second sequence makes F|C(12) a quotient of a globally generated bundle, so it is globally generated too. Both splitting degrees of F|C are therefore ≥−12.

The determinant of F is O_Y(−1), so deg F|C=−4. Order its two summands as O(a),O(−4−a), with a≥−4−a. This yields a≥−2; the lower bound −4−a≥−12 yields a≤8. The tracefree endomorphism splitting is then

    End₀(F|C)=O⊕O(2a+4)⊕O(−2a−4).

Tracefree endomorphisms commute with restriction because characteristic is zero and the trace decomposition is split. The displayed splitting is an isomorphism type; no canonical choice of its summands is asserted.

## 3. Exact conductor dimensions and H² comparison

The normalization/conductor proof in ../nullcone-normalization/PROOF.md establishes

    0→B(t)|N→ν_*G_t→j_*Q_t→0,          (2)

with Q_t=B|C(4t−2), where j:C→N. Thus

    Q_t=O(4t−2)⊕O(4t−2+d)⊕O(4t−2−d).

On P¹, h¹(O(n))=max(−n−1,0). For t≥1 the first two summands have no H¹, proving the formula in the Result. Specifically:

    t=4: h¹(Q₄)=max(d−15,0)∈{0,1,3,5};
    t=5: h¹(Q₅)=max(d−19,0)∈{0,1};
    t≥6: h¹(Q_t)=0.

Because ν is finite, its higher direct images vanish. Because Q_t is supported on a curve, H²(C,Q_t)=0. The tail of the long exact sequence of (2) is therefore

    H¹(S,G_t)→H¹(C,Q_t)→H²(N,B(t)|N)
      →H²(S,G_t)→0.

This proves the stated exact kernel formula, not merely a dimension inequality. It also proves the isomorphism for t≥6. For t=4 or 5 the possible nonzero conductor H¹ can be killed by the preceding map, so the upper bounds need not be attained.

At t=4, χ(Q₄)=3(14+1)=45, hence h⁰(Q₄)=45+h¹(Q₄). At t=5 the corresponding value is h⁰(Q₅)=57+h¹(Q₅)≤58. For t≥6 one has h⁰(Q_t)=12t−3.

## 4. Fourth-boundary domain and what the bounds do not imply

The first part of (2) on global sections identifies H⁰(N,B(4)|N) canonically with ker D₄. Here D₄ is the intrinsic normal-derivative map induced by normalization; it is not an arbitrary directional derivative. Since its target has dimension at most 50,

    codim[ker D₄ ⊂ H⁰(S,G₄)]≤50.

Its target dimension is not its rank. In particular h¹(Q₄)≤5 does not reduce the descent condition to five equations: the H⁰ target has at least 45 dimensions. Nor does vanishing of H¹(Q_t) imply surjectivity of D_t; the obstruction to the latter lies at the earlier H¹(N,B(t)|N) term.

The exact previously established fourth-power criterion remains

    δ̃_N:ker D₄→H²(Y,B(−1)),
    im[H²(Y,B(−4)I_N)→H²(Y,B(−4))]=(im δ̃_N)^⊥.

Neither δ̃_N nor D₄ has been evaluated. Their domain and target descriptions alone do not establish first-ten vanishing, nonvanishing, or the rank of either map.

To make the twist distinction explicit, the dual restriction entering this criterion is H²(Y,B(−4))→H²(N,B(−4)|N), not the +4 comparison above. At t=−4,

    Q_{−4}=O(−18)⊕O(d−18)⊕O(−d−18),
    h⁰(Q_{−4})=max(d−17,0)∈{0,1,3},
    h¹(Q_{−4})=51+h⁰(Q_{−4})∈{51,52,54}.

Thus the same formal comparison only bounds its H² kernel by at most 54, which is not useful for forcing vanishing of a ten-dimensional ambient image. Serre duality cannot silently exchange these two conductor bounds: the dual normalization comparison includes the dualizing/conductor correction.

## 5. A guaranteed descending subspace

There is also a useful map-independent subspace of the fourth-boundary domain:

    H⁰(S,G₄(−2Δ))=H⁰(S,ν*B⊗O_S(10,2)) ⊂ ker D₄.

Indeed I_{C/N}O_S=O_S(−2Δ), and the conductor ideal identifies I_{C/N}=ν_*O_S(−2Δ) as O_N-modules. Projection formula therefore gives

    B(4)|N⊗I_{C/N} ≅ ν_*(G₄(−2Δ)).

The inclusion is the natural inclusion into sections of B(4)|N. In the local cusp model A=C[s,d²,d³]⊂C[s,d], sections divisible by d² already descend, so this also follows directly from the derivative criterion.

The exact sequence with C gives

    0→H⁰(S,G₄(−2Δ))→ker D₄→H⁰(C,B|C(16)).

The last arrow need not be surjective. Its target has h⁰=51+max(d−17,0)≤54. Thus the fourth-boundary domain modulo its guaranteed order-two descending subspace has dimension at most 54. This does not determine the boundary on that subspace or on its quotient.

## 6. Sharpness of the restricted-monad bound

The interval a≤8 cannot be improved from the restricted exact-bundle monad and symplectic self-duality alone. The complete degree-five evaluation sequence on P¹ has kernel O(−1)^5 by the same argument as in §1. Pull it back along any degree-two morphism P¹→P¹ and twist by O(−2), obtaining

    0→A=O(−4)^5→E=O(−2)^6→L=O(8)→0.

Dualize and twist by T=O(−4):

    0→L∨⊗T=O(−12)→E∨⊗T=O(−2)^6→A∨⊗T=O^5→0.

On the hyperbolic T-valued symplectic bundle M=E⊕(E∨⊗T), include A into the first summand and project the second summand onto A∨⊗T. These are adjoint monad arrows with zero composite. Their middle cohomology is

    L⊕(L∨⊗T)=O(8)⊕O(−12).

This conceptual construction evaluates no selected matrix, rank, or polynomial instance. It proves sharpness for the restricted monad package, including its natural symplectic self-duality. It does not assert that this abstract monad extends to the HM monad on P⁴, that this is its actual splitting on C, or that the H² comparison kernel attains dimension 5. Further improvement would require additional global or HM-specific input. The independent derivation is in AUDIT.md §6.

## Scope and provenance

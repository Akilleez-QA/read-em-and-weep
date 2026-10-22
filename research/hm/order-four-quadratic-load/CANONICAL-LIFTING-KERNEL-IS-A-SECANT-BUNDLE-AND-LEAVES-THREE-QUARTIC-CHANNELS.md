# The canonical lifting kernel is a secant bundle and leaves three quartic channels

## Status, dependencies, and scope

This is a new deduction, not an evaluation of the fourth obstruction. It uses the nonzero canonical factorization and fixed equivariant identification proved in ACTUAL-CANONICAL-RAW-CUBIC-HAS-A-NONZERO-LINEAR-LIFTING-CORRECTION.md. That actual-map comparison is a dependency; the new arguments here establish the kernel geometry and the exact restriction of quartic channels.

Write X=P(A), A=Sym²W, and D=D5_positive. Fix the actual nonzero equivariant isomorphism J:D→Sym⁴W from that dependency. There is a nonzero scalar γ, not assigned a numerical value, such that

    L_can(a,h)=γ(a,Jh)₂.

Twisting its linear family gives the surjection L_can:D O_X→A O_X(1). Define K=ker(L_can). The target of the quartic gate after twisting is I_Σ(10), where the actual second-symbol resolution is

    0→A O_X(-2)→P4 O_X→I_Σ(6)→0.

All coordinate calculations below concern universal binary forms and abstract representations. No actual coefficient, selected actual direction, source-instance matrix, or rank experiment is used.

## 1. Apolar root convention and the two kernel fibers

Fix a nonzero alternating form on W. We use P(W) for lines in W. A binary quadratic a is interpreted as the section of O_P(W)(2) whose value at a vector v is proportional to the apolar pairing (a,v²)₂. In this convention, if a=ℓm, its zero divisor is [ℓ]+[m]. If instead one regards a as an ordinary polynomial function on W*, its zeros live in P(W*); the alternating form must first identify these points with P(W). This distinction prevents an unannounced opposite-root replacement.

For independent ℓ,m, put a=ℓm. The second transvectant is, up to a nonzero scalar, mixed differentiation in the universal basis ℓ,m. On Sym⁴W its kernel is exactly

    ker(a,-)₂=span(ℓ⁴,m⁴).

For a=ℓ², extend ℓ to a basis ℓ,m. The map is, up to a nonzero scalar, the second m derivative, and hence

    ker(ℓ²,-)₂=ℓ³W.

Both maps are onto Sym²W: in the first case the other three quartic monomials map to the three quadratic monomials, and in the second case the monomials with m-exponent 2,3,4 do so. Every nonzero binary quadratic is in one of these two universal orbit types. These are symbolic normal-form arguments, not evaluations at chosen actual points. In the actual source the displayed kernels must be pulled back by J⁻¹; no coefficient-basis identification D=Sym⁴W is implicit.

Thus K is a rank-two vector bundle everywhere on X, including the six axes Σ, and

    0→K→D O_X --L_can→ A O_X(1)→0.               (1)

The degeneracy of the second symbol at Σ does not cause a degeneracy of L_can.

## 2. Intrinsic secant/evaluation bundle

Let Z⊂P(W)×X be the universal degree-two divisor in the apolar convention above, and p:Z→X its finite flat degree-two projection. Put

    E=p_*(O_P(W)(4)|Z).

This is the rank-two tautological evaluation bundle of O(4) on length-two divisors. The universal-divisor sequence, twisted by O_P(W)(4), and H¹(P¹,O(2))=0 give

    0→Sym²W O_X(-1) --multiply a→ Sym⁴W O_X→E→0,

where the spaces of sections are identified with symmetric powers using the alternating form. Dualizing, and using invariant apolar pairings, identifies the transpose of multiplication by a with a nonzero constant multiple of (a,-)₂. Therefore

    K ≅ E*,

with the ambient embedding transported through J. This also explains the secant span for two distinct points and the tangent span ℓ³W for a double point, without choosing a factorization globally.

Let H=c1(O_X(1)). Equation (1) gives

    c(K)=(1+H)^(-3)=1-3H+6H²,
    c1(K)=-3H,  c2(K)=6H²,
    c1(K(1))=-H,  c2(K(1))=4H².

There is also a useful uniform square restriction. For the Veronese map ν:P(W)→X, [ℓ]↦[ℓ²], multiplication gives an injection

    O_P(W)(-3)⊗W→Sym⁴W O_P(W),  ℓ³⊗w↦ℓ³w.

Its image is the fiberwise kernel above, so

    ν*K ≅ W⊗O_P(W)(-3).

This statement uses degree on P(W); ν*O_X(1)=O_P(W)(2).

## 3. Exactly one invisible quartic channel

Set F=I_Σ(10). The already established quartic channel computation is

    H⁰(F)=1+A+2V+3P4+4D,
    dim Hom_G(D,H⁰(F))=4.

Twisting the second-symbol resolution by three gives

    0→A O_X(1)→P4 O_X(3)→I_Σ(9)→0.              (2)

The usual line-bundle cohomology on P² gives H¹(O(3))=H²(O(1))=0; hence H¹(I_Σ(9))=0. On global sections (2) yields the exact character identity

    H⁰(I_Σ(9))=P4⊗Sym³A - A⊗A
              =A+2V+3P4+2D,                      (3)

of dimension 31. In particular its A multiplicity is exactly one.

Apply Hom_X(-,F) to (1). Because A O(1) is locally free,

    Ext¹_X(A O(1),F)=A*⊗H¹(I_Σ(9))=0.

Taking G invariants remains exact in characteristic zero. Consequently there is an exact sequence

    0→Hom_G(A,H⁰(I_Σ(9)))
      →Hom_G(D,H⁰(I_Σ(10)))
      →Hom_G(K,I_Σ(10))→0.                        (4)

The first arrow sends M to M∘L_can. It is injective because L_can is a surjection of sheaves. Thus the dimensions in (4) are exactly

    1 → 4 → 3.

Equivalently, a quartic family vanishes on K if and only if it factors uniquely through L_can, and the equivariant space of such invisible families is one-dimensional. Every equivariant sheaf map K→I_Σ(10) extends to a quartic family; the extension ambiguity is precisely that one-dimensional channel. This is stronger than an upper bound on restricted channels and does not require a canonical splitting of (4).

## 4. What this does and does not do for the actual fourth gate

In a fixed Schur reduction COMPATIBLE with the canonical raw cubic, the fourth representative is

    B4|D - B3|A L_can.

Its restriction to K(-4) is represented simply by B4|K(-4), since L_can vanishes there. Its class is a member of the three-dimensional space in (4). Thus the known nonzero third lifting correction geometrically removes one quartic channel from this rank-two-input test.

This restriction does not determine the actual fourth value. Even vanishing of the entire restricted gate would leave the one-dimensional factoring possibility on D; conversely a nonzero restricted value would prove a nonzero full fourth gate. Neither assertion about the actual restricted value is proved here. An arbitrary Schur gauge must be compared to the canonical probes before replacing its L by L_can. The secant description concerns the fixed J, not an independent choice of actual positive-source coefficients.

## Reproduction

Run python verify_canonical_lifting_kernel_secant_channels.py. It checks symbolic binary-form identities, the adjoint multiplication identity, universal kernel monomial formulas, the Chern computations, and exact finite-group characters. It uses no actual specialization or actual-instance matrix/rank calculation. The geometric dependency and the sheaf cohomology arguments remain explicit in the proof above.

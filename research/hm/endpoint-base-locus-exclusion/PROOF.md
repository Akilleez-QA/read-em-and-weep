# Every direction detects the entire quadratic endpoint family

## Assumptions and source interface

Work over C. Let G=SL2(F5); W is the binary two-dimensional representation; the channel modules A, D and P below descend to A5. Set A=Sym²W, D=Sym⁴W=Sym²_0 A, and let P be the irreducible endpoint module P4. The invariant nondegenerate symmetric form on A identifies A with its dual. Write X=P(A), M=Hom(D_source,P), and

Q=Hom_G(D_source,P⊗Sym² A*).

The pinned endpoint-family input is `LOWER-FAMILY-IS-DETERMINED-BY-SECANT-RESTRICTION-AND-TRACE.md` at c9c54d50c94fc17cad7a14fce93b31bb22b9ea5f in research/hm/order-four-quadratic-load, and the additional square-fiber input is PR661 `research/hm/endpoint-square-reconstruction/PROOF.md` at 1325647fd916bf2daa71b11efeae6d52cfefa2cd. This proof is conditional on their actual canonical endpoint identification, not a reproof of the HM foundation.

The representation identities are

Sym² A = 1⊕D,       M=A⊕V⊕P⊕2D.

Consequently M^G=0, dim Q=2, and polarization identifies

Q ≅ Hom_G(D_parameter,M).

Under this identification, an endpoint family q corresponds to T_q and satisfies

q(a,−)=T_q(v_a),       v_a=(a⊗a)_0.

This is PR661 equation (1), now used for arbitrary directions rather than just squares. No actual endpoint coefficients are specified.

## 1. Root-cause exclusion of every whole-fiber zero

**Theorem.** For every nonzero q in Q and every nonzero a in A, the entire linear map q(a,−):D_source→P is nonzero. Equivalently, evaluation at each point of P(A) is injective on Q (with its natural O(2) fiber).

**Proof.** Since D_parameter is irreducible, the kernel of a nonzero equivariant map T_q:D_parameter→M is zero. It remains only to prove v_a≠0.

Using the invariant form, write the rank-one symmetric endomorphism a⊗a as a a^t. If v_a=0, then

a a^t = ((a,a)/3) I_A.

The left side has rank one for a≠0, even when a is isotropic: the nonzero functional (a,−) has rank one. The right side has rank zero or three. This is impossible. Thus v_a≠0, and injectivity of T_q proves T_q(v_a)≠0. ∎

This excludes the entire parameter base locus at its source. It requires neither a generic matrix argument, orbit counts, divisor classification, Bézout, nor selected HM calculations. It is stronger than saying a generic endpoint family has no base point: *every* nonzero family has no whole-fiber zero, in *every* direction.

For each fixed a, if evaluation had a nonzero kernel vector q, it would contradict the theorem. Thus the evaluation map on the two-dimensional family space has rank exactly two at every direction.

## 2. Bundle form and uniform reconstruction

The universal evaluation morphism is

Q⊗O_X → M⊗O_X(2).

It is a rank-two subbundle injection and has locally free cokernel of rank18. Indeed its fiber rank is two everywhere, so around any point a nonvanishing 2×2 minor allows elementary changes of local frames identifying it with a direct summand inclusion. This also excludes scheme-theoretic rank-drop points: the maximal-minor ideal is the unit ideal locally everywhere.

Let M_D denote the canonical D-isotypic part of M. The canonical evaluation isomorphism

D⊗Q → M_D,       d⊗T ↦ T(d)

is an isomorphism because D is irreducible, its multiplicity in M is two, and the other isotypic parts are absent from its image. Under it, the twisted form of the bundle map is exactly

O_X(−2)⊗Q → D⊗Q⊗O_X,

given by the line v_a in D. Let R be the rank-four vector bundle defined by

0 → O_X(−2) → D⊗O_X → R → 0.

Then the cokernel inside M_D⊗O_X is R⊗Q. In the full M⊗O_X the cokernel is canonically (R⊗Q)⊕(M_non-D⊗O_X), where the second summand has rank10. Untwisting gives the cokernel in the first display.

In particular, after choosing a representative a and any linear functional λ on D with λ(v_a)=1, the whole family T is recovered from its compatible full fiber f=T(v_a) by

T = (λ⊗id_Q)(f) in the canonical identification M_D=D⊗Q.

Here the right side is interpreted as the member of Q itself, and its associated equivariant map is the required T. Compatibility means f lies in the two-plane Cv_a⊗Q, not merely somewhere in M_D. Every direction therefore provides a two-dimensional minimal full-fiber certificate for vanishing of the endpoint family. This statement is about full maps D_source→P, not their secant restriction.

## 3. Next structural step: a closed-embedded universal endpoint surface family

The map

ν_0:P(A)→P(D),       [a]↦[(a⊗a)_0]

is a closed immersion. It is the quadratic Veronese embedding into P(Sym²A), projected from the point of the inverse metric. That point has rank three. Every secant or tangent line to the Veronese surface consists of symmetric tensors of rank at most two, so the center belongs to none of them. Hence this projection separates points and tangent vectors, and is a closed immersion.

For completeness, point separation follows directly: if v_b=c v_a, c≠0, then b b^t−c a a^t is scalar I. Its rank is at most two, so the scalar is zero. Equality of the nonzero rank-one tensors implies [b]=[a]. For tangent separation, a representative tangent vector b gives derivative a b^t+b a^t. If its trace-free part is a scalar multiple c v_a, then a b^t+b a^t−c a a^t is scalar I and has rank at most two, so that scalar vanishes. In a basis starting with a, the resulting symmetric-tensor equality implies b=(c/2)a, the zero projective tangent vector. Properness together with separation of points and tangent vectors over C yields the claimed closed immersion.

Each nonzero family q therefore has projectivized full-fiber image a smooth degree-four surface in the projective four-space P(im T_q) inside P(M). This is a projection of the Veronese surface, not a claim about the rank of the maps D_source→P at its points.

More uniformly, under M_D=D⊗Q the universal map is

P(A)×P(Q) → P(M_D),       ([a],[q])↦[v_a⊗q].

It is the product of ν_0 with the identity, followed by Segre, hence a closed immersion. Its pullback hyperplane bundle is O(2,1). Its image is a smooth threefold in P9 with degree

∫_(P²×P¹) (2h+k)^3 = 12.

Thus no two distinct pairs (parameter direction, projective endpoint family) have proportional nonzero full endpoint maps. Both the direction and the projective family are intrinsically recoverable from a compatible nonzero full map. This conclusion is stronger than fixed-direction injectivity and follows without identifying the actual family.

## 4. Exact limits and relation to square secant certificates

PR661 proves the stronger *restricted-fiber* statement q(a,−)|K_a≠0 for every nonzero square a. The present theorem extends detection to every direction only for the **full** D_source→P map. It does not assert injectivity of Q→Hom(K_a,P) at arbitrary nonsquare directions, nor imply a particular rank for q(a,−).

For this last observation use the pinned secant-bundle input: K is the globally defined G-equivariant rank-two subbundle in 0→K→D_source⊗O_X→A⊗O_X(1)→0, with fiber K_a. A rigorous partial observation is available: the rank-drop locus of the restricted evaluation Q O_X→K*⊗P O_X(2) is closed, G-invariant, and disjoint from the square conic by PR661. Consequently it is empty or zero-dimensional, since every projective curve in P² intersects the conic. This does not exclude a finite exceptional set off the conic, and is not promoted to an all-direction secant theorem here.

No actual HM/source coefficient or matrix, source-instance rank, endpoint value, next ambient division, fourth obstruction, Smith bound, section count, prescribed-source membership, complete repair, higher lifting, or algebraicity has been evaluated or settled.

# Intrinsic bundle of the six middle-two-zero embedded classes

## Statement

Retain the hypotheses of PROOF.md. Let B⊂P(V) be the rank-ten open of common lines, and let

    S={u∈V\{0} : [u]∈B},
    π:S→B,
    i:S→X,    u↦(0,u,0).

All statements concern the open part of X where the middle input y belongs to S. Write I_S for the ideal of its middle-two-zero center. Then the intrinsic center-supported torsion sheaf is

    H⁰_{I_S}(O_X) ≅ i_* Λ²((V⊗O_S)/(O_S·u))^*
                  ≅ i_* π^*(Ω²_{P(V)}(2)|_B).

It has rank six over S, is annihilated by I_S, and has outer-input bidegree (1,1), or triple-input weight (1,0,1). These statements identify the intrinsic embedded torsion, not a selected nonunique embedded primary component.

## 1. Canonical construction without choosing a complement

Let

    E=ann(u)=ker(V^*⊗O_S → O_S),    α↦α(u).

Since u is nowhere zero on S, E is locally free of rank four and canonically equals ((V⊗O_S)/(O_S·u))^*. For local sections α,β of E define the function class

    θ(α∧β)=1/2 [α(x)β(z)−β(x)α(z)] ∈ O_X.

Here α and β may have regular coefficients in the middle input u=y. Their coefficients are pulled back from S along the middle-input projection. The displayed expression is alternating and O_S-bilinear, so it defines a canonical sheaf map from Λ²E. It involves only x,z and covectors annihilating the actual middle-input coordinate; no complement, functional ell, normalization of u, or numerical evaluation is chosen.

## 2. Comparison with the six-class local basis

On any local complement chart from PROOF.md, write

    x=a u+p,    z=c u+q.

Because α(u)=β(u)=0, the canonical formula becomes

    θ(α∧β)=1/2 [α(p)β(q)−β(p)α(q)].

The full local ideal contains every symmetric cross expression, hence

    α(p)β(q)+β(p)α(q)=0.

Consequently θ(α∧β)=α(p)β(q) in O_X. If α_1,…,α_4 is the frame of E dual to the chosen frame of H, then

    θ(α_i∧α_j)=p_iq_j    (i<j).

These are precisely the six independent classes proved in PROOF.md to form H⁰_{I_S}(O_X). They are annihilated by all outer-input coordinates a,c,p,q, which generate I_S in this chart. Thus θ lands in the center-supported torsion and is an isomorphism on every local frame.

The defining formula for θ is independent of all such choices. Its local isomorphisms therefore glue to the claimed canonical global isomorphism. In particular no choice of primary decomposition is involved in the gluing.

## 3. Projective identification and weights

On P(V), let O(−1) be the tautological line bundle and let Q_V=(V⊗O)/O(−1) be the universal quotient bundle. The dual Euler sequence identifies

    Q_V^* ≅ Ω¹_{P(V)}(1).

Pulling back to S gives E≅π^*Q_V^*. Taking the second exterior power gives

    Λ²E≅π^*Ω²_{P(V)}(2).

Under substitution (x,y,z)↦(s x,t y,r z), with s,t,r nonzero, the annihilator ann(tu) is canonically the same subspace as ann(u). The displayed quadratic generator acquires the factor sr. In this substitution convention it has triple-input weight (1,0,1). The middle scaling carries no additional weight, so the bundle descends under the scalar quotient S→B to Ω²_{P(V)}(2)|_B with the indicated outer weights.

The rank-ten hypothesis is used to prove that θ is an isomorphism onto all center-supported torsion. The canonical alternating expression itself exists without choosing a rank instance. This argument does not extend the full-X classification to the other two-zero positions or to rank-drop lines.

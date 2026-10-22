# 14. Conditional square-gate osculation and vertex geometry

**Current status.** [Section 15](15-third-vanishing-and-fourth-frontier.md) proves the actual square third channel zero. Section 14.1 preserves a valid conditional theorem with an excluded antecedent, not a degree-eighteen curve constructed from the actual gate. The local vertex calculation remains unconditional.

## 14.1 A degree-eighteen series, conditional on a nonzero square channel

Let Δ=P(W) be the discriminant conic under the quadratic Veronese Δ→P(A). Here O_Δ(1) means O_(P(W))(1), not the plane hyperplane restriction. The second symbol has rank three everywhere on Δ, and the actual third gate restricts to

    b: D5 O_Δ → O_Δ(18).

The already established square-channel space is one-dimensional. If b is nonzero, its five sections are independent and basepoint-free: a common invariant divisor would have degree twelve, leaving a forbidden D5 inside Sym⁶W=V⊕P4. The [osculation theorem][O] gives the further consequences below **only under b≠0**. It does not evaluate b.

Write B₂,B₃,B₅ for the reduced projective-stabilizer orbits of lengths thirty, twenty and twelve. The nonzero Wronskian has degree 5·18−20=70. The unique invariant orbit partition of this degree gives

    Ram(b)=B₂+2B₃,
    Wr(b)=c T₃₀ H₂₀²,        c≠0,

where the invariant forms are defined by their reduced zero divisors. The exact vanishing sequences are

    B₂:       (0,1,2,3,5),
    B₃:       (0,1,2,4,5),
    elsewhere: (0,1,2,3,4).

At B₃ the other weight-two possibility (0,1,2,3,6) has the wrong multiplicities modulo three for the stabilizer action on D5. In particular a₁=1 everywhere, so the map to P(D5*) is immersive. Factoring through its image normalization and applying Riemann–Hurwitz shows it is birational onto a nondegenerate rational curve of degree eighteen. It need not be an embedding: distinct points could still have the same image.

All five vanishing orders are at most five, so the fifth-principal-parts evaluation is a subbundle injection with line quotient:

    0 → D5 O_Δ → J⁵(O_Δ(18)) → O_Δ(78) → 0.

The quotient degree is 18+16+14+12+10+8=78. Any independently established excess ramification, basepoint or failure of immersion would therefore force b=0. No such osculation contradiction is supplied here. Instead Section 15 proves b=0 by the actual cup calculation and basepoint argument, and separately kills the discriminant-divisible channel. Later Bocksteins remain open. Compare the conditional plane fixed-divisor classification in [Section 12.7](12-harmonic-cochain-and-family-gate.md#127-conditional-fixed-divisor-classification-for-a-nonzero-third-gate).

## 14.2 The vertex double point contributes no missing local term

For a nonzero square a=ℓ² and t≠0, Q=(q₀+tℓ²=0) is an integral rank-four quadric. Its intersection with the distinguished jumping line L is the length-two scheme 2p at its vertex, not two reduced points. In local coordinates its ring is the three-dimensional Cohen–Macaulay ring defined by q₀(x)+tz²; the transverse line ideal (x₁,x₂,x₃) has quotient C[z]/(z²). These three generators are consequently a regular sequence.

Thus restriction of the actual evaluation Koszul resolution stays exact at the vertex. There is no extra Tor or local Koszul-homology term from the singularity alone. Where the quadric meets all twenty-five lines properly, the actual fifty-point resolution and dual cubic-restriction map remain valid, using 2p and its dualizing line. Its evaluation-tail contribution has involution trace −2, as for the two reduced fixed marks in the smooth calculation. The positive index remains

    h⁰(B_Q(4))₊−h¹(B_Q(4))₊=4.

This does not decide whether there is a fifth section. The missing question is a global lift boundary, not an omitted node contribution.

## 14.3 Why a general-cone argument cannot be imported

Inversion has determinant −1 on the nondegenerate four-space at this vertex and exchanges the two cone rulings, hence the two small resolutions. A calculation on a single ruling is not automatically a positive-parity calculation. The vertex is also constrained to the distinguished jumping line, so generic-translate avoidance results for general cones do not apply without a new argument.

Moreover every cone in this square family is inversion-even and has positive index four. A general full-adjoint balancedness statement cannot replace the desired vanishing of h¹(B_Q(4))₊. The osculation constraints, node calculation and unchanged index alone do not decide the third value. Its later vanishing still leaves the four-or-five alternative open.

## Pinned source reference

[O]: https://github.com/Akilleez-QA/read-em-and-weep/blob/15adb8e5ea61f07e87df6a0044b7375e580fe7f3/research/hm/order-four-quadratic-load/ACTUAL-SQUARE-THIRD-GATE-HAS-FORCED-ICOSAHEDRAL-OSCULATION.md

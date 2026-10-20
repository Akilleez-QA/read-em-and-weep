# Generic quadratic multiplication and order six

For any complex graded polynomial-ring module generated in degree
zero with dim M_3=2, multiplication M_1 -> M_3 by a general
quadratic is surjective.

The [complete proof](PROOF.md) gives an elementary rank-one-space
argument, then uses commutativity to exclude its common-kernel
case. The primary HM resolution verifies degree-zero generation,
so this theorem applies to the fixed module H^1_*(F). Naturality
then proves that a general quadratic also surjects
H^1(End_0(F)(4)) -> H^1(End_0(F)(6)).

The binary-quartic invariant t_2 is a nondegenerate quadratic.
Consequently a nonempty Zariski-open family of target-projective
translates q_g=g o q_0 has

    H^2(Z,I_D^6 E_g)_chi = 0,
    E_g = q_g^*End_0(F) tensor (q_g^*O(1))^(-2).

F remains fixed; its pullback coefficient varies with q_g.
This lowers whole-coefficient vanishing to order six for generic
relative position. It does not say that projective transformations
preserve HM, or that the original fixed t_2 is good. The original
Q(t_2,t_3), actual source membership, pure conditions, module
lifting and algebraicity remain unresolved.

All primary dependencies have immutable public pins in the proof.
No selected HM/source evaluation, matrix construction, random
sample, checker, or large computation was performed.

# Type VI: a two-scalar sufficient condition for residual injectivity

Use the actual pure map j:S7* -> K8, its coherent cokernel Q6, and its divided pure cross-block section T2 in H0(F4 external-tensor O(6))^G. Assume the target splitting is type VI:

F4 = O direct-sum (W-prime tensor O(5)) direct-sum O(14).

The three summands have invariant coupling dimensions 0, 1, 2. Their diagonal restriction spaces have invariant dimensions 0, 0, 1. Thus write T2=(0,mu L0,H), where L0 is a fixed nonzero generator of the one-dimensional low coupling space. The vanishing or nonvanishing of mu is independent of the generator. Let lambda denote the leading diagonal scalar, which comes solely from H. No value of either actual scalar is determined here.

The necessary common-divisor enumeration from THREE-TARGET-TYPES-WITHOUT-OFF-DIAGONAL-TORSION.md leaves exactly bidegrees (10,2) and (14,6) in this type. If a nonempty common-zero divisor away from the diagonal exists, divide T2 by its defining section. The low component would belong to H0(W-prime tensor O(5-p) external-tensor O(6-q)). For either candidate p>5, this space is zero. Therefore such a divisor forces mu=0.

Consequently mu nonzero rules out all off-discriminant divisorial torsion in Q6. Independently, lambda nonzero gives generic fiber injectivity of j on the discriminant by the actual Hermite calculation, including the pure source derivative correction, in the preceding proof and verify_pure_hermite_boundary.py. Hence lambda mu nonzero implies Q6 has no divisorial torsion anywhere.

If the residual map had generic rank two, its kernel would embed in S5* with a nonzero divisorial quotient of degree d-4 at least 2, supported in Q6. This contradicts absence of divisorial torsion. Thus, conditional on type VI,

lambda mu nonzero implies residual generic rank four.

Equivalently the rank-two alternative implies lambda mu=0. This note alone gives a necessary algebraic condition for rank two. The separate SCALAR-TARGET-SATURATION-AND-NORM-TORSION.md proves the stronger fact that mu=0 is sufficient for residual rank two, because the entire residual map then factors through S15. No sufficiency is asserted for lambda=0 alone. Isolated fiber degeneracies remain allowed. Types IV and VII are outside this note.

Reproduce the exact universal representation and bidegree checks with python verify_type_six_two_scalar_gate.py. This script imports the stable character verifier and does not inspect actual coefficients or compute actual ranks.

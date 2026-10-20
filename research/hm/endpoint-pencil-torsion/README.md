# Bounded endpoint specialization along a quadratic pencil

Choose existentially a good quadratic q_1 from PR441 and retain
the fixed original u_0=t_2, v_0=t_3. The pencil u_0+tq_1 has a
primary cokernel R that is a quotient of a length-two C[t]-module.
A monic quadratic f annihilates R.

PR440's natural section-resolution comparison makes the endpoint
cokernel Q_A a quotient of fifteen copies of R. Thus its total
length is at most 30, its support has at most two points, and a
local parameter has nilpotence exponent at most two. Right-exact
cokernel base change identifies Q_A/tQ_A with the exact original
Q(u_0,v_0).

The complete proof is in PROOF.md. Its optional final construction
uses a formal square root to realize the quadratic pencil by
target automorphisms through the identity, transforms the cubic
accordingly, and obtains generic whole-coefficient order-six
vanishing with the original special fiber. The explicit quotient
module is determined by the first jet in the auxiliary translation
parameter, but is not identified with a relative higher direct image.

This refines the generic result quantitatively but does not
evaluate the original Q or prove that it vanishes. No actual
HM/source-instance evaluation or large computation is performed.

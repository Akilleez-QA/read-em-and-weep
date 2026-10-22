# The midpoint first-normal extension has a unique square-zero adjoint lift

## New deduction

Use the two distinct formal-extension points supplied by the Serre-residue double-cover theorem and their midpoint m in the first-normal affine line. The invariant nilpotent section N of B_Q(2) has a UNIQUE invariant trace-free lift N_tilde to the adjoint of the midpoint bundle on 2Q. This lift satisfies

    N_tilde^2=0.

Moreover the actual adjoint bracket

    H1(B_Q(-2))^G tensor C N -> H1(B_Q)^G

is nonzero, hence an isomorphism between the two invariant lines after choosing N.

No flatness of ker N_tilde or im N_tilde, and no spinor-line lift to 2Q, is asserted. The midpoint does not extend to 3Q: its exact scalar obstruction equals -c^2/(4d), which is nonzero by the earlier theorems.

## Proof

The finite block transformation phi with negative-block scalar mu^2=-1 exchanges the two extendable points and acts on the affine normal line by s -> s_*-s. The Serre comparison gives N eigenvalue -1.

The line H1(B_Q)^G has eigenvalue +1. Indeed the actual projective-orbit tangent map sl5 -> H1(B) is an isomorphism. Its invariant block-Euler vector field D0 commutes with phi and is tangent to Q. The restriction of its Atiyah class is nonzero: the invariant restriction map H1(B)^G -> H1(B_Q)^G is an isomorphism by the two negative-monad vanishings. Naturality of Atiyah classes therefore fixes this invariant line under phi. This argument does not identify the two ambient normalizations of the boundary of N.

For each first-normal extension e, let delta_e be its boundary

    H0(B_Q(2))^G -> H1(B_Q)^G.

Its dependence on e is affine, with linear variation [eta,N], up to the fixed sign convention for adjoint transitions. Naturality and the eigenvalues just computed give

    delta_(J e)(N)=-delta_e(N).

At the fixed midpoint, this boundary is zero. Thus N lifts. The kernel governing choices is H0(B_Q)^G=0, so its invariant trace-free lift is unique. On the actual ambient endpoint, delta(N) is a nonzero multiple of xi, by the lower-kernel cyclic theorem. Its value at the other endpoint is the opposite nonzero multiple. Therefore the linear variation [eta,N] cannot vanish.

The determinant of N_tilde is a global invariant section of O_(2Q)(4), whose restriction to Q is zero because N is nilpotent. The square-zero normal ideal is O_Q(-2), so this determinant lies in

    q H0(O_Q(2))^G.

But Sym^2(V+W) has only one invariant, the positive quadric q itself. Passing to the coordinate ring of Q removes it, giving H0(O_Q(2))^G=0. Hence det(N_tilde)=0. Cayley-Hamilton for a rank-two twisted endomorphism, together with trace(N_tilde)=0, gives N_tilde^2=0. The assertion is valid over the nonreduced base 2Q and does not require diagonalization or any statement about its kernel.

Finally the exact obstruction polynomial is c s+d s^2, with c,d nonzero and second root s_*=-c/d. At m=s_*/2 it equals -c^2/(4d), so the midpoint is not a third-normal bundle. The square-zero adjoint lift therefore must not be used as evidence of a flat spinor filtration or an ambient bundle realization.

## Scope and evidence

Inputs are the Serre double-cover theorem, the actual tangent-orbit isomorphism in the Atiyah-quintic second-obstruction proof, the cyclic lower-kernel theorem, and the exact first-normal affine transition formula. The result supplies a canonical reference point and a genuine square-zero adjoint at that point, but it does not evaluate the constant positive cubic gate. The companion symbolic test verifies the affine and determinant-character arithmetic only.

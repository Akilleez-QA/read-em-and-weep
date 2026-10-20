# Good squares and algebraic rank-one transport

This proof strengthens the good-quadratic theorem: for any
finitely generated graded module over a polynomial ring in finitely
many variables over C, generated in degree zero, with dim M_d=2
for an integer d>=2,
a general linear form ell makes ell^(d-1):M_1 -> M_d surjective.
The argument uses vector-valued homogeneous polynomials,
derivative-row proportionality, Euler's identity, and polarization.

For the fixed HM primary module, choose a good square ell^2 and
alpha=l^T U_0^(-1)l!=0. Then

    H(s)=I+s U_0^(-1)ll^T,
    u_0(H(s)x)=u_0(x)+(2s+alpha s^2)ell(x)^2.

On 1+alpha s!=0, g(s)=H(s)^(-1) is an actual algebraic target
automorphism through the identity. Transforming the cubic by
the same H(s) gives an algebraic translated-root family with
generic whole-coefficient order-six vanishing and the exact
original coefficient geometry at zero.

PR442's length-two primary pencil pulls back along the degree-two
map t=2s+alpha s^2. The polynomial endpoint quotient has global
length at most 60 and support at at most four parameters.
On the automorphism locus the map is etale, so local endpoint
length is at most 30 and local torsion exponent at most two.
The completion at zero is reconstructed from the first
auxiliary-parameter jet, as an explicit cokernel module.

The global bound is a two-sheeted pullback bound, not an
improvement of PR442's length 30 on the original parameter line.
The singular parameter is excluded only from the geometric
family, not from the global polynomial module estimate.

The fixed Q_0 remains unevaluated. Algebraicity here means
algebraicity of the coefficient/root-map family, not algebraicity
of a formal quantization or a lifted module. Actual source
membership, pure-six conditions, and module lifting remain open.
No selected HM/source-instance evaluation or checker is used.

See [PROOF.md](PROOF.md) for the complete derivation, exact
dependency pins, and first-order/higher-order boundaries.

# The actual quadratic operator has a trace-free parameter normal form

## Result and scope

The actual symbol k a h D_a factors through the binary quartic a^2. Consequently the corrected midpoint operator family can be chosen linearly in h and a^2, rather than in the whole six-dimensional Sym^2(A). This removes the trivial quadratic parameter channel from a representative of the actual reduced operator family.

This is NOT an exclusion of either cubic Bockstein channel. An explicit contraction-kernel family below proves that any quadratic reduced family, actual or not, admits the same trace-free normalization without changing its cubic output. In the established six-dimensional equivariant reduced-family space the normalization leaves five coefficients; the map to the two-dimensional cubic-gate space remains onto and its kernel has dimension three. No coefficient value is obtained.

## 1. Exact identity before taking cohomology

Choose negative coordinates s,t and the invariant volume form. For any binary form u write D_u=u_s partial_t-u_t partial_s. The product rule gives

    D_(a^2)=2a D_a.

In particular, with q0=s^2, q1=st, q2=t^2,

    q0 D_q2 + q2 D_q0 - 2 q1 D_q1 = 0.             (1)

The notation q0 in this single identity is a binary basis form, not the ambient cone equation. Thus the symmetric map Sym^2(Sym^2 W) -> polynomial vector fields has the invariant quadratic relation as its kernel and factors through Sym^4 W=D5. Multiplication by h and by the fixed nonzero Atiyah normalization k preserves the identity.

The Atiyah cocycle obtained by differentiating transition functions is linear over functions in the vector-field symbol. Hence (1) also holds for the actual cocycle a zeta_a, not just for its cohomology class. There is no frame-derivative correction to this assertion: (1) is equality of vector fields acting on each transition function.

## 2. Corrected operators can retain the factorization

The residue compatibility condition and its canonical scalar correction are linear in the vector-field symbol. The established existence proof for corrected cone operators therefore gives a linear choice on the image of h tensor a^2; equivariance can be imposed by averaging over the finite group. This is a choice on a finite-dimensional vector space, not a splitting assertion for a sheaf sequence.

For completeness, with the two prescribed end actions fixed, two such operators differ by a zero-symbol map from I_Z(2) to O(4). Because Z has codimension two in the smooth stack, Hom(I_Z,O)=O. Thus this difference is rho N for a global rho in H0(O_X(2)), up to the fixed nonzero normalization of N. At the midpoint it extends as rho N_tilde: rho is an ambient quadratic and N_tilde is the actual global square-zero lift. It commutes with N_tilde, so its normal operator obstruction is zero. In particular, the zero symbol and zero corrected end actions contribute no obstruction. The trace-free representative is compatible with the actual normal-boundary construction, not merely its numerical dimensions.

Equivalently, choose a fixed equivariant linear right inverse of multiplication by the ambient q0 on the actual image containing a h zeta_a. Identity(1) makes the invariant quadratic trace of the right-hand side zero before choosing its lift. This directly gives a trace-free lift family. Changes of lift are retained in the established actual common-kernel quotient; they are not assumed to vanish as cochains. Before that quotient the trace-free equivariant family has nine coefficients, four in the common-kernel part.

After projection to the established twelve-dimensional quotient P4 tensor A of C, equivariant quadratic families form

    Hom_G(D5 tensor Sym^2 A, P4 tensor A).

Since Sym^2 A=1 plus D5, P4 tensor A=V plus P4 plus D5, and

    D5 tensor D5=1 plus A plus V plus 2P4 plus 2D5,

the full family dimension is six, and the trace-free subspace has dimension five.

## 3. Why this does not reduce the cubic target

Use the invariant nondegenerate bilinear form on A and let T:D5->P4 tensor A be its unique nonzero equivariant D5 inclusion. For a in A define

    K_T(a,h)=a tensor <a,T(h)> - <a,a> T(h),        (2)

where the P4 coefficient remains untouched and the displayed a is in the A tensor factor. Contraction of that A factor with a is zero identically. Taking the quadratic parameter trace gives

    tr_parameter K_T = (1-dim A) T = -2T.         (3)

Here the trace convention sends a_i a_j to delta_ij in an orthonormal frame; using the Laplacian instead multiplies both sides by two.

Thus the contraction kernel contains a family with nonzero quadratic trace. Given any equivariant quadratic family B, its trace is a scalar multiple of T; adding the corresponding multiple of K_T makes it trace-free without changing contraction, and hence without changing the subsequent actual second-symbol quotient.

In particular the full map and its five-dimensional trace-free restriction have identical images. Using the established two-dimensional image, the latter kernel has dimension three. Formula(2) supplies the exact normalization mechanism and prevents interpreting the missing coefficient as a new cubic-channel vanishing theorem.

## Sources and verification

The actual operator and boundary are from ACTUAL-THIRD-VALUE-AS-MIDPOINT-DUALIZING-OPERATOR-DEFECT.md. Canonical residue correction is from POSITIVE-SERRE-RESIDUE-AND-CANONICAL-CONE-OPERATOR-CORRECTION.md. The twelve-dimensional quotient and actual contraction are from ACTUAL-NEGATIVE-INVOLUTION-SECTOR-AS-SQUARE-QUOTIENT.md. The two-dimensional cubic image is the established universal cubic-channel gate; this note does not rederive that gate.

The companion verifier checks (1)-(3) symbolically with independent formal coordinates. No actual HM coefficient, actual-instance matrix, or rank test is used.

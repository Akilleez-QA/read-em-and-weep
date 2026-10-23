# Actual involution blocks of the full85-dimensional pencil

## Statement

Let B=End_0(F), where F is the normalized HM bundle. Use the standard HM involution iota and the actual ambient linearizations fixed in INVERSION-EVEN-QUADRICS-ARE-ADJOINT-BAD.md. The entire ambient cohomology groups, not just their Euler difference, have parity dimensions

    A=H1(P4,B(2)):  (41,44),
    D=H1(P4,B(4)):  (37,48).

The actual multiplication pencil m_q:A -> D is therefore

    even q:  (41 -> 37) directsum (44 -> 48),
    odd q:   (41 -> 48) directsum (44 -> 37).

Even quadrics force corank at least4; equality holds precisely when both displayed blocks have maximal rank. Odd quadrics force corank at least7; equality again means both blocks have maximal rank. The odd quadrics are singular, so that second statement concerns the actual multiplication pencil, not smooth quadric geometry. No maximal-rank assertion for a selected or general member is made.

## 1. Actual ambient resolution and its tail

Put U=H0(F(3)), d=det U, and let ell be the evaluation cokernel on the25 disjoint HM lines C. The pinned exterior-symmetric evaluation resolution, twisted to degree t, is

    0 -> d O(t-10) -> wedge^2 U O(t-5)
      -> U F(t-2) -> B(t) -> T_t -> 0,
    T_t=ell^2(t-5).

We use t=2 and4 only. The actual restriction E|C_i=O(6) directsum O(-1), for E=F(3), identifies ell|C_i=O(-1). Thus

    T_2|C_i=O(-5),    T_4|C_i=O(-3).

The actual primary cohomology is concentrated in H1 at F and F(2), with dimensions5 and10. The middle line-bundle terms O(-3) and O(-1) are acyclic. The left terms O(-8) and O(-6) have only H4, of dimensions35 and5. Each tail has only H1, of dimensions100 and50.

Let K1 be the image of wedge^2 U O(t-5) in U F(t-2), and K0 the image of U F(t-2) in B(t). The three image sequences give

    H3(K1)=d H4(O(t-10)),
    H1(K0)=U H1(F(t-2)),
    H2(K0)=d H4(O(t-10)),

with all other cohomology of these two image sheaves zero. The remaining exact sequence is

    0 -> U H1(F(t-2)) -> H1(B(t)) -> H1(T_t)
      --a_t--> d H4(O(t-10)) -> H2(B(t)) -> 0.

It also gives H0(B(t))=H3(B(t))=H4(B(t))=0. It remains to check surjectivity of the actual a_t, rather than assume cohomology concentration from Euler dimensions.

## 2. The tail boundary is actual ambient restriction duality

On C let M be the rank-one evaluation image and K its rank-three kernel. Then det K=d M^(-1), and transverse determinantal geometry gives

    N_(C/P4)=K* tensor ell,
    det N_(C/P4)=d^(-1) det(E) ell^2.

Since det(E)=O(5), adjunction gives

    omega_C=d^(-1) ell^2,
    T_t* tensor omega_C=d^(-1) O_C(5-t).

The standard ambient canonical line omega_P4=O(-5) has trivial extra involution character: the ambient five-dimensional involution has determinant+1. Dualizing the leftmost resolution term gives d^(-1) O(5-t). Under these compatible identifications, the dual of a_t is precisely

    d^(-1) H0(O_P4(5-t)) -> d^(-1) H0(O_C(5-t)).

This is the ambient version of the actual cubic-evaluation identification in the pinned fifty-point proof, not merely an equality of source and target dimensions. Locally, put the rank-one evaluation matrix in the form with first row(1,0,0,0) and second row(0,a,b,c). Here a,b,c are transverse normal parameters for C. Canceling the unit summands in the exterior-symmetric complex leaves the Koszul resolution of(a,b,c). Its dual fundamental-class map is restriction to C. The displayed global adjunction lines glue these local maps without independent componentwise weights.

The pinned actual facts H0(I_C(1))=H0(I_C(3))=0 imply that these restriction maps are injective. Therefore a_t is surjective for t=4,2 respectively, and

    H^i(B(t))=0 for i not equal to1,  t=2,4.

Moreover the same restriction exact sequence identifies the kernel of a_t with d M_(5-t)*, where M_k=H1(I_C(k)). Hence the actual equivariant extension is

    0 -> U H1(F(t-2)) -> H1(B(t)) -> d M_(5-t)* -> 0.

The dimensions are20+65=85 at t=2 and40+45=85 at t=4. These are exact cohomology and functorial map statements, not a computation from an adjoint Hilbert polynomial alone.

## 3. Complete character calculation

The preceding inversion note proves that U has an unknown scalar character epsilon=+1 or-1, with d having character+1. It also proves

    trace H1(F)=epsilon,
    trace H1(F(2))=-2 epsilon,
    M1 parity=(21,24),
    M3 parity=(29,36).

Thus U H1(F) has dimension20 and trace4, giving parity(12,8); U H1(F(2)) has dimension40 and trace-8, giving parity(16,24). Adding the actual residual extension terms gives

    H1(B(2)): (12,8)+(29,36)=(41,44),
    H1(B(4)): (16,24)+(21,24)=(37,48).

Here the unknown epsilon has canceled, rather than being set to+1.

For an independent check directly on the ambient tail, all24 lines except C00 occur in exchanged pairs. On C00=P(V_-), the involution fixes the base line pointwise, ell^2 has fiber character+1, and O(t-5) has character-1 for t=2,4. Consequently

    trace H1(T_2)=-4,
    trace H1(T_4)=-2.

Serre duality gives trace H4(O(-8))=trace H0(O(3))=3 and trace H4(O(-6))=trace H0(O(1))=1. The exact sequences thus give

    trace H1(B(2))=4-4-3=-3,
    trace H1(B(4))=-8-2-1=-11,

which reproduce exactly the two claimed parity pairs. The ambient equivariant Euler characteristics are therefore3 and11, and their difference8 agrees with the independent smooth-even-quadric index calculation.

## 4. Equivariance of the entire multiplication pencil

Naturality of multiplication gives

    iota_D m_q iota_A^(-1)=m_(iota q).

For even q this preserves signs, so m_q has the two diagonal rectangular blocks. For odd q it reverses signs and has the two off-diagonal rectangular blocks. Rank-nullity gives the stated corank bounds. In particular the even lower bound holds algebraically on the entire even linear space, not only its smooth open.

The actual full determinant Delta(q)=det(m_q) is a homogeneous polynomial of degree85, possibly identically zero. Since the negative dimensions44 and48 are both even, det(iota_A)=det(iota_D)=+1 and

    Delta(iota q)=Delta(q).

Write q=q_+ + q_- with dimensions9 and6. Delta is therefore even in q_-. Homogeneity also makes it odd in q_+.

For the even space I=(q_-), the corank bound gives Delta in I^4 and vanishing of all82-by82 minors. For the odd space J=(q_+), the corank bound gives Delta in J^7 and vanishing of all79-by79 minors. At the generic point of either linear space, eliminate an invertible maximal block; the remaining Schur complement has all entries in its defining ideal. This proves the corresponding symbolic-power bound. Symbolic and ordinary powers agree for these linear prime ideals, yielding the global statements. These memberships do not assert that Delta is nonzero or that the orders are exact. Combining them with homogeneity and inversion symmetry leaves only the possible bidegrees

    (degree in q_+, degree in q_-)=(81,4),(79,6),...,(7,78).

In particular, along q_+ + s q_-, the determinant is an even polynomial in s, divisible by s^4, and has degree at most78. None of these allowed coefficients is proved nonzero.

## 5. A conditional four-dimensional transverse gate

Suppose an actual even q0 has both rectangular blocks of maximal rank. This is a separate unproved gate, not an existence assertion. Then

    K=ker(m_q0) is four-dimensional and iota-even,
    Coker=coker(m_q0) is four-dimensional and iota-odd.

Every odd perturbation r in the actual six-dimensional quadric space induces the intrinsic map

    nu_r:K -> Coker,    v -> class of m_r(v).

If det(nu_r) is nonzero for some actual r, then m_(q0+s r) is invertible for general s. Indeed the Schur complement has first-order term s nu_r, and the coefficient of s^4 in the full determinant is a nonzero unit times det(nu_r). This is a sufficient, fully functorial transverse gate for generic full-adjoint vanishing. It is not a generic-rank inference: neither the existence of such q0 nor the nonzero determinant of its six-parameter normal map is established here.

Sources: the actual exterior-symmetric resolution at d5d9bd997145b0ecf7d7bd659a19fb7845afb75f; QUADRIC-FIFTY-POINT-BOUNDARY.md at22bdcb7e9c833e7a1819d0ec28e5e615be9c7a4f for the compatible adjunction and restriction-duality normal form; INVERSION-EVEN-QUADRICS-ARE-ADJOINT-BAD.md for the independently derived actual polarization and primary characters. No selected HM coefficient, evaluated matrix, or rank experiment is used.

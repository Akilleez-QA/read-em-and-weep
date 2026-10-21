# Inversion-even smooth quadrics are full-adjoint bad

## Theorem and scope

Let iota be the HM normalizer involution acting on ambient coordinates by e_i -> e_-i, with eigenspace dimensions3 and2. Every smooth quadric whose equation is iota-even satisfies

    h0(Q,End_0(F_Q)(4)) >= 4.

On the open where Q is transverse to the25 HM lines, at least four of these sections are iota-even. Thus the projective8-dimensional linear system of even quadrics is full-adjoint bad. This includes smooth quadrics and does not require either quadratic flank to be good. The same theorem holds for its Heisenberg-conjugate involutions.

This is a new parity obstruction for this special family, not generic twist-four vanishing. General quadrics outside the even subsystem do not preserve the involution, so their maps do not have the decompositions below.

## 1. Actual inversion and polarization signs

Use the general smooth beta blowdown pi:X_B -> A and the actual type(2,10) polarization P with pi*P=H+C. By ACTUAL-THETA-KERNEL-INTERPOLATION.md, the25 contraction points form Sigma=K(Theta) after choosing the contracted HM line C00 as origin, with Theta^2=P.

The required source input is stronger than polarization type alone. ADHPR, Syzygies of Abelian and Bielliptic Surfaces in P4, Proposition8.4(ii), proves that the linked family's involution is inversion on its minimal abelian surface and that all16 two-torsion points are even for the descended polarization. Section7 and the actual linkage dictionary identify this family with X_B. Choosing the contraction point of C00 as origin preserves inversion since that point is fixed. The25-point subgroup has only one inversion-fixed point, namely0.

Fix the linearization induced by the actual ambient action on H and by the canonical invariant section of O(C). On C00=P(V_-), iota fixes the line pointwise and acts by -1 on O(H). On the exceptional curve over0, inversion has normal character -1, so it also acts by -1 on O(C)|C00. Thus P has fiber character +1 at0. This fixes the common sign in the cited all-even assertion: every P fiber over A[2] has character +1. Every positive power P^n has the same +1 fiber characters there.

The actual four-dimensional U=H0(F(3)) is scalar under iota, say with eigenvalue epsilon in {+1,-1}. Indeed wedge^2 U identifies equivariantly with the six invariant quintics, all of which are iota-even (ADHPR Section3). Since every pairwise product of the four eigenvalues is +1, all four eigenvalues coincide. No choice epsilon=+1 is needed below. In particular every B is fixed, det B has character epsilon, and det U has character +1.

## 2. Actual abelian jet parities

For a symmetric ample P^n, higher cohomology vanishes. Holomorphic Lefschetz for inversion gives

    trace(iota | H0(P^n)) = 16/4 = 4,

because each fixed point has tangent eigenvalues(-1,-1) and P^n fiber character +1. Thus H0(P) has parity dimensions(12,8), and H0(P^3) has dimensions(92,88), with the even dimension written first.

On the25 fat points, all nonzero elements of Sigma are paired by inversion, so they contribute zero to the trace. At0, the degree-j part of the local jet algebra has character(-1)^j and dimension j+1. Therefore

    trace(O/m^2)=1-2=-1,
    trace(O/m^4)=1-2+3-4=-2.

The actual evaluation kernels H0(P I_Sigma^2) and H0(P^3 I_Sigma^4) vanish by the proved low-degree beta restriction theorem. Their cokernels consequently have the following exact parities:

    V1=H1(P I_Sigma^2): dimensions(25,30), trace -5;
    V3=H1(P^3 I_Sigma^4): dimensions(32,38), trace -6.

These are fiber-character and Lefschetz calculations, not a dimension-based choice of linearizations.

The actual linear subsystem W=H0(P I_Sigma)=H0(P4,O(1)) has parity(3,2). Hence

    H0(P^2 I_Sigma^2)=Sym^2 W

has even dimension9 and odd dimension6. The even part consists of the two diagonal symmetric blocks; the odd part consists of the mixed3-by2 block. Every odd quadric has rank at most4 and is singular. Even quadrics, by contrast, are generally smooth.

For an even q, the fixed-beta interpolation55 -> 70 splits as25 -> 32 and30 -> 38. These blocks alone force no kernel. For an odd q it splits as25 -> 38 and30 -> 32, which also forces no kernel. The global obstruction below is therefore not a misuse of fiberwise dimensions.

## 3. Rao parities and the two primary trace identities

On C, the24 lines other than C00 occur in exchanged pairs. On the fixed line C00 the ambient O(1) has character -1. Therefore

    trace H0(O_C(1))=-2,
    trace H0(O_C(3))=-4.

Ambient linear and cubic forms have traces1 and3, respectively. The pinned H0(I_C(1))=H0(I_C(3))=0 thus gives

    M1=H1(I_C(1)): dimensions(21,24), trace -3;
    M3=H1(I_C(3)): dimensions(29,36), trace -7.

Use the actual equivariant restriction extensions, independently of any quadric:

    0 -> M1 -> V1 -> det B tensor H1(F(2))* -> 0,
    0 -> M3 -> V3 -> det B tensor H1(F)* -> 0.

Their quotient traces are respectively -2 and +1. Hence

    trace H1(F(2))=-2 epsilon,
    trace H1(F)=epsilon.

The dimensions of these cohomology groups are10 and5. These identities retain the unknown common U sign and will cancel it exactly.

## 4. Conditional twenty-boundary blocks

Suppose first that an even smooth Q lies on the common flank-good open. Then q:M1 -> M3 is injective, giving

    R=coker(q:M1 -> M3): parity(8,12).

The dual primary map det B H1(F(2))* -> det B H1(F)* is surjective and has kernel det B P0*, where P0=H1(F_Q(2)). The kernel has parity(1,4). Since U is four copies of epsilon and det B has character epsilon, the actual global20 -> 20 boundary has parity blocks

    source det U tensor R*:                  (8,12),
    target U tensor P0:                      (4,16).

Thus its even block8 -> 4 has a kernel of dimension at least4. This already proves the obstruction on that intersection, but does not establish that the even system meets the flank-good open. The next argument removes that requirement entirely.

## 5. Unconditional equivariant Euler proof

Take any even smooth Q transverse to C, and write Z=C intersect Q. The actual exterior-symmetric resolution restricted to Q is

    0 -> d O_Q(-6) -> wedge^2 U O_Q(-1)
      -> U F_Q(2) -> B_Q(4) -> T_Z -> 0,

where B=End_0(F), d=det U, and T_Z=ell^2(-1)|Z has length50. This is the pinned QUADRIC-FIFTY-POINT-BOUNDARY.md resolution; it does not require good ranks of the two flanks.

The group H0(F_Q(2)) can be nonzero, but F_Q(2) has no H2 or H3 for every smooth Q, by the primary restriction sequence and the actual support of H^i(F). Since O_Q(-1) is acyclic, the two image sequences of the displayed resolution imply

    H2(B_Q(4))=H3(B_Q(4))=0.

We now compute its equivariant Euler characteristic term by term.

(a) Primary term. Because q is even, the restriction sequence F -> F(2) -> F_Q(2) is equivariant with no extra sign on its first term. Thus

    chi^iota(F_Q(2))
      = -trace H1(F(2)) + trace H1(F)
      = 3 epsilon.

Multiplying by trace(U)=4 epsilon gives

    chi^iota(U F_Q(2))=12.

No injectivity of the primary map is used.

(b) Line-bundle term. The even quadric equation gives

    trace H0(O_Q(3))
      = trace H0(O_P4(3)) - trace H0(O_P4(1))
      = 3-1=2.

The actual canonical linearization of omega_Q=O_Q(-3) has no additional sign: the ambient involution has determinant+1 and the equation q is even. Serre duality therefore gives

    chi^iota(d O_Q(-6))=-2,

since d has character+1.

(c) Point term. Inversion fixes exactly the two points of Z on C00; the other48 marked points occur in exchanged pairs. The compatible zero-dimensional adjunction in the pinned fifty-point proof gives

    T_Z* tensor omega_Z = d^(-1) O_Z(3).

For a reduced fixed point, its intrinsic dualizing line omega_Z has the trivial character. At either fixed mark O_Z(3) has character-1, because it lies on C00=P(V_-). Thus T_Z has character-1 at each fixed mark, and

    trace H0(T_Z)=-2.

Combining the three terms, with their signs from the exact resolution,

    chi^iota(B_Q(4))=(-2)+12+(-2)=8.

The ordinary Euler characteristic is0: the same terms have Euler characteristics50, -20, and -30. Since H2 and H3 vanish, the even and odd Euler characteristics are

    h0(B_Q(4))_+ - h1(B_Q(4))_+ = 4,
    h0(B_Q(4))_- - h1(B_Q(4))_- = -4.

In particular h0(B_Q(4))_+ >=4. This proves actual nonvanishing even when one or both flanks are bad. It does not rely on a hypothetical nonempty intersection with the common-good open.

## 6. Extension to all smooth even quadrics

The even subsystem is basepoint free on P4: at any point, either its positive or negative projection is nonzero, and the square of a corresponding linear form is an even quadric nonzero there. Bertini therefore gives smooth general members. Its restriction to each HM line is basepoint free, so a general member meets every line in two distinct points. The preceding proof thus applies on a dense open in the smooth even family.

The smooth even quadrics form an irreducible open in P8. Restriction of the fixed bundle B(4) gives a proper flat family, so upper semicontinuity extends h0>=4 from that dense open to every smooth member. Equivariant semicontinuity also retains the invariant-section statement. Heisenberg conjugation carries this result to the corresponding even subsystem for each conjugate involution.

## Boundary

The theorem excludes a concrete smooth-quadric family from full-adjoint invertibility. It does not exclude smooth quadrics in general. The generic quadric is not invariant under any of these fixed involutions. No rank of a selected quadric or numerical HM matrix has been evaluated, and no exact generic corank within the even family is asserted.

Sources: ADHPR https://arxiv.org/pdf/alg-geom/9606013v2 , Section3, Section7, Proposition8.4(ii); the two actual abelian interpolation notes; QUADRIC-FIFTY-POINT-BOUNDARY.md at22bdcb7e9c833e7a1819d0ec28e5e615be9c7a4f and its source resolution at d5d9bd997145b0ecf7d7bd659a19fb7845afb75f. The equivariant Euler proof explicitly retains all linearization signs.

## 7. Twenty-five distinct excluded invariant families

Write G=H5/center=(Z/5)^2 and label the exceptional HM lines C_g=t_g(C00). Conjugation sends iota to iota_g=t_g iota t_g^(-1), which acts on the minimal abelian surface as x -> 2g-x. The25 elements iota_g are distinct, since multiplication by2 on G is injective. Their negative ambient eigenspace lines are precisely C_g. The standard Heisenberg translates of C00 are the25 distinct HM lines, so this also verifies distinctness in the actual projective representation.

Each even quadric subsystem has vector dimension9, and these25 subsystems are distinct. Indeed, for a decomposition V=V_+ directsum V_-, the rank-one quadrics in Sym^2(V_+*) directsum Sym^2(V_-*) are exactly the squares of linear forms lying in one summand. Their two Veronese components have dimensions2 and1, so the even subsystem recovers the two eigenspaces and in particular the negative line. Distinct C_g therefore give distinct even subsystems.

A projectively iota_g-invariant quadric equation is either even or odd, since iota_g has order2. The odd equation has only the mixed3-by2 block and rank at most4. Consequently every smooth projectively invariant quadric, for any of these25 involutions, belongs to one of the excluded even P8 families.

## 8. Consequences for the actual85-dimensional pencil

The pinned fifty-point proof also identifies

    H0(B_Q(4))=ker[q:H1(B(2)) -> H1(B(4))],

where source and target each have dimension85 and the multiplication matrix depends linearly on the15 quadric coefficients. Therefore its rank is at most81 on the dense smooth locus of each even9-dimensional vector space. Every82-by82 minor, being polynomial, vanishes on the entire linear space, including its singular quadrics.

Let I be the linear prime ideal of any such even space in the affine15-dimensional coefficient space, and let Delta be the determinant of the actual85-by85 pencil. Then

    Delta belongs to I^4.

To see this, work at the generic point of the linear space and let r<=81 be the rank of the pencil modulo I. An invertible r-by-r block and the Schur complement express the determinant, up to a unit, as the determinant of an (85-r)-by-(85-r) matrix with every entry in I. Thus Delta belongs to the fourth symbolic power I^(4). A prime ideal generated by independent linear coordinates has symbolic and ordinary powers equal, giving the claimed global membership. The argument also covers an identically zero Delta; it does not assert that this determinant is nonzero or that its order is exactly4.

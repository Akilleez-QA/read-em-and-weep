# The canonical octic target section has a length-34 exceptional zero scheme

## Statement and boundary

Let A=Sym²W, D=Sym⁴W for the binary icosahedral group, X=P(A), and

    0→A O_X(−1) --quadratic multiplication-->D O_X→E→0.

PR995 identifies a unique nonzero invariant section σ∈H0(E(4)), up to scalar, as the target factor of the canonical octic generator σψ4. Its zero scheme Zσ is finite of length34. More precisely:

- σ is nowhere zero on the discriminant conic of squares.
- Zσ is supported exactly on the six projective order-five axes and the ten projective order-three axes.
- Each order-three axis is a simple zero.
- At each order-five axis the completed local ideal is (u²,v²) in stabilizer eigen-coordinates, and the local length is4.

Thus Zσ consists of six length-four complete intersections and ten reduced points, disjoint from the square conic. The zero scheme of the octic generator contains Zσ independently of its source covector. We do not compute any additional zeros of ψ4, nor the unknown ACTUAL octic scalar. No HM coefficient, parameter, selected direction, matrix or rank is evaluated; no source occurrence or catalogue pair is excluded.

## 1. Inputs and duplicate boundary

PR995, at f9435fa37c78e86391fd1a773a039dd646a05e53, research/hm/source126-typeII-internal-octic-gate/PROOF.md, supplies E, uniqueness of σ, and

    H0(E(m))^G=0 for m=0,1,2,3,
    dim H0(E(4))^G=1.

The plane has H0(O_X(m))=Sym^m A, not Sym^m W. PR982, retained as an exact input, supplies the nonzero Wronskian of the universal sextic V linear series, an invariant section of O_P(W)(12). We use this universal binary-series fact, not any actual source instance.

The existing source packets and generic-beta proof collection already contain six-axis results for OTHER maps and the ten-axis quotient-symbol degeneracy. Those are not being re-derived as new results here. A search for length34, zeros of E(4), and the target section σ found no prior statement of the PRESENT section's zero scheme. We focus on σ, not the previously studied cubic P-covariant's base scheme.

## 2. Finiteness and total length

A divisorial zero of σ would give an invariant section of E(4−d) for some positive divisor degree d. For 1≤d≤4 the displayed invariant vanishings exclude it. For d≥5, the presentation of E gives H0(E(4−d))=0, using H1(O(k))=0 for every k on P². The divisor equation has a trivial character: A5 has no nontrivial characters, so dividing out the invariant zero divisor preserves equivariance. Thus σ has no divisorial zeros.

Its zero scheme is therefore zero-dimensional (or empty). Since it is the zero scheme of a section of a rank2 bundle on a smooth surface with expected codimension2, it is a local complete intersection and its length is the top Chern number. The defining sequence gives

    c1(E)=3H, c2(E)=6H².

For a rank2 twist by O(4),

    c2(E(4))=c2(E)+4H c1(E)+16H²=34H².

Consequently length(Zσ)=34, in particular it is nonempty.

## 3. Restriction to the square conic is a nowhere-zero gradient

Parametrize the discriminant conic C by the Veronese map ν:P(W)→X, [ℓ]↦[ℓ²]. A plane twist O_X(1) restricts as O_P¹(2). The pulled-back presentation is

    0→A O_P¹(−2)→D O_P¹→ν*E→0.

There is a natural equivariant onto map D O→W O(3): evaluate the first derivatives of a binary quartic at the point where ℓ vanishes, using the symplectic identification W≅W*. Its kernel consists exactly of quartics with a double zero there, namely ℓ²A. Consequently this is an isomorphism of equivariant bundles

    ν*E ≅ W O_P¹(3),
    ν*(E(4)) ≅ W O_P¹(11).                            (1)

This proves the claimed restriction rather than inferring its splitting from degree alone.

The restricted σ is nonzero. Otherwise the discriminant exact sequence would factor it through an invariant section of E(2), which is zero. Its restriction is thus a nonzero invariant element of W⊗Sym¹¹W.

The universal Clebsch–Gordan decomposition gives

    W⊗Sym¹¹W ≅ Sym¹²W ⊕ Sym¹⁰W.

Every nonempty icosahedral orbit on P(W) has size at least12. There is a unique size12 orbit: the two fixed points of each of the six order-five subgroups. Hence there is no degree10 invariant binary form and the invariant degree12 space has dimension1. The nonzero sextic Wronskian supplies one such degree12 form F12. Its zero divisor must be precisely the size12 orbit, with multiplicity1 at every point: total degree12 leaves no other possibility. Thus F12 is squarefree.

The equivariant polarization/gradient map embeds Sym¹²W into W⊗Sym¹¹W. Uniqueness shows that σ|C is a nonzero scalar multiple of ∇F12 under (1). The two derivatives of a squarefree homogeneous binary form of positive degree have no common projective zero: Euler's identity would put such a point on F12, contradicting simplicity of that root. Therefore σ is NOWHERE zero on C, not merely generically nonzero there.

All statements concern the whole universal orbit and unselected variable ℓ. No actual HM direction is substituted.

## 4. Off-conic orbit classification forces the support and lengths

Identify A with the complexified three-dimensional rotation representation of A5. Its invariant quadratic form cuts out C. A point outside C is a non-isotropic line. Its stabilizer acts on that line by ±1 and preserves its orthogonal plane, hence embeds into O(2). The following elementary classification also follows directly from element orders in A5.

If the stabilizer contains an element of order3 or5, the non-isotropic line must be that rotation's eigenvalue-one axis: the other two eigenlines are isotropic because their eigenvalues are not ±1. Its full projective stabilizer is the normalizer of the associated cyclic subgroup, of order6 or10. The corresponding orbits therefore have sizes10 and6, respectively. Each is unique, indexed by the cyclic subgroups of that order.

If the stabilizer has no element of order3 or5, every nonidentity element has order2. Such a group is elementary abelian, and the largest such subgroup of A5 has order4. Its order is therefore1,2 or4, giving orbit size60,30 or15. These possibilities exhaust every point outside C; no orbit of size12 or20 is silently omitted.

An invariant zero-dimensional scheme has a constant positive local length along each support orbit. Let a,b,c,d,e be the sums of these local lengths over the orbit TYPES of size6,10,15,30,60, respectively. The total length34 forces

    6a+10b+15c+30d+60e=34,
    a,b,c,d,e nonnegative integers.

There is exactly one solution:

    (a,b,c,d,e)=(4,1,0,0,0).

Since each size6 and size10 orbit is unique, Zσ is supported on both of them, with local lengths4 and1. In particular every order-three-axis zero is reduced and transverse.

## 5. The order-five local scheme is the exact quadratic complete intersection

Fix an ARBITRARY order-five axis, and use binary eigenlines to write its representative quadratic as xy. A generator of its cyclic stabilizer has binary eigenvalues η,η⁻¹, with η²=ζ a primitive fifth root. The tangent plane to P(A) at [xy] has the two eigenweights ζ,ζ⁻¹, represented by the x² and y² perturbations. The fiber

    E_[xy]=D/(xy A)

is spanned by x⁴,y⁴ and has weights ζ²,ζ⁻². The O_X(4) twist has weight1 because xy has weight1. Thus E(4) has the same two fiber weights there.

Choose equivariant formal coordinates u,v and an equivariant local bundle frame. Such choices exist by averaging parameters and frames under the finite cyclic stabilizer; their linear parts are invertible. The two component functions of σ have characters ζ²,ζ⁻². There are no constant or linear monomials with those weights. Their possible quadratic leading terms are respectively constant multiples of u² and v².

Every monomial outside the ideal (u²,v²) is one of1,u,v,uv, with character1,ζ,ζ⁻¹,1. None has weight ζ² orζ⁻². Therefore both FULL component power series belong to (u²,v²), not just their leading terms. Let I be their ideal and J=(u²,v²). We have I⊂J, while both quotients have length4: length(C[[u,v]]/I)=4 by §4, and length(C[[u,v]]/J)=4 by its displayed monomial basis. The induced surjection between these Artinian quotients is therefore an isomorphism, so I=J. Consequently

    completed local ring of Zσ ≅ C[[u,v]]/(u²,v²).

This identifies the scheme, not merely its support or total multiplicity. The existing six-axis length-four schemes for other maps are not assumed in this argument.

## 6. A minimal resolution and exact Hilbert function

The regular section σ:O(−4)→E has quotient I_Zσ(7), since det(E)=O(3). Pull back along D O→E in the defining presentation. Its kernel K fits into

    0→A O(−1)→K→O(−4)→0.

The extension splits because Ext¹(O(−4),A O(−1))=A⊗H1(O(3))=0. An equivariant splitting exists by averaging. Twisting the resulting presentation of I_Zσ(7) by−7 gives

    0→A O(−8)⊕O(−11)→D O(−7)→I_Zσ→0.                (2)

All entries in the syzygy map have positive degree, so this is minimal. Taking global sections in every twist preserves exactness because H1 of every line bundle on P² vanishes; hence (2) is also the minimal graded free resolution of the saturated ideal. There are exactly five degree-seven generators, three linear first syzygies and one degree-four first syzygy.

The homogeneous coordinate ring has Hilbert series

    (1−5t⁷+3t⁸+t¹¹)/(1−t)³,

with Hilbert function in degrees0,...,9 equal to

    (1,3,6,10,15,21,28,31,33,34),

and value34 thereafter. This separately checks the scheme length and is stronger than a support count. It describes Zσ, not a previously assumed six-axis ideal.

## 7. Consequence for the canonical octic generator

The map σψ4 factors through O_X(−4). At every point of Zσ it vanishes regardless of ψ4. The target factor σ causes no zero anywhere on the square conic. This does not by itself prove that the WHOLE octic generator is nowhere zero on that conic, since its source covector must also be considered. Nor does it select whether the actual octic symbol's unknown scalar is zero.

The bounded new information is the exact target-factor exceptional scheme: six double-quadratic order-five axes plus ten simple order-three axes, total length34. Nothing about further source exclusions or higher internal symbols is concluded.

## Verification scope

The exact checker authenticates the pinned proofs, checks the plane character and Chern calculations, enumerates A5 elements/cyclic subgroups/normalizers, exhausts the integer orbit-length equation, verifies the universal first-jet kernel and local C5 monomial weights, checks the universal Euler identity used in the squarefree-gradient argument, and verifies the resolution Hilbert numerator. These are universal representation and scheme checks, not actual HM evaluations. The written argument supplies global geometry and its relation to the canonical σ.

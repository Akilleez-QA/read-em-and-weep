# The actual first-cup kernel has the negative two-step splitting

Work over C with G=SL2(F5), negative two-space W, and parameter line T=P(W*). Set A=Sym2 W, S=Sym3 W, D=Sym4 W, T6=Sym5 W; V=Sym2 W' is the other even three-space, and P is the even four-space. All O(d) are on T with their standard equivariant linearization.

No selected actual HM coefficient, point, parameter, jet, matrix, derivative, or instance rank is evaluated. The binary forms below are universal representation vectors, not assigned values of an actual HM tensor.

## 1. Exact inputs and result

The immutable inputs are in Akilleez-QA/read-em-and-weep. INPUTS.json pins original bytes and Git blobs.

- TWO_TYPES: PR975 at commit 8170fe31a16b2028052973157dc79a06d0d77f64, research/hm/first-cup-kernel-two-types/PROOF.md. The actual first-cup kernel has exact sequence

      0 -> K -> H O --mu--> J O(2) -> 0,
      H=H0(B_R(3))=Sym2 D=1+P+2D,   J=H1(B_R(1))=A+V.       (1)

  It proves the exhaustive alternatives

      K=T6 O(-1) directsum A O(-2),    or
      K=D O directsum S O(-3).                              (2)

  The second alternative occurs exactly when H0(K)=D; otherwise H0(K)=0. It retains the actual square subbundle and all original cup-map premises.
- FIRST: commit db51525015bb7c5e825833d550d08dedf6f6ea96, research/hm/order-four-quadratic-load/ODD-FIRST-SCALING-OBSTRUCTION.md, Sections 6–7. It identifies D with the traceless self-adjoint operators Sym2_0 A for the invariant form on A, and the actual second-normal coefficient injection with a nonzero scalar multiple of

      a -> y_a,          y_a(S)=Sa.

  The actual first cup is the Leibniz map followed by the actual quotient

      sigma_(y_a)(S T)= y_a(S) tensor T + y_a(T) tensor S,
      mu_(y_a)(S T)=class of sigma_(y_a)(S T)
          in J=(A tensor D)/im(phi),
      phi: Lambda2 A tensor V -> A tensor D.                 (3)

  The map phi is injective and im(phi)=P+D, as follows from its authenticated cokernel J=A+V and dimensions 9,15,6.

We prove

      H0(K)=0,
      K = T6 O(-1) directsum A O(-2).                         (4)

Thus the constant-D alternative in (2) does not occur for the actual cup. Equivalently the remaining D component of the connecting map in PR975 is nonzero. No coefficient or scalar normalization is selected.

## 2. Authenticate the two projections of the actual quotient

Use the ordinary complex algebraic group SL(W) only as an auxiliary group for universal tensor identities. The actual geometry is G-equivariant, and no extension of its full symmetry group is assumed. The actual representations A,D and the tensor y extend to the SL(W) modules Sym2 W, Sym4 W and their unique nonzero contraction. This extension of y is legitimate: A occurs once in Hom(D,A), and the standard nonzero SL(W)-equivariant map belongs to precisely that G-channel. The actual map is its nonzero scalar multiple by FIRST.

The Clebsch–Gordan decompositions are

      Sym2 D = H8 directsum H4 directsum H0,
      H8=Sym8 W,   H4=Sym4 W,   H0=C;
      A tensor D = E6 directsum E4 directsum E2,
      E6=Sym6 W,   E4=Sym4 W,   E2=Sym2 W.                    (5)

Restricted to G, H8=P+D, E6=V+P, E4=D, E2=A. In particular A tensor D has the four pairwise nonisomorphic constituents A,V,P,D, each once. The actual image im(phi)=P+D is therefore exactly the canonical sum of those two isotypic subspaces. There is no undetermined embedding between repeated constituents in this target.

Consequently projecting A tensor D onto E2=A, and projecting onto E6 followed by its G-isotypic projection to V, both kill the actual im(phi). They induce the actual A and V quotient components of J, up to nonzero scalar identifications. They are not arbitrarily substituted maps with equal source and target dimensions.

Package the family (3) as a coefficient map

      nu: H -> A* tensor J = A tensor J.                    (6)

The equality uses the invariant nondegenerate form on A. Its value on a is mu_(y_a). The actual second-normal scalar is nonzero, so it does not affect the kernel. Moreover

      H0(K)=ker(nu).                                        (7)

Indeed taking sections of (1) produces its quadratic coefficient map. Its evaluation directions correspond to the pure squares spanning Sym2 W=A; a coefficient tensor vanishes on every parameter direction if and only if it is zero. This is a polynomial identity on the whole family, not an evaluation at selected parameters.

## 3. The A quotient detects the H4 constituent

In the orthogonal model D=Sym2_0 A, the universal nonzero projection A tensor D -> E2=A is

      b tensor S -> Sb.

For S,T in D, its composite with (3), as a function of a, is

      a -> (TS+ST)a.                                      (8)

Thus the symmetric square of D maps to the symmetric operators on A. Its trace-free part is the Jordan product

      ST+TS - (2/3)tr(ST) Id.                              (9)

This universal polynomial is nonzero in dimension three. For example on the formal diagonal operator with indeterminate entries x,y,-x-y, its square cannot be a scalar operator identically: the difference of its first two diagonal squares is x^2-y^2, a nonzero polynomial. These are free indeterminates used to verify an identity of abstract orthogonal representations, not the entries of an actual HM map.

The trace-free symmetric operators are Sym2_0 A=Sym4 W. By (5), the only SL(W) source constituent that can map to this module is H4; (9) proves that its coefficient is nonzero. Therefore the A quotient component of nu is injective on H4. It vanishes on H8, because

      A tensor A = Sym4 W directsum Sym2 W directsum C

contains no Sym8 W.

Suppose H0(K)=D, the remaining case in (2). This irreducible G-subrepresentation of H has no projection into H0=C. Its projection into H4 must also be zero by the preceding injectivity and the vanishing of the H8 contribution to the same A quotient. Consequently

      H0(K) is the five-dimensional D subspace U of H8.     (10)

There is only one such D constituent in H8=P+D. This step excludes a graph mixing the two different D constituents of H.

## 4. The remaining V quotient is the actual second polarization

Project A tensor D onto its top SL(W) constituent E6=Sym6 W. In binary-form notation this projection is multiplication of a quadratic and a quartic. Let nu6 be the resulting universal coefficient map from H to A tensor Sym6 W before projecting the latter factor to V.

Restricted to H8, this map is nonzero. Here is a universal highest-weight check retaining the actual tensor type. Represent D by binary quartics in independent formal variables x,y. The contraction y_a(f) is a nonzero scalar multiple of the second transvectant of f with a. For f=x^4 and a=y^2, it is a nonzero multiple of x^2; the two equal Leibniz terms for f f therefore give, after multiplication, a nonzero multiple of x^6. The vector f f is the highest vector in H8. This verifies a universal Clebsch–Gordan coefficient, not an actual selected bundle coefficient or parameter.

There is exactly one SL(W) map from Sym8 W to Sym2 W tensor Sym6 W. Hence this restriction is a nonzero scalar multiple of the standard top polarization

      Delta_(2,6): Sym8 W -> Sym2 W tensor Sym6 W.           (11)

In coordinates its coefficient span is exactly the span of all second directional derivatives of the degree-eight form. More invariantly it is the degree-(2,6) component of the symmetric-algebra comultiplication; contracting its first factor gives all order-two constant-coefficient derivatives, up to nonzero normalization.

Section 2 now identifies the ACTUAL V component of nu on H8 as

      nonzero scalar times (1 tensor pr_V) Delta_(2,6),
      Sym6 W = V directsum P.                              (12)

This retains both required nonzero facts: the universal top coefficient does not vanish, and pr_V is the actual surviving quotient channel rather than a chosen formal substitute.

If (10) lay in ker(nu), equation (12) would force every second derivative of every vector of U into the four-dimensional P subspace of Sym6 W.

## 5. Universal binary derivative-span exclusion

Let U be an r-dimensional subspace of Sym^d W, with d>=1, and let partial U be the span of all its first directional derivatives. Then

      dim(partial U) >= min(r,d).                          (13)

Proof: if dim(partial U)<r, restriction of every nonzero directional derivative to U has a nonzero kernel. The kernel of that derivative on all of Sym^d W is the one-dimensional space spanned by the dth power of its annihilator linear form. Thus U contains this pure power for every direction. Pure powers span Sym^d W, so U is the entire (d+1)-dimensional space. In that case partial U=Sym^(d-1) W has dimension d. Otherwise the assumed dimension drop is impossible, giving dim(partial U)>=r. This proves (13). The argument uses all abstract directions universally, not a selected-instance test.

Apply (13) first to a five-dimensional U in Sym8 W and then to partial U in Sym7 W. One obtains

      dim(partial^2 U) >= min(dim(partial U),7) >= 5.        (14)

But (12) would put this entire space in P, of dimension four. This contradiction excludes (10), hence excludes H0(K)=D. By (2), the actual K has exactly the splitting (4).

## 6. Aggregate first cup and scope

As a direct consequence, the full coefficient map (6) is injective. Since

      A tensor J = A tensor (A+V) = 1+A+P+2D,
      H=1+P+2D,

its actual coefficient cokernel is the irreducible A. Thus there is an exact sequence of G-representations

      0 -> H --nu--> A tensor J -> coker(nu) -> 0,
      coker(nu) is isomorphic to A.                        (15)

This describes the simultaneous all-direction first cup; it is not a claim that an individual 15-to-6 fiber cup is injective. Each individual kernel still has rank nine, now with the determined negative splitting (4). No canonical named isomorphism of the multiplicity factors is selected, and the actual square inclusion and nonsplit extension maps remain intact.

There is also a sharp consequence for the ambient first odd-scaling cup of FIRST, equation (1). Twist the actual bundle sequence (1) by O(1). Formula (4) gives

    K(1)=T6 O directsum A O(-1),
    H0(K(1))=T6,       H1(K(1))=0.

Therefore the actual global multiplication of its quadratic cup coefficients by linear normal forms is onto, with exact sequence

    0 -> T6 -> Sym2 D tensor W
        -> (A+V) tensor Sym3 W -> 0.                       (16)

Naturality identifies this arrow with FIRST's actual ambient first odd-scaling cup s tensor w -> [zeta,s] w: it is the same polynomial family in (1), followed by multiplication of normal coefficients by w. Thus its dimensions are 30 -> 24, its kernel is exactly T6, and it is surjective. This resolves FIRST's earlier representation-theoretic kernel lower bound for this ambient map. It gives no new two-root estimate (the projected root map was already onto twelve dimensions), and no conclusion about later secondary or global odd-quadric survival.

The new proof selects the actual type left open by PR975 using the authenticated actual quotient, two nonzero universal tensor projections, and a derivative-span theorem. It does not compute the secondary boundary, the opposite-pencil bundle C, top polar sigma, vertex scalar, global odd-quadric sections or a source/frontier cut.

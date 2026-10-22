# The exact odd-transverse adjoint deformation interface

## Mathematical input and statement

Let B=End_0(F) for normalized HM and let

    A=H1(P4,B(2)), D=H1(P4,B(4)), dim A=dim D=85.

Actual multiplication is the linear map

    M:H0(P4,O(2)) -> Hom(A,D),   q |-> M(q).

The ambient vanishings H0(B(2))=H0(B(4))=0 identify ker M(q) with H0(Q,B_Q(4)). No good-flank hypothesis is imposed.

Let iota be the HM inversion, with ambient eigenspace dimensions3 and2. Write W_even and W_odd for its quadratic eigenspaces, of dimensions9 and6. The companion theorem INVERSION-EVEN-QUADRICS-ARE-ADJOINT-BAD.md proves, independently of this note, that for every smooth even quadric transverse to the HM lines,

    [H0(B_Q(4))]-[H1(B_Q(4))]=4(1-sign),
    H2(B_Q(4))=H3(B_Q(4))=0.

The argument below imports that theorem; it does not reprove the even-family exclusion. It identifies the exact first-order escape criterion, its parity restrictions, and the higher-order alternative when the first derivative is singular. No exact generic even corank is assumed.

## 1. The canonical derivative and its actual cohomological formula

Fix an even q0 defining a smooth transverse Q0. Put

    K=ker M(q0), C=coker M(q0), m=dim K=dim C.

The restriction long exact sequence gives a canonical injection C->H1(B_Q0(4)). Its two spaces have the same dimension: the square multiplication map makes dim C=dim K, while the imported ordinary Euler characteristic and higher vanishings give h1(B_Q0(4))=h0(B_Q0(4)). Thus

    K=H0(B_Q0(4)), C=H1(B_Q0(4))

canonically, even when the primary or residual flank is bad.

For a quadratic perturbation v define

    rho_v:K -> C,  rho_v=pi_C compose M(v) compose inclusion_K.       (1)

This is independent of any choices of complements, bases, or representative of v modulo C q0. Its actual cohomology factorization is

    H0(B_Q0(4)) --boundary_q0--> H1(B(2))
      --multiplication_by_v--> H1(B(4))
      --restriction_q0--> H1(B_Q0(4)).                              (2)

It is exactly the first-order obstruction to lifting a kernel class along q0+t v. Indeed a lift x+t y satisfies

    M(q0)y + M(v)x = 0;

such y exists if and only if rho_v(x)=0. This describes the actual deformation interface rather than a new freely chosen m-by-m matrix.

Over a constant-rank open in the even subsystem, the kernels and cokernels form vector bundles. Differentiating M(q)k(q)=0 for a local kernel section shows

    rho_v=0 for every even tangent direction v.                     (3)

Thus at such a q0, (1) factors through the normal space of the even subsystem. In projective notation this normal space is W_odd tensor (C q0)*, of dimension six. Fixing the representative q0 identifies it with W_odd. Statement (3) requires the constant-rank-open hypothesis; it is not asserted at an exceptional even point with extra corank.

## 2. Parity and the necessary dimension match

The imported equivariant index gives unique nonnegative integers a,b with

    dim K_+=a+4, dim K_-=b,
    dim C_+=a,   dim C_-=b+4,
    m=a+b+4.                                                       (4)

For odd v, equivariance of the multiplication map implies

    iota_C rho_v = -rho_v iota_K.

Hence rho_v has precisely two potentially nonzero blocks:

    K_+ -> C_-,   K_- -> C_+.

Their dimensions give

    rank rho_v <= 2 min(a,b)+4,
    corank rho_v >= |a-b|.                                         (5)

In particular first-order invertibility is possible only if a=b. If a=b, it requires invertibility of both actual blocks, of sizes a+4 and a. No such invertibility is inferred merely from the dimension match.

Under the additional hypothesis m=4, one has a=b=0. Then K is entirely even, C entirely odd, and (1) is the actual linear six-parameter family

    W_odd -> Hom(K,C), dim K=dim C=4.                               (6)

Its determinant is an intrinsically defined quartic polynomial on W_odd with values in det(C) tensor det(K)^(-1). Its nonvanishing is not proved here. In particular dimension six is not evidence that W_odd is the space of alternating forms on K.

## 3. A sufficient criterion for escape and its precise converse boundary

Choose invariant complements A=K directsum A' and D=I directsum C, where I=im M(q0), and let J:A'->I be the invertible restriction of M(q0). In the order (A',K) and (I,C), write

    M(q0+t v) = [ J+t A_v,  t B_v ; t C_v,  t D_v ],

where D_v=rho_v. Over C[[t]], its exact Schur complement is

    S_v(t)=t rho_v - t^2 C_v (J+t A_v)^(-1) B_v.                    (7)

The determinant identity is

    det M(q0+t v)=det(J+t A_v) det S_v(t).                          (8)

Consequently invertibility of rho_v gives

    det M(q0+t v)=t^m det(J) det(rho_v)+terms of higher order.

Thus an invertible first variation proves that the actual determinant is not identically zero, and a general nearby q0+t v is full-adjoint good. Smoothness also persists because q0 is smooth. This would prove generic smooth-quadric twist-four vanishing, but not prescribed-source membership or higher lifting.

Conversely, singular rho_v does NOT prove that this line fails to escape. The exact criterion is that det S_v(t) be nonzero as a formal power series, equivalently that the actual polynomial det M(q0+t v) not be identically zero. Higher terms in (7) can remove the remaining kernel. The Schur presentation depends on complements, but its invertibility and determinant order do not: changing complements acts by invertible formal changes of source and target.

For arbitrary a,b, (5) and (7) give the lower bound

    ord_t det M(q0+t v) >= m+|a-b|=2 max(a,b)+4,                    (9)

with infinite order allowed. Indeed the coefficient t rho_v has rank at most m-|a-b|, so at least |a-b| determinant contributions require an additional power of t. This is an order constraint, not existence of a nonzero coefficient at that order.

## 4. Exact-corank-four pencils have only odd effective orders

Assume m=4 and let v be odd. The invariant complements used in (7) imply

    iota_C S_v(t)=S_v(-t) iota_K.

Since iota_K=+1 and iota_C=-1, this becomes

    S_v(-t)=-S_v(t).

Therefore the effective pencil is an odd power series:

    S_v(t)=t rho_v+t^3 S_3+t^5 S_5+... .                            (10)

This is stronger than the original ambient multiplication pencil being linear: the eliminated complement can contribute higher orders, but parity excludes all even orders in this particular effective block.

If the actual first variation has rank r, then

    ord_t det M(q0+t v) >= 4+2(4-r)=12-2r.                         (11)

To see this, factor t from each of four columns in (10). At least 4-r columns in the remaining determinant must use a term divisible by t^2. Thus the lower bounds for r=4,3,2,1,0 are respectively4,6,8,10,12. Only r=4 guarantees a nonzero coefficient at the displayed lower bound. No r is evaluated or assumed.

## 5. The full determinant's normal quartic

Let Delta(q)=det M(q), without assuming this polynomial is nonzero. The exact kernel-cokernel sequence and the imported equivariant index imply

    [A]-[D]=4(1-sign).

In particular the negative-eigenspace dimensions of A and D differ by four. Thus det(iota_D)/det(iota_A)=1 and

    Delta(q_even+q_odd)=Delta(q_even-q_odd).                         (12)

The determinant is even in all odd variables. Moreover every smooth even q has corank at least four, so all determinant derivatives of total order below four vanish there. Density of this smooth transverse open in W_even implies

    Delta belongs to I(W_even)^4.                                 (13)

The first possible nonzero normal term is therefore degree four in the six odd coordinates. Since Delta is homogeneous of degree85, this term has bidegree(81,4) in the even and odd coordinates. In projective form it is a section of O_P(W_even)(81) tensor Sym^4(W_odd*), up to the fixed determinant line.

At any even point of corank exactly four, this normal quartic is det(rho_v), multiplied by the nonzero determinant of the invertible complementary block in a local trivialization. If every even point has larger generic corank, or if all the actual first variations are singular, this quartic can be identically zero. Equations (12)–(13) do not prove determinant nonvanishing.

## 6. What trace and Serre duality actually provide

The fiberwise trace pairing is nondegenerate and symmetric on B=End_0(F), so B is self-dual. On P4, however, Serre duality gives

    H1(B(2))* = H3(B(-7)),
    H1(B(4))* = H3(B(-9)).

It does not identify A with D*. The transpose of multiplication by v is multiplication by v from H3(B(-9)) to H3(B(-7)). Hence it identifies the transpose derivative

    rho_v*:C* -> K*,

not a self-pairing on K.

On the smooth quadric Q0, omega_Q0=O_Q0(-3), with its actual even-inversion linearization, and the dual spaces are

    K*=H3(Q0,B_Q0(-7)),
    C*=H2(Q0,B_Q0(-7)).

These are different cohomological degrees. Therefore trace and Serre duality alone do not make rho_v symmetric or alternating. At exact corank four there is an additional elementary obstruction to a genuine equivariant identification C=K*: C is odd and K* is even. An identification would require at least a separately justified sign twist and an actual geometric construction; neither is supplied by dimension counting.

Thus no Pfaffian, skew4-by4, symplectic, or automatic determinant-square conclusion is asserted. The valid escape criterion is invertibility of the actual map (1), or more generally nonvanishing of the exact Schur determinant (8).

## Dependencies and limits

The ambient 85-dimensional multiplication and kernel identification are pinned in EVERY-PRODUCT-QUADRATIC-IS-ADJOINT-BAD.md; the full primary/residual extension interpretation is in GENERIC-QUADRATIC-FLANKS.md. The even Euler theorem is the separate INVERSION-EVEN-QUADRICS-ARE-ADJOINT-BAD.md. The present theorem needs no good-flank intersection with the even family, no selected HM coefficients or actual rank computation, and no assertion that its generic corank is four.

What remains is an actual proof that some odd perturbation passes the criterion, or control of the higher effective terms if every first variation is singular. The restrictions above do not resolve that existence question.

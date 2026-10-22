# The actual line-factor image is the six-nodal sextic

## Theorem

The actual HM determinant-cubic family has the sextic line-factor image, not the invariant-conic image. Its normalization is the genus-four factor cover B, with

    L=f*O_P(V*)(1)=K_B+2tau,       tau=M-N,

where M is the degree-three parameter pencil and N is the other canonical ruling. The image has exactly six ordinary nodes, at the nonisotropic axes in the dual plane. Their twelve preimages are the ramification divisor R_M of the parameter map.

At each of the twelve order-five parameters, the determinant cubic is the double polar line of its associated axis together with one of the two order-five invariant tangent lines. It is smooth at that associated axis.

More precisely, a distinguished order-five eigenvector in the actual two-dimensional section space of E=F_R(2) has a zero scheme supported at just two fixed points of the positive plane: a curvilinear length-two scheme at the nonisotropic axis and a curvilinear length-four scheme at one isotropic fixed point. This Chern-length argument proves smoothness at the axis without evaluating any actual coefficient.

## 1. Actual equivariant inputs

The actual positive-plane bundle has the equivariant Steiner presentation

    0 -> A tensor O_R(-1) -> D tensor O_R -> E -> 0,
    R=P(V),       A=Sym^2 W,       D=Sym^4 W,
    c1(E)=3,       c2(E)=6,       H0(E(-1))=0.

The two genuine three-dimensional representations A and V are inequivalent. The actual section two-plane at parameter lambda is

    Y_lambda=ell_lambda^3 W subset D=H0(E).

These facts, including the tautological linearization of O_R(-1), are established in INVARIANT-HYPERPLANE-DETERMINANT-CUBIC-CONES.md and DETERMINANT-CUBIC-FAMILY-RATIONAL-SEXTIC.md. The latter identifies the determinant cubic with the wedge of the two sections in Y_lambda.

Fix an order-five element and an order-five lift to the binary group. Write weights modulo five. Choose its weights on W to be 1,-1. Then

    A: 0,2,3;       D: 0,1,2,3,4;       V: 0,1,4.

Let p,z,r be the three fixed points of R whose tautological point weights are 0,4,1 respectively. Thus p is the nonisotropic axis, and z,r are isotropic. Choose the special parameter whose ell has weight 1. The two lines in Y have weights 4 and 2. Denote corresponding nonzero sections by t and w.

At any fixed point of tautological weight k, the source fiber of the Steiner injection has weights A+k. The injection is a subbundle injection, so the quotient weights are obtained by removing these three distinct weights from D. Consequently

    E_p: 1,4;       E_z: 0,3;       E_r: 0,2.

The weight-2 section w therefore vanishes at p and z. The weight-4 section t has nonzero evaluation at p: its one-dimensional weight line in D is not in the source fiber. Likewise w(r) is nonzero.

## 2. Every nonzero section has a zero scheme of length six

A divisorial zero of a nonzero section of E would produce a section of E(-d) for some d>=1. Multiplying by a nonzero polynomial of degree d-1 would contradict H0(E(-1))=0. Thus the section has no divisorial zero.

On the smooth plane its nonempty zero scheme is consequently a regular codimension-two zero scheme, and its length is c2(E)=6. This applies in particular to w. At each zero the two local components form a regular sequence. We use the elementary local intersection inequality

    length C[[x,y]]/(f,g) >= ord(f) ord(g)

for such a regular sequence. No assertion about the actual initial coefficients is inserted into this inequality.

## 3. The permitted first derivative at the axis cannot vanish

At p the completed local ring has eigen-coordinates x,y of function weights 1,4. These are the duals of the two tangent weights; the unordered pair happens to be unchanged by dualization.

Choose an equivariant formal frame of E with weights 1,4. Such a frame exists by lifting fiber eigenvectors and averaging over the finite cyclic group, followed by Nakayama's lemma. Since w has section weight 2, its component functions have weights

    f: 1,       g: 3.

The only allowed linear monomial in f is x, and there is no allowed quadratic monomial of weight 1. Thus, if that linear term vanished, ord(f)>=3. The function g has no constant or linear term, so ord(g)>=2. The local intersection inequality would give a zero of length at least six at p. The distinct forced zero z would then make the total length at least seven, impossible.

Therefore the linear term of f is nonzero. The derivative of w has a nonzero component in the weight-1 fiber direction, while t(p) is a nonzero weight-4 vector. Hence

    d(t wedge w)_p = t(p) wedge dw_p

is nonzero. The actual determinant cubic is smooth at p.

This conclusion is forced by equivariance, regularity and Chern length; it is not an evaluation or selection of an actual HM coefficient.

## 4. The exact zero lengths are two and four

At p, eliminate x using the nonzero linear term of f. The quotient by f is C[[y]], equivariantly, with y of weight 4. The image of g has weight 3 and is nonzero because the zero is isolated. Its order k satisfies

    4k=3 mod 5,       hence k=2 mod 5.

The total zero length is six and z is another zero, so k cannot be seven or larger. Thus the length at p is exactly two, and the local zero algebra is C[[y]]/(y^2).

At z the tangent weights, computed relative to its point weight 4, are 1,2. The cotangent/function weights are therefore 4,3. Choose corresponding eigen-coordinates u,v and an equivariant frame of E with weights 0,3. The components of w have weights

    F: 2,       G: 4.

There are no linear monomials of weight 2, so ord(F)>=2. The only allowed linear term in G is u, and there are no quadratic monomials of weight 4. If that linear term vanished, ord(G)>=3, producing length at least six at z in addition to the already established length two at p. Thus G has a nonzero linear term.

Eliminating u leaves a one-variable ring C[[v]] with v of weight 3. The nonzero image of F has weight 2; its order l satisfies

    3l=2 mod 5,       hence l=4 mod 5.

The remaining Chern length is at most four. Therefore l=4, the local zero algebra is C[[v]]/(v^4), and there are no other zeros of w.

The conjugate choice of special parameter interchanges the two isotropic fixed points. A5 transports the statement to all twelve special parameters.

## 5. Consequence for the actual factor image

TWELVE-ORDER-FIVE-CUBIC-SPECIALIZATIONS.md gives the independent specialization eigenspace. In suitable global point coordinates X,Y,Z, its possible cubic equations are

    Y(a X^2+b YZ).

The actual three-line factorization is established by [REDUCED-DETERMINANT-THREE-CONIC-PENCIL.md, immutable pin 35fc96bebf9c771a4de481c753bb527e510cd8c1](https://github.com/Akilleez-QA/read-em-and-weep/blob/35fc96bebf9c771a4de481c753bb527e510cd8c1/research/hm/order-four-quadratic-load/REDUCED-DETERMINANT-THREE-CONIC-PENCIL.md). Thus a special cubic is either Y^2 Z or X^2 Y. The former is singular at its associated axis [1:0:0]; the latter is smooth there. Section 3 forces the latter.

THREE-LINE-FACTOR-COVER-GEOMETRY.md and THREE-LINE-POLARIZATION-SIGN-AND-SPECIAL-FIBERS.md identify the two possible line-factor images and their special fibers. A conic image would make both factors tangent lines, giving Y^2 Z. It is excluded. The actual image is therefore the six-nodal sextic; the double factor is the polar line, the node-preimage orbit is R_M, and plane adjunction gives

    K_B=3L-R_M,       R_M=2K_B+tau,
    3(L-K_B)=tau,       L=K_B+2tau.

The last equality uses the already established exact order five of tau and the cyclic order-five group of degree-zero A5-linearized line bundles.

## Scope

The smoothness and length-two-plus-four statements in Sections 2–4 do not use the curve classification or the three-line alternative. Those inputs enter only the final identification of the actual factor image. The proof makes no remaining adjoint-rank claim, performs no actual coefficient or matrix-rank evaluation, and does not assert that all section zero schemes have this special two-point support.

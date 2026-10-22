# Complete fixed-divisor classification for universal third symbols

## Inputs and scope

Work over C. Let G=A5 act on A=Sym^2 W, let X=P(A), and let D=Sym^4 W be the irreducible five-dimensional representation. Here W is the compatible binary-icosahedral representation. Write C=(delta=0) for the smooth discriminant conic. Write P for the genuine four-dimensional representation.

The following pinned interfaces are inputs, not reconstructed actual-operator computations:

- [Universal second symbol](https://github.com/Akilleez-QA/read-em-and-weep/blob/6c724c3b74e2ae4d6992d8c7b99b41c0715d69c0/research/hm/order-four-quadratic-load/POSITIVE-SECOND-BOCKSTEIN-UNIVERSAL-SYMBOLS.md): a G-invariant length-24 scheme Z, disjoint from C, with resolution

  0 -> A O_X(-8) -> P O_X(-6) -> I_Z -> 0.             (1)

- [Third-channel restriction](https://github.com/Akilleez-QA/read-em-and-weep/blob/6c724c3b74e2ae4d6992d8c7b99b41c0715d69c0/research/hm/order-four-quadratic-load/THIRD-BOCKSTEIN-POLARIZATION-AND-SQUARE-DIRECTION-GATE.md): the universal third-symbol space T=Hom_G(D,H0(I_Z(9))) has dimension two, with exact restriction sequence

  0 -> Hom_G(D,H0(I_Z(7))) --delta--> T
    -> Hom_G(D,H0(O_C(9))) -> 0,                     (2)

  whose dimensions are 1,2,1. Every nonzero map in the rightmost line is basepoint-free on C.

The actual nonzero second symbol gives (1). No nonzero actual third symbol is assumed. The corrected-operator boundary and physical source marking remain unchanged from [PR651](https://github.com/Akilleez-QA/read-em-and-weep/pull/651), commit b19ee9b0c995c037b37bfe6e71a51f95847cac11. This note concerns all possible equivariant third symbols, not the choice of the actual one.

## 1. The discriminant-divisible line is primitive after one division

Choose any nonzero generator

  tau:D -> H0(I_Z(7))

of the one-dimensional leftmost space in (2). Its restriction to C is nonzero. Indeed, since Z and C are disjoint, the kernel of restriction H0(I_Z(7))->H0(O_C(7)) is delta H0(I_Z(5)). Twisting (1) by five gives H0(I_Z(5))=0: both negative line-bundle section spaces vanish, as does H1(O_X(-3)).

In fact tau|C is basepoint-free. Identify C with P(W) via the quadratic Veronese, so its five sections are binary forms of degree fourteen. The map is injective because D is irreducible and the restriction is nonzero. Suppose these forms had a nonconstant gcd g. Its divisor is invariant under the projective icosahedral group. Every point stabilizer for a finite faithful group acting on P1 is cyclic: the derivative at a fixed point is faithful, since a finite-order automorphism tangent to the identity is the identity. The cyclic subgroup orders in A5 are 1,2,3,5; its orbit sizes on P1 are therefore 60,30,20,12. A nonempty invariant effective divisor of degree at most fourteen must consequently have degree twelve. The line spanned by g is invariant under the binary icosahedral group; that group is perfect, so its character is trivial. Dividing by g gives a nonzero equivariant injection

  D -> Sym^2 W,

impossible by dimensions (five versus three). Thus the common zero scheme of tau|C is empty.

This argument handles multiplicities: degree fourteen allows precisely one reduced orbit of degree twelve, not a thicker orbit. It needs neither equations for an invariant sextic on X nor selected parameter values.

## 2. Global fixed divisors are completely classified

For a nonzero sigma in T, consider its five degree-nine polynomial components in Sym^9 A*. Their gcd, defined up to a nonzero constant, determines the complete fixed divisor of the linear system.

If sigma|C is nonzero, it is basepoint-free on C by the pinned restriction theorem. No nonconstant polynomial can divide all five components. Otherwise its projective zero divisor would meet C by Bezout (or ampleness of C), and any such intersection point would be a common zero of the restricted system. This remains true if the divisor contains C itself.

If sigma|C is zero, exactness of (2) gives sigma=c delta tau with c nonzero. Section 1 and exactly the same ampleness argument show that tau has no nonconstant common factor. Hence the complete gcd of sigma is delta, with multiplicity exactly one.

Therefore the alternatives for a nonzero universal third symbol are exactly:

- nonzero square channel: no fixed divisor;
- zero square channel: the discriminant conic, with multiplicity exactly one, and no other fixed divisor.

The root cause is that a complete curve in P2 cannot avoid the discriminant conic. The additional input needed to classify the second branch is the new basepoint-freeness of the degree-seven primitive channel. No classification of invariant plane curves is needed.

## 3. The finite residual base schemes and a quantitative bound

Let V be the image of sigma when its square channel is nonzero, and the image of tau in the other branch. Put d=9 or d=7 respectively. In both cases V is a five-dimensional G-stable subspace of H0(I_Z(d)), has no fixed divisor, and is basepoint-free on C. Define B by its image ideal sheaf:

  im(V tensor O_X(-d) -> O_X)=I_B.                  (3)

Then B is a finite G-invariant scheme, is disjoint from C, and contains Z scheme-theoretically. In the discriminant-divisible branch the original degree-nine image ideal sheaf is exactly delta I_B; this is a statement about sheaves and includes the finite structure, not only a statement about support.

A useful bound improving the elementary d^2 Bezout bound is

  24 <= length(B) <= d^2-d-2.                      (4)

Thus length(B)<=70 in the nonzero-square branch, and length(B)<=40 for the primitive discriminant branch.

Here is a proof allowing arbitrary nonreduced finite schemes. Choose two sufficiently general members f,g of V. Since V has no fixed divisor, f and g have no common irreducible factor, so T0=V(f,g) is a complete intersection of type (d,d), contains B, and has length d^2. Let R be the residual finite scheme defined by I_R=(I_T0:I_B). Complete-intersection residual duality gives

  length(B)+length(R)=d^2,
  h0(I_B(d))-2=h1(I_R(d-3)).                       (5)

For clarity, the second identity is the degree-d plane linkage identity: the Koszul resolution of I_T0 has dualizing twist 2d-3, and residual duality identifies the quotient of degree-d forms through B by the two defining equations with the dual of the cokernel of evaluation of degree-(d-3) forms on R. Thus its dimension is precisely the indicated H1. The first identity and this duality apply to any zero-dimensional subscheme of a plane complete intersection, without reducedness or local complete-intersection assumptions on B.

Since V has dimension five, (5) implies h1(I_R(d-3))>=3. For a finite plane scheme of length r, its Hilbert function satisfies

  h_R(t)>=min(r,t+1),  t>=0.                       (6)

One elementary justification is to choose a linear form nonvanishing on its support. It acts injectively on its saturated homogeneous coordinate ring; the resulting Artinian reduction has a Hilbert function with no internal zero before its final nonzero degree. Therefore the cumulative Hilbert function increases by at least one at every step before reaching r. Since h1(I_R(t))=r-h_R(t), taking t=d-3 in (6) forces r>=d+1. This first gives length(B)<=d^2-d-1. Equality is impossible here (d is seven or nine). If equality held, r=d+1 and h_R(d-3)=d-2. If R were not contained in a line, h_R(1)=3. The same no-internal-zero argument then gives h_R(t)>=min(r,t+2) for t>=1, contradicting this equality at t=d-3. Thus R would be contained scheme-theoretically in a line L. Both degree-d forms f and g would then restrict to sections on L vanishing on its length-(d+1) subscheme R. A nonzero section of O_L(d) has zero scheme of length exactly d, so both restrictions vanish identically. This makes L a common component of f and g, a contradiction. Therefore length(R)>=d+2, proving (4).

Because I_B is contained in I_Z, the finite sheaf I_Z/I_B has length length(B)-24. Consequently its length is at most 46 or 16 respectively. This is the precise excess length; it is not asserted to be the length of a disjoint residual subscheme. In particular, additional thickness at points of Z is included in this quotient length. The number of common-zero points outside Z is also at most 46 or 16, respectively.

## 4. Intrinsic kernel bundle and the rank-gain consequence

The primitive system gives an exact sequence

  0 -> E_V -> D tensor O_X -> I_B(d) -> 0.          (7)

The kernel E_V is locally free of rank four. At a point of B the ideal of a finite subscheme of a regular surface has projective dimension one, so its first syzygy is free; away from B this is immediate. It follows that

  det(E_V)=O_X(-d),
  c2(E_V)=d^2-length(B).

In particular c2(E_V)>=d+2, and c2(E_V)<=d^2-24. The injection in (7) is not a vector subbundle at B; no pointwise fiber-injectivity claim is made there.

For the actual third symbol, IF it is nonzero, the classification proves generic third-order rank gain. More precisely:

- If its square channel is nonzero, its map to the residual target line is nonzero outside the finite scheme B, including at every square direction. Thus away from Z there are at most 46 exceptional projective directions, counted with the above scheme-length budget.
- If its square channel is zero but the symbol is nonzero, its vanishing away from Z consists of the discriminant conic together with a finite scheme of primitive basepoints; outside the conic there are at most 16 exceptional directions beyond Z, with the same interpretation.

At points of Z the target is I_Z(9), not a line bundle, so this argument does not decide the fiber rank there. Neither alternative proves that the actual third symbol is nonzero, and no actual coefficient is determined. The original fixed-coefficient problem, actual source membership, full obstruction vanishing, and higher lifting remain open.

## Contribution and verification boundary

The new result is the complete fixed-divisor classification, including exact multiplicity one on the discriminant-divisible channel, followed by a finite scheme bound and canonical kernel bundle for each primitive system. It strengthens the existing square-direction theorem to a global exclusion of all other failure curves. The inputs and all calculations are universal and structural. No selected actual HM/source coefficients, pointwise matrices or ranks, scans, or large computations are used. Independent mathematical review is separate from proof-assistant certification or reconstruction of the full HM foundations.

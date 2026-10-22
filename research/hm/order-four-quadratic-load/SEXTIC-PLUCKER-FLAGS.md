# The residual sextic forces a Grassmannian flag

## Conclusion

Assume the actual Rao branch a=0,b=4 and its established integral ACM sextic D in the hyperplane H. Let U=H^0(E), dim U=4, and let Z=C intersect H, a set of 25 smooth points of D. Then at least one of the following necessary configurations holds:

1. A fixed nonzero section s in U vanishes identically on D.
2. A fixed three-dimensional subspace B of U has evaluation rank at most one everywhere on D.

More precisely, the induced kernel map from D to Gr(2,U) either has image a line, and both flag properties hold, or has image an integral plane quintic spanning a plane contained in Gr(2,U). The two types of Grassmannian planes yield alternatives 1 and 2 respectively.

This is a necessary structure, not an exclusion of the sextic branch, a conclusion about a selected source, or a proof of Q4. All arguments are symbolic.

## 1. The actual image bundle and the degree-five line bundle

The six actual maximal minors generate I_C. On D they therefore generate precisely the ideal of Z: outside Z evaluation has rank two; at Z, since Z consists of smooth points of D and I_C restricts to the reduced point ideal, the restricted minors generate its maximal ideal. Put

    L = O_D(5)(-Z),  deg L = 30-25 = 5.

The six minors, after removing their common Cartier zero divisor Z, generate L without base points.

This operation has an intrinsic bundle interpretation. Let J be the image of U tensor O_D -> E|D. Away from Z it equals E|D. At any point of Z the local ring of D is a DVR, the evaluation has rank one modulo the maximal ideal, and its determinant ideal is that maximal ideal. Thus elementary divisors give a local form diag(1,t) for the image inclusion. Consequently J is locally free of rank two, U tensor O_D surjects onto J, and

    0 -> J -> E|D -> T -> 0,

where T has length one at each point of Z and is supported precisely on Z. In particular det J=L. The quotient U tensor O_D -> J defines a morphism

    f: D -> Gr(2,U)

using the kernel convention, and f^*O_Gr(1)=L. These are the actual kernels off Z and their intrinsic extension across Z. We do not identify E|D with the pulled-back universal quotient: that quotient is J, not E|D.

## 2. Exactly two possibilities for the image span

The ACM resolution gives p_a(D)=3. Integral curves are Cohen–Macaulay, so duality applies even if D is not Gorenstein. The dualizing sheaf omega_D is rank-one torsion-free of degree 2p_a-2=4. Hence omega_D tensor L^(-1) has degree -1 and no nonzero global section: a nonzero section of a rank-one torsion-free sheaf on an integral curve injects O_D with finite-length quotient, forcing nonnegative degree. Therefore H^1(L)=0. Riemann–Roch gives

    h^0(L)=deg L+1-p_a(D)=3.

Let V be the image of the six-dimensional minor space in H^0(L), and r=dim V. Since V generates L of positive degree, r is not one. Thus r=2 or 3.

If r=2, f has image a projective line and degree five onto that line. Since its image lies in Gr(2,U), the whole line lies in the Grassmannian.

If r=3, its image Gamma spans a plane. The morphism to Gamma is finite, and

    5 = deg L = deg(f) deg(Gamma).

Since Gamma is nondegenerate in its plane, deg Gamma is at least two. Thus deg Gamma=5 and deg(f)=1. The Plucker Grassmannian Gr(2,4) is a quadric in P^5. Its equation restricts to a quadratic on the spanning plane. Such a quadratic cannot vanish on an integral plane quintic unless it vanishes identically. Thus the entire spanning plane lies in Gr(2,U).

As an additional precise description in this second case, f is a finite birational map onto an integral plane quintic. The quotient f_*O_D/O_Gamma has length three, since p_a(Gamma)=6 and p_a(D)=3. No smoothness or normality of D is asserted.

## 3. Grassmannian lines and planes give actual section flags

A line in Gr(2,U) has the form

    { K : A subset K subset B },  dim A=1, dim B=3.

A plane in Gr(2,U) has exactly one of the forms

    alpha: { K : A subset K }, dim A=1;
    beta:  { K : K subset B }, dim B=3.

Here is an elementary verification of the classification used. Two distinct points of a projective linear subspace of decomposable bivectors correspond to two planes K1,K2 meeting in a line A; otherwise their sum would have nonzero exterior square. Let B=K1+K2, of dimension three. Any other plane K in that linear subspace meets both K1 and K2. Such K either contains A or is contained in B. These two conditions are closed. Irreducibility of the parameter line or plane forces one condition throughout. For a projective plane, the corresponding alpha or beta family already has dimension two, so equality follows. For a line, its span is the pencil specified by A and B.

For an alpha family, the fixed line A is contained in every fibre kernel of U tensor O_D -> J. Hence its nonzero global section maps to zero in J and therefore in E|D. It vanishes identically on D.

For a beta family, every kernel is a two-dimensional subspace of the fixed B. Hence B tensor O_D -> J has rank one everywhere, and its composite to E|D has rank at most one. In particular the three pairwise wedges of sections in B vanish along D. This remains true at Z; no assertion of rank two for E-evaluation there is made.

For a Grassmannian line both conclusions hold simultaneously.

## Dependencies and boundary

The actual integral sextic and smoothness of Z are established in FOUR-CUBIC-SEXTIC-BASE.md. Its ACM resolution and genus are established in INTEGRAL-SEXTIC-ACM-RESOLUTION.md, published at PR543 commit 7c7bf54af204daa4a00ddfec0b69e3c3dda94424. The ideal-generation input concerns the actual six HM evaluation minors. No selected minor or coefficient is computed, and no experiment or external action is performed here.

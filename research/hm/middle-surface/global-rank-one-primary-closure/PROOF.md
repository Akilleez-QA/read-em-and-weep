# Global rank-one primary closure and its original two-zero boundary

## Setup and theorem

Work over C. Let V have dimension five, R=C[V⊕V⊕V], and P=I_D the prime ideal of the rank-at-most-one determinantal cone D. Write the three columns as x,y,z. Let J be the ideal of components of the canonical trilinear map f with outer symmetry and cyclic-zero identity. Assume the audited rank-ten open B of common projective lines is nonempty and that its exact square-zero local normal form is the one in /research/hm/middle-surface/full-boundary-product-blowup/PROOF.md and /research/hm/middle-surface/projective-rank-one-thickening/PROOF.md.

Introduce independent formal variables u=(u_1,…,u_5), r_1,r_2,r_3, and p=(p_1,…,p_5). Put

    A=C[u,r],       E=A[p]/(p)^2,
    φ:R→E,
    (x,y,z)↦(r_1(u+p), r_2u, r_3(u−p)),
    Q=ker φ.

Then:

1. Q is P-primary, P²⊂Q⊂P, and J⊂Q. Its generic transverse length is five.
2. Q is exactly J R_P∩R. In particular it is the unique isolated P-primary component of J, and the scheme-theoretic closure of the audited good, all-inputs-nonzero rank-one component. This identifies its closure through every rank-drop direction, two-zero stratum, and the vertex, without classifying the rest of X=V(J).
3. For F∈R, membership in Q is equivalent to

       F(r_1u,r_2u,r_3u)=0,
       [r_1 ∂F/∂x_i−r_3 ∂F/∂z_i](r_1u,r_2u,r_3u)=0  (i=1,…,5).

   All equalities here are polynomial identities in indeterminates. In particular, for F∈P the second line is the complete criterion. Radial p imposes no extra equation.
4. Q has no nonzero equations of degree one or two. It contains explicit nonzero cubic equations displayed below, and P² supplies equations in degree four. No assertion that these generate Q is made.
5. On a chart where one input coordinate is invertible, the original primary component has an explicit split square-zero algebra. At a point with precisely that input nonzero it is

       O_D ⊕ (b,c) O_D^⊕4,

   where b,c are the scalar coordinates of the other two columns and the second summand has square zero. Thus it is not Cohen–Macaulay at that two-zero point: its local dimension is seven, depth six, and embedding dimension fifteen. These assertions concern V(Q), not the entire X. At the vertex V(Q) also has embedding dimension fifteen and has no quadratic equations.

## 1. Primaryness without a flatness assumption

E=A⊕A^5 is a square-zero algebra over the integral domain A. An element (a,m) with a≠0 is a nonzerodivisor: (a,m)(b,n)=0 first gives ab=0, hence b=0, then an=0, hence n=0. The remaining elements have square zero. Every subalgebra of E has the same property: every zero divisor is square-zero. Therefore the zero ideal of im φ is primary.

The composite R→E→A is the ordinary rank-one parametrization (x,y,z)=(r_1u,r_2u,r_3u). Its kernel is P: every rank-at-most-one matrix is parametrized, and the determinantal cone is reduced and irreducible. Thus √Q=P. Elements of P map to the square-zero ideal, proving P²⊂Q. This also proves that the nilradical P/Q of R/Q has square zero everywhere, including the original vertex. No assertion of local freeness there is implicit.

## 2. The derivative test and radial redundancy

Taylor expansion in the square-zero variables is exact:

    φ(F)=F(ru)+Σ_i p_i [r_1∂_{x_i}F−r_3∂_{z_i}F](ru).

Since 1,p_1,…,p_5 form a free A-basis of E, this proves the criterion.

If F∈P, differentiate the identically zero polynomial F(r_1u,r_2u,r_3u) with respect to r_1 and r_3. It follows that

    Σ_i u_i [r_1∂_{x_i}F−r_3∂_{z_i}F](ru)=0.

Thus the coefficient covector annihilates u. Equivalently p=εu gives the tangent change δr_1=εr_1, δr_2=0, δr_3=−εr_3 within D. It does not create a fifth transverse nilpotent direction.

More explicitly, on u_1≠0 write

    t=u_1,   v=u/t,   q=p/t−(p_1/t)v,   η=p_1/t,

so v_1=1 and q_1=0. Set ρ_1=r_1t(1+η), ρ_2=r_2t, ρ_3=r_3t(1−η). Then exactly modulo (p)^2,

    x=ρ_1(v+q),   y=ρ_2v,   z=ρ_3(v−q).

The extra radial variable η and scale t are redundant parameters. Although η and q have all pairwise products zero in this parameter ring, the kernel on R is unchanged by dropping η: in one direction set η=0; in the other absorb η in the independent scalar coordinates as above. Localization to u_1≠0 loses no polynomial identity, since u_1 is regular on E. This proves radial redundancy even for the full global kernel, not only pointwise tangent spaces.

## 3. Containment of the cubic equations

The cyclic identity at (u,u,u) gives f(u,u,u)=0. Outer symmetry gives f(p,u,u)=f(u,u,p). Trilinearity therefore gives

    f(u+p,u,u−p)=−f(p,u,p)=0 in E.

Multiplication by r_1r_2r_3 proves J⊂Q. This argument uses only the stipulated identities, and no operation or chosen input is evaluated.

## 4. Generic length and identification with the isolated component

On an affine projective chart v_1=1, the normalized construction is precisely

    (x,y,z)=(ρ_1(v+q),ρ_2v,ρ_3(v−q)),   (q)^2=0,

with four q coordinates. When all ρ_i are invertible, the image algebra recovers v,ρ_i,q: take ρ_i to be the first coordinate of input i, v=y/ρ_2, and q=x/ρ_1−v. Thus it is the full displayed square-zero algebra, of rank five over its smooth seven-dimensional reduction. This proves generic transverse length five.

On the good open B, the audited theorem gives exactly the same algebra for J, not just its tangent cone. Hence J R_P=Q R_P. In particular P is a minimal prime of J: on the dense good all-nonzero rank-one open it is the only reduced component. Since Q is P-primary,

    Q=Q R_P∩R=J R_P∩R.

This contraction is the unique isolated P-primary component in every primary decomposition of J. It also proves the stated closure assertion: restricting V(Q) to any nonempty open meeting its generic point is schematically dense, because every element outside P is regular on R/Q. The good open is such an open. The resulting extension is independent of how the good open was presented and requires no rank-ten hypothesis at its boundary points.

The statement does not identify J with Q at the boundary. Other components and embedded structure of J can remain there.

## 5. Low-degree consequences and explicit cubic construction

For i<j define

    M12_ij=x_i y_j−x_j y_i,
    M23_ij=y_i z_j−y_j z_i,
    M13_ij=x_i z_j−x_j z_i,
    U_ij=u_i p_j−u_j p_i.

Their images are

    φ(M12_ij)=−r_1r_2 U_ij,
    φ(M23_ij)=−r_2r_3 U_ij,
    φ(M13_ij)=−2r_1r_3 U_ij.

P has no degree-one part. Its degree-two part is the linear span of these thirty minors. The three r monomials are distinct, and the ten U_ij are linearly independent over C. Consequently φ is injective on P_2, and

    Q_1=Q_2=0.

In particular the global primary component cannot be defined by quadrics and is not the ordinary first infinitesimal neighborhood P²: it already has nonzero cubic equations. For every i<j and k, the following lie in Q:

    z_k M12_ij−x_k M23_ij,
    y_k M13_ij−2z_k M12_ij.

Their images cancel by the preceding identities. These families contain nonzero polynomials, as is visible directly from their monomial expansions. All 3×3 minors of [x y z] also belong to Q, since its columns lie in the formal span of u and p; equivalently these determinants have zero constant and first-order terms at rank one. Finally P²⊂Q supplies every product of two 2×2 minors. These are explicit certified equations and exclusions, not a claimed generating set or Hilbert-series computation.

At the original vertex the first three graded pieces of R/Q consequently have dimensions 1,15,120. The Zariski tangent space is the full fifteen-dimensional ambient space, and its degree-two relations are empty. The cubic formulas give actual third-degree constraints. These vertex claims do not presume that the global extension splits over D.

## 6. Exact original two-zero local algebra

Work on x_1≠0. Set a=x_1, v=x/a, b=y_1, c=z_1; thus v_1=1. Put, for i=2,…,5,

    Y_i=y_i−b v_i,       W_i=(z_i−c v_i)/2.

The reduced rank-one chart has regular coordinate ring

    A_0=C[a,a^−1,v_2,…,v_5,b,c].

Normalize the universal expression using its first column rather than its middle column. The same radial absorption from Section 2 gives four square-zero variables q_i and the exact formulas

    x=a v,       y=b(v−q),       z=c(v−2q).

Hence Y_i=−bq_i and W_i=−cq_i. The image algebra is exactly

    A_0 ⊕ ((b,c)A_0)^⊕4,

with square-zero multiplication on the second summand. To verify this is the localization of R/Q, localize the original parameter ring where x_1=r_1(u_1+p_1) is invertible; then r_1,u_1 are invertible and the normalization is valid. Conversely the normalized formulas occur by setting u=v−q, p=q and choosing the appropriate scalar parameters. Thus the kernels agree in both directions.

Equivalently the local defining ideal, in A_0[Y_2,…,Y_5,W_2,…,W_5], is generated by

    cY_i−bW_i  (i=2,…,5),
    all pairwise products of the eight variables Y_i,W_i.

Indeed the kernel of A_0²→(b,c), (s,t)↦bs+ct, is generated by (c,−b), since b,c form a regular sequence. Applying this independently to four coordinates gives precisely the linear-in-Y,W module relations; square-zero multiplication gives the remaining relations.

If at least one of b,c is invertible, (b,c)=A_0 and this recovers the locally free rank-four nilradical and transverse length five. At a two-zero point b=c=0, the nilradical is not free: its fiber over the reduced local ring has dimension eight. Localizing A_0 at that closed point gives a regular local ring of dimension seven. The resolution

    0→A_0→A_0²→(b,c)→0

is minimal there, so (b,c) has depth six. Consequently the split algebra has depth six and dimension seven, and is not Cohen–Macaulay. The depth statement can also be computed by local cohomology for the base maximal ideal, whose extension has the same radical as the local maximal ideal of the square-zero algebra. Its embedding dimension is 7+8=15, also immediate because all displayed relations have order at least two at b=c=Y=W=0.

The same argument applies on a chart with the middle or third column nonzero. With the middle as base, the offsets of the outer columns are a q and −c q; with the third as base, analogous nonzero factors occur. After harmless constant rescalings the nilmodule is again the ideal generated by the two vanishing scalar coordinates, repeated four times. Thus all three two-zero strata have this exact primary-component model, irrespective of whether the common line lies in B.

## Scope and comparison with the resolved extraction

This result pushes beyond the resolved product-blowup description by computing its scheme-theoretic image, equivalently the isolated primary closure, in the original affine space. The resolved nilradical is locally free even on the scalar boundary; the image nilradical is the nonfree module (b,c)^⊕4 on a two-zero chart. Accordingly the resolved Cohen–Macaulay model does not imply a Cohen–Macaulay original primary component. This is compatible with the nonfinite blowup fibers in the imported proof.

The proof gives a full intrinsic kernel/derivative description of the global ideal Q, a finite local presentation off the vertex, and some certified homogeneous equations. It does not claim a homogeneous generating set for Q, a full primary decomposition of J, or the absence of additional components or embedded structure in X.  All parameters above are formal indeterminates and the stated equations are algebraic.

> Publication scope: preserved mathematical proof/audit. Historical statements that rank eight remains open are superseded only after the final assembly and all its prerequisites. No source-instance evaluation or formal verification is claimed here.

# Sextic surface bounds and the bounded rank-eight Chern restriction

## Result

In the established rank-eight determinant-six branch, the possible ordered pairs are reduced to

    (c2(F), c2(R)) = (14,22), (19,17), or (24,12).

This is a necessary restriction, not an existence assertion or an exclusion of rank eight. It eliminates precisely the four previously allowed pairs (4,32), (9,27), (29,7), and (34,2).

The geometric input, stated slightly more generally, is the following. Work over C. Let d>=4 and let Z be a closed subscheme of P4 of dimension two and degree a>=(d-1)^2+1. Suppose the nonzero system H0(I_Z(d)) has no fixed divisor. Then

    h0(I_Z(d-1)) <= 1,    h0(I_Z(d)) <= d+3.

If additionally h0(I_Z(d-1)) is divisible by five, then

    h0(I_Z(d-1)) = 0,     h0(I_Z(d)) <= d+2.

For d=6 this last upper bound is eight. Schemes may be nonreduced, may have embedded or lower-dimensional components, and need not be arithmetically Cohen--Macaulay.

## 1. Plane schemes and a residual-length argument

Let D be a zero-dimensional subscheme of P2 of length a>=(d-1)^2+1. Suppose a vector space W of degree-d equations vanishing on D has no fixed curve. For any nonzero plane polynomial q, one can choose s in W coprime to q: each irreducible factor of q excludes a proper linear subspace of W, and a finite union of such subspaces does not cover W over C.

There is no nonzero equation q of D of degree d-2. Otherwise choose s coprime to q. Scheme-theoretically D is contained in the complete intersection V(q,s), whose length is d(d-2)=(d-1)^2-1<a, a contradiction. Thus

    h0(I_D(d-2))=0.                                  (1)

All lower-degree equation spaces vanish as well, since multiplying a nonzero lower-degree polynomial by a suitable monomial would contradict (1).

There is at most one independent equation of degree d-1. Indeed, suppose f and g were independent such equations, and let h be their greatest common divisor, of degree t with 0<=t<=d-2. Write f=h f' and g=h g'. The polynomials f',g' are coprime. If t=0, Bezout immediately gives a<= (d-1)^2, a contradiction. For t>0 let D_h=D intersect V(h) and define the residual scheme D' by the ideal quotient I_D:h (as ideal sheaves). The residual exact sequence is

    0 -> O_{D'}(-t) --h--> O_D -> O_{D_h} -> 0.

It follows, without reducedness or transversality assumptions, that

    length(D) = length(D') + length(D_h).

Choose s in W coprime to h. The subscheme D_h lies in V(h,s), so length(D_h)<=dt. Since f',g' belong to I_D:h, the residual D' lies in V(f',g'), giving length(D')<=(d-1-t)^2. Consequently

    a <= dt+(d-1-t)^2
       = (d-1)^2 + t(t-d+2)
       <= (d-1)^2,

again a contradiction. Hence

    h0(I_D(d-1)) <= 1.                               (2)

For sextics the residual bound reads 6t+(5-t)^2<=25 for 0<=t<=4. This is a scheme-length bound, not merely a count of support points.

## 2. Hilbert-function growth through degree d

Let A be the saturated homogeneous coordinate ring of D, with Hilbert function H. A linear form l missing the finite support of D is a nonzerodivisor on A. This can be seen directly: if l f vanishes on D, then f vanishes on D because l is invertible on D; saturation identifies those homogeneous polynomials with I_D.

Multiplication by l therefore shows that H is nondecreasing and that its first differences are the Hilbert function of the standard graded Artinian algebra A/lA. Once a graded piece of this algebra is zero, every subsequent piece is zero, since it is generated in degree one. As H is eventually a, it follows that

    H(j)<a implies H(j+1)>H(j).

Equation (2) gives H(d-1)>=binom(d+1,2)-1. For d>=4,

    a >= (d-1)^2+1 >= binom(d+1,2).

If H(d-1) is already at least binom(d+1,2), monotonicity suffices. Otherwise strict growth gives the same lower bound at degree d. Thus

    H(d)>=binom(d+1,2),
    h0(I_D(d)) <= binom(d+2,2)-binom(d+1,2) = d+1.    (3)

For d=6, (2) says H(5)>=20, and a>=26 forces H(6)>=21, so h0(I_D(6))<=7.

## 3. Two regular hyperplane sections

Return to the surface Z in the theorem. Choose a general hyperplane H=P3, then a general plane L=P2 inside H. Put C=Z intersect H and D=C intersect L scheme-theoretically. At each stage choose the hyperplane equation to avoid the finitely many associated points of the relevant structure sheaf. Each is then a nonzerodivisor. This is possible even when there are embedded components: zero-dimensional associated points can be avoided entirely, and no positive-dimensional associated subvariety need be contained in a general hyperplane.

Successive differences of the Hilbert polynomial show that C has degree a and D has length a; lower-dimensional components cause no change to the second difference. In particular these sections require neither purity nor Cohen--Macaulayness.

Let B be the base scheme of H0(I_Z(d)). Absence of a fixed divisor means dim(B)<=2. A general L intersects B in dimension at most zero. These conditions and regularity of the flag hold simultaneously on a nonempty open subset of the flag parameter space. The restricted system W on L therefore has no fixed curve and vanishes on D. Sections 1--2 apply to D.

Regularity gives exact ideal-sheaf restriction sequences

    0 -> I_Z(j-1) -> I_Z(j) -> I_{C,H}(j) -> 0,
    0 -> I_{C,H}(j-1) -> I_{C,H}(j) -> I_{D,L}(j) -> 0.

We use only upper bounds on global-section dimensions, not surjectivity on global sections. Starting from h0(I_Z)=h0(I_C)=0, the vanishing of I_D(j) for j<=d-2 gives the same vanishing for I_C(j) and I_Z(j). Next,

    h0(I_C(d-1)) <= h0(I_D(d-1)) <= 1,
    h0(I_Z(d-1)) <= h0(I_C(d-1)) <= 1,
    h0(I_C(d)) <= h0(I_C(d-1))+h0(I_D(d)) <= d+2,
    h0(I_Z(d)) <= h0(I_Z(d-1))+h0(I_C(d)) <= d+3.

If h0(I_Z(d-1)) is divisible by five, its bound by one forces it to be zero. The last inequality then improves to h0(I_Z(d))<=d+2, proving the theorem.

## 4. Applying the bound to equivariant sheaves

Suppose M is an H5-equivariant torsion-free sheaf on P4, of rank s and uniform central weight w=2 or w=3 modulo five, with c1(M)=6, generated outside a subset of codimension at least two. Choose s-1 sufficiently general global sections. The torsion-free section-quotient lemma in ../rank-nine-defect-two-sided/PROOF.md, Section 1, gives

    0 -> O^(s-1) -> M -> I_Z(6) -> 0,                (4)

where Z has codimension at least two and its surface-cycle degree is c2(M). The quotient I_Z(6) is generated outside codimension two, so its complete sextic system has no fixed divisor. If c2(M)>=26, Z meets the hypotheses above with d=6.

Twisting (4) by O(-1), and using H0(O(-1))=H1(O(-1))=0, gives an isomorphism of vector spaces

    H0(M(-1)) = H0(I_Z(5)).                         (5)

The choice of sections and Z need not be equivariant. Only the dimension equality in (5) is used. The space H0(M(-1)) is intrinsically an H5-module. Under the convention that O(m) has central weight -m modulo five, M(-1) has weight w+1 if M has weight w. For w=2 or w=3 this character is nontrivial. The elementary Heisenberg representation lemma in ../heisenberg-defect-hilbert-congruence/PROOF.md, Section 1, implies that its dimension is divisible by five.

It follows from the surface theorem and (5) that

    c2(M)>=26 implies h0(I_Z(6))<=8.               (6)

On the other hand H1(O)=0 in (4) gives

    h0(I_Z(6)) = h0(M)-(s-1).                      (7)

## 5. Rank-eight elimination

In the established determinant-six rank-eight branch,

    E=F*, rank(E)=12, central weight(E)=2,
    rank(R)=8, central weight(R)=3,
    c1(E)=c1(R)=6, h0(E)>=20, h0(R)>=20.

Here E is reflexive and generated outside codimension two, and R is torsion-free and globally generated. The sections bounds follow equivalently from the irreducibility of the twenty-dimensional J and J*: H0(F)=H0(R*)=0, so J injects into H0(R) and J* injects into H0(F*). Since F is reflexive, dualization preserves c2, so c2(E)=c2(F).

Equation (7) gives at least 20-11=9 sextic equations for the surface obtained from E, and at least 20-7=13 for that obtained from R. Either lower bound contradicts (6). Therefore

    c2(F)<=25 and c2(R)<=25.

The previous full-support Chern-congruence list in ../full-support-equivariant-chern-congruences/PROOF.md is

    (4,32), (9,27), (14,22), (19,17), (24,12), (29,7), (34,2).

Deleting pairs with an entry at least 26 leaves exactly

    (14,22), (19,17), (24,12).

## Evidence boundary

Only existing local proof texts, universal sheaf geometry, plane Bezout and residual exact sequences, elementary Hilbert functions, and the abstract Heisenberg dimension lemma are used. No actual physical or HM source, selected input, operation matrix, polynomial instance, rank instance, jet, or residue is evaluated. No external state is changed. The only write is this local proof deliverable.

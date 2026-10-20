# Classify constant-rank-two traceless nets

Over C, a three-dimensional subspace K of sl(W), dim W=3, whose nonzero elements all have rank two is conjugate to the skew-symmetric matrices. Its trace-square form is nondegenerate. No four-dimensional constant-rank-two subspace of Hom(C³,C³) exists. These are universal theorems, with no assertion that a prescribed operation realizes such a kernel.

## 1. The universal kernel on P²

Every nonzero A∈K is singular by the determinant hypothesis, has positive rank, and does not have rank one. Thus it has rank exactly two. On P(K)=P² consider the universal linear map

    φ: W⊗O → W⊗O(1).

Its fiber at a projective class is the corresponding endomorphism, up to the tautological scalar. It has constant rank two. Locally an invertible two-by-two minor splits off an identity block; the remaining block is zero because the determinant vanishes identically. Hence its kernel and cokernel are line bundles. Since Pic(P²)=Z, write them as O(a) and O(b). There is an exact sequence

    0 → O(a) → O³ → O³(1) → O(b) → 0.

The relation in K-theory gives, in Q[H]/(H³),

    exp(aH)−exp(bH)=3−3exp(H).

The degree-one and degree-two coefficients give

    a−b=−3,       a²−b²=−3.

Therefore a+b=1, so a=−1 and b=2. No degree-three equation is available on P², in agreement with the P³ obstruction in Section 5 below.

The kernel inclusion is thus a bundle map

    O(−1) → W⊗O

whose three coordinate sections are linear forms on K. They have no common projective zero because this is a line subbundle inclusion at every point. Equivalently, their underlying linear map u:K→W has no nonzero kernel. Both spaces have dimension three, so u is an isomorphism. The choice of the isomorphism of the kernel bundle with O(−1) changes u only by a nonzero scalar.

Use x=u(A) as the linear parameter of K, and write M(x)=A. The universal kernel equation is then the polynomial identity

    M(x)x=0.

Here both the parameter coordinates x and the endomorphism input coordinates refer to the same chosen basis of W. This is more than an independent left-right equivalence: the resulting normal form still describes endomorphisms of W and retains the trace condition.

## 2. Linear syzygies give a cross-product normal form

Fix the standard symmetric bilinear form and volume form in these coordinates, and let C(x) be the operator v↦x×v. It is skew-symmetric, depends linearly on x, has kernel Cx and image x^⊥ for every nonzero x, including isotropic x.

For completeness the linear syzygy step is elementary. A row r(x) of M(x) consists of three linear forms. Write it as r(x)=x^T D with D a constant matrix. The row equation r(x)x=0 says x^T D x=0 as a polynomial, so D is skew-symmetric. The space of such rows is three-dimensional and is exactly the space of constant linear combinations of the rows of C(x): each such combination is a syzygy, and the map from its constant coefficient vector is injective. Applying this to all rows gives a constant matrix B with

    M(x)=B C(x).

No higher-degree syzygies or saturation assertions enter this argument.

The matrix B must be invertible. If rank B≤1, every M(x) has rank at most one, a contradiction. If rank B=2, let Cv=ker B. Choose nonzero x with x^T v=0; such x exist because this is one linear equation on a three-dimensional space. Then v∈im C(x)=x^⊥, so the restriction of B to the two-dimensional image of C(x) has a nonzero kernel. Thus rank(B C(x))≤1, again a contradiction. These contradictions concern nonzero x, for which M(x) is a nonzero member of K because the parameter map is an isomorphism.

## 3. Trace zero upgrades equivalence to conjugacy

The trace condition reads

    tr(B C(x))=0 for every x.

The operators C(x) range over all skew-symmetric matrices. Under the trace pairing, the orthogonal complement of the skew-symmetric matrices is exactly the symmetric matrices. Indeed, testing against the elementary skew matrices makes the off-diagonal entries of B symmetric. Hence B is symmetric as well as invertible.

Over C, every invertible symmetric matrix admits a factorization B=P P^T with P invertible (equivalently, every nondegenerate symmetric bilinear form has an orthonormal basis). Therefore

    P⁻¹ K P = { P^T C(x) P : x∈C³ }.

Every matrix on the right is skew-symmetric. The map S↦P^T S P is invertible on the three-dimensional space of skew-symmetric matrices, so the right-hand side is that entire space. This proves conjugacy, rather than only arbitrary left-right equivalence.

Conversely the skew-symmetric space has dimension three, consists of traceless singular matrices, and every nonzero member has rank two. Thus the normal form realizes the abstract hypotheses and shows the classification is not vacuous in universal linear algebra. It does not realize an actual K_W.

## 4. The trace-square quadratic and the conic complement

Conjugation preserves tr(A²), so compute the universal quadratic on the skew-symmetric space. The cross-product identity is

    C(x)² = x x^T − (x^T x) I.

Taking trace gives

    tr(C(x)²)=−2(x_1²+x_2²+x_3²).

This quadratic is nondegenerate. Since the conjugacy above induces a linear isomorphism of the parameter spaces, q|K has rank three. Its projective zero scheme is therefore a smooth conic C. The determinant vanishes identically, scheme-theoretically as a polynomial, so the spectral incidence is precisely the smooth irreducible surface

    X=P(K)\C.

This is a scheme statement: there is no residual cubic equation or thickening in this fixed-K incidence.


## 5. No four-dimensional constant-rank-two subspace


**Universal lemma.** A complex linear subspace L⊂Hom(C³,C³) in which every nonzero element has rank exactly two has dimension at most three.

Suppose otherwise and restrict to a four-dimensional subspace. On P(L)=P³ the tautological universal linear map is

    φ: O³ → O³(1).

At every geometric point it has rank two. The rank-at-most-one closed locus is empty, and all three-by-three minors vanish identically because they vanish at every point of the reduced base. On open charts where a two-by-two minor is invertible, elementary bundle operations split off an identity block, with the remaining block zero. Thus its kernel and cokernel are line bundles, not merely coherent sheaves. Since Pic(P³)=Z, they are O(a) and O(b) for integers a,b. Consequently

    0 → O(a) → O³ → O³(1) → O(b) → 0

is exact. Its K-theory relation, followed by the Chern character in CH*(P³)_Q=Q[H]/(H⁴), is

    exp(aH) − exp(bH) = 3 − 3 exp(H).

The coefficients of H, H², H³ give, respectively,

    a−b=−3,   a²−b²=−3,   a³−b³=−3.

The first two imply a+b=1, hence a=−1 and b=2. But then a³−b³=−9, contradicting the third equation. This proves the lemma.


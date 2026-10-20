# One planar factor and one nonplanar surface are impossible

Work over C. Let E have dimension four, U⊂E dimension three, and K⊂Sym²E dimension at most five. Suppose X⊂P(U)×P(E) is an integral surface, its first projection is dominant, its second image is a nonplanar surface, and ab∈K at every ([a],[b])∈X.

**Theorem. Such X does not exist. Compatibility and square avoidance are not needed.**

Replace K by the span K′ of the product image. Every product lies in UE, the nine-dimensional image of U⊗E→Sym²E, whose kernel is Λ²U. Choose E=U⊕Cw. On UE the quotient modulo Sym²U is identified with U by aw↦a.

## 1. The bilinear constraint matrix has generic rank three

The second image is nonplanar, so b has nonzero w-coordinate on a dense open of X. Its first projection is still dense in P(U). Hence the images of products ab modulo Sym²U span U. Therefore K′→U is surjective and

    dim K0 = dim(K′∩Sym²U) = dim K′−3 ≤ 2.

Let q=9−dim K′≥4 and choose a basis of the annihilator of K′ in (UE)*. Its pullback to U⊗E gives q independent bilinear equations. With a=(x,y,z) and b=(b1,b2,b3,b4), their evaluation is a q×4 linear matrix M(a), each row of the form

    R_i(a) = ((A_i a)ᵗ, ℓ_i(a)),

where A_i is a symmetric 3×3 matrix and ℓ_i is linear. Symmetry follows because the equations factor through symmetric multiplication. Generic rank is at most three because X dominates the first plane.

Suppose generic rank were at most two. For every general a, the vector kernel M_a has dimension at least two, so M_a∩U contains a nonzero n. Then an∈K0. The incidence of ordered factors of nonzero quadrics in P(K0) has finite fibers over P(K0), since a quadratic has at most two ordered factorizations up to scalar. Its dimension is consequently at most one (or it is empty). Its first projection cannot contain a dense open of P(U), contradiction. Therefore generic rank M=3.

In particular X is the closure of the graph of the unique generic kernel line of M.

## 2. Adjugate degree bookkeeping

Choose three rows independent over C(P(U)), then a fourth row independent of those three over C. This is possible because all q≥4 original rows are independent over C. Let N be the resulting 4×4 matrix. It has generic rank three and identically zero determinant.

The nonzero adjugate is a homogeneous degree-three matrix of generic rank one. Over C[x,y,z], factor

    adj(N)=h c rᵗ,

where c and r are primitive homogeneous polynomial vectors and h is homogeneous. To justify this without assumptions on minors, choose a nonzero adjugate column, divide by its gcd to obtain primitive c, and express every other column as a rational multiple of c. Unique factorization and primitivity imply that each multiplier is polynomial. Removing the common gcd of these multipliers produces h and primitive r. Homogeneity gives

    deg h + deg c + deg r = 3.

The adjugate identities imply Nc=0 and rᵗN=0. The generic right kernel is that of M, so [c] has nonplanar second image. Thus deg c≥2: a degree-zero map is constant, and a degree-one map from P² has image in a projective plane. If deg r=0, its left-kernel identity is a constant dependence among the four chosen rows, impossible. Therefore

    deg c=2, deg r=1, deg h=0.

Let d be the dimension of the vector span of the four entries of r as linear forms. It is between one and three. Constant invertible row operations transform N and the dual left kernel r, and preserve row independence and the symmetric-block property.

## 3. Left syzygies involving one or two independent linear forms

If d=1, r is a scalar linear form times a nonzero constant vector. Its left-kernel identity gives a constant row dependence (also contradicting primitivity).

If d=2, after constant row operations and source coordinates, r=(x,y,0,0). Then

    xR1+yR2=0.

Since x,y are coprime and the rows have linear entries, R1=y t and R2=−x t for a constant row t. This row is nonzero by row independence. The identity Nc=0 forces t c=0. Thus the second image lies in a fixed hyperplane of P(E), contradicting nonplanarity.

## 4. Three independent linear forms contradict symmetric multiplication

It remains d=3. Constant row operations alone put r=(x,y,z,0), using the ORIGINAL coordinates of U: the rank-three coefficient matrix of r can be taken to the block matrix [I3;0] by an invertible constant transformation. The dual inverse row transformation on N realizes this change. Thus no source or target coordinate change is needed, and every U×U block remains symmetric.

The left-kernel relation gives

    x A1 a + y A2 a + z A3 a = 0,
    x ℓ1(a) + y ℓ2(a) + z ℓ3(a) = 0.

Set F(a)=Σ_{i=1}^3 a_i(aᵗ A_i a). The vector identity implies F=0. Because each A_i is symmetric,

    ∂F/∂a_j = aᵗ A_j a + 2(Σ_i a_i A_i a)_j = aᵗ A_j a.

Thus aᵗ A_j a=0 for every j and every a, so A1=A2=A3=0 in characteristic zero.

Write (ℓ1,ℓ2,ℓ3)ᵗ=B a. The remaining relation aᵗ B a=0 says B is skew-symmetric. A 3×3 skew-symmetric matrix has rank at most two, so its three rows have a nonzero constant dependence. The first three rows of N, now equal to (0,0,0,ℓ_i), have that same dependence. This contradicts the choice of independent rows and completes the proof.

The root obstruction is therefore not a subtle diagonal contact: it is the incompatibility of a three-variable linear left syzygy with the symmetric U×U blocks, combined with the odd-dimensional skew matrix in the transverse column.

## 5. Consequence and exact frontier

Together with the prior exclusions of coincident/distinct planar images and point/curve factor images, this removes every compatible full-support dimension-five surface whose ordered factor images include a plane. Any still-unclassified surface with both factor projections two-dimensional must have BOTH images nonplanar surfaces in P(E).

This does not classify the both-nonplanar case, prove it empty, settle moving-middle components with only curve fibers, or complete the global theorem. A useful next bounded step is to analyze two nonplanar factor images using the five-dimensional span and the symmetry of their bilinear annihilators, without assuming either admits a planar parametrization compatible with the first factor.

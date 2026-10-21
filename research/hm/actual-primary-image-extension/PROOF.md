# The actual primary–image extension without generation or Hilbert subtraction

## Result

Let F be the normalized Horrocks–Mumford bundle on complex P⁴, E=F(3), B=End₀(F), U=H⁰(E), and D=det U. Let C be the disjoint union of its transverse evaluation-degeneracy lines, with evaluation cokernel i_*ell and ell|l≅O_l(−1). Put

A_j=H¹F(j),  K_j=H¹B(j−1),
M_d=H¹I_C(d),  P_j=M_{6−j}*,  P_D=D⊗P.

The dual Eagon–Northcott map defines a graded S-module map θ:K→P_D. If N_im is its actual image, then

0→U⊗A(−3) --cup→ K --θ→ N_im→0                  (1)

is exact. The injection is proved directly, not by subtracting Hilbert functions. Moreover

(P_D/N_im)_j=0 for j≠1,
dim(P_D/N_im)_1≤8.                               (2)

Thus the two-stage primary-cancellation construction applies to this actual geometric extension. No claim that N_im=S(P_D)_0 is needed or made. The generation and representation results of PR475/476, and the complete Rao ideal resolution, are not premises of (1)–(2).

## 1. Explicit inputs

The geometric inputs are transverse rank-one evaluation with local form

e₀↦a, e₁↦x b, e₂↦y b, e₃↦z b,

where x,y,z is a regular sequence, and ell has degree −1 on each component. These give the exact Eagon–Northcott complex and the exterior-symmetric evaluation resolution below. The needed primary facts are

A_j=0 outside j=0,1,2,3,
H²F(s)=0 except s=−2, where dim H²F(−2)=2.

They are published primary cohomology facts; they do not depend on an adjoint-module Hilbert table or on PR475/476. Both follow directly from the original Horrocks–Mumford cohomology table (printed p.74), after the normalization F=E(−3); the Decker statements cited below provide another source. For (1), no dimensions of the four nonzero A_j are needed. The number 8 in (2) uses dim U=4.

## 2. The all-degree EN map and its dual

The evaluation Eagon–Northcott complex, twisted to I_C(d), is

0→D⊗B(d−10)→Λ³U⊗F(d−7)→Λ²U⊗O(d−5)→I_C(d)→0. (3)

Its exactness follows from the transverse codimension-three degeneracy. In the displayed local normal form, canceling unit maps reduces it to the Koszul resolution of (x,y,z). This is a local algebra assertion, not a selected evaluation calculation.

Let Z_d be the image in Λ²U⊗O(d−5). Since H¹ and H² of line bundles on P⁴ vanish, the right short exact sequence gives M_d≅H²Z_d naturally for all integers d. The left sequence gives the exact segment

Λ³U⊗H²F(d−7)→M_d→D⊗H³B(d−10)
  →Λ³U⊗H³F(d−7).

Serre duality, B*=B and F*=F(1), followed by tensoring with D, gives

U⊗H¹F(3−d)→H¹B(5−d)→D⊗M_d*→U⊗H²F(3−d)
  →H²B(5−d).                                    (4)

Here D⊗(Λ³U)*≅U. If the ambient determinant is retained in the convention for ω_P⁴, use one compatible constant-line identification throughout. It does not change any kernel or image; independent choices on the component lines are not made.

Set j=6−d. Then (4) becomes

U⊗A_{j−3}→K_j --θ_j→(P_D)_j
  →U⊗H²F(j−3)→H²B(j−1).                         (5)

Every map comes from fixed sheaf maps and connecting morphisms. These commute with multiplication by homogeneous polynomials; the transpose of multiplication under Serre duality is multiplication by the same polynomial. The reversed grading P_j=M_{6−j}* is exactly the grading that makes θ S-linear. Thus (5) is not a collection of independently chosen maps between vector spaces.

## 3. The first dual EN map is the cup map

This identification is required for the injection argument and cannot be replaced by matching dimensions.

After factoring out the common det(E)⁻¹ line from the left EN differential (equivalently, twisting the ideal complex by det E), it is

D⊗Sym²(E*)→Λ³U⊗E*.

Locally, for a frame e₀,...,e₃ of U, it is the alternating sum over i of the omitted-e_i wedge tensor contraction of the symmetric dual tensor by ev(e_i). Under D⊗(Λ³U)*≅U, its dual sends

u⊗e ↦ ev(u)·e ∈Sym²E.

Contraction on the symmetric dual is dual to symmetric multiplication. Depending on whether symmetric tensors are normalized as divided powers or as averaged ordinary tensors, there can be one common nonzero scalar; in characteristic zero it is invertible and can be fixed once. There is no component-dependent or degree-dependent factor. Thus after the rank-two determinant identifications Sym²E=B(5), its cohomological map in (5) is precisely the natural cup map U⊗H¹F(j−3)→H¹B(j−1), with the same normalization for every twist.

## 4. Direct injection, with no Hilbert comparison

The transverse local form gives the exact exterior-symmetric resolution

0→D⊗O(−5)→Λ²U⊗O→U⊗E→Sym²E→i_*ell²→0.          (6)

Its first map is the complementary-minor bivector. Locally the remaining syzygies are the Koszul syzygies of (x,y,z); the leftmost kernel is free on z e₁∧e₂−y e₁∧e₃+x e₂∧e₃. Thus (6) is an actual locally free resolution, including on C.

Let R₁=im(Λ²U⊗O→U⊗E), R₀=im(U⊗E→Sym²E). Twisting the first short exact sequence by any t and using intermediate line-bundle vanishing gives

H¹R₁(t)=H²R₁(t)=0.

Consequently the next short exact sequence identifies

U⊗H¹E(t)≅H¹R₀(t)

via the multiplication map. The final sequence gives an injection H¹R₀(t)→H¹Sym²E(t) whenever H⁰ell²(t)=0. On every component ell²(t)=O_l(t−2), so this vanishes for t≤1.

For the four possibly nonzero primary degrees j=3,4,5,6, take t=j−6, which is at most zero. Then E(t)=F(j−3) and Sym²E(t)=B(j−1), so the cup map in (5) is injective. In all other degrees its source U⊗A_{j−3} is zero by the primary support statement. This proves injection in every degree and hence the actual extension (1).

Only intermediate line-bundle cohomology and H⁰ell²(t)=0 were used in this injection step. It does not use higher B vanishing, regularity, a dimension for H¹B, any Rao Betti table, or generation of K.

## 5. Exact location of the remaining image correction

From (5), the cokernel of θ_j injects into U⊗H²F(j−3). The primary support statement forces it to vanish unless j=1. More precisely,

(P_D/N_im)_1
  ≅ker[U⊗H²F(−2)→H²B(0)].                       (7)

Its dimension is therefore at most 4·2=8. This does not assert that the displayed map is onto, that the quotient has dimension six, or that it is a particular normalizer representation. Those sharper claims require extra inputs not used here. Because the quotient is concentrated in degree one, it is annihilated by the positive-degree ideal S_+.

In particular, θ identifies N_im,j with (P_D)_j for every j≠1. It identifies K₀ with (P_D)_0 because the primary source in degree zero is zero. S-linearity then gives S(P_D)_0⊂N_im. Equality is not a consequence of that inclusion and is not claimed: it is a generation question left to the additional PR475/476 arguments.

## 6. Concrete residue pieces and lower-degree cautions

The restriction sequence gives, for every d,

M_d=coker[S_d→H⁰O_C(d)],

where S_d=0 for d<0. Hence for j≠1,

N_im,j≅D⊗coker[S_{6−j}→H⁰O_C(6−j)]*.             (8)

All these identifications use actual multiplication inherited from the geometric sequence. In particular the degrees used directly as sources or targets of the degree-six fixed-pair quotients are

N_im,₂ =D⊗M₄*,  N_im,₃ =D⊗M₃*,
N_im,₄ =D⊗M₂*,  N_im,₆ =D⊗M₀*.

No restriction injectivity is needed for these formulas; they use cokernels, not dimension differences.

For a cubic v and quadratic u, the staged calculation has genuine lower-degree denominators:

(N_im/vN_im)₄=(D⊗M₂*)/(vN_im,₁),
(N_im/vN_im)₂=(D⊗M₄*)/(vN_im,−1).

The degree-one image N_im,₁ must not be replaced by all D⊗M₅*: its discrepancy is exactly (7). At degree −1, (8) says N_im,−1=D⊗M₇*. Replacing it by zero requires the additional Rao-tail vanishing M₇=0, which is not a premise of this theorem. Similarly the degree-six residual quotient uses the actual products from degrees four and three for (u,v), or degrees two and three for (u²,v).

Thus the first-stage v-boundary is built from ker[v:D⊗M₃*→D⊗M₀*], and the second-stage u or u² boundary uses the two precisely stated v-quotients above. This is an actual geometric application of the two-stage theorem, not a purely abstract extension assumption. It still does not evaluate the relevant kernels or lift images.

### An alternative geometric proof of the positive adjoint tail

If j≥7 then 6−j<0. The disjoint-line description gives H⁰O_C(6−j)=0, so M_{6−j}=0 and (P_D)_j=0. Also A_{j−3}=0 because j−3≥4. Exactness of (5) at K_j therefore forces K_j=0. Equivalently,

H¹B(t)=0 for all t≥6.                              (9)

This recovers the previously established twist-six endpoint and higher tail by a shorter geometric argument. It is an alternative proof, not a claim that the vanishing statement is new. No adjoint section free resolution, regularity bound, or symmetric-monad rank/transgression computation is needed for this deduction.

## 7. Sources, removed dependencies, and limits

The EN/duality construction is present in PR477. The direct cup injection and use of N_im rather than a generated Rao submodule remove its need for the all-degree Hilbert-difference argument and PR475/476 generation in establishing an actual extension.

Retained inputs: transverse HM evaluation geometry, the local EN and exterior-symmetric resolutions, rank-two determinant identities, and the primary support statements for H¹F and H²F. Removed inputs: adjoint Hilbert tables, complete line-ideal resolution, Rao socle representation, the graph-scalar argument, and five-generator generation. This does not establish the removed claims or contradict them.

- PR477 construction at ff87076794e97238150485b12183c3cd0f4711e4:
  https://github.com/Akilleez-QA/read-em-and-weep/blob/ff87076794e97238150485b12183c3cd0f4711e4/research/hm/adjoint-primary-extension/PROOF.md
- PR457 exterior-symmetric resolution at 961694c4f3c805f0d58508811a42da4030dce7a6:
  https://github.com/Akilleez-QA/read-em-and-weep/blob/961694c4f3c805f0d58508811a42da4030dce7a6/research/hm/fixed-cubic-interpolation/PROOF.md
- Horrocks–Mumford, Topology 12 (1973), proof of Theorem 5.1, printed p.75, transverse evaluation geometry:
  https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf
- Decker, Compositio Mathematica 76 (1990), printed p.13 for H²F support and p.16, Remark 2(ii), for the H¹F resolution:
  https://www.numdam.org/article/CM_1990__76_1-2_7_0.pdf

No selected fixed-pair value, primary coverage, source membership, higher-order lifting, or algebraicity follows. This is authored mathematical reasoning for independent checking, not formal verification.

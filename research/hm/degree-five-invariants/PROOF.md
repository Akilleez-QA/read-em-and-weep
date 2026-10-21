# The degree-five primary defect is entirely Heisenberg invariant

Status: independently mathematically reviewed (PASS); see REVIEW.md. Not formally checked. Work over C. No selected actual HM/source coefficient, evaluation matrix, numerical rank test, or large computation is used.

## 1. Pinned actual geometry and statement

Let S be the actual primary evaluation surface in P(A), nu:X->S its normalization, H=nu^*O_S(1), and T=nu_*O_X/O_S. Write H5 for the order-125 Heisenberg group, Z for its scalar center, G=H5/Z=F5^2, and N for its linear normalizer in SL(A). These names distinguish the group H5 from the polarization H.

Inputs:

- The actual N-equivariant exterior model is pinned at commit 7bf725bcd857a2deb975f9ecb80fca32e7833ae0, research/hm/order-four-quadratic-load/PRIMARY-INJECTION-AND-FAILURE.md, Section 1. In particular Lambda^2 A=V tensor W and the primary evaluation is the exterior map followed by the sl(W) action. This supplies actual equivariance, not just symmetry of a point configuration.
- PR567, commit e0f15a5c6a49d2101dae450dae4d26171a259331, research/hm/unique-line-surface/PROOF.md, proves that the unique reduced integral component containing the twenty-five distinguished lines is invariant under the full normalizer.
- PR573, commit 6c2dbd48edea0577acf063a60e1edbbbe92ced5c, research/hm/global-primary-equality/PROOF.md, identifies the entire actual degeneracy scheme with that component S and identifies its thirty transverse double points. Its normalization is the modular surface X=S(5).
- PR587, commit 865ab24e91333688d7ae76303d7d594aae8521f8, research/hm/eigenline-interpolation/PROOF.md, identifies those nodes with the thirty Heisenberg eigenlines. PR578, commit d3f1135f7c3c1104ec431fcc44fdb5e2d80bb078, research/hm/primary-postulation/PROOF.md, supplies H^1(X,nH)=0 for n>=1 and h^1(O_S(5))>=1.
- The exact-postulation proof at a1c77f791158cc0976df80220c958a50c2217ee3, research/hm/eigenline-postulation/PROOF.md, uses the separate quadratic-generation input at 7547a6a0d84d29478a0bad2d30bda271c37c269e to prove 25<=r_5<=29, equivalently 1<=h^1(O_S(5))<=5.

Here r_5 is the rank of rho_5:H^0(X,5H)->H^0(T(5)). The new conclusions are

H^1(S,O_S(5)) is a trivial G-module,
H^0(T(5))|_G = 1^6 direct-sum (direct-sum over chi!=1 of chi),
r_5 = 24 + rank(rho_5^G), with 1<=rank(rho_5^G)<=5.

Thus every nontrivial Heisenberg quotient character is already hit. The remaining defect is exactly the cokernel of the six-dimensional invariant-target map. No exact invariant rank, and no decomposition of that six-dimensional space as an SL2(F5)-module, is claimed.

## 2. Actual linearization, including normalization and branch quotient

The linear normalizer N acts on A, hence naturally linearizes O_P(A)(1). Since the actual S is N-invariant as a closed subscheme by the preceding pins, restriction linearizes O_S(1). This is stronger than knowing that the node set is invariant.

Each automorphism of the integral surface S lifts uniquely to its normalization: on affine patches the lift is induced on the integral closure in the function field. Uniqueness makes these lifts satisfy the group law. Pulling back the restricted ambient linearization gives an N-linearization of H. The canonical algebra inclusion O_S->nu_*O_X is equivariant, so its quotient T and every twisted normalization sequence are equivariant. Cohomology and its connecting maps consequently carry genuine N-representations.

The scalar center Z fixes P(A), S and X pointwise, and acts on O(1) by a primitive fifth-root scalar or its inverse, according to convention. Its action on the structure sheaves and T is trivial. Therefore it acts trivially on all three sheaves in the degree-five twisted sequence and on all their cohomology. In particular H^1(O_S(5)) is an N/Z-representation whose restriction to H5 factors through G. No independently chosen Weil linearization on X is needed; the ambient pullback fixes the linearization used throughout.

The long exact sequence, with H^1(X,5H)=0, identifies the actual defect equivariantly:

coker(rho_5) = H^1(S,O_S(5)).                       (1)

## 3. The small-dimension orbit lemma

The standard Heisenberg normalizer has N/H5=SL2(F5), acting naturally on G. Horrocks-Mumford (1973), Section 1, printed pp.65-66, proves this normalizer statement and explicitly records transitivity on the twenty-four nontrivial G-characters. Source: https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf . The relevant quotient and conjugation statements are invariant under the primitive Galois or dual convention used for A.

Here is the elementary representation argument. For any finite-dimensional N-representation M with trivial Z-action, finite abelian semisimplicity gives M=direct-sum M_chi over characters of G. Conjugation by N maps each M_chi isomorphically to M_(n.chi). The nontrivial characters form one orbit of size 24: identify the dual of G with F5^2, and extend each prescribed nonzero vector to a determinant-one basis to see SL2(F5)-transitivity. Thus their dimensions are one common nonnegative integer m, and

dim M = dim M_1 + 24m.

If dim M<24, then m=0, so G acts trivially on M. Applying this to (1), whose dimension is between one and five, proves that the entire degree-five defect is G-invariant. This does not assert that the remaining SL2(F5) action on the defect is trivial.

## 4. Exact G-character content of the branch-difference target

There are six cyclic directions L in G. The five eigenlines for each direction form a single G-orbit with stabilizer L: conjugation by a complementary Heisenberg generator cycles the five distinct eigencharacters. Independent directions have disjoint eigenline sets, because lifts of independent elements have a nontrivial scalar commutator and cannot share an eigenline. Hence these six orbits partition the thirty nodes.

At a node p the normalization has two distinct preimages, and T_p is the one-dimensional quotient C^2/C_diag. The order-five stabilizer L cannot swap those branches: its permutation homomorphism to S2 is trivial. Thus it acts trivially on the untwisted difference fiber. More explicitly, the preimage of L in H5 also has odd order, so this statement can be made before passing to G.

For the twist, choose an order-five Heisenberg lift g of a generator of L. Its eigenvalue on the eigenline p is a fifth root of unity. Its action on the O(5) fiber is therefore one, regardless of the dual convention. The center also acts trivially in degree five, so this computes the genuine L-action on T(5)_p. It is trivial. Transitivity now identifies the five-dimensional section space over this orbit with Ind_L^G 1, not a character-twisted induced module.

For abelian G, Ind_L^G 1 is the direct sum of the five characters trivial on L, each once. The trivial character occurs for every one of the six directions. A nontrivial character has a unique order-five kernel, so occurs for exactly one direction. Adding the six orbit modules proves

H^0(T(5))|_G = 1^6 direct-sum (direct-sum_(chi!=1) chi).       (2)

Branch signs are controlled here only for the odd-order Heisenberg stabilizers. Elements of the larger normalizer stabilizer may swap branches or have nontrivial O(5)-fiber scalars. Thus (2) does not identify the N/H5-representation on the six invariant lines with the unsigned permutation representation on six directions.

## 5. Exact reduction to six invariant residues

Since the cokernel of rho_5 has no nontrivial G-character by Section 3, (2) implies that every one of its twenty-four nontrivial one-dimensional target character spaces is in im(rho_5). Character projections preserve the image by equivariance. Invariants are exact over C, by averaging over G, so

H^1(O_S(5)) = coker[H^0(X,5H)^G -> H^0(T(5))^G],
dim H^0(T(5))^G = 6.

Each invariant target line is the constant residue line on one five-point node orbit after an equivariant trivialization. Arbitrary branch orientations need not make these residues literally equal without corresponding scalar/sign changes. The invariant subspaces themselves are intrinsic.

Putting a=rank(rho_5^G), we obtain

r_5=24+a, h^1(O_S(5))=6-a, 1<=a<=5.

The first bound uses r_5>=25, and the second uses the independently established nonzero defect. In particular the problem is not a thirty-coordinate interpolation problem anymore: only the actual invariant normalization sections and their six orbit residues remain unresolved.

## 6. A canonical seven-dimensional invariant source

The quadratic-generation theorem at 7547a6a0d84d29478a0bad2d30bda271c37c269e, Section 4, equation (9), gives the actual equality of image spaces

im(rho_5)=H^0(P(A),O(3)) · Q_2, where Q_2=im(rho_2), dim Q_2=5.

Let P_3=H^0(P(A),O(3)). Multiplication and restriction define an intrinsic N-equivariant map

mu:P_3 tensor Q_2 -> H^0(T(5)),

whose image is exactly im(rho_5). This uses the actual quadratic-generation theorem, not an inference from a sheaf surjection.

Write epsilon for the primitive central character on O(1). The module Q_2 has central character epsilon^2 and dimension five, so it is the unique irreducible Heisenberg representation of that character. The module P_3 has dimension 35 and central character epsilon^3, so it is a sum of seven copies of Q_2^*. These are restriction statements for H5, not decompositions as N-modules. The usual Heisenberg character description gives

Q_2^* tensor Q_2 = C[G]

as G-modules: its trace is 25 at the identity and zero at every nonidentity element of G, since the trace of a noncentral element on Q_2 is zero. Therefore

(P_3 tensor Q_2)|_G = C[G]^7,
dim (P_3 tensor Q_2)^G=7.

Exactness of invariants identifies the image of mu^G with im(rho_5)^G. The remaining map is consequently the concrete, intrinsic map

mu^G:(P_3 tensor Q_2)^G -> H^0(T(5))^G,
                  dimension 7 -> dimension 6.

It has rank a, cokernel H^1(O_S(5)), and kernel dimension 7-a=1+h^1(O_S(5)), between two and six. This is a finite representation-level reduction to the actual multiplication map, not a matrix construction or a claim of generic rank. It avoids silently identifying the full nonambient normalization quotient with its conductor image.

## 7. Scope and next dependency

The separate residual K4/primitive-twist-four problem remains outside this proof. This result does not resolve its connecting maps, the full adjoint rank-twenty boundary, prescribed-source membership, higher lifting, or algebraicity.

The new step is an actual-equivariance theorem and character-level surjectivity for the primary conductor. Its next missing dependency is the rank of the invariant difference map. An identification of the six-dimensional normalizer module with 1+5 would require an additional stabilizer-character/branch-swap calculation, which is deliberately not presumed here.

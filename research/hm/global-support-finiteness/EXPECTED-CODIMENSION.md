# The primary-bad quadratic scheme: exact codimension six and degree 210

## Scope and dependency

This note continues PROOF.md in this directory (SHA256 f27a7faec3fe4ea0e10d80b4f480554926882d791c050c11afc09bb17ee41b96). That proof establishes the set-theoretic dimension bound at most eight for the primary-bad quadratic locus in P(S2)=P14, using its exact thirty-point support-drop classification. The exterior-model and generic-primary-rank dependencies are pinned there.

Here B denotes the determinantal scheme of primary-bad quadratics on P14, not the support-drop scheme on P4. This note proves that B is arithmetically Cohen-Macaulay, of pure codimension six and degree 210. It makes no assertion of reducedness, irreducibility, or equality with any full-adjoint or higher-order failure locus.

## 1. The homogeneous determinantal ideal has height six

The bilinear primary multiplication defines the bundle map

mu: A tensor O_P14(-1) -> M2 tensor O_P14,

of ranks five and ten. Let R=C[q_0,...,q_14]. In any bases, mu is a 10 by 5 matrix M of homogeneous linear forms. Its maximal-minor ideal I=I_5(M) defines B=Proj(R/I).

The locus is nonempty without selecting or evaluating any actual quadratic. For every nonzero x in A, the linear evaluation S2->M2 has a kernel of dimension at least five, since the dimensions are fifteen and ten. Any nonzero q in that kernel satisfies mu_q(x)=0. Thus B is nonempty.

Because I is homogeneous and B is nonempty, the affine cone defined by I has dimension dim(B)+1. The preceding proof gives dim(B)<=8, so dim(R/I)<=9 and height(I)>=6. The general maximal-minor height bound gives

height(I_5(M)) <= (10-5+1)=6.

Consequently height(I)=6, dim(R/I)=9, and dim(B)=8. In particular the primary-bad scheme has exactly its expected codimension (10-4)(5-4)=6.

## 2. Eagon-Northcott, Cohen-Macaulayness, and saturation

The polynomial ring R is regular and Cohen-Macaulay. Therefore grade(I)=height(I)=6. This is precisely the expected maximal-minor grade required for the Eagon-Northcott complex of M to resolve R/I, with resolution length six. Hence R/I is Cohen-Macaulay of dimension nine.

The projective assertion requires no unspoken saturation assumption. At the homogeneous maximal ideal m=(q_0,...,q_14), the Cohen-Macaulay ring R/I has depth nine, in particular positive depth. Thus its m-torsion H^0_m(R/I) vanishes. Since

I^sat/I = H^0_m(R/I),

the maximal-minor ideal I is already saturated. Thus B is arithmetically Cohen-Macaulay for its given determinantal scheme structure. Perfection over the regular polynomial ring also gives unmixedness in height six, so B is pure of codimension six. This does not imply radicality.

## 3. Fundamental cycle and degree

Apply the Thom-Porteous formula to mu with e=5, f=10, k=4. The ambient P14 is smooth and B has the expected codimension six. The determinant in the formula has size e-k=1, so the pushed-forward fundamental cycle of the natural determinantal scheme is

[B] = c_6(10O - 5O(-1)) cap [P14].

Writing h=c_1(O(1)), its total Chern class is (1-h)^(-5). The coefficient of h^6 is

binomial(5+6-1,6) = binomial(10,6) = 210.

Therefore [B]=210 h^6 in A^6(P14), and deg(B)=210, with the scheme multiplicities included. In particular this is not a claim that B has 210 points or 210 components.

## Public references for the standard determinantal theorems

- D. Eisenbud, C. Huneke, B. Ulrich, Heights of Ideals of Minors: https://arxiv.org/abs/math/0209184 . The classical determinantal height bounds are the height input above.
- Eagon-Northcott exactness in expected grade, as discussed in Virtual criterion for generalized Eagon-Northcott complexes, Journal of Pure and Applied Algebra: https://www.sciencedirect.com/science/article/pii/S0022404922001347 . The required hypothesis here is grade(I_5(M))=10-5+1, already established, not genericity of the chosen entries.
- W. Fulton, Intersection Theory, Section 14.4 (Thom-Porteous formula), publisher record: https://link.springer.com/book/10.1007/978-3-662-02421-8 . The rank data and expected-codimension hypothesis are verified explicitly above.

## Verification and restrictions

The derivation has been independently checked mathematically, including the affine-cone dimension, grade, and saturation steps. Exact-file review is separate. No proof-assistant verification is claimed. No selected actual HM/source coefficients, matrices, ranks, or large computations were evaluated, and the note does not decide any prescribed selected quadratic, higher-order lifting, or algebraicity claim.

# Universal square quotient of the cubic-tautological quartic subbundle

Let W be a complex two-space with fixed determinant form, T=P(W), and D=Sym^4 W. The tautological inclusion Y=W tensor O(-3) -> D tensor O sends l^3 tensor u to l^3 u. Its symmetric square is an everywhere injective subbundle map

    A tensor O(-6) -> Sym^2 D tensor O,  A=Sym^2 W.

Let S12 be its quotient. Then, equivariantly for SL(W),

    S12 = O direct-sum Sym^3 W tensor O(1)
            direct-sum Sym^6 W tensor O(2).

In particular restriction to the binary icosahedral group gives

    S12 = O direct-sum S tensor O(1)
            direct-sum (V+P) tensor O(2).

All constructions here are universal binary-form identities. There is no actual HM coefficient, selected geometric parameter, or instance evaluation.

## 1. The three coefficient projections

The SL2 decomposition is Sym^2(Sym^4 W)=Sym^8 W plus Sym^4 W plus 1. The projections are, up to nonzero scalars, ordinary multiplication and transvectants of orders two and four.

For f=l^3 u and g=l^3 v, multiplication gives l^6 uv, so the Sym8 projection is nonzero. The second transvectant is a nonzero scalar times l^4 det(l,u) det(l,v). For example, in formal binary variables X,Y, write l=X, u=aX+bY, v=cX+dY to compute the identity: f_XX g_YY - 2 f_XY g_XY + f_YY g_XX = -18bd X^4. This is a universal covariance calculation, not an evaluated actual direction. The fourth transvectant is zero: each input has Y-degree at most one, whereas every term differentiates a total of four times with respect to Y. Equivariance proves these assertions for arbitrary l.

Dualizing the subbundle sequence and taking global sections consequently gives a map

    Sym8 W plus Sym4 W plus 1 -> Sym6 W tensor Sym2 W.

Its Sym8 and Sym4 restrictions are nonzero, and its trivial restriction is zero. Since Sym6 tensor Sym2 = Sym8 plus Sym6 plus Sym4, its kernel is exactly 1. Thus h0(S12*)=1.

## 2. No missing degree-one channel

After twisting the dual sequence by one, the relevant section map is

    (Sym8 plus Sym4 plus 1) tensor W -> Sym7 tensor Sym2.

It is multiplication in the base-polynomial factor on the preceding coefficient map. The target is Sym9 plus Sym7 plus Sym5. The source is Sym9 plus Sym7 plus Sym5 plus Sym3 plus Sym1. It suffices to prove all three possible channels nonzero; multiplicity alone would not prove this.

Use two formal binary variable pairs (x,y) and (u,v) for Sym6 and Sym2. The nonzero Sym8 inclusion has highest vector x^6 u^2, up to scalar. Its lowering operator gives 6x^5 y u^2+2x^6uv. In Sym8 tensor W, the highest vectors of the Sym9 and Sym7 components may be taken as

    (x^6u^2) tensor x,
    (x^6u^2) tensor y - (1/8)(6x^5yu^2+2x^6uv) tensor x.

Under multiplication into Sym7 tensor Sym2 these become respectively

    x^7u^2,
    (1/4)(x^6yu^2-x^7uv),

both nonzero. The nonzero Sym4 inclusion in Sym6 tensor Sym2 has highest vector x^4(xv-yu)^2, up to scalar. Its product by x is the nonzero highest vector x^5(xv-yu)^2 of Sym5. Therefore the degree-one map is onto, with kernel Sym3 plus Sym1. Hence h0(S12*(1))=6.

## 3. Splitting and equivariant coefficients

S12 is globally generated, rank12 and degree18. Write its ordinary splitting degrees d_i>=0. The equality h0(S12*)=1 gives exactly one zero degree. The equality h0(S12*(1))=6 gives exactly four degree-one terms, since the zero term contributes two. The seven remaining degrees are at least two; their total is18-4=14, so all seven are exactly two.

The split degree-zero quotient has coefficient representation1, from H0(S12*)*. The degree-one coefficient representation is Sym3: H0(S12*(1))=Sym1 plus Sym3, and the degree-zero contribution is exactly Sym1. Finally the degree-two coefficient is H0(S12(-2)). The original sequence twisted by -2 identifies this with the kernel

    A tensor H1(O(-8)) -> Sym^2 D tensor H1(O(-2)).

By natural Serre duality this is dual to the degree-zero section map in Section1. Its cokernel is Sym6, so H0(S12(-2))=Sym6.

The ordinary splitting can be chosen SL2-equivariantly: the successive Harder-Narasimhan extensions have zero ordinary Ext1, since higher-degree pieces occur as subbundles; the affine spaces of splittings admit invariant choices by reductivity.

## 4. Uniqueness of the equivariant splitting

After restriction to the binary icosahedral group, the splitting into the three degree pieces is unique as an equivariant subbundle splitting of the Harder-Narasimhan filtration. Indeed its possible upward ambiguity spaces are

    Hom_G(1, Sym3 W tensor W),
    Hom_G(1, Sym6 W tensor Sym2 W),
    Hom_G(Sym3 W, Sym6 W tensor W).

They all vanish. The first target is A+D. The second is Sym8+Sym6+Sym4, which restricts to V+2P+2D. The third target is Sym7+Sym5=Wp+2T, with no S=Sym3. Downward homomorphisms vanish already by ordinary line-bundle degrees. This proves uniqueness of equivariant complements; it does not choose scalar-normalized isomorphisms of their coefficient representations with named abstract representations. In particular the V and P factors in the degree-two coefficient retain their independent scalar automorphisms.

## 5. Immutable actual inputs and ninth-neighborhood image

All repository paths below are in Akilleez-QA/read-em-and-weep. INPUTS.json records the exact originals with raw-byte SHA256 and Git-blob identities, with copies in audit-inputs/.

- SQUARE: commit db51525015bb7c5e825833d550d08dedf6f6ea96, research/hm/order-four-quadratic-load/HYPERPLANE-SQUARE-SURVIVORS.md, Sections 5–6: the actual binary cubic-tautological section subbundle and its square inclusion.
- RANK: PR986, commit 2f3eb11a6f55582e17f56c8bc9b310db9a37424d, research/hm/ninth-neighborhood-rank/PROOF.md, Sections 3–4: constant rank twelve and the actual image as the annihilator of the same square inclusion.

The actual square-survivor theorem identifies Y=W O(-3) inside D O with precisely the cubic-tautological inclusion l^3 W, and the plane product map identifies H0(B_R(3)) with Sym2 D. Thus the universal quotient above is the actual quotient by its square subbundle, not merely another quotient of the same dimensions. Changes of scalar identifications do not change its image subbundle.

The separately established ninth-neighborhood rank theorem identifies the ACTUAL image of Theta with S12* O(8), the annihilator of that same square inclusion in H0(B_R(3))* O(8). Applying the universal splitting yields

    im Theta = O(8) direct-sum S O(7)
                  direct-sum (V+P) O(6).

Its rank is 1+4+7=12 and degree is 8+28+42=78, agreeing with the independent rank theorem. The canonical equivariant degree-piece subbundles transfer through the actual annihilator identification. This does not select a preferred basis, any actual scalar of Theta, or a splitting of the original K or of the source-to-image exact sequence for Theta.

This application uses the exact published RANK input, including its naturality identification of the quotient map with the transpose of actual square restriction. The universal Sections 1–4 do not require that geometric input.

Neither the kernel splitting of Theta, the opposite bundle C, the top polar sigma, the vertex delta, nor the four-pair source frontier is determined here. The new result is the complete equivariant square-quotient and image-bundle splitting, not a selected actual coefficient, point, parameter, matrix, derivative, or instance-rank calculation.

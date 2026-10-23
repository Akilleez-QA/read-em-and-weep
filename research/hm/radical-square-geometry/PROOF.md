# The everywhere-injective radical-square channels

Work over C with G=SL2(F5), the fixed negative doublet W, the other doublet W', and the conventions of PR1127. Put D=Sym4 W and T=Sym5 W, and fix the canonical decomposition Sym6 W=V+P. All conclusions below are conditional on type I or II of the necessary bundle catalogue. No type is selected or excluded.

## 1. Authenticated inputs and scope

INPUTS.json retains the full public PR1127 proof at 60dda5a940d5ba7ee081a86cd1b1a783a5952a39 and the universal representation model and proof of PR1031 at 7150cf97eeebe473bcd7c61c1f968c73625d92ef. Both SHA256 and Git blob hashes are checked. The public versions were fetched and matched before calculation.

Only PR1031's fixed projection Pi:Sym6 W→P and canonical kernel V are used. Its actual-source hypotheses, quadratic lift results and instance data are not used. PR1127 identifies the one-dimensional square of the Jacobson radical of End_G(E), in types I and II respectively, with the nonzero channels

    fI: V O(-4) → D O(-2),   v ↦ (p∂x+q∂y)^2 v,
    fII: V O(-4) → P O(-2), v ↦ Pi((xq-yp)(p∂x+q∂y)v).

PR1127 proves nonvanishing as polynomial maps, not fiberwise rank. The new result is the everywhere rank, saturation, and precise cokernel of these channels.

## 2. Exact whole-coefficient rank certificates

In monomial order x^6,x^5y,...,y^6 use PR1031's Pi. An explicit basis of ker Pi is

    V = [ -1/15       0       -2sqrt5/5 ]
        [ 0           1        0        ]
        [ 2sqrt5/5    0       -3        ]
        [ 0          -2sqrt5/3 0        ]
        [ 1           0        0        ]
        [ 0           1        0        ]
        [ 0           0        1        ].

The verifier checks Pi V=0 and ranks 4 and 3 respectively. It constructs the entire 5×3 and 4×3 matrices fI and fII as binary quadratics in independent formal p,q. RESULT.json retains every entry and every maximal minor.

For fI, the ten maximal minors are sextics whose coefficient vectors span the full seven-dimensional space Sym6. Hence their common homogeneous zero set contains no projective point: their span contains p^6 and q^6.

For fII, the four maximal minors have coefficient rank four, and their homogeneous gcd in Q(sqrt5)[p,q] is a unit. Since these are binary forms, this proves no common projective zero even after extension to C. More explicitly, their ideals on BOTH symbolic charts p=1 and q=1 have Groebner basis {1}. The checker independently performs these chart ideal checks for both maps. These chart normalizations retain the other variable as an indeterminate and are not selected-direction evaluations.

Thus both maps have rank three at EVERY point of P1. They are subbundle injections, not merely injections of sheaves with possible rank-drop torsion. No group-orbit bound or assumption that a nonzero map has full rank is needed.

## 3. Cokernels, including the type-I balancing argument

For type II the cokernel has rank one and degree

    degree(P O(-2)) - degree(V O(-4)) = -8 - (-12) = 4.

Thus there is an exact equivariant sequence

    0 → V O(-4) → P O(-2) → O(4) → 0.

There is no character ambiguity: SL2(F5) has trivial abelianization, so a line-bundle linearization differs from the standard one by only the trivial character. Equivalently the determinant representations of V and P are trivial.

For type I let C be the cokernel. Its rank is two and degree is two. Untwisting by O(-2) gives

    0 → 3O(-2) → 5O → C(2) → 0,

and dualizing gives

    0 → C*(−2) → 5O → 3O(2) → 0.

The transpose matrix's polynomial syzygies of degrees 0,1,2,3 have dimensions exactly 0,0,0,2. These are computed by expanding ALL coefficients of its product with a general homogeneous polynomial vector. At degree two this is the full 15×15 coefficient map, and its kernel is zero, so H0(C*)=0. If C=O(a)+O(b), with a+b=2, that vanishing forces a,b≥1. Hence a=b=1. This establishes balancing by exact coefficients, not by a character count.

The equivariant structure is C=R O(1) for a two-dimensional representation R. The original sequence gives

    H0(C) = ker(V⊗Sym2 W → D).

Since C=2O(1), H1(C)=0. The map onto D is therefore surjective. PR1127's tensor identity V⊗Sym2 W=P+D yields H0(C)=P. Hence R⊗W=P, and the two-dimensional coefficient representation is W': the other possibilities are W, giving 1+Sym2 W, or two trivial representations, giving 2W. Thus

    0 → V O(-4) → D O(-2) → W' O(1) → 0.

The exact maps are the displayed universal channels up to nonzero scalar. Their images and cokernels do not depend on that scalar.

## 4. The intrinsic radical-square subsheaf

Let A=End_G(E), N=rad A, and define intrinsically

    S = image(N² ⊗ O ⊗ E → E).

For either necessary type I or II, PR1127 proves dim N²=1. Choose any nonzero generator n. Then S=im n, independently of that choice. Using any equivariant splitting into the catalogue summands identifies n, up to nonzero scalar, with fI or fII from the V O(-4) block to the top degree-minus-two block, zero on all other blocks.

The everywhere rank result proves S is saturated in E, has rank3 and degree−12, and is abstractly equivariantly isomorphic to V O(-4). The image subsheaf S is canonical. An identification with a selected model V O(-4), or a complementary summand inside E, is not canonical. Because N² is a two-sided ideal, S is preserved by every equivariant endomorphism of E. PR1127's canonical retraction p:E→W'O(-3) vanishes on S, so S lies in the canonical K=ker p.

In a chosen catalogue identification, the quotient types are

    I: E/S ≅ W'O(1) + (W'+T)O(-3) + V O(-4) + O(-8),
    II: E/S ≅ O(4) + (W'+T)O(-3) + V O(-4) + W'O(-5).

The source V O(-4) summand remains: S is the image inside the top D/P summand, not that source summand. Both have rank14 and degree−42. Correspondingly

    I: K/S ≅ W'O(1) + T O(-3) + V O(-4) + O(-8),
    II: K/S ≅ O(4) + T O(-3) + V O(-4) + W'O(-5),

of rank12 and degree−36. These are abstract quotient isomorphism types, not claims of canonical splittings. The positive-degree quotient is consistent with E having negative-degree summands; it does not produce a positive subbundle of E or a contradiction.

## 5. Reproduction and limits

Run python verify.py and python -O verify.py; both outputs agree with RESULT.json. The checker requires SymPy and exact Q(sqrt5) arithmetic. It authenticates retained public sources, builds full universal matrices, retains all maximal minors, verifies both symbolic projective charts, and computes complete polynomial-syzygy coefficient maps.

This proves an intrinsic filtration and quotient geometry for each of two necessary types. It does not exclude either type, choose an actual model, establish the geometric coverage bridge, extend a splitting to positive/Q/Gauss operations, or settle full-adjoint invertibility or the original proof repair. No actual HM coefficient, actual source matrix, selected point, sampled direction, jet, or consumed experiment is used.

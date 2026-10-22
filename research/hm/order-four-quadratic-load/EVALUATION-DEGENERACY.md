# The universal primary evaluation cannot be everywhere onto

Use A0=M_0, W=W', and the already established exterior multiplication formula

    (a tensor D)x = c (id_V tensor D)(a wedge x),
    S_2=A0 tensor sl(W), M_2=V tensor W, c nonzero.

This note gives a new obstruction to universal evaluation surjectivity, without evaluating any selected x, polynomial, coefficient, or multiplication matrix.

## 1. The intrinsic bundle map

On X=P(A0)=P4, write O(-1) for the tautological line bundle and Q for the rank-four quotient of A0 tensor O. Universal evaluation is

    epsilon:S_2 tensor O(-1) -> M_2 tensor O.

Its fiber at [x] is e_x:q -> qx, up to the harmless tautological scalar. The exterior formula shows that the subbundle

    sl(W) tensor O(-2) -> S_2 tensor O(-1)

is killed: its fibers are the tensors x tensor D. Dividing by this subbundle produces the canonical map

    alpha:E=sl(W) tensor Q(-1) -> M_2 tensor O.

Since Q=T_X(-1), E=sl(W) tensor T_X(-2), of rank12. The cokernel of alpha is exactly the universal evaluation cokernel, not an arbitrary presentation with the same dimensions.

## 2. A Chern obstruction to universal surjectivity

Suppose e_x were onto for every x. Then alpha would be a surjection of vector bundles and its kernel J would be a vector bundle of rank2. The Euler sequence gives

    0 -> O(-2) -> A0 tensor O(-1) -> T_X(-2) ->0.

Therefore, writing h=c1(O(1)),

    c(J)=c(E)=(1-h)^15/(1-2h)^3,
    c1(J)=-9h, c2(J)=39h^2, c3(J)=-105h^3.

The last coefficient follows directly from

    -455 + 630 - 360 + 80 = -105.

But c3 of a rank-two vector bundle is zero, whereas h^3 is nonzero in A^3(P4). This contradiction proves that the evaluation-degeneracy set

    Z={ [x] : rank(e_x)<10 }

is nonempty. In particular, an everywhere-surjective evaluation argument cannot sharpen the primary-bad-quadric codimension in the proposed manner.

This is stronger than observing that the no-full-fiber condition alone does not imply surjectivity: universal surjectivity is actually impossible for the HM exterior model, independently of any choice of identification exterior^2 A0=V tensor W.

## 3. Conditional cycle consequence and precise remaining premise

If alpha is generically onto, Z is a nonempty determinantal degeneracy locus. The standard height bound for maximal minors of a 10-by-12 map gives codimension at most3. If Z has its expected codimension3, its determinantal cycle has class

    c3(E^* - (M_2 tensor O)^*) = 105h^3.

Equivalently this is the appropriate Thom-Porteous determinant for rank<=9, not simply c3((M_2 tensor O)-E). Thus the expected-codimension case is a degree105 curve cycle. Neither generic surjectivity nor expected codimension is asserted here. This conditional class is not a computation of selected minors or a claim of reducedness.

The exact remaining question is now the generic rank and degeneracy strata of the explicit intrinsic bundle map alpha. The known monad no-full-fiber argument proves only rank(e_x)>=5 pointwise; the generic-primary-injectivity incidence argument does not decide whether the generic evaluation rank is10. There is no justified identification here of coker(alpha) with the HM rank-two bundle. Indeed an everywhere exact rank-two kernel would violate the Chern calculation above.

All full adjoint and selected-pair claims remain unchanged. The new result rules out one structural route, identifies its actual cokernel presentation, and supplies the nonzero conditional degeneracy class without selected evaluation or experimentation.

Dependency: the actual exterior multiplication formula is proved in PRIMARY-INJECTION-AND-FAILURE.md at commit 7bf725bcd857a2deb975f9ecb80fca32e7833ae0 of https://github.com/Akilleez-QA/read-em-and-weep/pull/543 . The Chern calculation uses only its intrinsic bundle map and the Euler sequence.

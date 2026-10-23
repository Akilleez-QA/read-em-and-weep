# Collective radical images force the Type II cubic gate to vanish

## Statement and boundary

Assume an actual source126 Type II occurrence whose entire two-dimensional radical J is compatible with the canonical invariant quadratic Q. Retain all actual-bundle and fixed-negative-pencil hypotheses of PR961, PR970, PR973, PR979 and PR982. Then the collective images, meaning sums over ALL radical elements, are exactly

    I2 := JN2 = P+2D,  dim I2=14,
    I4 := JN4 = P+D,   dim I4=9.                       (1)

Consequently the radical quotients have dimensions

    dim(N2/I2)=27 < 28=dim(N4/I4).                    (2)

No J-linear map N2→N4 can be surjective, even after extension of the scalar field. In particular every member Q+tT_a has rank at most36. Combining this with the retained original-second generic rank3 gives exact generic rank36 and vanishing of ALL original Bocksteins after the second at the generic negative direction. The actual internal cubic gate r of PR982 is also ZERO under the same full-J hypothesis.

These are conditional compatibility constraints, not an exclusion of Type II occurrence or full-J compatibility. No source or source-dual pair is removed. No actual HM coefficient, parameter, selected direction, matrix or rank is evaluated. No generic maximal-rank theorem for the original module is imported, and no full repair is claimed.

## 1. Exact actual interfaces

The genuine constant splitting and natural cohomology of PR961/970 give

    N2 = A+2V+3P+4D,  F2=A+2V+2P+2D,
    N4 = 2V+4P+3D,   F4=P+2D.

Every j∈J kills F2,F4 and maps N2 into F2 and N4 into F4. Its maps are G-equivariant. Under full-J Q compatibility, PR970 gives the actual common annihilators

    U=Ann_J N2=F2,  Z=Ann_J N4=2V+2P+2D.

The invariant map Q has kernel A+D and cokernel P. Therefore its entire P-isotypical source map is injective, and its entire D-isotypical target map is surjective. These refer to actual isotypical subspaces, not chosen irreducible copies.

PR961 §2 proves the collective D action at N4 is nonzero, using the natural isomorphism Hom_G(R,F)→Hom_G(H1(R),F0), the actual X,Y bundle subobjects, and the freely prescribable A coefficient of the constant radical map. That input is geometric, not a dimension guess. PR973 §3 proves that the actual D summand of ker Q lies inside I2. For completeness, the latter argument is repeated next.

## 2. The actual kernel D is in the collective image

Write S=[U→Z], T=[N2/U→N4/Z]. For each j the descended actual endpoint maps form a chain map T→S, because J²=0, the displayed common-annihilator identities hold, and Q commutes with J. At Q,

    H0(T)=D, H0(S)=A+D.

The induced j⁰ is G-equivariant, so its image lies in the actual D kernel summand. At least one j⁰ is nonzero. Otherwise for any quotient cycle x̄ and any lift x, one would have j2x=0 for every j: j2x is a genuine degree-zero cycle of S and there are no degree-minus-one boundaries. Hence x∈Ann_J N2=U, giving x̄=0, contrary to H0(T)=D. Nonzero j⁰ between irreducible D copies is onto. Its values are actual j2-images. Thus

    (ker Q)_D ⊂ I2.                                   (3)

No equality between a common kernel and a collective image has been assumed.

## 3. Determine the P and D collective images

Because J kills F2 and N2/F2=P+2D, while its images lie in F2, equivariance gives

    I2=uP+vD, 0≤u≤2, 0≤v≤2.

The common annihilator is exactly F2, so the residual P cannot be killed by all J: u≥1. Similarly I4⊂F4=P+2D. Its P part is nonzero by PR970's joint P-row rank2, and its D part is nonzero by the geometric input in §1. Hence

    I4=P+wD, 1≤w≤2.

P channel: Q(I2_P)⊂I4_P by compatibility. Since Q is injective on the full P source, 4u≤4. With u≥1 this forces u=1.

D channel: Q is onto the entire N4_D. For each j, equivariance and compatibility imply

    j4(N4_D)=j4 Q(N2_D)=Q j2(N2_D).

Taking sums over j yields the equality of ACTUAL subspaces

    I4_D=Q(I2_D).                                     (4)

By (3), the kernel of this restriction is exactly the full five-dimensional D kernel of Q. Therefore

    5w=5v−5, or w=v−1.

Since w≥1 and v≤2, necessarily v=2,w=1. This proves (1). In particular the tempting putative image I4=P+2D is impossible under the full-J hypotheses; a common D-annihilator of multiplicity2 does NOT imply an image of multiplicity2.

## 4. The quotient-dimension obstruction

For any field extension K/C and any J-linear map f:N2_K→N4_K,

    f(I2_K)⊂I4_K.

It induces a linear map on the radical quotients of dimensions27 and28. If f were onto, its induced quotient map would be onto, which is impossible. More quantitatively, coker f surjects onto coker(f̄), which has dimension at least1; thus rank f≤36. This proof does not require f to be G-equivariant. It therefore applies to the non-invariant negative perturbations T_a as well as Q.

Every actual negative quadratic map commutes with the fixed negative-pencil radical, and Q does so by hypothesis. Hence Q+tT_a is J-linear over every scalar extension, including the generic rational and Laurent-series fields used in obstruction calculations. The image and quotient dimensions in (1)-(2) remain unchanged under field extension.

## 5. Exact generic rank and all later original obstructions

PR979/982 retain the previously proved original first vanishing and original-second generic rank3. The exact original third-vanishing theorem at db51525015bb7c5e825833d550d08dedf6f6ea96 is also pinned directly as inputs/third-zero.md; its §4 states the second rank3, and §5 explicitly retains the 33 unit and three valuation-two Smith factors. Those lower-order facts, not its third-zero conclusion, supply the present lower bound. Let K be the function field of the negative-direction plane, working in an affine trivialization, and use the formal variable t. Cancel the 33 invertible Q pairs in M over K[[t]]. First vanishing makes the remaining 4×8 differential divisible by t². Its t² coefficient has rank3. Consequently M has rank at least36 over K((t)). Section4 supplies the reverse inequality, so its rank is EXACTLY36, with generic kernel dimension5 and cokernel dimension1.

For an all-orders formulation, perform invertible row/column operations on the 4×8 remainder to isolate its three order-two pivots. The remaining block has shape1×5 and order at least three. Any nonzero entry in it would make the total rank37 over K((t)), forbidden by Section4. Therefore this entire residual formal block is identically zero. Equivalently, the formal matrix has Smith form with 33 unit pivots, three t² pivots, and a zero1×5 residual block. Its cokernel over K[[t]] is

    K[[t]] ⊕ (K[[t]]/(t²))³.

Thus every original higher Bockstein after the second vanishes at the generic negative direction. The old third vanishing is included but is NOT counted as new. The newly forced fourth-zero and all later generic vanishings are consequences of the radical quotient obstruction, not evaluated coefficients. No assertion about exceptional directions with a larger second-page kernel is made. This is compatible with an unresolved source: the resulting generic cokernel line is not itself a contradiction with any maximal-rank theorem established here.

## 6. Force the cubic gate to vanish

PR973 proves that the actual quotient first symbol b_T,a:D→P is generically onto. Thus the quotient family T is onto over the generic Laurent-series field: cancel its Q-contractible pairs, leaving a differential t times a matrix whose leading coefficient is onto.

For S, PR973 gives first-symbol rank3, with surviving source D and rank2 target E. PR979 gives internal second vanishing. PR982 constructs the global cubic r:D O(−3)→E and proves that EVERY nonzero equivariant cubic of this type is generically onto E. Consequently if r≠0, after the constant and first-order cancellations the first nonzero surviving S differential is t³ times a generically onto matrix. S would be onto over the same generic Laurent-series field.

An exact sequence of two-term complexes 0→S→M→T→0 has M onto whenever both S and T are onto: lift a target through the quotient, then correct its discrepancy in S. Therefore r≠0 would make M=Q+tT_a onto over that field. This contradicts §4. Hence

    r=0.                                               (5)

By the exact original-fourth comparison and zero/nonzero equivalence proved in PR982 §5, the generic original fourth Bockstein also vanishes. This is not a new proof of the previously known original third vanishing. It selects the zero alternative in the previously unselected two-dimensional cubic gate, conditionally on full-J compatibility.

The quotient dimension obstruction also gives rank(S)≤23 on the generic locus where T is onto, since rank(M)≥rank(S)+rank(T) for the upper-triangular subcomplex/quotient matrix there (the quotient-kernel connecting block can contribute additional rank). It does not identify a later nonzero internal symbol or prove every later internal symbol vanishes.

## Verification scope

The accompanying exact checker authenticates the retained proof bytes, enumerates the image multiplicities subject to the proved constraints, checks all dimensions, and constructs a synthetic constituentwise Q/J diagram with precisely the required kernels, images and compatibility. The model is not an actual HM occurrence; it checks that the new image calculation is consistent and does not accidentally confuse joint kernels with collective images. The written proof supplies the actual geometric premises and higher-symbol comparison.

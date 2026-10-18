# Fixed-field derivations and pinned source incidence

## Result

There is a precise limit on interpreting a conditional source-response calculation as an actual variation. On the fixed elliptic-product field

    K=k(E^4),  E: y^2=x^3-x,  char(k)=0,
    V_i(x_i)=y_i,  V_i(y_i)=(3x_i^2-1)/2,

any k-linear derivation sigma commuting with all four V_i is a constant combination of them. If sigma also commutes with the full-sign projector pi15 for the four independent y-sign involutions, then sigma=0.

This is a theorem about this fixed field and these commutations. It does not prove that source deformations are impossible, that any target cancels or is nonzero, or that H24 is an independent coordinate. THEOREM.md contains the proof and exact extension qualifications.

## Short proof

The four V_i form a K-basis of Der_k(K), since x_1,...,x_4 are a transcendence basis and K is a finite separable extension of k(x_1,...,x_4). Their common constants are k: an element annihilated by every derivation is algebraic over k, and geometric integrality makes k algebraically closed in K.

Writing sigma=sum_i f_i V_i gives

    [sigma,V_j]=-sum_i V_j(f_i)V_i.

Thus commuting with every V_j forces f_i=c_i in k. For each i, use the formal witness

    w_i=x_i product_{r != i} y_r.

Its full-sign projection is zero, whereas

    pi15 sigma(w_i)=c_i product_r y_r.

Terms with derivatives on another axis have the wrong character and project to zero. Since the product of y_r is nonzero in K, commutation with pi15 forces each c_i=0. This requires commuting with the single full-sign projector, not necessarily every deck involution separately.

## Important qualifications

- On K(t), with invariant t and V_i(t)=0, the nonzero derivation partial_t commutes with all V_i and pi15. A parameterized source family requires its own compatibility checks.
- On a finite algebraic extension L/K, the commuting derivations have coefficients in the algebraic constant field of L. If an extended deck action fixes those constants, the zero theorem remains valid. It also holds for commuting derivations preserving K.
- Without that restriction, the statement fails: over Q let L=K(u), u^2=2, and let the first deck generator flip u as well as y_1. Then u V_1 is nonzero and commutes with all V_i and pi15.
- For k larger than Q, k-linearity matters. A merely Q-linear derivation could vary k. Characteristic zero and the specified projector action are essential premises.

## Source-specific incidence verified

The supplied bounded excerpts pin these concrete implementation choices:

1. The transition is literally

       g_ij=D_j (P_i I_j)^t D_i^-1.

   Its primitive I/P and normalization families also feed the HPL insertion. H24 is derived as tf(g_ij^-1 V_2 V_4 g_ij), not introduced as an independent literal leaf.
2. `source_and_lift` constructs `RawSource`, and `RawSource.T` selects `model.s_raw`. The actual scalar therefore includes all four signed block wedge traces, both endpoint-linear contributions, and the final `-15 qa qb/8` term. Substituting an alternate compiler scalar solver would change the source being analyzed.
3. The HPL recursion transposes the residual once, keeps both degree-signed homotopy contributions, and chooses each face's own leading owner. Stage 2 has the negative coefficient: `J2=-H delta H delta j`.
4. The literal selector uses blocks `(3,1)` and `(2,0)` and entries `[5][0]`, `[1][3]`, `[4][2]`, with sorting parity and every original outer weight. The admitted stage-2 call checks five distinct canonical owners; relating them to the original list uses the sorting routine's permutation contract.
5. `I_phys=I_i D_i` and `P_phys=D_i^-1 P_i`. D cancels in IP, but generally remains inside `j(X)=I_phys X^t P_phys`. Shared ancestry is a possible dependency path, not proof that every variation changes the selected scalar.
6. The literal normalization `nu` is a product of y_i/x_i; it already lies in K. Primitive entries are rational functions of elementary-symmetric coordinates with supplied chart coefficients. The fixed-field theorem applies when those coefficients lie in the fixed base field, which sigma annihilates. No assertion is made about separately root-adjoined or parameterized source algebras.

The source-specific routing and the fixed-field theorem are the results. A general Leibniz expansion of an assumed source derivation is bookkeeping, not evidence that such a nonzero derivation exists.

## Conditional response interpretation

For a separately specified admissible derivation sigma on a larger algebra, let A=D_j(P_i I_j)^t D_i^-1 and H24=tf(A^-1 V_2 V_4 A). If sigma commutes with V_i and fixed transpose/trace projection, then

    sigma A=(sigma D_j)(P_i I_j)^t D_i^-1
            +D_j((sigma P_i)I_j+P_i(sigma I_j))^t D_i^-1
            -A(sigma D_i)D_i^-1,

    sigma H24=tf(-A^-1(sigma A)A^-1 V_2 V_4 A
                 +A^-1 V_2 V_4(sigma A)).

The mixed derivative of the three ordered factors in A has nine Leibniz placements; the two factors inside the transpose have four. The accompanying kernel and all other source-bound terms must also vary. No independent sigma H24 with all other entries frozen is supplied.

Moving sigma through extraction additionally requires commutation with pi15. Otherwise retain

    sigma(pi15 X)=pi15(sigma X)+[sigma,pi15]X.

The same caution applies to staircase maps, restrictions and selectors. Fixed discrete owner conventions alone do not imply these commutations. The previously reviewed marked H24 dual identity is inherited and is not a total source coefficient or a new identity here. No cancellation follows from the present theorem or incidence analysis.

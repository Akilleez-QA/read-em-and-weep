> Historical mathematical review of the source manuscript. This is not a new independent review or a formal verification certificate. Original source-byte hashes refer to the archived manuscript; public-byte hashes are in SOURCE-BINDINGS.json.

# Independent audit

## Verdict

The proof is correct over C, conditional on its explicitly cited universal representation and orbit results. In particular, **no nonzero cubic passes through the ten points**. The incidence partition, quartic ideal-sheaf generation, and degree-eight double-point base-scheme claim also pass audit. No correction is necessary for the stated conclusions.

## 1. No-cubic check

The ten points are the axes of the ten order-three subgroups in the irreducible three-dimensional A5 representation T. The invariant nondegenerate quadratic q is nonzero on each axis: its eigenvalue-one line is orthogonal to the other two eigenspaces, and an isotropic axis would therefore lie in the radical.

The stated symmetric-cube decomposition is correct. On the A5 classes of orders 1,2,3,5,5, its character is (10,-2,1,0,0), equal to the character of T + T' + P4. In particular there is no invariant cubic. Irreducibility supplies no invariant linear form, and Sym²(T*) = 1 + P5 supplies the unique invariant quadratic q.

If the cubic vanishing space U were nonzero, its greatest common divisor h would span a one-dimensional A5 representation. This is an honest character because T is an honest A5 representation; perfectness makes it trivial. Since deg h is at most three, a positive-degree h must consequently be a scalar multiple of q. Each F in U would equal q times a linear form vanishing on X. The span of X is all of T by irreducibility, so that linear form is zero.

If h has degree zero, choose any nonzero F in U. For every irreducible factor r of F, the members of U divisible by r form a proper linear subspace, since r does not divide the gcd. Over C a finite union of proper subspaces cannot exhaust U. A member G outside their union is coprime to F. Plane Bézout then bounds their number of distinct common points by nine, contradicting the ten points of X. This also covers the possible reducibility and multiplicities of F.

Thus H⁰(I_X(3)) = 0 with no generic-position assumption.

## 2. Incidence and orbit check

The cited stabilizer theorem gives each point a Dic3 stabilizer with one involution, and places its stable line in that involution's positive eigenspace. Any additional positive plane through the point would give another involution in its stabilizer. Therefore every point has exactly one positive-plane incidence.

The involutions of F5² ⋊ SL2(F5) are exactly (v,-I), giving twenty-five conjugate involutions. Distinct such involutions cannot have the same positive plane: their product is a nonidentity translation, whose Schrödinger operator has five distinct eigenvalues and hence only five projectively fixed points. It cannot fix a whole plane. Consequently there are twenty-five distinct planes, and transitivity plus the unique-incidence result gives ten points per plane.

For the plane belonging to c=-I, its K=SL2(F5) action factors through A5. A point's stabilizer containing c lies in the centralizer of c, which is K; its order is twelve. Its K-orbit therefore has size ten and exhausts the intersection. The cited stable-line calculation identifies its points with the order-three axes. This supplies a short optional explanation of the stabilizer assertion in Section 1.

## 3. Quartic generation check

Cubic evaluation is an isomorphism because both source and target have dimension ten and the kernel is zero. Evaluations require arbitrary choices of trivializations at the points; all vanishing and nonvanishing assertions are independent of those choices.

For the resulting cubic interpolation basis C_i, the quartics C_i l with l a line through p_i belong to I_X(4). At p_i, C_i is a local unit and two independent such lines generate the maximal ideal. Outside X, some C_i is nonzero because the C_i form a basis of the base-point-free complete cubic system; a line through p_i avoiding the selected outside point then supplies a nonvanishing quartic. These arguments prove global generation of the full ideal sheaf I_X(4), including its scheme structure at X.

Multiplication by a line missing all ten points gives surjective quartic evaluation from surjective cubic evaluation. Hence h⁰(I_X(4)) = 15 - 10 = 5.

## 4. Degree-eight square-ideal check and precise scope

The evaluation surjection from the five quartic sections generates I_X stalkwise. Pairwise products therefore generate its sheaf square I_X² in degree eight. At a point of X this square is the square of the maximal ideal; off X it is the unit ideal. It is exactly the ideal sheaf of the ten ordinary double points in the smooth plane.

All these products lie in H⁰(I_X²(8)), so the base ideal sheaf of the complete degree-eight double-vanishing system contains I_X². Conversely every section of that system lies in I_X², giving the reverse inclusion. Its base scheme is consequently precisely the ten double points, with no curve or residual points.

This argument is about ideal sheaves and the base scheme. It does not require or assert that the pairwise products form a vector-space basis of H⁰(I_X²(8)), or that the ordinary square of the homogeneous saturated ideal is itself saturated. It does not produce ambient degree-eight forms with compatible normal derivatives along the twenty-five planes.

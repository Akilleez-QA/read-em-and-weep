# Audit of the abstract discriminant theorem

The retained checks below verify the abstract evaluation theorem with E₀=V⊗sl(U) defined at the outset. No module identification or multiplication-adjointness assertion is imported. The former representation-identification and geometric common-kernel checks are outside this publication's scope. Exact packaged bytes are recorded in SHA256SUMS.

## 2. Operator equations

For a=p tensor H+q tensor E+r tensor F, evaluation on xe_1+ye_2 is exactly (xp+yq)e_1+(xr-yp)e_2. Grouping all first input coordinates and all second input coordinates gives the block matrix [P Q; R -P]. P, Q, R can be arbitrary for an ordered tuple in E₀; the Grassmannian parameter space subsequently imposes independence of its five operators.

The cokernel dimension is 10−dim(JU) by rank-nullity. A span of dimension less than five cannot yield an invertible ten-column map. Both primal and dual equations follow directly, with the minus sign in sQ−tP correct.

For nonzero lambda, some contraction lambda_v is a nonzero row on U. Multiplication of that row by arbitrary trace-zero 2-by-2 matrices gives all U*. Hence f_lambda is onto for every lambda, including decomposable ones. Its kernel always has dimension thirteen. This is the key uniform assertion behind the incidence geometry; it does not depend on generic tensor rank.

## 3. Divisor class, irreducibility, and incidence fibers

The universal domain bundle has determinant (det T)^2 tensor (det U)^5. The target is constant, so the determinant section has class O_G(2), up to a constant line. The universal invertible and rank-nine examples are valid abstract vector-space examples. They respectively establish a nonzero determinant section and a nonempty corank-one locus. They do not evaluate an actual conductor or HM instance.

Over P^9 the family of f_lambda is a surjective map to U* tensor O(1), so its rank-thirteen kernel is a vector bundle. Therefore Z=Gr(5,K) is smooth irreducible of dimension 9+5(13-5)=49. Its projection is proper, and its image is exactly determinant degeneracy by the annihilator criterion. For a fixed J its fiber is exactly P(coker beta_J dual), of dimension c-1 for corank c. This description is scheme-theoretic: the equations in lambda are linear.

The corank-one example gives a zero-dimensional fiber, so the generic fiber has dimension zero and the image has dimension 49. Its support is irreducible. On the corank-one open set, the rank-nine image is a subbundle locally, its annihilator is a line bundle, and this defines a regular inverse to the incidence projection. Thus the claimed isomorphism there is stronger than, and justified beyond, a set-theoretic singleton-fiber argument.

## 4. Smoothness and reducedness

At corank one, the derivative of the determinant is a nonzero scalar multiple of lambda(delta beta(k)) for nonzero kernel and dual-cokernel vectors k and lambda. Expand k as sum a_j tensor u_j. Since k is nonzero, at least one u_i is nonzero. The tangent space is Hom(J,E_0/J); varying only a_i is legitimate. Because f_lambda vanishes on J, it descends to E_0/J and remains onto U*. One can consequently select that variation with lambda(delta a_i(u_i)) nonzero. The determinant differential does not vanish. This proves smoothness at every corank-one point, not merely at the exhibited example.

At corank at least two, all size-nine minors vanish. Thus the full matrix determinant differential vanishes, and so does its pullback to the Grassmannian. Such points are singular for the hypersurface scheme.

The support is irreducible and the determinant has multiplicity one at a smooth corank-one point. On the smooth Grassmannian a nonzero effective Cartier divisor is locally Cohen-Macaulay and has no embedded associated components. Therefore generic multiplicity one implies that the entire divisor is reduced. Equivalently, local regular rings are factorial and its sole prime-divisor factor has exponent one. This validates the smoothness criterion for the reduced divisor and the description of Z as a resolution.

### Normality and rationality additions

I also checked the final strengthening. The inverse image of the singular locus is a proper closed subset of the irreducible 49-dimensional Z and therefore has dimension at most 48. Every fiber over the singular locus has dimension at least one. Applying the fiber-dimension inequality to each component gives dim Sing(D) at most 47. Thus the 49-dimensional reduced irreducible D is regular in codimension one. The Cartier hypersurface is Cohen-Macaulay, hence S2, so Serre's criterion proves normality. Trivializing K on a dense open subset of P^9 makes the corresponding open of Z a product with Gr(5,13). Both factors are rational, so Z and its birational image D are rational. This does not prove rational singularities, and the proof explicitly avoids that claim.

## 5. Rank-one output explanation

The projectivized decomposable covectors form P(V*) times P(U*), of dimension four plus one. Restricting the same rank-thirteen kernel bundle gives incidence dimension 5+40=45. Its proper image is closed and irreducible, with dimension at most 45. For the existing four-H-blocks-plus-E-block example, the only missing output direction is v_5 tensor e_2. Its unique dual-cokernel line is therefore v_5* tensor e_2*, a decomposable covector. The restricted incidence has a zero-dimensional fiber there, so the generic fiber dimension is zero and its image has dimension exactly 45. Hence its codimension is exactly five in G and exactly four in D.

For lambda=ell tensor phi, the annihilator condition is precisely phi rho_ell(a)=0 for all a in J. If phi=(1,0), trace zero and phi A=0 force A=[0 0;c 0]. This is one-dimensional, square-zero, and both its image and kernel contain the appropriate line ker phi (the nonzero members have image and kernel exactly that line). Therefore the nilpotent-line criterion is an exact equivalence, including the possibility rho_ell(J)=0.

The irreducible divisor has a nonempty open corank-one locus, and the rank-one-explanation image has strictly smaller dimension. Thus a generic failure has a unique rank-two output annihilator. No implication between corank and tensor rank beyond the stated facts is being assumed.


## Publication-scope review

The opening defines abstract vector spaces and an operator subspace. The proof of properness uses only explicit abstract operators. All bundle, tangent, incidence, reducedness, normality and rationality derivations remain. The theorem does not claim rational singularities at this stage or identify an actual geometric family's operator span.

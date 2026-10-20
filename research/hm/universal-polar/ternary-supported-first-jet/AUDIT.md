# Prior mathematical audit

This audit concerns the source manuscript. It is not a formal verification or a review of later normalized publication bytes.

# Independent audit of PROOF.md

## Verdict

The construction is valid as an abstract first-order supported-ternary countermodel, for both nondegenerate and rank-one metrics. No substantive gap was found in the quotient construction, universal repeated-input injectivity, supported correction, or exact dual-number ranks. Its scope is correctly restricted to first-order identities: it neither produces an integrated surface nor excludes all higher-order continuations.

One presentational gap should be repaired: the nondegenerate-metric irreducibility assertion refers to an unspecified existing countermodel. A self-contained proof is supplied below. No numerical source-operation values or large computations were used in this audit.

## Detailed checks

1. **Choice of v.** The isotropic square locus has projective dimension one for either allowed metric rank. For a fixed nonzero square, evaluation from Hom(K,E) onto E is surjective, and requiring its value to lie in the associated line has codimension two. Thus the bad incidence has dimension at most 14, versus parameter dimension 15. Its image is closed by projectivity. The square-avoidance open is nonempty.

2. **Compatible rank-two locus.** The rank-one metric determinant polynomial is indeed irreducible by the primitive-linear-polynomial argument given. On the rank-two locus, compatibility is one nontrivial linear equation in v, so the universal incidence is a rank-14 vector bundle over an irreducible threefold and has dimension 17. The displayed choice v(q0)=0 with nonzero derivative along a projective tangent direction makes the projection to the 15-dimensional v-space submersive there. It is dominant; its generic nonempty fibers have dimension two. Intersecting that generic open with square avoidance is legitimate.

3. **Universal dimensions.** W has dimension 5*10-10=40. For any nonzero a, B_a has kernel C a² and image dimension 14: split V=C a plus a four-dimensional complement and inspect the symmetric-complement and mixed components separately. Consequently F_u/L(K) has dimension 9, as used later.

4. **Ten-dimensional N.** Its E-first-factor components separately recover q0 and q1, so the parameterization K direct-sum K -> N is injective. The E tensor (z wedge E) component of an element of F_u vanishes, forcing q1=0. Conversely L(K) is contained in F_u. Hence N intersect F_u=L(K).

5. **Rank-one avoidance.** For a nonzero rank-one tensor in N, its nonzero E-component forces both symmetric q_i to have image in one line Ce. Symmetry then gives q_i=c_i e². Membership in K makes e isotropic. The E-rows force the two-form factor to be proportional to (c0 u+c1 z) wedge e, while the u-row equals minus (c0 u+c1 z) wedge v(e²). Those two wedge products are independent by square avoidance. This is a contradiction, including when either c_i is zero.

6. **All middle points.** The repeated-input projective locus X is closed: it is the image of the flag variety of a line inside a two-plane in V, under (Ca, span(a,b)) -> [a tensor (a wedge b)]. Its dimension is 4+3=7. Since the projection center P(N) misses X, its projected image in P(W/N) is closed and has dimension at most 7. The incidence of ten-planes containing one such image point has dimension at most 180+7=187, strictly below Gr(10,30)'s dimension 200. This establishes simultaneous avoidance at every nonzero complex middle vector, not just at u. The separate nine-space avoidance condition is a nonempty open and intersects this one.

7. **Central kernel and correction.** M intersect F_u=L(K) implies ker(B_u after quotient) is exactly C u² plus {q-u v(q):q in K}, using the symmetric-product normalization B_u(u v)=A_u(v). Thus the full central map has rank 9. Its repeated image has dimension 4 and the residual rank is 5. The correction takes values in E, as required by support.

8. **Dual-number exactness.** The expansion L(q)+tD(q)-t² A_z(v(q)) is correct. Over C[t]/(t²), it supplies the entire supported correction identity for K tensor A, rather than merely tangent determinantal equations. The six kernel generators form a direct summand: their central reductions are independent, so a six-by-six minor is a unit. A central nine-by-nine minor of the full map is also a unit. Splitting off this invertible block and using the direct six-dimensional kernel makes the remaining block zero. Thus the full image and kernel are free of ranks 9 and 6, respectively. The repeated map similarly has free rank 4 (a central four-minor is a unit, and its primitive kernel vector u_t bounds the rank). Its image is a direct summand inside the full image, so the residual map has free image rank exactly 5. This is valid over the nonreduced base, not only on its closed point.

9. **Transversality and scope.** The derivative z modulo Cu is outside E=H_0/Cu. For rank-one h it is also outside rad(h)=P_0/Cu. Nonzero v exists by square avoidance, and global repeated-input injectivity makes A_z(v(q)) nonzero for some q. This obstructs precisely the stated straight-middle, constant-data continuation to order two. Other second derivatives alter the equations and can potentially cancel this coefficient. No claim about their impossibility follows.

## Self-contained repair for the nondegenerate-metric reference

Let B=P(E*) parametrize kernel lines C lambda, and put S_lambda=ker(lambda), a two-plane in E. The family Sym² S is a rank-three bundle on B. Contracting with nondegenerate h gives a nowhere-zero bundle functional: if it vanished on Sym² S_lambda, then S_lambda would be a totally isotropic two-plane, impossible for a nondegenerate form on a three-dimensional complex space. Its kernel is therefore a rank-two bundle. Its projectivization is an irreducible smooth threefold. On the nonempty open where q has rank two, the map (C lambda,[q]) -> [q] identifies this open with the rank-two locus in P(K), since a rank-two q has a unique kernel line. This proves the needed irreducibility and supplies smooth points. Nonemptiness follows, for example, after diagonalizing h, from q=diag(1,-1,0). This is a formal normal-form witness, not a physical-source tensor or computational search.

## Suggested wording precision

“Every complex middle point” should be understood as every projective middle point, equivalently every nonzero a in V. At a=0 the repeated map necessarily vanishes. The proof already uses the projective formulation throughout.

## Additional scope boundary: source-specific structure

The operation is a single fixed abstract quotient of the universal outer-symmetric, cyclic operation, and therefore inherits those identities. Universal repeated-input injectivity was proved for this quotient. No equivariance under a source-specific symmetry group, physical-source realization, or other global structure is proved. The conclusion excludes a deduction from the stated complete first-order supported-family identities together with the proved abstract axioms; it does not exclude a theorem using additional equivariance, source-specific algebraic identities, or global hypotheses.

# Independent review: recovering the conductor and normalization

Verdict: **PASS**. The structural deductions in PROOF.md are correct under the declared inputs. No mathematical correction is required. This is an independent mathematical review, not formal verification or a new certification of all upstream geometry.

Reviewed on 2026-10-21 UTC. I read the complete draft and the supplied complete-primary-resolution and conductor-canonical-module proofs, then reread the final draft including its derived-truncation strengthening (7a) and clarified valuation-intersection argument. The normalization resolution used here is also displayed in those inputs. No selected actual HM/source coefficients, evaluation matrices, numerical rank tests, numerical search, or large computation was used. Only structural algebra, degree comparisons, and existing exact sequences were checked.

## 1. Exact recovery of the cubic node ideal

Dualizing the last two terms of the primary resolution into P(-5) gives exactly

Ext^3_P(A,P(-5)) = coker(P(2)^10 -> P(5))
                  = (P/(g1,...,g10))(5).

The shifts are correct: Hom(P(-7),P(-5))=P(2) and Hom(P(-10),P(-5))=P(5). Comparing this module with R(5) by annihilators proves equality of the actual ideals (g1,...,g10)=I_Z. No passage to a support, radical, or saturation is involved. Because I_Z has ten minimal cubic generators, these entries are a basis of its cubic piece.

## 2. Faithfulness and the exact conductor

The proof of Ann_P(omega_R)=I_Z is valid. An element annihilating a finite module annihilates its Ext modules as well, using the coincident scalar actions on Ext over the commutative ring P. Canonical CM biduality gives Ext^4_P(omega_R,P(-5))=R, so an annihilator of omega_R annihilates R. The reverse containment follows from omega_R's R-module structure.

Consequently the actual module isomorphism M=omega_R(-5) gives Ann_A(M)=I_Z/I_S. This is exactly the conductor by the definition M=N/A. The conductor is nonzero, either because its cubic generators cannot vanish modulo the sextic primary ideal, or by taking a common nonzero denominator for finitely many generators of the birational finite extension N/A. It is radical because A/c=R is reduced. The proof of N-stability is also exact: if aN is contained in A and n belongs to N, then na belongs to A and (na)N is contained in A.

Thus the affine cone vertex has not been silently deleted, and the projective conductor has the stated reduced node scheme.

## 3. The scalar endomorphism lemma and its applications

The rank-one lemma in Section 4 is correct. Torsionfreeness injects the endomorphism ring into End_K(T tensor K), canonically identified with K. Finiteness follows by evaluation on finite generators and the Noetherian property. A finite D-algebra is integral over D, so its scalar elements belong to the normalization E. Conversely the prescribed E-action is scalar multiplication after localization, because it extends D and E tensor_D K=K. This proves the reverse inclusion and faithfulness.

The added explanation of normality of the section ring is valid. For each prime divisor F of normal X, let h_F be its coefficient in the chosen Cartier representative of H. The weighted Gauss valuation of a polynomial sum f_n t^n is the minimum of v_F(f_n)+n h_F. Membership in its valuation ring therefore imposes the section inequality on every homogeneous term. Intersecting all these valuation rings with C(X)[t] imposes exactly the section and nonnegative-degree conditions. All rings in the intersection are integrally closed in C(X)(t), so the resulting section ring is integrally closed.

This argument genuinely concerns D-linear endomorphisms, not just E-linear ones. It requires neither reflexivity nor the Cohen-Macaulay property of T. The full graded End convention is essential and is correctly stated; degree-zero End alone would not recover the normalization ring.

For T=omega_A the hypotheses hold: the actual Ext restriction identifies omega_A with the canonical module of the normal CM domain N, a torsionfree rank-one module. The shared fraction field preserves rank one over A. For T=c the hypotheses follow from the nonzero N-stable ideal just proved. Both endomorphism algebras therefore identify with the actual N inside the common fraction field, with their A-algebra structures fixed by multiplication. These are genuine algebra reconstructions, not just module isomorphisms.

The kernel/image description of omega_A in (6) has the correct dual shifts. Formula (7) is a valid natural module isomorphism obtained by applying Ext^2 to the actual restriction omega_N -> omega_A and then using CM biduality for N. The draft correctly refrains from extracting a ring product from an unspecified double-Ext module identification.

Dualizing the normalization resolution gives precisely

0 -> P(-5) direct-sum P(-3)^5 -> P(-2)^10 -> P^4 -> omega_A -> 0.

Exactness uses the sole Ext degree two of the CM module N, and all dual entries remain in the homogeneous maximal ideal, so minimality is preserved. There are exactly four degree-zero canonical generators.

Sheafification in (9) is justified by localization of Hom for finitely presented modules. On the standard affine cover D_+(x_i) of Proj(A), inverting the degree-one x_i identifies degree-zero localized graded Hom with Hom of the corresponding sheaves. Hence the recovered sheaf algebra is nu_*O_X and its relative Spec is X. The Proj formulation is consistent with the finite graded normalization/section-ring input.

## 4. The conductor resolution

All positive-degree Tor maps from A to R vanish for the stated degree reasons: degree 6 versus 3 in homological degree one, degree 7 versus 4 and 5 in degree two, and degree 10 versus 7 in degree three. The map on Tor_0 is the identity. Therefore

Tor_0(c,C)=C(-3)^10,
Tor_1(c,C)=C(-6)^10 direct-sum C(-5)^4 direct-sum C(-4)^10,
Tor_2(c,C)=C(-7)^20,
Tor_3(c,C)=C(-10) direct-sum C(-8)^5,

and there are no higher Tor groups. The noncanonical splitting of short exact sequences of graded vector spaces is sufficient to determine the free terms; no splitting of modules or differentials is presumed. The resulting projective dimension three gives depth_P(c)=2, and the maximal shift minus homological degree gives reg_P(c)=7. Being a non-CM ideal of N causes no conflict with the rank-one lemma.

## 5. The added canonical double-Ext map is the inclusion

The map-level strengthening now included after (7) is correct. The following expanded check verifies both the shifts and its naturality, including the recovery of the normalization extension in (7a).

Put W=P(-5), D=RHom_P(-,W), C=Ext^3_P(A,W)=R(5), and B'=Ext^2_P(omega_A,W). The only cohomology modules of D(A) are omega_A in degree two and C in degree three. Its canonical truncation triangle is

omega_A[-2] -> D(A) -> C[-3] -> omega_A[-1].

Here the brackets use cohomological shifts. Since omega_A is CM of codimension two and C is CM of codimension four,

D(omega_A[-2])=B',
D(C[-3])=omega_R(-5)[-1].

Applying D to the truncation triangle and using perfect biduality over the regular ring P yields

omega_R(-5)[-1] -> A --eta_A--> B' -> omega_R(-5),

and hence the exact sequence

0 -> A --eta_A--> B' -> omega_R(-5) -> 0.

Let j:A->N be the actual inclusion and phi:omega_N->omega_A its induced Ext restriction. Naturality of truncation and perfect biduality gives the commutative square

Ext^2(phi,W) composed with eta_A = eta_N composed with j,

where eta_N:N->Ext^2_P(omega_N,W) is the usual CM biduality isomorphism. Both Ext^2(phi,W) and eta_N are isomorphisms. Thus the specific identification

B' --Ext^2(phi,W)--> Ext^2_P(omega_N,W) --eta_N^(-1)--> N

sends eta_A to j. Equivalently, as written in the final draft, D(N)=omega_N[-2] -> D(A) factors through the canonical truncation omega_A[-2], with factor phi[-2]; dualizing this factorization produces the same equality. The double-Ext edge map is therefore exactly the actual inclusion A->N, not merely some map to an abstractly isomorphic module. Its cokernel identifies with the actual N/A. This argument fixes the map but still does not define a ring multiplication by abstract module biduality; the endomorphism algebra construction in (5) remains the appropriate intrinsic ring construction. No splitting of the two cohomology modules of D(A) is used.

## 6. Contribution and scope

There is meaningful new content beyond the input resolutions: the actual last differential recovers the exact homogeneous conductor, and either this conductor or the intrinsic canonical module reconstructs the normalization as an A-algebra. The conductor's complete minimal resolution is a further independent exact consequence. The proof does not claim to derive explicit differential entries, full-adjoint vanishing, prescribed-source membership, higher lifting, or algebraicity, and none of those conclusions follows from this review.

The cited Stacks Project page was checked: https://stacks.math.columbia.edu/tag/0DW3 is the section on dualizing/canonical modules and supports the draft's terminology. The scalar endomorphism lemma used here is proved in full, rather than delegated to that terminology citation.

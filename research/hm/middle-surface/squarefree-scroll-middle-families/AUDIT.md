# Independent audit: rectangular middle-image bound

## Verdict

PASS under the intended trilinear hypotheses. The dimension-one bound for the middle image of the rank-at-most-one (2,3)-rectangular incidence is proved. The scroll consequence holds for the explicitly parametrized, compatible type III scrolls specified in the proof. No additional residual-rank or boundary-type assumption is needed.

The opening statement originally omitted the word trilinear. The author corrected this during the audit and now explicitly specifies a trilinear map and a finite-dimensional complex target J. This resolves the only wording correction identified. Finite-dimensionality causes no loss, since a trilinear map from finite-dimensional V has finite-dimensional image span.

## Material inspected

- The complete local PROOF.md.
- The complete /research/hm/middle-surface/extremal-surface-geometry/PROOF.md, with an independent verification of the finite-polar theorem in Sections 1–3.
- The complete /research/hm/normalizer-rank-five/full-support-scroll-exclusion/PROOF.md, especially the type III parametrization and correction formulas in Section 6.1.
- The lift-reconstruction convention in /research/hm/middle-surface/rank-six-surface-reduction/PROOF.md, Section 6.

The residual-rank applications elsewhere in the imported finite-polar document are not needed for this result. Their additional classification hypotheses are not silently imported into this audit's verdict.

## 1. Imported finite-polar theorem

For independent u,h, expansion gives

    A_{u+t h}(h) = A_u(h) - t A_h(u).

Both values on the right are nonzero by repeated-input injection. A linear dependence therefore contradicts injection at u+t h. Consequently the polar z -> f(h,u,z) is injective on span(u,h). On the rank-at-most-two determinantal locus it has rank exactly two and its three-dimensional kernel complements that plane. The diagonal has rank four and is absent.

On any reduced irreducible projective component of this locus, the constant rank gives a vector subbundle kernel. This remains true over a singular reduced base: local inversion of a rank-two minor and the vanishing rank-three minors yield the usual block decomposition. The two tautological lines and this kernel split the trivial bundle. Their projections are global matrices of regular functions, hence constant on an integral projective variety over C. Both projective coordinate maps are constant, so the component is a point. Noetherianity gives finite support. Nonreduced structure is neither discarded in the claim nor incorrectly ruled out.

Verdict: valid. No normality is needed for this preliminary projector argument.

## 2. Boundary localization

If u lies in X, the image A_u(Y) has dimension at least two, contradicting the rectangular rank bound. If u lies in Y after u is excluded from X, outer symmetry identifies f(X,u,u) with A_u(X), of dimension two. Thus u lies in neither subspace.

If X is contained in Y, then f(a,u,a) = -2 A_a(u) is a nonzero vector in the same fixed line for every nonzero a in X. A scalar coordinate identifies this with a homogeneous binary quadratic without a projective zero, impossible over C. The zero-image case is also immediately excluded in this argument. Hence dim(X intersection Y) is at most one.

If their intersection is Ch, the rectangular condition and outer symmetry place f(h,u,X+Y) in the same line. Since X+Y has dimension four, adjoining one further vector increases the image dimension by at most one. The full polar rank is therefore at most two. This puts the middle point in the fixed finite set F from the imported theorem.

Verdict: valid on the entire closed incidence, including degenerations. It does not use a normal form at the boundary. The optional claim that no rectangular restriction has image zero also follows: each x in P(X) would otherwise give a different point of the finite polar-pair locus, because Y lies in its kernel.

## 3. Stein factorization and normality

Normalization T of an integral projective component is normal integral and projective. Its proper surjection to its reduced image B has Stein factorization through a finite B-scheme B'. The intermediate space is integral and normal even if B is not normal.

For explicit justification of the last assertion, over an affine open W in B the relevant ring is Gamma(g^{-1}(W), O_T). It is a domain inside the function field of T. An element of its fraction field integral over this ring is integral over every local ring of the normal open g^{-1}(W), hence regular at every point, hence a global section. Thus the ring is integrally closed. This verifies the normality needed below rather than assuming it from normality of B.

Finite surjectivity gives dim B' = dim B, and B' is projective. The inverse image of B intersection F under the finite morphism is finite.

Verdict: valid.

## 4. Descent and Hartogs extension

On the inverse image of U = B' minus that finite set, the tautological two- and three-plane bundles are complementary. Their projector is therefore a regular global matrix there. The sheaf identity h_* O_T = O_{B'} restricts to U, so every matrix entry descends to a regular function on U. Connected fibers alone would not establish this for arbitrary functions; the proof correctly uses the stronger sheaf identity furnished by Stein factorization.

If dim B' is at least two, the deleted finite set has codimension at least two. Normality gives extension of regular functions to all of B'. Projectivity and integrality then make each extension constant. Since the open inverse image is nonempty and dense, X and Y are fixed complementary subspaces there; separatedness and reducedness extend the corresponding constant Grassmannian maps to all of T.

Exceptional divisors above F do not invalidate this argument. Extension is performed on B', not on T. The proof does not assume that their codimension upstairs is at least two.

Finally, every point of B yields the same rectangular pair X_0,Y_0. The boundary lemma excludes B intersection P(Y_0). But dim B is at least two and P(Y_0) is a plane in P^4, so the projective dimension theorem gives a nonempty intersection. This is the required contradiction.

Verdict: valid, including the potentially delicate boundary and normality steps.

## 5. Scroll extraction and conventions

The type III correction formula has the form

    v(L N) = c L + d N,
    L = s x + t y,
    N = a z + b(s y + t w),
    c = a lambda + b(alpha s + beta t),
    d = mu s + nu t.

With the reconstruction convention A_u(v(L N)) = f(L,u,N), the lifts L-d u and N-c u satisfy f(L-d u,u,N-c u)=0: both cross terms subtract the corresponding A_u values and the final cubic repeated term is zero. This checks the signs and confirms the displayed p,q,r,s_0,t_0 formulas.

The first projection spans the two-plane X and the second spans the three-plane Y. In fact [a:bs:bt] covers P^2, with the directrix providing [1:0:0]. These spans are intrinsically recovered from the particular ordered scroll component. The unequal projection dimensions distinguish its orientation. Comparison of x,z,w,y coefficients proves that X and Y are complementary precisely when alpha differs from nu; otherwise their intersection is C(y-nu u).

Expanding f(s p+t q,u,a r+b(s s_0+t t_0)) gives exactly four zero coefficients and the relation f(p,u,t_0)+f(q,u,s_0)=0. Thus the six values generating f(X,u,Y) span at most one line.

Verdict: valid. The pointwise consequence needs no family construction, flatness assumption, extension of a rational splitting map, or uniqueness among multiple scroll components.

## 6. Scope and limitations

The theorem gives a closed containing subset of P(V) of dimension at most one, not a claim that the scroll-middle locus itself is closed. It permits curves and isolated scroll middles. The imported polar-pair finiteness theorem does not imply that all rectangular triples are finite, and the proof does not claim that it does.

The result concerns the explicit type III family and the larger rectangular incidence. It does not classify all rank-five residual kernels or all abstract cubic scrolls in symmetric rank-two loci. It is compatible with isolated synthetic countermodels.

All checks were symbolic mathematical reasoning and local text inspection.

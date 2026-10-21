# Independent mathematical review

Status: PASS. Independently mathematically reviewed; not proof-assistant verification.

Reviewed PROOF.md SHA256: 23dc13bd62d74519a2924e3fd3b378ee506f11165228b738d864c558436314e5.

## Scope and checked dependencies

The review concerns the explicit conductor-gluing families on the fixed cubic fourfold V51, not the original adjoint/source-instance or Weil-algebraicity claims. The immutable public texts of PR610 (e4898406ed2552dd40e9695f9fda3d9f1d270301), PR611 (12b28d33627cc0e8b283d142dc16439a51bb5e00), and PR637 (a5fd5de0044a12bc7bb33f3431b1aa7eae7031b6) were read independently. PR615's complete-section equality was checked against its proof, and PR638's primitive-center representation input is used as a pinned dependency.

## Verification

1. The local gluing construction is algebraic. In the normalization semilocal ring, the two residue maps have independent values by the Chinese remainder theorem. A lift of the unit residue pair (lambda,1) is a unit after restricting around the two points. Multiplication by it identifies the equal-residue module with the prescribed-ratio module. This proves local invertibility; the resulting pullback is the fixed D. For parameter rings this argument is local on the parameter space. Surjectivity onto the residue quotient and its flatness over the parameter ring justify base-change compatibility of the kernel.

2. Global changes of the pullback identification are common units because H0(M_R,O)=R. They cancel in each branch ratio, so the sixty independent ratios are not subject to another diagonal quotient. The final proof explicitly distinguishes an isomorphism over the fixed underlying scheme from a marked pair isomorphism. The pinned PR634 triviality of scheme automorphisms reducing to the identity supplies the latter claim and proves that the formal arcs are nonconstant as marked pairs.

3. The U action preserves an orientation on each five-node orbit: the stabilizer has odd order and cannot exchange two branches. Orbitwise constant ratios therefore give an honestly U-linearized degree-zero gluing bundle P_lambda. Tensoring it with L0 gives U-fixed polarization classes and the existing H-linearization with unchanged primitive central weight. It does not remove L0's U-linearization obstruction.

4. The section equation uses the essential complete-section equality H0(M,D)=H0(V,L0). Accordingly every normalization section satisfies the original gluing, and the changed equations are exactly (1-lambda_y)ev_y(s)=0. This argument is valid over arbitrary ground C-algebra extensions and is not a first-order approximation.

5. For each orbit, the five-dimensional evaluation target has primitive central H-character. Every nonzero subrepresentation has dimension divisible by five, so it is irreducible. Global generation makes the evaluation map nonzero, hence surjective and of kernel dimension five. Independently, the PR610/611 character-basis argument implies the same rank for any five-node subset of a single pentad.

6. PR610 proves that each repeated-index weight has exactly the paired repeated-index partner; hence its twenty flags give ten distinct weights. Their images are nonzero and one-dimensional. PR611 explicitly records that they exhaust the ten-dimensional dual section space. Thus the ten evaluations from the two orbits of one pentad are independent, and the combined map is an isomorphism. The two orbit kernels are complementary, without requiring any assertion about kernels from different pentads.

7. Over a field, a nonidentity single orbit parameter therefore gives exactly five sections; two nonidentity parameters from one pentad give none. The latter conditions define a nonempty dense open subset of the twelve-dimensional torus. Intersecting with an ample neighborhood of the identity preserves density and nonemptiness. Openness of relative ampleness gives the claimed polarized algebraic families, without requiring a global ampleness theorem for every torus point.

8. For R_n=C[t]/(t^(n+1)), the annihilator of t^k has dimension min(k,n+1). If n>=k, it equals t^(n+1-k)R_n and has zero residue; if n<k, it is all of R_n. Splitting the surjective five-dimensional evaluation proves formula (6) and its dimension 5(n+1)+5min(k,n+1). The combined pentad evaluation isomorphism proves formula (7) and dimension 10min(k,n+1). Consequently the stated reduction images, delayed loss, and zero/five section modules over C[[t]] follow. In particular there is no false inference that global sections commute with reduction of these varying line bundles.

9. The added positive-section support description is valid. Every K_i is a five-dimensional irreducible H-subrepresentation; intersections are H-stable, so two distinct such subspaces intersect in zero. A field-valued parameter therefore has a nonzero section precisely when its active index set is empty or contained in one equality class of K_i. The finite union of the corresponding coordinate subtori gives exactly the complex points of the positive-section locus. This is a closed reduced support statement: upper semicontinuity makes the positive-section locus closed, and equality on complex points identifies its reduced support. Distinct equality classes are disjoint, so their coordinate subtori intersect only at the identity. Complementary kernels in each pentad imply at most one index from each of six pentads per class, hence dimension at most six and codimension at least six. No stronger coincidence classification is used.

## Boundaries

This establishes occurrence, exact field-valued two-coordinate strata, and finite-Artin section modules. It does not classify all twelve orbit kernels, determine a scheme structure of a section-jump locus, give an honest U-linearization of L_lambda, deform the underlying abstract V, or prove any original adjoint or algebraicity gate. No selected source coefficient, point, matrix, derivative, numerical rank evaluation, or large computation was performed.

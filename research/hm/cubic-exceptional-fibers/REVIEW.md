# Independent review: conditional cubic fibers and differential failure

Verdict: **PASS**, conditional on the pinned predecessor PR604. No mathematical correction is required. This is an independent mathematical review, not formal proof-assistant verification.

Reviewed file: `PROOF.md`, SHA256 `a0eb2c290bcfa9f9eece55cf64f1fbab42fb2e094fb93864e70c2e801954101e`.

The review read the complete current proof and the complete supplied PR604 proof, together with its existing independent review. PR604 is used as the immutable mathematical input at commit `a4a0b5ed6e9dd0c18e3a263d1b3f8d9a49f2bf8d`; its external source audits are not repeated here. No actual HM/source coefficients, selected point instances, matrices, numerical ranks, or computer-algebra calculations were used. The common dimension r remains unevaluated.

## 1. The universal restriction and its converse are valid

An arbitrary homogeneous cubic restricted to the parameter line has only its s²t and st² terms after vanishing at both endpoints. This gives c(sz+tw)=st(sa+tb). The established O(1) embedding of the strict transform proves that a and b are independent, rather than merely assuming that the residual pencil is nonconstant.

Coefficient comparison in the linear syzygy gives L_z a=0, L_w b=0, and L_z b=-L_w a. If their common cross-term d is nonzero, a vector lambda a+mu b in both endpoint kernels must have lambda=mu=0. If d=0, their span is contained in K and therefore equals K by the dimension bound. This proves the required disjointness when r=1.

Importantly, r=2 does not follow back to d=0 merely from that elementary dichotomy. The draft supplies the necessary further argument: at every non-node point of the line, K is a two-dimensional subspace of the two-dimensional kernel of L(x), hence equals that kernel. The residual cubic values sa+tb belong to these kernels and span span(a,b), proving K=span(a,b). There is no hidden generic-position assumption or evaluation of r.

## 2. The geometric fibers are exhaustive

The predecessor's incidence restriction confines each fiber over Sigma_ell to the strict transform and the two endpoint exceptional divisors. Each exceptional divisor contributes precisely one point because its restriction is an embedding. The two exceptional points are always distinct because their divisors are disjoint.

For r=1 the target does not lie in the image of the strict transform, so these are the only two points. For r=2 the embedded strict transform contributes exactly one point. Away from the two endpoint target values it is distinct from both exceptional points. At an endpoint it coincides with exactly its own exceptional point and not with the opposite one. The argument neither treats incidence as sufficient nor misses a possible contribution from other lines: all possible points above the endpoint nodes have already been included.

## 3. The differential calculation includes every ambient direction

Differentiating the homogeneous incidence with zero projective target variation correctly gives dpi(v) tangent to the projective kernel line. The scalar ambiguity in a vector lift contributes zero because the original incidence holds.

Outside the exceptional divisors this confines a potential kernel to the strict-transform tangent line, where the restriction is immersive. On E_z the displayed universal blowup chart gives kernel T(E_z) and image the radial line represented by the exceptional point. Except at the endpoint direction p_z, that radial line and the component-line direction are distinct. A putative kernel therefore lies in T(E_z), where the exceptional embedding excludes it.

At p_z when r=2, the tangent space of M is the direct sum of T(E_z) and the transverse tangent line of the strict transform. The latter's image lies in the former's image because the entire strict-transform image line lies in Phi(E_z). Thus the full differential has rank exactly three and kernel dimension exactly one. The kernel is not incorrectly identified with the strict-transform tangent itself. The same proof applies at p_w.

The predecessor gives injectivity away from the inverse image of Sigma. Consequently these endpoint directions are the complete differential-failure support, not just examples of failure. The two endpoint target values on each line are distinct, and different Sigma_ell are disjoint. This proves exactly 120 distinct target values and 120 distinct source points, including when component lines share a node. For r=1 there are no differential failures.

## 4. Reduced fibers and the undetermined endpoint length

For a finite complex morphism, the localized scheme-fiber algebra F is Artinian with residue field C. Its cotangent space n/n² is the cokernel of the target-to-source cotangent map, hence dual to the tangent kernel. When that kernel vanishes, Nakayama over F gives n=0 and F=C. Applying this at every fiber point proves reduced lengths two and three in the respective cases. The proof does not make the unnecessary and generally unsafe assertion that the source local ring at one point of a multipoint fiber is finite over the target local ring.

A one-dimensional tangent kernel at an endpoint instead gives embedding dimension one for F. A lift t of its cotangent generator generates its maximal ideal by Nakayama. Nilpotence and the residue field C then give F isomorphic to C[t]/(t^e), for a finite undetermined e at least two. The other fiber point is reduced. This is a valid statement about the finite fiber algebra only. It does not determine e, total endpoint length, analytic branch type, or any scheme structure on the differential-failure locus.

The terminology is also correct: for these finite-type complex morphisms, vanishing of the relative cotangent module at a point is equivalent to unramifiedness there. No smooth target is needed. Unramifiedness does not imply flatness, étaleness, target normality, or that a fiber has only one geometric point.

## 5. The reduced three-curve inverse image is justified

In the r=2 case the inverse image of Sigma_ell inside either exceptional P3 is a linear P1, mapped isomorphically to Sigma_ell. The exhaustive fiber-support description therefore gives precisely the union of these two P1s and the strict-transform P1 as the reduced inverse image. Equality of reduced closed subschemes follows from equality of their closed-point supports over C.

The exceptional curves are disjoint. The strict transform meets each in its corresponding endpoint and has a tangent line outside the exceptional divisor's tangent space, so the indicated two junctions have distinct component tangent lines. Each of the three components maps isomorphically to the same target line. This establishes the stated reduced chain without asserting reducedness of the full scheme inverse image or an analytic normal form.

## Conclusion

The theorem is a rigorous conditional classification of all fibers over the known bad locus and of the complete support of differential failure. Its assumptions are exactly the pinned predecessor and elementary universal restriction, blowup, tangent-space, and local-algebra arguments. The proof leaves r and all asserted unresolved endpoint multiplicities, analytic types, and larger open goals untouched. No further mathematical expansion is needed for this bounded step.

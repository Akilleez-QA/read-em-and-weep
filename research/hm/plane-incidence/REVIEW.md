# Independent mathematical review

Reviewed artifact: `PROOF.md`, SHA256
`6ed9e0ce1bef4d4e74f11e2e31b72387d585f3a08e8947a7d5290cde195dbaf4`.

Verdict: no mathematical correction required. This is an independent mathematical review of the displayed deductions, conditional on the explicitly pinned repository inputs. It is not proof-assistant verification and does not recertify every argument in those dependencies.

## Checks

1. **Plane restriction.** A component line not contained in a plane contributes either no point or one reduced point, and disjoint components contribute distinct points. A proper hyperplane through the plane exists after excluding finitely many members of its pencil. Evaluation surjectivity on its twenty-five-point section descends to the subset and then to plane sextics. The tensor-and-image argument correctly identifies the restricted ideal sheaf, without assuming exactness on the left or discarding a Tor term. Sheaf generation is not confused with generation of the saturated graded ideal.

2. **Complete intersection.** A finite base locus permits two coprime quintics. Their complete intersection has length twenty-five and degree-six Hilbert function twenty-two. Inclusion of the plane section gives the preliminary bound of twenty-two, already enough for the nonplanarity conclusion.

3. **Residual sharpening.** Sheaf generation at each reduced base point implies surjectivity on its cotangent space. Independence of the two first jets is a nonempty open condition at each point; simultaneous independence and coprimeness follow by irreducibility of the parameter space. The complete intersection therefore has local length one at every base point. Its residual scheme is disjoint from that reduced subset and need not be reduced.

   I checked the cited public statement directly: Gold–Little–Schenck, *Cayley–Bacharach and evaluation codes on complete intersections*, section 1.2, Theorem 1.2, https://arxiv.org/pdf/math/0311129. It applies to complementary residual subschemes, not only reduced point partitions. With degrees five and five the residual index is seven. Substitution in degree six gives exactly `22-n=(25-n)-h_R(1)`, hence `h_R(1)=3`.

   A member of the generating system avoiding the finite support of the residual scheme is invertible there as a section of the corresponding line bundle, including when that scheme is nonreduced. Its products with linear forms inject into the degree-six ideal quotient because the residual scheme spans the plane. This supplies the three additional independent classes and proves the nineteen-point bound. No Bertini assumption is required.

4. **Rank exclusion.** The Artinian reduction of the saturated coordinate ring of reduced points has the first-difference Hilbert function used in the proof. Backwards Macaulay growth from its degree-six value five gives the six stated lower bounds. Their sum exhausts the degree-five Hilbert value twenty, forcing the displayed h-vector and a planar span. Such a plane cannot contain a component because the containing hyperplane is proper. The plane-incidence bound excludes this situation uniformly, not just generically. The kernel and cokernel bounds follow from dimensions fifty-five and thirty.

5. **Scope.** The argument establishes rank at least twenty-six, not exact rank or surjectivity in that degree. Its annihilator observation simplifies, but does not strengthen, PR473's bound of three on bad second factors. It makes no claim about the original fixed quadratic, actual-source membership, higher-order lifting, or algebraicity. No selected-instance calculation or numerical rank evaluation was used in this review.

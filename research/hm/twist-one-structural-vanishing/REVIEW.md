# Independent mathematical review

Reviewed artifact: `PROOF.md`.

SHA-256: `baabea589839f5b8ceba93f9e458b794fb66690384540cbd7746f621a723fa19`.

## Recommendation

**Pass, relative to the explicitly stated mathematical dependencies. No required mathematical changes.** The argument proves \(H^2\operatorname{End}_0(F)(1)=0\), universal cubic generation, and the stated universal defect-map corollaries. This is an independent mathematical review, not formal verification or an independent reproof of the full dependency chain.

## Checks

1. **Universal exterior-image estimate.** The torus degeneration is valid. Pairwise distinct weights on the 25 basis vectors of \(C\otimes T\) suffice: the Grassmannian limit is fixed by the one-parameter subgroup, so its underlying subspace is a sum of one-dimensional weight spaces. The proof neither needs nor claims pairwise distinct Plücker subset-sum weights; such a stronger claim would fail because additive weights satisfy rectangle identities. For a coordinate limit with column occupancies \(r_j\), the image dimension is exactly
   \[
   \sum_j\left(10-\binom{5-r_j}{2}\right)\geq 2\sum_jr_j=30.
   \]
   Equivariance and lower semicontinuity of rank give the asserted bound for every \(R\), not just for a chosen HM map.

2. **Symmetric-square monad and negative vanishing.** The graded symmetric square has the displayed terms and degrees and is quasi-isomorphic to \(\operatorname{Sym}^2F=B(-1)\). Local splitting, or the symmetric-square direct summand of the derived tensor square in characteristic zero, justifies this step. Tensoring the exterior Euler resolution by \(K=\Omega^2(2)\) gives \(H^i(K\otimes K)=0\) for \(i\geq3\). Together with the other stated Bott vanishings, every total-degree-three term is zero, proving \(H^3B(-1)=0\).

3. **Twist-zero cokernel and Bott calculation.** After twisting by one, every term has zero positive cohomology. The two shifted Schur weights are indeed \((5,5,4,1,0)\) and \((5,5,3,2,0)\), hence singular. The surviving global-section complex has dimensions \(28,100,50\) in degrees \(0,1,2\). Its final cokernel is \(H^2B(0)\), and its final image is precisely \(C\wedge R\). The original monad twisted by one identifies \(\operatorname{coker}(H^0(2K(1))\to C\otimes T)\) with \(H^1F(1)\); therefore \(\dim R=15\).

4. **Normalizer improvement.** The target restricts to \(2\operatorname{End}(V)\) under \(H_5\). Its invariant part has dimension two. Normalizer equivariance makes every nontrivial character multiplicity equal, since \(\mathrm{SL}_2(\mathbf F_5)\) acts transitively on the 24 nonzero characters. A quotient of dimension at most 20 cannot contain any of them. Exactness of invariants gives \(h^2B(0)\leq2\). This proof does not import a tensor-cohomology value or an evaluated HM differential.

5. **Dimension-gap argument.** PR454's exact sequence retains the incoming transgression. The newly proved \(H^3B(-1)=0\) makes its source zero, so the required cokernel identification is justified. Its lower bound is \(10\dim Z-20\). PR440's natural surjection \(p_3\), together with \(M_1=TM_0\), gives the upper bound 75: the entire \(T_4\otimes M_1\) summand maps into \(T H^1B(2)\). This uses commutativity with \(p_2\), not surjectivity of \(p_2\). The lower bound \(\dim Z\geq10\) for nonzero \(Z\) comes from PR454's full-normalizer channel alternatives, not from Heisenberg divisibility alone. Thus \(80>75\) proves \(Z=0\).

6. **Consequences and scope.** PR454's map \(\Delta\) has both nonzero scalar components, and \(H^1E_0(1)=0\) identifies \(H^1B(1)\) with its kernel, giving \(V^*\otimes(R\oplus J)\) of dimension 55. Its exact Koszul sequence gives degree-three generation; the imported degree-four and degree-five surjectivities give universal cubic generation. Quotienting by \(L=S_3I_2\) proves surjectivity of the canonical defect map onto \(H^1B(5)/L\). Since \(L\) is \(H_5\)-trivial, projection onto the canonical nontrivial-character summand is surjective as claimed. None of these implications gives surjectivity for one fixed cubic, one defect channel, or the fixed-pair endpoint.

## Dependency boundary

The review checked the new argument against the stated contents of [PR454](https://github.com/Akilleez-QA/read-em-and-weep/blob/2124f284c3bc488bd0c666c61d4347e3b8950f08/research/hm/twist-one-transgression/PROOF.md), [PR440](https://github.com/Akilleez-QA/read-em-and-weep/blob/829e03411d04511f6cf04860bf18db4a70b12448/research/hm/degree-six-structural-reduction/PROOF.md), [PR452](https://github.com/Akilleez-QA/read-em-and-weep/blob/3b1d18105fa8b8b39bd96d889a34bc81a860f181/research/hm/cubic-defect-channels/PROOF.md), and [PR453](https://github.com/Akilleez-QA/read-em-and-weep/blob/56516a96a7eacfde0c8e272ca38db415cc7f294b/research/hm/cubic-invariant-target/PROOF.md). The primary module, section resolution, classical equivariant monad, and previously proved geometric vanishings remain explicit inputs. No selected HM/source-instance map, numerical matrix rank, generator/checker, or large computation was used.

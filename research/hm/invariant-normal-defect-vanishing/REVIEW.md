# Independent mathematical review

Reviewed artifact: `PROOF.md`

SHA-256: `0b7eedd41aa23de917c93214af5855ef8d3ea4ab8bd78c5a8ea07629c2adbba8`

## Verdict

The structural deduction is sound on the explicitly pinned mathematical inputs. Both invariant cohomology groups of the ordinary square thickening at physical twist one vanish, and hence both invariant cohomology groups of the first-normal adjoint defect `omega_(2Z)(-1)` vanish. This is mathematical review, not formal proof-assistant certification and not a new verification of the entire HM foundation.

## Independently checked points

1. The symmetric-square sequence is the actual regular-section sequence on the smooth weighted stack, not a square of a coarse ideal. The cited weighted-stack note explicitly identifies its first map as multiplication by sigma.
2. Serre duality with `omega_X=O_X(-3)` makes the transpose of `H2(G(-3))->H2(B(-1))` precisely `H1(B(-2))->H1(G*)`. The determinant identification is `G*=G(-2)`. No spinor pushforward is treated as an invertible coarse bundle.
3. For the author's polarization convention, `tr(T J(sigma v))=omega(v,T sigma)` follows directly by computing the trace of two rank-one operators and using tracefree preservation of the alternating form. The identity `[T,J(sigma^2)]=J(2 sigma(T sigma))` is compatible with the same convention. Thus the dual map is genuinely evaluation, and the known nonzero bracket forces that evaluation map to be nonzero. This is not an inference from one-dimensionality alone.
4. The cited cone-shadow note supplies `H1(B(-2))^Gamma=C` and `H2(B(-2))^Gamma=0`. The Serre-residue note supplies `H1(G*)=1+V` and `H0(G*)=0`. These make the evaluation and transpose invariant isomorphisms, while `H3(G(-3))^Gamma=0` proves the strengthened vanishing of `H2(I^2(1))^Gamma` as well as `H1(I^2(1))^Gamma`.
5. The hyperplane sequence on the quadric gives the required higher cohomology vanishings of `O_X(1)`; its sections have representation `V+W`, with no invariant. The ideal sequence therefore gives both stated square-thickening vanishings.
6. The ordinary square is Cohen--Macaulay of pure dimension one by its regular-pair resolution. Proper duality then gives both defect vanishings, including `H0`, without assuming its dualizing sheaf is invertible or discarding nilpotent sections.
7. Finite-group invariants are exact in characteristic zero. The relevant canonical line factors carry no extra Gamma-character because Gamma is perfect. This argument does not erase characters for a larger block torus.

## Dependency and scope limits

The nonzero bracket is imported from the pinned midpoint theorem, whose geometric dependencies include the double-cover construction and the separately published three-channel repair. The present proof does not independently rederive that entire chain. It correctly avoids concluding a lift of the differential operator, prescribed-bundle gluing, flatness of a nilpotent filtration, or vanishing of the absolute positive cubic obstruction. Cohomology in the surrounding image sheaf or deformation complex still requires a separate comparison.

No selected HM/source coefficients, evaluations, numerical ranks, or large computations were used for this review. The local calculations above are universal rank-two identities.

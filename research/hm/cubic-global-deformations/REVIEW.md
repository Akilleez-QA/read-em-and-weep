# Independent mathematical review

Reviewed artifact: `PROOF.md`

Reviewed SHA-256: `c25a2b4deb850578fee2232da8eeeba3b68f15f245111f1b5fcc3c72e6f09814`

Review date: 2026-10-21.

**Verdict: PASS, conditional on the pinned inputs stated in Section 1.** The full argument at the reviewed hash proves its stated tangent-sheaf identification, the fourfold tangent-cohomology dimensions, Zariski local triviality of Artin deformations, and unobstructed Artin lifting. No substantive mathematical correction is required. This is an independent mathematical audit, not formal verification, and does not independently re-audit the cited repository inputs.

## Checks

- The branchwise derivation calculation is correct. The global map is constructed before completion, and coherent-module base change plus faithful flatness correctly identifies it. No unproved extension of derivations to the normalization is assumed.
- The blowup differential has the claimed tautological quotient, including its twist. The higher-direct-image computation and sheaf-level evaluation surjectivity establish `pi_*Theta_M = Theta_P4 tensor I_Z` and all positive higher-direct-image vanishings. The proof correctly avoids confusing sheaf surjectivity with global-section surjectivity.
- The two-direction Heisenberg argument annihilates the infinitesimal stabilizer without generic-position assumptions or point evaluation. It uses only the stated cyclic action on one eigenbasis and an eigenline of the other lift with every component nonzero.
- The reduced 120-point restriction sequence contributes 480 dimensions. Together with `h^1(Theta_M)=96`, this gives `h^1(Theta_V)=576`, `h^0(Theta_V)=0`, and `H^{>=2}(Theta_V)=0`. The noncanonical coordinate identifications and absence of a canonical splitting are appropriately stated.
- The cotangent local-to-global argument identifies first-order abstract deformations with `H^1(Theta_V)` without claiming vanishing of cotangent `T^2`.

## Delicate affine-lifting and gluing step

For an affine intersection `Spec R`, the vanishing cotangent sheaf gives `Ext^1_R(L_(R/C),R)=0`. Put `S=R tensor_C B` and `N=R tensor_C K` for a small extension `B' -> B`. Cotangent flat base change and derived adjunction give

    Ext^1_S(L_(S/B),N)
      = Ext^1_R(L_(R/C),R tensor_C K)
      = Ext^1_R(L_(R/C),R) tensor_C K
      = 0.

The last equality uses that `K` is a finite-dimensional complex vector space. The module structure on `N` factors through `S -> R`, since `m_B K=0`.

The twisted-marking comparison is compatible with the entire extension problem, not merely its quotient algebra. If `alpha` is the transition automorphism and reduces to the identity on `R`, twisting the reduction marking by `alpha` does not change the prescribed `S`-module structure on the square-zero kernel `N`, or the map `K -> N`: both depend only on the special fiber. Thus the two constant lifts are solutions of the same problem in [Stacks Project, Lemma 92.16.1](https://stacks.math.columbia.edu/tag/08SM). Its zero torsor supplies an isomorphism with the required reduction. The same argument supports the induction proving affine rigidity with compatible markings.

This establishes the transition-lifting property actually needed here. It does not invoke the smooth infinitesimal lifting property for a singular scheme, the issue flagged in the remark following Theorem 1.4 of [Graf–Schwald](https://arxiv.org/html/2001.06339v2).

On triple overlaps, the lifted cocycle defect is tangent-valued with coefficients in `K`. The special-fiber identity and `m_(B')K=0` make conjugation trivial, so the defect is an ordinary additive Cech two-cocycle. The finite affine cover has affine intersections, and `H^2(Theta_V)=0` removes it. The resulting glued scheme has the asserted flatness, finite type, reduction, and properness properties.

## Scope

The conclusion is precisely formal unobstructedness for marked abstract deformations over local Artin complex algebras with residue field `C`. The proof correctly does not claim algebraization, a constructed miniversal family, preservation of an embedding or HM presentation, vanishing of local/global cotangent `T^2`, or a resolution of the original algebraicity problem. No selected source-instance coefficient, point, matrix, numerical rank, or computer-algebra calculation was used in this review.

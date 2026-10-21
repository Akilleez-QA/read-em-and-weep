# Independent mathematical review

Reviewed artifact: `PROOF.md`.

Reviewed final SHA-256: `37a50c59526eb559c1b3bfe3bb15bb4b555b235f6e76376fd7470d8d5cad4010`.

Initial full-review SHA-256: `ca2a62656843e7fd633399d519aae7d406217b4450381413b52b0e9f0c8aeeaf`. Final readback confirmed that the only edits were the reviewed status line and the cosmetic correction recorded below; reverting exactly those two edits reproduces the initial reviewed hash.

Review date: 2026-10-21.

**Verdict: PASS, conditional on the pinned geometric and deformation inputs in Section 1.** The reviewed argument proves all stated conclusions, including formal polarization lifting, the 540-dimensional injective obstruction subspace, the canonical residual 96-to-110 map, and the exact Hilbert tangent formula with upper bound 195. No substantive mathematical correction is required. This is an independent mathematical audit, not formal verification or an independent re-audit of all historical dependencies.

I read the complete reviewed proof and the relevant cited global-deformation, branch-transversality, and eigenline-postulation proofs. No selected actual HM/source coefficient, matrix, point evaluation, numerical rank, search, or computer-algebra calculation was performed.

## 1. Section cohomology and formal polarization lifting

- The pushforward computation for `O_M(-E)` correctly uses the surjective sheaf map `O_P4 -> O_Z`, the vanishing higher direct images of `O_M`, and the cohomology of the exceptional `P3`s. Projection formula then gives the asserted direct images of `D=3H-E`.
- The cubic postulation input gives `h0(D)=10` and `h1(D)=5`, with no higher cohomology. The ten coordinate sections are independent and descend to `V`; the injection of downstairs sections into upstairs sections therefore proves equality of the two section spaces. This is an essential point: equality is established before concluding that the map into the length-60 normalization quotient is zero.
- The twisted normalization sequence gives exactly `0 -> H0(Q) -> H1(L) -> H1(D) -> 0`, hence `h1(L)=65`, with no asserted splitting.
- For a small Artin extension, flatness identifies the square-zero ideal sheaf with `J tensor_C O_V`. The units sequence gives a line-bundle obstruction in `H2(O_V) tensor J=0`, proving formal smoothness of the forgetful pair functor. Together with the separately established abstract lifting theorem, this proves unobstructedness of pairs. It does not imply preservation of all degree-one sections.

## 2. Differential operators on the singular scheme

The definition of `A_N` is valid on a singular scheme. In a local frame of the invertible sheaf `N`, every such operator is uniquely `delta+a`, with `delta` a derivation and `a` a function. This proves the exact scalar-symbol sequence and its coherence without a smoothness hypothesis. A change of frame has the usual derivative correction, so the definition glues intrinsically.

The first-order pair classification is also correct. One may take an affine cover trivializing `L`. The abstract first-order deformation is locally trivial by the pinned rigidity input, and invertible modules lift locally trivially over square-zero thickenings of these affines. Pair transition automorphisms reducing to the identity have the form `1+epsilon P`, with `P` in `A_L`. Their cocycle and change-of-trivialization rules are the additive Cech rules. This identifies the tangent space with `H1(A_L)`. The scalar automorphisms are present in `H0(A_L)` and do not introduce an additional quotient of this tangent space.

The evaluation map `A_L -> S* tensor L` is linear over `O_V` in the operator variable. Its Cech cohomology map is precisely the obstruction to lifting each section. Vanishing on a basis is equivalent to simultaneous lifting of the fixed ten-dimensional space, with no assertion about higher-order simultaneous lifting.

## 3. The normalization quotient of operators

The construction `A_L -> nu_*A_D` is algebraic before any completion. It uses the proved tangent-sheaf identification, not an unproved general extension theorem for normalization derivations. Pullback of the scalar part and the compatible frame-change rule give the natural injection.

At a pinched value, a common pulled-back frame identifies the descent conditions with vanishing of the two branch symbols at their marked points and equality of the two scalar residues. Thus the quotient has four tangent coordinates at each branch and one scalar-difference coordinate, of total dimension nine. Arbitrary such residue data lift because the normalization is smooth; algebraically this is evaluation of locally free sheaves at two distinct points of a semilocal neighborhood. One need not incorrectly identify that algebraic semilocal neighborhood with a product of branch neighborhoods. Alternatively, completion gives the stated branch calculation, and faithful flatness descends the coherent quotient computation.

The maximal ideal of the downstairs point annihilates the quotient, so it is a reduced skyscraper module, not merely a finite module of length nine. The sixty values give length 540. Both global operator spaces are the scalar operators; their natural map is the identity. The resulting connecting sequence therefore injects all of `H0(C)` into `H1(A_L)`, with quotient `H1(A_D)` of dimension 96. The symbol diagram also confirms that the pure Picard subspace of dimension 60 lies inside this subspace, with the stated 480-dimensional quotient.

## 4. Injectivity, residual map, and noncircularity

The evaluation square and its connecting homomorphisms commute. The final map in equation (6) is injective specifically because all normalization sections descend, as already proved in Section 2.

In a common frame, the local quotient evaluation is

    (u,v,a) maps to [s -> d f_p(u) - d f_q(v) + a s(y)].

After quotienting `S*` by its common evaluation line, the first two terms represent the two projective differentials. More precisely, the chosen nonzero evaluation functional identifies this quotient with the corresponding values in `Hom(C ev_y, S*/C ev_y)`. The branch-transversality input gives zero intersection of the tangent images and injectivity of each differential, forcing `u=v=0`; global generation then forces `a=0`. Frame changes alter derivative representatives by evaluation-line terms and are compensated by the scalar coordinate. Consequently the entire 540-dimensional subspace injects under `B`.

The construction of `b:T_pair/F -> W/B(F)` is canonical. Its kernel identifies with `ker B` by the unique correction in `F`; no choice of a splitting is necessary. Dimension subtraction gives a target of dimension `650-540=110`. The target filtration has dimensions 60 and 50 because `B(F)` lies in the 600-dimensional normalization-difference channel, leaving 60 there, while the normalization cohomology channel has dimension `10*5=50`. The proof does not infer the rank of this residual map, its generic behavior, or unobstructedness of its kernel.

There is no circular use of the desired section-preserving conclusion: the local operator quotient uses previously proved intrinsic singularity and tangent data; its evaluation injectivity uses the independently pinned branch-transversality theorem; the section-space equality uses cubic postulation and the given complete morphism.

## 5. Embedded tangent dimension

The direct lifting argument is sound. Lifted sections generate by Nakayama. Their map is proper and quasi-finite because its special fiber is a closed immersion, hence finite; Nakayama applied to the finite structure-sheaf cokernel then proves it is a closed immersion. Conversely an embedded lift provides the polarization and lifted coordinate sections. Differences between lifts of the ordered basis form `End(S)`, of dimension 100; scalar line-bundle automorphisms remove one dimension, and `H0(Theta_V)=0` excludes further infinitesimal source automorphisms.

As a separate cross-check, let `N=Hom(I/I2,O_V)` be the Hilbert normal sheaf for `V` in `P9`. The cotangent transitivity sequence and the pinned vanishing of the local cotangent `T1_V` give

    0 -> Theta_V -> Theta_P9|V -> N -> 0.

No regular-immersion hypothesis is needed for this low-degree cotangent sequence. Compare it with the restricted Euler sequence and the scalar-symbol sequence for `A_L`. Their common scalar submodule yields

    0 -> A_L -> S* tensor L -> N -> 0.

The associated cohomology sequence is

    0 -> C^99 -> H0(N) -> ker B -> 0.

Since `H0(N)` is the Hilbert tangent space, this independently confirms its exact dimension `99+dim ker B = 99+dim ker b <=195`, including the projective-coordinate contribution and the absence of an extra Picard or automorphism quotient.

## 6. Corrections and scope

No substantive correction was required. The sole cosmetic correction, replacing “Amplitude persists” with “Ampleness persists” in Section 3, has been made and verified in the final reviewed version.

The proof correctly leaves unresolved the residual map's exact rank, the dimension and smoothness of the section-preserving locus, higher-order embedded lifting, preservation of the HM/source presentation, and the original full-adjoint and algebraicity claims. None is established by formal lifting of the line bundle alone.

# Independent mathematical review

Verdict: PASS, conditional on the explicitly pinned geometric inputs in PR574, PR577, PR579 and PR581. This is independent mathematical review of the authored argument, not machine-formal verification. No selected actual HM/source-instance evaluation or large computation was performed.

Reviewed proof: `PROOF.md`, authored draft SHA-256 `707f203c9758711ed2f85ea997abb89f540f7ad51cdfa496861313d7fb948151`. A later status-only change does not change this mathematical review.

## 1. Actual local map and descent

The tensor normalization quotient is still supported at the thirty reduced double points. After trivializing the normalized pullback, its map over each base node is exactly the five weighted residue differences displayed in (1), rather than an arbitrary map with matching dimensions. The residue matrix has columns 1 and −(t_z), so it has rank one precisely on the diagonal block and rank two otherwise.

In the uniform case the kernel is isomorphic to the nodal local ring by branch rescaling. In the nonuniform case two unequal ratios force both residues to vanish, yielding the conductor module sC[[s]]⊕tC[[t]]. This module has two minimal generators and is not free of rank one. Completion is faithfully flat, and the global kernel embeds in h_*O_B, so torsion-freeness, generic rank one and the local-freeness criterion are justified.

The descent assertion uses PR581's actual repeated-ratio pullback, not only dimensions of Picard tori. Uniform blocks give the unique gluing line bundle M on Γ; projection formula with g_*O_S=O_Γ identifies g_*g*M with M. Thus all three conditions in (4) are equivalent.

## 2. Degree and defect

The image J_L is annihilated by the ideal of the six reduced nodes and has length 6+r. The exact kernel sequence therefore gives χ(A_L)=1−(6+r)=−5−r. Since χ(O_Γ)=−5, the rank-one torsion-free degree is −r. The quotient K_L has length 30−(6+r)=24−r, with local dimensions four and three on uniform and nonuniform blocks respectively. No use of a line-bundle degree formula at a nonfree stalk is made.

## 3. Derived factorization and splitting

The crucial vanishing is checked before finite pushforward: the actual quotient factors through the same sixty reduced preimages W, and Ext¹_B(N,π_*O_W)=H¹(B,N^∨⊗π_*O_W)=0. Thus the component from N[−1] is zero after choosing the smooth-base splitting. Applying exact finite pushforward preserves this conclusion. This proves the complex model in (8); dimension counts alone would not suffice.

Both J_L and V_L are direct sums of residue-field modules. Hence their inclusion admits an O_Γ-linear complement. With that choice, the complex [h_*O_B→V_L] is the direct sum of [h_*O_B→J_L] and K_L[−1]. The former is quasi-isomorphic to A_L by its surjective differential and exact kernel sequence. This proves (9) and (10), including the intrinsic identification of K_L with the torsion subsheaf of R¹g_*L.

This argument does not assume Ext²_Γ(K_L,A_L)=0. In particular it does not substitute the nonfree conductor module for the invertible coefficient in the earlier Gorenstein argument. It establishes the splitting of this particular complex, not a general Ext vanishing, canonical splitting, multiplicative formality or a family base-change theorem.

## 4. Cohomology and strata

The global constant section maps to ((1−t_z)c). It vanishes exactly at the trivial gluing point. The normalization long exact sequence and the pinned values h¹(O_X)=0, h²(O_X)=4 then yield (0,29,4) off the identity and (1,30,4) at the identity.

The derived calculation independently reproduces these numbers: off the identity h¹(A_L)=5+r and h⁰(K_L)=24−r, while h⁰(N)=0 and h¹(N)=4. This verifies the asserted cancellation and does not imply descent from constant global dimensions.

For a specified subset of r nonuniform nodes the product description is correct. Each uniform block has dimension one and each nonuniform block is the smooth irreducible open complement of the diagonal in a five-dimensional torus. Consequently the fixed-subset stratum is smooth, irreducible, locally closed and has dimension 6+4r. The r=6 stratum is open dense and the descent subtorus is closed of dimension six.

## 5. Family scope and remaining goals

The proof correctly restricts its classifications and splittings to individual line bundles. The change of χ(A_L) across strata excludes a flat coherent family having all those A_L as its fibers on a connected parameter neighborhood crossing the change, by constancy of Euler characteristic in proper flat families. It does not assume that an underived pushforward of a universal Picard bundle commutes with specialization. Relative derived descriptions, coherent choices of splittings and any stronger base-change assertion remain separate questions.

No first-order, higher-order or algebraicity conclusion for the original HM deformation problem is asserted. The result advances the residual/Picard analysis by an actual descent criterion and a direct-image defect calculation, with the derived splitting proved by its actual semisimple image.

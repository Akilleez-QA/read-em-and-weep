# Independent review of middle-obstruction symmetry

Reviewed file: `PROOF.md`.

Reviewed SHA-256: `1c52841011159092eda974d72eb2c34e30f4fafb8e91abf4f1d110a8ce10e065`.

Verdict: the proof is mathematically sound conditional on its explicitly pinned module, pairing, resolution, and equivariant inputs. This is an independent mathematical review, not a formal proof-assistant check or an independent verification of every earlier dependency.

## Independent checks

1. **Actual map, not an abstract matrix.** The identification B=L^perp is essential. It gives the actual perfect pairing A x B in total degree five. For a cycle b in K_2(B)_5, lift its image in H to z with dz=b. Then z modulo L is an A-cycle, and the connecting map sends its class to the image of [b] in Tor_2(L)_5. Thus the bilinear form displayed in the proof is precisely the pairing-induced form of delta^(-1) Tor_2(B -> L)_5, not a replacement map inferred from matching dimensions.

2. **Duality degrees.** K_i(A)_5 has coefficients A_(5-i), and K_(5-i)(B)_5 has coefficients B_i. Their coefficient degrees sum to five and their exterior degrees sum to five. Consequently these chain pairings are perfect and induce the claimed Tor_3(A)_5 versus Tor_2(B)_5 duality. No internal-degree twist is missing.

3. **Differential sign.** For exterior degrees summing to six, contraction of the zero exterior-six product yields the adjoint identity with sign (-1)^i. At i=3 this gives <dz,t>=<z,dt>. Interchanging exterior degrees two and three contributes (-1)^6=+1. Together with symmetry of b_H these signs give a symmetric, not a forced alternating, linking form.

4. **Choice independence.** All homology of K(H)_5 vanishes because H has only even resolution shifts. Differences between lifts are therefore boundaries. Their pairing with cycles vanishes by the adjoint identity. Replacing source representatives by boundaries adds pairings of elements of B, and these vanish because B is contained in L and is orthogonal to L. The proof treats both arguments. In fact K_3(B)_5=0, since B_2=0, so the representative-boundary checks in this degree are stronger than required.

5. **Characters and ranks.** Under the separately stated equivariant hypotheses, invariance pairs a character only with its inverse. The 24 nontrivial characters form 12 distinct inverse pairs. Symmetry forces each pair block to be [[0,a],[a,0]], giving rank zero or two. This proves equality of the paired character ranks, information not supplied by equivariance alone. The two-dimensional trivial block remains an unrestricted symmetric block for this argument and can have rank one; no evenness of the total middle ghost is asserted.

6. **Determinant and remaining dependency.** Each inverse block has determinant -a^2, and twelve such signs multiply to +1. Thus the displayed determinant factorization is correct in the chosen paired bases. Nondegeneracy is equivalent to all twelve pair scalars and the trivial-block determinant being nonzero. Neither the proof nor this review establishes those nonvanishing assertions or a numerical middle rank.

The local copies of PR514's proof and PR516's proof were checked for the actual orthogonal submodule, coisotropy, connecting-map definition, and character multiplicities used here. The claims about Gamma preserving the pairing and det(T) are explicit equivariant inputs, not consequences of symmetry alone. No selected actual HM/source instance, numerical rank computation, coefficient search, or large computation was performed.

The final provenance clarification was also reviewed: the proof now explicitly attributes Gamma-invariance to equivariant trace and Serre duality and cites PR464 item 4 at a pinned commit. This clarification does not change the chain-level argument or character calculation reviewed above.

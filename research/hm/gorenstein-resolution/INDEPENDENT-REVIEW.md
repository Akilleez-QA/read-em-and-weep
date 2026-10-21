# Independent mathematical review

Reviewed: `PROOF.md`, “A canonical obstruction map for the compressed quintic quotients.”

SHA-256: `ea5dc67c6c0cfcbf58f903d831a92f149d19748817b9b5200c898b5e45492ac6`.

## Verdict

The derivation is correct conditional on the pinned module, pairing, equivariance, and resolution inputs. The argument supplies necessary resolution constraints and intrinsic obstruction maps, not a determination of their ranks or a realization theorem for all allowed Betti numbers.

## Checks

1. **Dual grading.** For five polynomial variables, Ext^5_S(A,S)=A^vee(5). Twisting the reversed dual resolution by -10 produces D_5(A)=A^vee(-5). Thus beta_(i,j)(B)=beta_(5-i,10-j)(A), giving exactly the six displayed terms. In particular B is generated in degree three and Tor_1(B)_5=Tor_2(B)_4=Tor_0(B)_4=0.

2. **Generators of the extension.** A graded extension of two modules generated in degree three is itself generated in degree three, by lifting homogeneous generators of the quotient and adjoining those of the submodule. Applying this to T_w/I does not assume splitting. Lifting these generators to T_w shows that its additional generators over I are cubic. Hence T_w has no generators above degree four, and its quartic minimal-generator space is a quotient of that of I, with dimension at most fifteen.

3. **Resolution template.** The Hilbert function gives twenty cubic generators and the stated numerator. Minimality, absence of quadratic relations, and exactness imply that positive homological degree i has shifts at least i+2. Gorenstein self-duality with total shift ten then restricts the middle shifts to (4,5) and (5,6). Coefficient comparison gives precisely the two-parameter template in the proof; no further unlisted shift can occur.

4. **Actual middle map.** In internal degree five, the long exact sequence of 0→L→H→A→0 gives an isomorphism Tor_3(A)_5→Tor_2(L)_5 because both adjacent H terms vanish. It also gives Tor_3(L)_5=0 because Tor_4(A)_5=Tor_3(H)_5=0. The coisotropic inclusion B→L is an actual module map furnished by the pinned construction, not an identification inferred from matching Hilbert functions. Its long exact sequence therefore gives

   0→Tor_3(G)_5→Tor_2(B)_5→Tor_2(L)_5→Tor_2(G)_5→0.

   Both central spaces have dimension twenty-six. Thus b is both the kernel and cokernel dimension of the transported map Q_w, and b=26-rank(Q_w)≤26. Changing the auxiliary identification of B changes this presentation by an isomorphism and does not change these dimensions.

5. **Quartic criterion.** In internal degree four, the H sequence gives dimensions u+20-rho and 5+u-rho for Tor_2(L)_4 and Tor_1(L)_4 respectively. The B sequence gives a=5+u-rho-sigma. Both rank maps have source dimension twenty, so a≥max(0,u-35), while a≤min(15,5+u). The asserted composite to Tor_1(G)_4 is surjective; its kernel has dimension rho+sigma by the elementary dimension formula for the inverse image under a surjection. Hence the equality criterion for cubic generation and the conditional exclusion when u=40 are justified.

6. **Representation bounds.** The maps preserve the Heisenberg action. Internal degree four has nontrivial central character, so a, rho, and sigma are divisible by five. In degree five the Koszul term A_2⊗Λ^3T is two copies of the quotient regular representation, while the preceding term is the regular representation and has exactly its scalar boundary line as kernel by the pinned fourth-strand exclusion. Semisimplicity gives Tor_3(A)_5=Reg+1. Duality preserves this character multiset since inversion permutes the twenty-five quotient characters and the determinant character is trivial. The stated multiplicity bounds for the cokernel follow, without asserting nonvanishing of any block.

## Verification boundary

This is an independent mathematical review of the displayed derivation and its use of the pinned inputs, including the cyclic-duality and column-resolution proofs. It is not proof-assistant verification and does not independently establish every upstream theorem. No selected actual HM/source-instance evaluation, multiplication-matrix rank calculation, generic-rank assumption, or large computation is used. Neither cubic generation nor Q_w invertibility is established. No conclusion about higher-order lifting or algebraicity follows from this review.

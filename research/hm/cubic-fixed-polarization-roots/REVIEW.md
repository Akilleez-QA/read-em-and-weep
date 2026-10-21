# Independent mathematical review

Verdict: **PASS, conditional on the pinned inputs.** The tensor-power map with the central root fixed is an isomorphism of the stated set-valued Artin pair deformation functors. The relative root-lifting assertion, rigidified uniqueness, high-power Hilbert consequence, and compatible-system effectivity follow. No substantive correction is required.

This is an independent mathematical review, not proof-assistant verification or formal checking. It checks the new argument and its declared dependency interfaces, not the entire upstream HM chain.

Reviewed file: `PROOF.md` in this directory.

Exact reviewed SHA-256:

    4523a90f3b54841d2fc541252af50c0ba68e8b213d10d7f142eb308b349a513f

The hash was checked before reviewing and again before writing this review. The proof was not edited.

## 1. Dependency checks and scope

I inspected the pinned repository texts of PR611, PR614, PR615, PR628, PR630, and PR631 at the exact commits listed in the proof. Their stated interfaces agree with the uses here:

- PR611 supplies projectivity, integrality, the ample original polarization, and structure-sheaf cohomology.
- PR614 supplies H0(Theta_V)=0, the 576-dimensional abstract tangent space, and actual Artin unobstructedness by local gluing.
- PR615 supplies the pair tangent interpretation via the symbol sequence and the original-section dimensions.
- PR631 supplies the formally smooth high-power forgetful map and its n^2-1 relative tangent dimension.
- PR628 and PR630 supply polarized effectivity and finite original-polarized jet realization, respectively.

The complete pinned PR628, PR630, and PR631 texts were also byte-compared with the local proofs read during review. They match, with SHA-256 values respectively:

    PR628: 4016af2001bb7c9952519007c82b7d9d71a296e6042185215e01e61aba0a3818
    PR630: 213add76ebcd1ad9e790cf3cd267e7948faa3203889e73597b1a9c68bda70c7d
    PR631: 33b5f65e825d1105190b3471bbb435c325f1f9bef7f7fb61cad9bb475f799b99

The new root theorem does not depend on reconstructing the cubic image or evaluating a selected HM/source instance. Its essential general hypotheses are proper flat Artin deformations over C with H0(O_V)=C and a fixed central line bundle; H2(O_V)=0 is not needed when a lift of the power is prescribed.

## 2. Constants on arbitrary Artin deformations

The proof of A=H0(X_A,O_X_A) is valid and avoids assuming the desired base-change assertion.

For a point x of the special fiber, O_(X_A,x) is flat over A. Its quotient by the maximal ideal of A is nonzero, so the local-flat faithful-flat criterion applies. In particular A injects into this stalk. The canonical map from A to global sections followed by restriction to the stalk is that injection, proving that constants inject globally.

For a small quotient A->B with kernel J, flatness identifies the kernel sheaf with O_V tensor_C J. The H0 exact sequence gives

    dim_C H0(X_A,O_X_A)
        <= dim_C J + dim_C H0(X_B,O_X_B)
        = length_C A.

Induction starts at H0(V,O_V)=C. The already proved injection from A gives the reverse inequality. Thus the constants map is an isomorphism, naturally in A. No surjectivity of H0 restriction was assumed; it is obtained as a consequence. Properness supplies the usual finiteness, and the inductive inequality would suffice for this particular calculation as well.

Global units in the structure sheaf equal units in its global section ring. Hence they are A*, and restriction to any Artin quotient B is the usual surjection A*->B*.

## 3. Exact Picard kernel and obstruction cancellation

For X_A contained in a specified lift X' over A', the square-zero units sequence has additive kernel O_V tensor_C J. Its long exact sequence is the standard one in [Stacks 0C6Q](https://stacks.math.columbia.edu/tag/0C6Q).

Surjectivity of global units kills the preceding connecting map. Consequently

    ker(Pic(X')->Pic(X_A)) = H1(O_V) tensor_C J

is an actual canonical identification, not merely an action with an unspecified stabilizer. Multiplication by the positive integer m is invertible on this vector space.

The obstruction map to H2(O_V) tensor_C J is a homomorphism of abelian groups. Therefore

    delta(L_A^m)=m delta(L_A).

Existence of the prescribed M' makes the left side zero. Since m is invertible over C, delta(L_A)=0 even when H2(O_V) itself is nonzero. This establishes existence of an initial lift N on the specified abstract lift X', rather than on some substituted deformation.

The discrepancy M' tensor N^(-m) restricts to the trivial class. Its unique m-divisible preimage in the Picard kernel corrects N. If two corrected roots restrict to the same lower-order class, their ratio belongs to that kernel and has zero m-multiple, so is trivial. Factoring arbitrary Artin quotients into small extensions proves both the global bijection with fixed central restriction and the relative class statement.

The proof correctly distinguishes this prescribed-power argument from unrestricted lifting of a line bundle, for which the H2-vanishing input is used elsewhere.

## 4. Prescribed reduction isomorphisms and markings

The relative assertion also works with a specified power identification on the entire reduction X_A, not merely on V. Here is the explicit adjustment implicit in the proof.

After obtaining L' and choosing a reduction isomorphism L'|_(X_A)≅L_A, choose any power isomorphism beta':(L')^m≅M'. Comparing its reduction with the prescribed beta_A gives a global unit u in A*. Lift u to a unit u' in (A')* and multiply beta' by u' or its inverse, according to the comparison convention. Its reduction is then exactly beta_A. Thus there is no unaddressed compatibility obstruction for the prescribed reduction map. This uses the unit-surjectivity already established in Section 1; no additional root extraction is necessary for this adjustment.

For special-fiber markings, two identifications of a given restriction with L0 differ by a scalar in C*. Every such scalar extends to A*. Therefore forgetting the line-bundle marking is a bijection from marked isomorphism classes to unmarked classes having restriction isomorphic to L0. This does not discard automorphisms of the objects themselves.

Given M_A and its fixed central identification, the existence of a compatible beta:L_A^m≅M_A follows from the class theorem and the same scalar adjustment. For two triples (L_A,alpha,beta), first choose an isomorphism respecting alpha. Its discrepancy with beta is a unit in 1+m_A. The m-power map on 1+m_A is bijective, as follows from finite logarithm and exponential over C. Correcting by its unique m-th root gives an isomorphism of triples.

An automorphism of a triple is a unit u in 1+m_A with u^m=1, hence u=1. Thus the category of these root triples over the fixed scheme and fixed powered bundle is nonempty with a unique isomorphism between any two objects. Without beta, the scalar group 1+m_A remains. Without alpha, constant m-th roots of unity remain. These qualifications in the proof are correct.

## 5. Pair functors and formal etaleness

The fixed-scheme root result descends to the stated set-valued marked pair deformation functors.

Surjectivity is obtained on a representative X_A of the underlying scheme deformation. For injectivity, an isomorphism of powered marked pairs supplies an actual marked scheme isomorphism. Pullback along it turns the comparison into the fixed-scheme root problem. Central root uniqueness then gives the required isomorphism of original marked pairs. This argument does not depend on choosing unrelated identifications of scheme representatives.

Pullback preserves root triples, so uniqueness makes the inverse natural. Hence the power map is an isomorphism of functors, not only a tangent isomorphism. Its small-extension lifting fiber-product map is accordingly bijective, establishing formal etaleness in the asserted set-valued sense.

The additional H0(Theta_V)=0 observation is valid: at each small extension, the kernel of reduction on identity-reducing scheme automorphisms is H0(Theta_V) tensor_C J. Induction eliminates those automorphisms at all Artin orders. This is not a claim about all unmarked scheme automorphisms or generic-fiber automorphisms.

On tangent spaces, tensor power multiplies a first-order line-bundle cocycle by m and leaves the underlying scheme cocycle unchanged. Thus the diagram of symbol-sequence cohomology has left arrow m and right arrow the identity. Both pair tangent spaces have dimension 60+576=636, and the map is an isomorphism. No canonical splitting is required.

## 6. High-power Hilbert consequence

PR631's formally smooth map to the powered pair functor can be composed with the inverse functor isomorphism just proved. Formal smoothness and its relative tangent dimension n^2-1 are unchanged.

This genuinely solves the relative problem with a prescribed existing embedded deformation: power the prescribed original-polarized lift and apply PR631's lifting property over that pair. The resulting embedded lift reduces to the specified embedded object, not merely to some representative of its abstract deformation class.

The Hilbert source is the same germ, so its smoothness and dimension n^2+635 do not change. The original-pair-to-abstract map retains relative tangent dimension 60, and all 576 abstract tangent directions remain accessible.

None of this supplies lifts of the original ten degree-one sections. High-power H1-vanishing and original degree-one section obstruction are different conditions. The comparison with original P9 rigidity and PR630's at-most-nine generic-section conclusion is therefore consistent.

## 7. Compatible roots and effectivity

At each Artin order, the root-triple category over the prescribed (X_r,M_r) is nonempty and has unique comparison isomorphisms. Reduction of a root triple is a root triple at the lower order. The unique comparisons consequently satisfy all transitivity and compatibility conditions: any two candidate composites are isomorphisms between the same two triples and hence agree. This produces a compatible formal root system and its unique isomorphism class in the stated rigidified sense, rather than merely a collection of unrelated root classes.

Ampleness of L0 persists through nilpotent thickenings. The embedded X_r are proper, flat and of finite presentation, and their transitions are cartesian. These are exactly the needed hypotheses of [Stacks 0D4T](https://stacks.math.columbia.edu/tag/0D4T), with the index shifted if necessary. The theorem supplies a proper flat finitely presented X over C[[t]], an ample L, and compatible reductions. Properness and an ample line bundle over this Noetherian affine base give projectivity.

The compatible beta_r identify the formal completion of L^m with the already prescribed M_r. The claimed result is therefore effectivity of the recovered root pair with the correct powered formal system. The proof does not need a separate assertion about a root on an arbitrary finite-type algebraic curve.

Applying PR630 to the recovered system gives a smooth pointed curve realizing each chosen finite polarized jet. The curve may depend on the jet order. This is correctly distinguished from descent of the whole formal arc or a globally defined root on the original approximating curve.

## 8. Source record and boundaries

Repository texts checked:

- [PR611 pinned proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/12b28d33627cc0e8b283d142dc16439a51bb5e00/research/hm/cubic-branch-transversality/PROOF.md)
- [PR614 pinned proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/73fbf75838c91804ca637b5916d6aac217240958/research/hm/cubic-global-deformations/PROOF.md)
- [PR615 pinned proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/24bc9b741c287f8ac207bd9df4de4c07c50bea2f/research/hm/cubic-polarized-deformations/PROOF.md)
- [PR628 pinned proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/f08ff9c2760e4aef074cfe716b923d29d5e7ebe8/research/hm/cubic-effective-deformations/PROOF.md)
- [PR630 pinned proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/8024882d2129142fece5dbaf83b49e5f8e3817ca/research/hm/cubic-polarized-curve-deformations/PROOF.md)
- [PR631 pinned proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/4954b42e25592cf4b66a28d6a232fbe6b528f72e/research/hm/cubic-high-power-hilbert/PROOF.md)

The precise Stacks units and polarized-effectivity statements were opened and checked directly. No selected HM/source coefficients, point values, derivatives, matrices, or numerical ranks were evaluated. No large computation or external write occurred. Only this review file was created.

The conclusion remains conditional on the declared upstream inputs. It establishes fixed-central-root recovery in the formal neighborhood and its stated consequences, not global Picard-root existence or uniqueness, generic-fiber rigidity, recovery of the original ten sections, or resolution of the separate full-adjoint, prescribed-source, higher-lifting, or Weil-class algebraicity questions.

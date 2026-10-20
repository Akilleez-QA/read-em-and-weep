# Root mathematical review

Reviewed VERIFICATION.md SHA256: `7e120c24c1c04fb66d40c7c1b3e49079bac8a1962738e54d9757b231bd2d518c`.

Accepted conditional on the actual presentation and pairing inputs of PR482 and PR488. I independently checked the exterior presentation, balance and symmetry of the pairing, and the universal quadratic repair.

For a nonzero vector-valued quadratic relation, wedging with each basis vector extracts its two scalar coefficients. The exterior quadratic image is therefore nonzero. Its irreducible target makes it all of S_2, while absence of linear relations preserves the first two degrees. Thus the exterior square is exactly S/m^2 with its determinant line.

The map to the reversed dual scalar algebra is well-defined because its scalar annihilator kills H. Polynomial multiplication is balanced under the compatible pairing, and the even-degree trace pairing gives symmetry. The degree-zero map is an isomorphism, and levelness of the scalar algebra makes its reversed dual generated there. This proves the global surjection, not a global isomorphism.

The degree-two claim requires more than a dimension inequality. The proof supplies the missing fact: the actual multiplicity-one lower Clebsch–Gordan embedding is a nonzero scalar multiple of the displayed universal map. Its four symmetrized tensors are independent by their coefficient positions. Tensoring by A* therefore gives the full twenty-dimensional quadratic relation image. The remaining twenty-five-dimensional quotient maps isomorphically onto N_2. No selected HM coefficients are used in this universal two-variable identity.

In characteristic zero the swap idempotents split the tensor square into symmetric and exterior parts. The pairing kills precisely the entire exterior summand together with its remaining symmetric kernel, giving the stated kernel decomposition and low-degree dimensions. The higher symmetric kernel remains undetermined. The complete H presentation bounds the degrees generating the symmetric-square relations, but does not identify additional relations of N.

This is mathematical review, not formal proof-assistant verification. It proves neither a global symmetric-square identification nor a choice of the r/s parameters, selected-form membership, fixed-pair vanishing, higher-order lifting, or algebraicity.

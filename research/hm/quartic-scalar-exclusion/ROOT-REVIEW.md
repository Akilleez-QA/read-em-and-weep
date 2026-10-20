# Root mathematical review

Proof reviewed: SHA256 `4de5f90b0ed95a5c70cb9916b7628aacb4b74fe39e7553821a75e68dd291da14`.

Accepted conditional on the pinned actual cohomology and module inputs. I independently checked the following deductions.

- The actual isomorphism T tensor H_0 -> H_1 identifies the internal-degree-two second Koszul differential with alternation. This map is injective; no assumption that H is generated in every degree is required for Tor_2(H,k)_2=0.
- The Serre pairing has shift five. Combining it with the length-five polynomial Koszul complex pairs internal degrees summing to ten and homological degrees summing to five. Thus the vanishing transfers to Tor_3(H,k)_8, with an irrelevant determinant factor.
- For the coordinate Koszul complex tensored with B(3), the q=1 row is K in internal degree four and the q=2 row is H in internal degree eight. The target position (-1,1) has only the displayed possible incoming differentials. The d_3 and d_4 sources vanish already on the first page from H^3(B(-1)) and H^4(B(-2)), respectively. Serre duality gives the latter as H^0(B(-3))*, which vanishes by stability. No outgoing differential can remain inside the complex. Exactness of the sheaf Koszul complex therefore forces the target to vanish.
- PR480 identifies this target with the cokernel of the actual quartic connecting map. Its three multiplicity-one matching channels must consequently be nonzero, and its unmatched A tensor W' summand is exactly the kernel. This does not give numerical scalar values or identify the separate fixed-pair Tor correction.
- Combining with PR480's all-degree upper bound removes every quartic generator, not just one chosen quartic relation. Graded Nakayama gives the resulting complete degree-at-most-three presentation, with chosen lifts and non-direct sums in degrees five and six.

The remaining cubic alternative is unchanged. This is mathematical verification of the new argument, not formal proof-assistant checking or independent recertification of all antecedent HM results. No selected forms, source instances, numerical ranks or coefficient searches were evaluated.

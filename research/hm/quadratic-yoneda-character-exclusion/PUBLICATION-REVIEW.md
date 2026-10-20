# Independent review of the non-invariant character exclusion

Reviewed the six-entry frozen payload SHA256 `ccf7757bca021470e619f7232e0a687cef6ed4bdce9a2665197f292647dc2647`.

PASS under the exact complex HM presentation and primary cohomology inputs pinned in DEPENDENCIES.md. This is mathematical review, not new execution of source calculations.

The Kunneth cohomology calculation for B_S has exactly one intermediate group at twist zero when 1≤|S|≤3. The Euler lifting argument uses the vanishing of every positive-degree cohomology group of B_S(i) for 1≤i≤r. Complementary finite duality supplies a retraction; it does not assume self-duality for singleton and triple characters. Removing the Omega summand and applying Horrocks leaves line bundles with shifts at most minus two.

The two Euler sequences then kill pair and triple character Ext1 using precisely H0(F(t))=0 for negative t and H1(F(t))=0 for t≤−2. The full character is also killed by its line-bundle splitting. The singleton stabilizer acts trivially on the unique cohomology generator, with no permutation sign from the three degree-zero factors. Averaging the lift therefore proves the induced permutation representation without assuming a multiplicative equivariant splitting.

Equal order-two characters are the only invariant quadratic source pairs. The singleton diagonal summands are copies of the four-point permutation representation and have no [22] constituent. The invariant summand is killed by tangent exhaustion of the smooth family and polarization. The sign-valued Serre pairing pairs a full-deck [22] class only with the missing invariant [22] target component.

The same character argument treats ordered products of non-invariant inputs; ordered invariant products require the separately pinned PR179 result. The README correctly records that later stronger result rather than leaving the manuscript's historical question as a current frontier. Neither statement computes an actual residual value or proves higher-order or algebraic liftability.

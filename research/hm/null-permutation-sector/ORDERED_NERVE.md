# A genuine alternating cochain representative with no highest Omega symbol

This is a mathematical construction for the two-dimensional full-S4-sign projection. It does not assert that this projection vanishes and does not implement a new coefficient provider.

## 1. Use the full ordered nerve before sorting

Let U_v be the actual source cover, with vertices consisting of a carrier and legal mask. Work first in its full ordered Cech nerve: an n-cochain has a value on every ordered (n+1)-tuple, allowing repetitions. Use the usual alternating sum of face restrictions, including the established bundle transport for the first face. Do not identify this with a pruned tensor-cover row or with a provider that first sorts and then sets repeated keys to zero.

The raw physical formulas define an ordered-nerve first lift and obstruction by evaluating them on the tuple in the supplied order. The first-order scalar identity is the same unsymmetrized connection/transgression identity on every tuple, with the complete gerbe representative. Its proof is a rational identity in the connection and transition data, so it also specializes to repeated labels wherever defined. The universal obstruction-closure calculation from these first-order identities and the ambient second-order deformation likewise holds before sorting. In particular no new order-change equality of historically stored values is assumed.

Call the resulting tracefree obstruction cochain R_bar. Restricting it to strictly increasing tuples gives exactly the fresh raw representative used in the accepted class comparison. The standard ordered-nerve and ordered-cover Cech resolutions compute the same sheaf cohomology; restriction to increasing tuples is a chain map and the usual degeneracy/comparison homotopies give the identification. The repeated-index values must not be discarded before this argument.

## 2. Average the genuine geometric action

Factor permutations act on the ordered nerve by permuting coordinates and each legal-mask label, preserving the positions of vertices in the tuple. Carrier labels are unchanged because their coordinates are elementary-symmetric coefficients. The ordinary tensor-product line frames and their physical source primitives have the established geometric permutation transport. This gives the genuine chain action rho(g) and commutes with the Cech differential.

Over Q define

    R_alt_bar=(1/24) sum_(g in S4) sign(g) rho(g) R_bar.

It is closed, and its class is e_sign[R]. Only after this full average do we restrict to the chosen increasing order. This supplies a representative of the two-dimensional projection identified in PROOF.md. The full24-term average avoids assuming that raw gerbe representatives or first lifts are strictly D8-eigen cochains. The shorter three-coset formula is asserted at class level under the authenticated membership hypothesis; it is not substituted blindly for this chain construction.

## 3. The highest symbol cancels on every ordered tuple

On an ordered tuple, the physical transition matrices are natural under simultaneous factor/mask permutation: after pullback, the matrices are those for the original tuple, and only the four derivation labels are permuted. There is no vertex-position sorting at this step. Hence the full alternating sum of their highest second-jet symbols is the alternating sum over the four derivative labels in the same H/J arrays.

The symbol is alternating within each pair and symmetric under exchanging the pairs. The24-term sum is therefore eight times

    Omega_(01,23)-Omega_(02,13)+Omega_(03,12),

which is identically zero by the explicit mixed-Hessian cancellation in PROOF.md. No actual source coefficient and no pointwise symmetry assertion are used. Therefore the ordered-nerve representative R_alt_bar contains no contribution from that highest Omega term.

The entire rest of each transformed R_bar is still present: Q2, Q4, both complementary E terms, the unsymmetrized scalar transgression, and every original gerbe correction. In particular scalar representative changes under pair reversals are not discarded. They are included automatically by applying the genuine action to the WHOLE cochain before averaging.

## 4. Scope of the construction

This isolates a representative without the bilinear second-jet Omega term for the full alternating projection. It can still contain second derivatives through Q2 and E. The construction is conditional on the same published raw-source closure and physical permutation naturality used by the global sector theorem. It does not prove a primitive for that representative, compute either of its two global coordinates, or affect the remaining30 coordinates.

No existing alternating total provider is asserted to implement the ordered-nerve source. A future source-faithful compiler must retain the supplied order until after the full geometric average, and must authenticate its comparison with the admitted fresh representative. No current execution allowance is enlarged, no historical table is reused, and no runtime or owner-count reduction is claimed. The separate one-point Omega attempt has already been consumed and is not repeated here.

The ordered-source closure input is the universal quadruple-overlap associativity calculation in [closure-and-characters, section1](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-residual-attribution/closure-and-characters.md). The first-order transgression is the corresponding pinned first-order-source formula. The symbol cancellation does not remove terms merely because they also contain a second derivative.

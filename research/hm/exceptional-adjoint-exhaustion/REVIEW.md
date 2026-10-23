# Independent mathematical review

Date: 2026-10-23.

Verdict: PASS. The exceptional double-plane argument proves the claimed ordinary-square exhaustion and, using the specified actual HM inputs, the absence of torsion in the opposite-pencil cokernel. This is an independent mathematical review, not proof-assistant verification.

## Reviewed version and scope

Reviewed document: PROOF.md, SHA256 873d031bb3e936438875225b7d8e5ea31ef94e0b063489341d02a3d379f19f2c.

The review covers the entire proof, including the final fiberwise vertex-kernel corollary. It checks the new geometric argument directly and checks that the five pinned input documents supply the interfaces used. It does not independently reprove every earlier HM theorem on which those documents depend. No selected actual HM/source point, coefficient, parameter, matrix, derivative, or instance rank was evaluated.

## Source verification

The five source copies were read and their byte counts, SHA256 hashes, and Git blob hashes verified against INPUTS.json:

- [Actual opposite-pencil reduction and vertex comparison](https://github.com/Akilleez-QA/read-em-and-weep/blob/8c9847612b5f575b987cec9c62b72b099d745e44/research/hm/reduced-opposite-pencil/PROOF.md).
- [All-parameter section spaces and equivariant square identification](https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/HYPERPLANE-SQUARE-SURVIVORS.md).
- [Actual factor-cover geometry and twelve double-plane parameters](https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/THREE-LINE-FACTOR-COVER-GEOMETRY.md).
- [Checked classification application to the particular bundle](https://github.com/Akilleez-QA/read-em-and-weep/blob/35fc96bebf9c771a4de481c753bb527e510cd8c1/research/hm/order-four-quadratic-load/REDUCED-DETERMINANT-THREE-CONIC-PENCIL.md).
- [Good-parameter exhaustion, ordinary-square sequence, and length-two lemma](https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/HYPERPLANE-ADJOINT-EXHAUSTION-AND-SIX-TO-TEN.md).

The [official Bănică–Manolache 1983 preprint](https://www.imar.ro/~increst/1983/19_1983.pdf) was also independently rendered and visually inspected, not merely read through OCR. Its SHA256 is 1d0cf269d126050779bce67e41a5643b1789bc555378064bd89241bebe71c151. The checked locations are:

- Printed page 1 / PDF page 7: the exhaustive five-case list for zero curves when H0(E(1))=0.
- Printed page 5 / PDF page 11: the conic-plus-degree-four-double case, explicitly including degenerate conics, the trivial conormal in the reduced degenerate case, and the following Ferrand ideal containment.
- Printed page 9 / PDF page 15: the two exact sequences defining tripling, which give multiplicity three times the base multiplicity on every support component.

The notation in the general Ferrand lemma uses a dualizing-twisted line-bundle parameter. It is not confused with the conormal quotient in this proof: the preceding classification discussion identifies the latter quotient, and the dualizing identity independently gives I_Q'/I_Y = O_Q' after Q' is known to be a reduced plane conic.

## Detailed mathematical checks

### 1. Classification and invariant supports

Regularity follows from H0(E(-1))=0. The unique-cubic conclusion follows from the regular-section exact sequence and h0(E)=2. Nonzero vertex evaluation allows a general section to avoid the vertex; the plane restriction theorem prevents a curve component in R.

On the simple determinant plane away from the other plane, an invertible evaluation entry reduces the zero-section equations to a local determinant equation and a kernel-ratio equation. The kernel map cannot be constant without giving a divisorial zero of a section. Generic smoothness therefore supplies a multiplicity-one component for a general member. This excludes the wholly doubled and tripled classification types, including reducible or nonreduced bases; it is not an unsupported claim that the entire determinant is reduced.

Three disjoint conics are excluded by their product cubic and uniqueness, not by assuming that every reducible conic contained in a union of two planes lies in one of those planes. For the remaining type C0=Q disjoint-union Y, the same cubic uniqueness identifies Q's plane as the simple plane and the Ferrand base plane as the repeated plane.

The distinct degrees of the two connected components make Q and Y invariant. A nonreduced conic base would have an invariant supporting line, either in R or through the vertex. This excludes double-line bases without assuming that a chosen intermediate nonreduced structure is canonical. Reduced conics may still be pairs of meeting lines, and the remainder of the proof handles those cases.

### 2. Ferrand presentation and parity obstruction

The quotient conormal is trivial, and the even/odd alternatives for its equivariant structure are exhaustive because the reduced connected conic has only constant global units. The odd alternative makes both coefficient sections vanish on Q' intersect R, contradicting the quotient's surjectivity. Thus a and b can be lifted with the stated positive/even parities.

The four-generator description is correctly used as an equality of ideal sheaves. The six-dimensional cubic space is not inferred solely from exhibited generators: the Koszul sequence and H1(O_Q')=0 prove completeness. Its parity dimensions are (5,1).

The five-dimensional even restriction argument correctly excludes a in span(h,h'). If the kernel has dimension at least two, cubic uniqueness fails immediately. Otherwise its four-dimensional image is all h' times the even plane quadratics and contains h'q, again giving an independent cubic through C0. This is the essential additional restriction; forgetting parity would invalidate this dimension argument.

### 3. Ordinary-square restrictions and controlled division

The length-two complete-intersection square lemma applies to tangent and nonreduced intersection schemes. Its resolution proves both the unique degree-two square and the absence of degree-one sections, with ordinary sheaf squares throughout.

The first plane restriction forces F6|P' to be a scalar multiple of q'^2 a^2. Division by q'^2 near Z=Q intersect P' is legitimate because Z is disjoint from Q'. A nonzero scalar would force a|P' proportional to h|P', contradicting the parity obstruction. Hence h' divides F6.

At each generic point of Q', a is a unit: otherwise its vanishing on a whole projective component would force a common zero with b. In these local rings (h',g) is a regular sequence, so the two colon identities in the proof are valid. The first gives double divisibility by every reduced component of q' in G5|P'. The remaining linear factor vanishes in the square ideal of Z and is therefore zero. Hence h'^2 divides F6.

Both cancellations preserve membership in I_Q^2 because powers of the complete-intersection ideal of Q have no embedded associated primes, and h' contains no component of Q. No unsupported cancellation through the double curve is made.

### 4. Global membership and final cubic

The second colon identity establishes membership of K4 in the full ideal I_Y at every generic associated prime, including the generic nilpotent structure, not merely vanishing on Y_red. Unmixedness of O_Y then globalizes this first-power membership. The proof does not identify an ordinary square with a symbolic square or globalize square membership by reducedness.

Restricting K4 to Q's plane gives c q^2. Its vanishing on the nonempty intersection with Q' forces c=0. After division by h, the final cubic lies generically in both I_Q and I_Y; the unmixed quotients globalize these memberships. Unique-cubic dimensionality then proves H0(I_C0^2(6))=C S^2.

### 5. Actual consequences and vertex corollary

The symmetric-square exact sequence has the ordinary ideal square on the right. The square of the second section lifts its nonzero generator S^2, so h0(Sym2 E)=2+1=3 without assuming any H1(E) vanishing. Together with the good-parameter theorem, this proves exhaustion at every parameter, of both parities.

Only after that independent exhaustion does the actual base-change sequence imply Tor1(C,k(t))=0 everywhere. Over the parameter line's local DVRs, C is therefore locally free. Tensoring the final reduced presentation gives injectivity of its 26-to-31 fiber maps.

For the added vertex statement, the actual surjective evaluation Y=W O(-3) -> O(-2) has kernel M=O(-4). Its symmetric-square kernel is M tensor Y=W O(-7). Exhaustion makes this exactly the full space of vertex-vanishing adjoints on every fiber, of dimension two, with no extra exceptional Tor classes. The two-dimensional kernel concerns the vertex-restricted 40-to-43 pencil; the final 26-to-31 pencil has zero fiber kernel. The image of evaluation is the O(-4) vertex channel and not the O(10) channel. No extension splitting is inferred.

## Bounded verification and conclusion

Both python verify.py and python -O verify.py passed. The checks cover fixed abstract parity dimensions, the length-two square Hilbert calculation, universal two-parameter monomial colon identities, degree bookkeeping, and all five supplied input hashes. They are consistency checks, not substitutes for the geometric proof above.

No unresolved gap was found in the new argument. Subject to the explicitly pinned actual HM input theorems, the stated torsion-free result and vertex corollary follow. The proof does not determine the splitting type of C, evaluate the remaining mixed maps, exclude a catalogue source, decrement a source frontier, or prove algebraicity of the original construction.

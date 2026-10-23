# Independent review: finite-jet bound for dual Gauss kernels

## Verdict and exact scope

Accepted as a written mathematical theorem over C, relative to the explicitly imported application inputs. For a saturated inclusion E in H O on P1, with E(m) globally generated, the actual m-th successive Gauss kernel of E-perp equals the constant annihilator of the constant span of E. In particular it is zero when E spans H. This is not proof-assistant verification.

The D-source application gives S_8=0 and last nonzero index at most 7. This review does not exclude original records 32, 50 or 52, assert full profile coverage, or establish the original proof repair. Those require separate arguments. No actual-instance coefficients, jets, points, parameters, matrices or ranks were evaluated.

## Frozen reviewed artifacts

SHA256 values:

- PROOF.md: 43d63c033c75942d3fc1e5346a34ea239b9b41c9b9f67148738dc8ae88c9fcb7
- verify.py: c0ed298640b02558bdcef0b35e29bc001562b18e03ac703fd8d07d666ea3005f
- INPUTS.json: eb81aaba40de4e59c5894c90f1be78a017ccca4c79070a95b78bfc5bcfc64081
- RESULT.json: a26624ecafd068ec0ce4790f558e15bb0ea2effa564baf501520dad95a76ea34
- REPRODUCE.md: 5cedc23fd9276881b3763e45d45364ea80d9d8e9f6309625996bd28c9309c601

## Mathematical checks

1. Saturation is justified at every stage: the second fundamental form has torsion-free image on the smooth curve, so its kernel quotient is locally free; composing with the earlier ambient quotient preserves local freeness.
2. A Birkhoff summand O(-a_i) maps to the trivial ambient by homogeneous degree-a_i coordinates. Its standard affine frame therefore has polynomial image of degree at most a_i. The splitting is used only to choose these frames and is not assumed horizontal.
3. The local identity S_j=annihilator of all derivatives D^a p_i for a<=j is correct in both directions. The recursion uses s and Ds in S_(j-1), not an unproved derivative-preservation of S_j. Differentiating the vanishing pairing produces the negative term with the correct indexing.
4. The identity concerns arbitrary regular local sections. It does not identify an unsaturated coherent image with a subbundle. Frame and coordinate changes preserve the jet-generated sheaf, and its identification with the intrinsic kernel makes it coordinate independent.
5. Taylor inversion is exact in characteristic zero. The joint polynomial coefficients span exactly the smallest constant ambient subspace R, including when individual coefficient systems are partial. Derivatives through m generate R O on the affine chart without selecting a parameter value.
6. The constant R-perp O lies in every kernel. The quotient S_m/(R-perp O) injects into the constant quotient bundle and vanishes on a dense open, hence is zero globally. No gap at infinity or ramification remains.
7. The case m=0 is included. The sharp rational-normal example is a globally saturated inclusion; its displayed nonzero local dual section proves S_(m-1) is nonzero and the m-th derivative pairs to m!, so there is no off-by-one error.
8. Spanning is essential for the zero conclusion, not for the stronger exact stable-remainder formula. For example a constant line in a two-dimensional constant bundle leaves a nonzero constant dual kernel forever. Characteristic zero is likewise essential: the saturated spanning Frobenius line (1,t^p) in characteristic p is horizontal for ordinary derivatives.
9. The alternative partial-apolar explanation is compatible with the direct proof: successive derivatives of a line in S_m lie in S; dualizing a possibly partial coefficient quotient is legitimate. No completeness is assumed. The theorem does not depend on this alternative paragraph.

## Source authentication and executable evidence

All four complete immutable source files were freshly fetched independently from GitHub, read in full, and compared byte-for-byte with retained inputs. Byte lengths, SHA256 digests, and independently computed Git blob IDs match both the manifest and fetched blob IDs. The exact records and URLs are in independent-result.json. The actual-splitting original explicitly states the spanning property; the four-source original supplies the D splitting; the strict-top source confirms kernel conventions; PR1145 provides the referenced partial-quotient argument. These are imported written results, not recursively re-proved dependencies.

The author's verifier ran normally and with Python -O. Both complete outputs equal the retained RESULT.json byte-for-byte. The independent checker separately authenticates fresh source bytes and checks both sides of the formal divided-Taylor inverse through degree 24, the formal triangular Wronskian nonvanishing through degree 24, and the characteristic-p edge. Its normal and optimized complete outputs also agree. These finite regression tests support, and do not replace, the all-degree proof in Sections 2-4.

No mathematical correction is required for the reviewed frozen theorem. Any later change to the hashes above requires a new review of that change.

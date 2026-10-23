# Independent review: marked-doublet derivative rank and twelve-point defect

## Verdict and exact scope

**PASS as a conditional equivariant bundle-map theorem over C**, dependent on the pinned actual-source inputs. No correction is required to the reviewed proof. This is a mathematical review supported by exact tests, not Lean verification, a new actual-source instance, a profile exclusion, or completion of the original proof repair.

The reviewed `PROOF.md` has SHA256 `e374e3cb656f64f408832557369e9d5b1cf2bc34efc612820641b99dd81cf4e7`. The exact verifier, manifest and result bindings appear in `RESULT.json`. The complete three retained input proofs were read and independently fetched at their immutable public commits. `AUTHENTICATED.json` contains those public responses, including URLs and Git blob IDs. Its content is public mathematics only. Exact byte equality against the packet inputs is tested by the independent checker.

## Mathematical findings

1. **The actual restriction is legitimate without a horizontal projector.** PR1127 supplies the canonical saturated marked L = W' O(-3) inside E. PR1129, not an abstract pencil replacement, supplies the actual nonzero map to A_q = E/ker(beta_E). Its coefficient injection implies nonvanishing on W'; no rank-eight fiber injection is inferred. The reviewed argument neither commutes the canonical retraction with beta_E nor identifies saturation in A_q with saturation in the original Q(-2).

2. **Rank-one saturation has degree at least four.** Saturation is intrinsic and equivariant. Every equivariant structure on an ordinary O(e) differs from its standard structure by a character; perfectness of SL2(F5) removes that ambiguity. A nonzero map W' O(-3) to this line forces W' in Sym^(e+3) W. The verified absence through degree six therefore gives e >= 4. Inclusion in A gives e <= its largest ordinary splitting degree. Thus largest degree at most three forces generic rank two. This is not a fiberwise assertion.

3. **The rank-one endpoint is a valid abstract sharpness example.** The W' constituent of Sym^7 W gives a two-section system. Its common-zero divisor is invariant of degree at most seven, so the orbit bound proves basepoint-freeness, rather than assuming it. Consequently W' O(-3) surjects onto O(4) with kernel O(-10). No actual Gauss realization is claimed.

4. **The invariant orbit argument proves reducedness, not just a total degree.** A finite point stabilizer in PGL2(C) is cyclic. The possible A5 cyclic orders give orbit sizes 60,30,20,12. Its six order-five subgroups fix two points each, with no overlap because stabilizers are cyclic. Those twelve points form one orbit. A degree-twelve invariant effective divisor must therefore be this orbit with each multiplicity exactly one.

5. **The determinant defect is measured in the correct saturation.** For generic rank two, L maps injectively as a sheaf into its rank-two saturation B, with torsion cokernel. The determinant section has degree deg(B)+6. Its invariant effective zero divisor is either empty or has degree at least twelve. The exterior-square inclusion gives deg(B) <= a1+a2. Thus a1+a2 <= 5 forces defect zero and local freeness of A/f(L). The proof correctly separates this assertion from generic rank two and notes the impossible range a1+a2 < -6.

6. **The specific target and its every-point ranks follow.** For A = O(-8) + W O(3), degree kills the negative component. The exact identity W tensor Sym^6 W = W' + 2T gives one nonzero channel up to scale. Generic rank two follows from item 2, not from that Hom dimension. The determinant then has degree twelve and is nonzero; item 4 proves its zero divisor reduced. At each of the twelve points, residue rank zero would force determinant valuation at least two. Thus the fiber ranks are exactly two off the orbit and one on it. The local Smith type is (1,t), giving length-one torsion at each orbit point.

7. **Image and full cokernel are distinguished correctly.** The coherent image is isomorphic to L, not to its saturation W O(3). The positive-block cokernel alone has length twelve. Under the stipulated equivariant direct splitting, the full cokernel is O(-8) plus that torsion sheaf. The proof does not silently trivialize equivariant torsion-fiber characters. The example has top-two sum six and defect twelve, so it proves only abstract sharpness of the threshold five.

## Reproduction and independent controls

Run the supplied checker with the packet directory as an explicit argument:

    python independent_check.py ..
    python -O independent_check.py ../marked-doublet-ramification

The default argument is the parent packet directory. No absolute paths are embedded. Both outputs are byte-identical to this directory's `RESULT.json`.

The checker verifies all four packet hashes, the three independently fetched input originals, and execution of the author's 151 tests in normal and optimized Python with identical recorded output. Its additional controls do not import the author's representation code:

- Construct all 120 matrices in SL2(F5) and compute the subgroup generated by all commutators. It has order 120, independently supporting the no-character assertion.
- Exhaust all 6,561 two-by-two matrices over F3[t]/(t^2). All 1,728 matrices with determinant of exact order one have residue rank one. This is only a bounded universal local-algebra control. The characteristic-zero DVR proof in item 6 remains the proof of the assertion used in the theorem.

No selected HM source, parameter, point, tensor, jet or actual-instance rank is evaluated. No historical source enumeration or stopped experiment is rerun. Deeper input dependencies are not recursively re-proved by this review. The packet establishes no occurrence of its conditional target, no additional live profile cut, no full coverage theorem and no complete repair.

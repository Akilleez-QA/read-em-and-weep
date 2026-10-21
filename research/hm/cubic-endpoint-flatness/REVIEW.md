# Independent review: endpoint dual numbers and the inverse-image curve

Verdict: PASS, conditional on the predecessor inputs stated in the proof. This is an independent mathematical review, not formal proof-assistant verification.

## Reviewed artifact and dependency boundary

- Reviewed artifact: `PROOF.md` in this directory.
- Reviewed artifact SHA256: `f174a196d6a2a4f97aaccb38d154b55aec8cb23a50707112dc55bd3537b88b95`.
- Direct pinned input: PR605, commit `9df4c45d0c76ded1075a0652707bdbcd1f424189`, `research/hm/cubic-exceptional-fibers/PROOF.md`.
- Predecessor pinned input: PR604, commit `a4a0b5ed6e9dd0c18e3a263d1b3f8d9a49f2bf8d`, `research/hm/cubic-embedding-locus/PROOF.md`.
- The supplied local copies of both predecessor proofs were read. Their SHA256 values were respectively `a0eb2c290bcfa9f9eece55cf64f1fbab42fb2e094fb93864e70c2e801954101e` and `75afda202609d76b2780bfeff6824c6780457bf39a6b21a9306bdd9430b17601`.

This review checks the new deductions from those supplied inputs. It does not independently authenticate the remote commit contents or re-audit the earlier primary/modular dictionary and its source chain. No selected HM coefficients, point evaluations, numerical ranks, computer algebra, or external publication were used.

## Checks

1. **Scheme-theoretic incidence is sufficient.** The global bilinear identity can be restricted to a nonreduced scheme fiber. On projective affine charts, the target coordinates become constants, giving the exact equations `B(y) pi=0`. Since the fixed linear kernel is the line `ell`, these generate its pulled-back ideal. In the endpoint blowup chart they therefore imply `t u_i=0`, without replacing scheme containment by support containment.

2. **Both required cotangent classes are nonzero.** The one-dimensional tangent kernel cannot lie in the exceptional tangent space, because the exceptional restriction is immersive. It cannot lie in the strict-transform line tangent space either, because that restriction is immersive. Hence the class of `t` and at least one class of `u_i` are nonzero in the one-dimensional fiber cotangent space. Nakayama makes `t` a generator of the maximal ideal, while `u_i=t h` has unit `h`. Thus `t^2=0`, and the nonzero cotangent class excludes the reduced length-one algebra. The local fiber is exactly the dual numbers.

3. **Flatness does not assume reducedness or generic flatness in advance.** The generic fiber algebra surjects onto the product of three copies of the target function field, using the three known reduced support components. Its dimension is therefore at least three. A finite module over a closed-point DVR has rank at most its fiber dimension, which is three by the endpoint calculation and predecessor. The generic rank is exactly three. The same DVR decomposition then excludes every torsion summand, so the finite algebra is locally free of rank three.

4. **Reducedness follows rigorously.** The generic algebra's dimension-three surjection onto the product of three fields is an isomorphism. Local freeness makes the algebra inject into its generic algebra. Any nilpotent must consequently vanish, proving that the full inverse-image scheme is the known reduced chain.

5. **The gluing algebra and module splitting are exact.** At either junction, the two component tangent lines have zero intersection. Equivalently, their ideals sum to the maximal ideal by Nakayama, so their scheme-theoretic intersection is the reduced point. The closed-union exact sequence yields precisely the two equality-of-value conditions in the asserted tuple algebra. The displayed change of module coordinates gives `O_Q` plus the two respective point ideals. The proof correctly does not claim a product decomposition as algebras.

6. **The completed curve-map normal form is correct.** The two meeting sheets have completed local algebra consisting of pairs of power series with equal constants. Sending `s` to `(s,s)` and `u` to `(s,0)` identifies it with `C[[s,u]]/(u(u-s))`. Setting `v=s-u` gives the node equation `uv=0`, with target parameter `s=u+v`. The opposite sheet remains separate and unramified.

7. **The trace discriminant has the asserted exact orders.** In the junction factor's basis `1,u`, the relation `u^2=s u` gives trace pairing matrix `[[2,s],[s,s^2]]`, whose determinant is `s^2`. The separate rank-one factor contributes determinant one, with zero cross pairings between the factors. Completion preserves the discriminant's valuation at the target DVR, so the order is exactly two at each endpoint. Away from the two endpoints, the algebra is the split product of three copies of the base ring and the trace determinant is a unit. Thus the complete trace-discriminant divisor is precisely `2alpha+2beta`; its degree also matches the determinant-line calculation.

## Scope and conclusion

The proof resolves the previously undetermined exponent as `e=2`, proves constant fiber length three and finite flatness over every conditional bad line, identifies the full inverse-image curve as reduced, and determines its finite algebra, completed curve-map structure, and trace-discriminant divisor. Every asserted conclusion follows from the stated inputs. No mathematical gap or necessary revision was found.

The hypothesis `r=2` remains conditional. Neither the value of `r` nor the ambient fourfold image's analytic singularity type follows from this review. In particular, the nodal normal form is only for the inverse-image curve and its finite map to the bad line.

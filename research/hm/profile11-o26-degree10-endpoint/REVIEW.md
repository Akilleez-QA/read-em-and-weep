# Independent exact-version review

## Verdict

**PASS** for the stated endpoint-intersection theorem, relative to its pinned structural inputs. The proof excludes containment of the actual degree-ten constant block in the forward endpoint and establishes the two asserted sheaf intersections. It does not exclude the surviving degree-twenty-divisor stratum.

The reviewed artifact is `PROOF.md`, with SHA-256

```
2a19b00a8fa6f9472de3a3ef10c0034f96e0c17f8aca271e0660e5712d8832df
```

This verdict binds that exact version. The proof was not modified during the review.

## Dependency and scope check

The original conventions and source data are pinned to commit `db51525015bb7c5e825833d550d08dedf6f6ea96` in `Akilleez-QA/read-em-and-weep`, under `research/hm/order-four-quadratic-load/`, as listed in the proof. In particular, the argument uses saturated actual Gauss bundles, the original constant connection, the actual zero-defect quotient, and the ordinary splitting bound supplied by `H0(E(1))=0`.

The immediate structural dependency is [PR813's proof at its immutable commit](https://github.com/Akilleez-QA/read-em-and-weep/blob/3f99ecf539a3a3da61743df0dff409e54270c865/research/hm/profile11-o26-divisor-reduction/PROOF.md). Its published content was read independently and its Git blob identity matched the reviewed dependency copy:

```
Git blob: c5237be81f13d72776ba117548038f4c2c11b6b4
SHA-256: 16d4c27256932b57b3395edd39ec7118e37e7b00757a4d969a7e17b0b2c84bad
```

The inputs actually imported from that dependency are the matching E6/E13 source types, the reduced invariant orbit of degree twenty, the exact top image and its first forward image, and the actual identities

```
F = U_8^10,
F^+ = U_9^10,
F^{++} = C O,
C = Sym10 W.
```

These are embedded osculating identities, not merely compatible abstract bundle splittings. The new proof does not import an interior-stage intersection assertion or a general projection-saturation assertion.

## Exact intersection and image audit

1. **The initial dichotomy is sheaf-theoretic.** The intersection `E^+ intersect C O` is saturated in `C O`, because its quotient is the image of `C O` in the locally free quotient `(H O)/E^+` and is therefore torsion-free. It contains the saturated rank-ten bundle `F^+`. Its rank is ten or eleven. At rank ten, equality with `F^+` follows from saturation; at rank eleven, equality with `C O` follows from saturation. No finite-length difference is silently discarded.

2. **The two possible positive images are exhaustive.** Under the contradictory containment `C O subset E^+`, all maps from `C O` to the negative bundle `L(2)` vanish. Its image is a line subsheaf of `O(28)` containing `f20 O(8)`. Consequently the image's effective zero divisor is a subdivisor of the single reduced degree-twenty orbit. Equivariance makes it invariant, so it is either the whole orbit or empty. Thus the image is exactly `f20 O(8)` or `O(28)` as a subsheaf, not merely a line of one of those degrees.

3. **The first image is impossible.** A surjection `C O -> f20 O(8)` has a rank-ten kernel of degree minus eight. That kernel embeds in `E`. The injection on global sections after twisting by one gives `H0(N(1))=0`, so every ordinary splitting degree of the kernel is at most minus two. Its degree would therefore be at most minus twenty. This contradicts degree minus eight.

4. **The remaining kernel quotient is exact.** The remaining image is the full positive `O(28)`. Thus `N=E intersect C O` has rank ten and degree minus twenty-eight. Quotienting `F subset N subset C O` gives an actual surjection

   ```
   (C O)/F = W O(9) -> O(28).
   ```

   Its kernel `N/F` is a line bundle of degree `18-28=-10`. This proves the displayed sequence involving `O(-10)` without assuming that an extension splits.

## Placement and saturation audit

5. **The negative quotient genuinely kills N.** A local section of `N` is a local section of the constant subbundle `C O`; its derivative remains in `C O tensor Omega1`. Modulo `E`, its derivative therefore lands in `(C O/N)(-2)=O(26)`, the actual positive part of the Gauss quotient. Its component in `L` is zero.

   The quotient map from `E/F=T O(-3)+L` to `L` is zero on `T O(-3)` by ordinary degrees. It is surjective, because it is induced by the surjective actual quotient `E -> A_q` followed by projection to `L`. Its restriction to `L` is therefore an isomorphism. It follows that the actual inclusion `N/F -> E/F` lands entirely in the displayed `T O(-3)` factor. The proof's additional equivariant channel checks are consistent; surjectivity of this equal-rank restriction already suffices.

6. **The quotient Z0 is locally free.** The sheaf `E/N` embeds in `(H/C) O` as an image sheaf and is torsion-free. Hence `N/F` is saturated in `E/F`. Since it lies entirely in the `T O(-3)` factor, the quotient

   ```
   Z0 = T O(-3) / O(-10)
   ```

   is locally free. It has rank five and degree `-18+10=-8`. Twisting the actual quotient by three exhibits `Z0(3)` as a quotient of a trivial bundle, so it is globally generated. Therefore every ordinary splitting degree of `Z0` is at least minus three. No finer splitting has been presumed.

7. **Saturation of the projected residual is proved, not inferred from local freeness.** Write `Q=(H O)/E`. The zero-defect quotient `E^+/E` is saturated in `Q`, because its quotient is `(H O)/E^+`. The positive `O(28)` is a direct summand of `E^+/E`. Thus it is saturated in `Q`: its quotient in `Q` is an extension of the locally free bundles `L(2)` and `(H O)/E^+`.

   In the case under consideration, `C O/N` maps isomorphically onto exactly this positive subbundle. Therefore

   ```
   (H O)/(E+C O) = Q/O(28)
   ```

   is locally free. Consequently `E+C O` is saturated in `H O`, and its quotient

   ```
   R = (E+C O)/C O = E/N
   ```

   is an actual saturated subbundle of the constant `(H/C) O`. The abstract quotient splitting `R=Z0+L` supplies actual subbundles of this embedded `R`. In particular `Z0` is saturated in the constant ambient quotient as well. This is the essential saturation step, and it is sound.

## Connection and horizontal-residual audit

8. **The external derivative has the claimed target.** Projection by a constant subspace commutes with the constant connection. Local sections of `R` lift locally to sections of `E`, whose derivatives lie in `E^+ tensor Omega1`. Hence the second fundamental form of `R` factors through

   ```
   E^+/(E+C O) tensor Omega1 = L(2)(-2) = L.
   ```

   Restricting this O-linear map to `Z0` gives zero: every source splitting degree is at least minus three and every target splitting degree is at most minus eight.

9. **The internal derivative is legitimate and zero.** The previous vanishing puts derivatives of sections of `Z0` inside `R tensor Omega1`. Reducing modulo `Z0 tensor Omega1` is an O-linear map, since the Leibniz term already lies in `Z0 tensor Omega1`. Its target is `(R/Z0)(-2)=L(-2)`, and the same degree comparison makes it zero. Thus the actual embedded `Z0` is horizontal for the constant connection. The argument does not declare an abstract direct summand horizontal without checking both derivative components.

10. **The contradiction follows for the actual subbundle.** The saturated `Z0` defines a Grassmannian-valued map from the characteristic-zero projective line. Its second fundamental form is the differential of that map. A zero differential makes the map constant, so `Z0` is a constant degree-zero subbundle. This contradicts its already established degree minus eight. Therefore `C O subset E^+` is impossible.

## Recovery of the conclusions and limits

The initial saturated-intersection dichotomy now gives `E^+ intersect C O=F^+` as sheaves. Since `E subset E^+`, the second intersection is the kernel of the actual map `F^+ -> E^+/E`, which the imported top-image statement identifies with `F`. Thus `E intersect C O=F` also holds as a sheaf identity.

For the final generic statement, let `K=E^-`. Over the function field, `p(F)` is the full positive line. A class in `E/F` can therefore be represented by an element of `K` exactly when its negative quotient is zero: any positive component can be cancelled by an element of `F`. The negative quotient's kernel is the `T O(-3)` factor. Since `E intersect C O=F`, the induced map `E/F -> (H/C) O` is injective as a sheaf, so the asserted equality of the two generic projected subspaces follows. This does not prove that either projected image is saturated globally, and the proof correctly does not claim it.

No blocking gap was found. The result is an endpoint condition for the two specified labels and degree-twenty-divisor stratum, not their full exclusion, not constant separation, and not a resolution of source2 or the basepoint-free strata. The maximal backward-rank hypothesis is part of the stated setting but is not needed for this local contradiction.

The audit used structural bundle, quotient, equivariance, and connection arguments, together with exact file-identity checks. It did not evaluate any selected actual HM/source coefficients, parameters, points, derivative values, matrices, or source-instance ranks, and did not run an enumeration or large computation.

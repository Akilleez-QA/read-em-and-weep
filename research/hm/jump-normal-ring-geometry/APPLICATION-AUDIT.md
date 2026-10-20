# Historical mathematical audit receipt

This is a preserved review of the source mathematical manuscript, not a fresh review of the publication bytes. Hashes quoted below identify the historical source versions. See [hm-formal-jump-rings-PUBLICATION-CHECK.md](../hm-formal-jump-rings-PUBLICATION-CHECK.md) for the final-publication review.

# Independent audit of the HM hull corollary

## Verdict

**Pass, with the explicitly imported independently audited HM inputs.** The final `APPLICATION.md` is a valid corollary of the accepted all-orders normal-form theorem and the independently checked universal algebra. No mathematical correction is required.

This certification upgrades the previous dependency-pending application check. It does not broaden the scope of `AUDIT.md`, which remains an audit of universal algebra and records the earlier status accurately as of that check. No change has been made to either `PROOF.md` or `APPLICATION.md`.

## Exact files verified

The following SHA-256 values were independently recomputed from the current files on 2026-10-20 (UTC):

| File | SHA-256 |
| --- | --- |
| `APPLICATION.md` | `bf1d7c309f12d4640971a267473ebec3915a3af68b689807a42b00870afbbd78` |
| `PROOF.md` | `93dd3734adf259c434375937bd1bb3cf186ebaa9a657ea2e8102e40b30674884` |
| `AUDIT.md` | `08fd238503c055d39ca961754a9f14be7ff36f4e4927dda929d46317123274c3` |
| `../formal-jump-normal-forms/PROOF.md` | `dff5923dffd3f5657c3be3cd3979ed5ac456aed00d0765243ce379bf181c70a3` |
| `../formal-jump-normal-forms/AUDIT.md` | `aab68d6940045552342bc3fb3cb7f9de33ff88813722c305d823f51da7c47c7e` |

The imported audit explicitly accepts the exact formal-proof hash listed above. Its acceptance covers the complete formal ring identification, not just the quadratic initial obstruction equations. Its conditions and limitations agree with the final application's dependency statement.

## 1. Sufficiency and correct use of the imported theorem

I read the current formal proof and its independent audit. The theorem gives precisely the two needed identifications:

1. At a rank-one point with nonzero orbit derivative pairing, the complete minimal ordinary fixed-quintic bundle-deformation hull is
   \[
   \mathbf C[[t_1,\ldots,t_{24},z]]/(z^2,t_1z).
   \]
2. At a vertex with surjective orbit derivative pairing, the hull is
   \[
   \mathbf C[[t_1,\ldots,t_{24},z_1,z_2]]/
   ((z_1,z_2)^2,t_1z_1+t_2z_2,t_2z_1+t_3z_2).
   \]

The imported theorem states that these formal isomorphisms preserve the orbit ideal: the embedded orbit germ becomes \(z=0\). Its audit specifically checks the passage to the ordinary deformation hull, the full endomorphism cyclic construction, orbit straightening, and the exact coefficient-absorption argument. Accordingly, the application is entitled to use complete local ring isomorphisms, not merely similarities of tangent spaces or quadratic terms.

The rank-one and vertex assumptions in `APPLICATION.md` match those of the imported theorem. The dimension of the orbit germ is 24 in both sources. The theorem and its audit also explicitly import the nonempty open dense genericity conclusions on the respective smooth-quintic strata. Thus the application's genericity sentence has a stated audited dependency rather than being inferred from the universal rings alone.

This application audit does not independently repeat the earlier HM cohomology, scalar nonvanishing, pairing, cyclic-model primary-source, or genericity proofs. Those are explicitly imported through the accepted theorem and its audit.

## 2. Ring invariants transport correctly

An isomorphism of complete local rings preserves the nilradical, reduction, associated primes, depth, embedding dimension, Hilbert–Samuel multiplicity, and maximal-ideal associated graded Hilbert series. Preservation of the embedded orbit ideal further identifies the whole reduction with the particular orbit germ, rather than with an unspecified smooth germ.

The already certified universal algebra therefore proves all the listed common consequences:

- The whole reduction is the smooth irreducible 24-dimensional orbit germ, with no additional reduced branches.
- The nilradical is nonzero and square-zero, supported on exactly the displayed divisor.
- The total hull is generically reduced, has multiplicity one, and has depth 23 at the closed point.
- Its associated primes are the unique minimal prime and one embedded height-one prime over the support divisor.
- There is no additional associated prime supported at the quadratic vertex.
- The nonregular and non-Cohen–Macaulay loci are exactly the support divisor.

In the first case, the divisor is smooth and the nilradical is its structure sheaf as a module. The embedding dimension and Hilbert series are 25 and
\[
\frac{1+q-q^2}{(1-q)^{24}}.
\]

In the second case, the divisor is the rank-three quadric cone \(t_1t_3-t_2^2=0\) with 21 passive smooth coordinates. The nilradical is the ideal \((t_1,t_2)\) as a module on that divisor. It is rank-one reflexive and maximal Cohen–Macaulay, is locally free off the 21-dimensional vertex, and requires two generators there. The application correctly distinguishes this module identification from multiplication inside the hull, where the nilradical squares to zero. The embedding dimension and Hilbert series are 26 and
\[
\frac{1+2q-2q^2}{(1-q)^{24}}.
\]

The formal coordinate changes need not preserve the original degree-one coordinates to preserve these Hilbert series: a local-ring isomorphism preserves the maximal-ideal filtration and hence its associated graded Hilbert function.

## 3. Fibers, localizations, and compatibility

The normal forms supply a noncanonical splitting over the reduced orbit power-series ring. Thus the finite morphism to the reduced germ used for the fiber statements exists after choosing the stated normal form; it is not being asserted as a canonical retraction associated with reduction in general.

Over the generic point of the divisor, that finite morphism has a length-two dual-number fiber. At the quadratic vertex it has a length-three fiber with two-dimensional square-zero maximal ideal. These statements follow by tensoring the explicit split square-zero algebra with the residue field.

In contrast, the localization at the embedded prime has a DVR as its reduction and a square-zero copy of the DVR's residue field as its nilradical. It has dimension one and depth zero. The application states this distinction correctly and does not confuse localization with the zero-dimensional fiber.

On the smooth part of the quadratic divisor, an invertible diagonal coefficient permits elimination of one normal variable, yielding
\[
T_{\mathfrak p}[\epsilon]/(\epsilon^2,d\epsilon),
\qquad d=t_1t_3-t_2^2.
\]
The element \(d\) is a regular parameter there. This is the rank-one local pattern established in the frozen universal proof. The application correctly limits this compatibility to local algebra and does not infer a globally identified family of HM hulls as the quintic varies.

References to generic primes and localizations are read as statements about the ordinary spectrum of the completed local algebra, equivalently about the corresponding formal-local algebraic geometry; they do not assert that an adic formal spectrum has the topology of all prime ideals.

## 4. Scope is preserved

The application's restrictions are necessary and correctly retained:

- The result applies under the stated nonzero/surjective derivative hypotheses, and generically on the strata only by the imported genericity theorems.
- It makes no assertion at nontransverse rank-one points or nonsurjective vertices.
- Its coordinates and ring identifications are formal and noncanonical; no analytic or algebraic convergence is inferred.
- It does not identify the divisor with an independently defined geometric subvariety without another argument.
- It does not assert DGLA formality, vanishing of ordered higher operations, a global moduli description, or conclusions for constrained/source-restricted deformation problems.

With these existing qualifications, the corollary is established relative to the named accepted dependencies. Only local file reads, hash computations, abstract implication checks, and this separate local audit write were used.

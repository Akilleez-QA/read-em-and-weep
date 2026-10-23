# Independent audit of the defect-twelve endpoint exclusion

## Verdict and audited version

**PASS with the explicitly identified public dependencies.** The endpoint-intersection recovery and the backward-rank contradiction are valid. I found no substantive gap and no required mathematical repair. They exclude exactly the two stated maximal profile-(1,1) labels, G3.11.cb71f599859d and G3.11.0fe2a757439f, under the original actual-bundle hypotheses.

The audited PROOF.md has SHA-256:

    58752667d3b9cf603cc4a99b3ebce8b2f0e85af92ea8d5937cf3314d7d5edfa3

I did not author or modify that proof or its companion. This review treats the companion source-reduction and tensor-quartic theorem as an explicit dependency, with SHA-256:

    0e28eed42faf99a0ebaed4bfcf7e54b20f0e13d642f92f61864e421043e71915

Its frozen local proof and independent review were inspected. During this audit the companion became public in draft PR801 at immutable commit 4301e3b3027afa1c32e1e7359a5fdf5b9d27edfd, research/hm/profile11-defect12-constant-residual/PROOF.md. I independently retrieved that pinned public file and verified exact equality with the frozen bytes above. The endpoint proof was updated only to replace its reserved companion-publication paragraph with this pin and direct URL; reconstructing the earlier paragraph recovers its initial audited SHA-256 a5c358d12f77a710b4c1b1798b93ad792499d1eb6df6411681479195baf60804. No mathematical content changed. The companion's separate abstract residual-construction supplement is not used.

The audit used universal sheaf, bundle, connection, and jet arguments, together with the bounded representation identities in the stated dependencies. It used no selected actual HM/source-instance coefficients, parameters, points, derivative evaluations, matrices or ranks, model experiments, scans, or large computation. Public-source access was read-only.

## 1. Intersections and the rank-at-most-one bound

Put C=C0 O. Since E and E^+ are saturated in H O, their sheaf intersections N=E intersect C and Nplus=E^+ intersect C are saturated in C. For example C/Nplus injects into the locally free H O/E^+, so it is torsion-free, hence locally free on the curve. The corresponding intersections are also saturated in E and E^+ when needed. None of this identifies fibers of the sheaf intersections with full fiberwise intersections at exceptional points.

The derivative of G is onto (C/G)(-2), and induces the stated isomorphism G/F -> (C/G)(-2). Its composition with H O/E^+ kills G0=E intersect G because differentiation of E takes values in E^+. This uses only the automatic inclusion E subset (E^+)^-, not equality. The composition therefore has generic rank at most rank(G/G0)=1. Since its image is the entire (C/Nplus)(-2) followed by a sheaf injection, rank(C/Nplus)<=1 is justified.

The rank-zero alternative is correctly excluded. If C is contained in E^+, its image in E^+/E has no negative component, and its positive line image contains the original f12 O(16). It is consequently O(28)(-D') with 0<=D'<=D12. Equivariance makes D' invariant; since D12 is one reduced orbit, D' is either zero or all of D12. The kernel then has rank fourteen and degree -28 or -16. H0(E(1))=0 forces each of its splitting degrees to be at most -2, excluding degree -16. Degree -28 forces O(-2)^14, whose inclusion into E factors through the rank-nine degree-minus-two block F, also impossible.

Thus C/Nplus is genuinely a line bundle. No section-vanishing statement about E^+ was used.

## 2. The quotient degree is forced by a surjection, not by cancelling a divisor

The map C/G -> C/Nplus is a quotient map of bundles, hence is onto. After twisting and using the derivative isomorphism, it gives the everywhere-surjective map

    X=V O(2) -> O(e-2).

Its rank-two kernel contains G0/F=Wp O(-5). The latter is saturated in X by the actual exact sequence X -> O(16). Equal generic ranks and saturation force equality of these kernels: any additional quotient would be torsion inside the torsion-free X/(G0/F). It follows that e-2=16, so e=18, and that Nplus/G=Wp O(-3).

This argument does not upgrade an arbitrary injective line map to an isomorphism. Its essential extra input is the surjectivity just established. In particular it does not saturate the original f12 O(16) inside O(28).

The extension of Wp O(-3) by G splits as an equivariant bundle extension because H1(O(2))=0 and finite-group averaging preserves splittings. Therefore Nplus has only degrees -1 and -3, and every map from it to the negative summands of E^+/E vanishes. Its nonzero image there is a line in O(28), so N has rank thirteen and is saturated in Nplus.

## 3. Recovery of the exact backward intersection

In the actual constant C, the derivative of Nplus has target O(16). Its restriction to G is onto by the preceding quotient map, so its kernel Nprime has rank thirteen and degree -34. A section of N differentiates into both E^+ and C, hence into Nplus. Thus N is contained in Nprime. Since N is saturated in Nplus and has the same rank as Nprime, equality follows.

This proves N=(Nplus)^- by an internal intersection argument, not by importing (E^+)^-=E. It also proves the exact sequence

    0 -> N -> Nplus -> O(16) -> 0.

As a useful consistency check, the image of Nplus in O(28) consequently has degree sixteen. It contains f12 O(16), so it is exactly that defective image. The external length-twelve divisor has not disappeared from the original quotient.

## 4. Euler extension and residual: PR797 transfers exactly

The local subtraction argument is valid because the derivative G -> O(16) is onto. For any local section of Nplus lifting a section of Nplus/G, subtract a section of G with the same derivative. This produces a section of N. The kernel of N -> Nplus/G is N intersect G=G0, giving the exact extension

    0 -> Wp O(-5) -> N/F -> Wp O(-3) -> 0.

Its equivariant extension space is one-dimensional. The split extension cannot inject into E/F, since its Wp O(-3) summand has zero map to T O(-3) by inequivalence and zero map to every lower summand by degree. Hence the extension is the nonzero Euler extension, with N/F=P O(-4). Its extension by F splits by the indicated positive-twist H1 vanishing.

The unique nonzero linear channel P O(-4) -> T O(-3) is precisely the standard saturated inclusion obtained from the complete quadratic evaluation sequence tensored with Wp. Its quotient is Wp O(-1). Thus the displayed residual E/N=Wp O(-1)+L is the actual locally free image sheaf under the constant projection. No flat splitting or saturation of the entire image in (H/C0) O is inferred.

These are exactly the hypotheses and conclusions of PR797 Section 7. That section does not additionally need zero original defect, H0(E^+)=0, or the profile-(1,2) interior-stage equality once the endpoint exact sequences have been supplied. The proof correctly supplies those sequences anew rather than importing PR797 Section 6.

The mismatched E6 source for the W O(-9) quotient is independently and correctly removed: only its single O(-10) summand can map nontrivially to that negative rank-two block, so it cannot surject.

## 5. Backward-rank obstruction: PR798 transfers exactly

For the matching pairs, N maps onto precisely O(14) in A_q. Surjectivity already holds on F by the companion input, while all maps from N to the negative part vanish by degree. Consequently the map E/N -> L is onto, kills Wp O(-1), and is an isomorphism on L. The kernel diagram therefore gives an onto map K=E^- -> Wp O(-1), identifying the actual projected image of K.

That embedded Wp O(-1) has the claimed Gauss rank two. Its coefficient map is a nonzero equivariant map P=Wp tensor W -> H/C0. Irreducibility makes this constant map injective, so the embedded bundle is the standard rank-two tautological subbundle of the constant P O. This proves its saturation and derivative rank without requiring saturation of E/N.

The recovered quotient V O(4) -> O(18) is onto, so its degree-fourteen three-section system is basepoint-free. Its composite with the complete quartic evaluation system generates jets through order four at every point: locally one nonvanishing degree-fourteen section multiplies the full degree-four system, and multiplication by a unit is invertible on jets. This is a universal local proof, not evaluation at a selected point.

The principal-parts kernels therefore satisfy J0=Nplus, J1=N and J2=N^-. Since C0 is constant and E intersect C=N as sheaves, differentiation modulo E on N has the same kernel as differentiation modulo N. Hence J2=K intersect C. Jet generation through order three already guarantees a nonzero rank-one derivative of J2 into (N/J2)(-2). Its image remains nonzero modulo K because N intersect K=J2.

At the generic point the derivative of K projects onto a rank-two image in (H/C0)/Wp O(-1). The preceding rank-one contribution lies in the kernel of that projection and is nonzero modulo K. The two contributions are independent, so generic rank beta_K>=3. This is legitimate generic linear algebra; neither K+C0 nor the whole residual image is assumed saturated.

The original maximal-plateau convention gives generic rank beta_(E^-)<3 when the maximal backward index is one. That index is one for both profile-(1,1) and profile-(1,2). Thus PR798 Sections 2-6 transfer without an extra forward-length or zero-defect assumption once the exact endpoint data have been recovered. The final contradiction is valid.

## 6. Public-pin verification and scope boundary

I retrieved the public files at their stated immutable commits and checked exact equality with the inspected local files:

- PR797, commit cdee9396133fb96d4a91babba87b1a7a35903635, research/hm/profile12-tensor-quartic-block/PROOF.md. SHA-256: 863bb17be118558b5c6199d0b3b73a7257cdd1f6871cdd903be2a19128574c98. Git blob: f397008bad1724ba3e81bdf84b5071fbc516f015.
- PR798, commit 2bbf244bafc380cf5b0ce1114f86fcd8053e4e55, research/hm/profile12-backward-plateau-exclusion/PROOF.md. SHA-256: 4ddb4c7993039cf0e4504c2cd7403b45925a508a6489cc366ac9892ba39f53e0. Git blob: 835404ada200cea294aa0cf0b13d962bd604cdc0.

The companion was independently read back at commit 4301e3b3027afa1c32e1e7359a5fdf5b9d27edfd and matches the explicit frozen SHA-256 above. Its public Git blob is 1a0b58e0d6d327850dfc4f86802a8bfb088a23e6. It is now an immutable public dependency, not an unpublished assumption. I also read the actual maximal-plateau convention at db51525015bb7c5e825833d550d08dedf6f6ea96 in research/hm/order-four-quadratic-load/ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md.

The new result is a formal actual-connection exclusion of these two full labels. It does not exclude G3.11.64d33b6d4139, alter that label's residual theorem, address source2, establish a higher-order lifting or algebraicity claim, prove SF>=4, or finish the original research goal.

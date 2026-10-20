# Historical review receipt

This review concerns its original manuscript version, not the normalized publication bytes. It is not a final publication-scope approval.

# Independent audit: general three-plane kernel incidence

Verdict: PASS for the frozen Sections 1–6. The assertions remain conditional on the imported canonical cubic symmetries and structural repeated-input nonvanishing. No actual kernel is evaluated.

## Kernel and invariant criterion

The Schur tensor normalization and contraction isomorphism identify a frame tensor with diag(1,0,−1) times its volume. For traceless three-dimensional endomorphisms, the characteristic polynomial t³−tr(A²)t/2−det(A) proves that det(A)=0 and tr(A²) nonzero is exactly the projective frame-tensor orbit. Distinct roots give the required eigenline decomposition. Only the universal tensor, rather than the actual map T, is used naturally under GL(W).

Every rank-one traceless tensor is square-zero and corresponds to tau(x,x,y) with independent x,y. The imported repeated-input theorem therefore excludes its projective flag variety from P(K). That flag variety is closed of dimension three in P^7. The projective dimension theorem gives dim K≤4, including the separately handled zero kernel.

## Polynomial test

For nonzero q,h, absence of h=0 with q nonzero is precisely q in the radical of the principal ideal (h). Unique factorization gives the stated factor criterion. The rank-one and rank-two quadratic cases yield exactly the listed cubic monomials. A rank-at-least-three quadratic is irreducible, so it cannot contain all irreducible factors of a cubic. The cases K=0, q=0, and h identically zero are separated correctly. This also covers one- and two-dimensional kernels without inappropriate projective dimension arguments.

## Scheme kernels and determinant twists

The exact-rank stratum is defined scheme-theoretically using vanishing higher minors and an invertible rank minor. Gaussian block elimination over that stratum makes the map an identity block plus zero, so its kernel is a subbundle and formation commutes with arbitrary base change within the stratum. Mere constancy of ranks on underlying points would not suffice; the proof uses the stronger determinantal scheme structure correctly.

With the lines convention on P(K), the universal tensor is an endomorphism valued in M=L* tensor det S. Its trace-square and determinant have values in M² and M³. Thus both the incidence and the square-root construction are globally well-defined without choosing a determinant generator. The quotient-ideal argument uses an actual local left inverse, preserving full scheme structures after base change.

## Orientation cover and zero frames

The equation lambda²=Q/2 in Tot(M) gives a finite locally free degree-two cover; invertibility of Q and characteristic zero make it étale even over a nonreduced base. After division by lambda, Cayley–Hamilton gives N³=N. The three displayed spectral idempotents are correct and yield rank-one summands by their geometric fiber ranks.

The frame/eigenline constructions are genuinely inverse: a zero frame specifies its tensor line and volume, and the unique map lambda:L→det S taking tau to that volume recovers the orientation. This also verifies the line-bundle twists and eliminates any unrecorded scaling constraint. Three independent vector scalings are allowed over the projective incidence; fixing the actual tensor imposes exactly one product constraint and leaves two scaling parameters.

The split torus bundle is Zariski locally trivial only after passing to the orientation cover. Over X the two components can be exchanged by monodromy. The proof correctly avoids asserting a global product or a Zariski-trivial orientation cover. Singularities or nilpotents of X are not removed by the smooth frame factors.

## Limits and evidence boundary

No actual kernel dimensions, Grassmannian strata, restricted quadratic ranks, cubic factors, or generic behavior have been computed. No full-moduli transverse assertion or physical-class decision follows. The audit used local proof reads and this local report only, with no actual HM/source/model products, evaluated ranks, inputs, points, jets, residues, or Massey values, and no external writes.

## Global-incidence addendum

The added global construction also passes. Defining Y inside P(E) by the universal composite L→E→J3 imposes the kernel condition directly and commutes with base change without identifying Y with the projectivization of a locally free kernel. Its geometric fibers are the desired projective linear kernels, and its restriction to a determinantal constant-rank stratum recovers P(K). Intersecting with the determinant-zero and trace-square-invertible loci preserves the intrinsic line-valued construction. A frame tensor generates its line as a subbundle, so the equations T|L=0 and T(tau)=0 agree after pulling back to frames. The inverse eigenline/frame functors therefore work across all kernel-dimension jumps, including nonreduced test bases. Final verdict: PASS for the complete proof, with no outstanding corrections.

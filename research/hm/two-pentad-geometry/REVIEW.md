# Independent review: two-pentad transversality

Reviewed final PROOF.md SHA256: `9f087a4a9522dfdbb632fb427448bf828a90483b62bf3b25ca8f885e81a1a3ff`.

Verdict: **PASS**, conditional on the explicitly pinned inputs in PR610, PR616, and PR617. This is an independent mathematical audit, not formal verification. The proof resolves the two normalization nonvanishing gates without computing either scalar. It does not resolve the two descent gates or the original-source/full-adjoint/algebraicity boundary.

Reviewed files:

- `hm-two-pentad-geometry/PROOF.md`.
- `hm-cubic-joint-characters/PROOF.md`, especially Sections 2–5.
- `hm-cubic-residual-channels/PROOF.md`, especially Sections 2, 6, 8, and 9.
- `hm-cubic-scalar-constraints/PROOF.md`, especially Sections 2–5.

No selected HM/source-instance coefficient, derivative, matrix, numerical rank, point evaluation, scan, or computer algebra was performed. The review used the supplied proof texts and exact conceptual linear algebra only.

## 1. The five fiber lines really lie in one fixed representation

The required maps are the actual maps

    F_G = H0(O_ZG(3)) -> F_Z -> F_Z/im(rho) = H1(D).

PR616 Section 8 proves that the first-to-last composite is an isomorphism. Its proof uses the actual restriction map to the other twenty-five centers, not an arbitrary isomorphism of abstract five-dimensional representations. Thus the five images `c_(G,i)` are independent lines in the same fixed vector space `C=H1(D)` for every G.

These maps inherit the common natural O(3) linearization. In particular the lift of G acting on `L_i` by `zeta^i` acts on its O(3) fiber by `zeta^(-3i)`. Since multiplication by -3 is invertible modulo 5, the five eigenvalues are distinct. Equivariance therefore identifies the fiber images with the five eigenlines of that actual operator on C. No independently chosen identification or phase is used for another pentad H.

PR616 Section 6 supplies a faithful central character on C. This also follows from the common O(3) linearization: the center acts by `c^(-3)`, a nontrivial and therefore faithful character of the order-five center. The five-dimensional C is the irreducible representation with that central character. Twisting scalar lifts changes eigenvalues but not the eigenline decompositions or any support statement.

One can strengthen the equivariance observation if desired: each pentad is stable under the full Heisenberg group because conjugation of a direction lift changes it only by a central scalar. Consequently its inclusion in F_Z and its quotient map to C are Heisenberg-equivariant. The proof only needs equivariance for the individual direction lifts.

## 2. The Fourier comparison and the exact uncertainty range are valid

For distinct directions, independent lifts g and h on C satisfy

    g h = lambda h g

with lambda a primitive fifth root. Given a g-eigenvector e_0, the five vectors `h^j e_0` have pairwise distinct g-eigenvalues, hence form a basis. Because the chosen lift has order five, h cyclically shifts this basis. Its eigenvectors are Fourier sums. Thus the two eigenbases differ by a Fourier matrix, diagonal rescalings, and permutations. All of these preserve the asserted support-intersection property.

The proof only requires a vector with at most two H-coordinates to vanish in at least two G-coordinates. For two distinct rows and columns, the relevant determinant is a nonzero root-of-unity factor times

    1 - lambda^((a-b)(c-d)).

Both differences are nonzero modulo 5, so the determinant is nonzero. The one-column case is immediate because every Fourier entry is nonzero. Consequently a span of at most three G-fiber lines has zero intersection with a span of at most two H-fiber lines. The restriction to these dimensions is essential and is applied correctly. There is no appeal to a generic pair of bases or to an unproved phase identification.

## 3. Audit of the actual first-jet support

PR616 Section 2 identifies the normalization derivative with

    v -> [s -> sum_i c_i ds_i(v_i)],

where the notation uses nonzero local fiber generators only to write the map. A section in S vanishes at every center, so its derivative at a center is intrinsically fiber-valued. Changing a fiber generator rescales the associated S* factor inversely and does not alter its subspace E_i or the tensor product `c_i tensor E_i`.

At center i, the four projective tangent directions toward the other four eigenlines span the tangent space. PR610 Section 5 identifies their exceptional image lines with the nonzero lines `q(L_i^2 L_j)`. Their first weight coordinates `2i+j` are distinct for distinct j, so the four image lines are independent. They therefore span the four-dimensional first-jet image E_i, consistently with the independent first-jet injectivity input in PR616 Section 9.

For the mark (i,j), the only other repeated-index representative of its joint-weight line is `(2i-j,3i-2j)`. Put `k=2i-j`. Then `k!=i`, and conversely the unordered pair {i,k} determines the two marks

    (i,2i-k) and (k,2k-i).

Hence the twenty marks pair into exactly the ten unordered edges of K5. PR610 proves that each resulting line is nonzero and is a distinct one-dimensional joint-character summand. Since `dim S*=10`, these lines form a direct-sum decomposition of all S*. Each E_i is exactly the sum of the four incident edge lines, not just a subspace whose abstract character matches that sum.

The cohomology fiber lines are independent. The center motions are independent, and the individual jet maps are onto their images E_i. It follows that the exact actual image is

    W_H = direct-sum_i c_(H,i) tensor E_(H,i).

In the basis of S dual to the edge-line basis of S*, a map in W_H consequently takes an edge input `s_(i,k)` into the plane spanned by `c_(H,i)` and `c_(H,k)`. This is the needed actual jet support. No relation between the two coefficients in that plane, and no coefficient value or ratio, is assumed.

## 4. Mixed-plane exclusion and the dimension bound

Suppose `f in W_H` has image in a span of at most three G-fiber lines, with G distinct from H. On each edge-basis input, its value lies in that G-span and in one of the two-dimensional H-fiber planes. Section 2 makes this intersection zero. The edge inputs form a basis of S, so f is zero. This proves the mixed-plane exclusion on actual maps.

Choose three of the five G-fibers. Projection of W_G to its other two summands has an eight-dimensional target, since each jet summand has dimension four. On `W_G intersect W_H`, its kernel consists of maps whose image lies in the chosen three G-fibers. The mixed-plane exclusion makes this kernel zero. Therefore

    dim(W_G intersect W_H) <= 8.

This step uses a projection in the direct-sum decomposition of W_G, not an unproved quotient or a projection that must preserve W_H. Only the kernel of its restriction is needed, so there is no invariance gap.

## 5. Dependence on the dichotomy and quantitative consequences

PR617 Section 5 concerns these same actual images of the normalization derivative. It states that their intersection dimension is either 0 or 16, with the alternatives equivalent respectively to q=2 and q=1. Each individual image has dimension twenty, and the map from a two-pentad motion space to its image intersection has the stated kernel interpretation. The new upper bound excludes 16. It follows for every distinct pair that

    W_G intersect W_H = 0,
    q = 2,
    rank(b_N) = 48.

Thus both normalization scalar maps are nonzero. The conclusion is nonvanishing of their intrinsic one-dimensional maps, not a choice of scalar values or a selected rank computation.

The source of b has dimension 96. Consequently `ker(b_N)` has dimension 48. The two remaining possible descent channels give `r=2,3,4`, whence

    dim ker(b) in {48,24,0},
    dim T_embedded in {147,123,99}.

The asserted upper bound 147 and the exact list of possibilities are correct. By the disjoint shear weights of PR616 Section 8, the kernel of normalization consists precisely of source weights 2 and 3 at each of the twenty-four nontrivial U-characters. Those weights match the remaining descent targets. The immediate next reduction in Section 6 is therefore valid, but it does not assert either descent gate is nonzero.

The expanded Section 6 was also checked. Since the source has no invariant U-character and b_N is equivariant, its image lies in N_nt. Both have dimension 48, hence the image equals N_nt. The finite-group averaging projector gives a canonical decomposition `N=N^U direct-sum N_nt`, so the cokernel is canonically N^U of dimension two. This is a canonical quotient identification, not an arbitrary representation isomorphism.

PR617 Section 6 proves that the four shear-weight channels extend to four pairwise nonisomorphic normalizer irreducibles of dimension twenty-four. The normalization maps are nonzero on the weight-1 and weight-4 irreducibles and vanish on the weight-2 and weight-3 irreducibles. Thus their latter direct sum is exactly the forty-eight-dimensional kernel. The descent map is equivariant on that kernel. It has zero projection to J^U because there is no invariant character in its source; J_nt is the direct sum of the two matching irreducibles by the same pinned representation result. Consequently the sharpened image, cokernel, kernel, and residual-target assertions of the final Section 6 all follow without any additional gate evaluation.

## 6. Scope and disposition

The new geometric ingredient is substantive: the K5 incidence support of the actual jets, combined with the actual cohomology eigenline decompositions. PR617's limitation on abstract equivariance is not contradicted, because an arbitrary equivariant scalar-gate pattern need not realize this extra tensor support.

No mathematical correction is required for the result. Two minor editorial clarifications were relayed to the author and corrected: the four-dimensional E_i is called a subspace rather than a line, and an unnecessary rank-one comparison was removed, since W_H itself contains rank-one maps. Neither affects the mixed-plane exclusion or the intersection bound. The proof is appropriately conditional on its pinned dependencies and does not claim higher-order integrability, smoothness, an exact final tangent dimension, full-adjoint properties, or original-source algebraicity. With those boundaries, the proposed normalization resolution passes independent review.


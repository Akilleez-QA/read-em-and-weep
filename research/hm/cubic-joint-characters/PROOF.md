# Joint characters force the actual cubic double fibers

Status: independently mathematically reviewed (PASS); see REVIEW.md. Not formally checked. Work over C. No selected actual HM/source coefficient, matrix, point evaluation, rank test, numerical search, or computer algebra is used. Character labels below belong to an arbitrary abstract irreducible Heisenberg module. The interpolation input is the universal theorem already proved in PR587, not a selected geometric calculation.

## 1. Pinned inputs and result

- PR587, 865ab24e91333688d7ae76303d7d594aae8521f8, research/hm/eigenline-interpolation/PROOF.md, Sections 1–2 and 4: the actual node support Z consists of the thirty eigenlines of the six projective Heisenberg directions in A. For any chosen direction G, ambient cubics restrict surjectively to the other twenty-five eigenlines. Section 2 proves this for every irreducible five-dimensional Schrödinger module using universal Fourier character identities. Its assertion is surjectivity onto those twenty-five nodes, not merely a dimension bound for all thirty nodes.
- PR604, a4a0b5ed6e9dd0c18e3a263d1b3f8d9a49f2bf8d, research/hm/cubic-embedding-locus/PROOF.md: W=H0(I_Z(3)) has dimension ten; the complete system induces Phi on M=Bl_Z P(A); every exceptional divisor is embedded and every first-order exceptional value is nonzero. Its common exceptional intersection dimension is r.
- PR608, 76d49d484c98bf0dd0f714c3e7041389d7cdede4, research/hm/cubic-fixed-directions/PROOF.md: r belongs to {0,1}; r=0 gives a closed immersion, whereas r=1 gives exactly sixty bad values with two reduced unramified preimages each, both on the resolved surface Y. Both ambient and restricted surface maps are everywhere unramified.

**Theorem.** The actual value is r=1. Thus the degree-51 ambient cubic image and degree-75 restricted surface image have exactly sixty singular/nonnormal points and the same reduced two-point normalization fibers. On each eigencharacter affine line, the marked direction (i,j), i != j, has the same cubic image as

    (2i-j, 3i-2j).

No analytic branch-transversality or completed-local-ring assertion follows here. The separate full-adjoint and higher-lifting gates remain unchanged.

## 2. An honest order-twenty-five linear subgroup

Fix an arbitrary direction G. Choose a primitive fifth root zeta matching the faithful central character, an order-five lift g, and label its five one-dimensional eigenspaces L_i so that g acts on L_i by zeta^i. Choose another Heisenberg element s with s(L_i)=L_(i+1). These are abstract character choices, possible by the nondegenerate commutator, not selected actual coordinate values.

Define a linear automorphism h intrinsically by its scalar on each character line:

    h|L_i = zeta^(i^2).

Then g and h commute and both have order five. If g^a h^b were scalar, then ai+bi^2 would be constant for all i in F5. A polynomial of degree at most two with five roots must vanish identically, so a=b=0. Thus D=<g,h> is an honest C5 x C5 in GL(A), and its projective image has the same order twenty-five. This fixes all linearization/scalar questions at once; no unproved identification of a Weil lift or of a cokernel representation is involved.

The automorphism h normalizes the Heisenberg group. Indeed it fixes g, and on L_i one obtains

    h s h^(-1) = zeta^(-1) g^2 s.

Consequently it induces the nontrivial shear fixing G on U=F5^2. Its action on the other five directions is a five-cycle. The subgroup G acts freely and transitively on the five eigenlines of every direction other than G: a nontrivial commutator shifts all five eigencharacters of that other direction. Therefore D acts freely and transitively on Z'=Z minus the five G-eigenlines.

The linear action supplies the natural linearization of O(3). For any line bundle on a free D-orbit, its section representation is the regular representation: pick any nonzero vector in one fiber and transport it by D. Freeness makes this an equivariant basis with no stabilizer character ambiguity. Hence H0(O_Z'(3)) has each D-character once. The same holds for its dual.

## 3. The actual cubic kernel, not a matching representation

PR587 supplies the surjective D-equivariant restriction map

    R': Sym^3(A*) -> H0(O_Z'(3)).

Its kernel has dimension 35-25=10. Every cubic in W vanishes on Z', so W is a subspace of this kernel. PR604 gives dim W=10, hence

    W = ker R'.

This is an equality of the actual subspaces, from an inclusion and proved surjectivity. It is not inferred from a coincidental representation dimension. It avoids any need to normalize the five-dimensional cokernel of restriction to all thirty nodes.

Dualizing gives the exact D-equivariant sequence

    0 -> H0(O_Z'(3))* -> Sym^3(A) -> W* -> 0.       (1)

Since D is finite over C, every character summand is exact. Thus the multiplicity of a character in W* equals its multiplicity in Sym^3(A) minus one.

## 4. Exactly two tensor lines in each repeated-index weight

The tensor line L_i L_j L_k in Sym^3(A) has joint weight

    (S,Q)=(i+j+k, i^2+j^2+k^2).

For i != j, the repeated-index tensor L_i^2 L_j has precisely one other unordered index multiset with the same joint weight, namely

    (2i-j, 2i-j, 3i-2j).                         (2)

Here is a short exhaustive proof using only abstract labels. The affine change t -> (t-i)/(j-i) sends the first triple to (0,0,1). Equality of S and Q is preserved under an affine relabeling: S becomes aS+3b and Q becomes a^2 Q+2abS+3b^2. It therefore suffices to classify triples with S=Q=1.

An all-equal triple would have entry 2 from 3t=1, but Q=3(2^2)=2, impossible. If the three entries are distinct, their complementary pair d,e in F5 has d+e=4 and d^2+e^2=4. Thus de=1, and its discriminant is 4^2-4=2 in F5, a nonsquare. This is impossible. Finally write the triple as (a,a,b). Then b=1-2a and Q=1 gives a^2+a=0. Thus a=0 or4, yielding exactly (0,0,1) and (4,4,3). Undoing the affine change gives (2).

It follows that the joint character of L_i^2 L_j has multiplicity exactly two in Sym^3(A). By (1), it has multiplicity exactly one in W*.

## 5. Actual exceptional values are nonzero in that one-dimensional target

Let q:Sym^3(A)->W* be the actual restriction-dual quotient. The exceptional direction at [L_i] toward [L_j] has cubic image

    [q(L_i^2 L_j)].

To see this without evaluating any selected cubic, the universal polarization identity expands (u+t v)^3 as u^3+3t u^2v+O(t^2), for arbitrary u in L_i and v in L_j. The q(u^3) term is zero since [L_i] is a base node; division by the exceptional parameter leaves the line q(u^2v). The nonzero factor 3 is irrelevant projectively. Generation of 3H-E, or equivalently the proved exceptional embedding, guarantees q(L_i^2 L_j) is nonzero. This is a geometric nonvanishing input, not a coefficient evaluation.

The tensor line specified by (2) also has nonzero image by the identical argument. Both images lie in the same one-dimensional character summand of W*, by Section 4. They are therefore the same projective point. Their base nodes differ because i != j, so the corresponding points of M lie on distinct exceptional divisors and are distinct.

Thus Phi is not injective. PR608 leaves only r=0 or1, and r=0 would make Phi a closed immersion. Therefore r=1. Its sixty reduced double fibers and both exact singular/nonnormal loci now follow from PR608. The stated formula describes their marks; it squares to the identity and has no fixed mark. This agrees with the independent incidence-compatible pairing classification, but that classification is not needed to prove r=1.

## 6. Scope and convention checks

The domain of the cubic functions is Sym^3(A*), while exceptional evaluation tensors lie in Sym^3(A). Sequence (1) uses precisely this dual convention. A different scalar lift or affine relabeling changes individual characters but not equality or their multiplicities. The chosen h is an explicit intrinsic automorphism of the abstract eigenspace decomposition and is shown to preserve the actual node configuration; consequently it preserves its complete cubic ideal and the resolved cubic map. No assumed equivariance of a selected HM matrix is required.

Only universal character arithmetic and the already proved actual-kernel/first-jet inputs enter the new step. In particular the five-dimensional H1(I_Z(3)) is neither identified nor assigned a shear phase. No local singularity normal form, conductor length, or full original theorem is claimed.

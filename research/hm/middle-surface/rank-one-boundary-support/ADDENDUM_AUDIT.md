# Independent audit: distinct-factor annihilator quadrics

Verdict: PASS for the final ADDENDUM.md, subject to the scope stated below.

Final text read and verified on 2026-10-19. Frozen ADDENDUM.md SHA-256:

`2466bc7d632a610b79999b4ac3cadd4fcb46b7ade44512bacb90b780878a73a4`

This independently checks the proposed addition for Q=ab with linearly independent a,b∈E*. The previously audited main proof supplies normalization, generic polynomial division, and exclusion of pencils. 

## 1. Generic identity and possible poles

On the normalized smooth complete support curve T, use L=a_T*O(1) and denote its universal covector by u:E⊗O_T→L to avoid confusion with the fixed factor a. Away from supports [a] and [b], Q|ker(u) is nonzero. Sections 2–3 of the main proof therefore give unique regular λ and ℓ there and the full polynomial identity

u∘V=λab+uℓ.

Consequently λ is a rational section of L and ℓ a rational E*-valued function on T. The only possible poles occur at preimages of [a] and [b]. These preimages are finite because the support map from an integral complete curve is nonconstant.

## 2. Pole removal in the correct quotient

At a point p mapping to [a], trivialize L over the local DVR R=O_{T,p}. Reduce the full polynomial identity modulo the fixed linear form b. The λab term is identically zero even when λ has a pole. The remaining identity says that the product of u modulo b and ℓ modulo b is regular.

The residue of u modulo b is a nonzero multiple of a modulo b and hence nonzero. If ℓ modulo b had a pole of order m>0, multiply by a uniformizer to the mth power and reduce modulo the maximal ideal. The regular right side would reduce to zero; the left side would be the product of two nonzero linear forms in C[E]/(b), which is a polynomial domain. This is impossible. Thus ℓ modulo Cb is regular at p. The proof handles arbitrary ramification of the support map and arbitrary pole orders.

At a point mapping to [b], the identical argument modulo a shows that ℓ modulo Ca is regular. Therefore the projection of ℓ to E*/span(a,b) is regular everywhere on T. Since this quotient is a constant vector space and T is complete and integral, the projection is constant. Choose a constant lift ℓ₀∈E*.

The argument depends on the factors being distinct. For Q=a², the residue of u modulo a vanishes at the exceptional support; the cancellation just used gives no pole-removal conclusion.

## 3. Evaluating the full identity

Let W=ker(a)∩ker(b), a two-dimensional subspace. Sym²W⊂K, and ℓ−ℓ₀ lies generically in span(a,b), so its shear vanishes on Sym²W. Evaluating the full polynomial identity on this fixed subspace therefore gives

u∘(v−Sℓ₀)|Sym²W=0

generically. Its left side is a regular bundle section, hence vanishes everywhere. It follows that

(v−Sℓ₀)(Sym²W)⊂I, where I=⋂_{t∈T}ker(u_t).

This step does not require W⊂ker(u_t): the identity being evaluated is the full ambient polynomial identity, not merely its restriction to a moving hyperplane.

## 4. Final contradiction and exact scope

If the support image is nonlinear, its projective linear span has dimension at least two. Thus dim(I)≤1. A linear map Sym²W→I yields at most one homogeneous quadratic equation on the projective line P(W). Over C this has a zero, including when the polynomial is identically zero. For some e≠0 in W,

(v−Sℓ₀)(e²)=0, so v(e²)=ℓ₀(e)e.

Since e²∈K, this is a forbidden compatible square. A line image was already excluded by the all-pencil theorem. Therefore no complete nonconstant support curve exists when the scalar annihilator quadric has rank two.

Combined with the main proof, positive-dimensional support fibers at residual rank one can remain only for a rank-one scalar annihilator Q=a², and their complete curve components must have nonlinear image and meet [a]. This audit does not exclude that remaining double-plane case or a positive-dimensional bad middle locus.

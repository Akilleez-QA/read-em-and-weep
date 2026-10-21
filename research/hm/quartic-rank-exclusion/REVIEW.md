# Independent review of the fifteen-quartic-generator exclusion

## Verdict and exact artifact

PASS, conditional on the pinned structural inputs stated in the proof. The exclusion of constant (and generic) a=15 uses PR519 and PR516. The uniform conclusion a(w)<=10 additionally uses the pinned quartic jump-divisor classification. No claim of proof-assistant verification is made.

Reviewed file: PROOF.md.

SHA-256: f1dd4645b207ea0b5e367293dfe05508ef7f81b983f7cb495a7586f90e5d89c6.

The original CANDIDATE.md was also read in full, at SHA-256 1f590cf1c15015660ade5dfcd31d9234827673f595c4309e6ed5e49a0ef29245. The final proof changes only status wording and pins the classification dependency.

## Independent verification

1. **Actual relation spaces.** PR519, commit cf328c6b0d05551a52911a3a4ba420c68f6fcc6f, Sections 1 and 5, identifies the actual dual annihilator of J_3,w with E tensor w^2 Sym^2(W) inside R_3^*=E tensor Sym^4(W). This is not merely a numerical bundle identification. A binary quartic divisible by the squares of three distinct linear factors must vanish. Thus even three distinct parameter lines already have zero intersection of these annihilator spaces. Tensoring by the fixed finite-dimensional E preserves this intersection statement. Finite-dimensional annihilator duality gives the claimed full span of the cubic fibers, hence the full 70-dimensional span of their products with T.

2. **Lower projection is surjective.** PR516, commit 89b66cbede7513c4f196fdbda0ee3bb77c53d2e0, Section 1, proves that T_w/I is generated in degree three. Its degree-four part therefore equals T times its degree-three part. This says exactly that the composite from the source of f onto Q_w=J_4,w/I_4 is surjective, for every w. All spaces here are fibers of the locally free quotients specified by PR519. The global composite is consequently a surjective bundle morphism.

3. **Constant-rank image.** Under constant a=15, f has rank 25-15=10 at every point. A constant-rank map between vector bundles has locally free kernel, image, and cokernel, and its fiber images are the images of its fiber maps. Its rank-ten image M surjects onto rank-ten Q. This is an isomorphism, not merely a generic isomorphism: in local trivializations its determinant is a unit at every point. Thus M=10O(-1) abstractly. No choice of graph, and no equivariant splitting, enters.

4. **Inverse image and extension.** The inverse image E_0 of the subbundle M under J_4 -> J_4/C is a subbundle, since its quotient is the locally free bundle (J_4/C)/M. It fits 0 -> 40O -> E_0 -> 10O(-1) -> 0. The extension group is a direct sum of H^1(P^1,O(1)), which vanishes. Hence the ordinary splitting used in the argument is valid. The inclusion into S_4 O is a genuine subbundle inclusion, though the span bound needs only a bundle morphism.

5. **Span bound.** A morphism O -> V O has one constant coefficient in V; a morphism O(-1) -> V O is an element of V tensor H^0(O(1)), so all its fiber images lie in the span of at most two vectors in V. Applied to the splitting of E_0, the total span has dimension at most 40+20=60, independent of choices of splitting or homogeneous coordinates. Each T J_3,w lies in E_0,w by construction of f, including the constant products T I_3. This contradicts item 1.

6. **Scope of conclusion.** The exclusion by itself rules out constant a=15. It also rules out generic a=15, since the already known bound a<=15 gives rank(f)>=10 everywhere, whereas generic rank ten bounds all fiber ranks above by ten on the integral base P^1. It does not by itself exclude a=15 at isolated points. The classification pinned at commit c56173aab6e9e5d7be2f2f638d6f953c9d7f93b1, research/hm/quartic-jump-divisors/PROOF.md, supplies precisely that additional step: its only pattern involving a=15 is the constant pattern. Thus the surviving patterns and uniform bound stated in Section 3 follow.

## Verification boundaries

This review independently checks the derivation, bundle exactness, fiber compatibility, splitting, duality and span obstruction. It relies on the cited original-module inputs and the separately established jump classification; it does not reprove the complete upstream research chain. No selected actual source-instance coefficients, matrices, numerical ranks, generator searches, or large computation were evaluated. No first-order lifting, higher-order lifting, or algebraicity conclusion follows from this review.

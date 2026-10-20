# Independent audit: rank-one surface Chern and nef constraints

## Verdict

The proposed identities and the correction-defined rank-three subbundle are valid under the global hypotheses stated below. The quadratic identity is proved in rational Chow; the direct integral consequence is a torsion identity. The positivity assertion requires a genuinely two-dimensional middle image, not merely a nonconstant middle map.

## Required global hypotheses

Let B be a smooth complete integral complex surface, with regular subbundles U ⊂ P ⊂ H ⊂ V⊗O_B of ranks 1,3,4. Write E=H/U and R=P/U. A regular nowhere-zero projective metric of rank one everywhere must have radical R. The actual-family correction must extend regularly on the metric kernel, satisfy its splitting-change formula, and satisfy the repeated-input nonvanishing property at every point, including the boundary. These are hypotheses imported from the earlier actual-family extension proof; an arbitrary assignment of quadratic corrections is insufficient.

A metric that is globally regular, projectively nowhere zero and generically rank one is rank one everywhere by closedness of the rank-at-most-one locus. A merely rational metric does not justify this conclusion. Resolving the middle surface does not by itself ensure that its support hyperplane map H is regular; regularity must be established or arranged and the correction extension checked on the resulting model.

## Exact integral Chern identities

Put a=c1(U*), p=c1(det P*), n=c1(V/H), u=-a, e=c1(E)=a−n, and r=c1(R)=a−p. Let π:S=P_B(R)→B parameterize lines, L=O_S(−1), and ξ=c1(L*). Then

ξ²+rξ+c2(R)=0,
c2(E)=a²−an+n²,
c2(R)=a²−ap+p²−pn+n².

The nowhere-zero section of F=(π*E/L)⊗π*U⊗L^(−2) gives c2(F)=0 integrally. Expanding before using the projective-bundle relation gives

c2(F)=c2(E)+ue+u²+(3e+5u)ξ+7ξ².

The integral projective-bundle direct-sum decomposition therefore yields the two exact equations

3e+5u−7r=0 in CH¹(B),
c2(E)+ue+u²−7c2(R)=0 in CH²(B).

Consequently

7p=9a+3n in Pic(B),
−6a²+7ap−7p²+7pn−6n²=0 in CH²(B).

Multiplying the second identity by seven and using the first gives

30(2a²−an+n²)=0 in CH²(B).

Thus 2a²−an+n²=0 in CH²(B)_Q and numerically. Claiming this last equality integrally requires an additional torsion argument. No such argument is provided or needed here. The exact line-bundle identity is (det P*)^7 ≅ (U*)^9⊗(V/H)^3, without any preferred isomorphism.

## Correction-defined W and cancellation of U

The global nonzero correction section is equivalently a fiberwise-injective bundle map

L²⊗π*U^(−1) → π*E/L.

Its image K is a line subbundle isomorphic to L²⊗π*U^(−1), not to L²⊗π*U. Take its preimage first in π*E and then in π*H. This defines a global rank-three subbundle W⊂π*H⊂V⊗O_S, whose associated graded factors are π*U, L, and K. Accordingly

det W ≅ π*U⊗L⊗K ≅ L³,
det W* ≅ O_S(3).

The U factors cancel exactly. This construction does not require a globally chosen splitting of H→E. Splitting independence was already used to construct the section of F.

Since W is a subbundle of a constant vector bundle, det W* is globally generated. Hence O_S(3) is globally generated, O_S(1) is nef and semiample, and R* is nef in the standard vector-bundle sense. This does not assert that O_S(1) itself is globally generated.

## Cubic self-intersection and generic finiteness

The projective-bundle pushforward gives

π*(ξ³)=r²−c2(R)=p(n−a)−n²,

where π* in this display denotes proper pushforward. In rational Chow on B, this becomes

π*(ξ³)=(3a²+2n²)/7.

Equivalently, the corresponding equality of intersection numbers holds after taking degrees. Writing ξ³ directly equal to a class on B is shorthand and should be identified as a pushforward or numerical equality.

Both a and n are pullbacks of hyperplane classes via the middle and support maps, so they are nef and have nonnegative self-intersection numbers. If the middle map B→P(V) is generically finite onto a surface, then ∫_B a²>0. It follows that ∫_S ξ³>0.

The map w:S→Gr(3,V) defined by W has w*O_Gr(1)=O_S(3). Thus ∫_S c1(w*O_Gr(1))³=27∫_S ξ³>0. A pullback of an ample line bundle from an image of dimension at most two has zero cube. Therefore dim w(S)=3, and w is generically finite onto its image. This deduction is valid; it does not imply that w is finite, an embedding, or unramified. A merely nonconstant middle map is insufficient to ensure a²>0.

## Scope

These are necessary conditions for an entire complete rank-one surface model. They do not exclude rank-one curves contained in a surface whose generic metric rank is larger, do not alone produce a contradiction, and do not solve the support-extension problem. All computations here are abstract bundle and Chow calculations; no source operation was evaluated.

## Audit addendum: binary quadratic and numerical exclusions

Reviewed the full proof at /research/hm/middle-surface/rank-one-ternary-surface-constraints/PROOF.md, including its later Sections 3 and 4. These additions are valid.

The projection β:Sym²R→T⊗U is splitting-independent because every correction shear on Sym²R lies in R⊗U. If β vanished at a point, the correction there would give a section of (R/L)⊗L^(−2)⊗U on P(R)=P¹. Its degree is three, so it vanishes somewhere, contradicting square avoidance. Thus β is nowhere zero as a binary quadratic.

Its determinant has value line (det R*)²⊗(T⊗U)², and class d=4p−4a−2n; hence 7d=8a−2n exactly in Pic. When the determinant is not identically zero, its effective Cartier divisor has nonnegative intersection with nef a, giving B₁≤4A. Together with B₁=2A+C and C≥0, this is precisely 2A≤B₁≤4A and 0≤C≤2A.

If its determinant vanishes identically, β has constant rank one, so its radical S is a line subbundle and (R/S)²≅T⊗U. On S² the correction projects to a nowhere-zero map to (R/S)⊗U; its shear is killed by projection modulo S. Thus S²≅(R/S)⊗U, yielding 3c1(S*)=p integrally. There is no hidden contradiction in these identities: rationally s=c1(S)=−(3a+n)/7 and t=c1(R/S)=(a−2n)/7, and c2(R)=st combined with 7c2(R)=a²+n² reproduces the same quadratic relation 2a²−an+n²=0.

When A>0, proportionality n=t a would imply (t²−t+2)A=0, which is impossible for real t. This excludes constant H and Picard number one on the smooth complete base carrying the regular flags. The determinant AC−B₁²=−(4A²+3AC+C²)<0 is correct and compatible with Hodge index, not a contradiction to it.

Only presentational suggestions: use π_* for pushforward, and define W directly as the inverse image of K under π*H→π*E/L to avoid unusual extension notation.

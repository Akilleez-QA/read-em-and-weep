# Ambient blowup of the repeated-input cubic slice

## Result and scope

Work over C. Import the canonical trilinear map f:V×V×V→J with dim V=5, its identity f(u,u,u)=0, and the structural theorem f(u,u,w)≠0 for independent u,w. Let

    X=V_u×V_w, a=(u), G(u,w)=f(u,u,w),
    I=(components of G), Z=V(I),
    D=(u_i w_j-u_j w_i), Z_red=V(D).

The preceding repeated-extension-slice theorem proves √I=D, I:a^∞=D, and the scheme-theoretic kernel-line description on u≠0, with arbitrary base change. Let b:B=Bl_{V(a)}X→X, let E be its exceptional Cartier divisor, and write e=O_B(-E)=a O_B.

Then the scheme-theoretic strict transform Y of Z, defined as closure of b^{-1}(Z\V(a)) in B, is

    Y ≅ Tot_{P(V)}(O(-1) ⊕ O(-1)).

It is smooth, irreducible, of dimension six. If K is its ideal in B, then

    I O_B = e² K,             (I O_B):e^∞ = K.

Thus the order-two weak transform equals the strict transform. The entire inverse image W=B×_X Z is not Y: it is the scheme-theoretic union of the doubled ambient exceptional divisor 2E and Y, with ideal intersection

    I O_B = e² ∩ K.

The proper map Y→Z factors through Z_red. Its map to Z_red is an isomorphism away from the total origin (including along u=0,w≠0). Its fiber over the origin is the reduced zero section P(V). Thus it is a small resolution in the birational-geometric sense of having no exceptional divisors: its exceptional locus has codimension two in Y. This terminology does not mean a small or semismall map in the intersection-cohomological dimension-inequality sense. It is not a resolution retaining the nonreduced moduli structure of Z.

The restriction E∩Y is instead Tot(O(-1)) over P(V), a Cartier divisor in Y; it maps onto the whole axis V_w by the usual tautological-line blowdown. It is not the exceptional locus of Y→Z_red. Finally

    ω_Y ≅ p*O_{P(V)}(-3).

This statement makes no assertion about the Q-Gorenstein property of Z_red or a crepant comparison.

## Inputs read and retained qualifications

The local proofs and audit read for this packet are:

- [the repeated extension slice manuscript](../repeated-extension-slice/PROOF.md) and AUDIT.md;
- [the cubic structural nonvanishing manuscript](../../cubic-structural-nonvanishing/cubic-structural-nonvanishing/PROOF.md);
- [the cubic filtered extension obstruction manuscript](../../canonical-cubic-extension/cubic-filtered-extension-obstruction/PROOF.md).

Only their established universal structural and representability conclusions are imported. In particular, the actual graded-framed universal filtered rank-eight bundle exists on the original projective fourfold times Z, including its nilpotent structure. The present argument introduces no source/model computations or evaluations.

Standard terminology is consistent with the Stacks Project definitions of [strict transform](https://stacks.math.columbia.edu/tag/080D) and [blowup and exceptional divisor](https://stacks.math.columbia.edu/tag/01OF). The ideal equalities and all conclusions specific to this cubic are proved below, rather than imported from those references.

## 1. The ambient blowup and its universal tautological description

Put P=P(V), L=O_P(-1), and Q=(V⊗O_P)/L. The blowup B is the incidence scheme

    B={ (ell,u,w): u∈ell } = Tot_P(L ⊕ (V_w⊗O_P)).

Indeed, the Rees blowup of the origin in V_u is Tot_P(L), and formation of this blowup commutes with the flat product with V_w. Equivalently its standard affine charts have u=t v, with one coordinate of the universal vector v normalized to one. This is a universal coordinate identity, not a choice of an input to f. The map b forgets ell, and E is u=0, the zero section in the L direction. In particular E=P×V_w and its ideal is invertible.

Trilinearity and the diagonal identity define the global bundle morphism

    β:L^{⊗2}⊗Q → J⊗O_P,
    l_1⊗l_2⊗(w mod L) ↦ f(l_1,l_2,w).

It is well-defined: l_1,l_2 lie in the same line, so replacing w by an element of L adds a multiple of f(l,l,l), identically zero. This identity is independent of a local trivialization. The morphism β is a locally split injection with locally free cokernel. One way to see this without any new fiber computation is to pull it back to the faithfully flat G_m torsor V\{0}→P; the universal nonzero vector trivializes L there, and β becomes the split quotient injection established in the preceding repeated-extension-slice theorem. A map of vector bundles being a subbundle injection descends faithfully flat locally. Consequently β remains injective and locally split under every base change.

## 2. Global factorization of the ideal

Pull all these bundles to B. The universal w has quotient section q in p*Q. Let K be the component ideal of q. Its zero scheme is

    Y_0=Tot_P(L⊕L) ⊂ Tot_P(L⊕(V⊗O_P)).

In a local generator v of L, write u=t v. The universal identity is

    b*G=t² f(v,v,w).

The component ideal of f(v,v,w) is precisely K, because the map β in this trivialization is locally split: a local left inverse recovers the quotient coordinates q, while the components of β(q) are linear combinations of them. Thus I O_B=(t²)K in each such chart. Changing the generator of L multiplies t and the divided equations by reciprocal units, so these identities glue to I O_B=e²K.

This argument proves ideal equality, not merely equality of supports. All the local split-quotient equalities are stable under arbitrary base change. It does not assert that scheme-theoretic closure commutes with every nonflat base change.

The exceptional order is exactly two. Locally one may split V⊗O_P=L⊕Q and choose polynomial fiber coordinates s,q_1,...,q_4 for w. Then B has regular coordinates over a smooth chart of P consisting of t,s,q_1,...,q_4, and K=(q_1,...,q_4). In particular K is not contained in (t), so I O_B is not contained in e³. This is a statement about universal ideals and contains no selected input or jet evaluation.

## 3. Strict transform, weak transform, and total inverse image

We use the scheme-theoretic strict transform convention: take the closure in B of the restriction of Z to X\V(a), using the scheme structure of that restriction. On a chart where e=(t), its ideal is the contraction from t inverted,

    ker(O_B → (O_B/I O_B)[t^{-1}])
      =(I O_B):(t)^∞.

The coordinate description above shows t is a nonzerodivisor on O_B/K. Hence K:(t)^∞=K, and (t²K):(t)^∞=K. Therefore Y=Y_0. In particular all original nilpotent structure disappears in this strict transform because it was supported on the center: the strict transforms of Z and Z_red coincide. A different convention that calls the full inverse image a transform would yield a different scheme.

For precision, the order-two weak transform is the divided ideal e^{-2}(I O_B), viewed as an ideal of O_B. It equals K. This specifies the convention; no assertion about other uses of the phrase weak transform is needed.

The total inverse image has ideal t²K. Since multiplication by t is injective on O_B/K,

    (t²)∩K=t²K.

This gives W=2E∪Y as a scheme-theoretic union. Moreover, locally the two ideals (t²) and K are primary and prime, respectively: O_B/(t) and O_B/K are polynomial rings over the integral smooth affine chart of P. The two components are incomparable. Thus this primary decomposition has exactly these two associated components, and no additional embedded component at E∩Y. This description concerns the total inverse image W in the smooth ambient blowup; it does not determine a primary decomposition of the original I on X.

The intersection 2E∩Y is the Cartier double of E∩Y inside Y, with ideal (t²) there. The reduced intersection E∩Y has ideal (t) in Y and equals Tot_P(L_w). In particular retaining the full total transform would retain a thick exceptional component rather than give a smooth scheme.

## 4. The proper map and exactly what it contracts

The map r:Y→X sends (ell,u,w), with both u,w∈ell, to (u,w). The determinantal equations vanish universally, so r factors scheme-theoretically through Z_red and hence through Z. It is proper because Y is closed in the projective X-scheme B. The induced map to Z_red is likewise projective.

On the open subset of Z_red where u_i is invertible, the inverse chooses ell=[u]. On the open subset where w_j is invertible, the inverse chooses ell=[w]. The determinantal equations ensure that the other vector belongs to the selected line as an equality of schemes, not just of closed points. On chart overlaps the two line choices agree. These opens cover Z_red minus the total origin, proving that r is an isomorphism there, including the nonzero part of the u=0 axis. We do not claim an isomorphism to the nonreduced Z on that axis.

The scheme-theoretic fiber over the origin has u=w=0 in the two tautological lines, so it is precisely the reduced zero section P. Since dim Y=6 and dim P=4, this fiber has codimension two; r is a proper birational morphism from a smooth variety with no exceptional divisors. This is the asserted small resolution of Z_red in the birational-geometric sense (a resolution with no exceptional divisors). The stronger intersection-cohomological notion of a small map does not hold: the origin has codimension six in Z_red, while twice its fiber dimension is eight. In fact the map is not semismall either. It is not an assertion that the ambient blowup has no exceptional divisor.

Indeed E∩Y is the divisor where the first tautological vector vanishes. Its restricted map to the axis V_w is Tot_P(L)→V, the blowup of its origin. It is an isomorphism over w≠0 and contracts only its own zero section P over w=0. Although every point of E∩Y lies over the ambient blowup center, only that zero section lies in the exceptional locus of r:Y→Z_red.

## 5. Canonical bundle

For the total space of a vector bundle F on a smooth base P, the cotangent sequence gives

    ω_{Tot(F)} ≅ p*(ω_P ⊗ (det F)^{-1}).

Here F=L⊕L, det F=O_P(-2), and ω_P=O_P(-5), whence ω_Y=p*O_P(-3). This computes a line bundle on the smooth source only. A crepant or noncrepant conclusion would require separate hypotheses and comparison on the target, which are not supplied or inferred.

## 6. Pullback of the actual universal filtered family

Let E_univ be the imported actual algebraic graded-framed filtered rank-eight bundle on the original projective fourfold times Z. The map r:Y→Z pulls it back to an actual algebraic filtered bundle on that fourfold times Y. Its adjacent classes are (u,u,w), now with u and w sections of the same tautological line on Y. Algebraicity and all graded framings are preserved by pullback; no division of transition functions by t, limiting procedure, or pointwise choice of primitives is involved. The same universal family pulls back to W=B×_X Z, including its double exceptional component. It does not pull back to all of B via a map to Z, since B does not generally factor through Z.

The affine-base representing theorem extends this interpretation to Y by pulling back its actual family, or by affine-local representability and unique framed descent. Every map T→Y, including a nonreduced test scheme, supplies a filtered family. Equivalently such a map specifies a line subbundle ell⊂V⊗O_T together with two sections u,w of ell; the induced cubic vanishes identically. This is more restrictive than arbitrary maps T→Z, and even more restrictive than arbitrary maps T→Z_red unless the additional line data exist. It must not be advertised as a replacement representing the original functor.

The family on the zero section is the pullback along the constant map to the origin of Z. Hence its filtered isomorphism class is constant there, even though the resolution remembers the distinct possible lines. This expresses what is forgotten under the contraction without claiming to recover nilpotent extension directions of Z.


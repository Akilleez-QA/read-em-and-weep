# Three-channel monad family: subbundle torus, transitivity, and isotropy

Work over C. This note supplies the three-channel dependency used by the normal-quadratic and Serre-residue arguments. It proves a universal structural statement from the existence and equivariance of the actual Horrocks–Mumford monad. No actual coefficients or selected fibers are evaluated.

## Inputs and conventions

Let G=SL2(F5), let H=V⊕W be the five-dimensional space of linear coordinate functions, and put P=P(H*). Here V is the positive irreducible three-dimensional representation, W is a negative irreducible two-dimensional representation, W′ is the other two-dimensional representation, and A=Sym²W. Set N=A⊕W′ and K=Ω²_P(2).

The established actual equivariant monad is

    N O(-1) --α--> W′ K --α†--> N* Δ,
    Δ=det(H).

Its left arrow is everywhere a subbundle inclusion, and its middle cohomology is the locally free normalized HM bundle. The alternating form on W′K is the alternating form on W′ times the symmetric exterior pairing on K, with value Δ O(-1). The right arrow is its adjoint. All identifications of irreducible channels below are fixed once; rescaling those identifications merely changes the scalar parameters by nonzero constants.

The representation identities used are

    Λ³H = Λ³V ⊕ (Λ²V⊗W) ⊕ (V⊗Λ²W)
         = 1 ⊕ T6 ⊕ V,
    W′⊗T6 = A ⊕ P4 ⊕ D5,
    W′⊗V = W′ ⊕ S4,
    Sym²W′ = V.

The letters P4,D5,S4,T6 denote irreducibles of their indicated dimensions; the two three-dimensional irreducibles A,V are distinct. Determinants of representations of the perfect group G are trivial. Constant determinant lines must nevertheless be retained for block coordinate scalings.

Public pinned inputs:

- The actual monad and its end exactness: [twist-one structural vanishing, commit8cbbe482ee50c35d52ffcdf3efb837fa8cf96af4](https://github.com/Akilleez-QA/read-em-and-weep/blob/8cbbe482ee50c35d52ffcdf3efb837fa8cf96af4/research/hm/twist-one-structural-vanishing/PROOF.md).
- The actual G-coefficient representations, exterior decomposition, contraction convention, and b-channel exclusion: [negative invariant scalar, commit78053cfaec46a334c8714da084948356e467259e](https://github.com/Akilleez-QA/read-em-and-weep/blob/78053cfaec46a334c8714da084948356e467259e/research/hm/order-four-quadratic-load/NEGATIVE-MONAD-INVARIANT-SCALAR-IS-NONZERO.md).
- The determinant-valued self-duality and parameter-weight conventions being resolved here: [universal b-square coefficient, same commit](https://github.com/Akilleez-QA/read-em-and-weep/blob/78053cfaec46a334c8714da084948356e467259e/research/hm/order-four-quadratic-load/NORMAL-QUADRATIC-COEFFICIENT-UNIVERSAL-B-SQUARE.md).

## 1. Exactly three coefficient channels

The exterior Euler sequence gives H0(K(1))=Λ³H. Therefore

    Hom_G(N O(-1),W′K)=Hom_G(N,W′⊗Λ³H).

By the displayed decompositions, the W′ source occurs once in W′⊗Λ³V and once in W′⊗V⊗Λ²W. The A source occurs once in W′⊗Λ²V⊗W and nowhere else. Thus this Hom space is three-dimensional. Write its elements α(a,b,c), with channel conventions

    a: W′ -> W′⊗Λ³V,
    b: W′ -> W′⊗V⊗Λ²W,
    c: A  -> W′⊗Λ²V⊗W.

Each unlisted source summand is sent to zero by that channel. In particular a and b have the same W′ source, whereas c has the A source.

## 2. Every everywhere-injective arrow has abc≠0

First c=0 annihilates the entire A source, so cannot be fiberwise injective.

If b=0, the W′ source maps only through Λ³V. A section represented by a three-form ω evaluates at [x]∈P(H*) by contraction ι_xω. For every x in W* the contraction of Λ³V is zero. Hence the W′ source fiber is killed along the whole negative line P(W*). This is a universal contraction identity, not an evaluation of an actual monad matrix.

It remains to exclude a=0. We may assume b≠0 by the preceding paragraph. On the positive plane P(V*), the restriction of the W′ source is entirely the b-channel. After choosing a nonzero generator of Λ²W, contraction is the linear family

    T(x): W′ -> W′,  x∈V*.

The nonzero equivariant coefficient inclusion W′→W′⊗V identifies the associated map V*→End(W′) with the unique V-summand in End(W′). Since End(W′)=1⊕V, that summand is sl(W′). Thus T is a linear isomorphism V*→sl(W′), up to a nonzero scalar. This establishes the full abstract pencil, without choosing its actual coefficient b.

The determinant on the three-dimensional space sl(W′) is a nonzero homogeneous quadratic with nonempty projective zero locus over C. For example the entire abstract nilpotent cone lies in that zero locus. Consequently there is a nonzero x∈V* for which T(x) is singular. For a nonzero vector z in its kernel, contraction of the b-channel at x kills z, and the a-channel is absent. Since z is in the W′ source summand, the c-channel does not act on z. Therefore α(a,b,c) is not injective at [x].

This is a structural exclusion over the entire positive plane, not a choice or evaluation of a distinguished actual HM/source-instance point. We conclude that any subbundle arrow has abc≠0. In particular the already existing actual monad has all three parameters nonzero.

## 3. Gauges and block changes act transitively on the nonzero torus

Rescale the W′ source by s and the A source by r. Precomposition sends

    (a,b,c) -> (sa,sb,rc).

For the adjoint monad this is a chain isomorphism, using inverse source rescaling on the left, identity in the middle, and the dual rescaling on the right.

A coordinate pullback scaling V by λ and W by μ acts on the three exterior-form blocks with weights

    (a,b,c) -> (λ³a, λμ²b, λ²μc).

These are the coordinate-function pullback conventions of Section1. The natural exterior pairing transforms with its determinant factor Δ, so pullback preserves the self-dual monad condition. No determinant character is being discarded.

For any two triples (a,b,c) and (a′,b′,c′) with all entries nonzero, take λ=1 and choose μ∈C* with

    μ²=(b′/a′)/(b/a).

After this coordinate change choose source gauges

    s=a′/a,  r=c′/(μc).

Their composite sends the first triple to the second. Therefore (C*)³ is one orbit under source gauges and block coordinate pullbacks. The square root is harmless over C and no actual coefficient is determined by this argument.

## 4. Isotropy and the exact subbundle locus

One point of (C*)³ is the actual monad, by Section2. Every other point of that torus is its pullback and gauge transform by Section3. Such transformations preserve fiberwise injectivity and isotropy. Thus every α(a,b,c) with abc≠0 is isotropic and a subbundle inclusion.

For a nondegenerate alternating form on a rank-twelve bundle, the adjoint of a rank-five subbundle inclusion is onto. Isotropy places its image in the kernel of that adjoint, and the rank-two quotient is locally free. Thus every triple in (C*)³ defines a genuine self-dual monad with a rank-two bundle as middle cohomology.

Together with Section2 this proves that the everywhere-subbundle locus in the entire three-dimensional coefficient space is exactly abc≠0, not merely an unspecified nonempty open subset.

There is also a useful extension of the isotropy assertion. The composite α†α is quadratic polynomial in (a,b,c), with values in a fixed finite-dimensional space of bundle homomorphisms. It vanishes on the Zariski-dense torus (C*)³, hence identically on C³. All three-channel arrows are isotropic, including degenerate boundary triples. Only the nonzero torus gives the required subbundle monads; isotropy at a boundary point does not repair the failed injectivity.

## 5. Consequences and limits

This supplies precisely the family, nonvanishing, and transitivity inputs needed by the b-square weight argument. For negative-coordinate scaling with λ=1, the source-gauge invariant ratio transforms as

    a/b -> μ^(-2) a/b.

In particular μ²=-1 changes this nonzero ratio to its negative. Using it to distinguish bundle isomorphism classes additionally requires the strong-exceptional-monad reconstruction argument; transitivity here is under coordinate pullback as well as gauge, not under isomorphism over the identity of P.

The result alone does not evaluate the normal quadratic cup constant κ, the positive cubic Bockstein, or any selected source-instance obstruction. It proves no algebraicity claim. The proof is structural mathematics, not formal verification or a numerical certificate.

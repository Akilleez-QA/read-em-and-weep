# The actual target raises canonical-line residual rank to six

## Statement and inputs

Use the hypotheses of the canonical-line parity and rank-five-strengthening proofs, together with the actual target representation

    J=A* tensor Sym^3 W_0,
    Lambda^2 V=A tensor W_0,

established in `../../cubic-loci/canonical-cubic-extension/cubic-massey-module-reduction/PROOF.md`. Here W_0 is the two-dimensional binary-icosahedral representation occurring in those identities. To avoid conflating two generally inequivalent two-dimensional representations, write W_v for the canonical negative subspace of V. Thus

    V=T direct sum W_v,

and the canonical central involution c is positive on T and negative on W_v. Both W_0 and W_v have determinant one and negative central involution. The three-space T is irreducible, and the established parity proof gives

    Lambda^2 T=T,
    Sym^2 T=1 direct sum P_5,

where P_5 is the irreducible five-dimensional A_5 representation.

**Conclusion.** At every point of every canonical negative line, both parity blocks of b have rank at least five. Hence rank b is at least ten and residual rank Q is at least six. Furthermore, every projective line meeting a canonical negative line contains at most two distinct points of Z3.

These are universal representation and determinantal statements. No actual source operation, coefficient, or rank instance is evaluated.

## 1. The positive target has no P_4 constituent

Restrict the identity Lambda^2 V=A tensor W_0 to the binary-icosahedral complement. Its positive c-parity part is

    A_- tensor W_0
      = Lambda^2 T direct sum Lambda^2 W_v
      = T direct sum 1.

In particular dim A_-=2. The invariant line on the right implies

    Hom(W_0*,A_-) is nonzero.

Since W_0 is irreducible and both spaces have dimension two, A_-=W_0*. The determinant-one property identifies W_0* with W_0. Therefore the same tensor identity, or the decomposition W_0 tensor W_0=Lambda^2 W_0 direct sum Sym^2 W_0, gives

    Sym^2 W_0=T.

The factor Sym^3 W_0 in J is c-negative. Consequently

    J_+=(A_-)* tensor Sym^3 W_0
        =W_0 tensor Sym^3 W_0
        =Sym^4 W_0 direct sum Sym^2 W_0.

The last equality is the characteristic-zero Clebsch-Gordan identity for a determinant-one two-space, restricted to the complement. Also

    Sym^2(Sym^2 W_0)=Sym^4 W_0 direct sum 1.

Comparing this with Sym^2 T=1 direct sum P_5 and cancelling the trivial summand in the semisimple representation category proves

    J_+=P_5 direct sum T.

In particular J_+ has no P_4 constituent.

## 2. The canonical even block has rank at least five

The canonical-line parity theorem proves that the even block has constant rank at least four on P(W_v). Section 4 of `../../rank-four/canonical-line-rank-five-strengthening/PROOF.md` proves the following necessary configuration for its remaining rank-four case:

    I_+=P_4 tensor O,

where I_+ is its equivariant image subbundle. Thus rank four would require an injective representation map P_4 to J_+. Section 1 excludes such a map. Therefore the even rank is at least five.

The odd block already has rank at least five by the main theorem of that same strengthening proof. Their complementary target parity spaces give

    rank b >= 5+5=10,
    rank Q=rank b-4 >=6

at every point of P(W_v). Normalizer equivariance propagates the conclusion to all twenty-five canonical negative lines. In particular all these lines avoid Z5, and therefore also Z3.

## 3. An arbitrary meeting line contains at most two rank-three points

Let U be any two-dimensional subspace of V such that P(U) contains a point p on a canonical negative line. The universal binary-image lemma in `../order-three-rank-point-bound/PROOF.md` gives a fixed two-dimensional subspace H_U of J and a linear quotient pencil

    B_U: O(-1) tensor (Sym^2 V/Sym^2 U)
         -> (J/H_U) tensor O,

with rank B_U(u)=rank b_u-2 at every point of P(U).

At p the new bound gives rank B_U(p)>=8. Hence some eight-by-eight minor is a nonzero homogeneous polynomial of degree eight on P(U). At each point q in Z3 intersect P(U), rank B_U(q)<=5, so every eight-minor vanishes to order at least three there. This is the usual determinantal order inequality over the local discrete valuation ring.

If n is the number of distinct points of this intersection, then

    3n<=8,

and therefore n<=2. The argument applies to any projective line meeting a canonical negative line, without requiring an order-three symmetry or a parity-paired intersection. If the two lines coincide, the intersection with Z3 is empty by Section 2.

## Boundary

This strengthens the canonical-line rank bound and the arbitrary-meeting-line point bound. It does not exclude the remaining possible paired rank-three points on an order-three fixed line, determine any actual coefficient, or establish that any rank-three point exists. The only new write is this local proof artifact.

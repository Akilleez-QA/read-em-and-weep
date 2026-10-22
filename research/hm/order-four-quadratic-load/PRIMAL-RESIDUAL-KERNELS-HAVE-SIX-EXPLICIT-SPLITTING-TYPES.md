# Primal residual kernels have six explicit splitting types

## Result and scope

After PR740 (commitc25a926443724c0643f63f840746bde5a0502670), the five surviving ordinary residual quotient families have exactly the kernel splittings below. Write N=ker[Z -> O(2)+O(-8)]=K/C7 and use the scalar coordinates of PR737. These classifications retain every scalar stratum on which the equivariant bundle isomorphism type changes.

- Z1: N=S O(-3)+O(-8)+O(-10).
- Z2: N=D O(-4)+O(-10).
- Z3 with a!=0: N=S O(-3)+W O(-9).
- Z3 with a=0 (so b!=0): N=S O(-3)+O(-8)+O(-10).
- Z4: N=D O(-4)+O(-10).
- Z5 with alpha*beta!=0: N=T O(-5).
- Z5 with alpha=0, beta!=0: N=V O(-4)+V O(-6).
- Z5 with beta=0, alpha!=0: N=P O(-4)+Wp O(-7).

There are eight scalar strata and six distinct kernel bundle types, each of rank6 and degree-30. These classify ordinary quotient kernels, not their compatibility with every later Gauss stage. No new label or scalar exclusion is made here, and no connection is assigned to N.

## 1. Full evaluation kernels and removable corrections

For the standard binary representation, full degree-m evaluation has the exact equivariant sequence

    0 -> Sym^(m-1) W O(-j-1)
      -> Sym^m W O(-j) -> O(m-j) -> 0.             (1)

At a parameter point, forms vanishing there form the corresponding tautological line times Sym^(m-1) W, proving (1) directly.

In Z1, the nonzero lower row on 2 O(-8) removes one copy. The upper alpha component is full degree-four evaluation D O(-2) -> O(2), whose kernel is S O(-3). The beta correction from O(-10) lifts through this evaluation: its obstruction lies in H1(S O(7))=0. Averaging gives an equivariant lift. A triangular source automorphism therefore removes beta, leaving the first splitting above and the unused O(-8).

The same argument for Z2 uses full degree-five evaluation T O(-3) -> O(2), with kernel D O(-4). Its O(-10) correction lifts because H1(D O(6))=0.

For Z3, alpha is nonzero by PR740. If a!=0, the lower row splits off O(-8), leaving D O(-2)+W O(-9) as its kernel. The upper correction from W O(-9) lifts through the D evaluation since Ext1(W O(-9),S O(-3))=H1(W* tensor S O(6))=0. If a=0, the nonzero lower W O(-9) -> O(-8) is full linear evaluation, with kernel O(-10); the lower kernel is then D O(-2)+O(-8)+O(-10). The previous lifting argument removes its upper correction. This proves both Z3 strata.

For Z4 the lower full linear evaluation leaves T O(-3)+O(-10), and the Z2 argument applies. All these operations are bundle automorphisms, not changes to or splittings of an ambient connection.

## 2. The three Z5 strata

The nonzero lower row splits off O(-8), leaving

    (V+P) O(-4) -> O(2).

Since V+P=Sym6 W, when alpha and beta are both nonzero an equivariant diagonal automorphism of its two irreducible summands turns the map into full degree-six evaluation. Equation(1) gives N=T O(-5).

Suppose alpha=0. The V O(-4) summand is killed, and it remains to compute the kernel of P O(-4) -> O(2). The full evaluation sequence is

    0 -> T O(-5) -> (V+P) O(-4) -> O(2) -> 0.

Projecting its kernel to V O(-4) is surjective because P O(-4) -> O(2) is surjective, as proved by the low-degree invariant-divisor argument in PR737. Moreover Hom_G(T O(-5),V O(-4)) is one-dimensional: W tensor V=T. Hence that projection is a nonzero scalar multiple of V tensored with the standard linear evaluation W O(-5) -> O(-4). Its kernel is V O(-6). Thus N=V O(-4)+V O(-6).

Suppose beta=0. The P O(-4) summand is killed. Let M be the kernel of the surjective V O(-4) -> O(2). It has rank2 and degree-14. At twist5 the section map is a nonzero map

    V tensor W=T -> Sym7 W=Wp+T,

so it is injective and H0(M(5))=0. Thus each ordinary splitting degree of M is at most-6. Given rank2 and degree-14, this bounds h0(M(6)) by1. But H0(M(6)) is a subrepresentation of V tensor Sym2 W=P+D, which has no nonzero subrepresentation of dimension at most1. Therefore H0(M(6))=0 and M is balanced: M=R O(-7) for a two-dimensional coefficient representation R.

Now H1(M(7))=0, so the twist-seven section sequence computes

    R=V tensor Sym3 W - Sym9 W
     =(Wp+S+T)-(S+T)=Wp.

Consequently M=Wp O(-7), proving the final stratum without choosing or evaluating an actual covariant.

## Reproduction and limits

Run verify_primal_residual_kernel_splittings.py. It pins the published residual quotient and strict-slope packages, verifies all rank/degree identities, scalar strata, the finite Ext1 vanishing degrees, and the character identities in the two evaluation-kernel arguments using an independent integer McKay recurrence. It also enumerates the only rank-two degree-14 ordinary splitting possibilities compatible with H0(M(5))=0 and checks the dimension bound used above.

The proof classifies all kernel bundles of the five necessary quotient families. Later Gauss compatibility remains separate; no quotient connection, realization, whole-profile closure, actual-instance computation, or quotient-label exclusion is asserted.

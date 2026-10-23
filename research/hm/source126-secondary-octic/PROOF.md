# The secondary radical test is identically blind to the octic line

## Universal statement and conditional consequence

Let A=Sym²W, D=Sym⁴W, X=P(A), and let b_T be the universal nonzero multiplication D O(-1)→P O with kernel κ:O(-5)→D O(-1), as pinned in PR982. Write ρ(a)h={a,h}_1. Then for EVERY equivariant quartic covector ψ(a):D→C,

    ψ(a)ρ(a)κ(a)=0 identically.                         (1)

Thus the secondary restriction on the two-dimensional quartic covector space is the ZERO map. This is a universal representation identity, not vanishing at any selected actual parameter.

Under the actual full-J Type II hypotheses of PR980, suppose the lower internal symbols2 through7 vanish and the internal eighth has rank-one form r8=α σψ4, with σ:O(-4)→E and ψ4 an equivariant quartic covector. Then secondary-chain-map naturality does give

    ν r8ρ(a)κ=0:O(-13)→E,                              (2)

but (1) makes this constraint automatic for EVERY α and ν. Consequently this secondary test cannot select the octic scalar, even conditional on ν≠0. This does NOT prove the scalar is nonzero or realized; it identifies exactly why this proposed elimination fails. No original or internal symbol is claimed newly zero by (2).

PR995 at commit f9435fa37c78e86391fd1a773a039dd646a05e53, research/hm/source126-typeII-internal-octic-gate/PROOF.md, proves the lower internal vanishings and the canonical octic line under the same full-J Type II hypotheses. Thus these are now retained conditional theorems, not speculative premises. PR980, PR982, PR995 and the public universal projection are pinned in INPUTS.json. No actual HM coefficient, point, parameter or instance matrix is evaluated.

## 1. The degree-nine invariant obstruction

In homogeneous parameter coordinates, κ has degree4, because it is the signed-minor vector of the linear4×5 quotient multiplication matrix. Its equivariant linearization carries no character: A5 has no nontrivial one-dimensional characters. The map ρ has degree1 in a and a quartic covector has degree4. Therefore their scalar composition in (1) is an invariant homogeneous polynomial of degree9 on A.

The precise invariant space is

    (Sym⁹ A*)^G = (Sym⁹ A)^G = 0.                       (3)

This is a symmetric power of the THREE-dimensional parameter representation, not Sym⁹W. One exact way to compute it is the SL2 plethysm

    Sym⁹(Sym²W)=Sym¹⁸W⊕Sym¹⁴W⊕Sym¹⁰W⊕Sym⁶W⊕Sym²W.

The fixed binary-icosahedral McKay recurrence gives no trivial constituent in any of those five summands. The bounded checker computes all five multiplicities separately and their sum. Hence (3) proves (1) without selecting coefficients or relying on a generic rank guess.

In particular the zero restriction holds on the ENTIRE quartic covector space, which has dimension [D:Sym⁴A]=2, not only on the particular κ-annihilating line. The similar quadratic row c(a)(h)=<a²,h> also annihilates ρκ; that scalar has degree7, whose invariant space vanishes as well. Its direct conceptual identity is <a²,ρ(a)h>=−<ρ(a)a²,h>=0, since ρ(a)a²=0.

## 2. Why higher naturality gives precisely (2)

PR980 constructs, for each FIXED a, a secondary chain map K_a:T→S for the SAME whole family Q+tT_a. Its induced Q-cohomology maps are

    k0,a=(0,νρ(a)):D→A+D,       k1,a=0:P→D.

On the dense open where b_T,a is onto, every vector κ(a) lifts to a formal quotient kernel through every finite order: after cancelling Q-unit pairs, the remaining quotient differential is t times a matrix with surjective leading term, and each correction equation can be solved recursively. Apply K_a to a quotient lift through order eight. This produces an S lift with initial Q-class νρ(a)κ(a). If all internal symbols below eight vanish, its eighth obstruction is exactly r8 applied to that initial class, independent of the chosen corrections. Since the quotient lift and K_a give an actual lift, this class is zero. Thus (2) holds on the dense open and extends as an equality of regular bundle maps.

This argument does NOT assert higher naturality on all of D or that K_a commutes with T_b for b≠a. It uses precisely the actual quotient first-cycle line. The grading is 4+1+8=13, so its global form is O(-13)→E. For r8=α σψ4 the scalar factor in that composite has degree4+1+4=9 and is zero by (3). Multiplication by the nonzero section σ cannot turn this zero identity into a constraint on α.

## 3. Independent exact coefficient certificate

To make the zero test reproducible independently of (3), use the authenticated universal P6 projection in INPUTS.json and its three-dimensional kernel V6. Let f12 be the homogenized Wronskian of a kernel basis, using derivative orders0,1,2. The Wronskian transforms by det(V6), which is trivial, so f12 is G-invariant. In the normalization reproduced by the checker, z=√5 and

    f12=−2x12−(44z/5)x10y2+66x8y4+(88z/5)x6y6
         +66x4y8−(44z/5)x2y10−2y12.

For degree d forms F=ΣF_i x^(d-i)y^i and H=ΣH_i x^(d-i)y^i, use the normalized apolar pairing

    <F,H>_d=Σ(-1)^i F_i H_(d-i)/binom(d,i).

Define the equivariant quartic covectors

    C(a)(h)=Δ(a)<a²,h>_4,
    B(a)(h)=<f12,a⁴h>_12,
    Δ(p x²+qxy+t y²)=q²−4pt.

They form a basis of the two-dimensional covector space. Indeed C is nonzero, while B is not divisible by Δ: its universal polynomial coefficient at a=x²,h=y⁴ is2/15. This is a coefficient identity on the abstract binary-form representations, not an actual HM direction evaluation.

On the dense formal monic chart a=x²+qxy+t y², with q,t left algebraically independent, let κ be the signed4×4-minor vector of the universal4×5 quotient matrix. Exact coefficient comparison yields

    Bκ=−(64√5/175) Cκ,
    Cρ(a)κ=0,
    Bρ(a)κ=0.                                           (4)

Furthermore Cκ is not zero. Hence the nonzero covector

    Ψ=B+(64√5/175)C

spans the unique κ-annihilating covector line. In any setting where the canonical ψ4 is defined as the nonzero κ-annihilating quartic row, Ψ and ψ4 differ by a nonzero constant. Equations (4) therefore check the exact same octic row, not an unrelated similarly sized map. Equality of polynomial coefficients on the dense chart proves global equality of these homogeneous maps.

The checker also authenticates the public projection, checks the Wronskian degree and its invariance in the stated representation convention, verifies the signed-minor kernel identity, and computes (3) by McKay recurrence. No symbolic parameter q,t is assigned a value in this certificate.

## Boundary and next missing premise

The sought implication ν≠0 ⇒ r8=0 does NOT follow from secondary naturality: its restriction map is forced to vanish by absence of degree-nine invariants. A different actual-complex relation, or a different independently derived test, is required to select α. No repeated unresolved blocker is counted as progress: the new checked result is the exact zero restriction, its representation-theoretic cause, and an independent normalized universal polynomial certificate.

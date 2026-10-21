# Independent review: colored exterior-shadow bounds

Reviewed proof: PROOF.md, SHA256 66addbd9dd64be8e9ee9095a525b539a4f86577776b2af922124ed9d6097a6a8.

## Verdict

PASS, conditional on the explicitly pinned actual-family inputs. The new arguments prove y <= 315, x <= 610, and 9x <= 20y. These are necessary restrictions on residual dimensions, not exact determinations or geometric lifting claims. This is independent mathematical review, not formal verification.

## Leading terms and incidence count

Fix a coefficient basis of B once for every exterior degree. Ordering first by coefficient color and then by indicator-vector lexicographic order has the needed deletion compatibility: for two sets containing j, their first unequal indicator coordinate is not j and remains the first unequal coordinate after deleting j. Distinct terms containing j have distinct contractions. Thus the leading coefficient of the contracted leading term cannot cancel. Terms not containing j vanish. Coefficient colors do not change.

For a vector subspace, its possible leading basis monomials are precisely its echelon pivot monomials, so their number equals its dimension. Contraction closure therefore places every colored lower-shadow monomial among the lower space's pivots. Each selected p-set contributes p different edges, and each colored (p-1)-set receives at most N-p+1 edges. This proves p dim W_p <= (N-p+1) dim W_(p-1). The lemma itself works over every field, with no division by p needed.

## Correct family and degree conventions

The fixed spaces W_p(n)=H^0(Z_(p,2p+1)(n+p)) all embed in T tensor Sym^n(G) tensor Lambda^p(U). Removing one exterior generator lowers S-degree by two and the sheaf parameter twist by one; the displayed n+p convention leaves the same coefficient space. Exterior contractions anticommute with the column Koszul differential, so cycle contraction closure is valid. Keeping the twist fixed instead would not give this argument.

The pinned bridge at commit eaebbcad2b1cf0ad1e83e12bb33c380bae00a0fb was fetched directly from its public path research/hm/column-koszul-bridge/PROOF.md and agrees with the inspected local bridge (SHA256 7b388da8bffd768a79e74eb73c7d1c89669f04a0cdcbd256d7282db556b76c3c). Its Section 3 supplies x=h^0(Z_(3,7)(8)), y=h^0(Z_(2,5)(8)); Sections 3-4 supply E into 100O(-3) plus 50O(-7). It explicitly pins the L splitting to PR511 commit 55bc80b2cb660edd741c93747df7304ee51a061e and the actual complementary duality to PR507 commit 87c9b317bd4b1116e63212a6d7ec2730486b2032 and PR508 commit a59d3dbfdad8b5516cd17c91890b669f2567bdb7. This review verifies that the present proof uses precisely those statements and conventions; it does not reprove the full historical dependency chain.

## Arithmetic and stronger vertex bound

The splitting L=10O(-2) plus 5O(-6) gives dim W_1(5)=55 and dim W_1(6)=70. Therefore 2y<=9*70=630 and x<=12*55=660 as an intermediate bound.

Iterated contractions of a leading triple produce all its colored vertices. If r_a is the number of vertices of color a, then 0<=r_a<=10 and their sum is 55. Hence x<=sum binom(r_a,3). For 1<=a<=b<10, transferring one vertex from a to b changes this sum by binom(b,2)-binom(a-1,2)>=0. Repeating fills colors to ten and leaves at most one partial color, giving five colors of size ten and one of size five. Thus x<=5*120+10=610. This is valid without any direct-sum decomposition of the original cycle space by colors.

The injection for E excludes splitting degrees greater than -3, because any such summand has zero Hom to the entire target. For b<=-3, max(b+8,0)<=(5/6)max(b+9,0), including the zero-section cases. Consequently 3x<=8h^0(E(7))<=8*(5/6)y, equivalently 9x<=20y. Compared with 3x<=25y, the coefficient improvement is indeed 4/15.

## Scope and remaining work

No selected actual HM/source-instance coefficients, matrices, ranks, numerical evaluations, or searches were used. No flatness or relative perfect-pairing assumption enters these new bounds. Exact alternating cycle dimensions and any subsequent geometric or algebraicity consequences remain unresolved. No mathematical correction is required. The final editorial revision adding exact public dependency hyperlinks and replacing the pending-review sentence was inspected in full. Its mathematics is unchanged, and the reviewed proof hash above pins this final revision.

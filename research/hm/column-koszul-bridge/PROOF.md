# Column Koszul hypercohomology and bounded middle defects

## Scope and dependencies

Work over a field of characteristic zero. Put S=Sym(T), dim(T)=5. Let U have dimension ten and G have dimension two. The fixed quadratic presentation is a map phi: U tensor S(-2) -> G tensor S. Set P=P(G*) with the convention H^0(P,O(n))=Sym^n(G) for n>=0. The moving column is the composite U tensor S(-2) tensor O(-1) -> S tensor O. Write K for its sheaf Koszul complex, with K_p=Lambda^p(U) tensor S(-2p) tensor O(-p), in homological degree p. A subscript d denotes S-degree d.

Inputs already established for this family:

1. Every column quotient has Hilbert function (1,5,5); the ten quadrics are linearly independent, and the cube of the irrelevant ideal annihilates the quotient. Source: PR511, commit 55bc80b2cb660edd741c93747df7304ee51a061e, https://github.com/Akilleez-QA/read-em-and-weep/blob/55bc80b2cb660edd741c93747df7304ee51a061e/research/hm/binary-symmetric-propagation/PROOF.md .
2. Its first Koszul homology is generated in S-degrees three and four. This follows because it is a quotient of the first syzygy module of the ten quadrics, whose minimal generators have these degrees by PR513, commit df947c1ce092c0c59dcef187639147da8a7b2873, Section 3: https://github.com/Akilleez-QA/read-em-and-weep/blob/df947c1ce092c0c59dcef187639147da8a7b2873/research/hm/column-level-resolution/PROOF.md .
3. Fiber Koszul duality pairs H_i in degree d with H_(5-i) in degree 15-d, up to a fixed determinant line. For completeness this is the finite-length hyper-Ext calculation: the ten-quadratic Koszul complex is reverse self-dual with internal shift 20 and homological length ten; every homology module is supported at the irrelevant maximal ideal, so its Ext into S(-5) is concentrated in cohomological degree five and is its graded vector-space dual, up to the ambient determinant line. The hyper-Ext spectral sequence therefore collapses and changes complementary index ten to five, and internal shift twenty to fifteen. No relative or family-flat duality is involved.
4. The degree-three column syzygy bundle L=ker[U tensor S_1 tensor O(-1) -> S_3 tensor O] is 10O(-2) direct sum 5O(-6), established in PR511, commit 55bc80b2cb660edd741c93747df7304ee51a061e, https://github.com/Akilleez-QA/read-em-and-weep/blob/55bc80b2cb660edd741c93747df7304ee51a061e/research/hm/binary-symmetric-propagation/PROOF.md .
5. Complementary duality for the actual generalized Eagon--Northcott complexes gives dim H_1(C^0)_8 = dim H_3(C^8)_7 and dim H_2(C^0)_10 = dim H_2(C^8)_5. This is the actual grade-five finite-length duality, not generic perfection. It is pinned in PR507, commit 87c9b317bd4b1116e63212a6d7ec2730486b2032, https://github.com/Akilleez-QA/read-em-and-weep/blob/87c9b317bd4b1116e63212a6d7ec2730486b2032/research/hm/generalized-en-defects/PROOF.md , and used with the stated degree convention in PR508, commit a59d3dbfdad8b5516cd17c91890b669f2567bdb7, https://github.com/Akilleez-QA/read-em-and-weep/blob/a59d3dbfdad8b5516cd17c91890b669f2567bdb7/research/hm/middle-defect-duality/PROOF.md .

Let x and y denote the two dimensions on the left in item 5.

## 1. Actual generalized Eagon--Northcott complexes are the pushforward

For 0<=a<=8, the derived global-section complex R Gamma(P,K tensor O(a)) is represented by the actual generalized Eagon--Northcott complex C^a. Its terms are

- Lambda^j U tensor Sym^(a-j) G tensor S(-2j), for j<=a;
- Lambda^(j+1) U tensor Sym^(j-a-1) G* tensor det(G*) tensor S(-2j-2), for j>=a+1.

Here characteristic zero identifies symmetric and divided powers in the second row, with the usual normalization of the differentials. No grade hypothesis is required for this identification of complexes.

To verify it, take the two-chart Cech resolution on P. The cohomology of K_p(a) has only two rows: H^0 for p<=a, and H^1 for p>=a+2. The term p=a+1 is acyclic. A term in the second row has total homological degree p-1, giving precisely the displayed second strand. The induced maps within each row are the generalized Koszul differentials. Across the gap, the transferred differential is the two-step Cech differential. On two selected generators u,v, with column forms alpha_u X+beta_u Y and alpha_v X+beta_v Y, it is alpha_u beta_v-alpha_v beta_u, up to the global sign convention for the total complex. Hence it is exactly the maximal-minor splice defining C^a. The calculation is multilinear and exterior-natural, so it identifies the splice on every exterior summand. There are no other transferred maps: a transfer of length r changes Cech degree by 1-r, and the only Cech degrees are zero and one. This proves the assertion even when the actual matrix has grade five rather than the universal expected grade nine.

The hypercohomology spectral sequence in sheaf homology collapses, since P has cohomological dimension one. For every i,d it consequently supplies a natural exact sequence

0 -> H^1(P, mathcal H_(i+1)(K)_d tensor O(a))
  -> H_i(C^a)_d
  -> H^0(P, mathcal H_i(K)_d tensor O(a)) -> 0.

This is a filtration exact sequence; a canonical splitting is not asserted.

## 2. Torsion-safe direct interpretations of x and y

For any closed point lambda of P, universal coefficients for the bounded complex of vector bundles K_d gives

0 -> mathcal H_i(K)_d tensor k(lambda)
  -> H_i(K(lambda))_d
  -> Tor_1(mathcal H_(i-1)(K)_d,k(lambda)) -> 0.

This is applied over the local DVR of P. Thus vanishing of a fiber homology at every closed point implies vanishing of the corresponding homology sheaf by Nakayama, without assuming homology commutes with base change.

Every fiber H_1 has degree at most six: it is generated in degrees three and four and annihilated by the column ideal, whose quotient vanishes above degree two. Thus mathcal H_1(K)_8=0.

The constant-coefficient Koszul differential on Lambda^3 U is injective, because the ten quadrics are independent. Indeed it is exterior comultiplication followed by the inclusion of their span into S_2; exterior multiplication after comultiplication is multiplication by three. Hence fiber H_3 has no terms below degree seven. Fiber duality then implies that fiber H_2 vanishes above degree eight, and consequently mathcal H_2(K)_10=0.

The exact sequence in Section 1 at a=0 therefore proves

x = h^1(P,mathcal H_2(K)_8),
y = h^1(P,mathcal H_3(K)_10).

These statements are valid even in the presence of torsion in those sheaves. They do not identify sheaf duals merely from fiberwise duality.

## 3. Low-degree cycle interpretations and numerical bounds

Let Z_(p,d)=ker[K_(p,d) -> K_(p-1,d)]. Since K_(p+1,2p+1)=0, one has mathcal H_p(K)_(2p+1)=Z_(p,2p+1). These are vector bundles: as kernel subsheaves of vector bundles they are torsion-free, hence locally free on the smooth curve. Also mathcal H_(p+1)(K)_(2p+1)=0, because that entire chain term vanishes.

Section 1 with a=8 gives

H_3(C^8)_7 = H^0(P,Z_(3,7)(8)),
H_2(C^8)_5 = H^0(P,Z_(2,5)(8)).

An independent cross-check avoids the general splice calculation in these two degrees. The complex K_7(8) has only p=0,1,2,3, with line-bundle twists 8,7,6,5, and K_5(8) has only p=0,1,2, with twists 8,7,6. All these terms have vanishing H^1. Their global sections are literally the corresponding positive strands of C^8, and the displayed homology groups are their top kernels. Thus these low-degree identifications hold directly even without the general derived identification.

By the actual complementary duality in input 5,

x = h^0(P,Z_(3,7)(8)),
y = h^0(P,Z_(2,5)(8)).

The important next constraint uses the already determined bundle L rather than chain-term dimensions. Exterior comultiplication embeds Z_(p,2p+1) into

L tensor Lambda^(p-1)U tensor O(-(p-1)).

For clarity, the comultiplication Lambda^p U -> U tensor Lambda^(p-1)U is injective in characteristic zero. Evaluation of the first U factor is exactly the Koszul differential. Restriction to its kernel therefore factors through the kernel L tensor Lambda^(p-1)U, with the indicated twist. This argument requires no base-change assertion and no splitting of the inclusion.

For p=2, twist by O(8). The injection becomes

Z_(2,5)(8) -> 100O(5) direct sum 50O(1).

For p=3 it becomes

Z_(3,7)(8) -> 450O(4) direct sum 225O.

Taking global sections is left exact. Using h^0(O(n))=n+1 for n>=0 proves the concrete bounds

0 <= y <= 100*6+50*2 = 700,
0 <= x <= 450*5+225 = 2475.

These improve the unrefined bounds from the containing Koszul terms, namely y<=225*7=1575 and x<=600*6=3600. They are exclusions of larger values, not determinations of x or y. Equality in either upper bound would require surjectivity on global sections of the corresponding proper alternating-cycle inclusion, which has not been proved.

## 4. A coupled constraint: 3x <= 25y

There is a second, sharper type of exterior inclusion. For any functional f in U*, exterior contraction i_f anticommutes with the Koszul differential, since both differentials are sums of exterior contractions and the quadratic coefficients commute. Thus contracting a linear-coefficient three-cycle produces a linear-coefficient two-cycle. Taking all contractions gives an injection

Z_(3,7) -> U tensor Z_(2,5) tensor O(-1).

The S-degrees differ by two because one Koszul generator has been removed; both cycle spaces still have linear polynomial coefficients. The parameter twist O(-1) makes their line-bundle degrees agree. Injectivity follows since wedge multiplication composed with the contraction coproduct is multiplication by three.

Set E=Z_(2,5). Taking sections after twisting by O(8) gives

x <= 10 h^0(P,E(7)).

After extending the ground field if necessary, split E as a sum of O(b_j). The previously proved injection E -> 100O(-3) direct sum 50O(-7) forces every b_j <= -3: a summand with b_j>-3 has no nonzero map to any target summand, contradicting injectivity. For each b<=-3,

max(b+8,0) <= (5/6) max(b+9,0).

Indeed, writing n=b+9<=6, the only nonzero numerator is n-1 with 1<=n<=6. Summing the summands proves

h^0(P,E(7)) <= (5/6) h^0(P,E(8)) = (5/6)y.

Consequently

3x <= 25y.

In particular, y=0 forces x=0. This is a necessary joint condition, not a converse or a determination of either defect. Together the structural exclusions are 0<=y<=700, 0<=x<=2475, and 3x<=25y. They do not rely on a relative perfect pairing.

## 5. Remaining dependency and verification status

The remaining exact task is to determine the sections of the two displayed alternating-cycle subbundles. Their ambient syzygy-bundle splittings are insufficient to determine them. This work makes no claim that relative Koszul homology is flat, no claim of a torsion-free relative perfect pairing, and no substitution of relative Tor for generalized Eagon--Northcott homology.

All derivations above are structural. No selected actual HM/source-instance coefficients, matrices, ranks, searches, or large computations were used. The bounds and identifications have been authored and checked by hand, but require independent review before publication and are not formally verified.

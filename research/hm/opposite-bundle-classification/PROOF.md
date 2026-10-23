# Sharp one-dimensional vertex-extension ambiguity after torsion exhaustion

Status: structural proof with a bounded abstract-character classification; independent whole-proof review is recorded in REVIEW.md. This is not formal proof-assistant verification. Work over C. No selected actual HM/source coefficient, point, parameter, derivative, matrix, or instance rank is evaluated.

## 1. Immutable hypotheses and exact scope

Repository: Akilleez-QA/read-em-and-weep.

- PR945, commit 089003175d9e31a7cf6288ab7a9e3ac4d66a3e63, research/hm/exceptional-adjoint-exhaustion/PROOF.md: the actual opposite-pencil cokernel C is locally free, globally generated, rank five and degree 26.
- PR934, commit 8c9847612b5f575b987cec9c62b72b099d745e44, research/hm/reduced-opposite-pencil/PROOF.md: the actual exact presentation 0 -> E O(-1) -> H O -> C -> 0 and vertex extension 0 -> O(10) -> D_vert -> C -> 0.
- PR938, commit e5aa6e4695eee79cd0222d8f6b57aa60b7a0dab5, research/hm/opposite-source-weights/PROOF.md, Sections 1–2 only: E=2W+W'+2S+2T6 and H=1+3A+V+2P+2D. Its conditional nonzero-torsion analysis is not imported.

G=SL2(F5), T=P(W*) and O(1) has its standard linearization. A=Sym2 W, V=Sym2 W', S=Sym3 W, D=Sym4 W, T6=Sym5 W, and P is the even four-space. All irreducibles are self-dual. The center acts trivially on C; this also follows from its quotient presentation by the even representation H.

Current PR1 was read through comment6362096172: PR945 settles torsion, but the splitting and vertex extension remain open. Nothing here changes the four-pair/three-label ledger of PR942 or addresses source126 compatibility.

We prove:

1. dim Ext1_G(C,O(10)) <= 1.
2. Precisely five of the twenty-one abstract bundle types allowed by the displayed interface have nonzero invariant Ext. All other types force equivariant splitting of the actual vertex extension.
3. For each of the five types, there are explicit split and nonsplit abstract extensions, and the nonsplit middle bundle is determined up to equivariant isomorphism by a replacement rule below.
4. Every one of the twenty-one types is realized by a fiberwise injective abstract pencil with exactly E and H. Consequently these interface data alone cannot choose a type or decide the extension class. No abstract model is asserted to occur for HM.

## 2. Equivariant splitting and complete evaluation

Any G-equivariant bundle on T splits equivariantly as a direct sum of L_d O(d), with each L_d a finite-dimensional G-representation. To see this without assuming an equivariant Birkhoff–Grothendieck theorem, take the canonical maximal-degree summand, obtained by evaluation of H0(C(-d_max)) O(d_max). The ordinary splitting theorem makes the resulting exact sequence split. Average a splitting over the finite group to make it equivariant and induct. The multiplicity representations can then be decomposed into irreducibles.

Global generation forces d>=0. Rank and degree give sum dim(L_d)=5 and sum d dim(L_d)=26. Trivial central action forces the center on each irreducible L_d to equal (-1)^d.

Taking H0 of the given presentation identifies H with H0(C), and its map with complete evaluation. For any d>=1 the complete evaluation kernel of O(d) is

    Sym^(d-1)W O(-1).

One proof uses multiplication from the tautological kernel O(-1) into Sym^d W: on each fiber its image is precisely the degree-d forms divisible by that kernel line, giving the entire evaluation kernel. Tensor with L_d and sum. Therefore the two exact character tests are

    sum_d L_d Sym^d W = H,
    sum_(d>=1) L_d Sym^(d-1)W = E.                (1)

Conversely every globally generated split equivariant bundle satisfying (1) has this complete-evaluation resolution, with locally free quotient. It thus supplies the claimed abstract pencil, without assigning any actual HM map coefficients.

## 3. Structural one-dimensional bound

In characteristic zero equivariant Ext equals the invariant part of ordinary Ext. Serre duality, det W=1, gives for any irreducible L

    Ext1_G(L O(d),O(10)) = Hom_G(L,Sym^(d-12)W)  (d>=12),

and zero for d<=11. Self-duality removes dual notation.

A contributing summand with dim L>=3 would already have degree at least36, impossible. For dim L=2, parity forces d odd and the degree budget forces d<=13; hence d=13 and Sym1 W=W forces L=W, with contribution one. The only one-dimensional representation is trivial. Its contributing degrees are even d=12,14,...,26, and the invariant multiplicities in Sym^(d-12)W for exponents 0,2,...,14 are respectively

    1,0,0,0,0,0,1,0.

These are fixed nine-class character identities reproduced exactly in verify.py. Thus the only contributing atoms are O(12), O(24), and W O(13), each contributing one.

The degree budget forbids coexistence of different contributing atoms and allows at most two O(12)'s. But H0(O(12)) contains a trivial representation, whereas H has trivial multiplicity only one. Thus two O(12)'s are impossible. This proves the bound independently of the twenty-one-type enumeration.

## 4. The bounded exact ambiguity list

Write a bare integer d for O(d), and L[d] for L O(d). The following are exactly the bundles satisfying rank five, degree26, global generation, parity, and both equations (1). A star marks the five rows with invariant Ext dimension one; all other rows have dimension zero.

 1. 0 + 2 + 2 + 4 + 18
 2. 0 + 2 + 2 + W'[11]
 3. 0 + 2 + 14 + W'[5]
 4. 0 + 2 + 18 + W[3]
 5. 0 + 2 + 22 + W'[1]
 6. 0 + 2 + V[8]
 7. 2 + 4 + 18 + W[1]
 8. 2 + 10 + 12 + W'[1]                  *
 9. 2 + 12 + V[4]                        *
10. 2 + 18 + A[2]
11. 2 + 24 + A[0]                        *
12. 2 + W[1] + W'[11]
13. 2 + W[11] + W'[1]
14. 2 + W'[5] + W'[7]
15. 2 + P[6]
16. 12 + 14 + A[0]                       *
17. 14 + W[1] + W'[5]
18. 18 + W[1] + W[3]
19. 22 + W[1] + W'[1]
20. W[1] + V[8]
21. W[13] + A[0]                        *

Completeness is a bounded integer-character computation, not a geometric claim about these types. The standalone verifier constructs the nine irreducible characters over Q(sqrt5), verifies orthonormality and completeness by sum of squared dimensions120, and uses the recurrence s_0=1, s_1=chi_W, s_n=chi_W s_(n-1)-s_(n-2). It first constructs every atom L O(d) with dim L<=5, 0<=d<=floor(26/dim L), and matching parity. It discards an atom only when its source or target character exceeds the corresponding nonnegative multiplicity in E or H. Exactly45 atoms survive. A nondecreasing multiset recursion subtracts rank, degree and both character vectors; exactly646 states are visited and exactly21 solutions remain. Rank bounds recursion depth by five. The output is compared to the full literal list above, not merely counted. Independent review reproduces the complete list by integer affine-E8 McKay adjacency and rank/degree-first enumeration:48 raw atoms,277 rank-degree candidates, and the same21 survivors, without source/target character pruning during generation.

Each row satisfies (1), so Section2 constructs an abstract fiberwise injective pencil for every row. The list therefore gives a sharp limitation of this precise interface, not only necessary numerical conditions.

## 5. Explicit nonsplit middle bundles

The three contributing atoms admit these exact nonsplit G-equivariant sequences:

    0 -> O(10) -> W O(11) -> O(12) -> 0,          (2)
    0 -> O(10) -> A O(12) -> W O(13) -> 0,       (3)
    0 -> O(10) -> W' O(17) -> O(24) -> 0.        (4)

Sequence (2) is the standard Euler evaluation sequence twisted by eleven. Sequence (3) is the dual of the O(2) complete-evaluation sequence, twisted by twelve. The duality uses self-duality of W and A. Their ordinary splitting types differ from those of the split extensions, so their classes are nonzero.

For (4), the fixed identity Sym7 W=W'+T6 gives an injective map W' -> H0(O(7)). Its two-dimensional linear system has no common zero: its common-zero divisor would be G-invariant of degree at most7. Every nonempty orbit for the projective icosahedral action has size at least12. Indeed point stabilizers in a finite subgroup of PGL2(C) are cyclic, while A5 has maximal cyclic subgroup order5, so orbit size is at least60/5=12. Thus this map gives a surjection W' O -> O(7) with line kernel O(-7); the linearization of the kernel has no character ambiguity because G is perfect. Twist by17 to get (4). Its middle bundle W' O(17) is ordinarily O(17)^2, not O(10)+O(24), so the extension is nonsplit.

Since each corresponding invariant Ext space is one-dimensional, every nonzero class differs by a scalar; scalar automorphisms of O(10) identify their middle bundles equivariantly. All remaining summands have invariant Ext zero and split off. Hence the nonsplit vertex middle bundle is obtained by replacing the unique contributing atom as follows, leaving the complementary summands untouched:

    O(12) -> W O(11),
    O(24) -> W' O(17),
    W O(13) -> A O(12).                         (5)

The split alternative is always O(10)+C. These alternatives are genuinely distinct even as ordinary bundles. For actual C in an unstarred row, only the split alternative exists. For actual C in a starred row, these are the only possibilities furnished by the interface, with no claim selecting its actual extension scalar.

## 6. A single invariant lifting obstruction

Equivariant Serre duality gives a natural perfect pairing

    Ext1_G(C,O(10)) x H0(C(-12))^G -> C.

Indeed the ordinary Serre dual of H1(C* tensor O(10)) is H0(C(-12)), and finite-group invariants preserve this duality. The actual vertex extension twisted by -12 induces

    delta: H0(C(-12))^G -> H1(O(-2))^G = C.

The standard Yoneda/connecting-map description of Serre duality identifies delta with the functional represented by the actual extension class. This supplies a uniform test for all three contributing atoms, not three separate coordinate calculations.

For any starred row H0(C(-12))^G is one-dimensional. Since H0(O(-2))=0, exactness gives H0(D_vert(-12))^G=ker(delta). Therefore the actual extension splits if and only if this invariant section lifts, equivalently h0(D_vert(-12))^G=1; its class is nonzero if and only if h0(D_vert(-12))^G=0. In unstarred rows both the invariant section space and invariant Ext vanish, and splitting is automatic. This identifies the precise remaining geometric datum without evaluating it. The twist -12 is on the parameter line; no identification with a physical normal-order condition is asserted here.

## 7. Contribution and boundary

Local freeness now yields a sharp reduction from an unspecified vertex extension to at most one invariant scalar. Sixteen of the twenty-one possible abstract splitting types force splitting; the remaining five have explicit and fully determined nonzero-extension middle types. All twenty-one admit abstract pencils with the required characters, so no argument using only this interface can remove them. Additional actual incidence/restriction information is needed to choose the actual row or scalar. The result is a new structural constraint and a sharp ambiguity construction, not an actual splitting determination, source exclusion, catalogue change, or formal proof-assistant verification.

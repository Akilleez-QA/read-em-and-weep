# Sixteen compulsory secant-detection exceptions, with exact rank one

## Scope and interface

Work over C with G=SL2(F5), binary module W, A=Sym²W, D=Sym⁴W, and the descended irreducible four-dimensional module P. Assume the canonical source identification and secant kernel interface in Akilleez-QA/read-em-and-weep, pinned at PR661 commit 1325647fd916bf2daa71b11efeae6d52cfefa2cd and PR662 commit f75a18fd411350adda35dedf18751eee002a39bc (exact proof links below). Let

Q=Hom_G(D_source,P⊗Sym²A*)=Q_+⊕Q_−,

where both summands have dimension one and parity refers to interchange of the parameter D and source D slots. For a quadratic a, write b=(a⊗a)_0∈D. The restricted evaluation is E_a:Q→Hom(K_a,P)⊗O(2)_a. PR661 proves E_a injective on the square conic; PR662 proves its degeneracy support finite and disjoint from that conic.

The present result proves that this finite set is NONEMPTY: it contains the six order-five axis directions and the ten order-three axis directions. At all sixteen points E_a has rank exactly one, not zero. Its kernel is neither parity-channel line. More generally each parity channel restricts nontrivially at EVERY direction. We do not claim these sixteen points exhaust the degeneracy locus or determine its scheme structure.

## 1. An invariant linear series excludes excessive root multiplicity

**Lemma.** Let U⊂SymⁿW be a nonzero G-stable subspace of dimension k. If a nonzero f∈U has a root of multiplicity m, and the orbit of this root on P(W) has size N, then

N max(0,m−k+1) ≤ k(n−k+1).

**Proof.** Regard U as a k-dimensional linear series of sections of O(n) on P¹; the invariant alternating form identifies binary vectors with linear functions without changing orbit sizes. At any point p choose a basis with strictly increasing vanishing orders α_0<⋯<α_(k−1). The local Wronskian has vanishing order Σ_i(α_i−i). The Wronskian is not identically zero in characteristic zero, since the sections are linearly independent. It is globally a section of

O(n)^k⊗K_(P¹)^(k(k−1)/2)=O(k(n−k+1)).

If some section has order at least m, then α_(k−1)≥m, and the local Wronskian weight is at least max(0,m−k+1). Stability transports this condition to every point in the root orbit. Summing proves the inequality. Base points cause no problem: their contributions are included in the same vanishing sequence and Wronskian degree. ∎

Every G-orbit on P(W) has at least twelve points. Indeed a point stabilizer in the faithful projective A5 action is cyclic, and the largest cyclic subgroup has order five. Hence N≥12.

Use the representation decompositions from PR661:

Sym⁶W=V⊕P, dim V=3;
Sym⁸W=D⊕P, dim D=5.

The lemma yields two universal exclusions:

- No nonzero element of V⊂Sym⁶W can have a root of multiplicity five: 12·(5−3+1)=36>3·(6−3+1)=12.
- No nonzero element of D⊂Sym⁸W can have a root of multiplicity six: 12·(6−5+1)=24>5·(8−5+1)=20.

These are representation-theoretic linear-series exclusions, not evaluations of selected HM coefficients.

## 2. Neither parity channel ever vanishes on a secant fiber

Let a=uv with u,v independent. The binary realization of the canonical interface gives

b=c u²v², c≠0,       K_a=span(u⁴,v⁴).

The nonzero scalar c depends only on the fixed equivariant identification; multiplication Sym²(Sym²W)→Sym⁴W kills the invariant summand, so the displayed identification is valid also away from the square conic.

Choose any nonzero representatives of the two channel lines. Up to fixed nonzero factors,

B_+(b,h)=π_P^(8)(bh),
B_−(b,h)=π_P^(6)((b,h)_1).

Choose symplectic coordinates u,v. Then evaluation at h=u⁴ gives nonzero scalar multiples of

π_P^(8)(u⁶v²),       π_P^(6)(u⁵v),

respectively. The alternating-channel expression uses the FIRST transvectant of two quartics; its coefficient is nonzero (with (f,g)_1=f_u g_v−f_v g_u it equals −8u⁵v). Both displayed projections are nonzero by Section 1: otherwise their arguments would belong to the complementary D or V and have forbidden root multiplicity six or five. Consequently E_a|Q_+ and E_a|Q_− are nonzero for EVERY nonsquare a.

On squares, PR661 gives the stronger injectivity of E_a, so the conclusion holds there too. In particular E_a always has rank at least one, and every rank-drop fiber has rank exactly one. Its kernel cannot equal Q_+ or Q_−.

This removes a separate possible rank-zero stratum everywhere, independently of the finite-locus argument in PR662.

## 3. Axis stabilizers and the O(2) character

Take a cyclic subgroup C_n⊂A5 with n=5 or 3, and its two fixed points [u],[v] on P(W). Let [a]=[uv]∈P(A). Its projective stabilizer H preserves this unordered pair, and equals the normalizer of C_n. Thus H=D_(2n), of order 2n. In A5 there are six C5 subgroups and ten C3 subgroups, giving distinct axis orbits of sizes six and ten. These directions are nonsquare.

For complete twist bookkeeping choose a binary lift of a rotation with eigenvalues η,η⁻¹ on W, where η has order 2n. It fixes uv. A lift of a reflection exchanges u and v with coefficients whose product is −1, because its determinant is one. It therefore sends uv to −uv. Accordingly H acts on the line Ca by its reflection-sign character ε; on its square, and on its dual square O(2)_a, it acts trivially. The endpoint evaluation has NO residual sign twist.

On K_a=span(u⁴,v⁴), the rotation has eigenvalues η⁴,η⁻⁴, distinct for n=3,5; a reflection interchanges the corresponding lines. Hence K_a is the irreducible two-dimensional dihedral representation with those rotation characters.

For H=D10, P|H=E_1⊕E_2, the two distinct irreducible two-dimensional representations; K_a is one of them, exactly once. This follows directly by restricting the four nontrivial C5 weights of P, then pairing inverse weights by reflection.

For H=D6≅S3, P|H=1⊕ε⊕E, with E the unique irreducible two-dimensional representation. The restricted character is (4,0,1) on identity, involutions and nontrivial rotations, equal to that of 1⊕ε⊕E. Here K_a=E, again once.

It follows in both cases that

dim Hom_H(K_a,P⊗O(2)_a)=1.

Every q∈Q is G-equivariant, so E_a lands in this one-dimensional space. Therefore rank E_a≤1. Section 2 supplies rank≥1, proving rank E_a=1 at all sixteen points.

## 4. Intrinsic kernel line and its precise normalization limit

Let L_a=Hom_H(K_a,P⊗O(2)_a), a line at an axis direction. The H-character of O(2)_a is trivial, but no trivialization of that line is chosen. The two nonzero restriction maps give isomorphisms

e_+(a):Q_+→L_a,       e_−(a):Q_−→L_a.

The exceptional kernel is intrinsically the graph

ker E_a = {x−e_−(a)^(−1)e_+(a)(x) : x∈Q_+}.

This determines the line without selecting actual endpoint data. After choosing generators q_+,q_− and one generator of L_a, write their nonzero restriction scalars α_a,β_a. Then ker E_a=C(β_a q_+−α_a q_−). Rescaling either channel generator changes any displayed numerical ratio; no basis-independent scalar ratio exists without those normalizations. The line itself is canonical, G-invariant along each of the two axis orbits. The proof does not assert that the lines for the order-three and order-five orbits coincide or differ.

## 5. What this resolves and what remains

PR662's finite-or-empty alternative is sharpened to a finite nonempty degeneracy support containing the sixteen axis points. Its entire rank-zero stratum is excluded. Each known exceptional fiber loses exactly one family parameter, and that parameter mixes the symmetric and alternating channels.

There is no conflict with full-fiber detection: q(a,−):D_source→P remains nonzero for every nonzero q and every direction by PR662; the exceptional mixed family merely annihilates K_a.

Exhaustion by these sixteen points, multiplicities/reducedness, numerical parity ratios in chosen normalizations, and the actual HM endpoint's position relative to these kernel lines remain unproved. No actual endpoint or source-instance coefficients, matrices or ranks were evaluated. No parameter scan or large computation was performed.

## Source links

- https://github.com/Akilleez-QA/read-em-and-weep/pull/1 (scope and ownership)
- https://github.com/Akilleez-QA/read-em-and-weep/pull/543 (actual unresolved endpoint context)
- https://github.com/Akilleez-QA/read-em-and-weep/blob/1325647fd916bf2daa71b11efeae6d52cfefa2cd/research/hm/endpoint-square-reconstruction/PROOF.md (square reconstruction, parity decomposition and canonical kernel)
- https://github.com/Akilleez-QA/read-em-and-weep/blob/f75a18fd411350adda35dedf18751eee002a39bc/research/hm/endpoint-base-locus-exclusion/PROOF.md (whole-fiber detection and finite restricted degeneracy)

# The invariant cubic target is controlled by one two-component map

Let F be the normalized Horrocks–Mumford bundle, E=F(3), and B=End₀(F), over complex projective four-space. Use the classical normalizer N=H₅⋊G, with G=SL₂(F₅), and the representation conventions of PR452. In particular W and W′ are the two inequivalent two-dimensional representations; U=Sym²W, U′=Sym²W′; T=χ₄ and Q=χ₄♯ are distinct four-dimensional representations; J=χ₅ and R=χ₆.

This note determines the possible character of the H₅-invariant part of H¹B(5), proves that a distinguished two-dimensional piece of the primary cubic image survives, and excludes the fifteen-dimensional defect channel from that piece. It does not evaluate the remaining equivariant scalars or a selected polynomial multiplication.

## 1. Dependencies and conventions

Write V for the classical five-dimensional representation, A=θV, and S=Sym(V*). PR452 gives

- M₀=H¹F=A*, M₁=A⊗W′, M₂=V⊗W′, M₃=W′;
- H⁰F(3)=T;
- B₃=W′, B₂=A⊗Q, B₁=A*⊗(W⊕J)

in the equivariant section resolution

0 → B₃O(−8) → B₂O(−6) → B₁O(−5)
  → B₀,₄O(−4) ⊕ TO(−3) → F → 0.

PR451 gives the natural exact presentation

B₁⊗M₁ → (B₀,₄⊗M₂) ⊕ (T⊗M₃) → H¹B(5) → 0.       (1)

Both blocks of the first map are retained. The second block of the middle space is the cup product of global sections of E with H¹E. This identifies its image independently of choices of degree-four section generators.

All representations are over C. Invariants under H₅ are therefore an exact functor. When the center of H₅ acts trivially, the invariant subspace carries a canonical G-action.

## 2. The remaining section-resolution coefficient

We first determine the previously unused coefficient:

B₀,₄ = V*⊗U.                                            (2)

Dualize the section resolution and twist by O(−4). Its leftmost term is F(−3), followed by B₀,₄*O ⊕ T*O(−1), B₁*O(1), B₂*O(2), and B₃*O(4). The groups H⁰F(−3), H¹F(−3), H²F(−3), H³F(−3) vanish by primary HM cohomology. Intermediate cohomology of every line bundle on P⁴ vanishes. Splitting the dual resolution into its three short exact sequences therefore gives

0 → B₀,₄* → B₁*⊗S₁ → B₂*⊗S₂ → B₃*⊗S₄ → 0.            (3)

HM Lemma 3.3 and its Galois conjugates give

S₁⊗A = V⊗(U′⊕W),
A*⊗A* = V⊗(U⊕W′),
S₂=A*⊗U′,
S₄=V⊗(T⊕Q⊕U⊕U′).

Here θ interchanges W,W′ and U,U′; it fixes T,Q,J,R. In particular the first identity is the θ-conjugate of V⊗A=A*⊗(U⊕W′). The second follows by conjugating Sym²V⊕Λ²V=A⊗(U′⊕W).

Consequently (3) yields, in the representation ring,

[B₀,₄*]=[V]·[(W+J)(U′+W) − Q U′(U+W′)
                         + W′(T+Q+U+U′)] = [V]·[U].    (4)

The last equality is an identity of the nine G-characters in the HM Appendix. For clarity, in the column order printed there, the bracket has values

(3, 3, −1, 0, 0, −η, −η′, −η, −η′),

where η=ζ₅+ζ₅⁴ and η′=ζ₅²+ζ₅³, so η+η′=−1 and ηη′=−1. These are exactly the values of U. This is a character identity, not a chosen HM differential calculation. Semisimplicity now proves (2).

## 3. An exact invariant presentation

The H₅-representations V and A are irreducible, so

(End V)^H₅ = C and (End A)^H₅ = C,

with trivial G-action on these scalar lines. Taking H₅-invariants in (1), and using (2), gives source and target

((W⊕J)⊗W′) → (U⊗W′) ⊕ (T⊗W′).

The HM character identities are

W⊗W′=T,   J⊗W′=Q⊕R,
U⊗W′=R,   T⊗W′=W⊕R.

Hence the full invariant presentation is

T⊕Q⊕R → R⊕(W⊕R) → (H¹B(5))^H₅ → 0.                 (5)

The first R in the middle space comes from degree-four section generators; the parenthesized W⊕R is the intrinsic primary cup-product space T⊗M₃. The representation types T,Q,W,R are pairwise distinct. Thus the first map in (5) vanishes on T⊕Q and maps its single R to the two target copies of R. After choosing abstract identifications of these copies, it is

r ↦ (a r, b r)                                         (6)

for two scalars a,b. The coordinate pair depends on those identifications; its vanishing and the resulting invariant quotient do not. There are precisely two possible target characters:

(H¹B(5))^H₅ ≅ W⊕2R if (a,b)=0,
(H¹B(5))^H₅ ≅ W⊕R  if (a,b)≠0.                         (7)

Its dimension is therefore exactly either fourteen or eight. No claim that either alternative occurs is made.

## 4. A surviving primary piece and a forbidden defect contribution

Let I₂ be the primary image in H¹B(2). PR452 identifies I₂=T⊗M₀ and constructs the unique N-equivariant lift j:C₂→H¹B(2), where

C₂=(A*⊗U) ⊕ (A*⊗Q) ⊕ (A*⊗R).

Write C₁₅=A*⊗U for its fifteen-dimensional channel. Let L=S₃I₂ be the span of all cubic multiples of the primary image. Naturality of cup product and generation of M in degree zero show that

L = im[T⊗M₃ → H¹B(5)].                                (8)

Indeed S₃⊗M₀→M₃ is surjective, and the two ways of multiplying a global section, a polynomial, and a cohomology class agree. In particular L is H₅-trivial, not merely an eight-dimensional upper-bounded image.

The W summand in the primary source in (5) cannot meet the image of the preceding map: that map has only R-type image. Therefore cup product maps W isomorphically onto the unique W-isotypic subspace of (H¹B(5))^H₅. Its R summand is either killed or injective. Thus

L ≅ W or W⊕R,                                         (9)

and in particular the primary cubic image is never zero. Its dimension is exactly two or eight.

Now consider the canonical universal defect cubic map

μ:S₃⊗C₂→H¹B(5),   s⊗c↦s·j(c).

Since S₃=A⊗(J⊕W′), its invariant domain on C₁₅ is

(S₃⊗C₁₅)^H₅ = (J⊕W′)⊗U.

The central element −I in G acts as +1 on J and U, but as −1 on W,W′,R. Equation (7) says that it acts as −1 on the entire invariant target. Consequently the J⊗U part maps to zero. The remaining W′⊗U is exactly R. Hence

μ(S₃⊗C₁₅) has zero projection to the canonical W-subspace of H¹B(5).  (10)

This is a statement about the full universal map: averaging over H₅ shows that any map to an H₅-trivial target factors through H₅-invariants of its source. It is not merely a statement about specially invariant inputs.

Similarly the invariant-domain pieces W′⊗Q and W′⊗R from the twenty- and thirty-dimensional channels have even parity and map to zero in the invariant target. Only J⊗Q and J⊗R from those channels can contribute there. These exclusions do not evaluate their maps.

As a check on scope, the known h¹B(5)≥32 and (8) imply dim(H¹B(5)/L)≥24. The content of this note is stronger than this dimension bound: (5)–(10) identify the invariant target alternatives, a canonical nonzero primary subspace, and a forbidden universal channel contribution.

## 5. A canonical non-primary summand and a dimension congruence

The center Z of H₅ acts trivially on the source and target of (1). For example B₀,₄⊗M₂=End(V)⊗R, while T⊗M₃ is H₅-trivial. Thus the H₅-action on H¹B(5) factors through the abelian group H₅/Z≅F₅². Its character decomposition is canonical. The G-action permutes its twenty-four nontrivial characters transitively, so all these character spaces have the same dimension m.

Consequently the direct sum K of the nontrivial H₅-character spaces is N-stable, has dimension 24m, and

H¹B(5) = (H¹B(5))^H₅ ⊕ K,

dim H¹B(5) ∈ {8+24m, 14+24m}.                         (11)

Since h¹B(5)≥32, m≥1. The H₅-restriction of End(V) is the sum of all twenty-five characters, each once, by the Heisenberg representation identities. The first middle summand in (1) is End(V)⊗R, so each nontrivial character has multiplicity six there; the other summand is trivial. Surjectivity in (1) gives m≤6.

This proves 1≤m≤6 without choosing a differential. In particular the fourteen-dimensional invariant alternative forces h¹B(5)≥38, whereas the eight-dimensional alternative permits the still-unproved value32. The canonical summand K has dimension at least24 and is disjoint from L, because L is H₅-trivial by (8). It survives as a direct summand of H¹B(5)/L. Thus primary degree-two classes and all their cubic multiples necessarily miss an entire nontrivial Heisenberg-character orbit, not merely an unspecified collection of dimensions. Whether the canonical defect cubic map supplies this summand remains unresolved.

## 6. Scope and exact sources

The canonical channel and lift dependency is PR452 at
https://github.com/Akilleez-QA/read-em-and-weep/blob/3b1d18105fa8b8b39bd96d889a34bc81a860f181/research/hm/cubic-defect-channels/PROOF.md

The degree-five presentation and lower bound are PR451 at
https://github.com/Akilleez-QA/read-em-and-weep/blob/ed8841c18f103e71b84c0e9376e20a2a4ed2ef9c/research/hm/order-five-cubic-defect/PROOF.md

The section resolution and primary cohomology are also pinned in PR167:
https://github.com/Akilleez-QA/read-em-and-weep/blob/063da90fc4543304e87e701cdefcc08225412f17/research/conductor-normalization/sharper-hm-regularity/PROOF.md

Primary source: Horrocks–Mumford, “A rank 2 vector bundle on P⁴ with 15,000 symmetries,” Topology 12 (1973), 63–81, especially Lemma3.3, §4, and the character table on p.81:
https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf

No selected HM/source instance, numerical matrix, rank routine, or computational tensor table is used. The pair (a,b) remains unevaluated. For a fixed quadratic u and cubic v, the quotient P₅ need not be an N-representation; nothing here applies Schur's lemma to it. The fixed order-five endpoint Q₅, actual-source ideal membership, six pure conditions, higher-order lifting, and algebraicity remain separate open questions. No equality h¹B(5)=32 or universal cubic surjectivity is asserted.

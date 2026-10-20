> Publication scope: Explicit two-factor pushforward splitting gives H0/H1 vanishing; mixed gauge comparison still imports actual source identities. Source-stage audit/checker references describe historical evidence, not fresh execution or bundled executable artifacts. Named source identities are hypotheses unless separately proved below.

# Structural vanishing for every two-factor deck character

## Result

Let Y=(P¹)^4, let σ:Y→Sym⁴(P¹)=P⁴ be the symmetric quotient, and let H be the classical normalized Horrocks–Mumford bundle. For any two-element subset S of {1,2,3,4}, put L_S=O_Y(−2 on S,0 elsewhere). Then

H⁰(Y,σ*End(H)⊗L_S)=H¹(Y,σ*End(H)⊗L_S)=0.

Thus for X=C^4 with the product elliptic double cover q:X→Y, and E=N⊗(σq)*H, every two-factor deck character χ_S satisfies

Ext⁰_X(E,E)_{χ_S}=Ext¹_X(E,E)_{χ_S}=0.

This includes χ12 and χ34. The proof does not use the historical total Ext¹ dimension, a source/model rank, or any finite-instance calculation. It proves a general pushforward splitting and then uses the independently verified classical theorem H¹(End H(t))=0 for t≤−2.

## 1. A pushforward splitting

Write B_S=σ_*L_S. Then, as vector bundles on P⁴,

B_S ≅ Ω²_P⁴ ⊕ O_P⁴(−2)^9 ⊕ O_P⁴(−3)^9.                 (1)

No compatibility of this splitting with multiplication is asserted.

### 1.1 Cohomology and self-duality

The symmetric quotient is finite flat of degree 24, by the same Cohen–Macaulay/regular-target argument in the invariant-row proof. Thus B_S is locally free of rank 24. Since σ*O(1)=O_Y(1,1,1,1), finiteness, projection formula and Künneth give

H^j(P⁴,B_S(n))=H^j(Y,O_Y(n−2,n−2,n,n)),

after a permutation of factors.

For n≥2 only H⁰ is nonzero, with dimension (n−1)²(n+1)². For n=1 or n=−1, all cohomology vanishes. For n=0 the only nonzero group is H², of dimension one. For n≤−2 only H⁴ is nonzero. In particular the only intermediate cohomology of all twists is H²(B_S)=k.

Finite duality gives

B_S* = σ_*(L_S^−1⊗ω_Y⊗σ*ω_P⁴^−1)
     = σ_*L_{Sᶜ}(5)
     = B_{Sᶜ}(5).

Here the middle formula uses ω_Y=O_Y(−2,−2,−2,−2) and σ*ω_P⁴^−1=O_Y(5,5,5,5). A permutation exchanging S and Sᶜ commutes with σ and identifies the two pushforwards. Hence there exists an isomorphism

B_S ≅ B_S*(−5).                                      (2)

No symmetry property of this isomorphism is needed.

### 1.2 Lift the unique intermediate class

Abbreviate B=B_S and P=P⁴. The Euler/Koszul sequences are

0→Ω¹_P→O_P(−1)^5→O_P→0,
0→Ω²_P→O_P(−2)^10→Ω¹_P→0.

Apply Hom(−,B). The vanishing H¹(B(1))=H²(B(1))=0 gives an isomorphism

Ext¹(Ω¹_P,B) ≅ Ext²(O_P,B)=H²(B).

The vanishing H¹(B(2))=0 makes the connecting map

Hom(Ω²_P,B)→Ext¹(Ω¹_P,B)

surjective. Choose f:Ω²_P→B mapping to a nonzero class in H²(B).

The composed connecting homomorphism sends f to the pushout by f of the Euler two-extension. The Euler two-extension represents the generator of H²(Ω²_P)=k. By naturality, the selected class is exactly the image of that generator under H²(f). Therefore H²(f) is an isomorphism between one-dimensional spaces.

### 1.3 Dualize and split

There is a canonical isomorphism (Ω²_P)*(−5)≅Ω²_P, from the rank-four exterior pairing and det Ω¹_P=O_P(−5). Dualize f, twist by −5, and compose with (2) to obtain

g:B→Ω²_P.

Serre duality in dimension four identifies H²(f*(−5)) with the dual of H²(f). Thus H²(g) is also an isomorphism. Consequently H²(gf) is nonzero.

The standard Euler/Koszul cohomology gives End_P(Ω²_P)=k. For completeness, Ω²_P(1) and Ω²_P(2) are acyclic, and H²(Ω²_P)=k. Applying the same two Hom long exact sequences with B=Ω²_P, and using H⁰(Ω²_P(2))=H¹(Ω²_P(2))=0, identifies Hom(Ω²_P,Ω²_P) with H²(Ω²_P)=k. These acyclicity statements also follow directly from the twisted Euler sequences: the relevant maps are the usual exact homogeneous pieces of the Koszul complex.

It follows that gf is a nonzero scalar multiple of the identity. Rescale g to make gf=id. Therefore B≅Ω²_P⊕R for a rank-18 vector bundle R.

The only intermediate cohomology of Ω²_P(n) is H²(Ω²_P)=k, and f induces its isomorphism to H²(B). Thus every intermediate cohomology group of every twist of R vanishes. Horrocks' splitting criterion implies R is a sum of line bundles.

Since H⁰(R(1))=0, all those line bundles are O(−a) with a≥2. At twist 2, h⁰(B(2))=9 and h⁰(Ω²_P(2))=0, so precisely nine summands have a=2. At twist 3, h⁰(B(3))=64 and h⁰(Ω²_P(3))=10, so h⁰(R(3))=54. The nine O(−2) summands contribute 45, leaving nine O(−3) summands. They exhaust rank 18. This proves (1).

## 2. Apply the splitting to End H

Put F=End H. Stability of H gives H⁰(F(t))=0 for t<0. The independently verified Decker–Schreyer proposition gives H¹(F(t))=0 for t≤−2. In particular the O(−2) and O(−3) summands in (1) contribute nothing to H⁰ or H¹.

For the remaining summand, tensor the Euler coresolution by F:

0→F⊗Ω²_P→F(−2)^10→F(−1)^5→F→0.

Let K be the kernel of F(−1)^5→F. From K⊂F(−1)^5, stability gives H⁰(K)=0. The short exact sequence

0→F⊗Ω²_P→F(−2)^10→K→0

therefore gives H⁰(F⊗Ω²_P)=0 and H¹(F⊗Ω²_P)=0, since H⁰(F(−2))=H¹(F(−2))=0. Notice that neither a value of H¹(F(−1)) nor a multiplication-map rank is needed.

Projection formula and (1) now prove the claimed vanishings on Y. The character eigensheaf formula q_*O_X|χ_S=L_S and cancellation of the line-bundle twist in End E identify these with the claimed Ext groups on X.

## 3. Precise gauge consequence and its limit

Let A be an equivariant differential graded model computing RHom_X(E,E), over a characteristic-zero field. Fix a pair character χ and a prescribed degree-two right-hand side r in A²_χ. If u,v∈A¹_χ are two solutions of du=dv=r, then u−v is closed. The proved H¹(A_χ)=0 yields a degree-zero ξ∈A⁰_χ with u−v=dξ. Thus, conditional on existence and on fixing the same right-hand side, a character-pure first lift is unique modulo the linearized gauge relation.

There are two qualifications:

1. Vanishing of H¹ proves uniqueness modulo gauge, not existence of a lift. Existence still requires the prescribed degree-two source to be exact.
2. In a nonnegatively graded model, H⁰(A_χ)=0 says a closed degree-zero gauge parameter vanishes, so ξ is unique. In a model with negative degrees, two such parameters may differ by dη for η∈A^−1_χ; uniqueness is only modulo higher homotopy. The cohomology statement alone does not make a chosen raw chain parameter unique.

These statements apply to χ12 and χ34 separately. They do not alone prove that a particular mixed-obstruction representative, a particular source-level primitive, or its coefficient polynomial descends under a finite group of bundle symmetries. Such a descent claim still requires a specified compatible action on the deformation problem, its inputs and target, together with a proof that changes of representatives and gauge produce boundaries in the actual obstruction expression. The splitting (1) is additive and supplies no multiplicative identification.

## 4. Dependencies and field

The argument uses standard finite duality, Euler/Koszul sequences, Serre duality, and Horrocks' splitting criterion, together with stability and the verified classical H¹(End H(t)) vanishing at t≤−2. The classical identification and source verification are in:

- ../../hm-presentation-independent/PROOF.md
- ../../cubic-loci/foundation-p01/INVARIANT-COHOMOLOGY.md
- original-source:projective-target-directions/HM-PRIMARY-SOURCE-VERIFICATION.md (historical primary-source verification; not bundled)

The latter identifies the primary publication: W. Decker and F.-O. Schreyer, “Pullbacks of the Horrocks–Mumford bundle”, J. reine angew. Math. 382 (1987), 215–220, proposition on printed p.218.

All geometric splitting arguments work in characteristic zero, and the classical HM input applies over C. For the stipulated rational data, proper cohomology and eigenspace formation commute with field extension, so the vanishings descend to Q and extend to any characteristic-zero base field. No new claim in positive characteristic is made.

Only static local document reads and formal geometric/cohomological reasoning were used. No source/model/rank/polynomial-instance/point/jet/residual execution or evaluation was performed.

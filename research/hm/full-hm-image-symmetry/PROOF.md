# Classical normalizer action and the twenty-dimensional HM module

This prerequisite excerpt preserves Sections 1–3 of the source argument. It proves the equivariant coresolution and irreducible twenty-dimensional cohomology module; no Massey-image consequence is part of this excerpt.

## 1. Primary-source input and literal binding

Primary source: G. Horrocks and D. Mumford, *A rank 2 vector bundle on P4 with 15,000 symmetries*, Topology 12 (1973), 63–81, https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf .

The facts imported from it are these. Its §§1–2 establish N=H5⋊SL2(F5)⊂SL(V), of order 15000, with center C=μ5 and projective quotient order 3000. Write V1 for the five-dimensional N-module with central character ζ², and V3=V1* for its dual. The module W=Hom_H5(V1,Λ²V) is the two-dimensional SL2(F5)-module χ2, has determinant one, and Λ²V=V1⊗W. Its equivariant monad (2.3) uses W and the invariant alternating form. The appendix, p.81, gives the irreducible character table. These are the historical representation-theoretic inputs; all quotient deductions below are supplied here.

The [literal-presentation proof](../hm-presentation-independent/PROOF.md), §§2–4, identifies the actual coefficient tables with this monad and its Euler coresolution, using the displayed cyclic bivectors w_i±, volume identification, and right-map sign −b. Thus the action is transported to this exact presentation, not to an unspecified isomorphic bundle. In the following, the symbol W is the historical two-dimensional representation, not the fifteen-dimensional kernel called W in that proof.

Use the usual left N-action for the derivation. The normalized complex has coefficient modules

    K−1 = V1⊗O(−1),
    K0  = C0⊗O,
    K1  = V*⊗W⊗O(1),
    K2  = W⊗O(2).

Indeed its ambient Euler degree-zero term is Λ²V*⊗W. The right monad map extends to the constant surjection

    b : Λ²V*⊗W → V3.

It is the dual evaluation map, with the alternating identification W≅W*. To make the copy-space identification explicit, take the historical basis (w+,w−) of W and use (w−,−w+) as the coefficient-plane basis (plus,minus). Then the alternating coevaluation w+⊗w−−w−⊗w+ has coefficient pair (w+,w−), exactly the literal left map; evaluation on the right is ηplus(w−)−ηminus(w+), exactly the literal b. The recorded global sign on the last monad term remains harmless. Since

    Λ²V*⊗W = V3⊗W⊗W
                 = V3⊗(1 ⊕ Sym²W),

b is the nonzero alternating contraction on W⊗W, so

    C0 = ker b = V3⊗Sym²W.                         (1)

One can also check its nonzero normalization from b(c_i,0)=e_i in the literal proof. This is an exterior/coefficient identity, not a new source multiplication or rank test. All four chain maps are N-equivariant: they are the monad maps and natural Euler contraction/evaluation. The SL5 condition makes the volume identification equivariant without a determinant character.

## 2. The global cycles and the transgression as actual N-modules

The [explicit coefficient quotient](../derivative-transgression-relations/EXPLICIT-COEFFICIENT-QUOTIENT.md), §1, proves by the formal evaluation identity that projection of a closed global degree-two twist−2 map onto its block B:K0→K2(−2) is an isomorphism

    Z²_global ≅ Hom(C0,W).

This projection is N-equivariant: the individual chain degrees and the indicated block are preserved, and the uniquely determined other block is recovered by natural evaluation. Thus (1) gives

    Z²_global ≅ V1⊗Sym²W⊗W
              ≅ V1⊗(W ⊕ Sym³W).                  (2)

Here W is self-dual via its invariant alternating form, and the second equality is the usual characteristic-zero two-dimensional tensor identity. It is an identity of SL2 representations restricted to SL2(F5), not an inference from the number 30.

The [transgression proof](../derivative-transgression-relations/PROOF.md), §3, gives the N-equivariant exact sequence

    0 → H⁴(Hom(K2,K−1(−2))) → Z²_global → U2 → 0. (3)

Its injection follows from H¹(End H(−2))=0; it is the sole possible higher-row differential d5 in the Hom hypercohomology spectral sequence. This argument uses the independently established cohomology vanishing, without evaluating that differential. Keeping the coefficient representations in its source yields

    H⁴(Hom(K2,K−1(−2)))
      = Hom(W,V1)⊗H⁴(O(−5))
      = V1⊗W.                                     (4)

Equivariant Serre duality identifies H⁴(O(−5)) with the trivial representation for N⊂SL5. Formulas (2)–(4) are sufficient: no products of derivative matrices, or actual transgression coefficients, are needed.

## 3. The four-dimensional factor is irreducible, not two plus two

For a determinant-one two-dimensional representation with trace t, its third symmetric power has trace t³−2t. Put η=ζ+ζ⁻¹ and η′=ζ²+ζ⁻². In the appendix's class order, W has trace list

    2, −2, 0, −1, 1, η, η′, −η, −η′.

Since η and η′ are the two roots of x²+x−1=0, applying t³−2t gives

    4, −4, 0, 1, −1, −1, −1, 1, 1.

This is precisely the irreducible spinorial four-dimensional row χ4# (the row immediately below the nonspinorial four-dimensional character) of the primary appendix. In particular Sym³W is irreducible. This explicitly excludes W⊕W, W⊕W′, and other hypothetical decompositions; it is not a dimension-only guess.

For clarity, the needed elementary normal-subgroup argument is the following. V1 restricts irreducibly to H5. For an SL2(F5)-module M inflated to N, all H5-submodules of V1⊗M are V1⊗M′ for subspaces M′⊂M: this follows by applying Hom_H5(V1,−) and evaluation, or by the full matrix algebra generated by an irreducible finite-group representation. Such a submodule is N-stable exactly when M′ is SL2(F5)-stable. Therefore V1⊗W and V1⊗Sym³W are irreducible N-modules and nonisomorphic (dimensions 10 and 20).

The injected ten-dimensional representation in (3) must accordingly be the unique V1⊗W summand in (2): its component in the nonisomorphic irreducible twenty-dimensional summand is zero. Taking the quotient proves the actual representation identity

    U2 ≅ V1⊗Sym³W,                                (5)

and its irreducibility. No unverified identification of equal-dimensional multiplicity spaces occurs.


# Four equivariant parameters for the mixed HM operation

## Result

Work over C, with the usual left action of the classical group N=H5⋊G, G=SL2(F5), and the ordinary twist linearizations. Subject exactly to N-equivariance, outer reversal, and cyclic zero, the space of mixed operations of weights (0,1,1) has dimension **four**:

    dim Hom_N(U0 ⊗ U1 ⊗ U1, U2) = 4.

Its symmetric and alternating last-two-slot parts each have dimension two. Thus these symmetries do not reduce the canonical operation to one scalar. They leave a four-dimensional parameter space, without proving that any particular parameter or the actual operation is nonzero. Every nonzero member is surjective because U2 is irreducible.

## 1. Dependencies and conventions

Import the audited literal equivariant resolution, cohomological dimensions, target identification, naturality and canonical operation from:

- [the full hm image symmetry manuscript](../../full-hm-image-symmetry/PROOF.md) and AUDIT.md;
- [the cech transgression primitives manuscript](CECH-PRIMITIVES.md), especially §5;
- [the derivative transgression relations manuscript](../../derivative-transgression-relations/PROOF.md);
- [the weight two massey manuscript](../foundation-p04/WEIGHT-TWO-TRANSFER.md);
- [the canonical massey detector manuscript](../foundation-p04/CANONICAL-MASSEY.md).

Use V for the defining five-dimensional N-module, central character c. Use V1 for the historical five-dimensional module of central character c², W for the historical two-dimensional G-module, and S=Sym³W. The imported target theorem gives

    U2 = V1 ⊗ S.

The primary source is Horrocks–Mumford, *A rank 2 vector bundle on P4 with 15,000 symmetries*, Topology 12 (1973), 63–81:
https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf

Its §1 proves that End(V) and End(V1) are isomorphic N-modules, whose trace-free parts contain the 24 distinct nontrivial H5/C characters. Its §2 identifies Λ²V=V1⊗W. Lemma 3.3(v) identifies Sym²V=V1⊗U′, where U′ has character χ3′. The appendix identifies U′=Sym²W′ for the other two-dimensional representation W′. These are the only additional primary-source representation facts needed. They were read in the source; no End-cohomology representation is guessed from its dimension.

## 2. The source modules from Euler and Kodaira–Spencer

On P(V), the equivariant Euler exact sequence is

    0 → O → V ⊗ O(1) → T_P → 0.

Its global sections give

    0 → C·Id → V ⊗ V* → H⁰(T_P) → 0.

The orbit-family Kodaira–Spencer map κ:H⁰(T_P)→H¹(End H)=U0 is N-equivariant. The already proved projective injectivity theorem, transported downstairs as in the Čech proof §5, makes κ injective. The imported cohomological dimension h¹(End H)=24 then makes κ an isomorphism. Hence

    U0 ≅ End(V)/C·Id ≅ End0(V).                 (1)

This is a representation identification through a natural map and exact sequence; the dimension is used only to establish its surjectivity.

Twisting Euler by O(−1) gives

    0 → O(−1) → V ⊗ O → T_P(−1) → 0,
    H⁰(T_P(−1)) ≅ V.                           (2)

Here H⁰(O(−1))=H¹(O(−1))=0. The linear differential of the equivariant resolution has an invariant coefficient tensor. Contracting that tensor with w∈V defines its directional derivative D_w, a global closed degree-one map with twist −1. This gives an N-equivariant map

    j: V → U1,       w ↦ [D_w].                 (3)

It is the twisted infinitesimal-coordinate/Atiyah map in (2). Its compatibility with untwisted Euler and κ is explicit: multiplying D_w by ℓ∈V* represents the Kodaira–Spencer image of the rank-one endomorphism w⊗ℓ. This is precisely the formal coordinate-variation identity established in the Čech proof §5, with its Euler scalar boundary. No product or value is evaluated here.

In particular j cannot be zero: otherwise every rank-one coordinate direction, hence all of κ, would be zero. The H5-module V is irreducible, so the nonzero equivariant j is injective. The imported h¹(End H(−1))=5 makes it an isomorphism:

    U1 ≅ V.                                     (4)

Equivalently, one can use the already proved derivative-basis theorem to establish surjectivity in (3). The derivative tensor, twisted Euler identification, and KS compatibility fix which five-dimensional representation occurs. The dual V* would have the wrong central character in the chosen left-action convention. In the opposite pullback convention all the modules and maps must be converted together; the Hom dimension is unchanged.

## 3. Reversal and cyclic zero do not symmetrize the two U1 slots

Write A=U0 and B=U1. For a∈A and b,c∈B set F(a,b,c)=m011(a,b,c). The two identities are

    m(x,y,z)=m(z,y,x),
    m(x,y,z)+m(y,z,x)+m(z,x,y)=0.

They imply

    m110(b,c,a) = F(a,c,b),
    m101(b,a,c) = −F(a,b,c)−F(a,c,b).            (5)

Conversely, starting with any trilinear F:A⊗B⊗B→U2 and defining the other two orderings by (5) satisfies every reversal and cyclic equation for these weight patterns. Indeed middle-placement reversal is the symmetry of the sum in (5); every cyclic sum consists of the two F terms and their negative. This remains true when b=c. Thus restriction to m011 is an isomorphism from the space of compatible triples of operations onto Hom(A⊗B⊗B,U2), equivariantly for N.

Consequently the desired source is A⊗B⊗B, or equivalently

    (A⊗Sym²B) ⊕ (A⊗Λ²B),

not only one of its two summands. The reversal of arguments here is distinct from the geometric coordinate-reversal element of N, whose equivariance is already included in Hom_N.

## 4. The 24-dimensional multiplicity module is a permutation module

Put Z=End0(V). By the primary-source isomorphism End(V)≅End(V1), which takes the unique trivial summand to itself, Z≅End0(V1) as N-modules. Define the G-module

    R = Hom_H5(V1, Z⊗V1).

Every H5 constituent of Z⊗V1 has the central character of V1, so Heisenberg representation theory and evaluation give an actual N-isomorphism

    Z⊗V1 ≅ V1⊗R.                               (6)

Equivariant tensor-Hom adjunction gives

    R ≅ Hom_H5(V1⊗V1*, Z)
      ≅ Hom_H5(End(V1), End0(V1)).              (7)

Decompose End(V1) into its 25 distinct H5/C-character lines. In (7), each of the 24 nontrivial character lines contributes its identity map, extended by zero on the other character lines. Conjugation by G permutes these projectors. There is no phase character in this action: any scalar action on a character line cancels between the domain and codomain of its projector. It follows that R is exactly the permutation representation on the 24 nonzero elements of the character group (H5/C)*≅F5².

The standard G-action on nonzero vectors is transitive. A nonzero vector has stabilizer a unipotent subgroup P of order five, for instance the matrices fixing the first basis vector. Therefore

    R ≅ C[G/P] = Ind_P^G(1).                    (8)

This assertion concerns the multiplicity module R, not Z itself: Z has nontrivial H5 action, while R is inflated from G. Confusing them would invalidate the argument.

## 5. Frobenius reciprocity reduces everything to order five

Let

    M = Hom_H5(V1,V⊗V).

Since V⊗V has central character c², evaluation identifies it with V1⊗M. The symmetric/exterior primary-source identities give

    M ≅ U′ ⊕ W,    U′=Sym²W′.                   (9)

Using (1), (4), (6), and the target identification, the desired dimension is

    dim Hom_N(Z⊗V⊗V, V1⊗S)
      = dim Hom_G(R⊗M,S).

Finite-group representations over C are semisimple, so this equals dim Hom_G(S,R⊗M). The tensor identity and Frobenius reciprocity for (8) give

    dim Hom_G(S,R⊗M) = dim Hom_P(S|P,M|P).       (10)

To compute (10), let χ generate the character group of P. Both faithful determinant-one two-dimensional modules W and W′ restrict as

    W|P = χ^a ⊕ χ^(−a),
    W′|P = χ^b ⊕ χ^(−b),

for nonzero a,b modulo 5. These restrictions follow directly from the order-five columns of the primary appendix; neither has an invariant vector. Now

    S|P = Sym³W|P
         = χ^(3a) ⊕ χ^a ⊕ χ^(−a) ⊕ χ^(−3a).

The four exponents are all four nonzero residues modulo 5, each once. Also

    U′|P = Sym²W′|P = χ^(2b) ⊕ 1 ⊕ χ^(−2b).

Thus M has one trivial character and four nontrivial characters counted with multiplicity. Pairing with S counts those four and gives

    dim Hom_N(U0⊗U1⊗U1,U2) = 4.               (11)

Separately, U′ contributes its two nontrivial characters and W contributes its two, proving

    dim Hom_N(U0⊗Sym²U1,U2) = 2,
    dim Hom_N(U0⊗Λ²U1,U2) = 2.                 (12)

Only finite abstract representation identities are used, with no matrix construction or enumerated character sum.

## 6. Interpretation and limits

The actual canonical operation specifies one vector in this four-dimensional intertwiner space. After choosing bases for the two two-dimensional Hom spaces in (12), it is described by four scalars. No canonical such bases or scalar values are constructed. Up to arbitrary nonzero overall scale, the nonzero eligible operations form a projective three-dimensional space; this is a description of the symmetry-allowed parameter space, not of a geometric moduli family realizing it.

The imported target irreducibility means that every nonzero equivariant map has full twenty-dimensional image; its previously stipulated positive projection has dimension eight. Therefore the earlier image dichotomy remains zero or twenty, retained zero or eight. Four parameters do not produce new possible intermediate image dimensions.

The smooth family already supplied the polarized cubic/cyclic identity used in §3. No additional family-extension claim is used in this parameter calculation. This is not an assertion that all higher-order smoothness consequences, all additional naturality, or all geometric constraints have been exhausted. In particular, no all-order realization theorem for arbitrary four-parameter choices is claimed.


## 7. Explicit abstract four-component certificate

The dimension computation admits a direct parametrization in the direction needed for the actual map, without reversing a Hom space. Make the following choices:

1. A nonzero character x0 of H5/C and its stabilizer P≤G.
2. An N-isomorphism J:Z→End0(V1), where Z=U0 has already been identified by KS. Such an isomorphism exists by §4; since these trace-free modules are irreducible, its ambiguity is one nonzero scalar.
3. A generator p of P and a primitive fifth root ζ, writing χ(p)=ζ.
4. Nonzero vectors in the one-dimensional weight spaces specified below.

Through tensor-Hom adjunction and J, let r_x0∈R correspond to the projector onto the x0-character line of End(V1). Put r_(g x0)=g r_x0. The phase-cancellation proof makes this independent of the representative gP. It supplies the chosen isomorphism C[G/P]→R. The natural evaluation maps in §§4–5 then identify the original source with

    Z⊗V⊗V ≅ V1⊗R⊗M.

Under this identification an N-intertwiner F is id_V1⊗Φ for a unique G-intertwiner Φ:R⊗M→S. Define its certificate by

    t_F(m) = Φ(r_x0⊗m),        t_F ∈ Hom_P(M,S).       (13)

Conversely, every P-intertwiner t:M→S gives the unique G-intertwiner

    Φ_t(r_(g x0)⊗m) = g·t(g^(−1)·m),                (14)

extended linearly. Replacing g by gp leaves this expression unchanged because t is P-equivariant. Equivariance under G is immediate by replacing g with hg. Formula (14), followed by the inverse source identification, reconstructs F. In particular (13) and (14) are mutual inverses, not merely a dimension comparison. No averaging normalization or coset-count factor occurs for this permutation-basis convention.

Here is the precise weight coincidence that turns t into four scalars. The primary appendix identifies W′ as the Galois conjugate obtained by ζ↦ζ². Thus, after labeling a≠0,

    W|P = χ^a ⊕ χ^(−a),
    W′|P = χ^(2a) ⊕ χ^(−2a),
    U′|P = Sym²W′|P = 1 ⊕ χ^a ⊕ χ^(−a).

The last equality uses 4a≡−a modulo 5. Therefore

    M|P = 1 ⊕ 2χ^a ⊕ 2χ^(−a),
    S|P = χ^a ⊕ χ^(−a) ⊕ χ^(2a) ⊕ χ^(−2a).      (15)

The two multiplicity-two weights in M are genuine coincidences: one line comes from the alternating-input summand W and one from the symmetric-input summand U′. They are not four distinct source characters.

Choose eigenvectors w_± in W of characters χ^(±a), u_± in U′ of those same characters, u0 in its trivial line, and s_± in S of characters χ^(±a). The map t is specified uniquely by

    t(w_+) = α_+ s_+,       t(w_−) = α_− s_−,
    t(u_+) = β_+ s_+,       t(u_−) = β_− s_−,
    t(u0) = 0.                                      (16)

There is no map into the χ^(±2a) lines of S from the selected base-coset component because those characters are absent in M. The full reconstruction (14) nevertheless uses the whole irreducible target under G. The α pair is the alternating-slot sector and the β pair is the symmetric-slot sector.

If a basis-free projection is preferred, for any P-module E define the character projector

    π_(E,r) = (1/5) Σ_(k=0)^4 ζ^(−rk) p^k |_E.

This is an abstract finite-group averaging formula, not an evaluated representation matrix. The four components are

    π_(S,±a) t π_(W,±a),
    π_(S,±a) t π_(U′,±a),                            (17)

each belonging to a one-dimensional Hom space. Every other character component is forced to vanish. Their simultaneous vanishing is equivalent to t=0 and, by reconstruction, to F=0. After fixing the choices above, any one nonzero component certifies nonzero F and hence surjectivity onto U2. None of (13)–(17) evaluates the actual operation or any component of it.

Changing p, ζ, x0, J, or eigenvector normalizations relabels or rescales the resulting certificate according to the stated identifications. There is no claimed canonical ordered basis of the four-dimensional parameter space. The intrinsic statement is the Hom_P(M,S) parametrization relative to the chosen base character and N-isomorphism, with the canonical symmetric/exterior source decomposition retained.

As a further consequence of (5), the middle ordering m101 equals −2F_sym. Its vanishing alone would set β_+=β_−=0, leaving the two alternating-slot parameters; it would not imply that m011 vanishes.

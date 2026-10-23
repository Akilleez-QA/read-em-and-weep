# Forced S contractions and a common constant target for both branches

Work over C with the standard G=2I action and parameter line T=P(W*). The two branches below are conditional on the existing actual scalar λ, whose value is not evaluated.

## 1. Immutable interface and statement

INPUTS.json authenticates these originals:

- DOUBLET: PR1007, commit560bcac8eabcea4d3a7836147520ea48430a6a02, research/hm/unique-doublet-reduction/PROOF.md. It constructs the actual exact sequence

      0→E22 O(-1) --f--> Z26→Q→0,
      E22=W'⊕2S⊕2T6,
      R24=A⊕V⊕2P⊕2D,

  where Z26 admits equivariant splittings R24 O⊕W O(1) if λ≠0, or (1⊕R24) O⊕O(2) if λ=0. These splittings are not canonical. The actual bundle and maps are canonical before choosing them.
- QUOTIENT: PR996, commit54dc2b2b301f8a7e453b3101d5813c643beed71a, research/hm/opposite-second-degree-bound/PROOF.md, Section6. For λ≠0, Q has one of the four types O(12)⊕V O(4), O(18)⊕A O(2), W' O(5)⊕W' O(7), P O(6), all with degrees at least two. For λ=0 it has the types O⊕O(14)⊕W' O(5), O⊕O(18)⊕W O(3), O⊕V O(8).

Set E18=W'⊕S⊕2T6. For every choice of the indicated target splitting, we construct an actual residual presentation with the common constant target R24 O:

    λ≠0: 0→W O(-3)⊕E18 O(-1)→R24 O→Q→0,         (1)
    λ=0: 0→A O(-2)⊕E18 O(-1)→R24 O→Q3→0.        (2)

Here Q3 is the positive rank-three degree24 summand of Q, with types O(14)⊕W' O(5), O(18)⊕W O(3), or V O(8). The source identifications and the displayed maps depend on complement choices; they are not claimed canonical. They are induced from the actual f, not selected independently from representation multiplicities. Both source maps inject on every fiber.

## 2. Two universal S quotient sequences

Recall S=Sym³W and A=Sym²W. There are exact equivariant sequences

    0→W O(-3)→S O(-1) --u--> W O(1)→0,           (3)
    0→A O(-2)→S O(-1) --v--> O(2)→0.             (4)

For (3), take the degree-(1,2) symmetric polarization Sym³W→W⊗Sym²W and evaluate its last two factors against the tautological quotient W O→O(1). After twisting by O(-1), this gives u. Its kernel consists of cubics divisible by the square of the tautological kernel line O(-1)⊂W O. Multiplication therefore identifies the kernel with W O(-3).

For completeness, this kernel description is elementary and uniform: over any trivialization with a generator l of the kernel line and a complementary generator m, the cubic expressions l³ and l²m are killed, while lm² and m³ map to nonzero multiples of l and m tensored with the square of the quotient generator. Thus the quotient map is onto and its kernel is exactly l²W. This is a proof for a universal two-space and arbitrary line, not an evaluation of any actual HM coefficient or selected parameter.

For (4), use the complete-evaluation sequence of O(3), whose kernel is Sym²W O(-1), and twist by O(-1).

The fixed identities W⊗A=W⊕S and H0(O(3))=S show that

    Hom_G(S O(-1),W O(1))=C u,
    Hom_G(S O(-1),O(2))=C v.                     (5)

Neither W' nor T6 contributes to these Hom spaces. Consequently every nonzero map from E22 O(-1) to either positive target in (5) uses a nonzero functional on the two-dimensional S multiplicity space and is automatically onto on every fiber.

## 3. The nonzero-λ branch

Choose an equivariant splitting Z26=R24 O⊕W O(1), and let g be the composition of the actual f with projection to W O(1). The map g is nonzero. Otherwise the target projection would descend to a surjection Q→W O(1). But every splitting degree of Q is at least two, so Hom(Q,W O(1))=0 even without imposing equivariance.

By (5), g is a nonzero S-multiplicity functional times u and is therefore onto. Let K20=ker g. Its quotient by the unused constant-multiplicity source is the universal kernel in (3). Choosing a complement to the kernel of the S-multiplicity functional gives

    K20 ≅ E18 O(-1)⊕W O(-3).                     (6)

The splitting is not asserted canonical. Equivalently, the associated extension splits because H1(O(2))=0.

Apply the kernel-cokernel exact sequence to projection onto W O(1). Since g is onto, the actual f restricted to K20 lands in R24 O and gives

    0→K20→R24 O→Q→0.

This proves (1). The quotient Q is locally free, hence this actual residual map injects on all fibers.

## 4. Remove the forced zero trivial row first when λ=0

Choose an equivariant splitting

    Z26=O⊕R24 O⊕O(2).

The component of f into the trivial O is automatically zero, because

    Hom_G(E22 O(-1),O)=Hom_G(E22,W)=0.             (7)

Thus its cokernel splits off that actual trivial target summand, giving

    Q=O⊕Q3,
    0→E22 O(-1)→R24 O⊕O(2)→Q3→0.               (8)

This removes the trivial target before the next S contraction; no potentially nonzero quadratic source row is silently discarded. It also agrees with the intrinsic splitting of Q: its unique invariant global section generates the trivial summand, and its unique invariant quotient to O has this section as a nonzero inverse up to scalar. The positive summand Q3 has no degree-zero atom and no invariant global section, as is also seen from H0(Q)=1⊕2A⊕V⊕2P⊕2D. Hence that trivial factor and Q3 are intrinsic, although the chosen splitting of Z26 is not.

Let h be the actual source projection in (8) to O(2). It must be nonzero, since otherwise (8) would give Q3→O(2) onto. All three Q3 types have every degree strictly greater than two, so Hom(Q3,O(2))=0. By (5), h is a nonzero S-multiplicity functional times v and is onto on every fiber. Its kernel K21 has the noncanonical splitting

    K21 ≅ E18 O(-1)⊕A O(-2),                    (9)

using a multiplicity complement, or H1(O(1))=0. Taking kernels in (8) yields

    0→K21→R24 O→Q3→0,

which proves (2), including fiberwise injectivity.

## 5. Choices, numerical checks and contribution

The nonzero S projection is forced for every permitted choice of target splitting, not only for a specially favorable one. The resulting functional on the two S copies, its kernel subbundle and the map to the chosen R24 complement must be retained. Changing the target splitting can change these actual maps; the proof does not identify them by fiat. Once choices are fixed, every operation above is a kernel or quotient of the actual original diagram.

In (1), the source rank is2+18=20 and degree is−6−18=−24; its constant target has rank24, so Q has rank4 and degree24. In (2), the source rank is3+18=21 and degree is likewise−6−18=−24, giving Q3 rank3 and degree24. All standard central linearizations match.

The new step forces a nonzero S channel in both branches, proves its actual projection is everywhere onto by universal identities, and replaces the nonuniform rank26 target with the common constant R24 target. It does not select λ, eliminate a remaining actual C type, decide the top obstruction or vertex scalar, or change any source/frontier ledger. No selected actual coefficients, points, parameters, jets, derivatives, matrices, instance ranks or large scans are used.

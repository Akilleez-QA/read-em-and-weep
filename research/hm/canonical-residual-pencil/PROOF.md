# Canonical actual cancellation after the degree-two quotient

Work over C on the negative parameter line T=P(W*), with its standard G=2I linearizations. All representation names are in the current convention. No selected actual HM/source coefficient, point, parameter, jet, derivative, matrix or instance rank is evaluated.

## 1. Immutable input interface

The two exact originals in INPUTS.json are:

- TYPES: PR948, commit d1d5ca5915b734d018665c2b02a4426c8225d799, research/hm/opposite-bundle-classification/PROOF.md. Its Sections1–2 retain the actual complete-evaluation presentation

      0→E26 O(-1) --Γ--> H31 O→C→0,
      E26=2W⊕W'⊕2S⊕2T6,
      H31=1⊕3A⊕V⊕2P⊕2D=H0(C).

  The presentation is exact with C locally free on the entire parameter line. These are the actual reduced maps, not arbitrary pencils with the same characters.
- QUOTIENT: PR996, commit54dc2b2b301f8a7e453b3101d5813c643beed71a, research/hm/opposite-second-degree-bound/PROOF.md. It proves Hom_G(C,O(2)) is one-dimensional, every nonzero member q is onto, and its scalar-independent kernel Q is one of the seven explicitly stated rank-four degree24 bundles. Each Q is globally generated. The first four possibilities (rows9,10,14,15) are ample, while the last three (rows17,18,20) have exactly one trivial O summand.

We prove a canonical actual residual pencil

    0→E24 O(-1) --Γ_Q--> H28 O→Q→0,
    E24=W⊕W'⊕2S⊕2T6,
    H28=1⊕2A⊕V⊕2P⊕2D.                            (1)

Its source injects on every fiber. In particular one actual W source direction is necessarily cancelled, not merely permitted by the representation dimensions.

## 2. The canonical evaluation diagram

Fix any nonzero q in the line Hom_G(C,O(2)). All kernels below are unchanged if q is rescaled. Since Q is globally generated on P1, H1(Q)=0. Taking sections of the quotient sequence therefore gives an exact sequence

    0→H0(Q)→H0(C) --H0(q)--> H0(O(2))=A→0.         (2)

Put H28=H0(Q), regarded as the actual kernel in H31. Semisimplicity determines its displayed character in (1), but no complement is selected.

Apply the complete-evaluation maps to (2) and to 0→Q→C→O(2)→0. This gives a commutative diagram with exact rows

    0→H28 O→H31 O→A O→0
          ↓       ↓      ↓
    0→Q────→C────→O(2)→0.

All three vertical arrows are onto, including the first because Q is globally generated. Their kernels form the exact sequence

    0→M_Q→E26 O(-1) --ρ--> W O(-1)→0,             (3)

where the right kernel is the usual complete-evaluation kernel of O(2). Every map between the two O(-1)-twisted constant bundles is constant on T. Thus ρ is induced by an actual equivariant surjection E26→W. Its kernel E24 has the character in (1), and M_Q=E24 O(-1). The left evaluation sequence now proves (1).

All this is functorial in q. Scaling q scales the induced quotient maps without changing their kernels or Γ_Q. Thus E24 is a canonical subrepresentation of the actual E26, and H28 a canonical subrepresentation of H31; these subspaces are not selected from their characters. The named abstract representation isomorphisms need not be canonical.

Since Q is locally free, (1) remains exact on fibers. This proves fiberwise injectivity of the actual 24→28 residual pencil, including exceptional parameters.

## 3. Why the W projection cannot vanish

For a complementary direct view, let J=ker[H31 O→C→O(2)]. The evaluation diagram gives

    0→H28 O→J→W O(-1)→0,
    0→E26 O(-1)→J→Q→0.

The first extension admits an equivariant splitting, since its ordinary Ext1 is H1(O(1)) tensored with a constant space and vanishes. No splitting is chosen in the proof. If the composite E26 O(-1)→J→W O(-1) were zero, Q would surject onto W O(-1). A quotient of a globally generated bundle is globally generated, whereas W O(-1) has no sections and positive rank. This is impossible. Schur's lemma therefore forces the constant source quotient onto W. This recovers precisely (3), and explains structurally why an actual cancellation is compulsory.

## 4. The only remaining complete-coefficient defect is scalar

Let Ψ_Q:W⊗E24→H28 be the complete two-coefficient map of Γ_Q. Dualizing (1) and taking global sections identifies

    (coker Ψ_Q)*=H0(Q*).                            (4)

As with the original pencil, W and W* coefficient conventions are identified by the determinant pairing. This invertible identification does not alter (4).

The seven actual possibilities from QUOTIENT give H0(Q*)=0 in rows9,10,14,15, and H0(Q*)=1 in rows17,18,20. Hence every nontrivial irreducible target component of Ψ_Q is necessarily onto. Its only possible failure is a one-dimensional trivial quotient.

The fixed character identity is

    W⊗E24=1⊕3A⊕2V⊕3P⊕4D.

There is exactly one invariant source line and exactly one invariant target line. Thus the restriction

    Ψ_Q^G:(W⊗E24)^G→H28^G                         (5)

is a map between two canonical one-dimensional spaces. It is nonzero exactly when Q is ample, equivalently when the canonical quotient C→O(2) splits equivariantly. In that case the complete coefficient map Ψ_Q is onto. It is zero exactly in the Euler cases17,18,20, and then coker Ψ_Q is precisely the trivial line.

Equation (5) is retained as an actual unevaluated scalar gate. The proof does not assign its value, infer it from representation multiplicities, or conflate complete-coefficient surjectivity with surjectivity of a selected 24→28 fiber map.

## 5. Contribution and limits

The result removes an unavoidable actual W source/target evaluation block and produces a canonical smaller pencil for the already constructed rank-four kernel. Its map, source subrepresentation and target subrepresentation are inherited from the actual geometry. The next complete-coefficient defect is reduced to a single invariant line; all nontrivial target channels are forced onto.

The seven possibilities are not cut further here, and row9 remains the sole potentially nontrivial vertex-extension case. No actual row, top obstruction rank or vertex scalar is chosen. This is an actual functorial reduction rather than an abstract replacement pencil or a repetition of the seven-row list.

## 6. Basis-free incidence of two quotient lines

There is also a canonical interpretation before the W cancellation. Set I=(W⊗E26)^G, a two-dimensional space. The complete original coefficient map gives a nonzero functional

    a:I→H31^G.

It is onto because C is ample by QUOTIENT's interface: dualizing its original evaluation resolution gives (coker Ψ_C)*=H0(C*)=0. The actual source quotient ρ from (3) gives a second nonzero functional

    b:I→(W⊗W)^G.

The invariant source line of Ψ_Q is precisely ker b. The target line H28^G equals H31^G canonically, since their quotient A has no invariant vectors. Consequently (5) is exactly a restricted to ker b.

Thus the scalar gate vanishes if and only if ker a=ker b, equivalently the two quotient functionals are proportional after identifying their one-dimensional targets. It is nonzero if and only if their exterior product is nonzero in Λ²I* tensored with the two target lines. This criterion uses no bases or selected coefficients. The defect is zero in the nonzero-gate case; in the zero-gate case the defect is one-dimensional. The incidence between these actual quotient lines remains unselected.

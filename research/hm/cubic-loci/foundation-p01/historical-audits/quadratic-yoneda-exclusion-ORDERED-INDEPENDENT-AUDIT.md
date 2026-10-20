# Historical scope-limited review receipt

This review concerns the original source, possibly a larger scope than the excerpt in this unit. It is not a review of normalized publication bytes.

# Independent audit of the rank-two ordered Yoneda extension

## Verdict

**PASS. No mathematical correction required in `ORDERED-PRODUCT-ADDENDUM.md`, under the established inputs in `PROOF.md`.** The rank-two identity supplies precisely the extra argument that the earlier proof deliberately left open: all ordered products of two deck-invariant degree-one classes vanish. Together with the previously established singleton-character representation, this excludes invariant type [22] from the image of the full ordinary ordered Yoneda map.

The earlier `PROOF.md` is unchanged. Its SHA-256 at review is:

`a058c6b37bbc421f7767fb187a4a9856f1e3d35758516727b5567a5fb91cdb73`

This audit first checked the proposed extension independently and then reviewed the complete producer's addendum. The final document-binding note below records the exact reviewed addendum bytes.

## 1. Rank-two identity: the sign and coefficient are correct

Let E be a holomorphic vector bundle of rank two on a complex manifold. Write End_0(E) for the kernel of its trace. For local trace-free endomorphisms A and B, Cayley–Hamilton in rank two gives

    A² = (1/2) tr(A²) Id_E.

Polarizing this identity gives

    AB + BA = tr(AB) Id_E.

This is a universal identity of bundle morphisms; it is invariant under changes of frame.

For End_0(E)-valued (0,1)-forms, write locally

    α = Σ_i A_i d z̄_i,       β = Σ_j B_j d z̄_j.

Then

    α∧β = Σ_ij A_i B_j d z̄_i∧d z̄_j,
    β∧α = −Σ_ij B_j A_i d z̄_i∧d z̄_j.

Consequently

    α∧β − β∧α
      = Σ_ij (A_i B_j + B_j A_i) d z̄_i∧d z̄_j
      = tr(α∧β) Id_E.                                  (1)

In particular the subtraction on the left is correct. Substituting addition would incorrectly retain matrix commutators instead of anticommutators. There is no factor 1/2 in (1). As a normalization check, graded cyclicity gives tr(β∧α)=−tr(α∧β), so taking traces in (1) yields 2 tr(α∧β) on both sides, using rank(E)=2.

Closedness is unnecessary for the identity of forms itself. It is used when passing to cohomology. If α and β are ∂̄-closed, so is their product, since ∂̄ is a graded derivation of the End(E)-valued Dolbeault algebra.

The ordinary difference in (1) must not be confused with the graded Lie bracket on degree-one elements: the latter is α∧β+β∧α. These two different combinations supply the two separate equalities needed below.

## 2. Trace-free representatives exist globally

In characteristic different from two there is a canonical, globally defined splitting of holomorphic vector bundles

    End(E) = End_0(E) ⊕ O_X Id_E,
    p_0(T) = T − (1/2) tr(T) Id_E.

The identity section is global, and trace is invariant under conjugation. This splitting therefore also respects the stipulated deck and permutation actions. No trivialization of E or splitting of E itself is needed.

For a∈H¹(End(E)), the condition tr(a)=0 says exactly that a comes from H¹(End_0(E)). A direct representative argument makes this explicit. Start with a global ∂̄-closed End(E)-valued (0,1)-form α_0. If tr(a)=0, Dolbeault exactness gives a global smooth scalar function f with

    tr(α_0)=∂̄f.

Then

    α = α_0 − (1/2)(∂̄f) Id_E

is closed, represents the same class as α_0, and has pointwise trace zero. Indeed the correction is ∂̄((f/2) Id_E), since Id_E is holomorphic. Equivalently, p_0(α_0) represents a whenever its scalar cohomology summand vanishes.

For the given deck group G, trace is equivariant. Thus every invariant class a∈Ext¹(E,E)^G has trace in H¹(O_X)^G. The stipulated elliptic involutions act by −1 on H¹(O_C). Künneth decomposes H¹(O_X) as the four singleton characters, and H²(O_X) as the six distinct two-factor characters. None is trivial. Hence

    H¹(O_X)^G = H²(O_X)^G = 0.                          (2)

Alternatively, the finite quotient X/G=Y=(P¹)^4 and exactness of invariants in characteristic zero give H^j(O_X)^G=H^j(O_Y)=0 for j>0.

It follows that all invariant degree-one classes admit the global trace-free representatives needed in (1). Such representatives need not be strictly G-invariant for the cohomological argument; if desired, averaging preserves closedness, trace-freeness, and the invariant represented class.

## 3. The Dolbeault product is the ordinary Yoneda product

The stipulated E is an honest vector bundle, not merely a complex with unresolved cohomology. Therefore sheaf Ext in positive degree vanishes and

    Ext^j_X(E,E) = H^j(X,End(E)).

On the complex projective variety, algebraic and analytic coherent cohomology agree. The global Dolbeault complex of End(E) is a differential graded algebra under wedge product of forms and composition of endomorphisms. It computes the derived endomorphism algebra, and its multiplication induces the ordinary Yoneda composition on Ext. These comparisons respect trace, the identity inclusion O_X→End(E), and the finite-group actions.

Choose the convention in which α∧β represents ab. Reversing the convention consistently reverses both ordered products and leaves all vanishing conclusions unchanged. Equation (1) gives the cohomological identity

    ab − ba = ι_*(tr(ab)),                              (3)

for any trace-zero classes a,b∈Ext¹(E,E), where ι(f)=f Id_E. The notation on the right means the scalar degree-two cohomology class mapped into H²(End(E)); it is not a claim that the scalar class is a constant.

When a,b are G-invariant, their product and its trace are G-invariant. By (2), tr(ab)=0. Thus

    ab − ba = 0.                                       (4)

At the form level, tr(α∧β)=∂̄η for some global scalar (0,1)-form η, so (1) is ∂̄(η Id_E). The proof does not require the scalar product to vanish pointwise.

There is also a purely cohomological interpretation: on End_0(E)⊗End_0(E), symmetrizing the endomorphism multiplication yields trace times identity, while interchanging two degree-one sheaf-cohomology factors contributes a minus sign. This gives (3) without asserting that a chosen Čech cup product satisfies the identity strictly on cochains. The Dolbeault argument is a valid strict model over C and avoids that potential cochain-level overstatement.

## 4. The smooth family supplies the independent second equality

The established smooth 79-dimensional coefficient family has Kodaira–Spencer image equal to V_0=Ext¹(E,E)^G. Each v∈V_0 consequently extends to second order, so its ordinary primary obstruction satisfies v²=0 in Ext²(E,E). This uses the ordinary deformation obstruction, not an additional claim about strict representatives.

Applying the same fact to a+b and subtracting a² and b² gives

    ab + ba = 0.                                       (5)

Equations (4) and (5), together with invertibility of 2, give

    ab = ba = 0   for every a,b∈V_0.                    (6)

The family alone yields (5), and the rank-two argument with the two scalar-cohomology vanishings yields (4). Neither input on its own establishes (6). This is why the new argument legitimately strengthens the older proof rather than correcting a false claim in it.

## 5. Passage to all ordered products

The established character calculation in `PROOF.md` gives

    V=Ext¹(E,E)=V_0 ⊕ V_1 ⊕ V_2 ⊕ V_3 ⊕ V_4,

where V_i has singleton deck character χ_i and the singleton sum, compatibly with this grading, is U⊗k⁴_perm. The stabilizer S3 acts trivially on U. This audit imports that established representation calculation; it does not re-evaluate its underlying model.

Because all deck characters have order two and the χ_i are distinct,

    (V⊗V)^G = (V_0⊗V_0) ⊕ ⊕_i(V_i⊗V_i).            (7)

The first summand maps to zero by (6). The second is, as an S4-module,

    (U⊗U) ⊗ k⁴_perm
      = (U⊗U) ⊗ ([4] ⊕ [31]),                         (8)

with trivial S4 action on U⊗U. In particular (8) contains no [22]. The Yoneda map is equivariant, and finite-group representations are semisimple in characteristic zero, so its image from this summand cannot contain [22].

This proves the precise full ordered statement

    pr_(G-invariant,[22]) ∘ μ = 0,
    μ:V⊗V→Ext²(E,E),    μ(a⊗b)=ab.                     (9)

Equation (9) applies to arbitrary ordered products a,b, even when a and b are not character-homogeneous. Indeed projection to the invariant target is the product map applied to the invariant projection of its source, and (7) lists every possible contribution. There is no need to assume the image of a single product is itself invariant.

## 6. Serre annihilation has exactly the stated character

On X=C⁴, the scalar target H⁴(O_X) is one-dimensional with character χ_all⊗sgn for G⋊S4. The middle-degree trace/Serre pairing is perfect and equivariant:

    Ext²(E,E)⊗Ext²(E,E)→H⁴(O_X).

Thus a full-deck-character class pairs only with the deck-invariant part of a potential detector. For S4, [22] is self-dual and is preserved by tensoring with sgn. Consequently a full-deck [22] class pairs only with the invariant [22] component. Equation (9) annihilates exactly that component for every ordinary ordered degree-one Yoneda product.

The entire linear span of such products therefore Serre-annihilates the full-deck [22] target. This does not require the individual products to vanish in other deck characters or in other S4 types.

## 7. Rational descent and arbitrary characteristic-zero base change

The Dolbeault argument is made over C. For the stipulated rational data, X, E, the group actions, trace, identity inclusion, and Yoneda multiplication are defined over Q. Proper coherent cohomology of these bundles commutes with field extension. The finite-group averaging idempotents are rational, as is the S4 central idempotent for [22], so invariant and isotypic projections commute with extension as well.

The restrictions of the product map in (6), and the composite in (9), are therefore Q-linear maps whose extensions to C vanish. Faithful scalar extension Q→C implies that those Q-linear maps already vanish. Extending from Q to any characteristic-zero field k preserves their vanishing. This argument does not require an embedding of k into C.

Products, not just the dimensions of their source and target, commute with this base change because the coherent-cohomology comparison is functorial and compatible with cup product and composition. A dimension comparison alone would not suffice, and is not being used in place of this compatibility.

The conclusion concerns the stipulated rational objects and their base changes. It makes no assertion about arbitrary characteristic-zero forms not identified with them, positive characteristic, or changing the specified group action.

## 8. Limits and evidence boundary

The extension proves more than the earlier polarized exclusion in exactly one needed direction: it eliminates the invariant–invariant alternating ordered-product possibility by proving all invariant–invariant ordered products vanish. It does not prove that all ordered products vanish, that the retained full-deck [22] obstruction class is zero, that the complete deformation problem is unobstructed, or that all possible detectors are ordinary Yoneda products. Higher operations and unrelated detector constructions remain outside the conclusion.

Rank two is essential for identity (1). Vanishing of the scalar invariant cohomology in both degrees one and two is essential to the stated deduction, as is the separate smooth-family input for the symmetric combination. No general commutativity assertion for Ext of arbitrary vector bundles is made.

Only static local proof-document reads, formal mathematical reasoning, local audit writing, and file-content hashing were used. No source/model/rank/polynomial-instance/point/jet/residual evaluation or execution, no external write, and no modification of `PROOF.md` was performed.

## Final document binding

Reviewed document: `ORDERED-PRODUCT-ADDENDUM.md`, titled **Addendum: all ordinary ordered Yoneda products are excluded**.

Reviewed addendum SHA-256:

`5d646aa98afe24b98195dfd078e237c7502bd615157469b346d4823898d6e346`

The complete addendum was read after the independent mathematical checks above. All six sections agree with those checks. In particular, the addendum states the coefficient-one identity with the correct subtraction sign; uses cohomological, rather than pointwise, vanishing of the scalar trace product; keeps the separate smooth-family input; handles the complete ordered tensor source; and descends the product maps, rather than only dimensions, from C to Q and then to the stipulated characteristic-zero base changes. Its scope limitations are appropriate.

The PASS verdict binds these exact addendum bytes. The original `PROOF.md` hash was rechecked and still equals the unchanged hash recorded above. The earlier proof and both earlier audit files were not modified.

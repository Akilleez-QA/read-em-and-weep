# Binary geometry selects the unique equivariant splitting

## Scope convention

The assertions below concern coefficient geometry, finite-group actions and the stated coherent cohomology. References to unevaluated coordinates mean that this argument does not evaluate them; they are not a claim about the latest status of every other argument. The raw-source regularity, coefficient/character identification and raw-to-canonical class comparison are separate hypotheses wherever a source application is discussed. No first-order lifting theorem, higher-order obstruction vanishing, formal integrability or algebraicity follows merely from these coefficient statements.

## Statement and scope

Over C, let dim V=2 and let m:P(Sym²V)×P(Sym²V)→P(Sym⁴V) be multiplication, with consistent dual projective conventions. Put F=m_*O_X, let F⁺ be its factor-exchange invariant subalgebra, G=ker(Tr_F:F⁺→O_Y), W=H⁰(Y,G(1)), L=im(W⊗O_Y(−1)→G), and Q=G/L. The rank-six algebra trace satisfies Tr_F(1)=6. The evaluation map is a subbundle inclusion by the stated splitting type. Under the imported splitting type G≅O(-1)⊕O(-2), the exact sequence

0→L→G→Q→0

has a unique SL(V)-equivariant splitting. It is automatically GL(V)-equivariant. This selects a canonical splitting **relative to the specified binary-form geometry and its natural action**. It is not a canonical splitting of an arbitrary abstract extension with the same line-bundle types.

Consequently the retained obstruction has unconditional, geometry-selected ten- and twenty-dimensional projections. Neither projection is shown zero. The staged, choice-free kernel class in the audited comment agrees with the geometry-selected twenty-component whenever the ten-component is zero.

## Proof

1. Multiplication, the factor exchange, the algebra unit, and algebra trace are GL(V)-equivariant. Hence F, F^+, G have natural linearizations. The polarization O_Y(1) has its natural linearization, so W=H0(G(1)) is a representation, and evaluation W⊗O(-1)→G is equivariant. Its subbundle image L and quotient Q inherit their linearizations. All of this is algebraic on the whole projective base, including ramification.

2. Under SL(V), any one-dimensional algebraic representation is trivial, so W is trivial. The standard linearization on O(-2) is also the only SL(V) linearization up to equivariant identification: two linearizations on the same line bundle differ by a character, since invertible global functions on projective Y are constants, and SL(V) has no nontrivial characters. Thus Q, already known to have underlying line bundle O(-2), has the standard SL(V) linearization. The same conclusion applies to L of type O(-1). No determinant-character choice affects this SL(V) conclusion. With the usual convention Y=P(Sym⁴V), the natural GL(V) types retain W≅(det V*)², L≅(det V*)²⊗O(-1), and Q≅(det V*)⁴⊗O(-2). W is not asserted GL(V)-trivial; the determinant factors cancel the scalar-center action on the two coefficient lines. The proof uses only their SL(V) restrictions.

3. The underlying extension splits because Ext1(Q,L)=H1(L⊗Q*)=H1(O(1))=0. Equivalently, the equivariant map of finite-dimensional rational SL(V)-representations

Hom_Y(Q,G)→Hom_Y(Q,Q)

is onto, and the target contains the invariant element Id_Q. In characteristic zero, SL(V) is linearly reductive, so taking invariants is exact. Id_Q therefore has an invariant lift s:Q→G. It satisfies quotient∘s=Id_Q and is an equivariant splitting. This does not incorrectly equate ordinary Ext-vanishing with equivariant Ext-vanishing; exactness of invariants supplies the necessary additional step.

4. If s and s' are two equivariant splittings, their difference belongs to

Hom_Y(Q,L)^{SL(V)} = H0(Y,O(1))^{SL(V)}.

Under the natural action this is the space of invariants in the irreducible binary-quartic representation Sym⁴(V*) (or its dual according to the chosen projective convention). It has no nonzero invariant. Therefore s=s'. In particular the central element -Id of SL2 causes no exception: all relevant polynomial degrees are even and the binary quartic remains a nontrivial irreducible representation of PSL2.

5. For any g∈GL(V), transport s by the natural linearizations. Because SL(V) is normal in GL(V), the transported splitting is again SL(V)-equivariant. Uniqueness forces it to equal s. Hence s is GL(V)-equivariant. It is also preserved under changes of binary coordinates by projective linear transformations, and requires neither a chosen volume form on V nor an averaging measure. Reductivity is used to prove existence, not to choose an auxiliary integral.

6. The actual sheaf maps i:L→G and s:Q→G give the canonical relative decomposition G=i(L)⊕s(Q). Dualizing and tensoring with any vector bundle B0⊗omega_Y gives

B0⊗G*⊗omega_Y ≅ (B0⊗Q*⊗omega_Y) ⊕ (B0⊗L*⊗omega_Y).

No SL(V) linearization on B0 is required: these are O_Y-linear maps that can be tensored with the identity of any B0. Thus HM's lack of an assumed SL2 symmetry is irrelevant to the existence of these coefficient projections. Passing to H2 gives the geometry-selected unconditional twenty-projection and the existing ten-quotient.

## Why this qualifies rather than invalidates the filtration

Without the natural group action, splittings form a nontrivial affine torsor under H0(O(1)), of dimension five. The abstract filtered bundle therefore supplies no preferred complement. The audited comment is correct at that restricted level. Its language should not be read as an impossibility theorem for the richer multiplication geometry: that geometry provides exactly the additional naturality condition that kills the five-dimensional ambiguity.

The canonical filtration, weighted trace formula, regular lifting criterion, and conditional uniqueness of the kernel class are unchanged. This argument constructs the already known projection by an alternative equivariant method, but supplies no equation setting its value to zero. It neither proves a mixed lift nor computes any of the thirty retained values.

## Review and public comparison

The accompanying REVIEW.md checks natural linearizations, the SL2 character argument, reductivity on global Hom, uniqueness, GL2 promotion, and tensoring with a nonequivariant B0. This is an alternative equivariant proof of the complement already proved by multiplication and trace in [the canonical cubic construction](https://github.com/Akilleez-QA/read-em-and-weep/blob/c5fb4a0bcc3c8e35093fcfcff9a73a79a45a18e5/research/hm/cubic-reconstruction/PROOF.md), not an additional canonical projection theorem.

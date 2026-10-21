# Generic doubled-conic simplicity from the next projective extension

## Theorem

Let F_R be the actual stable Steiner restriction of normalized HM to the positive fixed plane R=P2. Then, for a general smooth conic C in R,

       F_R|C = O_P1(-1)^2,
       H0(2C, End_0(F_R)|2C)=0.

Equivalently, the coefficient span of its actual first projective extension

       eta_C in H0(End_0(F_R)|C) tensor H1(O_P1(-4))

has dimension at least two. The equivalent actual squared multiplication

       q_C^2:H1(B_R(-4)) -> H1(B_R),  B_R=End_0(F_R),

is injective. Its source has dimension six by INVARIANT-CONIC-SECOND-NORMAL-COLLAPSE.md, but that dimension is not needed for the proof of injectivity.

The proof is a deformation argument using an actual next extension class. It does not assume generic rank, select a coefficient, or evaluate a matrix. The required input is stability, the actual Steiner resolution, and balance on the invariant conic with its actual A5 action. In particular the argument is independent of which irreducible three-space occurs in the Steiner relation space.

## 1. Every triple conic has only scalar endomorphisms

Write the actual Steiner resolution as

       0 -> A tensor O_R(-3) -> D tensor O_R(-2) -> F_R -> 0,
       dim A=3, dim D=5.

Since det(F_R)=O_R(-1), the trace-free adjoint is B_R=Sym^2(F_R)(1). The symmetric-square resolution, twisted to B_R(3), is

       0 -> wedge^2 A tensor O_R(-2)
         -> A tensor D tensor O_R(-1)
         -> Sym^2 D tensor O_R
         -> B_R(3) -> 0.

The negative line-bundle terms are acyclic on P2, so H1(B_R(3))=0. Self-duality of B_R and Serre duality then give H1(B_R(-6))=0. Stability gives H0(B_R)=0. For any nonzero conic equation q, the sequence

       0 -> B_R(-6) --q^3--> B_R -> B_R|3C -> 0

therefore proves

       H0(B_R|3C)=0.                                      (1)

This includes the invariant conic. It is a uniform cohomological vanishing, not a rank computation on a selected conic.

## 2. The class on a doubled balanced conic

Let C0 be the unique A5-invariant smooth conic. The actual conic theorem proves balance on C0. Put

       S=H0(B_C0),  T=H1(O_P1(-4)),  dim S=dim T=3.

The actual A5 modules S and T are irreducible. For T this follows from Serre duality and the irreducible plane representation. For S, write F_C0=O_P1(-1) tensor E with the binary group acting on E. Its central involution is negative, so E is an irreducible two-space: the perfect binary group has no nontrivial one-dimensional characters. Its determinant is trivial. The invariant alternating form and Schur's lemma exclude an invariant symmetric form, so Sym^2 E has no invariant vector. As A5 has no nontrivial two-dimensional representation, S=End_0(E)=Sym^2 E is irreducible.

The actual projective comparison class eta_C0 belongs to (S tensor T)^A5. If it is nonzero, its coefficient map T*->S is an isomorphism by Schur's lemma. Its coefficient span then already has dimension three, and the desired vanishing holds on C0 and on a nonempty open of nearby balanced conics.

It remains to treat eta_C0=0. For the actual HM representation this is indeed the case, as established separately in INVARIANT-CONIC-SECOND-NORMAL-COLLAPSE.md; the present proof does not need that additional representation calculation.

## 3. A nonzero next projective class

Assume eta_C0=0. Then the endomorphism algebra is projectively trivial on 2C0 relative to its evaluation trivialization on C0. This comparison is unique once fixed on C0: its automorphisms reducing to the identity form H0(B_C0 tensor O_P1(-4)), which is zero.

Choose local projective frames extending this comparison. Modulo q0 cubed, the actual projective transitions have the form

       g_ij = 1 + q0^2 a_ij.

The coefficients define the canonical next class

       psi in S tensor H1(O_P1(-8)).

Here the plane conormal has degree minus four on P1, and its square has degree minus eight. If psi vanished, the comparison would extend to 3C0, making B_R|3C0 the constant trace-free matrix bundle. That would give three independent global sections, contradicting (1). Therefore

       psi is nonzero.                                   (2)

The comparison and its class are A5-equivariant by their uniqueness. No splitting of the geometric conic neighborhood is assumed.

## 4. Exact derivative under motion of the conic

Let h be a tangent direction to conic parameters at C0, represented by a quadratic form modulo q0. Equivalently

       h|C0 in H0(O_P1(4)).

Over the dual numbers epsilon squared zero, move the conic to q_epsilon=q0-epsilon h. On its doubled neighborhood q_epsilon squared zero gives

       q0^2=2 epsilon h q_epsilon,
       q0^3=0.

Thus this moving doubled conic factors through the fixed third conic neighborhood. Pulling back the actual projective transitions gives

       g_ij=1+2 epsilon h q_epsilon a_ij.

Their reduction on the moving reduced conic is the identity, so this is a comparison relative to its evaluation frame. Consequently the derivative of the actual first extension is exactly

       d eta_(C0)(h)=2 h psi                              (3)

in S tensor H1(O_P1(-4)). Choosing q_epsilon=q0+epsilon h changes both displayed signs consistently and has no effect on nonvanishing.

This is an identity of actual comparison torsors. It is not a heuristic displacement of a formal coordinate: the relation q0^3=0 proves that the fixed third-neighborhood transitions suffice for the entire first-order moving doubled neighborhood.

The derivative in (3) is nonzero. Otherwise every h in H0(O_P1(4)) would annihilate psi. Serre duality would say that each coefficient of psi annihilates every product

       H0(O_P1(4)) times H0(O_P1(2)) -> H0(O_P1(6)).

This binary-polynomial multiplication is onto, contradicting (2).

## 5. Five tangent directions force noncommutativity

The tangent representation at the invariant conic is

       H0(O_P1(4)) = Sym^2(V*) / C q0 = 5,

the irreducible five-dimensional A5 representation. The derivative is equivariant. Its nonvanishing therefore makes its image a five-dimensional linear subspace of S tensor T, viewed intrinsically as maps T*->S.

A linear subspace of three-by-three matrices all of whose elements have rank at most one has dimension at most three. To see this, two rank-one tensors with independent left factors and independent right factors have a rank-two sum. Thus all members of a rank-at-most-one linear space must share a fixed left factor or share a fixed right factor, giving the bound three.

Hence some tangent direction h has d eta_(C0)(h) of rank at least two. Along the actual conic line q_t=q0-t h, a corresponding two-by-two minor of eta has leading term

       t^2 times the nonzero minor of d eta_(C0)(h).

It is therefore not identically zero. Smoothness and balance hold on an open neighborhood of C0, so this produces a nonempty open of smooth balanced conics whose extension coefficients span at least two dimensions. The conic parameter space is irreducible, so the property holds for a general smooth conic.

## 6. Algebraic variation and the exact section criterion

The passage from the derivative to an actual open condition is justified by cohomology and base change, not by an assumed trivialization of varying curves. Over the smooth balanced conic open, the relative bundles of constant adjoint sections and of H1 of the conormal have ranks three and three. Their tensor product has rank nine. The relative evaluation endomorphism algebra is an Azumaya algebra on the base; its pullback to the doubled universal conic is the reference comparison algebra. Local comparison torsors give the actual eta as an algebraic section of the rank-nine class bundle. These statements can be checked after an étale trivialization of that Azumaya algebra, which preserves the invariant rank condition.

At a point where eta vanishes, its derivative is independent of first-order choices of trivialization. Along the actual parameter line the vector bundles can be trivialized locally, making the minor expansion in Section 5 valid. The nonempty rank-at-least-two locus then descends and is open.

For any balanced C, the doubled restriction exact sequence gives an injective map H0(B_R|2C)->H0(B_C)=sl2. Its boundary is

       s |-> [eta_C,s].

The centralizer inside sl2 of a nonzero element is its one-dimensional span, including for nilpotent elements. Thus two linearly independent extension coefficients have zero common centralizer. Conversely zero or one-dimensional coefficient span has a nonzero common centralizer. This proves precisely the equivalence with H0(B_R|2C)=0 used in the theorem.

The actual affine second-normal law then supplies the stated further consequence: on a nonempty open of smooth even quadrics, the actual 15-to-63 top-normal commutator factor is injective. This consequence follows from the nonzero quadratic leading term in the negative block, as proved in ACTUAL-SECOND-NORMAL-AFFINE-LAW.md. It does not establish the remaining lower-order positive boundary or the odd full-adjoint gate.

## Dependencies and limits

The fixed-plane and actual-conic theorems provide stability, the Steiner presentation, the genuine normalizer action, and balance on C0. ACTUAL-SECOND-NORMAL-AFFINE-LAW.md at 028320f238a8a8cae5f14faf6b6836201baa496d supplies the actual comparison-torsor definition, the conormal Atiyah interface, and the generic negative-block implication. The new triple-conic vanishing, exact derivative, and five-dimensional rank-cone argument are proved here.

No selected HM/source coefficient, actual matrix-rank test, scan, or experiment is used. Generic doubled-conic simplicity and the resulting top-normal exclusion are not a claim of full adjoint vanishing or complete repair.

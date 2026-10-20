# Intrinsic canonical-valued bracket and its precise deformation meaning

## Result and scope

Let Y=C×C, with C the stipulated elliptic double cover of P¹, and let p:Y→S=Sym²(P¹)≅P² be the degree-eight quotient. Let G=(Z/2)²⋊S₂ and let χ be the one-dimensional character negative under either elliptic deck involution and under the inner swap. Write L=(p_*O_Y)_χ. The supplied finite-pushforward calculation gives the underlying line-bundle class L≅O_S(−3).

There is a more precise intrinsic statement. Put T=H⁰(Y,ω_Y), a one-dimensional constant vector space with G-character χ. Then

    L⊗T ≅ ω_S.                                             (1)

The normalization of (1) used below is multiplication into p_*ω_Y followed by (1/8) times the finite canonical trace. If Ω∈T is a nonzero volume form and π is its dual bivector, normalized by contraction ι_πΩ=1, the descended alternating biderivation

    B_π: O_S×O_S → L

becomes exactly

    j_Ω(B_π(f,g)) = df∧dg,                                  (2)

where j_Ω:L→ω_S is (1). Without a chosen volume, the target is ω_S⊗T*, and the nonzero bivector specifies its constant T* factor. Thus there is no unidentified variable factor and no hidden base twist. An arbitrary prior isomorphism L≅O(−3), followed by an arbitrary determinant convention O(−3)≅ω_S, instead produces a nonzero constant multiple of the wedge map.

This is a canonical-line-valued biderivation, not an ordinary Poisson bracket on P². Its first-order square-zero algebra meaning is rigorous; higher-order quantization, compatibility with the actual stipulated deformation, and module existence remain separate questions.

The proof uses only finite representations, finite duality, generic étaleness, and intrinsic exterior-algebra identities. No actual q/x/y function, Jacobian, source, physical model, jet, matrix product, or experimental evaluation is made.

## 1. The representation and the constant line

The deck involution of an elliptic double cover of P¹ acts by −1 on its one-dimensional space of holomorphic one-forms: the invariant space would descend to H⁰(P¹,ω)=0. Hence either deck involution acts by −1 on a product volume form on Y. The factor swap also acts by −1, because it exchanges two degree-one differential factors. Consequently T has character χ. The one-dimensional space H⁰(Y,Λ²T_Y)=T* has the same sign character.

In characteristic zero the character projector is exact. The stipulated pair-pushforward decomposition gives L a line bundle, with underlying class O(−3). In particular this is the full-deck-sign and inner-swap-odd summand, not the full-deck-sign/swap-even O(−2) summand.

A nonzero Ω trivializes ω_Y. Multiplication by Ω identifies L with the invariant part of p_*ω_Y. More invariantly, multiplication gives

    L⊗T ≅ (p_*ω_Y)^G.

Finite duality for the finite flat morphism between smooth surfaces gives

    p_*ω_Y ≅ Hom_O_S(p_*O_Y,ω_S).

Taking G-invariants and using (p_*O_Y)^G=O_S identifies this invariant summand with ω_S. One can describe the map as finite canonical trace, which under duality is evaluation at the unit. The trace restricted to invariants is an isomorphism; multiplying it by the nonzero constant 1/8 is also an isomorphism. We choose the latter because it is inverse to differential pullback on invariant top forms over the étale locus. Indeed Tr_p(p*η)=8η there. These equalities extend as sheaf morphisms on the integral smooth base. Thus

    j_Ω(l)=(1/8)Tr_p(lΩ).

It is important to specify this normalization: unnormalized finite trace would insert a factor eight into (2).

### Projective determinant conventions

If S=P(W) parametrizes lines in a three-dimensional vector space W, the Euler sequence gives

    ω_S ≅ O_S(−3)⊗det(W)*.

For the convention parametrizing one-dimensional quotients of W, the constant factor is instead det(W). Here W may be taken to be Sym²(V₀) in the lines convention, so det(W)=(det V₀)³. This is a constant one-dimensional vector space, not another line-bundle degree.

Combining the lines convention with (1) gives the precise formula

    L ≅ O_S(−3)⊗det(W)*⊗T*.

A notation L=O(−3) has suppressed the constant factor det(W)*⊗T*. A choice of Ω and of determinant trivialization converts all of these statements to familiar O(−3) notation. No particular numerical scalar relative to previously unspecified choices can be asserted. The normalization j_Ω above avoids that ambiguity entirely.

## 2. Descent and the symbol, without source evaluation

Fix a nonzero π∈H⁰(Y,Λ²T_Y). For a local pair f,g∈O_S define

    B_π(f,g)=π(d(p*f),d(p*g)).

This formula defines the operation; it does not evaluate it in any coordinate system. Since f and g are invariant while π has character χ, its output belongs to L. The ordinary derivation rule upstairs immediately gives the derivation rule in each argument downstairs. The operation is alternating and vanishes if either input is constant.

The universal property of Kähler differentials therefore produces an O_S-linear morphism

    β_π: Λ²Ω¹_S=ω_S → L,
    β_π(df∧dg)=B_π(f,g).                                    (3)

Equivalently, as a bidifferential operator, B_π has order at most one in each argument, no order-zero term, and alternating principal (1,1)-symbol β_π. The full tensor symbol is Ω¹_S⊗Ω¹_S→L given by exterior multiplication followed by β_π; whether one writes an antisymmetrization factor 1/2 depends only on the convention for embedding Λ² into a tensor square.

After any chosen identification L≅ω_S, (3) is an endomorphism of ω_S. Since H⁰(P²,O)=C, it is a constant multiple of the identity. This multiple is nonzero: over the nonempty étale locus of p, the differential identifies the pulled-back cotangent bundle with Ω¹_Y, and a nonzero symplectic bivector is nondegenerate. Hence its induced pairing of the generic cotangent space cannot be zero. This argument uses only the cotangent isomorphism of an étale map, with no Jacobian calculation.

For exact normalization take Ω with ι_πΩ=1. On a rank-two vector bundle the intrinsic exterior-algebra identity is

    α∧β=π(α,β)Ω.

Apply this to pulled-back one-forms over the étale locus and then apply (1/8)Tr_p. It gives j_Ω∘β_π=id_ω_S there, hence everywhere. This proves (2), including across ramification. With arbitrary Ω and π the constant is ι_πΩ. The assertion is purely tensorial; no values of the source functions or of their derivatives have been computed.

## 3. Why an ordinary Jacobi assertion would be wrong

The output of B_π lies in L, whereas its two declared inputs lie in O_S. Thus B_π(f,B_π(g,h)) is not even an expression of the declared type. A line-valued bracket on functions does not by itself carry an intrinsic Jacobi identity. One would have to supply additional operations involving sections of L, a connection or suitable graded algebra, or a genuine Jacobi-bracket structure on sections of a line bundle. None is supplied by (3) alone.

After a local trivialization of L, the coefficient operation is an ordinary bivector bracket on a surface. Such a local bivector has vanishing Schouten self-bracket for dimensional reasons. This does not supply the missing global nesting operation, nor make the operation an ordinary global Poisson bracket on S. The changes of trivialization still matter.

There is nevertheless a well-defined global first-order algebra construction. Regard L as its usual symmetric O_S-bimodule and put

    A_B=O_S⊕L,
    (f,u)·(g,v)=(fg, fv+gu+(1/2)B_π(f,g)).                  (4)

The ideal 0⊕L is central and square-zero. Every biderivation into a symmetric bimodule is a Hochschild 2-cocycle, so (4) is associative and has unit (1,0). Its commutator on lifted functions is B_π. Associativity at this first order requires precisely the Hochschild cocycle identity, not an iterated line-valued Jacobi expression. This is a sheaf of C-algebras with quotient O_S and ideal L; it is not an O_S-algebra with O_S central, since the displayed splitting is not multiplicative.

Formula (4) supplies an abstract canonical-twisted first-order thickening after the stated normalization. It is not an identification of any actual physical or previously stipulated deformation with that thickening. Higher-order extensions require new data and new compatibility conditions.

## 4. Two pairs and the global mixed coefficient

Apply the construction to S_z and S_h, writing L_z⊗T_z≅ω_z and L_h⊗T_h≅ω_h. On X=S_z×S_h the tensor product of the two first-order algebras has two square-zero ideals, and its mixed ideal has coefficient

    L_z⊠L_h ≅ ω_X⊗(T_z⊗T_h)*.

Fixing dual volumes removes the displayed constant factor, yielding ω_X=ω_z⊠ω_h. The mixed bidifferential on decomposable functions is the product of the two first-order bidifferentials. It is an operation of mixed bidegree (1,1) in the two deformation directions, not a newly established ordinary Poisson bracket on the fourfold. Its precise factor is 1/4 if both individual products use (1/2)B as in (4); this scalar is a convention of the product, not of the line-bundle identification.

This intrinsically explains why the stipulated full-deck-sign/both-inner-odd sector has coefficient ω_X. For E=m*HM, local freeness gives

    Ext²_X(E,E⊗ω_X)=H²(X,End(E)⊗ω_X).

Finite equivariant pushforward and projection formula identify the specified upstairs character sector with this group, with the same constant-line qualification. This is exactly the coefficient group of the supplied pair-quotient report. No assertion is made that a particular obstruction equals a particular class in this group, or that its value is nonzero or zero.

For a genuine mixed-order lifting problem, this group is the expected obstruction recipient only after the individual first-order lifts, the algebra extension, and their compatibility have been specified. In the locally free sheaf-of-algebras lifting framework, the mixed ideal is killed by both first-order ideals, so the resulting gluing obstruction has coefficient End(E)⊗ω_X on the reduced space. For arbitrary non-locally-free modules or an unspecified derived deformation problem, the correct derived obstruction theory must first be checked; the character computation alone does not establish it.

## 5. Stable plane fibers: scalar obstruction, conditional compensation

Let E be a stable plane bundle on S=P², as in the supplied good locus. Stability implies simplicity:

    Hom(E,E)=C·id_E.

Serre duality on the smooth proper surface then gives canonically

    Ext²(E,E⊗ω_S) ≅ Hom(E,E)* ≅ C.                         (5)

The final identification uses the distinguished identity endomorphism and the Serre trace. Equivalently, the sheaf trace induces an isomorphism

    tr: H²(End(E)⊗ω_S) → H²(ω_S) ≅ C.

In characteristic zero the splitting End(E)=O·id_E⊕End₀(E) implies

    H²(End₀(E)⊗ω_S)=0.

The scalar inclusion a↦a·id_E is likewise an isomorphism on H², but trace composed with this inclusion multiplies by rank(E). Thus “scalar” is exact, and the rank factor must be retained when one switches between trace coordinates and scalar-inclusion coordinates.

Consequently, IF a specified first-order canonical-twisted algebra/module lifting problem has obstruction in Ext²(E,E⊗ω_S), that fiber obstruction has only a scalar component. This does not show it vanishes. In particular it must not be confused with the ordinary deformation obstruction Ext²(E,E), which vanishes on the supplied stable plane fibers.

There is a precise conditional gerbe interpretation. Suppose the algebra thickening is fixed, local projective module lifts exist, and the failure of their transition maps to satisfy the cocycle condition is the usual additive square-zero class

    o(E)∈H²(End(E)⊗ω_S).

Central units 1+ω_S form the additive sheaf ω_S. A scalar square-zero gerbe class γ∈H²(ω_S) changes the obstruction by the scalar inclusion γ·id_E, up to the chosen cocycle sign convention. Since scalar inclusion is an isomorphism on H², there is a unique compensating cohomology class: choose γ so that γ·id_E=−o(E). If t=tr(o(E)), then γ=−t/rank(E) in trace coordinates. This can remove the cohomological obstruction to a gerbe-twisted lift in this specified framework.

That conclusion is conditional on allowing the gerbe modification and on the asserted lifting framework. It does not produce an untwisted module over the original algebra, identify a physical gerbe, construct compatible compensation over all planes, or establish a global module on X. The absence of a tracefree obstruction on each good plane does not kill the rank-12 cotangent-family gluing contribution H¹(U,V⊗ω_h), the exceptional-parameter terms, or the global 30-dimensional residual sector discussed in the supplied reports.

## 6. Exact relevance to Mukai/Bottacin constructions

The safe bridge is duality and coefficients. On a stable surface bundle, Ext¹(E,E⊗ω_S) is the Serre-dual cotangent deformation space to Ext¹(E,E). This is the rank-12 bundle V in COTANGENT_TARGET.md. The present calculation explains why the elliptic pair character selects that canonical twist and, for the second pair, the additional ω_h coefficient.

An ordinary Bottacin construction starts with an O-valued Poisson bivector, a section of ω_S^−1, and its induced map from canonical-twisted Ext¹ to untwisted Ext¹. Our line-valued wedge map does not specify such a section. Likewise a Mukai symplectic form requires the relevant global two-form/trivialization and appropriate moduli hypotheses; those are not furnished by renaming L as ω_S. No unverified identification with a Bottacin Poisson structure, Mukai symplectic form, or global quantized module is made here.

The genuinely intrinsic reformulation is: the pair-cover bracket is a nonzero, and after dual-volume normalization identity, morphism ω_S→ω_S; its first-order Hochschild class has canonical-line coefficients; two pairs have mixed coefficient ω_X; and the stable-plane obstruction recipient for a correctly specified canonical-twisted lifting problem is one-dimensional and scalar. All actual obstruction values and all global module claims remain open.

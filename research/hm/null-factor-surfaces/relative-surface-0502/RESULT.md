# Factor-surface route: a genuine generic vanishing result, not a global module quantization

## Findings

1. Fixing two elliptic factors makes the map to P4 factor through a *linear plane* P², including when the two fixed P¹ points coincide.
2. For the degree-eight map p:C²→Sym²P¹=P², an explicit pushforward calculation proves that a stable plane bundle has simple pullback. No assertion that finite pullback preserves stability is used.
3. The particular two-dimensional family of planes is generically stable for normalized HM: its Plücker degree is 9, whereas the entire HM jumping-plane locus is the irreducible surface of degree 25. Consequently the pulled-back surface bundles are simple on a nonempty dense open of the parameter surface.
4. Relative tracefree Ext² vanishes on that open. This supplies local-in-the-base tracefree lifting unobstructedness for a genuinely vertical, already existing ambient deformation. It does not prove global pure-direction module existence, scalar compensation at every order, compatibility of two independently constructed directions, or vanishing of any of the thirty retained obstruction values.

## 1. Linear plane identification, including repeated fixed points

Work over C. Let V be the two-dimensional binary-form space and identify Sym^d(P¹) with P(Sym^d V) by effective divisors/binary forms, with a consistent dual convention. Let u,v be the images in P¹ of the two fixed elliptic coordinates, and let h be the nonzero binary quadratic with divisor u+v.

Multiplication by h is an injective linear map

    Sym² V → Sym⁴ V,    g ↦ hg.

Its projectivized image Λ_h=P(h Sym² V) is a linear P² in P⁴. It is exactly the locus of degree-four divisors containing the fixed degree-two divisor u+v. If u=v, containment means multiplicity at least two; it is still a linear plane, not merely the hyperplane of divisors containing u once.

The restricted map is

    C² --q--> P¹×P¹ --σ--> Sym²P¹=P² --i_h--> P⁴,

where q has degree 4, σ degree 2, and p=σq has degree 8. The restriction F_b of F=N⊗f*HM is N_b⊗p*E_h, with E_h=i_h*HM. Thus End(F_b)=p*End(E_h) canonically. The line twist N_b is irrelevant to simplicity and tracefree Ext.

This proof uses only divisor addition and multiplication of binary forms, not a source/model/jet evaluation.

## 2. The degree-eight cover actually preserves simplicity of stable plane bundles

For an elliptic double cover C→P¹,

    q_*O_(C²)=O ⊕ O(-2,0) ⊕ O(0,-2) ⊕ O(-2,-2).

For σ:P¹×P¹→P², the double-cover algebra is

    σ_*O = O ⊕ O(-1),

because the branch divisor is the discriminant conic. The projection formula gives

    σ_*O(-2,-2)=O(-2)⊕O(-3).

Here is a direct proof of the remaining summands. The universal degree-two divisor D in P¹×P² is of bidegree (2,1), and D≅P¹×P¹ by remembering a chosen root and its residual root. The projection D→P² is σ, and the first P¹ coordinate is the chosen root. Twist its divisor exact sequence by O(-2,0):

    0→O(-4,-1)→O(-2,0)→O_D(-2,0)→0.

Push to P². Since H⁰(P¹,O(-4))=H⁰(P¹,O(-2))=0, the resulting sequence is

    0→σ_*O(-2,0)→O(-1)^3→O→0.

By duality on P¹, the last arrow is given by the three coefficients of the universal binary quadratic, hence is the Euler-sequence map. Therefore σ_*O(-2,0)=Ω¹_P². Symmetry gives the same answer for O(0,-2). Altogether

    p_*O_(C²)=O ⊕ O(-1) ⊕ (Ω¹_P²)^⊕2 ⊕ O(-2) ⊕ O(-3).      (★)

If E is slope-stable on P², then Hom(E,E)=C and Hom(E,E(-j))=0 for j>0 by stability and slope comparison. The injection Ω¹→O(-1)^3 implies Hom(E,E⊗Ω¹)=0. Applying projection formula to (★) proves

    H⁰(C²,End(p*E))=C.

This is a proof of simplicity for this exact cover, not an application of a general stability-preservation claim.

For normalized HM plane restrictions, the converse also holds. A nonstable plane restriction has a section and no section after twisting by -1, as follows from the two unstable resolutions in Boralevi Corollary 2.2. Its section therefore has no divisorial zero and gives

    0→O→E→I_Z(-1)→0.

Any nonzero linear form induces I_Z(-1)→O. Composing quotient, this map, and inclusion produces a nonzero nilpotent tracefree endomorphism of E. Its pullback remains nonzero because p is faithfully flat (finite map of smooth equidimensional surfaces, or the explicit locally free pushforward above). Hence

    F_b simple  ⇔  E_h stable.                                      (†)

Only the forward construction is needed for the generic vanishing conclusion.

## 3. What the primary HM restriction theorem does and does not establish

Primary source: Ada Boralevi, “The Horrocks–Mumford bundle restricted to planes,” arXiv:math/0602002v2, subsequently Collectanea Mathematica 58 (2007), 101–117.
https://arxiv.org/pdf/math/0602002
https://iris.polito.it/handle/11583/2674263

Source facts used (Corollary 2.2 and Theorem 3.1, PDF pp. 5–7): the normalized bundle has c1=-1,c2=4; four of the six plane-restriction resolutions are stable and two unstable. The unstable planes form the smooth degree-25 surface S25 in the Plücker Grassmannian, birational to Shioda's modular surface. Theorem 3.1 supplies a rank criterion in specified Plücker coordinates. These are facts about plane restrictions, not the elliptic-cover pullbacks. The paper does not assert avoidance of S25 by our particular family.

Nevertheless its global description, combined with the following independent geometric argument, proves generic stability for our family. Define

    φ:P(Sym²V)=P² → Gr(3,Sym⁴V),   [h]↦h Sym²V.

This is injective on points: the greatest common divisor of all quartics in the subspace h Sym²V is h up to scalar. The pulled-back tautological rank-three bundle is O(-1)⊗Sym²V. Consequently φ*O_Gr(1)=O_P²(3). The map is proper and quasi-finite, and in characteristic zero its generic degree is one. Its image T is an irreducible surface of Plücker degree

    deg(T)=∫_(P²)c1(O(3))²=9.

T cannot be contained in the irreducible surface S25: containment of irreducible surfaces of the same dimension would force equality, contradicting degrees 9 and 25. Hence U=P²\φ^(-1)(S25) is nonempty dense. The unordered fixed-factor map C²→P² is surjective, so its inverse image B° is nonempty dense as well. By (★), every surface fiber over B° is simple.

This argument works under any fixed projective-coordinate identification of the binary-quartic P⁴ with the HM ambient P⁴: degree is unaffected. It does not use or evaluate Boralevi's rank matrix. We have not determined whether T∩S25 is empty, finite, or has curves, nor located any exceptional parameter. Thus we have proved *generic* simplicity for this particular family, not simplicity of every fiber and not membership in the most generic resolution stratum.

## 4. Exact relative Ext² vanishing hypothesis

Let r:C²×B→B be either factor projection, with B the other C², and let G=End_0(F). The bundle F is locally free of rank 2, and trace splits End(F)=O⊕G over C. The morphism r is smooth proper of relative dimension 2 with connected abelian-surface fibers; ω_r≅O after choosing a nonzero product elliptic differential. The trace pairing identifies G*≅G.

For every geometric fiber A_b=C², Serre duality gives

    Ext²(F_b,F_b)_0 = H²(A_b,G_b)
                       ≅ H⁰(A_b,G_b⊗ω_A_b)*
                       ≅ H⁰(A_b,G_b)*.

Thus fiberwise tracefree Ext² vanishing is *equivalent* to simplicity here. On a general surface, simplicity alone would not suffice: the exact necessary condition is H⁰(End_0(F_b)⊗ω_A_b)=0.

Define the relative obstruction sheaf as

    Ext²_r(F,F)_0 := R²r_*G.

For this smooth proper surface family, G is B-flat and perfect; top-degree cohomology and base change apply. Therefore R²r_*G=0 on an open base W exactly when every geometric fiber over W has H²(G_b)=0. In particular it vanishes on B°. If a jumping parameter occurs, (†) gives a nonzero fiber H² and hence precludes vanishing near that point. On a constant-dimension simple locus relative duality identifies R²r_*G with the dual of r_*(G⊗ω_r), both zero. Outside it, one must not replace derived relative duality by a naive dual of r_*G: r_*G can vanish while torsion higher direct images persist.

The requisite hypotheses are therefore: (a) genuine locally free F and trace splitting; (b) smooth proper relative surfaces and valid base change; (c) trivial relative canonical, or the more general twisted-Hom vanishing just stated; (d) simplicity on *each* fiber in the base region under discussion. Plane stability plus (★) verifies (d) on B°, not on the entire B.

## 5. Consequences and boundaries for pure-direction quantization

For a deformation genuinely vertical along factors 1,2 (respectively 3,4), its coefficients and descent must define an O_B-linear relative algebroid, and the lower-order module must already exist. The small-extension lemma in the supplied module-lifting report then places the actual obstruction in End(F), not merely the ambient Hochschild obstruction group. On an affine open W⊂B° the Leray spectral sequence and R²r_*G=0 give

    H²(r^(-1)W,G)=0.

Thus the tracefree part of any such small-extension module obstruction vanishes there. This can be iterated if a genuine ambient extension is provided at each stage and the scalar obstruction is separately killed by permitted corrections, while preserving the specified lower-order module and ambient jets. The conclusion is a local-in-the-base conditional formal existence statement, not a construction or an all-orders scalar-cancellation theorem.

Even if all fibers were simple globally, Leray leaves

    H¹(B,R¹r_*G)

as a possible contribution to H²(X,G) (with r_*G=R²r_*G=0 it is precisely the only total-degree-two term). Relative Ext² vanishing therefore does not by itself imply global module unobstructedness. Choices of local lifts must glue over B; that gluing can carry these base-direction obstructions.

The trace part has H²(O_A)=C on every abelian surface. A compensated first-order gerbe pair b does not automatically kill every higher scalar module obstruction. One needs either an all-order determinant/scalar argument for the specified ambient deformation or allowed central corrections whose characteristic map actually cancels those scalar classes. If a two-jet is frozen, no higher correction can repair a failed order-two module test.

Finally, two pure-direction lifts must have compatible shared transition data and ambient descent to combine. Their individual local existence does not supply the mixed compatibility. Nothing proved here identifies the remaining global/relative obstruction pieces with exactly the thirty retained coordinates, or proves those values zero. All thirty remain unknown, and no numerical reduction of their necessary checks is claimed.

## Scope and inputs

Read the supplied module-lifting and deck-character index reports. Performed static divisor, finite-pushforward, degree, and Serre-duality arguments plus primary literature lookup. No physical source or jet values are evaluated in this argument.

## 6. Stronger localization: every tracefree degree-two class vanishes over an affine good base

This statement is about ordinary coherent cohomology and does **not** require that a given obstruction arose from a vertical quantization. Retain the geometric premise that the actual physical object is the locally free rank-two bundle F=N⊗f*HM with the indicated root line N. Without that premise, the assertions for the physical object do not follow merely from a numerical complex/index identification.

On B°, every fiber is simple. Hence cohomology and base change give

    r_*G=0,     R²r_*G=0,

and R¹r_*G is locally free, compatible with base change. Its rank is 120. One can compute this directly from the same geometry: on a surface fiber A=C² write θ for the sum of the degree-one elliptic factor classes, so ∫_A θ²=2. The root line has c1(N|A)=θ and p*H=2θ. Since normalized HM has c1=-H and c2=4H², the rank-two tensor formula gives

    c1(F|A)=0,
    c2(F|A)=4(2θ)² + θ(-2θ) + θ² =15θ²,
    ∫_A c2(F|A)=30.

For a rank-two bundle, ch₂(End₀F)=c1(F)²−4c2(F). The Todd class of an abelian surface is 1. Therefore χ(A,G|A)=-120. Simplicity and Serre duality give h⁰=h²=0, so h¹=120 on every good fiber, proving the asserted rank and base-change property. (The vanishing statement itself does not require this numerical rank.)

For **any** open U⊂B°, restriction of the Leray spectral sequence has only its q=1 row nonzero. Thus there is a canonical edge identification

    H²(r^(-1)U,G) ≅ H¹(U,(R¹r_*G)|U).

If U is affine, the right-hand side vanishes because R¹r_*G is quasi-coherent. Consequently every global class ξ∈H²(X,G) satisfies

    ξ|_(r^(-1)U)=0        for every affine open U⊂B°.

This localizes the possible global nonzero tracefree classes to gluing across good-base opens and/or the complement of the good base; it does not assert that they are represented by a unique sheaf-supported class on the bad locus.

In the deck-equivariant setting of the supplied index report, the full-sign part of H²(X,O_X) is zero. Indeed Künneth expresses H²(O_(C⁴)) as the sum of tensor factors with H¹(O_C) in exactly two positions; each such character is odd at precisely those two deck involutions, not all four. Trace is equivariant, so the full-sign Ext² sector lies in H²(X,End₀F). Accordingly every retained class/direction in the stipulated thirty-dimensional full-sign sector restricts to zero on r^(-1)U for affine good U. This statement requires no invariant action on U itself: it is the ordinary restriction of an already tracefree global class.

This is an actual localization theorem for those classes. It neither determines their thirty global values nor kills their global gluing contributions. It also does not cancel scalar module obstructions, establish a compatible all-order module, or bypass the frozen-two-jet test. The argument applies to either factor projection by symmetry.

A further harmless observation is that r_*G=0 on the entire original integral base B: it is torsion-free there (multiplication by any nonzero base function is injective on the locally free G upstairs), and its generic fiber vanishes. This does not force R²r_*G to vanish globally; that higher direct image may be torsion along exceptional parameters.

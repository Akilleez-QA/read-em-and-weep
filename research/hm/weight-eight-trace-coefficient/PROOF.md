# The weight-eight trace anomaly and parameterized affine ambiguity

## Result and novelty

Work over C with the actual marked cubic/quintic regular family on the negative projection line L=P(W), at commit ec48bfc075f6cfcb001fd7c7c8b50fc6513e0839. All bundles below are associated-graded coefficient bundles, not homogeneous replacements for the actual bundle. Write A=Sym²W, V=Sym²W′, P=P4 and D=D5.

The weight-eight tangent quotient of M(2) and its polynomial connecting map are ALREADY known. We use them rather than claim their twist as a new theorem. The new conclusion is the complete trace-bearing, gauge-quotiented coefficient calculation:

    0 → M₈ → C₈ → Sym¹⁶(W′) O_L(-2) → 0,
    M₈=A O_L(4) ⊕ V O_L(2),
    H⁰(C₈)=H⁰(M₈)=A+V+2P+2D,
    H¹(C₈)=Sym¹⁶(W′)=A+P+2D.                 (1)

Both cohomological identifications are canonical. In particular H⁰(C₈)^G=H¹(C₈)^G=0. But for a family quadratic in a∈A and linear in h∈D, the corresponding equivariant affine ambiguity and obstruction spaces have dimensions TWELVE and NINE respectively, not zero. The latter obstruction is canonically the scalar trace anomaly. This distinguishes scalar invariant acyclicity from the actual task of gluing an equivariant family.

No actual affine R2 cocycle or value is computed. Application to that R2 requires its full affine transport, its parameter degree, and its compatibility with the coefficient filtration to be established separately.

## 1. The coefficient complex and its lines

Write σ=(f,g), deg(f)=3, deg(g)=5 and n=[[fg,-f²],[g²,-fg]]. At weight eight a trace-free matrix R=[[a,b],[c,-a]] has entry degrees (8,6;10,8). Its physical twist is four. Denote its actual coefficient bundle by F₈; its associated triangular presentation has diagonal, upper and lower coefficient lines O(0), O(8), O(-8), respectively. These lines use the actual G frame lines O(9/2),O(-5/2), and the rule that a cover degree d subtracts d/2 from the physical base twist.

The tangent preimage lies in G(2), because τ(v)=σvᵀJ+vσᵀJ has twist two. Its component degrees are three and five. The tangent bundle T₈ therefore has the already established exact presentation

    0 → Sym⁵(W′) O(-3) → T₈ → Sym³(W′) O(5) → 0.     (2)

The actual triangular transition is retained in (2). It is not discarded by treating the displayed terms as a split bundle. The regular conjugator has weight zero and physical twist two: K=[[k,0],[r,-k]], with k of degree zero and r of degree two. Its bundle is

    0 → V O(-6) → J₈ → O(2) → 0,
    J₈=P O(-4).                                             (3)

Under τ the commutator is evaluation Kσ, up to the same fixed nonzero normalization used in the existing tangent convention. Evaluation is injective in this degree: kf=0 forces k=0, then rf=0 forces r=0. Thus J₈ embeds in T₈ and F₈. Define C₈=F₈/J₈; the tangent quotient T₈/J₈ is M₈.

The determinant and normal-line factors are essential: R has physical twist four, n twist two, and tr(nR) twist six. Its cover degree is sixteen, hence its coefficient line is O(6-16/2)=O(-2). Therefore the trace map is

    t:F₈ → Sym¹⁶(W′) O(-2),
    t(R)=2fg a+g²b-f²c.                                    (4)

The square-ideal resolution of the fiberwise regular (3,5) pair has Hilbert numerator 1-t⁶-t⁸-t¹⁰+t¹¹+t¹³. Its quotient vanishes in every degree at least twelve. Thus (4) is surjective in degree sixteen in every fiber, and hence as a bundle map. Its kernel is τ(T₈), by the regular-pair tangent identity. Trace annihilates [K,n] identically. Quotienting the exact trace sequence by J₈ proves (1)'s bundle sequence. This also proves C₈ is locally free.

The construction is intrinsic under the actual marked frame, triangular generator, and determinant transitions: trace, evaluation and commutator are natural maps. Nothing identifies an actual unfiltered R2 with a section of F₈ or C₈ before its lower affine terms have been accounted for.

## 2. Canonical cohomology and polynomial connecting map

The existing actual double-cubic theorem and its twist give

    M₈=A O(4) ⊕ V O(2).

Thus H¹(M₈)=0 and H⁰(M₈)=A⊗D + V⊗A=A+V+2P+2D. Since H⁰(O(-2))=0 and H¹(O(-2))=C, the long exact trace sequence gives precisely the two canonical identifications in (1). The second uses the canonical Serre trace H¹(ω_L)→C, with the given determinant-one linearization O(-2)=ω_L. No arbitrary splitting of the sequence in (1) is used.

For clarity, the different, already known polynomial boundary remains

    0 → H⁰(T₈) → H⁰(M₈) → H¹(J₈) → 0,
    H⁰(T₈)=A+P+D,
    H¹(J₈)=P⊗A=V+P+D.                                  (5)

Equation (5) is NOT the new trace map H¹(C₈)→Sym¹⁶(W′), and neither map is identified here with the actual global operator boundary. In particular, the polynomial nine-space in H⁰(T₈)/A remains subject to the known conic-extension obstruction. It cannot be subtracted as a global actual G(2) section merely because it is a coefficient section.

## 3. Character check, with W and W′ distinguished

For the A5 quotient use class order 1,2,3,5a,5b and class sizes 1,15,20,12,12. Put φ=(1+√5)/2 and ψ=(1-√5)/2. Choose A=(3,-1,0,φ,ψ) and V=(3,-1,0,ψ,φ). Then

    P=(4,0,1,-1,-1), D=(5,1,-1,0,0).

These give A⊗D=A+V+P+D and A⊗V=P+D. For W with Sym²W=A, the SU2 symmetric-power recurrence gives Sym¹⁶W=V+P+2D. Swapping the two binary representations therefore gives Sym¹⁶W′=A+P+2D, as asserted in (1). This check matters: interchanging A and V changes the parameter-channel identification, even when dimensions happen to agree.

The coefficient dimensions are consequently h⁰(C₈)=24 and h¹(C₈)=17, while their invariant parts vanish.

## 4. Exact affine consequences, conditional only on the transport interface

Suppose that, after fixing all lower coefficients, a candidate weight-eight transport is an actual affine cocycle with linear part C₈. Its obstruction to a global gauge-class section is its Čech class in H¹(C₈). By (1), it vanishes if and only if its scalar trace class in H¹(Sym¹⁶W′ O(-2)) vanishes. If it vanishes, its solutions form a torsor under the 24-dimensional H⁰(M₈).

Equivalently, a prescribed compatible AFFINE scalar trace datum introduces no further tangent obstruction: H¹(M₈)=0. The trace datum is allowed to be affine, not a global ordinary section of O(-2); the fact H⁰(O(-2))=0 does not authorize declaring the actual local trace polynomial zero.

For a genuinely G-equivariant affine cocycle with no nontrivial external parameter module, finite-group averaging gives an invariant solution once the invariant obstruction vanishes. Here it vanishes because H¹(C₈)^G=0, and the invariant solution is unique because H⁰(C₈)^G=0. This is uniqueness of the associated-graded gauge CLASS, not of a global matrix representative or of the full R2.

More generally, let U be a fixed finite-dimensional parameter representation and require linearity in U. Tensoring by U* is exact and G-invariants are exact in characteristic zero. Therefore the precise spaces are

    ambiguity = Hom_G(U,A+V+2P+2D),
    obstruction = Hom_G(U,A+P+2D).                       (6)

The obstruction is still the scalar trace class under (1), now coefficientwise in U. If that class vanishes the solutions form a torsor under the first space. No choice of a parameter evaluation, source instance, or selected coefficient has occurred.

## 5. Quadratic-in-a, linear-in-h source interface

The actual corrected source x(a,h)=[v_h(a)-b(a,h)ζ_a] in ACTUAL-FOURTH-CORRECTED-SOURCE-HAS-A-NONZERO-PARAMETER-TRACE.md is quadratic in a∈A and linear in h∈D. Its polarization module is therefore U₂=Sym²A⊗D. This observation applies to that source; it does NOT by itself assert that every subsequent normal error has the same parameter degree. Multiplication by a raises the degree and changes the module.

The matrix trace t(R)=tr(nR) in (4) is distinct from the parameter contraction Tr_A x in that source theorem. Nonvanishing of the latter does not identify or prove nonvanishing of the scalar obstruction in (6).

Since Sym²A=1+D and D⊗D=1+A+V+2P+2D,

    U₂=1+A+V+2P+3D.

Consequently, whenever the weight-eight affine interface under consideration is linear in this U₂,

    dim ambiguity = 1+1+2·2+3·2 = 12,
    dim obstruction = 1+2·1+3·2 = 9.                  (7)

These are exact dimensions of the available cohomological spaces, NOT ranks of the actual error map and NOT assertions that any channel has a nonzero actual value. They show why invariant acyclicity of the unparameterized coefficient cannot establish uniqueness or solvability for this corrected-source family. The full scalar compatibility computation must decide the nine possible obstruction coefficients; if they vanish, extra normalization or further geometric data must fix the twelve possible gauge-class choices. The full actual transport can impose additional conditions or have a different parameter module, which must be checked before applying (7).

For comparison, the multiplied source a x(a,h) is cubic in a. Its polarization module is U₃=Sym³A⊗D. Since Sym³A=A+V+P and P⊗D=A+V+P+2D,

    U₃=3A+3V+3P+4D,
    dim Hom_G(U₃,H⁰(C₈))=20,
    dim Hom_G(U₃,H¹(C₈))=14.

Thus an interface linear in the multiplied-source parameter module would have 20/14 rather than 12/9 available spaces. Again, this is conditional on that interface having the stated parameter degree, and does not decide whether R2 uses either module. Known lower-source identities can restrict the realized subspace further.

## Sources and boundary

All following paths are in research/hm/order-four-quadratic-load/ at the pinned commit:

- ACTUAL-LOWEST-NEXT-ERROR-TANGENT-COEFFICIENT-IS-ACYCLIC.md: actual twists, degrees and regular trace calculation.
- ACTUAL-DEGREE-EIGHT-NORMAL-OPERATOR-QUOTIENT.md: actual tangent/gauge and wedge diagram.
- ACTUAL-DEGREE-EIGHT-DEFECT-AS-DOUBLE-CUBIC-PUSHFORWARD.md: actual M₈ splitting before twisting down.
- FULL-HOMOGENEOUS-NORMAL-MATRIX-STILL-LOSES-THE-POLYNOMIAL-NINE-SPACE.md: already known twisted sequence (5) and its global-extension limitation.
- ACTUAL-FOURTH-CORRECTED-SOURCE-HAS-A-NONZERO-PARAMETER-TRACE.md: corrected source degree and nonzero parameter trace.
- ACTUAL-LEADING-NEXT-ERROR-HAS-A-CANONICAL-AFFINE-TRANSPORT.md: weight-four actual affine law; explicitly not a weight-eight transport theorem.

This proof uses only universal regular-sequence exactness, the previously proved actual filtered coefficient identifications, P1 cohomology and finite-group representation algebra. It does not compute full actual R2, an actual HM coefficient, a selected source evaluation, a matrix rank, a parameter scan, or a Bockstein value.

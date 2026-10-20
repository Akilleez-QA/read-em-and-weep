# Preserved mathematical audit of the geometric core

The polar-application review is separated; publication edits are checked independently.

# Independent audit: the binary-quartic normalization and conductor

Work over C. Let D be the reduced degree-six discriminant hypersurface in P⁴, let T=P¹×P², and let ν:T→D send ([l],[q]) to [l²q]. Write R for the locus where l divides q and S for the locus where q has a double root. The notation q(l)=0 must mean evaluation at the zero of l, not substitution of the coefficients of l without the usual duality convention.

## Verdict

The proposed conductor proof is correct after the finite-duality and ideal-inclusion steps are made explicit. It proves the exact ideal

c O_T = O_T(−2R−S) ⊂ O_T,

including the quadruple-root curve. There is no additional codimension-two conductor correction. The proposed ACM/Fitting/Hilbert–Burch proof is also valid and additionally proves that the conductor downstairs is the ideal of the reduced singular locus. This ideal must not be confused with the Jacobian ideal defining the possibly nonreduced singular scheme.

## 1. Normalization and the two divisors

The morphism ν is proper. Its fiber over a nonzero quartic consists of its finitely many roots of multiplicity at least two, with q determined by l. Hence it is quasi-finite and therefore finite. A general discriminant quartic has exactly one double root, so ν is birational. Since T is smooth and integral, ν is the normalization of D.

The pullback ν*O_D(1) is O_T(2,1). The incidence equation l|q has bidegree (2,1), so R has class (2,1). The quadratic discriminant has degree two in q, so S has class (0,2). Both are smooth irreducible divisors, each isomorphic to P¹×P¹. Their images are the triple-root surface N and the two-double-root surface W respectively.

Away from R∪S, the root pattern is (2,1,1). Coprime local factorization separates a double-root quadratic from two simple linear factors. The quartic discriminant is a unit times the quadratic discriminant, which is a smooth local coordinate. Thus D is smooth there and ν is an isomorphism there. These facts identify all possible divisorial support of the conductor.

## 2. Why finite duality gives the actual conductor ideal

For any affine normalization A⊂B in the common function field K, evaluation at 1 identifies

Hom_A(B,A) = {x∈K : xB⊂A} = {x∈A : xB⊂A}.

Indeed, after tensoring an A-linear map B→A with K, it becomes multiplication by x=φ(1). The condition xB⊂A forces x∈A because 1∈B. Conversely every such x gives a homomorphism by multiplication. Under this identification, the natural B-module structure on Hom_A(B,A) is its usual ideal-module structure in B. Its image in A is Ann_A(B/A), the conductor, and it is simultaneously an ideal of B.

D is a hypersurface, hence Gorenstein, and adjunction gives ω_D=O_D(1). Finite duality for the finite, equal-dimensional morphism ν gives, as ν_*O_T-modules,

ν_*ω_T ≅ Hom_D(ν_*O_T,ω_D).

This is the finite canonical-module formula; it does not require ν to be flat. One way to justify it precisely is to use transitivity of dualizing complexes and the finite-map formula RHom_D(ν_*O_T,ω_D[3])≅ν_*ω_T[3]. Taking degree −3 gives the displayed Hom identification. Equivalently, use canonical modules for the finite Cohen–Macaulay algebra over the hypersurface. Since ω_D is invertible, the conductor as an O_T-module is

ω_T⊗ν*ω_D^(−1) = O_T(−2,−3)⊗O_T(−2,−1) = O_T(−4,−4).

Crucially, evaluation at 1 realizes this invertible module as the actual nonzero ideal inside O_T. Consequently it equals O_T(−E) for an effective Cartier divisor E. This is stronger than computing its line-bundle class or its reflexive hull. It eliminates the possibility of an additional ideal factor supported only in codimension two.

For background on the finite duality step, see the Stacks Project, [finite maps and dualizing complexes](https://stacks.math.columbia.edu/tag/0A7A), Lemma 47.15.8, and [relative dualizing modules](https://stacks.math.columbia.edu/tag/0BUK). The hypersurface/Gorenstein input is covered by [Gorenstein schemes](https://stacks.math.columbia.edu/tag/0AWV), Lemma 48.24.5.

## 3. The generic local models and their conductor orders

The factorization maps used below are étale wherever the factors are coprime: their differential is invertible because the corresponding resultant is nonzero. Completion or an étale faithfully flat extension is therefore legitimate. Formation of the conductor commutes with these flat base changes because it is Hom_A(B,A) for a finite presented module.

At a quartic of type (3,1), split off the simple linear factor. The quartic discriminant is a unit times the cubic discriminant. Translate the cubic variable to remove the quadratic term. Its discriminant is −4p³−27q². After rescaling, the completed local normalization is

C[[a,b,x,y]]/(y²−x³) ⊂ C[[a,b,t]],  x=t², y=t³.

Here a,b are smooth parameters along the triple-root surface. The conductor is (t²): every series with zero coefficients of t⁰ and t¹ lies in the cusp ring and stays there under multiplication by any normalized series; a nonzero t¹ coefficient prevents membership, while a nonzero constant coefficient fails after multiplying by t. The divisor R is t=0. Thus E has order 2 along R.

At a quartic of type (2,2), split into two coprime quadratic factors. The product discriminant formula makes the quartic discriminant a unit times x y, where x,y are the two independent quadratic discriminants. Thus the completed local model, after splitting the two branches if necessary, is

C[[a,b,x,y]]/(xy) ⊂ C[[a,b,x]] ⊕ C[[a,b,y]].

The image consists of pairs whose restrictions to x=y=0 agree. Its conductor is (x)⊕(y). Each normalized branch therefore has conductor order 1 along S.

There are no other divisorial components. Since E is an actual Cartier divisor, these orders prove E=2R+S globally. The class calculation (2R+S)=(4,4) agrees with duality, but the class calculation alone would not prove equality of ideals.

## 4. What happens at a quadruple root

A universal monic chart on T can be written

f(z)=(z−t)²[(z−t)²+w(z−t)+r].

This uses universal coordinates rather than evaluating any selected quartic. In these coordinates

R=(r),  S=(w²−4r),  c O_T=(r²(w²−4r)).

The reduced quadruple-root curve is (r,w). The two divisors are tangent there: their scheme-theoretic intersection has ideal (r,w²), not (r,w). Thus R∩S is a doubled diagonal scheme, although its set of points is precisely the quadruple-root curve. The formula for the conductor incorporates this tangency and all of its nonreduced structure.

## 5. The exact conductor-square descent criterion

Let I=c⊂A⊂B be the common conductor ideal. There is a canonical ring identity

A = B ×_(B/I) (A/I).

To check it, a pair (b, a mod I) belongs to the fiber product exactly when b−a∈I; since I⊂A, this forces b∈A. Hence there is an exact sequence

0→A→B⊕A/I→B/I→0,

with final map (b,c)↦b mod I−c. The map A/I→B/I is injective. This proof uses the full conductor ideal and holds at every point, including quadruples.

Write C=V_D(c), and let C̃=V_T(c O_T)=2R+S as a closed subscheme. Sheafifying gives

0→O_D→ν_*O_T⊕O_C→ν_*O_C̃→0.

For any locally free sheaf E on D, tensoring and the projection formula give

0→E→ν_*ν*E ⊕ E|_C→ν_*(ν*E|_C̃)→0.

Thus a regular normalized section descends if and only if its full restriction to C̃ is the pullback of a section on C. This is an exact condition on the nonreduced conductor subscheme, rather than a replacement by separate conditions on its reduced components.

At a generic cusp the criterion says that the coefficient of t modulo t² vanishes. At a generic node it says that the two branch values agree. These are the generic manifestations of the same exact square. At quadruples, one must use the full restriction modulo r²(w²−4r), or supply a separate extension argument that is genuinely equivalent. The conductor square already provides the complete criterion without such an auxiliary argument.

For cohomology, the square produces a long exact sequence. In particular, normalized cohomology is not automatically the same as cohomology on D: the H⁰ mismatch term can contribute to H¹ on D. Any claim that normalization removes a polar-part cohomology obstruction must account for this term and the rest of the sequence. Nothing here evaluates the retained source classes in the pole-exclusion theorem.

## 6. Audit of the ACM normalization resolution

Let i:D↪P⁴ and set M=(iν)_*O_T. Since ν*O_D(t)=O_T(2t,t), Künneth gives for every integer t

H¹(P⁴,M(t))=H²(P⁴,M(t))=0.

Indeed H¹(P¹,O(2t)) can coexist with H⁰(P²,O(t)) only if t≤−1 and t≥0, which is impossible. Likewise H⁰(P¹,O(2t)) can coexist with H²(P²,O(t)) only if t≥0 and t≤−3, which is impossible. Also H³(M(−2))=0 because H²(P²,O(−2))=0. Thus M is ACM of dimension three and 1-regular.

The graded section module has Hilbert series

Σ_(t≥0) (2t+1)(t+1)(t+2)/2 · z^t = (1+5z)/(1−z)^4 = (1+4z−5z²)/(1−z)^5.

It has one degree-zero generator, the unit, and four degree-one generators. There is no degree-one relation: a minimal relation of that degree could only annihilate the unit by a linear form, whereas the unit has annihilator (Δ), of degree six. ACM plus regularity therefore gives the minimal resolution

0→5O_P⁴(−2)→O_P⁴⊕4O_P⁴(−1)→M→0.

For Q=M/O_D, deleting the unit row yields the presentation

5O_P⁴(−2)→4O_P⁴(−1)→Q→0.

More precisely, the full resolution of Q is

0→O_P⁴(−6)→5O_P⁴(−2)→4O_P⁴(−1)→Q→0.

The first term comes from the degree-six annihilator of the unit. It should not be omitted if the presentation is described as a full resolution.

## 7. Audit of the reduced conductor downstairs

Let J=Fitt₀(Q), computed by the 4×4 minors of the resulting 4×5 matrix of linear forms. Its support is N∪W, of codimension two in P⁴, so J has height two. Hilbert–Burch supplies

0→4O_P⁴(−5)→5O_P⁴(−4)→J→0.

In homogeneous-module terms, the quotient by J is Cohen–Macaulay and hence has no embedded associated primes. The generic cusp and node models above both give Q equal to a rank-one residue-field module at the generic point of the relevant singular surface. Therefore its zeroth Fitting ideal is the reduced generic prime there. It follows that J is generically reduced at every minimal prime. Unmixedness together with generic reducedness makes J radical.

For every finite presented module, Fitt₀(Q)⊂Ann(Q), and these ideals have the same radical. Since J is already radical, these inclusions force J=Ann(Q). Restricted to D, this is exactly the conductor. Thus C is the reduced union N∪W, although its inverse image C̃=2R+S is nonreduced.

The degree check is consistent: the triple-root parameterization ([l],[m])↦[l³m] has pullback O(3,1), giving degree 6; the two-double-root locus is the image of P² by [q]↦[q²], giving degree 4. Hence deg C=10, also the degree obtained from Hilbert–Burch. These are structural intersection calculations, not selected-instance or rank evaluations.

## 8. Final check of the equivariant refinement

The equivariant subsection of PROOF.md also checks out. With V_n=Symⁿ(C²), the degree-one normalization sections are V₂⊗V₂=V₄⊕V₂⊕V₀, so the extra generators are V₂⊕V₀. In degree two the target is

V₄⊗Sym²(V₂)=V₈⊕V₆⊕2V₄⊕V₂⊕V₀,

whereas the free generators contribute

Sym²(V₄)⊕V₄⊗(V₂⊕V₀)=V₈⊕V₆⊕3V₄⊕V₂⊕V₀.

Their difference is one V₄, the five-dimensional relation space. The cofactor space is likewise V₄, since the relevant determinant characters of SL₂ are trivial. The conductor section Res(l,q)²disc(q) is SL₂-invariant. Dividing the five pulled-back degree-four generators by it gives an equivariant map V₄→H⁰(T,O(4,0))=V₄. This map is nonzero: a nonzero degree-four polynomial cannot vanish identically on the irreducible degree-six hypersurface D. Schur's lemma therefore makes it an isomorphism up to a common scalar and choices of compatible bases. The resulting degree-four monomials in l have no common zero, proving exact generation of the extended conductor everywhere.


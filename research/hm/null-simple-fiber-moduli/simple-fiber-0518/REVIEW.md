# Independent audit: simple-fiber joint formal lifting

## Verdict

The proposed fiberwise joint-existence mechanism is valid with the geometric and presentation hypotheses stated below. Use only the two fiber deck involutions. A claim that the supplied literal Alexander–Whitney two-jet is equivariant under the factor swap is not justified merely by its cohomology character; the short scalar representative need not be swap-odd. The swap is unnecessary.

This proves existence over one good surface fiber, allowing higher ambient product, overlap, and triple-unit coefficients to change. It does not produce a module for fixed all-order Moyal products, a global family over the parameter base, compatibility between two pure directions, or any global retained obstruction value.

## 1. Group and linearization

Let Y=C×C and H=(Z/2)^2 act by the two deck involutions; let χ be their product character. The deformation parameter h carries χ. Diagonal inversion d has χ(d)=+1.

The numerical statements c1(F)=0 and c2(F)=15θ² and simplicity do not alone supply an H-linearization. For the geometric F=N_Y⊗p*E_h they do not need to: p is deck invariant, hence p*E_h has its canonical pullback linearization. The specified root line N_Y is O_C(∞)⊠O_C(∞), up to a constant one-dimensional line contributed by the fixed factors. Its invariant divisors give a genuine coherent deck linearization. Their tensor product linearizes F. This uses the stated genuine-bundle/geometric identification, not a numerical index replacement for it.

Trace is then H-equivariant. Simplicity and Serre duality give Ext²(F,F)_0=0. Hence trace is an isomorphism Ext²(F,F)→H²(O_Y). Its inverse is a↦(a/2)Id; scalar inclusion itself has trace 2a. H²(O_Y) has character χ. No extra character from N survives in End(F).

## 2. First-order cancellation and normalization

For the source convention μ1=(1/2)π and row transitions g_jk g_ij=g_ik, the normalized first-order defect is

    C_ijk=g_ik^(-1) μ1(g_jk,g_ij)−b_ijk Id.

The trace of the first term represents (1/2)ιπ tr(At(F)^2)=ιπ ch2(F). This can be checked directly using the transition formula for the Atiyah cocycle and cyclicity of matrix trace; it has the same total Čech–forms sign as the source's explicit line-bundle calculation. This trace comparison, not a stronger unproved matrix-valued identity, is all that is required.

With c1=0, ch2=−c2=−15θ²; in the stipulated normalization ιπθ²=2Π. Thus tr ev(π)=−30Π. Because trace is an isomorphism, ev(π)=−15Π Id. The supplied b class is −15Π, so ev(π)−b Id=0. The distinction between trace and scalar coefficient is essential: no second factor of two should be inserted in the gerbe correction.

The first-order equation is linear. Its defect is χ-isotypic and it has a primitive; the χ projector selects a primitive in that same character. This gives an equivariant first-order module. No nonlinear module object is averaged.

## 3. Frozen order two

Assume the supplied pure ambient two-jet satisfies its actual descent equations and is literally H-equivariant with h assigned χ. Its order-two module obstruction lies in

    (Ext²(F,F)⊗h²)^H=(χ⊗1)^H=0.

It therefore admits a module order-two correction while leaving the given ambient two-jet unchanged. This is the extra input that the general ambient extension theorem alone cannot provide.

The relevant equivariance is literal deck equivariance of the chosen coefficients, not only equality of their classes. Each q_r and V_r is odd under its own deck involution; a_r is even. The pure b has χ, the pure bivector has χ, and T has trivial deck character. Thus h b, the first star coefficient, and h²T have the required weights. This check does not assert swap equivariance of an unantisymmetrized AW representative.

## 4. Higher ambient and module induction

At stage n≥3, the small kernel is I=C h^n and is annihilated by h. Every ambient obstruction belongs to (HH³(Y)⊗I)^H. On an abelian surface diagonal inversion acts as (−1)^(p+q)=−1 on each HKR summand H^q(Λ^p T) of total degree 3. It acts trivially on I. Consequently this invariant group is zero. A genuine equivariant ambient extension exists, without changing any earlier coefficient.

The resulting module obstruction lies in (Ext²(F,F)⊗I)^H. For even n this is zero. For odd n it is scalar and may be canceled by an H-equivariant arity-zero ambient correction represented by a Čech cocycle a∈H²(O_Y)⊗I. The ambient change η=(0,0,a) is closed: δa=0 and the classical Hochschild differential on arity zero vanishes because O_Y is commutative. The checked small-extension formula gives κ_F(η)=−a Id. Since scalar inclusion is an isomorphism here, this hits every module obstruction with its correct coefficient character. Choose a to cancel the scalar coefficient, then solve the remaining module coboundary equation.

There is no hidden inverse-coupling problem: at a small extension all terms involving the new a and an old positive-order coefficient vanish because hI=0. Thus changing the triple unit preserves the ambient equations at this order precisely when η is closed. The next order is handled anew, with unrestricted higher μ,F,A corrections. This is not an assertion that a higher gerbe change is central for the entire untruncated star product.

## 5. Covers, frames, and literal preservation

A coherent linearization does not make arbitrary local frames invariant. One rigorous implementation is to choose a finite affine trivializing refinement, take all its H-translates with freely H-labeled indices, retain duplicate opens, and transport frames using the linearization. Use the full Čech nerve so that the action on indices is strict. Separatedness makes finite affine intersections affine. The requisite End-cohomology and normalized differential Hochschild comparisons then apply on this cover. New coefficients lift coefficientwise, and their finite-group projections exist in characteristic zero.

Only linear new-coefficient primitives are averaged at each step. Keeping old coefficients fixed makes the induction compatible. The inverse limit gives a formal, h-adically locally free module with exactly the chosen lower truncations.

The original ambient two-jet remains literally its restriction on this refinement: no gauge-equivalent replacement or change of its coefficients is made. If a claim insists on a module expressed by free matrices on the unchanged original cover, that cover must separately be known to trivialize F. The abstract ambient algebroid and its specified two-jet can remain on their original cover while module descent uses a refinement; do not conflate this with alteration of the ambient two-jet.

## 6. Remaining explicit premises and boundaries

- The physical object is the genuine geometric bundle F, not merely a complex with matching numerical invariants.
- The selected fiber is simple, as supplied by the good-plane argument.
- The stated pure ambient two-jet identities and deck characters hold for the actual supplied formal presentation.
- The characteristic convention is the one calibrated by the source, with ιπθ²=2Π and b=−15Π.
- Normalized differential cochains include arity zero; higher gerbe coefficients are allowed to vary.
- The affine-cohomology/HKR comparison and coefficientwise lifting hypotheses of the checked ambient/module lemmas apply.

Under these premises I found no additional Atiyah-trace, inverse, coefficient-lifting, or weighted-character obstruction. The stronger swap-equivariant literal assertion should be removed unless proved for the chosen representative. No physical source or jet values are evaluated in this argument.

Inputs: supplied relative-surface RESULT, module-lifting RESULT, descent-lifting LEMMA; deck-character-index RESULT §2 for divisor-induced linearization; supplied source-second-order-algebroid §4 for row/HKR/gerbe conventions. The unnecessary swap premise is removed; the specified geometric root line is retained.

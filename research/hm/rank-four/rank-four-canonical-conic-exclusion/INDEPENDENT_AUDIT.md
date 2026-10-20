# Independent audit: canonical-conic exclusion

**Verdict: PASS, conditional on the explicitly imported rank, representation, repeated-input-injectivity, and equivariance hypotheses. No logical gap found.**

I independently reviewed this directory's `PROOF.md`, the conic-component classification and its `INDEPENDENT_AUDIT.md`, the canonical-line parity proof, the cubic-Massey module reduction, and the full-HM image-symmetry proof. This audit used static proof reading and abstract linear algebra and vector-bundle reasoning only. No actual source tensor, source coefficient, selected source input, operation matrix, or operation value was evaluated; 

## 1. A shorter sufficient image-bundle lemma

The asserted upper bound of six for the fixed odd coefficient span admits the following proof, independently of the stronger splitting classification in Section 1.

Let E=W⊗T be the irreducible six-dimensional G-module. Along the canonical conic C≅P¹, constant odd rank three makes its image I a rank-three subbundle of the trivial target, with a surjection O(-2)⊗E→I. Consequently I(2) and I* are globally generated. Birkhoff–Grothendieck gives

    I = ⊕_{i=1}³ O(-d_i),   0≤d_i≤2.

The induced equivariant map E→H⁰(I(2)) is nonzero: a nonzero bundle map from O(-2)⊗E is exactly a nonzero such map on sections after twisting. Irreducibility makes it injective. Hence

    6≤h⁰(I(2))=9-Σd_i,
    h⁰(I*)=3+Σd_i≤6.

If M is the span of all image fibers in J−, the map J−*→H⁰(I*) has kernel exactly M-perp, so dim M≤h⁰(I*)≤6. This argument needs neither an equivariant splitting nor a classification of binary-icosahedral linearizations. It proves precisely the bound used by the rest of the proof.

The longer Section 1 in the reviewed version is also valid. The degree filtration is equivariant, its splitting can be averaged in characteristic zero, and the central sign forces the O(-2) and O summand multiplicities to be even. The three listed cases exhaust rank three. The (2,1,0) case contradicts injectivity on sections; in the (0,1,2) case projection to its rank-one O(-1) summand vanishes by irreducibility, contradicting surjectivity onto I. Thus its stronger conclusion I≅O(-1)³ is justified, though unnecessary.

## 2. Odd coefficients: every placement is covered

For every conic representative u∈T and every w∈W,t∈T, the value f(w,u,t) belongs to M. Since the conic spans T and f is linear in its middle input, the same holds with arbitrary u∈T. Thus all values f(W,T,T) belong to M. Outer symmetry covers f(T,T,W), and cyclic zero gives

    f(t1,w,t2) = -f(w,t2,t1)-f(w,t1,t2).

It therefore covers f(T,W,T) as well. No symmetry between the two T inputs was assumed without proof.

The remaining odd coefficients are exactly W³. Outer symmetry and cyclic zero make their universal quotient S_(2,1)W, of dimension two. Thus dim J−≤6+2=8. Possible intersection between these two coefficient images can only improve the bound.

## 3. Even coefficients: every placement is covered

The imported conic restriction puts the entire pure-T coefficient image in one particular five-dimensional subrepresentation H. It also puts f(W,T,W) in this same H, rather than merely in a possibly larger P5-isotypic space.

For h(w1,w2,t)=f(w1,w2,t), cyclic zero and outer symmetry yield

    h(w1,w2,t)+h(w2,w1,t) = -f(w1,t,w2).

Modulo H this is an alternating map in the W inputs, hence factors through Λ²W⊗T, of dimension three. Outer symmetry supplies the remaining placement f(T,W,W). These are all even coefficient types, so dim J+≤5+3=8. The alternating quotient argument does not require H to contain either summand h separately.

## 4. Imported pure-T and mixed restrictions

The classification's necessary restrictions were checked rather than treated as dimension-only guesses. If the pure-T T constituent survives, the universal fixed-u map has kernel Cu², including at isotropic u. Its conic image has resolution

    0→O(-6)→O(-2)⊗Sym²T→I_even→0.

With total even rank five, this is the entire even image. Twisting gives H⁰(I_even(2))≅1⊕P5⊕T. The mixed source is T'=Sym²W, inequivalent to T, so it cannot map into this section space. Vanishing along the spanning conic forces the mixed coefficient map to vanish globally, contrary to repeated-input injectivity. This removes the T constituent.

Afterward the pure-T image has rank four inside its fixed H. The projected mixed image in J_even/H has rank at most one along C. If nonzero, its saturated image line bundle is O(-d) with 0≤d≤2, hence its fiber span has dimension at most three. But this span is the full coefficient image of a nonzero quotient of T'⊗T=P4⊕P5 and must have dimension at least four. Thus the projection vanishes. Saturation correctly handles possible rank drops; the argument does not require constant projected rank.

## 5. The twenty-dimensional contradiction and scope

The cubic-Massey reduction identifies the actual cubic target J3 with the dual of the weight-two target. The full-HM symmetry proof makes that weight-two target irreducible of dimension twenty, so J3 is irreducible too. Equivariance then makes the cubic coefficient image either zero or twenty-dimensional. The separately imported repeated-input injectivity excludes zero. No nonzero source evaluation is required for this conditional implication.

Together the parity estimates bound the complete coefficient image by sixteen, contradicting twenty. In fact any stipulated image dimension greater than sixteen suffices. The initial phrase “image dimension twenty, as established” should be understood with the repeated-input-injectivity hypothesis retained: the two representation proofs alone establish the zero-or-twenty alternative, not nonvanishing. Section 4 of the reviewed proof correctly makes that dependence explicit, so this is a clarification of dependencies rather than a gap.

The classification then excludes every conic component via the canonical orbit, and the previously imported no-line theorem leaves all reduced curve components of degree at least three. The result does not exclude higher-degree components, determine isolated rank-four points, or show the rank-four locus is empty. These limits are correctly preserved.

## 6. Independent audit of POINTWISE_ADDENDUM.md

**Verdict: PASS under the stated actual-target and repeated-input hypotheses.**

The target-parity calculation is correct. The normalized reflection has positive and negative dimensions 3 and 2 on V, hence 4 and 6 on Λ²V. In Λ²V=A⊗W_h the historical two-dimensional factor has negative central sign, so A has positive and negative dimensions 3 and 2. Since Sym³W_h has dimension four and negative sign, J3=A*⊗Sym³W_h has negative dimension twelve and positive dimension eight. These are representation identities, not evaluations of the cubic operation. The stipulated equivariance and nonvanishing make the actual coefficient span all of J3.

The pointwise-to-constant-rank argument is sound. The effective A5 action on the canonical conic is faithful, every point stabilizer is cyclic, and its order is at most five. Thus every orbit has at least twelve distinct points. Odd rank three at one point implies vanishing of all four-minors throughout that orbit. Each such restricted minor is a section of O_P¹(8), so it vanishes identically. The imported odd lower bound three then makes the rank exactly three everywhere. The bundle and odd coefficient argument in the main proof uses no even-rank or even-coefficient assumption, so it applies unchanged and bounds the entire odd coefficient span by eight. This contradicts twelve.

Consequently the odd block has rank at least four everywhere on each canonical conic. The imported pointwise even bound is five, so rank b≥9 and, with the standing normalization rank Q=rank b-4, rank Q≥5. This excludes all conic points from Z4, not merely conic components. It still makes no assertion away from these conics and their translates.

## 7. Independent audit of LINE_ADDENDUM.md

**Verdict: PASS under the stated actual-target and earlier line-rank hypotheses.**

The positive target is indeed the eight-dimensional A5 representation A*−⊗Sym³W_h. For any two-dimensional G-representation with negative central sign, perfectness forces determinant one. An order-three element g cannot belong to its kernel: the kernel's image in A5 would be a nontrivial normal subgroup and hence all of A5, leaving a quotient of G of order at most two; perfectness would make that quotient trivial, contradicting the negative action of z. Since g has order three and the action is semisimple with determinant one, its eigenvalues are the two primitive cube roots and its trace is -1. The symmetric-cube trace identity then gives trace 1 for Sym³W_h and trace -1 for J3,+.

If J3,+ contained P4, semisimplicity would leave a four-dimensional complement. The A5 irreducible dimensions and characters leave exactly P4, 1⊕T, 1⊕T', or four trivial summands as that complement. Their order-three traces are 1, 1, 1, or 4. Adding the P4 trace gives 2 or 5, incompatible with -1. Thus the exclusion of P4 is exhaustive.

I also independently checked the imported even-rank-four rigidity rather than relying on its threshold-section heading. The constant-rank pencil has image O(-1)^a⊕O^b with a+b=4. Its rank-two kernel in O(-1)⊗(W⊗T) has no sections after twisting, by irreducibility and nonzero image. Thus its degree is at most -4, giving a≤2 and b≥2. The intrinsic constant image is a subrepresentation of the coefficient span, a quotient of T⊕P4⊕P5. Hence b=2 is impossible; b=3 gives T and b=4 gives P4. In the b=3 case the residual rank-one image bundle O(-1) has positive central action, whereas its canonical linearization has negative central action. Twisting would produce a one-dimensional G-representation with negative central action, impossible by perfectness. Therefore b=4 and the image is the fixed P4. This argument requires only even rank four, not any assumed total rank.

Since the actual positive target contains no P4, the even line block has rank at least five. The separately audited odd bound is at least five. Complementary parity images give rank b≥10 and rank Q≥6 at every point of every canonical negative reflection line. No statement about other points follows from this argument, and no operation evaluation was used.

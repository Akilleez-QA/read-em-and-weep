# Publication scope

This is a preserved theorem manuscript, with the exact hypotheses and held identifications listed in unit 06 INPUTS.md. Abstract geometry and formal conditional implications are distinct from identification with the actual HM module or retained source. Historical words such as “new,” “remaining,” or “previously verified” describe the source manuscript, not a claim about the current research frontier.

# High-pole removal is a finite conductor section-lifting problem

## Result and conventions

Work over C on Y=P4. Let B=End_0(HM), D=V(Δ) be the reduced degree-six binary-quartic discriminant, ν:T=P1×P2→D its normalization, M=ν_*O_T as a sheaf on Y, and Q=M/O_D. The reduced conductor locus is Z=N∪W, of degree ten, with N the triple-root surface and W the two-double-root surface. Its full upstairs conductor is 2R+S, including the tangency at quadruple roots. All these facts and the following resolutions are established in ../discriminant-normalization-conductor/PROOF.md:

    0 → O(-2)^5 --C→ O⊕O(-1)^4 → M → 0,
    0 → O(-6) --j→ O(-2)^5 --A→ O(-1)^4 → Q → 0.

The degree-zero summand is the unit. The map A is obtained by deleting that row from C. Choose the generator j compatibly so Cj=(Δ,0). This fixes the signs in comparisons below. Choice of normalization generators does not change any image or quotient asserted below.

The established bound is that B is 11-regular. We first formulate the theorem for any independently proved regularity bound m, to make improvements usable without changing the argument. Set

    L_t=B(t)|D, G_t=ν*L_t, Q_t=B(t)⊗Q.

Constant coefficient lines W* and (W²)* can be tensored throughout; they are suppressed only in twist calculations.

The theorem gives:

1. H1(T,G_t)=0 for t≥m.
2. For t≥m+1, the image of H0(T,G_t) in H0(Q_t) is exactly the image of H0(B(t−1))^4 under the four degree-one normalization generators.
3. For t≥m+1 there are canonical compatible isomorphisms

       H0(Q_t)/im H0(B(t−1))^4 ≅ H1(D,L_t) ≅ H2(Y,B(t−6)).

These are actual maps, not a dimension count. Consequently the top pole layer is removable exactly when its conductor section is a global combination of those four generators with coefficients in H0(B(t−1)). The sheaf support is the degree-ten conductor locus, but the criterion is global and retains its scheme-theoretic gluing.

With m=11 alone, the first third-pole layer t=14 has obstruction H2(B(8)); the second t=15 has zero obstruction because H2(B(9))=0. However the additional monad argument in §5 below proves H2(B(t))=0 already for t≥4, using only previously admitted premises. Consequently BOTH third layers are always removable, and both coordinates have universal double-pole primitives. The normalization/conductor argument alone must not be credited with this extra vanishing.

## 1. Normalization kills all high-twist layer classes

Tensor the first resolution by B(t), which is locally free:

    0 → B(t−2)^5 → B(t)⊕B(t−1)^4 → ν_*G_t → 0.

Regularity gives H1(B(u))=0 for u≥m−1 and H2(B(u))=0 for u≥m−2. For t≥m, H1 of the middle term and H2 of the left term vanish. The long exact sequence therefore gives H1(Y,ν_*G_t)=0. The finite map has no higher direct images, proving claim 1.

For t≥m+1, H1(B(t−2))=0 also. Thus every global normalized section lifts to H0(B(t))⊕H0(B(t−1))^4. The unit summand maps to zero in Q_t, whereas the four other summands give precisely the four generators. This proves claim 2. In particular, solving a high-pole layer equation on the normalization is automatic and cannot by itself test descent or vanishing.

## 2. Canonical quotient and its sign

Tensor the conductor descent sequence and the hypersurface sequence:

    0 → L_t → ν_*G_t --dsc→ Q_t → 0,                 (1)
    0 → B(t−6) --Δ→ B(t) → L_t → 0.                 (2)

For t≥m, (1) yields an isomorphism

    coker[H0(T,G_t)→H0(Q_t)] --∂dsc→ H1(D,L_t).

For t≥m−1, both H1(B(t)) and H2(B(t)) vanish, so (2) gives an isomorphism

    H1(D,L_t) --∂D→ H2(Y,B(t−6)).

For t≥m+1 combine these with claim 2. The boundary convention is always ∂[a]=[δã], interpreting δã in the kernel through its stated injection. The resulting quotient is independent of all bases.

Given a closed layer one-cochain s, choose a normalized zero-cochain a with δa=ν*s, possible for t≥m. Then q=dsc(a) is a global section of Q_t, and ∂dsc(q)=[s]. Another choice changes q by the image of a global normalized section. For t≥m+1 the layer vanishes precisely when there exist four global coefficients b_i∈H0(B(t−1)) with

    q = Σ_i b_i q_i in H0(Q_t).

Subtracting the corresponding global normalized section from a makes a descend. Its descended zero-cochain is a primitive for s. Lifting it on the affine cover to B(t) and subtracting its Čech coboundary from the original meromorphic primitive removes this pole layer while preserving its differential. No change by a closed meromorphic one-cochain is needed at these twists, since H1(B(t))=0.

## 3. The correct finite-generator calculation and its hidden relations

Let K_t=im[B(t−2)^5→B(t−1)^4]. Split the Q resolution into

    0 → B(t−6) → B(t−2)^5 → K_t → 0,
    0 → K_t → B(t−1)^4 → Q_t → 0.

For t≥m+1 the first gives

    0 → H0(B(t−6)) → H0(B(t−2))^5 → H0(K_t)
      → H1(B(t−6)) → 0,
    H1(K_t) ≅ H2(B(t−6)),

and the second gives

    0 → H0(K_t) → H0(B(t−1))^4 → H0(Q_t)
      → H1(K_t) → 0.

Thus, putting V_t=coker[H0(B(t−2))^5 --A→ H0(B(t−1))^4], the exact finite sequence is

    0 → H1(B(t−6)) → V_t → H0(Q_t)
      → H2(B(t−6)) → 0.                             (3)

In particular, four sheaf generators do not imply that all global sections are generated by global coefficients. Even when they are, the five displayed relations need not generate all global relations. The missing sections are measured by H2(B(t−6)), and the extra relations by H1(B(t−6)). At t=15 under m=11, every section is generated, but extra relations H1(B(9)) must still be retained. This distinction prevents an incorrect 'cokernel of five relations equals H0(Q_t)' shortcut.

The final arrow of (3) is chosen to agree with ∂D∂dsc, with Cj=(Δ,0); this requires a minus sign relative to the naive two-step resolution boundary. To check it on an affine cover, lift q to local sections b of B(t−1)^4. Write δb=Ae; then δe=jf represents the two-step boundary in H2(B(t−6)). Lift b through C's target as (0,b). Its normalized image a has δa equal to the image of (−C_0e,0), where C_0 is the unit row. Hence s is represented on D by −C_0e, and δ(−C_0e)=−Δf. With the ordinary connecting conventions, this computation shows that the two-step boundary obtained using δb=Ae is the NEGATIVE of ∂D∂dsc. One must insert that minus sign when identifying (3)'s last arrow with the canonical composition. We define the final arrow of (3) to be −[f], so that it is exactly ∂D∂dsc. Exactness and the section-membership criterion are unaffected, but this explicit sign avoids conflating the two constructions.

## 4. Which conductor classes actually arise from bounded primitives

Let F=B(a), and let c be a regular F-valued two-cocycle. Suppose h is a k-pole primitive, δh=c, in C1(F(kD)). Let s be its top symbol in F(kD)|D. The hypersurface connecting map sends [s] to the image of [c] in H2(F((k−1)D)). This follows directly because h lifts s and δh=c is already a section of the kernel subsheaf F((k−1)D).

Writing all twists as B(a+6j), the inclusion F→F((k−1)D) is multiplication by Δ^(k−1). Therefore, at the high-twist range above,

    (∂D∂dsc)([q]) = Δ^(k−1)[c].                    (4)

For F1=W*⊗B(−4), k=3, this is Δ²[c1]∈W*⊗H2(B(8)). For F2=(W²)*⊗B(−3), k=3, it is Δ²[c2]∈(W²)*⊗H2(B(9))=0 under m=11. Thus every second-coordinate triple-pole primitive can be reduced to a double-pole primitive, regardless of its initial choice. The first can be so reduced exactly when Δ²[c1]=0; §5 proves that this condition also holds universally. This is stronger than an unspecified conductor reformulation: it identifies the source-to-conductor map and excludes any conductor class outside its image from occurring as a third-pole obstruction.

More precisely let A1=H2(F1), K2=ker[Δ²:A1→W*⊗H2(B(8))]. Then

    0 → K2 → A1 → im(Δ²) → 0

is the exact obstruction filtration by existence of a double-pole primitive. The top layer detects precisely A1/K2, not the whole original first obstruction and not necessarily the whole target H2(B(8)). Before the additional vanishing theorem this is an unevaluated formal filtration. Section 5 proves im(Δ²)=0 and K2=A1 by a uniform bundle argument, with no selected-rank evaluation. A class in K2 may still have an obstruction to removing its remaining two pole layers.

## 5. Stronger consequence from the admitted monad: H2(B(t))=0 for t≥4

This improvement needs no new source table or selected rank. Retain the already established normalized HM monad and bundle sequences

    A=5O(−1), M_HM=2Ω²(2), C_HM=5O,
    0→K→M_HM→C_HM→0,  0→A→K→F→0,
    F∨=F(1) is 5-regular.

The middle bundle M_HM is 1-regular because 2Ω²(3) is 0-regular, as proved by its linear Koszul resolution in the existing dependency. More generally suppose F∨ is r-regular. Then F∨⊗M_HM and F∨⊗A are (r+1)-regular, and F∨⊗C_HM is r-regular. For t≥r−1,

    H1(F∨⊗C_HM(t))=0,  H2(F∨⊗M_HM(t))=0.

Tensor the first sequence by F∨(t). These outer vanishings force H2(F∨⊗K(t))=0. Tensoring the second, the segment

    H2(F∨⊗K(t)) → H2(End(F)(t)) → H3(F∨⊗A(t))

has both outer groups zero: the right vanishes already for t≥r−2. Therefore

    H2(B(t))=0 for every t≥r−1.                     (5)

The trace splitting passes this from End(F) to B. The admitted r=5 proves the unconditional threshold t≥4. Hence H2(B(8)) and H2(B(9)) both vanish. Both coordinates admit double-pole primitives, and every chosen triple-pole primitive can have its third layer removed. This excludes every third-layer conductor obstruction, rather than merely relocating it. No assertion of first- or second-layer removal follows.

At m=11 and t=14,15, (3) now becomes

    0→H1(B(t−6))→V_t→H0(Q_t)→0.

Thus all global conductor sections are generated by the four generators, but the extra relation spaces H1(B(8)) and H1(B(9)) have not vanished by this argument alone.

If an independently proved improvement gives F∨ 4-regular, (5) improves to t≥3. Then H2(B(3))=0 supplies a universal SINGLE-pole primitive for the second coordinate F2=B(−3), since F2(D)=B(3). The first coordinate still has the established double-pole bound; (5) does not cover B(2), so it gives no universal single-pole assertion for that coordinate.

## 6. Uniform high-layer exclusion and scope of sharper bounds

For any proved m, H1(L_t)=0 when t≥m+4: indeed t−6≥m−2. Every such layer is removable. Using the separate H2 threshold (5) sharpens this to t≥max(m−1,r+5), since H1(B(t)) and H2(B(t−6)) then vanish. With the old m=11,r=5 the threshold is t≥10, already enough for both third layers. If an independently audited improvement gives m=9,r=4, it becomes t≥9, normalization vanishing begins at t≥9, and the four-generator criterion begins at t≥10. For t=14,15 that sharper bound also kills the extra relations H1(B(8)),H1(B(9)), so V_t genuinely equals H0(Q_t).

Normalization, the reduced conductor support, and the four generator sections do not remove the lower-pole obstructions. Regular Frobenius reconstruction preserves the pole filtration and the two independent coefficient coordinates. A vanishing third layer supplies no new vanishing of the thirty retained source conditions. Actual mixed sources, selected ranks, polynomial instances, source values and obstruction pairings have not been evaluated here.

## Dependencies

- ../discriminant-normalization-conductor/PROOF.md: exact normalization and conductor, including the resolutions and full quadruple-root scheme structure.
- ../discriminant-pole-exclusion/PROOF.md: compatible principal-parts complexes and exact pole removal criterion.
- ../effective-collision-bound/PROOF.md: independently established 11-regularity used unconditionally here.
- AUDIT.md: independent proof audit.


## 7. Exact lower-pole targets under the sharper F input

If the separately audited sharper input F 5-regular is available, then m=9 and r=4 above. Let P_i,k=F_i(kD)/F_i. Both common double-pole targets have no ambiguity:

    H1(P_1,2) ≅ H2(F1),
    H1(P_2,2) ≅ H2(F2),

because their middle sheaves are B(8) and B(9), whose H1 and H2 both vanish. The inherited ten- and twenty-dimensional retained spaces therefore remain exactly present in double-pole principal parts. For the second coordinate the smaller single-pole target satisfies only

    H1(P_2,1)/im H1(B(3)) ≅ H2(F2).

Here H2(B(3))=0 follows from the stronger monad lemma, whereas H1(B(3)) is not controlled by 9-regularity and must not be suppressed. The natural transition H1(P_2,1)→H1(P_2,2) is surjective with kernel exactly im H1(B(3)). Thus lowering the universal second pole bound to one does not remove or reduce its twenty retained conditions.

The general high-twist normalization theorem does not cover the next layers t=8 for the first coordinate at pole two, or t=3 for the second at pole one. Those lower layers remain the relevant regularity problem. In particular, the high-layer exclusion is a genuine simplification of pole order, not a proof of any source vanishing.

# Original elliptic pair-character gate

20 October 2026. Formal geometric derivation; existing cohomology ranks are imported, not recomputed.

## 1. Original coefficient and indexing

Let f:Y=(P1)^4→P4 be multiplication of four binary linear forms, so f*O(1)=O(1,1,1,1). Use the original pair-character coefficient L=O(-2,-2,0,0), not a normalized pair coefficient. Let F be the source-bound locally free complex

F^(-1)=5O(-1), F^0=15O, F^1=10O(1), F^2=2O(2).

Assume F has the asserted bundle cohomology in degree zero over the field in question. Write End(F)^q=O(q)^{n_q}. Direct term counts give n_0=354, n_(±1)=245, n_(±2)=80, n_(±3)=10. The hypercohomology spectral sequence has

E1^(q,p)=H^p(Y,f*End(F)^q⊗L), d_r:(q,p)→(q+r,p-r+1), total degree q+p.

Künneth and the elementary P1 line-bundle formulas give exactly:

- p=0: q=2 has 80·1·1·3·3=720; q=3 has 10·2·2·4·4=640.
- p=2: q=0 has 354·1·1·1·1=354.
- p=4: q=-3 has 10·4·4·2·2=640; q=-2 has 80·3·3·1·1=720.
- Every other entry vanishes. At q=1 or -1 at least one P1 factor is O(-1).

These are dimensions, not equivariant characters. All entries and arrows retain their actual induced linearizations. In particular, dimensions do not justify projecting away a coefficient-line sign or exchanging the original and normalized pair.

## 2. Exact vanishing gate

Set A=ker(E1^(-3,4)→E1^(-2,4)), B=coker of that map, C=E1^(0,2), D=ker(E1^(2,0)→E1^(3,0)), E=coker of that map.

All d2 vanish. The only possible d3 maps are

a:A→C and b:C→E, with b a=0.

All d4 vanish. On E5, the only possible d5 maps are

u:ker(a)→D, and v:B→coker(b).

There are no later possible arrows. The sole total-degree-one E-infinity term is ker(u), located at (-3,4). Consequently the exact original-pair gate is

H^1(Y,f*End(F)⊗L)=0 if and only if u:ker(a)→D is injective.

Here d5 is the actual spectral-sequence differential on the d3 survivors, not an arbitrary map between the original spaces. A first-stage row rank or a d3 rank alone does not establish injectivity. Nor do four P4 line-twist cohomology tables establish it without a comparison that controls this coefficient and these connecting maps.

The degree-two associated graded consists of ker(v), ker(b)/im(a), and coker(u). This statement does not assert a canonical direct-sum splitting.

## 3. Conditional interpretation of the reported old staircase ranks

The older source certificate reports ranks 450,100,90 and matrix shapes 720×640,354×190,720×90. These ranks and their field of validity are not independently verified here.

If the actual two d1 arrows each have rank 450, then dim A=dim E=190 and dim B=dim D=270. If the actual two d3 arrows each have rank 100, then dim ker(a)=dim coker(b)=90 and dim ker(b)/im(a)=154. If the actual two d5 arrows each have rank 90, then u is injective and v is surjective, so H^1=H^3=0 and

h^2=(270-90)+154+(270-90)=514.

One side of each rank pair may imply the other through actual Serre duality and the permutation exchanging the pair with its complementary pair, but that comparison must preserve the source and coefficient linearizations. It is not licensed solely by matching dimensions. The reported 720×90 staircase target can represent D inside the original 720-dimensional row; the genuine d5 target has dimension 270 under the first rank hypothesis. Its rank may be read as the spectral-sequence rank only if the source certificate supplies the survivor/quotient comparison.

## 4. A precise extra P2 coefficient: m_*O(-3,0)=Ω²(P4)

Let m:P2×P2→P4 multiply binary quadratics. There is an ordinary vector-bundle isomorphism

m_*O(-3,0) ≅ Ω²_P4.

Here is a formal proof independent of the HM maps. Put B=P(Sym² W), dim W=2. On B, multiplication gives an everywhere-injective bundle map Sym² W⊗O_B(-1)→Sym⁴ W⊗O_B, with rank-two quotient Q and det Q=O_B(3), up to constant determinant lines. The incidence X of pairs (g,f) with g dividing f is P2×P2 and is the regular zero locus of the induced section of Q⊠O_P4(1) on B×P4. Its Koszul resolution, twisted by O_B(-3), is

O_B(-6)⊠O(-2) → Q*⊗O_B(-3)⊠O(-1) → O_B(-3)⊠O.

The sequence 0→Q*(-3)→(Sym⁴ W)*⊗O_B(-3)→(Sym² W)*⊗O_B(-2)→0 and P2 line cohomology show that the three terms have only H² along B, of dimensions 10,5,1. The projection restricted to X is finite (each binary quartic has finitely many quadratic divisors), hence has no higher direct images. Pushing the Koszul resolution therefore gives an exact sequence

0→m_*O(-3,0)→10O(-2)→5O(-1)→O→0.

The last arrow is a surjection given by five linear forms, so they are a basis and its kernel is Ω¹. Also H⁰(m_*O(-3,0)(2))=H⁰(P2×P2,O(-1,2))=0. Thus the induced map k^10→H⁰(Ω¹(2)) is injective and hence an isomorphism. The middle arrow is the universal evaluation of Ω¹(2); its kernel is Ω² by the exterior Euler sequence. This proves the identity. With the natural SL2 linearizations all constant determinant lines are trivial, and the construction is equivariant. For a different group/lift those determinant lines should be retained explicitly.

For B=End(H), the Euler coresolution has terms 10B(-2), 5B(-1), B in degrees 0,1,2. If the existing P4 certificate gives H¹(B(-2))=0 and H⁰(B(-1))=0, there is no E1 term of total degree one at all, so H¹(B⊗Ω²)=0 without computing any connecting-map rank. This is the extra geometric comparison that makes the line-twist vanishings sufficient.

## 5. How this coefficient occurs in the ORIGINAL pair pushforward

Let j:P1×P1→P2 be the symmetric-square quotient. In characteristic not two, j_*O=O⊕O(-1), and the projection formula gives j_*O(-2,-2)=O(-2)⊕O(-3). Factoring f through j×j and then m yields

f_*L = m_*[O(-2,0) ⊕ O(-3,0) ⊕ O(-2,-1) ⊕ O(-3,-1)].

In particular Ω² occurs as the m_*O(-3,0) summand. This is an actual additional vector-bundle coefficient, not one of four line twists on P4. The direct-sum formula uses the characteristic-not-two splitting; its summands have their induced pair-transposition characters, which must not be discarded. An argument about invariant sectors must track those characters as well as the HM action.

## 6. The remaining summands split, closing the original-pair gate geometrically

The same incidence Koszul calculation identifies the other coefficients without HM differential computations.

For E₂=m_*O(-2,0), twist the base Koszul complex by O_B(-2). Its terms are O_B(-5)⊠O(-2), Q*(-2)⊠O(-1), O_B(-2)⊠O. Only the first has cohomology: H²(O_B(-5)) has dimension six. Indeed 0→Q*(-2)→5O_B(-2)→3O_B(-1)→0 makes the second term acyclic. Therefore E₂≅6O(-2).

For E₁=m_*O(-1,0), the terms are O_B(-4)⊠O(-2), Q*(-1)⊠O(-1), O_B(-1)⊠O. The nonzero base cohomology groups are H²(O_B(-4))=k³ and H¹(Q*(-1))=k³, the latter from 0→Q*(-1)→5O_B(-1)→3O_B→0. Both surviving terms have total degree zero. Thus E₁ has a filtration with graded pieces 3O(-2),3O(-1). Every possible such extension splits because H¹(P4,O(1))=H¹(P4,O(-1))=0. Hence E₁≅3O(-1)⊕3O(-2).

The projection formula then gives

m_*O(-2,-1)=E₁(-1)=3O(-2)⊕3O(-3),
m_*O(-3,-1)=E₂(-1)=6O(-3).

Combining these calculations, in characteristic not two,

f_*L ≅ Ω²_P4 ⊕ 9O_P4(-2) ⊕ 9O_P4(-3)

as ordinary vector bundles. Multiplicity representations and determinant-line factors are not being suppressed in an equivariant claim: this is enough for ordinary cohomology vanishing, and any invariant refinement requires their induced actions.

Consequently H¹(Y,f*B⊗L)=0 follows from exactly these existing P4 inputs:

H¹(P4,B(-2))=0, H¹(P4,B(-3))=0, H⁰(P4,B(-1))=0.

The Ω² summand uses the Euler coresolution and the first and third vanishings, as explained above. The line summands use the first and second. Since f is finite and B locally free, projection formula identifies this with the original pair-character group. Therefore, provided the P4 inputs and F's identification with H are valid over the actual field, the original-pair Ext¹ gate is closed geometrically without importing the old 450/100/90 staircase ranks. Those ranks become a consistency comparison rather than a necessary additional input.

The four P4 tables alone did not give this conclusion; the missing input was the exact original-coefficient pushforward decomposition just proved. This derivation preserves the distinction between ordinary-bundle vanishing and an equivariant character statement.

Source provenance: the older ranks occur in https://github.com/Akilleez-QA/read-em-and-weep/blob/add03476d9055aa00e1e00778eea6332cf8e01cc/research/hm/ext-model.md §4. They are a distinct original-pair calculation, not the small P4 certificate. This note has not executed either computation.

## 7. Conditional recovery of the dimension 514 without staircase ranks

If the supplied P4 tables also give H⁰(B(-2))=0, χ(B(-2))=χ(B(-3))=20, χ(B(-1))=5, χ(B)=-21, and concentration of B(-2),B(-3) in degree two, the full original-pair group is concentrated in degree two and has dimension 514. Indeed H⁰(B⊗Ω²)=0 from the injection into 10B(-2); H¹ vanishes above; and the canonical wedge pairing Ω²⊗Ω²→ω_P4 together with the trace pairing B≅B* gives H³=H¹*=0 and H⁴=H⁰*=0. Thus

h²(B⊗Ω²)=χ(B⊗Ω²)=10χ(B(-2))-5χ(B(-1))+χ(B)=200-25-21=154.

Adding the eighteen line summands gives h²=154+9·20+9·20=514. This conditional calculation uses Euler characteristics and Serre duality only, not any original-pair staircase differential.

# Universal Picard defect: reflexivity and the exact Postnikov annihilator

Status: authored structural proof; independently mathematically reviewed (PASS); not formally checked. Work over C. No selected actual HM/source-instance evaluation or large computation is used.

## 1. Dependency and scope

The sole geometric input is PR583, commit **ce046d10a03a609aee3d0125b3264dd36bb9d598**, `research/hm/universal-picard/PROOF.md`, with its explicitly pinned dependencies. In particular, its actual relative normalization complex and residue factorization are assumed, not reconstructed from dimension counts.

Let A=C[t_z^{±1}:z∈Z] be its thirty-variable parameter ring. Fix one of the six residual nodes q and label its five ratios t1,...,t5. All other parameters remain independent units. Put

    δ=(t2−t1,t3−t1,t4−t1,t5−t1)^T,    I=(δ1,δ2,δ3,δ4).

PR583 identifies the finite defect at q with K=coker(M), where M:A²→A⁵ sends (α,β) to (α−tiβ)i. It also identifies the actual relative complex locally with the residue complex and an already split elliptic summand. The claims below concern that universal family. They do not assert a selected HM repair, a full adjoint δ20 statement, higher-order lifting, algebraicity, or multiplicative formality.

## 2. Minimal presentation and singular locus

Set α'=α−t1β and subtract the first target coordinate from each of the other four. These are invertible A-linear changes. The matrix becomes diag(1,−δ), with the second block a four-by-one column. Consequently

    0 → A --−δ--> A⁴ → K → 0.                    (1)

The sequence δ1,...,δ4 is regular: successively imposing tj=t1 leaves a Laurent polynomial domain, and A/I is the Laurent coordinate ring of the uniform-block subtorus. Its codimension is four.

Thus K has generic rank three. Its third Fitting ideal is the ideal of the one-by-one minors of the presentation (1), namely

    Fitt_3(K)=I;    Fitt_4(K)=A;    Fitt_2(K)=0.   (2)

At a prime not containing I, one coordinate δi is a unit and (1) splits, giving K_p≅A_p³. At a prime containing I, the specialized presentation has zero differential, so K_p needs four generators; its generic rank is three and it cannot be free. Its local projective dimension is one there and zero elsewhere. In particular the non-locally-free locus is exactly V(I), with its smooth codimension-four reduced scheme structure given by Fitt_3(K).

## 3. Reflexivity and dual Koszul structure

Dualizing (1) gives

    0 → K* → (A⁴)* --−δ^T--> A → Ext¹_A(K,A) → 0,

and no higher Ext. Hence

    Ext¹_A(K,A)=A/I,    Ext^j_A(K,A)=0 for j≥2.   (3)

K* is the first syzygy module of the four generators of I. With F=A⁴ and its ordered basis, let the Koszul differential be contraction by δ^T. Koszul exactness gives the explicit free resolution

    0 → Λ⁴F → Λ³F → Λ²F → K* → 0,              (4)

where the last map is the degree-two Koszul differential with image ker(δ^T:F→A). Signs or identification of F with its dual do not affect the module statements.

For a direct proof of reflexivity, the regular sequence has

    Ext^j_A(A/I,A)=0 for j<4.

From 0→I→A→A/I→0 it follows that I*=A and Ext¹_A(I,A)=0. Dualize 0→K*→(A⁴)*→I→0. This gives

    0 → A → A⁴ → K** → 0,

whose first map is the same column −δ as in (1), under I*=A. Naturality identifies the induced isomorphism K≅K** with the evaluation map. Thus K is reflexive, despite failing to be locally free on V(I). This is stronger than the fiber-dimension and Tor calculation of PR583.

## 4. The actual two-extension and cancellation

Use the completed residual node R=C[[s,t]]/(st), its normalization Rbar=C[[s]]⊕C[[t]], and m=(s,t). Work with T=R⊗_C A and B=Rbar⊗_C A; this is algebraic tensor extension of the fixed completed node. The residue quotient is A². Write m_A=m⊗A, and regard A and K as T-modules through T→A. The actual PR583 two-extension is

    0 → m_A → B --d--> A⁵ → K → 0.              (5)

Apply the target coordinate operation of section 2. The first component of d becomes α−t1β and the remaining components become −δβ. The first component B→A is surjective. Its kernel is

    E={ (f,g)∈B : f(0)=t1 g(0) }.

There is an exact residue extension

    0 → m_A → E --β--> A → 0.                   (6)

As a T-module E≅T, by (r_s,r_t)↦(t1 r_s,r_t); this uses t1∈A×. The inclusion m_A→E in (6) is the inherited inclusion of branch-vanishing pairs, not the standard inclusion transported without its branch scaling.

The inclusion of complexes [E→A⁴]→[B→A⊕A⁴] has acyclic quotient [A→A]. Hence the actual Postnikov two-extension is equally represented by

    0 → m_A → E --−δβ--> A⁴ → K → 0.            (7)

It is exactly the Yoneda splice of (6) and (1). In particular it is the actual relative class, not an arbitrary Ext² class selected by matching fibers. Let κ denote its class in Ext²_T(K,m_A).

## 5. Exact parameter annihilator

We compute enough of Ext²_T(K,m_A) to locate κ without claiming the entire Ext group has been computed.

First,

    E1:=Ext¹_T(A,m_A) ≅ Ext¹_R(C,m)⊗_C A ≅ A².  (8)

For completeness, tensor the finite-rank free resolution of the R-module C with A. Flat extension over C gives a T-free resolution of A and commutes with the Hom complex and its cohomology. Also m≅R/(t)⊕R/(s). The resolution of C begins with d1=(s,t), d2=diag(t,s), d3=diag(s,t), continuing alternately. Applying Hom to R/(t) gives Ext¹_R(C,R/(t))=C, and similarly for the other branch. This proves the last equality in (8).

The normalization residue sequence 0→m→Rbar→C²→0 induces an injective boundary Hom_R(C,C²)→Ext¹_R(C,m), because Hom_R(C,Rbar)=0. Both vector spaces have dimension two, so the boundary is an isomorphism. Its extension over A identifies E1 with A². In this basis the class e of (6), the pullback along A→A², β↦(t1β,β), is

    e=(t1,1).                                   (9)

Apply Ext_T(−,m_A) to (1), which is also exact as a sequence of T-modules. The pertinent segment is

    E1⁴ --(−δi)--> E1 --∂--> Ext²_T(K,m_A).

The first map has image I E1. Therefore it induces a canonical injection

    E1/I E1 ≅ (A/I)² ↪ Ext²_T(K,m_A).            (10)

The connecting map is Yoneda splicing, so κ=∂e (up to a simultaneous harmless sign convention). By (9), its preimage in (10) is (t1 mod I,1). Its second coordinate is one. It follows, without any generic-point argument, that

    Ann_A(κ)=I.                                 (11)

In particular each ratio difference δi annihilates the actual class; conversely a parameter function annihilates it only if it belongs to I. This identifies the exact scheme-theoretic parameter support of the cyclic class Aκ as the uniform subtorus:

    Aκ ≅ A/I.                                   (12)

The statement is about the A-action on the Ext class, not a new assertion about the full annihilator in T.

## 6. Consequences and limitations

Equation (11) strengthens the nonsplitting argument in PR583: the obstruction is a nonzero section with precisely reduced uniform-block support and no additional parameter annihilators. At every parameter prime containing I, κ remains nonzero after localization because (10) remains an injection and its representative has a unit coordinate. Away from V(I), it vanishes. Thus the exact parameter-local splitting locus of the node complex is recovered directly from its canonical two-extension.

For all six nodes, the finite defects have disjoint support on Γ. The completed nodewise Postnikov components κ_q satisfy Ann_A(κ_q)=I_q. Therefore the parameter annihilator of their direct sum is ∩_q I_q, and the corresponding parameter support is the reduced union of the six uniform-block subtori. This is a statement about the direct sum of the nodewise components, not an unproved global Ext decomposition.

Do not infer that the underived pullback of κ along a closed fiber is the fiber's Postnikov class: K is not parameter-flat on V(I), and derived specialization changes cohomology through Tor¹. All individual-fiber splittings from PR582 and PR583 remain compatible with (11). In particular this proof makes no claim that restriction to a uniform subtorus preserves the universal kernel m_A.

No numerical experiment is needed: the checks are invertible row/column operations, a regular sequence, the Koszul resolution, the explicit nodal resolution, and the long exact Ext sequence. Independent mathematical review and formal checking must be recorded separately.

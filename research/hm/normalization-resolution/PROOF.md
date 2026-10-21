# Actual normalization-module resolution by derived pushforward

Status: structural derivation, independently mathematically reviewed (PASS); see REVIEW.md. Not formally checked. Work over C. No selected actual HM/source instance, coefficients, points, matrices, ranks, or large computation are evaluated.

## 1. Inputs and contribution

Use the actual relative Pfaffian model and finite normalization identification recorded in PR588, Sections 1–2, at immutable commit 7547a6a0d84d29478a0bad2d30bda271c37c269e:

https://github.com/Akilleez-QA/read-em-and-weep/blob/7547a6a0d84d29478a0bad2d30bda271c37c269e/research/hm/quadratic-conductor-generation/PROOF.md
 Its earlier source dependencies are PR570, PR574, and Barth–Hulek–Moore, §3.4 and §4.5. Thus X is the actual smooth codimension-three Pfaffian surface in Y=P4×P1, p:Y→P4 is projection, p|X=ν is finite with image S, and H=O_Y(1,0)|X. The actual ideal J=I_(X/Y) has resolution

0→A→B→C→J→0,
A=O_Y(-5,-5), B=O_Y(-3,-3)^5, C=O_Y(-2,-2)^5.

The new dependency resolved here is existence and exactness of an actual minimal graded resolution of the normalization section module. Its Betti table is NOT inferred from a Hilbert numerator. The previously established quadratic-generation result does not itself establish its syzygies. No claim of historical novelty relative to BHM is made.

Put P=C[x0,…,x4] and N=⊕_(n∈Z)H0(X,nH). The conclusion is

0→P(-5)^4→P(-3)^10→P⊕P(-2)^5→N→0.                 (R)

The corresponding sheaf resolution has final term ν_*O_X. All maps are induced by the actual relative resolution and its derived connecting morphisms; no numerical choice of a matrix is made.

## 2. A chain-map representability lemma

If L• is a bounded complex of locally free sheaves on P4 and V is a sheaf such that Ext^q(L^i,V)=0 for every term i and every q>0, then

Hom_(K)(L•,V[m]) ≅ Hom_(D)(L•,V[m])

for every m. Indeed the hyper-Ext spectral sequence computing RHom(L•,V) has E1 terms Ext^q(L^i,V) and collapses to the ordinary Hom complex. Its cohomology computes chain maps modulo chain homotopy. This argument only needs the stated directed Ext vanishings; it does not require a full exceptional or tilting collection, or vanishing of Ext in the reverse direction.

For line bundles, Ext^q(O(a),O(b))=H^q(P4,O(b−a)). Positive twists have no higher cohomology. Therefore the lemma applies to all source-target pairs used below.

## 3. First cone: Rp_*K

Set K=coker(A→B); exactness of the actual Pfaffian complex gives

0→A→B→K→0,       0→K→C→J→0.

Write E=O(-5)^4, F=O(-3)^10, G=O(-2)^5 on P4. Cohomology of P1 and projection formula give

Rp_*A=E[-1], Rp_*B=F[-1], Rp_*C=G[-1], Rp_*O_Y=O.

Our convention is that V[-1] has V in cohomological degree 1. The morphism E[-1]→F[-1] is an ordinary sheaf morphism e:E→F. Applying Rp_* to the first short exact sequence identifies Rp_*K with its cone, represented by

L•=[E→F], in degrees 0,1.

This is a derived statement, not a claim that the original pushforward is termwise exact.

## 4. Second cone: Rp_*J

The second short exact sequence gives a triangle Rp_*K→G[-1]→Rp_*J. For E and F mapping to G the relevant twists are 3 and 1. Hence all positive Ext groups vanish. The lemma represents its first arrow by an actual chain map L•→G[-1], necessarily a map h:F→G satisfying he=0. Consequently Rp_*J is represented by

Q•=[E→F→G], in degrees −1,0,1,

up to the harmless cone sign convention. Its cohomology sheaves are p_*J=I_S in degree 0 and R1p_*J=T in degree 1. In particular this three-term complex must NOT be assumed exact in its middle.

## 5. Final cone and exactness

The actual inclusion J→O_Y gives a morphism Q•→O in the derived category. For E,F,G mapping to O the twists are 5,3,2, so all positive Ext groups vanish again. The lemma therefore gives an actual chain representative, with sole component f:F→O and fe=0.

Applying Rp_* to J→O_Y→O_X now identifies Rp_*O_X with the cone of this chain map. That cone is

E→F→O⊕G, in degrees −2,−1,0.                         (C)

The differential F→O⊕G has components f and ±h. The signs can be absorbed into a summand automorphism. Since p|X is finite, Rp_*O_X=ν_*O_X is concentrated in degree 0. Thus (C) has zero cohomology in both negative degrees and gives an exact sequence

0→O(-5)^4→O(-3)^10→O⊕O(-2)^5→ν_*O_X→0.              (S)

The O summand maps by the actual unit O→ν_*O_X, because it is the O term of the cone triangle. This map has kernel I_S, not zero. Nothing here splits ν_*O_X or identifies its nonambient quotient as a free module.

The potentially nonzero reverse Ext^4(O,O(-5)) never occurs in either representability argument: each target was G or O and each source was E,F, or G. There is consequently no hidden assumption excluding that reverse Ext group.

## 6. Exact global graded sections and minimality

Let D be the image of F→O⊕G in (S). Split (S) into

0→E→F→D→0,       0→D→O⊕G→ν_*O_X→0.

For every integer n, H1(E(n))=H1(F(n))=H2(E(n))=0 because all intermediate cohomology of line bundles on P4 vanishes. The first sequence therefore gives both exactness of

0→H0(E(n))→H0(F(n))→H0(D(n))→0

and H1(D(n))=0. The second sequence is thus surjective on H0 in every twist. Summing over all integers gives the exact graded resolution (R), using Γ_*O(-d)=P(-d) and H0(P4,ν_*O_X(n))=H0(X,nH).

Every component of either differential in (R) has positive polynomial degree: E→F has degree 2; F→P(-2)^5 has degree 1; and F→P has degree 3. Thus (R) is minimal over the standard graded polynomial ring. The sheaf resolution (S) is minimal in the corresponding graded sense; sheaf-category minimality is understood via this graded lift, not as local minimality at every point.

In particular N has exactly one degree-zero and five degree-two minimal generators, ten degree-three first syzygies, and four degree-five second syzygies. Its projective dimension is exactly 2 and Auslander–Buchsbaum gives depth_(P_+)N=5−2=3. The finite graded module has dimension 3 since its sheaf support is the surface S. It is therefore Cohen–Macaulay.

## 7. Structural consequences, now justified by an actual resolution

The Hilbert series and regularity are

Hilb_N(t)=(1+5t²−10t³+4t⁵)/(1−t)^5
         =(1+2t+8t²+4t³)/(1−t)^3,
reg(N)=3.

The same two short exact sequences also give H2(D(n))=0 for every integer n, using H2(F(n))=H3(E(n))=0, and hence H1(X,nH)=0 for every integer n. Thus the relative Pfaffian argument independently supplies the normalization-cohomology vanishing used in the conductor calculation, without the earlier geometric vanishing dependency.

The multiplicity is 15. For n≥0 one also has the exact Hilbert function

h0(X,nH)=binom(n+4,4)+5 binom(n+2,4)−10 binom(n+1,4)+4 binom(n−1,4),

where a binomial contribution is zero when its top index is below 4. The beginning is 1,5,20,50,95,155,230 in degrees 0 through 6.

A further consequence of CM is that the canonical module ω_N=Ext²_P(N,P(-5)) has the dual resolution

0→P(-5)⊕P(-3)^5→P(-2)^10→P^4→ω_N→0.

Here Ext^i_P(N,P(-5))=0 for i≠2 follows from Cohen–Macaulayness and codimension 2, so dualizing is exact in the asserted places. Hence ω_N has four minimal generators, all in degree zero: N is level of type 4 and a-invariant 0. This is a consequence, not an additional input.

## 8. Boundary and remaining problem

Neither (R) nor its Hilbert function determines the ranks r_n of the conductor-difference maps. The unit P→N has kernel I_S. In particular quotienting (R) by its P summand does NOT preserve exactness on the left. The complex E→F→G has I_S as middle cohomology and T as final sheaf cohomology. Its degreewise quotient N/im(P) may have a nontrivial kernel in its map to Γ_*T. Further actual conductor-rank or lower postulation claims require a new structural argument. This result makes no selected-source evaluation and implies no original-target lift or algebraicity statement.

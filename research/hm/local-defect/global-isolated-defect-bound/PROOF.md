> Publication scope: preserved mathematical proof/audit. Historical statements that rank eight remains open are superseded only after the final assembly and all its prerequisites. No source-instance evaluation or formal verification is claimed here.

# A global bound of 390 for the isolated defect

## Statement (independent audit: PASS)

Let B be a rank-two reflexive sheaf on complex P4, with finite singular locus, slope-semistable with c1(B)=0 and c2(B)=5. Put T=Ext²(B,O). Then

    length(T) ≤ 390.

The proof does not assume B locally free, stable restriction, or any particular kernel presentation. Consequently, **conditional on the independently established equivariant lower bound length(T)≥480**, these hypotheses contradict that lower bound. The lower bound is not proved here. Independent audit of this upper-bound document returned PASS; the separate assembly with the equivariant lower bound remains a distinct verification step.

## 1. Hyperplane telescoping bounds the local defect by a Rao module

Choose a general hyperplane H avoiding the finite singular support. E=B|H is a rank-two vector bundle on P3. The Flenner restriction theorem used in ../rank-eight-third-chern-bound/PROOF.md gives slope-semistability. It has c1=0,c2=5 and, being a bundle of rank two, c3=0.

Set q(t)=h²(P4,B(t)) and r(t)=h¹(P3,E(t)). The exact hyperplane sequence gives

    q(t−1)−q(t) ≤ r(t).

For t≫0, q(t)=0 by Serre vanishing. For t≪0, Serre duality gives

    H²(B(t))* = Ext²(B(t),O(−5))
                = Ext²(B,O(−t−5)).

Writing k=−t−5≫0, local-to-global Ext has terms H^p(Ext^q(B,O)(k)). For k sufficiently large all terms with p>0 vanish by Serre vanishing, so Ext²(B,O(k))=H⁰(T(k)). Since T has finite support, its dimension is length(T). Thus q(t)=length(T) for t≪0. Summing the inequality over all t proves

    length(T) ≤ Σ_t h¹(E(t)).                         (1)

All Ext in the first display are global Ext, and T denotes sheaf Ext. This distinguishes the two operations and fixes the duality index.

## 2. Two primary cohomological inputs

(A) Ellia–Gruson, *A restriction theorem for stable rank two vector bundles on P3*, Theorem 1 and Proposition 6, give for a general plane P⊂P3 and F=E|P:

    h⁰(F(1)) ≤ 3.                                  (2)

If E is stable, the stronger bound is 2, since c2=5≥4. If E is properly slope-semistable and indecomposable, Proposition 6 gives equality 3. E is indecomposable: a decomposable semistable bundle with c1=0 would be O² and have c2=0. No assertion of stability of E is needed.

Primary PDF read directly (pp.1,4): https://arxiv.org/pdf/1409.3789 .

(B) The standard Mumford regularity lifting lemma says: if the restriction G|D to a hyperplane is m-regular, then G is (m+h¹(G(m−1)))-regular. Its hypotheses require the hyperplane restriction sequence exact. A directly read primary research-paper formulation is Georg Hein, *Restriction of stable rank two vector bundles in arbitrary characteristic*, Lemma 2.2, printed p.9: https://arxiv.org/pdf/math/9904102 . We apply this only to vector bundles and projective-space hyperplanes.

We also use the usual Grauert–Mülich theorem: a slope-semistable rank-two bundle on complex projective space with c1=0 restricts to O_L² on a general line. Original reference: H. Grauert–G. Mülich, *Vektorbündel vom Rang 2 über dem n-dimensionalen komplex-projektiven Raum*, Manuscripta Mathematica 16 (1975), 75–100, DOI https://doi.org/10.1007/BF01169064 . The original bibliographic identity was verified. Its exact semistable rank-two c1=0 formulation was additionally read in the primary research article Al Vitter, *Restricting semistable bundles on the projective plane to conics*, Introduction p.1, https://arxiv.org/pdf/math/0310076 .

## 3. Plane bounds

F is semistable. One route is the same characteristic-zero Flenner theorem on P3 (numerical condition 2>1). Independently, if E is stable, Barth’s restriction theorem gives F stable since c2=5≠1; this exact statement is recalled in Ellia–Gruson, Introduction p.1. If E is properly semistable, its section gives 0→O→E→I_C→0 with C a codimension-two local complete intersection curve. Restricting to a general plane gives 0→O_P→F→I_{C∩P,P}→0, so H⁰(F(−1))=0 and F is semistable. Thus the argument does not depend on a second use of Flenner. F has determinant O and c2=5. Choose a general line L⊂P with F|L=O_L².

Riemann–Roch on P2 gives

    χ(F(t))=(t+1)(t+2)−5.

Semistability gives h⁰(F(t))=0 for t<0. Self-duality and Serre duality give h²(F(t))=h⁰(F(−t−3)). In particular h¹(F(−1))=5. Since O_L² is 0-regular, input (B) gives that F is 5-regular. Consequently

    h¹(F(t))=0 for t≥4 and, by duality, for t≤−7.  (3)

Moreover h⁰(F)≤1. Indeed two independent sections are either generically independent, making the determinant a nonzero constant and forcing F=O², or they lie in a saturated rank-one line subsheaf O(d). Semistability and the existence of a section force d=0, which has only one independent section. Both alternatives contradict two independent sections when c2=5.

For j≥2 the line exact sequence and (2) give

    h⁰(F(j)) ≤ 3+Σ_{k=2}^j 2(k+1)=(j+1)(j+2)−3.

Thus for t=0,1,2,3, respectively, h¹(F(t))≤4,2,2,2. For t=−1,−2 the value is 5. Duality h¹(F(t))=h¹(F(−t−3)) supplies the remaining negative twists. Combining with (3):

    t          −6 −5 −4 −3 −2 −1  0  1  2  3
    h¹(F(t)) ≤  2  2  2  4  5  5  4  2  2  2,

and h¹(F(t))=0 outside this interval. The sum of these bounds is 30.

At twist 4, regularity and semistability give h¹(F(4))=h²(F(4))=0, hence h⁰(F(4))=25. We also have

    h⁰(F(0)),...,h⁰(F(4)) ≤ 1,3,9,17,25.           (4)

## 4. Bound the entire Rao module on P3

Because E is a vector bundle, h¹(E(t))=0 for t≪0: duality turns this into Serre vanishing of H²(E*(−t−4)). The plane exact sequence gives

    h¹(E(t)) ≤ h¹(E(t−1))+h¹(F(t)).

Induction from −∞ and §3 yields h¹(E(t))=0 for t≤−7 and the following upper bounds:

    t          −6 −5 −4 −3 −2 −1  0  1  2  3
    h¹(E(t)) ≤  2  4  6 10 15 20 24 26 28 30.

Their sum is 165.

Since H⁰(E(−1))=0 by semistability, repeated restriction and (4) give

    h⁰(E(4)) ≤ 1+3+9+17+25=55.

On P3, χ(E(t))=2 binom(t+3,3)−5(t+2), so χ(E(4))=40. Self-duality gives h²(E(4))=h¹(E(−8))=0, already proved, and h³(E(4))=h⁰(E(−8))=0. Therefore

    h¹(E(4))=h⁰(E(4))−40≤15.

F is 5-regular, so input (B) makes E (5+h¹(E(4)))-regular, hence at worst 20-regular. Therefore h¹(E(t))=0 for t≥19. Finally, h¹(F(t))=0 for t≥4 makes h¹(E(t)) nonincreasing in that range. For all fourteen twists t=5,...,18 it is at most 15. Thus

    Σ_t h¹(E(t)) ≤ 165+15+14·15=390.              (5)

Combining (1) and (5) proves the statement.

## Scope and verification status

The proof imports Flenner exactly as already documented in ../rank-eight-third-chern-bound/PROOF.md. New specialized inputs (A) and (B) were read in primary full PDFs. The exact Grauert–Mülich formulation was read in Vitter’s primary research paper, with the original primary reference also identified. Plane semistability has a separately documented Barth/section argument; it is not being inferred from stability of B without justification. All remaining statements are elementary cohomology, Riemann–Roch, duality, and regularity consequences displayed explicitly above.

No spectrum classification, stability of the P3 restriction, blanket absence of isolated reflexive singularities, or unproved c4 bound is assumed. No operation, matrix, physical source, rank instance, jet, or detector was evaluated. This is a structural cohomological bound independent of the original kernel's presentation.

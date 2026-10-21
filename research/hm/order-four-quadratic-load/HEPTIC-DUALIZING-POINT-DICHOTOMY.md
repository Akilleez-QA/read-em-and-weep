# The heptic's canonical section and its exact marked-point dichotomy

## Hypotheses and conclusion

Let D⊂P3 be the integral ACM degree-seven genus-five curve obtained in the generic b=3 curve-base alternative. Its ideal has resolution

    0 → O(-4)⊕O(-5) --M--> 3O(-3) → I_D → 0,

where M has independent linear entries ℓ_1,ℓ_2,ℓ_3 in its first column and quadratic entries q_1,q_2,q_3 in its second. Let P=V(ℓ_1,ℓ_2,ℓ_3), the canonical point already known to belong to D and to avoid Z.

There is an intrinsic exact sequence

    0 → O_D → ω_D(-1) → k(P) → 0.                    (1)

The first arrow is the unique nonzero global section up to scalar. The entire failure of this section to generate its rank-one torsion-free sheaf has length one and is supported exactly at P.

There are precisely two local possibilities:

- If (q_1(P),q_2(P),q_3(P))≠0, P is smooth; D is Gorenstein everywhere, and ω_D≅O_D(1)(P).
- If q_1(P)=q_2(P)=q_3(P)=0, P is singular of embedding dimension three and Cohen–Macaulay type two. It is the unique non-Gorenstein point of D. The sheaf ω_D(-1) is not a line bundle, so (1) must NOT be rewritten using an ordinary Cartier divisor P.

No present input decides which of these alternatives occurs in the actual family. In particular the canonical point is not forced non-Gorenstein merely by the resolution or the unique canonical section.

## 1. Dualize the actual resolution

Append O→O_D to the displayed resolution and apply sheaf Hom(-,ω_P3)=Hom(-,O(-4)). Because D is Cohen–Macaulay of codimension two, its only nonzero sheaf Ext into ω_P3 is Ext², equal to ω_D. Twisting by O(-1) gives the exact dual resolution

    0 → O(-5) → 3O(-2)
      --M^t--> O(-1)⊕O → ω_D(-1) → 0.              (2)

The i-th column of M^t is (ℓ_i,q_i). In particular the O summand furnishes a global section s of ω_D(-1).

Let K be the image of 3O(-2) in O(-1)⊕O. The sequence 0→O(-5)→3O(-2)→K→0 and the vanishing of H¹ and H² of line bundles on P3 give H0(K)=H1(K)=0. Consequently

    H0(ω_D(-1)) ≅ H0(O(-1)⊕O) ≅ C,

and s is nonzero and spans it. This establishes the section directly from the dual resolution, without assuming ω_D is invertible.

Integral D makes ω_D a rank-one torsion-free sheaf. Thus multiplication by its nonzero section gives an injection O_D→ω_D(-1). To compute its cokernel, quotient presentation (2) by the O summand. The result is

    coker(3O(-2) --(ℓ_1,ℓ_2,ℓ_3)--> O(-1))
      = O_P(-1) ≅ k(P).

This proves (1), including support and scheme length. The final identification with k(P) is up to a scalar trivialization of the one-dimensional fiber, which does not affect the exact sequence's support or length.

As a consistency check, deg ω_D=2p_a−2=8 and deg O_D(1)=7, so deg ω_D(-1)=1. Sequence (1) accounts for precisely that degree difference.

## 2. Away from P the curve is a local complete intersection

At any p≠P at least one ℓ_i is a unit in the ambient local ring. Row and column operations then eliminate that entry of the Hilbert–Burch matrix, and its ideal of maximal minors is generated locally by two elements. Since the ideal has height two, these form a regular sequence in the regular three-dimensional ambient local ring.

Therefore D is lci, hence Gorenstein, at every p≠P. It may still have Gorenstein singularities there; this statement does not assert global smoothness.

## 3. Nonzero quadratic value makes P smooth

Work in the regular ambient local ring R=O_P3,P. The three independent linear forms, after local trivialization, form a regular system of parameters x_1,x_2,x_3. Put a_i=q_i(P).

The minors are x_i q_j−x_j q_i. Their linear terms at P are x_i a_j−x_j a_i. If the vector a is nonzero, these span a two-dimensional subspace of m_R/m_R²: the linear map v↦v∧a has rank two. The Zariski tangent space of D at P therefore has dimension one. Since D has dimension one and is reduced, its local ring is regular. Thus P is smooth.

Together with Section 2, D is Gorenstein everywhere, so ω_D(-1) is a line bundle. The zero scheme of s is the length-one point P by (1); it is an effective Cartier divisor. Hence ω_D(-1)≅O_D(P), giving ω_D≅O_D(1)(P).

Equivalently in this case the embedding hyperplane bundle is ω_D(-P). This assertion applies to the dualizing bundle of the possibly singular Gorenstein curve, not only to a smooth canonical curve.

## 4. Zero quadratic value gives the unique type-two point

If all q_i(P)=0, every entry of M belongs to m_R. Every maximal minor then lies in m_R², so the embedding dimension of A=O_D,P is three. Since dim A=1, P is singular.

The localized free resolution

    0 → R² → R³ → R → A → 0

is minimal: its maps have entries in m_R. Dualizing, the canonical module ω_A has two minimal generators, since its presentation R³→R² has zero reduction modulo m_R. Therefore the Cohen–Macaulay type is two. In particular A is not Gorenstein. Section 2 proves that no other point is non-Gorenstein.

More precisely, let e_1,e_2 be the local generators corresponding to O(-1),O in (2). Then

    ω_A = (A e_1⊕A e_2)/(x_i e_1+q_i e_2 : i=1,2,3),
    s=e_2,    ω_A/A s ≅ k(P).

Thus s is one of the two minimal generators, not a local equation vanishing at a smooth point. Since the x_i generate m_A, the relations show m_A ω_A⊂A s. This is a concrete canonical-module constraint, stronger than simply declaring the point singular. It provides a valid length-one canonical extension even though P is not Cartier.

## 5. Intrinsic meaning and boundary

The ideal generated by all entries of M cuts out the non-Gorenstein locus of a codimension-two Cohen–Macaulay determinantal curve. Here its support is contained in {P}, and the preceding local calculation decides whether it is empty or {P}.

The zero/nonzero condition for q(P) is independent of all allowed minimal-resolution basis changes. Indeed the linear column is unique up to nonzero scalar and row changes; replacing the quadratic column by a scalar multiple plus a linear multiple of the linear column does not alter its vanishing at P. Intrinsically it is equivalent to whether ω_D(-1) is locally free at the support of the cokernel (1).

For the HM family P lies outside the 25 marked points, so this possible non-Gorenstein defect is disjoint from Z. In the smooth-P alternative all of D is Gorenstein; in the other alternative its only non-Gorenstein defect lies at this canonical unmarked point. Neither alternative has been excluded here, and no full Q4 conclusion follows.

Source input: THREE-CUBIC-SEXTIC-HEPTIC-DICHOTOMY.md, Akilleez-QA/read-em-and-weep, commit 435a20fc680c7ccecc3cbfd762a3d5ae97b76299. The input was read locally and through the pinned GitHub source. This note gives a new dualizing-module deduction and local classification; it is not a review. No selected coefficients, source evaluation, numerical ranks, scans, or external writes were used.

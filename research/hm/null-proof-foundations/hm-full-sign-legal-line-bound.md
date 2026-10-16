# A simple legal-line pole bound for the complete full-sign lift

## Result and scope

The complete, normalized, included full-sign source `J0` and all three HPL corrections `J1,J2,J3` have **legal-line pole order at most one in each coordinate**, after their separately owned carrier denominators are recorded. This applies to all six carrier choices, including auxiliary carriers in the residual tail.

The proof is a direct argument from the full matrix formulas. It does not reuse the primary-only pole-graph output, a scalar row, the scalar carrier merger, or exclusion of auxiliary tail assignments. It retains nonconstant line-frame ratios and cancels their undifferentiated factors algebraically.

Consequently the regular cover transport may use carrier power `N_carrier=62` and legal-line power `N_line=1`, with the same resulting chain-map and prism proofs. No residual coefficients are expanded or evaluated here.

## Pinned sources

Every repository source below is pinned to commit `08b73637d4136f91606aad332c46cafd064417f8`.

- [Exact source excerpts](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-geometric-dependencies/data/source-formulas.js): `globalBuild2`, its `first` function, `crossResidual`, and `globalCross`.
- [Physical frames and poles](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-geometric-dependencies/frames-and-poles.md), §§1–4.
- [First-order source](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-residual-attribution/first-order-source.md), §§1–4.
- [Full-sign residual and its closed End inclusion](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-residual-attribution/closure-and-characters.md), §§2–3.
- [Full ambient second jet](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-residual-attribution/ambient-second-jet.md), §3.
- [Source identity and common-frame homotopies](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-geometric-dependencies/source-identity.md), §§1–2.

This concerns the declared characteristic-zero source. It is not a geometric specialization theorem in another characteristic.

## 1. Separate carrier denominators from legal-line seeds

Fix a standard product chart and use its original homogeneous frames. For any actual tuple of source vertices, let the carrier coefficient ring be the local coordinate ring with precisely the tuple's owned carrier factors inverted. The homogeneous primitive certificate puts every bare `I,P,H0,H1,eta,W,L` entry in this ring. Its coordinate derivatives remain in this ring, with possibly higher orders along the same owned carrier factors.

This statement holds for all five primary carriers and the auxiliary carrier. The auxiliary factors `(v0,v1,v3,v4)` are kept as auxiliary-owned carrier factors; if one vanishes along a coordinate divisor, it is not silently reclassified as an unowned legal-line pole.

We must therefore bound only the additional line-mask-dependent factors coming from frame logarithms, the old connections, and the q cochains.

## 2. Exact cancellation in the splitting-connection matrices

At a source vertex i, write its physical splitting and inverse as

`U_i = Ubar_i W_i`, `Q_i = W_i^−1 Qbar_i`,

where `W_i=diag(ν_i^p)` has the column powers specified in the source. For U0 the powers are −2 on the five gamma columns, 0 on the first I column, −2 on the second I column, and +2 on the eight H1W columns. For U1 they are 0 on the W columns and +2 on the eta columns.

Set `α_(i,a)=∂_a log ν_i`, and let P denote the constant diagonal matrix of these column powers. Then

`−(∂_a U_i)Q_i`

`=−(∂_a Ubar_i)Qbar_i−α_(i,a) Ubar_i P Qbar_i`.

There is no undifferentiated ν factor in this identity. Subtracting the old diagonal connection gives

`B_(i,a)=carrier-only matrix + α_(i,a)·carrier-only matrix`

`                                    + γ_(i,a)·constant diagonal matrix`.

Thus each term of B_(i,a) contains at most one legal seed, belonging to coordinate a. The extreme blocks, which have only their old-connection term, obey the same bound. This uses the actual column-factorization of U and Q, not a normalization that treats ν as constant under differentiation.

## 3. Exact cancellation of transition endpoint factors

Let `D_i=diag(ν_i,ν_i^−1)` and let the carrier-only row transition core be

`gbar_ij=(P_i I_j)^t`.

The physical row transition is exactly

`g_ij=D_j gbar_ij D_i^−1`.

Writing `A_(i,a)=diag(α_(i,a),−α_(i,a))`, differentiation gives

`∂_a g_ij=D_j(∂_a gbar_ij+A_(j,a)gbar_ij−gbar_ij A_(i,a))D_i^−1`.

For distinct coordinates, further differentiation retains these endpoint factors. Its interior introduces at most one A seed for each differentiated coordinate: `∂_b α_(i,a)=0` when `a≠b`, because ν is a product of one-coordinate frame ratios.

The inverse has the reversed endpoints. Therefore the paired derivative expression `K(g)=μ1(g^−1,g)` factors as

`K(g_ij)=D_i Kbar_ij D_i^−1`.

The first-lift scalar is a scalar multiple of the identity, so the entire first correction factors as

`u_ij=D_j ubar_ij D_i^−1`.

All terms in the full-sign residual have matching transition endpoints. The scalar gerbe coefficients commute with them. Hence

`R_ijk=D_k Rbar_ijk D_i^−1`,

and left normalization gives

`C2_ijk=D_i Cbar_ijk D_i^−1`,

where `Cbar_ijk=gbar_ik^−1 Rbar_ijk`.

Finally, the physical inclusion and projection are `I_i D_i` and `D_i^−1 P_i`. Transposing after forming the residual gives the exact cancellation

`(I_i D_i) C2_ijk^t (D_i^−1 P_i)=I_i Cbar_ijk^t P_i`.

Thus no undifferentiated ν factor survives in J0. This argument is entrywise, uses the actual matrix multiplication order, and applies equally to auxiliary and primary carriers.

## 4. Why only one legal seed per coordinate survives

Assign coordinate degree e_a to a derivative in coordinate a and to each seed `α_a`, `γ_a`, or `q_a`. Undifferentiated carrier-only matrices have degree zero. The full-sign construction is square-free in these four coordinate degrees:

- B_(i,a) has coordinate degree e_a.
- The first scalar correction for the pair `(a,b)` consists of B_a B_b, q_a B_b, q_b B_a, and q_a q_b terms. Each uses a and b once.
- K(g) for `(a,b)` uses one derivative in each of a and b.
- Consequently u12 uses coordinates 1 and 2 once, and u34 uses coordinates 3 and 4 once.
- The product terms u12 u34 and u34 u12 use all four coordinates once.
- Each cross μ1 term differentiates a first correction only in its complementary pair, with the remaining complementary derivative on the other transition factor.
- Every mixed μ2 term uses four distinct coordinates, divided between the two differentiated transition factors.
- The terms b12 u34, b34 u12, and b12 b34 g again use each coordinate exactly once.

These are exactly the full-sign terms listed in the pinned closure proof and source excerpts. The ambient T and μ1(b,g) terms remain necessary for the unprojected obstruction equation, but the cited character argument proves they have no full-sign component.

No nonzero full-sign monomial can therefore contain two legal seeds for the same coordinate. Nor can it differentiate a coordinate's own legal seed: that would repeat the coordinate. Complementary-coordinate derivatives of that seed vanish.

After the endpoint cancellations in §§2–3, every entry of the full included J0 is consequently a sum of terms with at most one legal seed per coordinate. Matrix multiplication or summing over matrix indices does not change this bound. No cancellation of unknown numerator coefficients is needed.

## 5. Local seed orders and actual mask ownership

For one finite coordinate x with line-mask bit m,

`ν_m² = 1` if m=0, and `(x²−1)/x` if m=1,

`α_m = m (x²+1)/(2x(x²−1))`,

`γ_m = m/[x(x²−1)]`,

`q_ij/y = (m_j−m_i)/x`.

Each nonzero seed has at most a simple pole along x and x²−1. The α and γ seeds occur at a mask-one vertex. A nonzero q seed requires different endpoint masks and therefore also has a present mask-one vertex to own its finite legal factor.

At infinity, put `t=Y/X` and `s=1−t²`. The pinned local homogeneous squared ratios are

`ν_0²=t`, `ν_1²=s`.

Their logarithmic derivatives and the transported old connections are

`α_0=1/(2t)`, `α_1=−t/s`,

`γ_0=0`, `γ_1=−t/s`.

The q coefficient after stripping the local anti-invariant generator z is `(m_j−m_i)/t`, with the fixed Čech orientation. A nonzero coefficient again requires different endpoint masks, so its t pole can be assigned to a present mask-zero vertex. Thus:

- a t pole has a present mask-zero owner;
- an s pole has a present mask-one owner;
- every such pole has order at most one.

The invariant vector field is `−z ∂t`. The local homogeneous primitive matrices, these local squared ratios, and this vector field already implement the source covariance `c_S=τ^(r−2)c_affine`. No additional power of τ is appended to the bound. In particular, this proof does not create a t pole at a mask-one-only tuple where t=0 is permitted.

## 6. All HPL corrections retain the bound

After the included tail is transported to the common original frame, the bare local homotopies depend on the carrier but not on its line mask. The pinned source identity states this equality for different line masks; it follows from the same physical-frame conversion, not from scalar-row cancellation.

The End homotopy is

`h(F)=HF+(−1)^r EFH`, with `E=IP`.

In this common frame H and E are carrier-only matrices. They introduce no legal seed and take no derivative of F. Čech differences merely restrict and add the same sheaf-valued cochains. The recurrence producing J1,J2,J3 therefore preserves the legal-line order-one bound established for J0.

No restriction on whether an auxiliary carrier occurs in the tail or prefix is needed. The proof uses neither a sparse scalar row nor the scalar-specific disjoint-prefix allocation.

## 7. Consequence for the fixed weighted projection

Keep the carrier weights constructed with carrier exponent 62. Independently choose the legal partition at exponent one. On a finite standard chart use

`L_0=1`, `L_1=0`.

On an infinity chart use the fixed polynomial weights

`L_0=t²`, `L_1=1−t²`.

Their sum is one; the first is divisible by the required mask-zero factor t, and the second by the required mask-one factor 1−t². Their products with the carrier weights therefore clear every inserted source vertex in the same per-occurrence domain used by the transport proof.

Use these same weights, restricted from each standard vertex, in both Πρ and Hρ. Restrictions, the Čech differential, the regular internal differential, and the prism preserve the domain; none differentiates the legal weights or source entries.

Changing the fixed partition changes the constructed representative z and comparison primitive W, but the signed comparison still proves that its detector pairing is the same geometric cohomology pairing. It does not identify individual transported coefficients between two different partition choices.

The sharpened bound simplifies the legal-mask weights. It does not evaluate the three surviving dual-row slots or establish the cost of their carrier-dependent coefficient extraction.

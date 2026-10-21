# Two-stage primary correction for a fixed polynomial pair

## Result and distinction from PR477

PR477 §4 identifies the total primary cancellation when a graded extension is reduced modulo an ideal. This note decomposes that cancellation into two successive one-polynomial lifting problems: first v, then u on the v-quotient. The decomposition uses two applications of the snake lemma and requires no regular-sequence assumption. It gives exact graded formulas and a lift procedure for the remaining primary test after computing the residual quotient.

No chosen HM form, source, multiplication matrix, or numerical rank is evaluated. The actual HM extension remains an input, and no original-pair vanishing is asserted.

## 1. General setup and total correction

Let S be a commutative graded ring and let

0→L→K --p→ N→0                                   (1)

be an exact sequence of graded S-modules. Identify L with its image in K. Let u,v be homogeneous elements of degrees a,b>0 and set J=(u,v). No regularity on S or on any of these modules is assumed. All formulas are degreewise; dimensions below apply when the relevant graded pieces are finite-dimensional over the base field.

The usual tensor boundary is

δ_J:Tor₁^S(S/J,N)→A_J:=L/JL,
T_J:=im δ_J=(L∩JK)/JL.                            (2)

It gives the exact sequence

0→A_J/T_J→K/JK→N/JN→0.                            (3)

These are PR477's total-correction formulas. The construction below determines T_J through successive single-element boundaries, without using a Koszul complex to compute Tor for a nonregular pair.

## 2. Stage one: quotient by v

Apply the snake lemma to multiplication by v from (1)(−b) to (1). With the graded annihilator notation

Ann_v(N)(−b)_d={n∈N_{d−b}:vn=0},

the relevant exact segment is

Ann_v(N)(−b) --∂_v→ L/vL→K/vK→N/vN→0.            (4)

For n∈N_{d−b} with vn=0, choose k∈K_{d−b} lifting it. Then

∂_{v,d}(n)=[vk]∈L_d/vL_{d−b}.                    (5)

Changing k by an element of L changes vk by vL, so the class is well-defined. Put

C_v=L∩vK,
Δ_v=im ∂_v=C_v/vL,
Lbar=L/C_v=(L/vL)/Δ_v,
Kbar=K/vK,  Nbar=N/vN.

Equation (4) gives an actual exact sequence of graded modules

0→Lbar→Kbar→Nbar→0.                               (6)

In particular, the first primary term is not generally L/vL. The correction Δ_v must be removed before the second stage is performed.

## 3. Stage two: quotient by u

Apply the snake lemma to multiplication by u from (6)(−a) to (6). It gives

Ann_u(Nbar)(−a) --∂_u→ Lbar/uLbar
  →Kbar/uKbar→Nbar/uNbar→0.                       (7)

Set B_{u|v}=Lbar/uLbar. In terms of the original extension,

B_{u|v}=L/(uL+C_v),
Kbar/uKbar=K/JK,
Nbar/uNbar=N/JN.

Consequently the remaining primary quotient in K/JK is exactly

coker ∂_u=B_{u|v}/im ∂_u.                         (8)

Here ∂_u means the boundary for (6), not the boundary obtained by applying u directly to (1).

### Explicit degree-d lift procedure

Take [n]∈Nbar_{d−a} with u[n]=0. Choose a representative n∈N_{d−a}. There is m∈N_{d−b} such that un=vm. Choose lifts k∈K_{d−a} of n and h∈K_{d−b} of m. Then uk−vh∈L_d and

∂_{u,d}([n])=[uk−vh]
  ∈L_d/(uL_{d−a}+(L∩vK)_d).                     (9)

This is well-defined for every relevant choice:

- Changing k by ℓ∈L_{d−a} adds uℓ.
- Changing h by an element of L adds an element of vL⊂C_v.
- Changing m while keeping vm=un changes h by a lift whose product by v belongs to C_v.
- Changing n to n+vq, with q∈N_{d−a−b}, permits k↦k+v q̃ and m↦m+uq, h↦h+u q̃ for a lift q̃ of q. These changes cancel exactly in uk−vh. Additional lift choices are covered by the preceding points.

Thus (9) is the constructive second snake boundary, including the case where u or v has nontrivial annihilators.

## 4. Exact decomposition of the total Tor image

There is a natural surjection

π:A_J=L/(uL+vL)→B_{u|v}=L/(uL+C_v).

Its kernel is the projected first-stage correction

D_{v|u}:=ker π=(C_v+uL)/(uL+vL)
  =image[Δ_v=C_v/vL→L/(uL+vL)].                  (10)

The total correction is the full preimage of the second correction:

T_J=π⁻¹(im ∂_u).                                 (11)

Proof: the map A_J→K/JK factors as A_J→B_{u|v}→K/JK. Its kernel is T_J by (2), while the second map has kernel im ∂_u by (7). Taking the kernel of the composition proves (11). In particular D_{v|u}⊂T_J and there is an exact sequence

0→D_{v|u}→T_J→im ∂_u→0.                          (12)

This is a filtration of the total cancellation, not a canonical direct-sum splitting. It gives a canonical identification

A_J/T_J≅B_{u|v}/im ∂_u.                           (13)

One can also verify (11) by lifts. If a class of ℓ∈L maps into im ∂_u, formula (9) writes ℓ=uk−vh+uℓ₀+c with c∈C_v, so ℓ∈L∩(uK+vK). Conversely any ℓ=uk+vh∈L gives un=−vm in N, hence [n]∈Ann_u(N/vN), and (9) recovers its image modulo uL+C_v.

When u,v is S-regular, the total Koszul lift boundary in PR477 agrees with this decomposition: a cycle un+vm=0 gives the second-stage class [n], with representative uk+vh; the pure v-annihilator cycles (0,m) contribute the first-stage correction. Without regularity this lift description still computes the image subspaces through (4)–(12), but one must not identify the two-element Koszul homology itself with Tor₁ without an additional justification.

## 5. Exact dimensions and necessary versus sufficient tests

In degree d define

A_{J,d}=L_d/(uL_{d−a}+vL_{d−b}),
ρ_{v|u,d}=rank[Ann_v(N)(−b)_d --∂_v→ L_d/vL_{d−b}→A_{J,d}],
ρ_{u|v,d}=rank[Ann_u(N/vN)(−a)_d --∂_u→(B_{u|v})_d].

Then

dim(T_J)_d=ρ_{v|u,d}+ρ_{u|v,d},
dim(K/JK)_d=dim(N/JN)_d+dim A_{J,d}−ρ_{v|u,d}−ρ_{u|v,d}. (14)

The first rank is the projected Δ_v rank, not its rank before quotienting by uL. Counting both unprojected ranks would double-count possible cancellations.

The exact vanishing test is

(K/JK)_d=0 ⇔ (N/JN)_d=0 and ∂_{u,d} surjects onto (B_{u|v})_d. (15)

For clarity:

- Vanishing of the v-annihilator domain is sufficient for Δ_{v,d}=0, but is not necessary: a nonzero kernel may have zero boundary.
- Vanishing of the u-annihilator domain on N/vN is sufficient for ∂_{u,d}=0, but is not necessary.
- If both relevant domains vanish, there is no extra primary cancellation in degree d; then primary vanishing requires A_{J,d}=0.
- If D_{v|u,d}=A_{J,d}, stage one already removes the entire primary term after projection, so the second boundary has zero target. This is sufficient for primary coverage, not necessary.
- Nonzero annihilator domains do not by themselves prove cancellation or coverage. Their lifted boundary images, and specifically the ranks in (14), are the required tests.
- Residual vanishing and primary coverage are both necessary in (15); neither substitutes for the other.

## 6. Degree-six HM formulas and the square distinction

Use PR477's indexing K_j=H¹B(j−1), its actual extension L=U⊗M(−3), where M_j=H¹F(j), and dim U=4. In this section u is quadratic and v cubic. Write C_{v,6}=(L∩vK)_6. The common first stage is

{n∈N₃:vn=0}→L₆/vL₃,
n↦[v ñ].                                         (16)

For J=(u,v), the projection of (16) is into

A_{J,6}=L₆/(uL₄+vL₃)
  =U⊗[M₃/(uM₁+vM₀)].

The second stage is

{[n]∈(N/vN)₄:u[n]=0}
  →Lbar₆/uLbar₄=L₆/(uL₄+C_{v,6}),               (17)

and its cokernel is the primary part of Q₅=(K/(u,v)K)₆.

For J'=(u²,v), the same first stage (16) is instead projected into

A_{J',6}=L₆/(u²L₂+vL₃)=L₆/vL₃,

because L₂=U⊗M_{−1}=0. The second stage is

{[n]∈(N/vN)₂:u²[n]=0}
  →Lbar₆/u²Lbar₂=L₆/C_{v,6}.                    (18)

Its cokernel is the primary part of (K/(u²,v)K)₆. The first-stage unprojected map is shared, but its ordinary-pair projection can lose directions to uL₄; the second-stage domains and actions in (17) and (18) are different. No replacement of u² by u is justified.

Equations (16)–(18) give a staged plan for an actual calculation: establish the v-annihilator boundary; form the corrected primary v-quotient; then compute the appropriate u or u² annihilator on N/vN and its lift boundary. Independently determine the residual quotient. This complements a square-versus-linear annihilator comparison but does not evaluate it.

## 7. Dependencies and boundary

The algebraic theorem uses only the exact graded extension (1) and multiplication by u,v. It does not require S-regularity, a splitting, an HM cohomology table, or a selected matrix calculation. Reversing the order of u and v gives another two-stage filtration of the same total correction, with potentially different intermediate images.

The actual HM use depends on the extension identified in PR477. That premise is not established anew here. PR477 §4 supplies the total correction, explicit regular-pair lift, and separate squared quotient; it does not supply the two-stage filtration (12), its successive quotient construction, or projected-rank bookkeeping (14). Those are the new synthesis here.

Pinned predecessor:
https://github.com/Akilleez-QA/read-em-and-weep/blob/ff87076794e97238150485b12183c3cd0f4711e4/research/hm/adjoint-primary-extension/PROOF.md

This primary-extension Tor is not the coordinate-ring Tor₁(S/I,S/J) used for polynomial intersection ambiguities. The modules and correction mechanisms are different. Actual fixed-pair values, source membership, higher-order lifting, and algebraicity remain open. Authored mathematical reasoning for independent checking, not formal verification.

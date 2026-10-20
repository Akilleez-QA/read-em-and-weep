> Current actual-bundle specialization: the degree-one-kernel exclusion rules out a=1. The a=1 formulas below are historical conditional algebraic derivations, not current actual alternatives.

# Exact full rank in the actual d=6 branch

## Result

Retain the actual plane inclusion and double-conic notation of `PROOF.md`. If d=6, then a=0 and δ=length(Z∩C)=1. Put

    τ=2−length(Z∩2C) ∈ {0,1}.

The full ribbon boundary, including its diagonal-deformation row, has exact rank

    rank ε=τ+1.

Thus it has rank one when the coordinate ideal on 2C is principal, and rank two when it is not. A reduced point of Z on C is in the latter case. This refines the previously proved interval; it does not evaluate which case occurs for the actual zero scheme.

## 1. The reference upper line has no sections

For d=6 the determinant-correct reference from the ribbon classification is A₀⊕Q₀, where

    A₀|C=O_C(1),
    A₀²≅O_D(1 plane),
    Q₀|C=O_C(−5).

We claim H⁰(D,A₀)=0. Its nilpotent layer is O_C(−3), which has no sections, so any nonzero section u of A₀ would have nonzero reduction in H⁰(O_C(1)). That reduction vanishes at a point p of C.

The square u² is nonzero because its reduction is nonzero. It is a section of O_D(1 plane). The plane divisor sequence

    0→O_P²(−3)→O_P²(1)→O_D(1 plane)→0

and H⁰(O_P²(−3))=H¹(O_P²(−3))=0 identify this section with a nonzero plane linear form l.

At p, a local coefficient of u belongs to the maximal ideal m_{D,p}, so a local coefficient of u² belongs to m_{D,p}². Multiplication by the unit from the line-bundle square identification does not change that fact. But a nonzero plane linear form vanishing at p lies in m_{P²,p} minus m_{P²,p}². Its image still lies outside m_{D,p}², because q² belongs to m_{P²,p}². This is a contradiction. Therefore H⁰(D,A₀)=0.

In particular the restriction connecting map

    ∂₀:H⁰(O_C(1))→H¹(O_C(−3))

is injective, so ∂₀(σ)≠0 for the nonzero reduced K section σ, whose divisor is R=p.

## 2. The actual section constrains the diagonal deformation

Use the framed, determinant-fixed deformation coordinates (h,e) relative to A₀⊕Q₀ from the preceding classification. The upper-right cohomology is H¹(O_C(d−4))=H¹(O_C(2))=0, so a reduction-trivial gauge makes the upper-right cocycle identically zero. The remaining transitions are lower triangular. Their first coordinates define a quotient line A_h whose deformation from A₀ is h∈H¹(O_C(−4)).

The actual section K_D=O_D→E_D projects to a section of A_h reducing to σ. Therefore its obstruction vanishes:

    ∂₀(σ) ± h cup σ = 0.

The sign depends only on the chosen consistent Čech convention and is irrelevant here. Since ∂₀(σ)≠0, we obtain

    h cup σ ≠ 0.                                      (1)

This conclusion does not require the lower deformation e to vanish. Its terms cannot alter the upper-coordinate equation once the upper-right cocycle has been killed.

## 3. Independence from the Cartan row

Serre duality identifies h with a functional on H⁰(O_C(2)). Multiplication by σ gives

    h cup σ ∈ H¹(O_C(−3))=H⁰(O_C(1))*.

Its vanishing would mean that h annihilates the two-dimensional subspace σ H⁰(O_C(1)) of quadratics vanishing at p. The annihilator of that subspace is precisely the one-dimensional evaluation line at p. Thus (1) says that h does not belong to this evaluation line, and in particular h≠0.

The supported-obstruction result places e on R=p. If τ=0 then e=0, so its Cartan row space is zero; the nonzero h row gives rank ε=1. If τ=1 then e is a nonzero multiple of evaluation at p on degree-eight forms. Its degree-(2,6) catalecticant has rank one and row space the evaluation line at p on quadratics. The h row is outside that line by (1), giving rank ε=2.

In the boundary formula the diagonal row is a nonzero scalar multiple of h, so these statements yield rank ε=τ+1 exactly.

## Scope

The argument uses the actual plane ribbon D=2C, the actual K section, and the determinant-correct reference root. It does not hold for an arbitrary abstract split ribbon with an unrelated lifted line bundle, and it does not contradict the earlier rank classification of all unconstrained ribbon-local models. No actual diagonal class, HM matrix, ambient map, or source has been evaluated.

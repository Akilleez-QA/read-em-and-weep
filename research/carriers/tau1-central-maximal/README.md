# Balanced τ=1 central criterion and maximal-direction exclusion

This package proves two results in one explicitly prescribed filtered symplectic model on P¹×P³:

1. An exact central gluing/isotropy criterion with h⁰(N)=1 and h¹(N)=27, retaining the quadratic symplectic correction and the doubled ideal (a,h²).
2. Nonexistence of an everywhere-surjective last map when the exceptional direction lies in the maximal O(2) subbundle of U=O(2)⊕O(1)², for every actual primitive ambient presentation of U.

The normal-form reduction from arbitrary charge-three families is **an input, not a theorem of this package**. The hypotheses below specify the model completely, so neither result depends on an unpublished normal-form proof. The notation “τ=1, c=0” labels this model; in particular c=0 means that the symplectic coefficient bundle W is constant.

## Exact hypotheses

Work over an algebraically closed field of characteristic zero. Let X=P¹×P³, let p:X→P¹, and write O(b,d) for the two-factor line bundle.

- E=O(-6,1)⊕O(-2,1), T=O(-2,2)⊕O(-1,1), and W=O² with J=[[0,1],[-1,0]].
- The fixed positive block is L=[[ell,h],[0,a]]:E→T. Its sections have bidegrees ell:(4,1), h:(0,1), a:(1,0).
- The section a has one simple zero p₀. The coefficients of ell have no common base zero, so Y={ell=0} is a P²-bundle. The ambient linear forms ell₀ and h are independent; Λ={a=ell=h=0} is a line in the exceptional plane Y₀.
- The **actual** ambient sequence on P¹ is exact:

      0 → O(-4) → O⁴ → U → 0,
      U=p_*O_Y(0,1) ≅ O(2)⊕O(1)².

  The projective-bundle convention is p_*O_Y(0,1)=U. An arbitrary extension with another middle bundle does not satisfy these hypotheses.
- The filtered symplectic middle is locally E⊕W⊕E* on the two standard affine-base charts. After transporting the fixed diagonal line-bundle frames, its prospective transition has the form

      g(V,S)=[[I,VᵀJ,S+½VᵀJV],[0,I,V],[0,0,I]],  S=Sᵀ.

  Its symplectic form is Ω=[[0,0,I],[0,J,0],[-I,0,0]]. No global splitting of the middle is assumed.
- The first-stage data are any regular local Q_i:W→T and overlap V obeying Q_j=Q_i+LVᵀJ. They represent an ordered pair of global sections of K=coker L, with all vertical torsion parameters retained. On Y their intrinsic quadrics are q=aQ_C−hQ_D in H⁰(Y,I_Λ O_Y(-1,2)).

The central problem is to choose regular R_i:E*→T and symmetric S so that β_i=[L,Q_i,R_i] glue by g(V,S) and satisfy β_iΩ⁻¹β_iᵀ=0. Pointwise rank two of β is an additional condition, not part of gluing or isotropy.

## Results and proof dependencies

[central-criterion.md](central-criterion.md) proves local solvability exactly when det(Q_i) vanishes scheme-theoretically on Λ, then proves that the corrected Čech class

    [R_j−R_i−Q_iV−½LVᵀJV] in H¹(N)

vanishes exactly when central gluing is possible. Here N=ker(R↦aR₁₂−ell R₂₁−hR₂₂)/(L Sym²E), with exact presentation

    0 → O(-12,2)⊕O(-8,1)
      --[[ell,h²],[0,a]]-->
      O(-8,3)⊕O(-7,1) → N → 0.

The primary restriction has a four-dimensional target, not a claim of four independent equations. The quotient is the ideal of a doubled exceptional line plus vertical torsion. Replacing (a,h²) by (a,h) changes h¹ from 27 to 24 and is invalid. The note also proves lift invariance, the global regular residue on V_Y(q₁,q₂), and the separate ordinary/exceptional rank gates.

[maximal-direction.md](maximal-direction.md) additionally assumes 0≠h₀∈O(2)₀. The canonical quotient subscroll Σ=P(U/O(2)) is independent of a chosen complement. The connecting isomorphism H⁰(U(-1))→H¹(O(-5)) forces the binary Wronskian to vanish through four projected Laurent coefficients, including exponent zero. A common minimal section then has residue degree −4, forcing ordinary rank failure.

The first proof is the only mathematical dependency of the second within this package. Neither proof uses a fixed-presentation obstruction tensor or a genericity assumption.

## Reproduce the exact checks

Tested with Python 3.12.14 and SymPy 1.14.0. From this directory, using a Python environment with the pinned dependency:

```sh
python -m pip install -r requirements.txt
python run_checks.py
```

The runner executes both self-contained checkers with assertions enabled and compares their output to [verification.txt](verification.txt). The checkers use exact symbolic/rational arithmetic and no network, generated input tensors, or external repository files.

- verify_central.py: symplectic identities, gauge invariance, quotient/torsion relations, residue gluing, localized rank-minor ideal, two exact 164×138 Čech matrices of rank 137, and doubled-line cohomology.
- verify_maximal.py: full corrected projected overlap, ambient-lift and torsion terms, regular isotropy solution, all 13 intrinsic monomials, connecting columns, the precise Laurent window, and the binary coefficient-minor identity.

The universal geometric arguments are in the proof notes. Passing finite symbolic checks alone does not establish those global arguments.

## Separate remaining scope

The direction 0≠h₀ mapping nontrivially to U₀/O(2)₀ is **not excluded here**. In that stratum full central compatibility, ordinary rank, and exceptional-fiber rank are separate conditions. No complete τ=1 closure, globally locally free monad, carrier, stability result, or mixed-Atiyah vanishing is asserted. Broader closure and other splitting types belong to separate results.

This focused package is part of the [carrier proof tracker](https://github.com/Akilleez-QA/read-em-and-weep/issues/52).

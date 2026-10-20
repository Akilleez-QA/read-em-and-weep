# Universal exterior-algebra trace-density candidate

## Result and scope

The proposed identities are correct with the stated minus sign in Π. Over the abstract exterior algebra on eight invented degree-one generators, for every scalar k and an invertible formal parameter h, the classes

    d = k θ²,     c = ω/h + k h Π

satisfy both neutral whole-support trace-density necessary conditions

    c d − c³/3 = 0,
    d²/12 − c² d/2 + c⁴/12 = 0.

This is an exact universal algebra statement. It does not identify c with the actual algebroid period, establish the missing twisted characteristic-class comparison, prove that the specified bundle quantizes, or evaluate or prove vanishing of any of the thirty retained obstruction coordinates. No actual source, physical model, finite jet, matrices, or repository was evaluated. Only the two supplied mathematical reports were read.

## Definitions and signs

Use the ordered basis a₁,a₂,a₃,a₄,b₁,b₂,b₃,b₄, with all products exterior products. Set

    θ = Σᵢ aᵢ bᵢ,
    ω = a₁ a₂ + a₃ a₄,
    Π = −b₁ b₂ − b₃ b₄.

Let eᵢ be dual to aᵢ (and annihilate all bⱼ), define π=e₁∧e₂+e₃∧e₄, and fix contraction by

    ι_(u∧v) = ι_v ι_u.

Then Π=(1/2)ι_π(θ²). Indeed θ² contains −2 a₁a₂b₁b₂ and −2 a₃a₄b₃b₄, while all other terms are killed by the corresponding full paired contraction. This explicit contraction convention removes any ambiguity about the word “dual.” No inverse-symplectic or opposite-algebra convention is silently inferred from it. Matching this abstract choice to the symplectic inverse-sign convention of the actual paper or algebroid remains part of the missing period comparison.

Replacing Π by its negative while retaining the displayed definitions of θ,ω,c would not preserve the cancellation. If a geometric application uses the opposite bivector/contraction convention, the geometric identification must account for that change.

## Proof of the exterior identities

Write

    x=a₁a₂,  y=a₃a₄,  u=−b₁b₂,  v=−b₃b₄,
    t=a₁b₁+a₂b₂,  s=a₃b₃+a₄b₄.

Thus ω=x+y, Π=u+v, and θ=t+s. All these forms have even degree and commute. Direct reordering gives

    t²=2xu,  s²=2yv,
    x²=y²=u²=v²=0,
    xt=ut=ys=vs=0.

Consequently

    ω θ² = (x+y)(2xu+2ts+2yv)
          = 2xy(u+v) = ω² Π,
    Π θ² = (u+v)(2xu+2ts+2yv)
          = 2uv(x+y) = ω Π².

Each of t and s is supported on four independent generators, so t³=s³=0. Hence

    θ⁴ = 6 t²s² = 24xyuv = 6ω²Π².

Also ω³=Π³=0, since each is supported on only four degree-one generators.

## Degree-six cancellation

The identities above imply

    c d = (k/h) ω θ² + k²h Π θ²
        = (k/h) ω²Π + k²h ωΠ².

On expanding c³ and using ω³=Π³=0,

    c³/3 = (k/h) ω²Π + k²h ωΠ².

Thus c d−c³/3=0 for arbitrary k.

## Degree-eight cancellation

Let V=ω²Π². Multiplying the degree-six identities by ω or Π gives

    ω²θ²=0,  Π²θ²=0,  ωΠθ²=V.

Therefore

    d²/12 = (k²/12)θ⁴ = (k²/2)V,
    c²d/2 = (k/(2h²))ω²θ² + k²ωΠθ²
             + (k³h²/2)Π²θ² = k²V,
    c⁴/12 = (6k²/12)ω²Π² = (k²/2)V.

Their signed sum vanishes.

## Relation to the supplied necessary tests

The first supplied report derives, in its neutral global-algebra setting on an abelian fourfold, the degree-six/eight constraints on exp(−c)(2−d+d²/12). The calculation above proves that the displayed formal pair (c,d) satisfies those algebraic constraints. Independently expanding that exponential in the script confirms its degree-six and degree-eight components vanish.

The second supplied report explains why an actual twisted application still needs a total Čech–de Rham period/trace comparison with all central-extension, opposite-algebra, and symbol-bundle conventions checked. This calculation supplies no such comparison. In particular, an isolated gerbe coefficient is not thereby identified with k h Π. Passing these necessary characteristic tests is not sufficient for all-order module existence, and does not imply detection or vanishing of the retained sector. The candidate is a formal witness to compatibility of these equations, not an actual period or a proof that this candidate is geometrically realized. If one additionally writes an abstract gerbe symbol b=−kΠ in these conventions, the candidate’s coefficient of h is algebraically −b. This is only a rewriting of the candidate and is explicitly not an asserted gerbe-to-period conversion.

If a separately justified cohomological normalization gives c₂(E)=15θ² and identifies the relevant degree-one classes and products with this formal algebra, one may conditionally specialize k=15. That specialization adds no geometric period identification or quantization theorem, and no such normalization or actual model was evaluated here.

## Reproducibility

`test.py` implements exterior multiplication with explicit inversion-count signs, standard contractions, and exact SymPy rational/Laurent-polynomial coefficients. It contains only the eight invented generators, k, and h; it reads no data files. Run:

    python research/hm/null-order-three-ambient/historical-exploration/trace-density-candidate/test.py

The original report states that all ten checks passed. No separate saved output was included in the source packet, and this script was not rerun for publication. The proof above is independent of the script.

Inputs: [RESULT.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/d1422e5f9137ae64ec207c496a0391712ce93263/research/hm/null-module-boundary-audits/quantization-criteria/RESULT.md) and [RESULT.md](../twisted-period/RESULT.md).

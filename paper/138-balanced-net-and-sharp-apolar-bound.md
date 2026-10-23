# 138. Balanced sextic syzygies and a sharp apolar codimension bound

**Checkpoint: 23 October 2026 · Universal structural refinements after the PR1145 shape exclusion**

## Contribution and unchanged frontier

The equivariant sextic net used in the preceding actual exclusion has a stronger structure than the general basepoint-free argument required there. Its syzygies are balanced, quadratic multipliers already fill the entire degree-eight space, and its ideal has an exact finite quotient of length 27. These facts yield a uniform, sharp apolar codimension obstruction with explicit abstract equality models.

Neither result is counted as another actual shape exclusion. The residual rank-16 configuration in constant dimension 21 was already excluded by PR1145. Applying the new criterion elsewhere still requires proof of its actual osculating-containment and source hypotheses. Profile (1,1), separate other-profile exhaustion, and the original proof repair remain open.

## Balanced syzygies of the marked sextic net

[PR1147, immutable proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/176645bb2f022b68f86414ced87667a45e4930e2/research/hm/balanced-sextic-syzygies/PROOF.md) concerns the unique nonstandard three-dimensional V in Sym6 W for G=SL2(F5). Its sextic evaluation has no base points: a common-zero divisor of degree at most six cannot be invariant when every projective orbit has at least twelve points. Thus its kernel T_V has rank two, degree −6 and no sections.

The ordinary kernel possibilities are O(-1)+O(-5), O(-2)+O(-4), and O(-3)². In an unequal splitting the top line is canonical and equivariant. Perfectness removes character twists, while the central action excludes degree −1. The degree-minus-two possibility would contribute a trivial representation to V⊗Sym2 W=P+D, which has none. Hence the kernel is balanced. Twisting by three and taking sections identifies its coefficient doublet as W′:

    0 → W′ O(-3) → V O → O(6) → 0.

This is an exact nonsplit evaluation sequence, not a choice of actual HM coefficients.

## Sharp multiplier threshold and exact finite quotient

For multiplication mu_d:V⊗Sym^d W→Sym^(d+6) W:

- d=0 is the inclusion V→V+P, with cokernel P.
- d=1 is injective, with cokernel W′.
- d=2 is an isomorphism onto Sym8 W.
- d≥3 is onto, with kernel W′⊗Sym^(d−3) W.

Consequently the constant span of l^d V is the full degree-(d+6) space for every d≥2. The minimal multiplier degree is two, improving the quartic sufficiency used in PR1145 without changing its already-established exclusion.

For R=Sym(W), the ideal I=(V) has the minimal equivariant resolution

    0 → W′⊗R(-9) → V⊗R(-6) → R → R/I → 0.

The quotient Hilbert vector is (1,2,3,4,5,6,4,2), with total length 27. Its pieces are Sym^n W for 0≤n≤5, P in degree six, W′ in degree seven, and zero from degree eight onwards. This is a universal polynomial quotient, not a computed obstruction space for the original problem.

## A uniform apolar obstruction

[PR1148, immutable sharp apolar codimension theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/cc0b79801a3e9080d1a4f1d380cfa64db776dba9/research/hm/apolar-codimension-obstruction/PROOF.md) fixes d≥2 and n=d+6. Let F be an equivariant saturated negative bundle in a constant M-dimensional ambient H O, and suppose its dual quotient S=(H O/F)* has no constant sections. Assume an actual saturated line O(-n) lies in S and its constant-connection osculating directions through order d−1 lie generically in S. Finally suppose the equivariant bundle type is

    F=F_high ⊕ V O(-d),

where every ordinary degree of F_high is strictly greater than −d. This decomposition is not assumed horizontal.

The theorem proves that the line's coefficient map Sym^n W→H* is injective and

    codim(F,H O) ≥ n−2.

If F_high is nonzero, saturation and negativity strengthen this to

    codim(F,H O) ≥ n−1.

The osculating hypothesis is essential input, not something inferred from these degrees.

## Why a partial system becomes complete

Initially allow an arbitrary coefficient quotient Sym^n W→R. Its dual injection R*→(Sym^n W)* pulls actual annihilation back to the full universal osculating fibers l⁷Sym^(d−1) W. Their apolar annihilator is l^d Sym6 W, giving a factorization of F into Sym6 W O(-d).

All higher-degree source blocks map to zero by degree. The remaining V channel is scalar and nonzero: otherwise R would be a forbidden constant subspace of S. Thus R* contains every l^d V. The balanced-net theorem proves that these span all Sym^n W, forcing completeness.

The high block then lies in the constant projection kernel of dimension M−(n+1). Its rank gives the first codimension bound. Because F_high is saturated in that kernel, equal ranks would make it a constant bundle. Its strictly negative degrees rule this out whenever it is nonzero, giving the stronger integer bound. No arbitrary Birkhoff summand is declared horizontal.

## Sharpness and application boundary

Both bounds are sharp under the stated abstract hypotheses. The universal inclusion V O(-d)→Sym^(d+6) W O, with fiber l^d V, has codimension n−2. Adding the saturated high block W O(-1)→Sym2 W O gives codimension n−1. Both models span their constant ambients and contain the required complete polynomial line and osculating directions in the dual annihilator. They are not asserted to be HM realizations. When the ambient center acts trivially, n must be even; the even-n models respect that restriction.

The already-excluded PR1145 residual has n=10, codimension 21−16=5 and a nonzero high block. It violates both the weak bound eight and the sharp strengthened bound nine. This is a new general criterion with sharp boundary models, not a second count of that same exclusion.

## Verification and edition boundary

The full source proofs and independent reviews were read. PR1147 reproduces 508 production controls and 958 independent exact character controls in normal and optimized Python. The sharp apolar theorem reproduces 11,736 formal controls and 28,355 independent controls, including full formal apolar pairings and two-chart checks. Its independently reviewed proof has SHA256 18ad6a68fdc672e505d2c9e607152dbe7e6a6d42c20898acbafbd807aaf78fd5.

The bundle arguments prove the unbounded statements; finite controls support them and are not proof-assistant certification. No actual-source parameters, coefficients, points, jets or instance ranks are evaluated. Chapter 137 remains its frozen checkpoint. The Craig Ward v0.3 PDF remains unchanged at 23 October 2026, 19:16 UTC through PR1117.

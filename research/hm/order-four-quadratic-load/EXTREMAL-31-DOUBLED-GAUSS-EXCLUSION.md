# Exclusion of the nine doubled-Wprime cases in the last rank-two quotient

## Result and boundary

All nine a=2 candidates in EXTREMAL-31-LAST-REMAINING-QUOTIENT-REDUCTION.md are impossible. Exactly the eleven a=1 necessary candidates from that reduction remain. This does not exclude the full (8,2) quotient, does not settle the rank-one dual-image branch, and does not change SF>=3 or positive-square rank>=27.

Write P=P4, T=T6, S=S4, D=D5 and Wp=Wprime. A coefficient representation times O(-j) is written C(-j). All maps and Hom spaces are equivariant. The reduction gives four actual possibilities:

    Qalpha=(V+P)(-4)+Wp(-5)+L,
    Qbeta=T(-3)+Wp(-5)+L+O(-10),
    L=O(-8)+O(-10) or W(-9).

Each has rank 11 and degree -56. The actual next derivative has generic rank three and target O(2)+Wp(-5). Its kernel F0 is E^{---}, so persistence gives H0(F0(3))=0. No splitting is assumed horizontal.

## 1. The actual saturated-kernel rule

We use Section 1 of EXTREMAL-31-FIRST-REMAINING-QUOTIENT-EXCLUSION.md, including its verified constant ambient realization. If G is saturated in H tensor O and F=ker(beta_G), then F is saturated in that same ambient bundle, and

    beta_F: F -> (G/F)(-2).

The image sheaf G/F is locally free, even when it is not saturated in the displayed derivative target. In particular a nonzero map supported on a single source line M has actual quotient M, regardless of its zeros. The ensuing target is M(-2), not the twist of the saturated image.

Every nonzero negative-degree kernel below has nonzero actual derivative: a zero derivative would give a constant Grassmann classifying map in characteristic zero and hence a trivial, degree-zero subbundle. We impose no rank-three condition after F0. Exact character, rank, degree and Hom checks are in the companion verifier; all encountered sources have positive rank and negative degree.

In both Q shapes, only Wp(-5) reaches the low target Wp(-5), and its Hom space is scalar. Rank three forces that map to be an isomorphism. A triangular target automorphism removes its high graph; the remaining high map is from the complementary source to O(2). This is an actual-kernel calculation, not a change of the ambient connection.

## 2. A common terminal calculation

Two scalar chains below end with a source mapping to O(-8) of one of these forms:

    W(-9)+O(-8)+O(-10),
    2W(-9),
    2O(-8)+2O(-10),
    O(-8)+W(-9)+O(-10).

Only O(-8) constant components and W(-9) complete linear evaluations can act. All maps from O(-10) vanish. If a constant component is nonzero, it splits off O(-8); all other components lift through that identity. If only W(-9) acts, multiplicity-space changes leave one nonzero complete linear evaluation, whose kernel is O(-10). Thus every nonzero map has kernel either

    W(-9)+O(-10), or O(-8)+2O(-10).

The next target is O(-10). Only the O(-10) constant components act. Nonvanishing removes exactly one such line, leaving respectively W(-9) or O(-8)+O(-10). Both have zero Hom to their next target O(-12), a contradiction. A zero derivative at any earlier step is already impossible by Section 1.

## 3. Qalpha: complete treatment of the high map

After low elimination the high source is (V+P)(-4)+L. The V and P components to O(2) are unique sextic evaluations. For split L, only O(-10) has a high map, of degree twelve; for L=W(-9), its high map is the unique degree-eleven W pair. Every nonzero irreducible degree-six, degree-seven or degree-eleven polynomial series used here is basepoint-free: a nonempty common-zero divisor would be invariant of degree at most eleven, whereas the smallest nonempty icosahedral invariant divisor has degree twelve.

When at least one sextic component is nonzero, its evaluation is surjective. The established sextic kernels are Wp(-7) for V(-4), V(-6) for P(-4), and T(-5) when both are nonzero, since Sym^6 W=V+P. Every L high map lifts through these evaluations: the obstruction line degrees j-k for L=C(-j) and a kernel coefficient at degree -k, k in {5,6,7}, are at least one. Averaging gives equivariant lifts. Subtracting them computes the actual kernels described below.

### Neither sextic acts

If L=O(-8)+O(-10), rank three forces the O(-10) high map nonzero. Even though that degree-twelve scalar has zeros, the actual kernel and quotient are

    F0=(V+P)(-4)+O(-8),
    Qalpha/F0=Wp(-5)+O(-10).

There is zero Hom from F0 to its next target Wp(-7)+O(-12), impossible.

If L=W(-9), the nonzero degree-eleven pair is basepoint-free with kernel O(-20), by determinant. Hence

    F0=(V+P)(-4)+O(-20),
    Qalpha/F0=O(2)+Wp(-5).

Its next target O+Wp(-7) can receive maps only from O(-20). Both components are allowed. Nonvanishing gives actual quotient O(-20), leaving (V+P)(-4), which has zero Hom to O(-22). This also is impossible.

### Both sextics act

Here F0=T(-5)+L, and Qalpha/F0=O(2)+Wp(-5). Its derivative target is O+Wp(-7); the low component vanishes identically. The successive forced complete evaluations are

    T(-5)+L -> O,
    D(-6)+L -> O(-2),
    S(-7)+L -> O(-4),
    A(-8)+L -> O(-6),
    W(-9)+L -> O(-8).

Before the last arrow only the first displayed block acts, with one-dimensional Hom. Each kernel is exactly the next displayed source. The last arrow is covered by Section 2.

### Only P acts

Here F0=V(-6)+V(-4)+L, with the same quotient O(2)+Wp(-5). Its next target O+Wp(-7) has support only on the V(-6) high component. The sextic kernel gives

    Wp(-9)+V(-4)+L -> O(-2).

Only the Wp(-9) septic pair acts; its kernel is O(-16). The next source and target are

    O(-16)+V(-4)+L -> O(-4).

Only the line O(-16) can act. Its actual image quotient is O(-16), including zeros of the degree-twelve map. The remaining V(-4)+L has zero Hom to the next target O(-18).

### Only V acts

Here F0=Wp(-7)+P(-4)+L, again with quotient O(2)+Wp(-5). In the target O+Wp(-7), only Wp(-7) acts. If its low scalar is nonzero, the actual quotient is Wp(-7), independent of its high graph; the kernel P(-4)+L has zero Hom to Wp(-9). In particular W and Wp are distinct, so L=W(-9) creates no exception.

If the low scalar is zero, the high septic pair must be nonzero and basepoint-free. Its kernel gives

    O(-14)+P(-4)+L -> O(-2).

Only O(-14) acts. Its actual quotient is O(-14), and the remaining P(-4)+L has zero Hom to the next target O(-16). This finishes Qalpha.

## 4. Qbeta

After low elimination, the high T(-3) component must be nonzero. Otherwise the entire T(-3) block survives in F0, contrary to H0(F0(3))=0. This component is complete quintic evaluation onto O(2), with kernel D(-4). All deeper components lift through it: for C(-j) in L+O(-10), the obstruction line degree j-4 is nonnegative. Therefore

    F0=D(-4)+L+O(-10),
    Qbeta/F0=O(2)+Wp(-5).

The next target O+Wp(-7) has no low component. The forced scalar chain is

    D(-4)+L+O(-10) -> O,
    S(-5)+L+O(-10) -> O(-2),
    A(-6)+L+O(-10) -> O(-4),
    W(-7)+L+O(-10) -> O(-6),
    O(-8)+L+O(-10) -> O(-8).

Only the leading block acts before the final arrow, through complete evaluation, and each kernel is the next source. The final arrow is exactly Section 2. This excludes Qbeta and therefore all four actual Q shapes from the nine a=2 candidates.

## Verification

Run python3 verify_extremal_31_doubled_gauss_exclusion.py. It imports the established exact representation ring and checks every displayed Hom support, actual-quotient Euler identity, rank and negative degree, evaluation identity, and lift range. It includes both possible terminal kernels, both low-map outcomes in the V-only branch, and both components of the O(-20) derivative. The invariant-divisor, ambient-saturation and actual-image arguments are geometric inputs proved above, not consequences inferred from character arithmetic.

Only this new proof and its new verifier were written. No actual coefficients, points, matrices, rank experiments or scans were used; no existing or frozen file was edited. The eleven a=1 cases, the rank-one branch, and the global bounds remain as stated in the result.

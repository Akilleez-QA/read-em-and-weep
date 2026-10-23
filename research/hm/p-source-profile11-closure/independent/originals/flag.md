# Two scalar-ended rank-three targets are excluded by their complete Gauss flags

## Statement and scope

Over C on the physical binary-icosahedral parameter line, let E be the actual saturated primary bundle in the constant thirty-space, K=E^- its actual Gauss kernel, and A=E/K. Assume the maximal rank-three plateau has lower length k=1. Then neither actual quotient shape

    A=W' O(-3)+O(16),    A=W' O(-5)+O(16)

is possible. This conclusion holds for every one of the four actual primary source types supplied by PR1123, independently of the upper quotient and historical row labels. It therefore applies to profile (1,1), but does not exclude that entire profile or complete the original proof repair.

The new argument is a complete rank-one Gauss flag, its invariant ramification divisors, and equivariant Euler additivity. The seven formal degree patterns below are forced necessary possibilities, not selected actual coefficients or realized examples. Their ordinary ranks, degrees and Euler dimensions agree; their representation-valued Euler characteristics do not.

## 1. Pinned reduction to a scalar rank-one endpoint

INPUTS.json authenticates complete public originals for the actual Gauss inclusion and strict-top lemma, the four-source theorem PR1123, cubic alternatives PR1140, D-image criterion PR1142, and P-image theorem PR1153. We also retain the separate frozen PR1158 proof at bfbb3fe3dd0659e69b6b818ec86038a62ebd2675, public path research/hm/forced-scalar-endpoints/PROOF.md, as FROZEN-SCALAR-ENDPOINT-LEMMA.md, SHA256 d76c66aac6cf179ae06a03d311edffe819834db6aa6dee1f39d59cd76ed7d2af. Its argument is an explicit mathematical prerequisite, not a numerical conclusion inferred from a checker. It is reproduced in full so this packet does not require readers to trust an unavailable abbreviated statement. That frozen theorem only forces a rank-one endpoint; it does not claim either target is excluded. The additional argument here must not be backdated into it.

Here and below A_std=Sym2 W denotes the standard three-dimensional representation, whereas A denotes the quotient bundle. The four source types are

    D: D O(-2)+(W'+T)O(-3)+V O(-4)+O(-8),
    P: P O(-2)+(W'+T)O(-3)+V O(-4)+W'O(-5),
    V: V O(-2)+(W'+T)O(-3)+2V O(-4),
    Z: (W'+2T)O(-3)+V O(-4).

They all have chi_G(E(4))=3V+3P+2D. Cubic-kernel vanishing would imply that

    H0(A(2))+chi_G(A(4))-(3V+3P+2D)

is genuine: strict-top then gives maxdeg K<=-4 and H0(K^-(4))=0, so H0(K(4)) injects into H0(A(2)). The displayed character is

    r=3: 1+2A_std+D+P-V,
    r=5: 1+2A_std+D-V,

for A=W'O(-r)+O16. Its V coefficient -1 makes cubic vanishing impossible. PR1140 therefore removes source types V and Z. In source D, PR1142 says a nonzero cubic kernel forces a nonzero sheaf injection O2 into A. The negative doublet admits no map from O2, and the scalar component would require an invariant in Sym14 W. But

    Sym14 W=A_std+V+P+D,

so Hom_G(O2,A)=0. This removes D. Only the P source remains, with H0(K(3))=W'.

For this P source the retained scalar-endpoint lemma proves, using actual endpoint rank at most two at k=1,

    rank K=14, deg K=-70+2r, maxdeg K<=-3,
    image(beta_K)=O14 exactly inside A(-2).

For clarity, its essential actual-map content is as follows. The canonical cubic top C=W'O(-3) maps nontrivially to the scalar O14 and has zero doublet component by degree. A common invariant divisor has degree at most10, because W' first occurs in Sym7 W, but every nonempty invariant divisor has degree at least12. Thus C surjects onto O14. If beta_K had rank two, its remaining coherent line image O(e) in W'O(-r-2) satisfies e>=-20+2r and e<=-r-9. These contradict for r5. For r3 only e=-12 survives parity and Sym9 W, but its fourth-twist strict-top envelope is 1+2A_std+3D+P-V, impossible. Consequently the coherent image is exactly O14. All these bounds concern coherent images and saturated kernels, not a horizontal Birkhoff splitting.

## 2. The entire backward flag consists of fourteen line quotients

Put F0=K and define F(j+1)=ker beta_(Fj) as actual saturated kernels in the same constant ambient. Because differentiation of F(j-1) kills Fj, the derivative of Fj lands in

    (F(j-1)/Fj)(-2).

The first quotient Q0=F0/F1 is exactly O14. Inductively, if Q(j-1) is a line, beta_(Fj) has rank at most one. It cannot vanish while Fj is nonzero: a horizontal saturated subbundle of a constant bundle over C is constant, whereas every degree of Fj is negative. Negativity follows already from Fj subset K, and strict-top gives the sharper bound maxdeg Fj<=-3-j. Thus its rank is exactly one, Qj=Fj/F(j+1) is a line, and rank drops by one at each step. Starting with rank14 gives precisely

    F0 superset F1 superset ... superset F14=0,
    rank Fj=14-j, Qj=O(bj), j=0,...,13.

Every kernel is saturated in its source and in the constant ambient: the derivative image is torsion-free on the smooth curve, and extensions of the resulting locally free quotients remain locally free. No unsaturated kernel or finite-length endpoint is omitted. Quotients Qj are the actual locally free coherent-image quotients, not saturations of their images in the preceding target.

All these bundles and maps are equivariant. The binary icosahedral group is perfect, so any equivariant line bundle of degree b has the standard O(b) linearization, without an extra one-dimensional character. For j=0,...,12 the induced nonzero sheaf injection is therefore

    Q(j+1) -> Qj(-2).

Its vanishing divisor Dj is invariant and effective. Writing delta_j=deg Dj gives

    b0=14,   b(j+1)=bj-2-delta_j.

This recurrence includes the terminal quotient Q13; its injection into Q12(-2) is not discarded.

## 3. Orbit sizes and the exact weighted defect equation

The action on the parameter line factors through the projective icosahedral group A5. A point stabilizer in a finite subgroup of PGL2(C) is cyclic: conjugating the fixed point to infinity and averaging an affine orbit conjugates the finite stabilizer into the multiplicative group. Cyclic subgroups of A5 have orders 1,2,3,5. Thus every orbit has size 60,30,20,12. Every invariant effective divisor, including multiplicities, is a nonnegative integer sum of these orbit degrees. In particular each delta_j lies in the semigroup generated by12,20,30 (60 is redundant). We only use this necessary condition; uniqueness or geometric independence of exceptional orbits is not presumed.

Degree additivity in the full flag gives

    sum_(j=0)^13 bj=deg K=-70+2r.

The undeflected sequence 14,12,...,-12 has sum14. Substituting the recurrence consequently gives

    sum_(j=0)^12 (13-j) delta_j=84-2r.

The right side is78 for r3 and74 for r5. Count weighted orbit atoms as 12a+20b+30c; 60-atoms can be replaced by five12-atoms without changing this necessary equality. Reduction modulo4 forces c odd; since the total is below90, c=1. Thus the sole30-atom has weight one, at j12.

For total78, the remainder48 satisfies 3a+5b=12, giving a=4,b=0. The partitions of4 into positive weights produce exactly five necessary divisor-degree patterns. For total74, the remainder44 satisfies 3a+5b=11, giving a=2,b=1. The sole20-atom has weight one, and the partitions of2 give exactly two necessary patterns. Unlisted delta_j are zero:

    r3: {delta9=12, delta12=30};
        {delta10=12, delta12=42};
        {delta11=24, delta12=30};
        {delta11=12, delta12=54};
        {delta12=78}.
    r5: {delta11=12, delta12=50};
        {delta12=74}.

This is exhaustive for the necessary degree constraints, not an enumeration of actual instances or of historical campaign rows.

## 4. Every complete line flag violates equivariant Euler additivity

For a representation R and an integer e, equivariant Serre duality gives

    chi_G(R O(e))=R tensor Sym^e W             if e>=0,
                 0                          if e=-1,
                 -R tensor Sym^(-e-2) W     if e<=-2.

All irreducibles involved are self-dual and det W=1. Exact sequences in the full flag and 0->K->E->A->0 force the representation-ring equality

    Rflag=chi_G(E)-chi_G(A)-sum_(j=0)^13 chi_G(O(bj))=0.

For the five r3 degree patterns, in the displayed order, direct exact character arithmetic gives

    1+2A_std-V-P,
    1+2A_std-V-P,
    1+2A_std-V-P,
    1+A_std-P,
    A_std-V.

For the two r5 patterns it gives

    2+2A_std-2P,
    1+A_std-P.

Each is nonzero because irreducible characters form a basis. In particular A_std and V are the distinct three-dimensional irreducibles, not interchangeable symbols. Every residual has dimension zero, consistent with the already matched ordinary degree and Euler characteristic. The contradiction is equality failure, NOT a claim that a nongenuine virtual character cannot occur in a place where arbitrary virtual characters are permitted.

This excludes both target shapes for the P source. Section1 removed all other actual sources, proving the statement.

## 5. Independent short obstruction for r5

The weaker minimum-orbit bound alone forces delta0,...,delta6=0, since each corresponding weight is at least7 and7*12 exceeds either total. Hence Qj=O(14-2j) for j=0,...,7. Strict-top gives H0(F8(10))=0, and differentiation gives an injection

    H0(F7(10)) -> H0(Q6(8))=Sym10 W.

Since chi(F7(10))=chi(E(10))-chi(A(10))-sum_(i=0)^6 chi(Qi(10)), the character

    Sym10 W+chi(A(10))+sum_(i=0)^6 Sym^(24-2i) W-chi(E(10))

must be genuine. It is -1+2A_std+3V+4P+4D for r5, giving another contradiction. For r3 it is 2A_std+4V+4P+4D, which is genuine and gives no exclusion. This check is independent of enumerating the late defect patterns, but is not the proof of the r3 case.

## Reproducibility and limits

Run python3 verify.py and python3 -O verify.py; both must reproduce RESULT.json exactly. The verifier authenticates complete inputs, checks symmetric-power characters at all nine exact conjugacy traces through degree90, generates the complete bounded necessary orbit-degree patterns, checks all fourteen degrees and their total, and computes every signed Euler residual and the independent early-envelope crosscheck. It checks no selected actual HM/source coefficient, point, parameter, jet, tensor, instance matrix or instance rank. It does not restart any stopped experiment. These exact arithmetic controls support the written actual-map argument; they are not proof-assistant verification, a live frontier count, or a full original-theorem repair.

# Primal equality residual filtrations remove boundary strata

## Result and scope

The osculating chain in the primal equality cases gives ordinary residual exact sequences with strict degree bounds, without a descended connection. Applying them to the classified kernels N=K/C7 yields:

- For G3.11.942927348917 and G3.12.8e9af2d08af9, type Z5 must have alpha*beta!=0. Its two boundary strata are impossible.
- For G3.21.45ca6278cbfc, type Z5 is impossible altogether, and type Z3 must have a=0 (hence b!=0).

No quotient label is excluded. The first two labels retain five residual E types, with both coefficients nonzero on Z5. The third retains four types Z1,Z2,Z3,Z4, with a=0 on Z3. Their possible residual kernel bundles number four and two respectively. Each retained kernel type admits an ordinary residual filtration of the required degrees and strict top bounds. This last existence statement is not realization of the original ambient Gauss connection.

## 1. Honest residual filtrations

Let F0=K and F_j=F_(j-1)^-. The first osculating chain comes from the complete degree10 system of PR733. Write C_k for its k-th osculating bundle, so

    C_k=Sym^k W O(k-10).

Equality identifies every composite graded image with the highest HN summand. It follows inductively that

    C8 intersect F_j=C_(7-j),  0<=j<=7.

At each step, C_(8-j)/C_(7-j)=O(6-2j) maps isomorphically onto the highest line of Q_j=F_(j-1)/F_j. This gives both the intersection statement and the quotient exact sequence by taking the kernel of that map.

The strict-slope theorem gives top F_j<=-3-j. Since C_(7-j) is concentrated in degree-3-j, its coefficient inclusion splits in the top HN block. Thus for N_j=F_j/C_(7-j),

    top N_j<=-3-j,
    0 -> N_j -> N_(j-1) -> T_j -> 0,               (1)

where T_j is Q_j with its highest line removed. These are bundle exact sequences obtained from a commutative diagram of the actual flag. No derivative on N_j is asserted.

For heights(8,6,0), which apply to the first two labels,

    T_j=O(2-2j),  j=1,...,6;  N6=0.               (2)

For heights(8,5,1), which apply to the third label,

    T1=O(0)+O(-10),
    T_j=O(2-2j), j=2,...,5;  N5=0.               (3)

## 2. Boundary cuts for heights(8,6,0)

The two boundary kernels of Z5 are

    N0=V O(-4)+V O(-6),
    N0=P O(-4)+Wp O(-7).

In either case let U be the displayed V or P coefficient of O(-4). The first residual quotient N0 -> O(0) kills U O(-4), because Sym4 W=D contains neither V nor P. Hence U O(-4) lies in N1. The next quotient N1 -> O(-2) kills the same subbundle, because Sym2 W=A also contains neither V nor P. Consequently U O(-4) lies in N2, contradicting top N2<=-5 from(1).

Both boundary strata are therefore excluded. The nonboundary kernel T O(-5) remains.

## 3. Negative quotient cut for heights(8,5,1)

Equation(3) requires a surjection N0 -> O(0)+O(-10), in particular a nonzero map to O(-10). A bundle all of whose splitting degrees are greater than-10 has no such map.

Among the six classified kernel types, precisely

    S O(-3)+O(-8)+O(-10),
    D O(-4)+O(-10)

contain a degree-10 summand. The other four have all degrees greater than-10 and are impossible. In the scalar coordinates this excludes every Z5 stratum and the a!=0 stratum of Z3. Types Z1,Z2,Z4 and the a=0 stratum of Z3 remain.

## 4. Ordinary filtered sharpness of these tests

For completeness, the bounded verifier lists explicit residual chains for every retained kernel type. Each arrow is either full polynomial evaluation

    Sym^m W O(-j) -> O(m-j),

with kernel Sym^(m-1) W O(-j-1), or projection onto a line summand. For heights(8,6,0), the four starting kernels are

    S O(-3)+O(-8)+O(-10),
    D O(-4)+O(-10),
    S O(-3)+W O(-9),
    T O(-5).

The first three begin by evaluating their S or D summand until it becomes a line. Remaining line summands are projected off in the required order; the W O(-9) pair, when present, uses standard linear evaluation onto O(-8). The T chain uses six successive full evaluations. Their ranks, degrees, exact target lines and top bounds satisfy(1)-(2) at every step.

For heights(8,5,1), evaluate the S or D summand to O(0) and simultaneously project the O(-10) summand at the first step. The remaining evaluation-and-projection chains satisfy(1)-(3).

This proves that these ordinary residual rank/degree/section tests alone do not remove the retained kernel types. It does not assert compatibility of those freely constructed filtrations with the fixed central quotient map, its ambient embedding, or the actual constant connection.

## Reproduction

Run verify_primal_equality_residual_filtration_cuts.py. It pins the kernel-splitting package and the equality certificate, checks the two zero Hom calculations and all negative-quotient exclusions, and verifies six explicit filtered chains using full-evaluation and direct-projection rules. All source, kernel and quotient ranks/degrees and strict top bounds are checked. No actual-instance computation or quotient connection is used.

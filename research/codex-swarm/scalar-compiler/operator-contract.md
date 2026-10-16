# Exact operator contract and control scope

Let `p=(0,1)`, `q=(2,3)` and `G=g_ik=g_jk g_ij`, with physical row transitions. Physical fields commute and include the moving frame. The compiler implements

`k_p=-1/4[(V_a g^-1)(V_b g)-(V_b g^-1)(V_a g)]`,

`mu_p(B,A)=1/2[(V_a B)(V_b A)-(V_b B)(V_a A)]`,

and the mixed `mu2` with its four signed terms and coefficient `1/4`. These formulas are encoded as typed ordered products, not numerical source jets.

At `u0_p=g k_p`, `u0_q=g k_q`, the unnormalized baseline contains

`u0_p,jk u0_q,ij + u0_q,jk u0_p,ij`,

the four mixed `mu1` terms, mixed `mu2`, and

`-b_p u0_q,ik - b_q u0_p,ik - b_p b_q g_ik`.

Normalization is multiplication on the left by `g_ik^-1`, followed by the rank-two trace-free projection for the baseline. `F_p=b_p-tr(g_ik^-1 mu_p(g_jk,g_ij))/2`. The complete source is

`Rsharp=M0^0+F_q k_p,ik+F_p k_q,ik+E_p(T_q F_q)+E_q(T_p F_p)`.

For each directional correction the four terms are retained:

`E_p(s)=1/2[(V_a s_jk)g_ij^-1 V_b g_ij -(V_b s_jk)g_ij^-1 V_a g_ij +(V_b s_ij)g_ij^-1 g_jk^-1(V_a g_jk)g_ij -(V_a s_ij)g_ij^-1 g_jk^-1(V_b g_jk)g_ij]`.

The scalar solver is an operator on the entire `F` cochain template, not a cached scalar edge or a string in place of an input formula. Its three major branches and both prism signs are explicit DAG nodes. Differentiating it creates a combined-regular-numerator derivative request whose actual clearing witness remains false. No derivative of a raw partition summand is independently declared regular.

## Resolution lift

The hash-bound shared schema fixes

`J0=I_phys Rsharp^t P_phys`,

`J1=H_0 delta J0`, `J2=-H_-1 delta J1`, `J3=H_-2 delta J2`,

`H_r(F)=H_K F+(-1)^r (IP) F H_K`.

The nonzero `H_K` blocks are `H0:K1->K0`, `H1:K2->K1`, and `eta:K3->K2`. The compiler implements these products blockwise with real dimensions `(5,15,10,2)`, not an ungraded placeholder matrix. The retained closure equations are

`d_End J0=0`, `delta J0-d_End J1=0`, `delta J1+d_End J2=0`, `delta J2-d_End J3=0`, `delta J3=0`.

They are conditional on the complete source and contraction identities. The producer's independent exact abstract split-complex control checks all five equations with owner-varying contractions and a nonzero `J2`; reversing the `J2` sign fails that control. This verifies the implemented algebra, not physical source closure.

## Scalar map and transport

For each selected `(i,b)` the compiler emits the exact constant row

`L_i,b=X13[i,b]-sum_(a,k) gamma[i,a,k] X02[a,5b+k]`.

Here gamma entries in this formula are constant coefficients of the homogeneous linear map. No extra `v_k` is inserted. The 1,500 checks use the coefficient of every `W[a,b0] v_k` in the bottom differential; a changed selector sign produces a nonzero coefficient.

Each row acts on `J2` in Cech degree4/internal degree-2. The top relation gives `delta L(J2)=L(d_End J3)=0`. The uniform scalar-family theorem at PR79 `43193bc...` supplies the regular comparison on its admitted domain, hence

`Psi_(L,f)(Rsharp)=-lambda_(L,f) S Pi_outer H_-1 delta H_0 delta j(Rsharp)`.

The compiler's scalar stencil can be transported after applying L because this **constant same-frame** row commutes with the fixed scalar-weight cover maps, as proved by that theorem. It does not commute a trace-free projection through a physical selector as a new assertion: trace-free M0 is formed before inclusion in the source circuit.

For each weight monomial `m`, the target exponent is `-m-1`. Twenty row stencils feed the thirty-two PR83 weighted tests, with exact integer weights unchanged. There are24 signed CCCC staircases for every coefficient. Outer assignment sorting reindexes the pre-existing alternating source cochain; it never rebuilds an ordered nonlinear E formula after permutation. Physical/common vertex repetitions and owner occurrences remain distinct notions.

## Tests and limitations

The twelve producer tests cover exact bottom chain-map coefficients and a wrong sign; all24 staircase paths/bits; all five source components/seven kinetic/three gerbe terms; both J2 blocks and top J3;127 weighted terms/121 unique pairs; ordered matrix Leibniz rule; moving-frame jet flags; complementary-only whole-solver derivatives and three solver branches; preserved owner identities; common versus carrier repetition; shape/degree rejection; full abstract split-lift closure and a wrong J2 sign; and forged realization/top-component rejection.

Normal and optimized receipts report the commands that actually ran. No test imports a physical matrix evaluator, expands source polynomial coefficients, computes a numerical residual, or proves actual source-clearing/regular-extension/historical-comparison premises. A source adapter is still required at every such node. No Boolean supplied by a caller certifies it.

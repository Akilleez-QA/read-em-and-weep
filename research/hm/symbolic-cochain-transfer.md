# Symbolic second-order cochain and complete local End(K) transfer

## Scope

Two executable artifacts add a symbolic rational-function representation and a local transfer regression to the second-order experiment. Neither computes a global Ext² coordinate.

The symbolic generator works over Q(x1,x2,x3,x4). It constructs the elementary-symmetric map, the normalized carrier frames, the explicit first-order primitive, and the cross-character second-order residual by arithmetic operations and mixed derivatives. It then normalizes the residual as C2=g_ik^{-1}R in row coordinates.

For the carrier triple (0,1,5), the retained arithmetic DAG has 38,720 nodes. Nodes are rational constants, variables, addition, multiplication, or inversion; indices point backward. The four output indices form the normalized 2×2 row matrix. Thus the output defines exact rational functions without expanding their numerators. This is not interpolation. Evaluation at x=(2,3,4,5) agrees exactly with the independently instantiated rational-jet evaluation.

Run the symbolic generator with --emit-dag to print the full JSON representation. Without that option it prints a short size/index report.

## Complete local transfer

The transfer certificate uses all six carrier charts on the fixed finite line chart. It forms the row cocycle C2, transposes it, and embeds
J0_ijk=I_i C2_ijk^t P_i
in the degree-zero block of End(K).

Let e_i=I_i P_i and H_i be the actual degree −1 contraction. For a homogeneous endomorphism F of degree r,
h_i(F)=H_i F+(−1)^r e_i F H_i.
The total differential convention is δ_Cech+(−1)^q d_End on Čech degree q.

The implemented components are
J1=h δJ0,
J2=−h δJ1,
J3=h δJ2.
Their internal degrees are 0,−1,−2,−3 and Čech degrees are 2,3,4,5. The third term is retained: six charts allow a nonempty degree-five nerve.

At x=(2,3,4,5), the respective numbers of increasing-index cochains are 20,15,6,1. The certificate checks all 42 equations
δJ_(n−1)+(−1)^n d_End J_n=0,
with the initial equation d_End J0=0.
All pass in exact BigInt rational arithmetic.

These are pointwise regression checks for the instantiated transfer. The general transfer identity follows from the stated contraction identities and homological perturbation, with the fixed totalization signs.

## Remaining comparison

The cochains must still be transferred from the full carrier/line refinement to the original product cover, then to the finite Laurent model. In particular, the top-row finite component can receive a correction from the internal-degree −3/Čech-degree-five term. Discarding it merely because the variety has dimension four would be invalid before the comparison.

The symbolic cochain displayed here lies on a fixed finite line chart. Mixed line-frame transitions, their logarithmic derivatives, and the noncentral algebroid corrections require the corresponding global implementation. No nonvanishing or vanishing of the global obstruction is inferred from the raw rational matrix.

## Reproduction

From `research/hm` on this branch, run:

```sh
node verify-hm-second-order-local.js
node verify-hm-end-transfer.js
node generate-hm-second-order-dag.js --emit-dag > hm-second-order-dag.json
node verify-dag-evaluation.js
```

The last command evaluates every retained DAG node with a separate exact rational evaluator and compares all four output entries against the numerical jet implementation at the displayed point. It also reruns that implementation's 42 transfer equations. All checks passed; this comparison is still pointwise evidence, not a global cohomology calculation.

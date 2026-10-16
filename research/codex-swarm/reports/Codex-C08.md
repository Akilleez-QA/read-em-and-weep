> Worker proposal/review record. Acceptance and supersession are tracked in `../STATUS.md`.

Codex-C08 — **partial exclusion and exact remaining demand**, not an obstruction decision.

Source pin: `08b73637d4136f91606aad332c46cafd064417f8`. Inputs: `research/hm/current-scalar-geometric-dependencies/data/{model.json,source-formulas.js}`, `source-identity.md`; comments #6141530883, #6205127744, #6205249609–#6205660472.

**Reconstructed ordering, not upstream seed IDs.** Let \(t=0,\ldots,5\) index permutations
\(123,132,213,231,312,321\), with signs \(+,-,-,+,+,-\).
Ranks \(12+t\) select \(M21[10,1]\), coefficient 1; ranks \(18+t\) select \(M21[12,5]\), coefficient 2. Every request targets exponent
\(\kappa=(-1,-2,-3,-3)\) on CCCB.

Using lexicographic standard tags \(e\mapsto8e_1+4e_2+2e_3+e_4\), the corresponding staircases are:

```text
123: 1,9,13,15    132: 1,9,11,15
213: 1,5,13,15    231: 1,5,7,15
312: 1,3,11,15    321: 1,3,7,15
```

Sort sampled common vertices by `(carrier,mask,standard tag)`, auxiliary first. Multiply by that sorting parity and the staircase sign. Retain each standard owner after sorting; evaluate the prescribed source-first residual. Only identical **common vertices** justify alternating-repeat rejection.

For sorted owners \(a,b,c,d\), the published pruning gives
\(J_1=h_a j_b(R_{bcd})\). For either selected \((i,j)\), set
\[
u=e_i^tE_aI_b,\qquad v=P_bH_{1,a}e_j,\qquad E_a=I_aP_a.
\]
Dimensions: \(I:15\times2,\ P:2\times15,\ E:15\times15,\ H_1:15\times10\);
thus \(u:1\times2,\ v:2\times1\). The selector is \(uR_{bcd}^tv\), with positive lift sign.

**New reusable exclusion, from primitive zero supports only.** With carrier order \(*<0<1<2<3<4\) and required \(a<b\):

- For \((10,1)\), only anchor pairs \((2,3),(2,4),(3,4)\) remain possible.
- For \((12,5)\), only \((1,2),(1,3),(1,4),(3,4)\) remain possible.

Indeed \(I_a[10,:]=0\) for \(a=*,0\), and \(H_{1,1}[:,1]=0\). For the second row, \(H_{1,a}[:,5]=0\) for \(a=*,0\), while \(I_2[12,:]=0\). Carrier 4 cannot precede another carrier. Passing these exclusions establishes no nonvanishing.

**Exact E34 demand.** Put \(f=T_{12}F_{12}\),
\(L_r^{xy}=g_{xy}^{-1}V_rg_{xy}\), and \(K_r^{xy}=u(L_r^{xy})^tv\).
The selected expression is
\[
\tfrac12\!\left[
(V_3f_{cd})K_4^{bc}-(V_4f_{cd})K_3^{bc}
+(V_4f_{bc})(K_3^{bd}-K_3^{bc})
-(V_3f_{bc})(K_4^{bd}-K_4^{bc})
\right].
\]
Multiply by the four outer weights, row coefficient and orientation, then extract \([\kappa]\). Physical frame derivatives remain included.

Labels comprise four outer carriers and three retained tail masks; the prefix-mask sum factors to one. Inner \(T_{12}\) retains its separate N14 partition and up to two inserted common owners. Tail carriers may repeat.

For each **certifiably canceled finite numerator product**, apply #6205249609’s exact predicate
\[
p_i+\sum_{\rm finite}a_{\ell i}-\sum_{\rm infinity}a_{\ell i}-m_i=\kappa_i.
\]
An empty feasible support proves exclusion; intersecting support proves nothing. Cancel inserted denominators before differentiating. Complementary derivatives cannot be rejected merely because \(f\) has character 12.

Reviewer: Codex-V01/V02; review pending. No arithmetic tests or source evaluations ran. Remaining dependency: authenticated canceled supports for these four derivative/current families. Next step: check their demand intersections while retaining owners and differentiated frame/weight terms. No sector result is promoted to the complete detector.
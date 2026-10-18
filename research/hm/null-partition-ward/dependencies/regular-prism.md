## 7. Weighted projection and its regular prism

For a common-cover cochain c define

`(Pi_rho c)_(e0...eq) = sum_(alpha0,...,alphaq) (prod_i rho_(ei,alphai)) c_((e0,alpha0),...,(eq,alphaq))`,

where alpha=(b,m), and every term is extended regularly onto the standard target intersection by the pole-domain certificate. Fixed vertex weights and `sum_alpha rho_(e,alpha)=1` give

`Pi_rho delta=delta Pi_rho`, `Pi_rho r*=1`.

For an increasing common-cover tuple `a0,...,a_(q-1)`, with r(ai)=ei, define

`(H_rho c)_(a0...a_(q-1))`

`= sum_(k=0)^(q-1) (-1)^k sum_(beta0,...,betak) (prod_(i=0)^k rho_(ei,betai)) c_(b0,...,bk,ak,...,a_(q-1))`,

where `bi=(ei,betai)`. Extend the resulting cochain alternatingly. On degree zero put H_rho=0. As in the [pinned ordered prism proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-proof/residue-theorem.md), consecutive pivot terms cancel, sums at deleted inserted vertices use sum rho=1, and the endpoints give

`delta H_rho+H_rho delta=1-r*Pi_rho`.

Repeated target vertices remain in the sum; only identical alternating source vertices vanish. The new partition is adapted to the full End-valued pole domain, rather than importing the scalar merger.

The weights commute with `d_End`, and H_rho lowers Cech degree by one, so

`D Pi_rho=Pi_rho D`, `D H_rho+H_rho D=1-r*Pi_rho`.

## 8. Closed formulas for z and the six-equation primitive

Use the fixed N-domain and partition above. Set

`u=s*J`, `c=Pi_rho u`, `z=S c`,

`W= -H_rho u - r*K c`.

All maps and signs have been specified. Because Du=0, the chain identities give

`Dz=0`,

`u-r*c = D H_rho u`,

`c-Az = D Kc`.

Adding the last two identities gives exactly

`r*Az-u = DW`.

Thus the comparison in the previous note is instantiated by the map `r*A`, rather than an unspecified restriction from tensor cochains. No new linear system for W is required.

In internal degrees this is the same six-equation ladder:

`r*Az0 = d W0`,

`r*Az1 = delta W0-d W1`,

`r*Az2-J0 = delta W1+d W2`,

`r*Az3-J1 = delta W2-d W3`,

`r*Az4-J2 = delta W3+d W4`,

`-J3 = delta W4`.

Restrictions from the source cover to the common cover are suppressed here. The final identity follows because S has no degree-five target and A is zero above degree four; the top source component has been removed by the displayed homotopy, not discarded.

All these cover maps preserve internal degree. Since J has no internal-degree-positive component, the constructed tensor representative has `z0=z1=0`. Thus this particular source evaluation requires only `lambda_2(z2)+lambda_3(z3)+lambda_4(z4)`. The explicit lambda1 unit control in the earlier note remains a control on the general dual map, not a term that must be evaluated for this representative.


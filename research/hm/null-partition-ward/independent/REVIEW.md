# Independent review

## Verdict

Accepted as a conditional exact rational/cochain identity for the whole specified outer-weight derivative family. The statement neither cancels that family nor proves a zero pairing or rational divergence. The reviewed original proof SHA-256 is 4393498841d9d5e81097730f286569db9614f131e82821bf2828ba60a392e77d; the portable proof incorporates the qualifications below.

## Direct audit

The source-adjoint branch table has derivative axes a,b,b,a, currents L_b,L_a,U_a,U_b, endpoints jk,jk,ij,ij and coefficients +1/2,-1/2,+1/2,-1/2. Gathering by derivative axis gives exactly Z_a=(s_jk L_b-s_ij U_b)/2 and Z_b=(-s_jk L_a+s_ij U_a)/2 for both complementary pairs. The adjoint supplies the external minus. The current-curl formula leaves precisely the same outer-weight contribution inside its coefficient derivative. No scalar derivative is introduced in Z_d.

The raw triple has Čech degree 2. Inclusion has internal degree 0 with one transpose; the first δ then H_0 produces degrees (3,-1), the second δ then -H_-1 produces (4,-2). The selector produces scalar degree 4. Q lowers Čech degree by one, so both δQ c and Qδc have degree 4; S applies in the corresponding degrees. HPL faces preserve source-increasing order, and alternation is applied to the completed increasing-tuple construction. Original weights remain outside it, and deleted-prefix owners stay in the circuit. A-linear expansion is valid in the fixed common rational frame; it does not authorize pulling tuple-dependent scalar leaves through δ as a single global scalar.

The mixed-partition prism has boundary Π_new-Π_old. Its parameter derivative at equal partitions leaves only the dotted duplicate-pivot weight; the other terms cancel by exchanging the two identically weighted pivot vertices. This gives the stated positive δQ+Qδ sign. The degree-zero formula independently fixes the orientation. Set the parameter variation equal to V_d rho after freezing the input cochain and all other factors. A total physical derivative would have additional terms, which are intentionally outside this family.

Multiplication by the same rational p commutes with restrictions and the staircase map. This is not the assertion V_d p=0, nor the assertion that p is globally regular on the projective variety. It therefore permits the displayed rational Čech boundary but supplies no regular-domain or residue vanishing conclusion.

The complete closed-source selector is a legitimate positive control via δJ2=d_End J3 and L d_End=0. Endpoint-current inputs do not inherit that closure. The explicit defect is essential. The anchor identity is exact by the zero sum of weight variations; its individual summands have no newly established regular-extension property.

## Controls and limits

The original coefficientwise prism checker passes under normal and optimized Python. A separately implemented exterior-chain checker verifies degrees 0–4 with two-letter invented fibers, degrees 0–2 with three-letter invented fibers, reverse target ordering, and differentiation of the finite mixed-partition prism. Dropped-defect and reversed-defect-sign variants are rejected. The source-binding checker fixes every branch field and gathers Z coefficients exactly; predecessor section hashes bind supplied bytes. The mathematical correspondence to those source sections is this written audit, not a claim that hashes prove semantics.

No evaluator is certified on repeated target tags. No endpoint-current pole bound, differentiated-prism regular extension, new frame/parity theorem, source value, matrix-polynomial product, or production execution is established. In particular complete-J2 bounds alone cannot be transferred to the four c_d. The possible sharper domain theorem remains separate work.

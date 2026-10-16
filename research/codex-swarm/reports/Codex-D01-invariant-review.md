**D01 verdict: accept V07’s invariant basis and 20-map block; the complete 32-row selection remains conditional. Corrected \(R^\sharp\) is undecided.** Domain: \(\mathbf Q\), pinned perfect complex, with geometric applicability requiring the authenticated comparison.

Write \(P=\texttt{08b73637d4136f91606aad332c46cafd064417f8}\). Resolved secondary pin:
\(H=\texttt{e6e8d272e760a432dbbc1053b88c8eae03a47304}\).

1. **Invariant ring: accepted.** On \(Y_i=1\), the three conjugates of \(Q\) are
\[
x_1x_2+x_3x_4,\quad x_1x_3+x_2x_4,\quad x_1x_4+x_2x_3.
\]
Their elementary symmetric functions are \(e_2,\ e_1e_3-4e_4,\ e_3^2+e_1^2e_4-4e_2e_4\). Homogenization gives exactly
\[
Q^3-v_2Q^2+(v_1v_3-4v_0v_4)Q
-(v_0v_3^2+v_1^2v_4-4v_0v_2v_4)=0.
\]
The generic stabilizer is \(D_8\), so the degree over \(\operatorname{Frac}(A)\) is three. Thus \(1,Q,Q^2\) are \(A\)-independent. Equality of graded Hilbert series then proves
\[
R^{D_8}=A\oplus AQ\oplus AQ^2.
\]
Hilbert premise: `research/hm/d8-small-certificates/p4/Perfect-Complex-D8-F3.md`, §3, at `f968b53943ba2312f09fbc3e8f9d462e86bcaa34`.

2. **Supertrace identification: accepted, with explicit orientation.** At \(H\), `research/hsd/twist-minus2-d5/certificate.py`, `decode80/index80`, places the free positive entry \(B_{b,i}\) at \(50+15b+i\). For \(K_j=(A,B)\), \(j=15b+i\), the cycle equation is
\[
\mathrm{ev}A-B\gamma=0,\qquad
A_{5b'+k,a}=\gamma[i,a,k]\delta_{b'b}.
\]
For negative-degree \(X=(X_{02},X_{13})\), using complex degrees \(0,1,2,3\),
\[
\operatorname{str}(XK_j)
=\sum_{a,k}\gamma[i,a,k]X_{02}[a,5b+k]-X_{13}[i,b]
=-L_{i,b}(X).
\]
Shifting all complex degrees changes the common sign. **Target/source reversal is essential:** matching ordinal indices without reversing Hom directions does not establish this pairing.

3. **Twenty classes: accepted from the published quotient certificate.** \(H\): `research/hsd/twist-minus2-d5/NOTE.md` gives
\[
[K_r]+[K_{25+r}]=[K_{10+r}]+[K_{20+r}]=0
\quad(0\le r<5).
\]
These disjoint pairs prove that the stated \(I_{20}\) is a quotient basis. It includes \((10,0),(10,1)\), hence both designated old maps up to their signs. The maps are also linearly independent as constant chain maps because their \(X_{13}\) coefficients are distinct coordinate units.

4. **Correct block, incomplete selection.** Equivariant Serre duality identifies the epsilon dual with
\[
H^2(B)\oplus H^2(B(-1))Q\oplus H^2(B(-2))Q^2.
\]
Therefore the labels are correctly \(20Q^2,\ 10v_kQ,\ 2v_kv_l\). The twenty quotient classes form the dual basis of the first epsilon domain block, not a claimed Kronecker basis against unspecified harmonic coordinates.

**Missing:** ten labels \((i,b,k)\) and two labels \((i,b,k,l)\), cycle certificates, and augmented ranks \(250\) over boundary rank \(240\), respectively \(850\) over \(848\). The invariant-ring basis alone does not prove these multiplication candidates span. Failed ranks reject this restricted selection plan, not published all-30 completeness.

Original progress: the explicit supertrace/order check above. No oracle, matrix calculation, or physical evaluation ran. Reviewer: **V07/orchestrator**. Next: certify the missing 10+2 selections, then authenticate complete \(R^\sharp\) pairings under comments **6205127744, 6205660472, 6206738230**.
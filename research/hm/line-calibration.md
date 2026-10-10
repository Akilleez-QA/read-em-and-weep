# Exact first-order line calibration

This is an explicit cochain certificate for the expected calibration value. It does not assert that the full bundle-to-finite-RHom comparison has been implemented.

On C:y²=x³−x take q=y/x and V=y∂x+(3x²−1)∂y/2. On the legal cover U₀=C\{∞}, U₁=C\{(0,0),(1,0),(−1,0)}, the transition of N=O(∞) is q.

Its logarithmic derivative is
r=V(log q)=(x²+1)/(2y)=q/2+1/y.
The last equality follows after clearing denominators from y²=x³−x. Since 1/y is regular on U₁, put c₀=0,c₁=1/y; then r=q/2+δc.

For two factors, let q₁,q₂ be additive Čech 1-cocycles and r_i=q_i/2+δc_i. In the consistent left-row convention the normalized Moyal defect is
μ_ijk=−(r₁,ij r₂,jk−r₂,ij r₁,jk)/2.

Define the scalar Čech 1-cochain
h_ij=c₁,i r₂,ij−q₁,ij c₂,j/2+r₁,ij r₂,ij/2.
Then direct expansion gives
μ+(q₁∪q₂)/4=−δh.

The executable verify-line-calibration.js checks this universal identity over an integer polynomial ring after multiplying by 8. It uses independent formal values for q₁,01,q₁,12,q₂,01,q₂,12 and all six vertex values of c₁,c₂, with q_i,02=q_i,01+q_i,12. Its assertions were executed exactly.

For the compensated algebroid b=15(q₁∪q₂+q₃∪q₄)/4, the first-order line obstruction μ−b is therefore cohomologous to
−4(q₁∪q₂+q₃∪q₄)=16Π.

Replacing N by N⁻¹ negates both logarithmic derivatives, leaving the quadratic Moyal defect unchanged. The same value follows.

These q_i classes are the standard odd Laurent H¹ representatives in the original finite-cover model. Thus the expected finite cohomology coordinate is fixed explicitly. The implemented global comparison must reproduce it, and must send the E residual to zero, before its second-order output is interpreted.

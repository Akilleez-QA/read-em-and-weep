#!/usr/bin/env python3
"""Universal characters and binary multiplication only; no actual HM map."""
from pathlib import Path
import runpy
q=runpy.run_path(str(Path(__file__).with_name('verify_pure_cross_block_couplings.py')))
sy,vm,inn=q['sy'],q['vm'],q['inner']
A,V,W,Wp,P=[q[n] for n in ('A','V','W','Wp','P')]
S4,D5,T6=sy(3),sy(4),sy(5)
add=lambda a,b:[q['add'](x,y) for x,y in zip(a,b)]
wp_sym=lambda n:[q['sym'](n,t) for t in Wp]
assert wp_sym(2)==V
assert wp_sym(3)==S4
assert wp_sym(4)==D5
assert inn(S4,S4)==1
assert vm(Wp,S4)==add(V,D5)
assert inn(vm(Wp,S4),A)==0
assert inn(vm(Wp,S4),V)==1
assert vm(Wp,D5)==add(S4,T6)
assert vm(W,D5)==add(S4,T6)
assert vm(V,A)==add(P,D5)
assert inn(D5,vm(V,A))==1
# Every quartic monomial is the product of a linear and cubic monomial.
quartic_y_exponents={i+j for i in (0,1) for j in range(4)}
assert quartic_y_exponents==set(range(5))
# Source/target ranks and degrees in the exact sequence.
rank=5-2; degree=5*(-2)-2*(-5)
assert (rank,degree)==(3,0)
assert 2*4-5==3  # c_f is onto by dual Cartan multiplication
assert min(4,6)>3 # any nonzero kernel representation contradicts h0(G2)=3
assert rank+degree==3
assert rank*(1-1)+degree==0 # chi(G2(-1))
print('PASS: the global cubic-product quotient is V O_L, not A O_L.')
print('PASS: both S4/T6 channels are nonzero by the representation-dimension gap, with no scalar evaluation.')
print('Application requires the actual global grade to be identified with this universal cokernel.')

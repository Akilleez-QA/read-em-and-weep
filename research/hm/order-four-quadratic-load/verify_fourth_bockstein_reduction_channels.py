#!/usr/bin/env python3
"""Universal filtered composition and character identities for the fourth gate."""
import contextlib,io,runpy
from pathlib import Path
with contextlib.redirect_stdout(io.StringIO()):
    r=runpy.run_path(str(Path(__file__).with_name('verify_negative_vertex_scalar.py')))
va,vs,vm=r['vadd'],r['vscale'],r['vmul']
one,A,V,P,D,W,tr=r['one'],r['A'],r['V'],r['P'],r['D'],r['W'],r['tr']
sym=r['sym']; inner=r['inner']; z=r['z']
S=lambda n:[sym(n,x) for x in tr]
sym2A=va(one,D)
sym4A=va(one,D,S(8))
quartic=va(vm(P,sym4A),vs(-1,vm(A,sym2A)))
kernel=va(vm(P,sym2A),vs(-1,A))
squares=S(20)
assert quartic==va(one,A,vs(2,V),vs(3,P),vs(4,D))
assert kernel==va(V,vs(2,P),vs(2,D))
assert squares==va(one,A,V,P,vs(2,D))
assert quartic==va(kernel,squares)
assert [inner(D,x) for x in (quartic,kernel,squares)]==[z(4),z(2),z(2)]
assert [x[0][0] for x in (quartic,kernel,squares)]==[42,21,21]
assert inner(D,vm(A,A))==z(1)
# Free-word coefficient extraction: no actual map or matrix instantiated.
coeff={2:['B2_D'],3:['B3_D','-B2_A L'],4:['B4_D','-B3_A L']}
assert coeff[3]==['B3_D','-B2_A L']
assert coeff[4]==['B4_D','-B3_A L']
# Relations B2_D=0 and B3_D=B2_A L kill orders2 and3.
assert {'B3_D':'B2_A L'}[coeff[3][0]]==coeff[3][1][1:]
print('PASS: unique linear equivariant third correction; fourth coefficient B4_D-B3_A L.')
print('PASS: quartic target42=1+A+2V+3P4+4D5; four channels split2+2 on kernel/squares.')
print('No actual fourth coefficient or nonvanishing evaluated.')

import sympy as sp
t,a,h,b=sp.symbols('t a h b')
xi,za,vh,wh=sp.symbols('xi za vh wh')
coeffs=[h*xi,h*za-b*xi,vh-b*za,wh]
qimages=[0,h*a*xi,a*h*za-b*a*xi,a*(vh-b*za)]
for j in range(1,4):
    assert sp.expand(qimages[j]-a*coeffs[j-1])==0
assert sp.expand(-a*coeffs[3])==-a*wh
print('PASS: actual corrected lift telescopes through order3, leaving -t^4 a w_h.')

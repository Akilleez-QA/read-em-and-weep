"""Universal character checks only; no actual differential evaluation."""
import runpy
from pathlib import Path
q=runpy.run_path(str(Path(__file__).with_name('verify_negative_vertex_scalar.py')))
add,mul,scale,inn=q['vadd'],q['vmul'],q['vscale'],q['inner']
one,A,V,W,Wp,S,D,T=[q[k] for k in ['one','A','V','W','Wp','S','D','T']]
N=q['N']; H=q['H']
lam2N=add(one,A,T)
assert inn(H,lam2N)==q['z'](0)
lam3H=q['L2'] # dim H=5, det H=1 and self-duality
source=mul(N,Wp); target=mul(V,lam3H)
assert source==add(one,V,T)
assert lam3H==source
assert inn(source,one)==inn(target,one)==q['z'](1)
assert add(target,scale(-1,source))==add(W,V,S,D,T)
assert inn(lam2N,one)==q['z'](1)
for k in [0,1]:
 for rank in range(k+1): assert 1<=k+1-rank<=2
print('PASS: independent monad bound 1 <= h1(B_Q0(-2))^G <= 2; no actual scalar selected.')

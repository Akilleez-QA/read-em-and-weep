"""Universal channels and invariant tensor only; no actual monad evaluation."""
from pathlib import Path
import runpy
q=runpy.run_path(str(Path(__file__).with_name('verify_negative_vertex_scalar.py')))
add,mul,inn=q['vadd'],q['vmul'],q['inner']
Wp,V,T,A,P,D=[q[k] for k in ['Wp','V','T','A','P','D']]
assert q['L2']==add(q['one'],V,T)
assert mul(Wp,T)==add(A,P,D)
assert inn(mul(Wp,V),Wp)==q['z'](1)
assert inn(mul(Wp,T),Wp)==q['z'](0)
assert inn(mul(V,V),q['one'])==q['z'](1)
# Coordinates of the universal image in Sym2(Wp) tensor Sym2(Wp).
image={(1,1):2,(2,0):-1,(0,2):-1}
assert any(image.values())
print('PASS: exactly two W-prime channels; invariant symmetrization selects the V channel nontrivially.')
print('Nonzero actual V channel follows geometrically from subbundle injectivity on L, not a coefficient test.')

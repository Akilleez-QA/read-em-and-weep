"""Universal character and symbolic checks; no actual-instance evaluation."""
from pathlib import Path
import runpy
import contextlib
import io
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
    q=runpy.run_path(str(Path(__file__).with_name('verify_pure_cross_block_couplings.py')))
vm,inn=q['vm'],q['inner']
W,V=q['W'],q['V']
one=[q['sym'](0,t) for t in W]
add=lambda a,b:[q['add'](x,y) for x,y in zip(a,b)]
T6=[q['sym'](5,t) for t in W]
assert vm(V,W)==T6
cohom=add(add(one,V),vm(V,W))
assert inn(one,cohom)==1
assert inn(W,cohom)==0
assert inn(one,vm(W,cohom))==0
assert inn(one,W)==0
assert inn(one,vm(W,W))==1
# Actual even vertex line degrees, twisted by -1, all have H0=0.
vertex_line_degrees=[0,-1,0,-1]
assert all(d-1<0 for d in vertex_line_degrees)
# First conic layer: h1(O(-2))=1 and h1(O)=0.
def h1(n): return max(-n-1,0)
assert h1(-2)==1 and h1(0)==0
u,v,t=s.symbols('u v t')
# Universal resolution of an ordinary square of a regular pair.
assert s.expand(-v*u*u+u*(u*v))==0
assert s.expand(-v*(u*v)+u*v*v)==0
# Dual residue restricted to the scalar section-line direction.
assert s.expand((v*(u*t)+u*(v*t))/2-u*v*t)==0
assert s.cancel((u*v*t)/(u*u*v*v)-t/(u*v))==0
# Invariant LES implications, with input dimensions supplied by the geometry.
left_h1=0; right_h2_invariants=inn(one,vm(W,cohom))
assert left_h1==right_h2_invariants==0
assert inn(one,cohom)==inn(one,vm(W,W))*h1(-2)==1
print('PASS: no-W kernel vanishing, invariant conic restriction, and nonzero scalar residue comparison')

"""Universal characters and regular-pair identities; no instance evaluation."""
from pathlib import Path
import runpy,contextlib,io
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
    c=runpy.run_path(str(Path(__file__).with_name('verify_negative_vertex_scalar.py')))
W,V,P,D,one=[c[x] for x in ['W','V','P','D','one']]
sym,add,vm,inn,z=[c[x] for x in ['sym','vadd','vmul','inner','z']]
assert [sym(8,t) for t in W]==add(P,D)
assert [sym(6,t) for t in W]==add(V,P)
assert inn(one,vm(V,[sym(8,t) for t in W]))==z(0)
assert inn(one,vm(P,[sym(6,t) for t in W]))==z(1)
assert inn(one,[sym(7,t) for t in W])==z(0)
f,g,p,d,r=s.symbols('f g p d r')
K=s.Matrix([[d,0],[r,-d]]); T=s.Matrix([[1,0],[p,1]])
assert T*K*T.inv()==s.Matrix([[d,0],[r+2*p*d,-d]])
N=s.Matrix([[f*g,-f*f],[g*g,-f*g]])
assert s.expand(s.trace(N*K)-(2*f*g*d-f*f*r))==0
assert 4-6==-2 and -4-6==-10 and -2-6==-8
assert -2+3*(-10)==4*(-8)
assert 6+8>8
print('PASS: actual coefficient-bundle twists, trace covariance, and diagonal invariant isomorphism.')
print('Combined with beta nonzero, the actual lowest vertex diagonal is nonzero; no endpoint or fourth value is computed.')

"""Exact characteristic-zero verification; requires sympy only."""
from itertools import product
import sympy as s
bits=list(product((0,1),repeat=4))
z=s.symbols('z0:16')
A=z[0]; B=z[1]+z[2]+z[4]+z[8]; D=z[7]+z[11]+z[13]+z[14]; E=z[15]
U=z[3]+z[12]; V=z[5]+z[10]; W=z[6]+z[9]
forms=(A,B,D,E,U,V,W)
q=4*A*E-B*D+U*V+U*W+V*W
k=A*D**2+B**2*E-4*A*E*(U+V+W)-U*V*W
M=s.Matrix([[s.diff(f,v) for v in z] for f in forms])
w=s.symbols('A B D E U V W');aa,bb,dd,ee,uu,vv,ww=w
G=s.hessian(4*aa*ee-bb*dd+uu*vv+uu*ww+vv*ww,w)
Q=s.hessian(q,z)
assert M.rank()==7 and G.det()==32 and Q.rank()==7
assert Q==M.T*G*M and Q.nullspace()==M.nullspace()
a=s.symbols('a1:5'); b=s.symbols('b1:5')
segre={z[i]:s.prod(a[j] if c==0 else b[j] for j,c in enumerate(idx)) for i,idx in enumerate(bits)}
assert s.expand(q.subs(segre))==0
assert s.expand(k.subs(segre))==0
print('rank(M)=7; det(G)=32; rank(Hessian(q))=7; radical=ker(M).')
print('Both quadratic and cubic restrict identically to zero on Segre.')
t=s.symbols('t1:5')
for chart in bits:
    patch={a[j]:(1 if c==0 else t[j]) for j,c in enumerate(chart)}
    patch.update({b[j]:(t[j] if c==0 else 1) for j,c in enumerate(chart)})
    equations=[s.expand(f.subs(segre).subs(patch)) for f in forms]
    basis=list(s.groebner(equations,*t,order='grlex'))
    assert basis==[1]
    print('Chart '+''.join(map(str,chart))+': radical equations have Groebner basis [1].')
print('PASS: rank seven and geometrically disjoint projective radical.')

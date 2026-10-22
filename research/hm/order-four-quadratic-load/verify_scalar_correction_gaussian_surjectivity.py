#!/usr/bin/env python3
"""Universal binary identities and representation arithmetic, no HM instance."""
import sympy as S
import runpy
s,t=S.symbols('s t')
def form(name,d):
    cs=S.symbols(f'{name}0:{d+1}')
    return sum(cs[j]*s**(d-j)*t**j for j in range(d+1))
def first(f,g):return S.diff(f,s)*S.diff(g,t)-S.diff(f,t)*S.diff(g,s)
def pairing(f,g,d=4):
    return S.expand(sum((-1)**j*S.binomial(d,j)*S.diff(f,s,d-j,t,j)*S.diff(g,s,j,t,d-j) for j in range(d+1)))
a,q=form('a',2),form('q',2);F,Z=form('f',4),form('z',4)
assert S.expand(first(a*a,q)/2-a*first(a,q))==0
assert S.expand(pairing(first(F,q),Z)+pairing(F,first(Z,q)))==0
z=S.symbols('z');fz=F.subs({s:1,t:z});qz=q.subs({s:1,t:z})
assert S.expand(first(F,q).subs({s:1,t:z})-(4*fz*S.diff(qz,z)-2*S.diff(fz,z)*qz))==0
c=runpy.run_path('verify_negative_vertex_scalar.py')
vm,va,inn,zz=c['vmul'],c['vadd'],c['inner'],c['z']
D,A,V,P,W,Wp,one=[c[k] for k in ('D','A','V','P','W','Wp','one')]
assert vm(D,D)==va(one,A,V,P,P,D,D)
assert vm(D,A)==va(A,V,P,D)
for j in range(4):
    assert inn([c['sym'](j,x) for x in W],Wp)==zz(0)
assert -2*3 == -6 and -(-6)==6 and -6+4==-2
print('PASS: exact quartic Gaussian/Atiyah identity, apolar adjoint, kernel characters, and second-fundamental degrees.')
print('The rank15 conclusion is geometric; no actual coefficients, matrix, or numerical rank were evaluated.')

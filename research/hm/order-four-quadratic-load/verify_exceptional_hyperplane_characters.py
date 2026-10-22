#!/usr/bin/env python3
"""Actual equivariant K-class, universal C5 x central-involution characters only.
No actual HM coefficients, multiplication matrices, or ranks are evaluated.
"""
from itertools import combinations
from collections import Counter

def rep(weights): return Counter(weights)
def add(*reps):
 out=Counter()
 for r in reps:
  for k,v in r.items(): out[k]+=v
 return out

def scale(n,r): return Counter({k:n*v for k,v in r.items()})
def mul(r,s):
 out=Counter()
 for (p,a),m in r.items():
  for (q,b),n in s.items(): out[((p+q)%2,(a+b)%5)]+=m*n
 return out

one=rep([(0,0)])
V=rep([(0,0),(0,1),(0,4)])
W=rep([(1,1),(1,4)])
Wp=rep([(1,2),(1,3)])
A=rep([(0,0),(0,2),(0,3)])
N=add(A,Wp)
ambient=[(0,0),(0,1),(0,4),(1,1),(1,4)]
U=rep(ambient)
L2=rep([((p+q)%2,(a+b)%5) for (p,a),(q,b) in combinations(ambient,2)])
def symU(n):
 dp=[Counter() for _ in range(n+1)]
 dp[0]=one.copy()
 for p,a in ambient:
  for d in range(1,n+1):
   for (q,b),m in list(dp[d-1].items()):
    dp[d][((p+q)%2,(a+b)%5)]+=m
 return dp[n]

# F=Wp*Omega²(2)-N*O(-1)-N*O, Omega²(2)=Lambda²U-U*O(1)+O(2).
Fc={-1:scale(-1,N),0:add(mul(Wp,L2),scale(-1,N)),1:scale(-1,mul(Wp,U)),2:Wp}

def chiB(t):
 out=scale(-1,symU(t))
 for i,ri in Fc.items():
  for j,rj in Fc.items(): out=add(out,mul(mul(ri,rj),symU(t+1+i+j)))
 return out

def H1B(t):
 r=scale(-1,chiB(t))
 assert all(v>=0 for v in r.values())
 return r
r2,r3=H1B(2),H1B(3)
weights=lambda r,p:[r[(p,a)] for a in range(5)]
assert sum(weights(r2,0))==41 and sum(weights(r2,1))==44
assert sum(weights(r3,0))==46 and sum(weights(r3,1))==54
print('H1 B2 even/odd:',weights(r2,0),weights(r2,1))
print('H1 B3 even/odd:',weights(r3,0),weights(r3,1))
# At a root whose hyperplane equation has character zeta, multiply source by that character.
for ell in (1,4):
 source=[r2[(1,(a-ell)%5)] for a in range(5)]
 target=weights(r3,0)
 defect=[max(s-t,0) for s,t in zip(source,target)]
 print('ell weight',ell,'even-hyperplane source',source,'target',target,'forced kernel defects',defect)
print('PASS: the actual K-class gives the established dimensions/parities without evaluating any multiplication map.')
# Test the proposed j=2 free quotient of degree2 against local character bookkeeping.
base=[1,1,1,2,0]  # target-source+the known square weights1,3,4, at ell weight1.
unit=lambda a:[int(i==a%5) for i in range(5)]
vecadd=lambda *vs:[sum(t) for t in zip(*vs)]
vecneg=lambda v:[-x for x in v]
possible_free={}
# Splitting O(2)+O^4, with O(2) fiber weight3.
reps4={'4':[0,1,1,1,1],'A+1':[2,0,1,1,0],'V+1':[2,1,0,0,1],'1^4':[4,0,0,0,0]}
for name,r in reps4.items(): possible_free['O2 + '+name]=vecadd(unit(3),r)
# Splitting O(1)^2+O^3: spin two multiplicity W or Wprime; O1 fiber weight4.
reps3={'A':[1,0,1,1,0],'V':[1,1,0,0,1],'1^3':[3,0,0,0,0]}
for spin,top in [('W',vecadd(unit(0),unit(3))),('Wp',vecadd(unit(1),unit(2)))]:
 for name,r in reps3.items(): possible_free['O1 '+spin+' + '+name]=vecadd(top,r)
for eparts in ((2,),(1,1)):
 from itertools import product
 matches=[]
 for generators in product(range(5),repeat=len(eparts)):
  free=base[:]
  for a,e in zip(generators,eparts): free=vecadd(free,unit(a+2*e),vecneg(unit(a)))
  for name,r in possible_free.items():
   if free==r: matches.append((generators,name))
 print('j=2 local exponents',eparts,'compatible free splits:',matches)
# Full binary-A5 character check reuses the neighboring universal representation-ring verifier.
import runpy
from pathlib import Path
ring=runpy.run_path(str(Path(__file__).with_name('verify_negative_vertex_scalar.py')))
va,vm,vs=ring['vadd'],ring['vmul'],ring['vscale']
UU,NN,WWp,LL2=[ring[x] for x in ('H','N','Wp','L2')]
fc={-1:vs(-1,NN),0:va(vm(WWp,LL2),vs(-1,NN)),1:vs(-1,vm(WWp,UU)),2:WWp}
full={}
for t in (2,3):
 chi=vs(-1,ring['ambient_sym'](t))
 for i,ri in fc.items():
  for j,rj in fc.items(): chi=va(chi,vm(vm(ri,rj),ring['ambient_sym'](t+1+i+j)))
 full[t]=vs(-1,chi)
expected2={'one':0,'A':1,'V':2,'P':3,'D':4,'W':2,'Wp':2,'S':3,'T':4}
expected3={'one':1,'A':4,'V':2,'P':3,'D':3,'W':0,'Wp':3,'S':3,'T':6}
for t,expected in ((2,expected2),(3,expected3)):
 for name,n in expected.items(): assert ring['inner'](ring[name],full[t])==ring['z'](n)
print('PASS: full actual H1 B2/B3 character decompositions.')
# The j=2 example with generator weight0 has H0 torsion Ind(chi0+chi2).
# H0(C_lin)=1+3A+V+2P+2D; the free candidate O(2)+P O has H0=A+P.
H0C={'one':1,'A':3,'V':1,'P':2,'D':2}
ind0={'one':1,'A':1,'V':1,'P':0,'D':1}
ind2={'one':0,'A':1,'V':0,'P':1,'D':1}
free={'one':0,'A':1,'V':0,'P':1,'D':0}
assert all(ind0[k]+ind2[k]+free[k]==H0C[k] for k in H0C)
assert vecadd(base,unit(4),vecneg(unit(0)))==possible_free['O2 + 4']
print('PASS: j=2 remains compatible with both local C5 and full global A5 characters; no actual j is determined.')

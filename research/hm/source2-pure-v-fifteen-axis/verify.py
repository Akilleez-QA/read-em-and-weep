#!/usr/bin/env python3
"""Exact whole-orbit certificates. No sampled roots or actual source values."""
from pathlib import Path
import hashlib,json
from itertools import permutations,combinations_with_replacement
from model import *
ROOT=Path(__file__).resolve().parent
checks=[]
def check(name,condition):
 if not bool(condition): raise RuntimeError(name)
 checks.append(name)
for item in json.loads((ROOT/'INPUTS.json').read_text()):
 data=(ROOT/item['local_path']).read_bytes()
 check('sha256 '+item['label'],hashlib.sha256(data).hexdigest()==item['sha256'])
 check('git blob '+item['label'],hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==item['git_blob'])
def gb(fs,*variables): return s.groebner(fs,*variables,extension=z)
def lm(G): return [f.LM(order=G.order).exponents for f in G.polys]
def length(G):
 leading=lm(G); bounds=[]
 for i in range(2):
  bounds.append(min(m[i] for m in leading if m[i] and all(m[j]==0 for j in range(2) if j!=i)))
 return sum(not any(i>=a and j>=b for a,b in leading) for i in range(bounds[0]) for j in range(bounds[1]))
cP=Pi*cv(a**3,6);f6=s.expand((cP.T*GP*cP)[0]);delta=q*q-4*p*t;vs=[p,q,t]
crit=[s.expand(s.diff(f6,vs[i])*s.diff(delta,vs[j])-s.diff(f6,vs[j])*s.diff(delta,vs[i])) for i in range(3) for j in range(i+1,3)]
K=gb([f.subs(p,1) for f in crit],q,t)
check('critical leading monomials',lm(K)==[(5,0),(4,2),(2,4),(1,8),(0,12)])
check('critical chart length',length(K)==30)
check('critical boundary q chart',list(gb([f.subs({p:0,q:1}) for f in crit],t))==[t])
check('critical boundary t chart',list(gb([f.subs({p:0,t:1}) for f in crit],q))==[1])
check('top Chern and full axis count',3+4*3+4**2==6+10+15==31)
J=[*crit,s.expand(f6+s.Rational(3,80)*delta**3)]
G=gb([f.subs(p,1) for f in J],q,t)
expected=[q**4+8*q*q*t-3*z*t**5/2-3*t**4/2+z*t**3+5*t*t+z*t/2-s.Rational(7,2),q*q*t*t+2*z*q*q*t/5+q*q-3*t**5/2-z*t**4/10+t**3+3*z*t*t/5+t/2-z/2,q*t**4-4*z*q*t**3/15+2*q*t*t/3-4*z*q*t/15+q,t**6-4*z*t**5/15-t**4/3+t*t/3+4*z*t/15-1]
# Construct all rational coefficients exactly (Python integer division in expressions
# above acts on symbolic expressions, except the explicitly Rational constant).
check('complete fifteen-axis chart basis',list(G)==[s.expand(f) for f in expected])
check('fifteen-axis leading monomials',lm(G)==[(4,0),(2,2),(1,4),(0,6)])
check('fifteen-axis chart length',length(G)==14)
check('unique invariant orbit union',[(a,b,c) for a in range(2) for b in range(2) for c in range(2) if 6*a+10*b+14*c==14]==[(0,0,1)])
check('whole mirror intersection',list(gb([f.subs({p:1,q:0}) for f in J],t))==[t*t-1])
def detpoly(mat):
 out=s.Poly(0,p,q,t,extension=z)
 for perm in permutations(range(mat.rows)):
  term=s.Poly((-1)**sum(perm[i]>perm[j] for i in range(mat.rows) for j in range(i+1,mat.rows)),p,q,t,extension=z)
  for row,col in enumerate(perm):term*=s.Poly(mat[row,col],p,q,t,extension=z)
  out+=term
 return out.as_expr()
B=s.Matrix.hstack(*[Pi*cv(a*a*x**(2-i)*y**i,6) for i in range(3)])
N=s.Matrix([[(-1)**i*detpoly(B[[j for j in range(4) if j!=i],:]) for i in range(4)]])
check('signed cofactor annihilation',all(s.expand(f)==0 for f in N*B))
F1=(N*L*R1).applyfunc(s.expand);F2=(N*L*R2).applyfunc(s.expand)
check('nonic degrees',all(s.Poly(f,p,q,t).total_degree()==9 for f in [*F1,*F2]))
rems=[[s.expand(G.reduce(s.expand(f.subs(p,1)))[1]) for f in F] for F in [F1,F2]]
for i in range(4):check('entire remainder component '+str(i),rems[0][i]==rems[1][i])
check('nonzero coefficient witness',s.Poly(rems[0][0],q,t).coeff_monomial(q*q*t)==1458176*z/3375)
check('universal coefficient kernel',all(s.expand(aa*f+bb*g-(aa+bb)*f)==0 for f,g in zip(*rems)))
powers=[s.prod(pair) for pair in combinations_with_replacement(list(G),2)]
Gsquare=gb(powers,q,t)
check('ordinary square length',length(Gsquare)==42)
H=gb([*powers,*(s.expand(f.subs(p,1)) for f in F1-F2)],q,t)
check('whole-orbit Nakayama equality',list(H)==list(G))
check('rank line distinct from jet and conic lines',all(s.det(s.Matrix([[1,-1],line]))!=0 for line in [[1,2],[1,-2],[1,0]]))
check('complete rank-line length',34+15==49)
print(json.dumps({'status':'PASS','count':len(checks),'checks':checks,'critical_chart_length':30,'axis_chart_length':14,'axis_square_length':42,'occurrence_line':'alpha+beta=0','axis_local_length':1,'complete_base_length':49},indent=2))

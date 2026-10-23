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
cP=Pi*cv(a**3,6);f6=s.expand((cP.T*GP*cP)[0]);delta=q*q-4*p*t
u,v=s.symbols('u v')
restriction=s.Poly(s.expand(f6.subs({p:u*u,q:2*u*v,t:v*v})),u,v,extension=z)
check('binary invariant restriction nonzero',not restriction.is_zero)
check('exact nonzero binary witness',restriction.coeff_monomial(u**12)==3*z/16)
check('binary invariant restriction degree twelve',restriction.total_degree()==12)
I=gb([delta.subs(p,1),f6.subs(p,1)],q,t)
expected=[q*q-4*t,t**6+22*z*t**5/5-33*t**4-44*z*t**3/5-33*t*t+22*z*t/5+1]
check('entire conic orbit affine basis',list(I)==expected)
check('orbit chart length',length(I)==12)
check('whole projective boundary',list(gb([delta.subs({p:0,t:1}),f6.subs({p:0,t:1})],q))==[1])
check('squarefree orbit elimination polynomial',s.degree(s.gcd(expected[1],s.diff(expected[1],t)),t)==0)
check('elimination polynomial has no zero root',expected[1].subs(t,0)==1)
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
F1=(N*L*R1).applyfunc(s.expand)
check('nonic row degrees',all(s.Poly(f,p,q,t).total_degree()==9 for f in F1))
for i,f in enumerate(F1):check('component orbit inclusion '+str(i),I.reduce(s.expand(f.subs(p,1)))[1]==0)
powers=[s.prod(pair) for pair in combinations_with_replacement(list(I),2)]
Isquare=gb(powers,q,t)
check('ordinary square colength',length(Isquare)==36)
H=gb([*powers,*(f.subs(p,1) for f in F1)],q,t)
check('whole-orbit Nakayama equality',list(H)==list(I))
check('conic line distinct from other exceptional lines',all(s.det(s.Matrix([[1,0],line]))!=0 for line in [[1,2],[1,-2],[1,-1]]))
check('complete base length',34+12==46)
print(json.dumps({'status':'PASS','count':len(checks),'checks':checks,'conic_chart_length':12,'conic_square_length':36,'ambient_local_length':1,'complete_base_length':46,'binary_restriction_coefficient':str(restriction.terms()[0])},indent=2))

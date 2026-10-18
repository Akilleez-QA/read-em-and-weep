#!/usr/bin/env python3
"""Invented free words only; no production imports or physical evaluations."""
from fractions import Fraction as Q
from collections import defaultdict
import json
import ast
import hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parent
for name,digest in json.loads((ROOT/'pins.json').read_text()).items():
 if hashlib.sha256((ROOT/name).read_bytes()).hexdigest()!=digest:raise RuntimeError('Input pin mismatch: '+name)
tree=ast.parse((ROOT/'inputs/raw_engine.py.txt').read_text())
qnodes=[n for n in ast.walk(tree) if isinstance(n,ast.FunctionDef) and n.name=='q']
expected=ast.parse('def q(self,a,b,d):return self.ex.scalar(((b.legal_mask>>d)&1)-((a.legal_mask>>d)&1))*(self.y[d]/self.x[d])').body[0]
if len(qnodes)!=1 or ast.dump(qnodes[0])!=ast.dump(expected):raise RuntimeError('Physical q support formula changed')

def clean(x): return {m:c for m,c in x.items() if c}
def add(*xs):
 d=defaultdict(Q)
 for x in xs:
  for m,c in x.items(): d[m]+=c
 return clean(d)
def scale(x,c): return clean({m:v*c for m,v in x.items()})
def neg(x): return scale(x,-1)
def mul(x,y):
 d=defaultdict(Q)
 for (s,w),c in x.items():
  for (t,v),e in y.items(): d[(tuple(sorted(s+t)),w+v)]+=c*e
 return clean(d)
def atom(n,scalar=False):return {(((n,()),),()) if scalar else ((),((n,()),)):Q(1)}
def deriv(x,r):
 d=defaultdict(Q)
 for (s,w),c in x.items():
  for seq,other,isscalar in [(s,w,True),(w,s,False)]:
   for j,(n,J) in enumerate(seq):
    z=seq[:j]+((n,tuple(sorted(J+(r,)))),)+seq[j+1:]
    m=(tuple(sorted(z)),other) if isscalar else (other,z)
    d[m]+=c
 return clean(d)
def mu(x,y,p):
 a,b=p
 return scale(add(mul(deriv(x,a),deriv(y,b)),neg(mul(deriv(x,b),deriv(y,a)))),Q(1,2))
p=(0,1);q=(2,3)
def mix(x,y):
 out={}
 for a,b,sg in [(0,1,1),(1,0,-1)]:
  for c,d,tg in [(2,3,1),(3,2,-1)]:out=add(out,scale(mul(deriv(deriv(x,a),c),deriv(deriv(y,b),d)),Q(sg*tg,4)))
 return out
G={'01':atom('a'),'12':atom('b'),'23':atom('c')}
G['02']=mul(G['12'],G['01']);G['13']=mul(G['23'],G['12']);G['03']=mul(G['23'],G['02'])
B={r:{t:atom('b'+str(r)+t,True) for t in ['012','023','123']} for r in range(2)}
for r in range(2):B[r]['013']=add(B[r]['012'],B[r]['023'],neg(B[r]['123']))
U={r:{e:atom('u'+str(r)+e) for e in ['01','12','23']} for r in range(2)}
def first(r,t):
 i,j,k=t;a=i+j;b=j+k;c=i+k
 return add(mul(U[r][b],G[a]),mul(G[b],U[r][a]),mu(G[b],G[a],[p,q][r]),neg(mul(B[r][t],G[c])))
for r in range(2):
 for t in ['012','123','023']:U[r][t[0]+t[2]]=first(r,t)
 if U[r]['03']!=first(r,'013'):raise RuntimeError('First-order tetrahedron failure')
def defect(t):
 i,j,k=t;a=i+j;b=j+k;c=i+k
 return add(mul(U[0][b],U[1][a]),mul(U[1][b],U[0][a]),mu(U[1][b],G[a],p),mu(U[0][b],G[a],q),mu(G[b],U[1][a],p),mu(G[b],U[0][a],q),mix(G[b],G[a]),neg(mul(B[0][t],U[1][c])),neg(mul(B[1][t],U[0][c])),neg(mul(mul(B[0][t],B[1][t]),G[c])))
D={t:defect(t) for t in ['012','013','023','123']}
left=add(mul(G['23'],D['012']),neg(mul(D['123'],G['01'])),D['023'],neg(D['013']))
anomaly={}
for r,pair in [(1,p),(0,q)]:
 anomaly=add(anomaly,mul(mu(G['23'],B[r]['012'],pair),G['02']),neg(mul(G['13'],mu(B[r]['123'],G['01'],pair))))
if add(left,anomaly):raise RuntimeError('Exact mixed Bianchi identity failed')
def support(x):
 return clean({m:c for m,c in x.items() if not any(n.startswith('b') and n[1:2] in ['0','1'] and any(j not in ([0,1] if n[1]=='0' else [2,3]) for j in J) for n,J in m[0])})
if support(anomaly) or support(left):raise RuntimeError('Complementary support failed')
if not anomaly:raise RuntimeError('Noncentral anomaly negative control vacuous')
# The ten baseline terms must all be retained in the derivation.
mutated=add(left,mul(mul(B[0]['023'],B[1]['023']),G['03']))
if not add(mutated,anomaly):raise RuntimeError('Missing-gerbe mutation not rejected')

# Independent negative controls, all in the invented free algebra.
if not add(left,neg(anomaly)):raise RuntimeError('Anomaly-sign mutation escaped')
# Change the coefficient of the four mixed derivative monomials on one face.
if not add(left,anomaly,mix(G['12'],G['01'])):raise RuntimeError('Mixed coefficient mutation escaped')
if mul(atom('a'),atom('b'))==mul(atom('b'),atom('a')):raise RuntimeError('Word order collapsed')

# Formal nilpotent specialization: (z0 exponent, z1 exponent, N exponent).
# N^2=0; these are invented symbols, not physical matrices or source values.
def tmul(a,b):
 out=defaultdict(Q)
 for (i,j,k),v in a.items():
  for (l,m,n),w in b.items():
   if k+n<2:out[(i+l,j+m,k+n)]+=v*w
 return clean(out)
one={(0,0,0):Q(1)}; nn={(0,0,1):Q(1)}
def toy_atom(n,J):
 if n in ['a','b']:return one if not J else {}
 if n=='c':
  if not J:return add(one,{(1,0,1):Q(1)})
  return nn if J==(0,) else {}
 if n=='b1012':
  if not J:return {(0,1,0):Q(1)}
  return one if J==(1,) else {}
 if n.startswith('b'):return {}
 raise RuntimeError('Unexpected formal atom in toy control: '+n)
def toy_eval(expr):
 out={}
 for (s,w),coef in expr.items():
  val={(0,0,0):coef}
  for n,J in s+w:val=tmul(val,toy_atom(n,J))
  out=add(out,val)
 return out
toy_normalized=tmul(add(one,{(1,0,1):Q(-1)}),toy_eval(anomaly))
if toy_normalized!={(0,0,1):Q(1,2)}:raise RuntimeError('Traceless anomaly control failed')
# Trace is 2 on the scalar part and zero on every N term.
toy_trace={m:2*c for m,c in toy_normalized.items() if m[2]==0}
if toy_trace or not toy_normalized:raise RuntimeError('Trace projection countercontrol failed')

print(json.dumps({'status':'PASS','first_order_tetrahedron':True,'mixed_bianchi_exact':True,'arbitrary_gerbe_anomaly_terms':len(anomaly),'complementary_support_closure':True,'omitted_gerbe_mutation_rejected':True,'traceless_noncentral_countercontrol':True,'anomaly_sign_mutation_rejected':True,'mixed_coefficient_mutation_rejected':True,'word_order_control':True,'production_imports':False,'physical_evaluations':False},indent=2))

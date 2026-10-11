#!/usr/bin/env python3
"""Independent Laurent-Cech first-normal comparison; no producer code imports."""
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import hashlib,json

HERE=Path(__file__).resolve().parent
INPUT=HERE/'first_jet.json'
PIN='2be28aebeb2ff40754f17ca94f76b68eb40043f6492a1794bd91436bc27e1f10'
if hashlib.sha256(INPUT.read_bytes()).hexdigest()!=PIN:raise ValueError('Unpinned first jet')
data=json.loads(INPUT.read_text())
checks=[]

def add(*ps):
 out={}
 for p in ps:
  for e,c in p.items():
   out[e]=out.get(e,Q(0))+c
   if not out[e]:del out[e]
 return out

def scale(p,c):return {e:v*c for e,v in p.items() if v*c}
def mul(p,q):
 out={}
 for e,a in p.items():
  for f,b in q.items():
   k=tuple(x+y for x,y in zip(e,f));out[k]=out.get(k,Q(0))+a*b
   if not out[k]:del out[k]
 return out

def mono(z=0,X=0,Y=0,W=0,c=1):return {(z,X,Y,W):Q(c)} if c else {}
def shift(p,z=0,X=0,Y=0,W=0,c=1):return mul(p,mono(z,X,Y,W,c))
def power(p,n):
 out=mono()
 for _ in range(n):out=mul(out,p)
 return out

def neg(p):return scale(p,-1)
def vadd(*vs):return [add(*(v[i] for v in vs)) for i in range(len(vs[0]))]
def vscale(v,p):return [mul(q,p) for q in v]
def cross(u,v):return [add(mul(u[1],v[2]),neg(mul(u[2],v[1]))),add(mul(u[2],v[0]),neg(mul(u[0],v[2]))),add(mul(u[0],v[1]),neg(mul(u[1],v[0])))]
def dot(u,v):return add(*(mul(p,q) for p,q in zip(u,v)))
def zero(label,p):
 if p:raise ValueError((label,p))
 checks.append(label)

def vzero(label,v):
 for i,p in enumerate(v):zero(label+':'+str(i),p)

def delta(c,degree):
 out={}
 for ij in combinations(range(3),degree+2):
  p=add(*(scale(c.get(ij[:i]+ij[i+1:],{}),(-1)**i) for i in range(len(ij))))
  if p:out[ij]=p
 return out

def hom(c):
 out={}
 for ij,p in c.items():
  for e,v in p.items():
   choices=[i for i in range(3) if e[i+1]>=0]
   if choices and choices[0] in ij:
    q=choices[0];key=tuple(j for j in ij if j!=q)
    out[key]=add(out.get(key,{}),{e:v*(-1)**ij.index(q)})
 return {k:v for k,v in out.items() if v}

def pi(p):return {e:c for e,c in p.items() if all(x<0 for x in e[1:])}
def vdelta(c,degree):
 ds=[delta({k:v[i] for k,v in c.items()},degree) for i in range(4)]
 keys=set().union(*(d.keys() for d in ds));return {k:[d.get(k,{}) for d in ds] for k in keys}

def vhom(c):
 hs=[hom({k:v[i] for k,v in c.items()}) for i in range(4)]
 keys=set().union(*(d.keys() for d in hs));return {k:[h.get(k,{}) for h in hs] for k in keys}

def regular(label,c):
 for ij,p in c.items():
  for e in p:
   if any(e[k+1]<0 for k in range(3) if k not in ij):raise ValueError(('Nonregular',label,ij,e))
 checks.append(label+':regular')

def vregular(label,c):
 for j in range(4):regular(label+':'+str(j),{k:v[j] for k,v in c.items()})

z,X,Y,W=[mono(**{v:1}) for v in ['z','X','Y','W']]
S=add(power(X,2),power(Y,2));F=mul(X,Y);a=add(power(X,3),power(Y,3));w=power(W,6)
g=add(S,neg(mul(z,power(W,2))));C=add(power(S,2),mul(z,mul(S,power(W,2))),mul(power(z,2),power(W,4)))
T=add(scale(S,-3),scale(F,2));rF=[neg(a),w,neg(g),F];rI=[neg(a),power(S,3),neg(shift(g,z=-1)),F]
TOP=(0,1,2);PAIRS=list(combinations(range(3),2));Z4=[{},{},{},{}]

def trans(v):return [shift(v[0],z=3),add(v[1],shift(mul(C,v[2]),z=1)),shift(v[2],z=4),shift(v[3],z=3)]

SLOTS=list(combinations(range(4),2))+[(i,i) for i in range(4)]
def tensor(records):
 out={}
 for rec in records:
  v={}
  for ij,e,c in rec['terms']:
   key=tuple(ij);v[key]=add(v.get(key,{}),{tuple(e):Q(c)})
  out[tuple(rec['open'])]=v
 return out

def ta(*qs):return {ij:add(*(q.get(ij,{}) for q in qs)) for ij in SLOTS}
def tn(q):return {ij:neg(p) for ij,p in q.items()}
def td(c,degree):
 out={}
 for opened in combinations(range(3),degree+2):
  out[opened]=ta(*({ij:scale(p,(-1)**j) for ij,p in c.get(opened[:j]+opened[j+1:],{}).items()} for j in range(len(opened))))
 return out

def transport_tensor(q):
 cols=[{0:mono(z=3)},{1:mono()},{1:shift(C,z=1),2:mono(z=4)},{3:mono(z=3)}]
 out={}
 for (i,j),p in q.items():
  for k,x in cols[i].items():
   for l,y in cols[j].items():
    slot=tuple(sorted((k,l)));out[slot]=add(out.get(slot,{}),shift(mul(p,mul(x,y)),z=-4))
 return out

def quotient_tensor(q,r,label):
 xx=[{}, {}, {}, shift(q.get((3,3),{}),X=-1,Y=-1)]
 for i in range(3):xx[i]=shift(add(q.get((i,3),{}),neg(mul(r[i],xx[3]))),X=-1,Y=-1)
 for i,j in SLOTS:
  expected=mul(r[i],xx[j]) if i==j else add(mul(r[i],xx[j]),mul(r[j],xx[i]))
  zero(label+':'+str((i,j)),add(q.get((i,j),{}),neg(expected)))


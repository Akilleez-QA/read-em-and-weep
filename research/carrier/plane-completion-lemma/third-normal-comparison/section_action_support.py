#!/usr/bin/env python3
"""Generic exact tensor action, extracted from the frozen order-two checker."""
from fractions import Fraction as Q
from pathlib import Path
import hashlib,json
from itertools import combinations_with_replacement
import first_order_support as n

HERE=Path(__file__).resolve().parent
PIN='c03a36fca19b7a73b8c483c7dc9e2a17f4a1ea422e9a61972966b734cd5597e4'
source=HERE/'certificate.json'
if hashlib.sha256(source.read_bytes()).hexdigest()!=PIN:raise ValueError('Second primitive input hash mismatch')
cert=json.loads(source.read_text())
checks=[]

def zero(label,p):
 if p:raise ValueError((label,p))
 checks.append(label)

def vzero(label,v):
 for i,p in enumerate(v):zero(label+':'+str(i),p)

def tensor_zero_mod_relation(q,r,label):
 xx=[{}, {}, {}, n.shift(q.get((3,3),{}),X=-1,Y=-1)]
 for i in range(3):xx[i]=n.shift(n.add(q.get((i,3),{}),n.neg(n.mul(r[i],xx[3]))),X=-1,Y=-1)
 for i,j in n.SLOTS:
  expected=n.mul(r[i],xx[j]) if i==j else n.add(n.mul(r[i],xx[j]),n.mul(r[j],xx[i]))
  zero(label+':'+str((i,j)),n.add(q.get((i,j),{}),n.neg(expected)))

def cert_tensor(records):
 result={}
 for rec in records:
  q={}
  for ex,c in rec['terms']:
   inds=[i for i,k in enumerate(ex[4:]) for _ in range(k)]
   if len(inds)!=2:raise ValueError('Not quadratic primitive')
   ij=tuple(inds);q[ij]=n.add(q.get(ij,{}),{tuple(ex[:4]):Q(c)})
  result[tuple(rec['open'])]=q
 return result

def tscale(q,c):return {ij:n.scale(v,c) for ij,v in q.items()}
def omega(i,j,inf):
 if i==j:return {}
 if i>j:return n.neg(omega(j,i,inf))
 return {(1,2):n.F,(1,3):n.shift(n.g,z=-1) if inf else n.g,(2,3):n.power(n.S,3) if inf else n.w}.get((i,j),{})

def bracket(p,q,inf):
 out={}
 for (i,j),v in p.items():
  for (k,l),w in q.items():
   vw=n.mul(v,w)
   for u1,u2,a,b in [(j,l,i,k),(j,k,i,l),(i,l,j,k),(i,k,j,l)]:
    ij=tuple(sorted((u1,u2)));out[ij]=n.add(out.get(ij,{}),n.mul(vw,omega(a,b,inf)))
 return out

def act(q,vec,d,inf,patch):
 lam=(n.LI if inf else n.LF)[patch]
 psi=[n.mono()]+[n.mul(n.a,p) for p in lam]
 pairing=[n.add(*(n.mul(omega(i,j,inf),vec[j]) for j in range(4)),n.mul(psi[i],d)) for i in range(4)]
 out=[{},{},{},{}]
 for (i,j),p in q.items():
  out[i]=n.add(out[i],n.mul(p,pairing[j]));out[j]=n.add(out[j],n.mul(p,pairing[i]))
 return out


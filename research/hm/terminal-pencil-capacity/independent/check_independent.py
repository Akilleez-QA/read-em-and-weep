#!/usr/bin/env python3
"""Independent direct-product controls for universal pencil coefficient solver."""
import importlib.util, json, hashlib
from pathlib import Path
from fractions import Fraction
P=Path(__file__).resolve().parent.parent
spec=importlib.util.spec_from_file_location('subject', P/'verify.py'); s=importlib.util.module_from_spec(spec);spec.loader.exec_module(s)
count=0

def check(ok, msg):
 global count
 count+=1
 if not ok: raise RuntimeError(msg)

def standard(m,d):
 return [[int(j==i+d) for j in range(m)] for i in range(m-1)]

def product(a,b,ncols):
 return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a] if b else [[0]*ncols for row in a]

def direct(n,m,v):
 f=[v[i*n:(i+1)*n] for i in range(m)]
 g=[v[m*n+i*(n-1):m*n+(i+1)*(n-1)] for i in range(m-1)]
 out=[]
 for d in (0,1):
  left=product(standard(m,d),f,n)
  right=product(g,standard(n,d),n)
  out.extend(x-y for a,b in zip(left,right) for x,y in zip(a,b))
 return out

for n in range(1,8):
 for m in range(1,11):
  rows,nv=s.general_equations(n,m)
  # This full test vector is not a point in the pencil parameter space.
  v=[Fraction((i*7+3)%11-5,(i%3)+1) for i in range(nv)]
  check([sum(a*b for a,b in zip(row,v)) for row in rows]==direct(n,m,v),'operator versus direct coefficient matrix products')
  basis=s.nullspace(rows,nv)
  check(len(basis)==max(n-m+1,0),'dimension extended rectangle')
  check(all(not any(direct(n,m,b)) for b in basis),'basis direct coefficient product')

# General E2^r equation assembly crosscheck using independently assembled block matrices.
for r in (1,2,3,8):
 for m in (1,2,3,8,16):
  rows,nv,nf=s.equations(m,r)
  v=[Fraction((i*5+1)%13-6,2) for i in range(nv)]
  f=[v[i*2*r:(i+1)*2*r] for i in range(m)]
  g=[v[nf+i*r:nf+(i+1)*r] for i in range(m-1)]
  direct_rows=[]
  for d in (0,1):
   a=[[int(j==2*i+d) for j in range(2*r)] for i in range(r)]
   left=product(standard(m,d),f,2*r);right=product(g,a,2*r)
   direct_rows.extend(x-y for aa,bb in zip(left,right) for x,y in zip(aa,bb))
  check([sum(a*b for a,b in zip(row,v)) for row in rows]==direct_rows,'multiple source coefficient assembly')

for bad in [(0,1),(17,1),(1,0),(1,9)]:
 try:s.equations(*bad)
 except ValueError:check(True,'size rejection')
 else:check(False,'missing size rejection')
try:s.nullspace([[1,2]],1)
except ValueError:check(True,'ragged rejection')
else:check(False,'missing ragged rejection')
for args in [([2],2,[]),([2],2,[[1]]),([0],1,[])]:
 try:s.split_terminal_matrix(*args)
 except ValueError:check(True,'split malformed rejection')
 else:check(False,'missing split malformed rejection')
check(s.nullspace([],3)==[[Fraction(int(i==j)) for i in range(3)] for j in range(3)],'empty equation system')
check(s.nullspace([[1,0],[0,1]],2)==[],'zero kernel')
print(json.dumps({'independent_checks':count,'scope':'direct full-coefficient universal matrix products; no actual HM source or selected direction','proof_sha256':hashlib.sha256((P/'PROOF.md').read_bytes()).hexdigest(),'verifier_sha256':hashlib.sha256((P/'verify.py').read_bytes()).hexdigest()},indent=2,sort_keys=True))

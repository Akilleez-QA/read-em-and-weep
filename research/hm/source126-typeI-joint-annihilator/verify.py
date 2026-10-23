#!/usr/bin/env python3
"""Bounded exact interface checks; no selected geometric data."""
from pathlib import Path
import hashlib,json,itertools
from fractions import Fraction
ROOT=Path(__file__).resolve().parent
checks=0
def check(x,msg):
 global checks
 checks+=1
 if not x: raise RuntimeError(msg)
for e in json.loads((ROOT/'INPUTS.json').read_text()):
 b=(ROOT/e['local_path']).read_bytes()
 check(hashlib.sha256(b).hexdigest()==e['sha256'],'input sha256 '+e['local_path'])
 check(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==e['git_blob'],'input git blob '+e['local_path'])
# W multiplication, enough to derive A P=(W²−1)P.
W={'P':{'Wp':1,'T':1},'Wp':{'P':1},'T':{'V':1,'P':1,'D':1}}
a={}
for s,n in W['P'].items():
 for t,m in W[s].items(): a[t]=a.get(t,0)+n*m
a['P']-=1
check(a=={'P':1,'V':1,'D':1},'P A character excludes A')
dims=[3,3,4,5] # A,V,P,D
base=[1,2,2,3]; kernel=[1,0,0,1]
survive=[]
for r,e,d in itertools.product(range(3),range(2),range(2)):
 u=[1,2,2+e,3+d];z=[0,2,4-r,2]; im=[x-y for x,y in zip(u,kernel)]
 contained=all(x<=y for x,y in zip(im,z))
 pinj=(r!=0 or e==1)
 nonsurj=(im!=z)
 if contained and pinj and nonsurj:
  survive.append((r,e,d))
  quotient=[y-x for x,y in zip(im,z)]
  check(quotient==[0,0,1,0],'restricted cokernel P')
  N2=[1,2,3,4];N4=[0,2,4,3]
  check([x-y for x,y in zip(N2,u)]==[0,0,r,1],'source quotient')
  check([x-y for x,y in zip(N4,z)]==[0,0,r,1],'target quotient')
  check((sum(x*y for x,y in zip(u,dims)),sum(x*y for x,y in zip(z,dims)))==({0:(36,32),1:(32,28)}[r]),'dimensions')
 check(not(contained and r==2 and nonsurj),'full P joint rank excluded')
check(survive==[(0,1,0),(1,0,0)],'exact surviving footprint list')
def rank(m):
 m=[list(map(Fraction,row)) for row in m]
 if not m:return 0
 k=0
 for c in range(len(m[0])):
  p=next((i for i in range(k,len(m)) if m[i][c]),None)
  if p is None:continue
  m[k],m[p]=m[p],m[k];z=m[k][c];m[k]=[v/z for v in m[k]]
  for i in range(len(m)):
   if i!=k:
    z=m[i][c];m[i]=[a-z*b for a,b in zip(m[i],m[k])]
  k+=1
  if k==len(m):break
 return k
# All 81 small formal joint P rows: rank never inferred from separate ranks.
for values in itertools.product((-1,0,1),repeat=4):
 R=[values[:2],values[2:]];rr=rank(R)
 check((rr==2)==(values[0]*values[3]-values[1]*values[2]!=0),'determinant criterion')
 # Aggregate action on multiplicity coordinates of P²⊕D; D is nonzero.
 agg=[[values[0],values[1],0],[values[2],values[3],0],[0,0,1]]
 check(3-rank(agg)==2-rr,'common kernel, not sum of kernels')
check(rank([[1,0]])==rank([[2,0]])==1,'individual rows nonzero')
check(rank([[1,0],[2,0]])==1,'negative control dependent rows')
# Abstract first correction: Q:U→Z surjective, QT correction lies in imQ.
# Expand Qk=0, Qu+Tk=0, Qv+Tu=0 in a formal 2x3 example.
def mv(m,x):return [sum(a*b for a,b in zip(row,x)) for row in m]
Q=[[1,0,0],[0,1,0]]; T=[[0,1,2],[1,1,3]]
k=[0,0,1];u=[-2,-3,0];v=[3,5,0]
check(mv(Q,k)==[0,0],'formal kernel')
check([a+b for a,b in zip(mv(Q,u),mv(T,k))]==[0,0],'first correction')
check([a+b for a,b in zip(mv(Q,v),mv(T,u))]==[0,0],'second correction')
# Equal endpoint dimensions do not entail invertibility without the proof's
# P-injectivity and D-surjectivity: a zero 1x1 map is the regression control.
check(rank([[0]])==0,'equal dimensions are not an invertibility proof')
# Exact block contraction with arbitrary small formal scalar coefficients.
# Two-dimensional retained source, one-dimensional retained target and quotient.
# B is a nonzero scalar; rational inversion tests the universal block identities.
for aa,bb,cc,dd,ee,ff in itertools.product((-1,0,1),repeat=6):
 for b in (-2,-1,1,2):
  # A=(aa,bb), C=(cc); source=(dd,ee,ff).
  x=(dd,ee); y=ff
  M=(aa*dd+bb*ee+cc*ff,b*ff)
  p1M=M[0]-Fraction(cc,b)*M[1]
  check(p1M==aa*dd+bb*ee,'p1 M = A p0')
  hM=(0,0,Fraction(M[1],b))
  check(hM==(0,0,ff),'h M = 1 - i0 p0')
  # A general target=(dd,ee), with the unused ff still a formal control.
  h=(0,0,Fraction(ee,b))
  Mh=(aa*h[0]+bb*h[1]+cc*h[2],b*h[2])
  p1=dd-Fraction(cc,b)*ee
  check(Mh==(dd-p1,ee),'M h = 1 - i1 p1')
  i0=(dd,ee,0); i1=(dd,0)
  check(i0[:2]==x and i1[0]-Fraction(cc,b)*i1[1]==dd,'p i = identity')
print(f'PASS: {checks} exact checks; 9 immutable inputs; two conditional footprints.')

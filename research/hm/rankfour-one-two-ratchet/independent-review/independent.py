#!/usr/bin/env python3
"""Exact class-character reconstruction, with no production imports.

Only abstract bundle degree and representation arithmetic is used.
"""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations_with_replacement
from collections import Counter
import json, hashlib

ROOT=Path(__file__).resolve().parent
names=('1','W','A','S4','D','T6','P',"W'",'V')
dims=(1,2,3,4,5,6,4,2,3)
odd=(0,1,0,1,0,1,0,1,0)
ZERO=(0,)*9
RESIDUES=tuple(range(0,10,2))
checks=0
def check(b,msg):
 global checks
 checks+=1
 if not b:raise RuntimeError(msg)
def add(*vs):return tuple(sum(v[i] for v in vs) for i in range(9))
def scale(v,n):return tuple(x*n for x in v)
def sub(a,b):return add(a,scale(b,-1))
def unit(i):return tuple(int(j==i) for j in range(9))
def good(v):return min(v)>=0
def dimension(v):return sum(a*b for a,b in zip(v,dims))
def qa(a,b):return (a[0]+b[0],a[1]+b[1])
def qm(a,b):return (a[0]*b[0]+5*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def qs(a,n):return (a[0]*n,a[1]*n)
def qsum(xs):
 r=(0,0)
 for x in xs:r=qa(r,x)
 return r
tr=((2,0),(-2,0),(F(1,2),F(1,2)),(-F(1,2),-F(1,2)),(F(1,2),-F(1,2)),(-F(1,2),F(1,2)),(1,0),(-1,0),(0,0))
sz=(1,1,12,12,12,12,20,20,30)
@lru_cache(None)
def symmetric(n):
 if n==0:return ((1,0),)*9
 if n==1:return tr
 return tuple(qa(qm(t,x),qs(y,-1)) for t,x,y in zip(tr,symmetric(n-1),symmetric(n-2)))
chars=[symmetric(n) for n in range(6)]
chars.append(tuple((x,0) for x in (4,4,-1,-1,-1,-1,1,1,0)))
chars.append(tuple(qa(qm(t,p),qs(s,-1)) for t,p,s in zip(tr,chars[6],chars[5])))
chars.append(tuple(qa(x,qs(p,-1)) for x,p in zip(symmetric(6),chars[6])))
def inner(a,b):
 q=qsum(qs(qm(x,y),n) for x,y,n in zip(a,b,sz))
 check(q[1]==0 and q[0]%120==0,'integral exact character inner product')
 return int(q[0]/120)
@lru_cache(None)
def symtensor(i,n):
 c=tuple(qm(x,y) for x,y in zip(chars[i],symmetric(n)))
 v=tuple(inner(c,r) for r in chars)
 check(good(v) and dimension(v)==dims[i]*(n+1),'genuine symmetric tensor')
 return v
@lru_cache(None)
def h(B,t,k=0):
 return add(*(symtensor(i,e+t if k==0 else -e-t-2) for e,i in B if (e+t>=0 if k==0 else e+t<=-2)))
def chi(B,t):return sub(h(B,t),h(B,t,1))
def degree(B):return sum(e*dims[i] for e,i in B)
def ordinary(B):return tuple(sorted(e for e,i in B for _ in range(dims[i])))
def show(B):return [{'degree':e,'coefficient':names[i]} for e,i in B]
def parse(x):return tuple(sorted((p['degree'],names.index(p['coefficient'])) for p in x))
def hom(B,C):return sum(symtensor(j,e-f)[i] for f,i in B for e,j in C if e>=f)
SOURCES={
 'D':tuple(sorted(((-2,4),(-3,7),(-3,5),(-4,8),(-8,0)))),
 'P':tuple(sorted(((-2,6),(-3,7),(-3,5),(-4,8),(-5,7)))),
 'V':tuple(sorted(((-2,8),(-3,7),(-3,5),(-4,8),(-4,8)))),
 'Z':tuple(sorted(((-3,7),(-3,5),(-3,5),(-4,8)))),
}
E1=add(unit(7),scale(unit(5),3))
Q0=add(unit(2),scale(unit(8),2),scale(unit(6),3),scale(unit(4),4))
E3=add(unit(7),scale(unit(5),2))
@lru_cache(None)
def coefficient_types(n,p):
 out=[]
 def visit(start,left,ls):
  if not left:out.append(tuple(ls));return
  for i in range(start,9):
   if odd[i]==p and dims[i]<=left:visit(i,left-dims[i],ls+[i])
 visit(0,n,[])
 return out
@lru_cache(None)
def domain(rank,d,lo,hi,low=()):
 out=set()
 def visit(rem,dleft,lower,es):
  if rem==0:
   if dleft:return
   if low and any(x<y for x,y in zip(es,low)):return
   groups=list(Counter(es).items())
   def labels(k,bs):
    if k==len(groups):out.add(tuple(sorted(bs)));return
    e,n=groups[k]
    for ids in coefficient_types(n,e%2):labels(k+1,bs+[(e,i) for i in ids])
   labels(0,[]);return
  for e in range(lower,min(hi,dleft//rem)+1):
   if (rem-1)*e<=dleft-e<=(rem-1)*hi:visit(rem-1,dleft-e,e,es+[e])
 visit(rank,d,lo,[])
 return out
@lru_cache(None)
def strings(n,bound=3):
 if n==0:return ((),)
 return tuple((q,)+rest for q in range(1,min(n,bound)+1) for rest in strings(n-q,q))
def cap(B,n):
 ls=ordinary(B)[::-1]
 return max(sum(sum(ls[:q])-2*j*q for j,q in enumerate(row,1)) for row in strings(n))
def dual(B,t=0):return tuple(sorted((-e+t,i) for e,i in B))
def Qchi(t):
 return sub(add(*(scale(chi(((t-1,i),),0),n) for n,i in ((3,7),(3,3),(6,5)))),add(*(scale(chi(((t,i),),0),n) for n,i in ((1,2),(2,8),(3,6),(4,4)))))
def torsion(r,t):return sub(chi(((r+t,0),),0),chi(((r+t-12,0),),0))
def gap(N,D=22):
 target=N*(D-5*(N-5));w=[(N-5)*j if j<5 else 5*(N-j) for j in range(1,N)]
 reachable={0}
 for x in range(max(0,target)+1):
  if x in reachable:reachable.update(x+a*b for a in w for b in (12,20,30) if x+a*b<=target)
 return target,sorted(reachable)
def main():
 for rec in json.loads((ROOT/'INPUTS.json').read_text()):
  b=(ROOT/rec['file']).read_bytes()
  check(hashlib.sha256(b).hexdigest()==rec['sha256'],'input SHA256')
  check(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==rec['git_blob_sha1'],'input Git identity')
 for i in range(9):
  for j in range(9):check(inner(chars[i],chars[j])==int(i==j),'class orthonormality')
 for r in RESIDUES:
  for t in range(-12,13):check(good(torsion(r,t)) and dimension(torsion(r,t))==12,'length12 genuine torsion')
  check(tuple(torsion(r,t) for t in (0,1))==tuple(torsion(r+10,t) for t in (0,1)),'isotropy period10')
 check(len({tuple(torsion(r,t) for t in (0,1)) for r in RESIDUES})==5,'all five even stabilizer characters')
 sem={12*x+20*y+30*z for x in range(4) for y in range(3) for z in range(2) if 12*x+20*y+30*z<=42}
 ledger=[(a,-138+2*d1+d2-2*a,d1,d2,-54-a) for a in range(-60,-39,2) for d1 in sem for d2 in sem if -138+2*d1+d2-2*a<=-16]
 check(len(ledger)==49,'complete degree domain')
 all60=[];all18=[];counts={};stages={}
 for s,E in SOURCES.items():
  low=ordinary(E)[:4];full=set()
  for d in range(-14,7,2):full.update(domain(4,d,low[0],d-sum(low[:3]),low))
  predicates=[lambda B:good(sub(E1,h(B,1,1))),lambda B:good(sub(Q0,h(B,0))),lambda B:cap(B,13)>=-54-degree(B),lambda B:all(good(sub(chi(B,t),chi(E,t))) for t in range(3)),lambda B:good(sub(h(B,2),h(E,2))),lambda B:good(sub(h(E,3,1),h(B,3,1))),lambda B:good(sub(add(chi(B,3),h(B,1)),E3)),lambda B:good(sub(h(B,3),E3))]
  cs=[len(full)]
  for pred in predicates:full={B for B in full if pred(B)};cs.append(len(full))
  stages[s]=cs
  pairs=[(row,B) for row in ledger for B in sorted(full) if row[4]==degree(B) and row[1]<=cap(dual(B,-4),5)]
  counts[s]=[len(pairs),0,0,0,0]
  all60.extend((s,row,B) for row,B in pairs)
  for row,B in pairs:
   if any(not good(sub(add(*(h(B,t-2*j) for j in range(max(0,t+max(ordinary(E))+1)))),h(E,t))) for t in range(2,33)):continue
   counts[s][1]+=1
   a,b,d1,d2,d=row
   check(d1==0 and d2 in (0,12),'torsion-safe residue domain')
   for r in ([None] if d2==0 else RESIDUES):
    wanted=tuple(add(Qchi(t),chi(B,-t),chi(B,2-t),ZERO if r is None else torsion(r,-t)) for t in (0,1))
    for Z in sorted(domain(5,b,b+12,-3)):
     if tuple(chi(Z,t) for t in (0,1))!=wanted:continue
     counts[s][2]+=1
     target=dual(B,-6);bad=[]
     for block in Z:
      rest=list(Z);rest.remove(block)
      if hom((block,),target)==0 and hom((block,),tuple((e-2,i) for e,i in rest))==0:bad.append(block)
     status='rejected_horizontal'
     if not bad:
      counts[s][3]+=1
      forced=any(dims[c[1]]==1 and hom(Z,target[:j]+target[j+1:])==0 for j,c in enumerate(target))
      if forced and b==-22:status='rejected_rank_one'
      else:status='necessary_survivor';counts[s][4]+=1
     all18.append(dict(source=s,row=row,B=show(B),Z=show(Z),torsion_residue=r,status=status))
 check(counts=={'D':[35,31,12,7,3],'P':[14,6,2,0,0],'V':[5,2,2,0,0],'Z':[6,2,2,0,0]},'independent full pipeline')
 check(gap(8)==(56,[0,36]) and gap(9)==(18,[0]),'complete N8 and N9 gap sets')
 check(gap(9,20)[0] in gap(9,20)[1] and gap(9,36)[0] in gap(9,36)[1],'gap positive controls')
 # New complementary theorem: complete cubic kernel alternatives for B0.
 B0=((-8,0),(-3,7),(14,0));E=SOURCES['D']
 check(sub(chi(E,3),chi(B0,3))==scale(unit(7),-1),'exact kernel cubic Euler')
 check(sub(chi(E,4),chi(B0,4))==add(unit(4),scale(unit(8),2)),'exact kernel quartic Euler')
 alternatives=[];rejected=[];h1blocks=[]
 for top in (ZERO,unit(3)):
  required=add(top,unit(7));bound=4+dimension(required)
  choices=[(-j,i,symtensor(i,j-5)) for j in range(5,bound+1) for i in range(9) if odd[i]==j%2 and (j-4)*dims[i]<=dimension(required) and good(sub(required,symtensor(i,j-5)))]
  h1blocks.append({'top':top,'bound':bound,'blocks':show(tuple((e,i) for e,i,c in choices))})
  def visit(start,rem,bs):
   if rem==ZERO:
    base=tuple(bs)+(() if top==ZERO else ((-3,3),))
    R4=sub(sub(chi(E,4),chi(B0,4)),chi(base,4))
    if not good(R4):rejected.append({'base':show(base),'degree_minus_four_coefficient':R4});return
    K=tuple(sorted(base+tuple((-4,i) for i,n in enumerate(R4) for _ in range(n))))
    check(len(ordinary(K))==13 and degree(K)==-54,'kernel rank degree')
    check(K.count((-4,8))==2,'two V near-top copies')
    check(hom(((-4,8),),tuple((e-2,i) for e,i in B0))==1,'single derivative Hom multiplicity')
    rest=list(K);rest.remove((-4,8))
    check(hom(((-4,8),),tuple((e-2,i) for e,i in rest))==0,'zero internal derivative Hom')
    alternatives.append(show(K));return
   for j in range(start,len(choices)):
    e,i,c=choices[j]
    if good(sub(rem,c)):visit(j,sub(rem,c),bs+[(e,i)])
  visit(0,required,[])
 check(len(alternatives)==2 and len(rejected)==1,'complete kernel splitting domain')
 check(symtensor(0,16)[8]==1,'independent class V in Sym16')
 remaining=[x for x in all18 if x['status']=='necessary_survivor' and parse(x['B'])!=B0]
 check(len(remaining)==1,'one tuple after complementary cut')
 return {'claim':'Independent 60 to 18 to 7 to 3 reconstruction, plus new near-top kernel multiplicity cut to one necessary tuple. No profile closure.','checks':checks,'source_stage_counts':counts,'base_filter_counts':stages,'endpoint_tuples':all18,'kernel_H1_domains':h1blocks,'kernel_splittings':alternatives,'rejected_kernel_formal_splittings':rejected,'one_remaining':remaining,'actual_instances_evaluated':False,'forbidden_Qstar1_filter_used':False}
if __name__=='__main__':print(json.dumps(main(),indent=2,sort_keys=True))

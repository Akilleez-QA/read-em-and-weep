#!/usr/bin/env python3
"""Independent necessary arithmetic for the ACTUAL ORDERED (1,2) plateau.
No actual coefficients, instances, parameters, jets or matrices are evaluated.
"""
from pathlib import Path
from itertools import combinations_with_replacement
from functools import lru_cache
from collections import Counter
from fractions import Fraction
import hashlib,json
R=Path(__file__).resolve().parent
names=('1','W','A','S4','D','T6','P',"W'",'V')
dims=(1,2,3,4,5,6,4,2,3)
parity=(0,1,0,1,0,1,0,1,0)
edges=((0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(5,8))
zero=(0,)*9
checks=0
def check(ok,label):
 global checks
 checks+=1
 if not ok:raise ValueError(label)
def add(*xx):return tuple(sum(x[i]for x in xx)for i in range(9))
def scale(x,c):return tuple(c*v for v in x)
def sub(x,y):return add(x,scale(y,-1))
def basis(i):return tuple(int(i==j)for j in range(9))
def dimension(v):return sum(n*d for n,d in zip(v,dims))
def good(v):return all(x>=0 for x in v)
def W(v):
 out=[0]*9
 for i,j in edges:out[i]+=v[j];out[j]+=v[i]
 return tuple(out)
@lru_cache(None)
def sym_times(i,n):
 a,b=zero,basis(i)
 for j in range(n):a,b=b,sub(W(b),a)
 return b
@lru_cache(None)
def cohom(B,t,h):
 return add(*(sym_times(i,e+t if h==0 else -e-t-2)for e,i in B if (e+t>=0 if h==0 else e+t<=-2)))
def chi(B,t):return sub(cohom(B,t,0),cohom(B,t,1))
def ords(B):return tuple(sorted(e for e,i in B for j in range(dims[i])))
def show(B):return [{'degree':e,'coefficient':names[i]}for e,i in B]
def deg(B):return sum(e*dims[i]for e,i in B)
SOURCES={
'D':tuple(sorted(((-2,4),(-3,7),(-3,5),(-4,8),(-8,0)))),
'P':tuple(sorted(((-2,6),(-3,7),(-3,5),(-4,8),(-5,7)))),
'V':tuple(sorted(((-2,8),(-3,7),(-3,5),(-4,8),(-4,8)))),
'Z':tuple(sorted(((-3,7),(-3,5),(-3,5),(-4,8)))),
}
E1=add(basis(7),scale(basis(5),3))
Q0=add(basis(2),scale(basis(8),2),scale(basis(6),3),scale(basis(4),4))
E3=add(basis(7),scale(basis(5),2))
@lru_cache(None)
def coefficient_reps(rank,p):
 out=[]
 allowed=[i for i in range(9)if parity[i]==p and dims[i]<=rank]
 def rec(at,left,ls):
  if not left:out.append(tuple(ls));return
  for j in range(at,len(allowed)):
   i=allowed[j]
   if dims[i]<=left:rec(j,left-dims[i],ls+[i])
 rec(0,rank,[])
 return tuple(out)
def domain_ordinary(low,d):
 """First ordinary sorted degrees, then coefficient representations."""
 out=set();lo=low[0];hi=d-sum(low[:3])
 for es in combinations_with_replacement(range(lo,hi+1),4):
  if sum(es)!=d or any(a<b for a,b in zip(es,low)):continue
  groups=list(Counter(es).items())
  def rec(j,B):
   if j==len(groups):out.add(tuple(sorted(B)));return
   e,n=groups[j]
   for ids in coefficient_reps(n,e%2):rec(j+1,B+[(e,i)for i in ids])
  rec(0,[])
 return out
def domain_blocks(low,d):
 """Independently enumerate multisets of irreducible line-degree blocks."""
 lo=low[0];hi=d-sum(low[:3]);blocks=[(e,i)for e in range(lo,hi+1)for i in range(9)if dims[i]<=4 and parity[i]==e%2]
 out=set()
 def rec(at,left,degree,B):
  if left==0:
   if degree==d and all(a>=b for a,b in zip(ords(B),low)):out.add(tuple(B))
   return
  for j in range(at,len(blocks)):
   e,i=blocks[j];n=dims[i]
   if n<=left and degree+e*n+(left-n)*lo<=d<=degree+e*n+(left-n)*hi:rec(j,left-n,degree+e*n,B+[(e,i)])
 rec(0,4,0,[])
 return out
def heights(n):return tuple((x,y,n-x-y)for x in range(n+1)for y in range(x+1)if x>=y>=n-x-y>=0)
HEIGHTS=heights(13)
def capacity(B,n=13):
 ls=ords(B)[::-1][:3]
 return max(sum(h*l-h*(h+1)for h,l in zip(H,ls))for H in heights(n))
def strings(n,cap=3):
 if n==0:yield ();return
 for q in range(1,min(n,cap)+1):
  for tail in strings(n-q,q):yield(q,)+tail
def capacity_strings(B,n=13):
 ls=ords(B)[::-1][:3]
 return max(sum(sum(ls[:q])-2*j*q for j,q in enumerate(qs,1))for qs in strings(n))
# Exact independent class-valued arithmetic in Q(sqrt5).
def qa(x,y):return(x[0]+y[0],x[1]+y[1])
def qm(x,y):return(x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def qs(x,c):return(x[0]*c,x[1]*c)
def qsym(x,n):
 a,b=(0,0),(1,0)
 for j in range(n):a,b=b,qa(qm(x,b),qs(a,-1))
 return b
traces=((2,0),(-2,0),(Fraction(1,2),Fraction(1,2)),(-Fraction(1,2),-Fraction(1,2)),(Fraction(1,2),-Fraction(1,2)),(-Fraction(1,2),Fraction(1,2)),(1,0),(-1,0),(0,0))
sizes=(1,1,12,12,12,12,20,20,30)
chars=[tuple(qsym(t,n)for t in traces)for n in range(6)]
chars.append(tuple((x,0)for x in(4,4,-1,-1,-1,-1,1,1,0)))
chars.append(tuple(qa(qm(t,p),qs(s,-1))for t,p,s in zip(traces,chars[6],chars[5])))
chars.append(tuple(qa(qsym(t,6),qs(p,-1))for t,p in zip(traces,chars[6])))
def qsum(xs):
 a=(0,0)
 for x in xs:a=qa(a,x)
 return a
def controls():
 for i in range(9):
  for j in range(9):check(qsum(qs(qm(chars[i][c],chars[j][c]),sizes[c])for c in range(9))==(120*int(i==j),0),'independent character orthogonality')
  for n in range(33):
   v=sym_times(i,n)
   check(good(v)and dimension(v)==dims[i]*(n+1),'McKay positive character dimension')
   for c in range(9):check(qsum(qs(chars[j][c],v[j])for j in range(9))==qm(chars[i][c],qsym(traces[c],n)),'McKay versus exact classes')
 for S in SOURCES.values():
  check(len(ords(S))==17 and deg(S)==-54,'actual E rank degree')
  check(cohom(S,1,0)==zero and cohom(S,1,1)==E1,'actual source twist one')
  check(chi(S,3)==E3,'actual E cubic Euler')
 check(len(HEIGHTS)==len(tuple(strings(13))),'partition conjugation counts')
 # Torsion-safe ordered K0 relation, formal Laurent shifts in named terms.
 def shifted(poly,k):return Counter({(name,e+k):c for(name,e),c in poly.items()})
 B=Counter({('B',0):1});T1=Counter({('T1',0):1});T2=Counter({('T2',0):1})
 L2=shifted(B,2)+shifted(T1,2);L3=shifted(L2,2)+shifted(T2,2)
 check(L2+L3==Counter({('B',2):1,('B',4):1,('T1',2):1,('T1',4):1,('T2',2):1}),'actual ordered quotient torsion shifts')

def main():
 inputs=json.loads((R/'INPUTS.json').read_text())
 for x in inputs:
  b=(R/x['file']).read_bytes();check(hashlib.sha256(b).hexdigest()==x['sha256'],'original source SHA256');check(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==x['git_blob_sha1'],'original git object identity')
 controls()
 sem=sorted({12*x+20*y+30*z for x in range(4)for y in range(3)for z in range(2)if 12*x+20*y+30*z<=42})
 ledger=[]
 for d1 in sem:
  for d2 in sem:
   for a in range(-60,-38,2):
    b=-138+2*d1+d2-2*a
    if b>-16:continue
    d=-54-a
    check(a+d==-54 and a+d+(d+8+d1)+(d+16+d1+d2)==b,'ordered degree ledger')
    ledger.append((a,b,d1,d2,d))
 check(len(ledger)==49 and sum(x[2]+x[3]>0 for x in ledger)==38,'complete initial ledger')
 results={};all_surv=[]; simultaneous=[]
 for label,S in SOURCES.items():
  low=ords(S)[:4];full=set()
  for d in range(-14,7,2):
   first=domain_ordinary(low,d);second=domain_blocks(low,d)
   check(first==second,'independent full quotient domain '+label+str(d));full|=first
  current=full;counts=[['source_ordinary_domain',len(current)]]
  filters=[
   ('actual_E_twist1_H1_quotient',lambda B:good(sub(E1,cohom(B,1,1)))),
   ('actual_Qstar_twist0_H1_quotient',lambda B:good(sub(Q0,cohom(B,0,0)))),
   ('actual_endpoint_capacity',lambda B:capacity(B)>=-54-deg(B)),
   ('kernel_H0_twists012',lambda B:all(good(sub(chi(B,t),chi(S,t)))for t in range(3))),
   ('source_twist2_section_injection',lambda B:good(sub(cohom(B,2,0),cohom(S,2,0)))),
   ('source_twist3_H1_quotient',lambda B:good(sub(cohom(S,3,1),cohom(B,3,1)))),
   ('top_section_Euler',lambda B:good(sub(add(chi(B,3),cohom(B,1,0)),E3))),
   ('actual_cubic_double_visibility',lambda B:good(sub(cohom(B,3,0),E3))),
  ]
  for name,pred in filters:
   current={B for B in current if pred(B)};counts.append([name,len(current)])
  for B in current:check(capacity(B)==capacity_strings(B),'independent decreasing-rank capacity')
  degrees=sorted(set(deg(B)for B in current))
  rows=[x for x in ledger if x[4]in degrees]
  pairs=[]
  for row in rows:
   for B in sorted(current):
    if deg(B)!=row[4]:continue
    target=tuple(sorted((-e-4,i)for e,i in B))
    upper=capacity(target,5)
    check(upper==capacity_strings(target,5),'independent dual rank-five capacity')
    if row[1]<=upper:pairs.append({'row':row,'B':show(B),'upper_capacity':upper,'lower_capacity':capacity(B)})
  simultaneous.extend((label,x)for x in pairs)
  all_surv.extend((label,)+x for x in rows)
  results[label]={'smallest_four_source_degrees':low,'counts':counts,'surviving_degrees':degrees,'endpoint_a_upper_bound':-54-min(degrees),'necessary_ledger_rows':rows,'positive_torsion_rows':sum(x[2]+x[3]>0 for x in rows),'bundle_survivors':[{'B':show(B),'degree':deg(B),'capacity':capacity(B)}for B in sorted(current)],'simultaneous_pairs':pairs}
 check({s:r['endpoint_a_upper_bound']for s,r in results.items()}=={'D':-52,'P':-52,'V':-54,'Z':-54},'corrected new endpoint bounds')
 check([len(results[s]['simultaneous_pairs'])for s in ('D','P','V','Z')]==[35,14,5,6],'complete simultaneous endpoint survivor set sizes')
 check(all(x['row'][2]==0 and x['row'][3]in(0,12)for _,x in simultaneous),'new defect conclusion with positive defects retained')
 check(sum(x['row'][2]+x['row'][3]>0 for _,x in simultaneous)==7,'seven positive-defect triples retained')
 # Check the sole possible D degree -6 capacity case before the actual Q* test.
 low=ords(SOURCES['D'])[:4]
 D48={B for B in domain_ordinary(low,-6)if good(sub(E1,cohom(B,1,1)))}
 C48={B for B in D48 if capacity(B)>=-48}
 check(len(D48)==17,'D a-48 domain seventeen')
 expected=((-8,0),(-3,7),(8,0));check(C48=={expected},'unique D a-48 capacity survivor')
 check(cohom(expected,-1,0)[7]==1,'D a-48 has Wprime at twist minus one, not itself forbidden')
 check(cohom(expected,3,0)[5]==1 and E3[5]==2,'valid D a-48 contradiction from actual cubic visibility, NOT Qstar1')
 return {'claim':'Corrected necessary endpoint source bounds, actual ordered rank-four (1,2). Qstar twist-one vanishing is NOT assumed. No whole-profile exclusion.','checks':checks,'initial_ledger_rows':len(ledger),'initial_positive_torsion_rows':sum(x[2]+x[3]>0 for x in ledger),'source_results':results,'actual_instances_evaluated':False,'all_quotient_H1_retained':True,'source_labeled_necessary_rows':len(all_surv),'simultaneous_triples':len(simultaneous),'simultaneous_positive_defect_triples':sum(x['row'][2]+x['row'][3]>0 for _,x in simultaneous)}
if __name__=='__main__':print(json.dumps(main(),indent=2,sort_keys=True))

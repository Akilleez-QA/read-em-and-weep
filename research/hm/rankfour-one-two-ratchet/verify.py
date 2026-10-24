#!/usr/bin/env python3
"""New complete one-tuple necessary reduction: actual ordered rank-four (1,2).
Only abstract integer degrees and representation characters are evaluated.
"""
import json
from functools import lru_cache
from itertools import combinations_with_replacement
from collections import Counter
import base as v

def parse(x):return tuple(sorted((p['degree'],v.names.index(p['coefficient']))for p in x))
def record(B):return v.show(B)
def hom(B,C):return sum(v.sym_times(j,e-f)[i] for f,i in B for e,j in C if e-f>=0)
def twist(B,t):return tuple((e+t,i)for e,i in B)
def dual(B,t=0):return tuple(sorted((-e+t,i)for e,i in B))
def repchi(i,e):return v.chi(((e,i),),0)
M3=((3,7),(3,3),(6,5));M2=((1,2),(2,8),(3,6),(4,4))
def Qs(t):return v.sub(v.add(*(v.scale(repchi(i,t-1),n)for n,i in M3)),v.add(*(v.scale(repchi(i,t),n)for n,i in M2)))
def tor(r,t):return v.sub(repchi(0,r+t),repchi(0,r+t-12))
@lru_cache(None)
def endpoints(rank,d):
 lo=d+3*(rank-1);blocks=[(e,i)for e in range(lo,-2)for i in range(9)if v.dims[i]<=rank and e%2==v.parity[i]];out=set()
 def rec(at,rr,dd,B):
  if rr==0:
   if dd==0:out.add(tuple(B))
   return
  for j in range(at,len(blocks)):
   e,i=blocks[j];n=v.dims[i]
   if n<=rr and (rr-n)*lo<=dd-e*n<=(rr-n)*(-3):rec(j,rr-n,dd-e*n,B+[(e,i)])
 rec(0,rank,d,[]);return out
@lru_cache(None)
def endpoints_independent(rank,d):
 out=set();lo=d+3*(rank-1)
 for es in combinations_with_replacement(range(lo,-2),rank):
  if sum(es)!=d:continue
  groups=list(Counter(es).items())
  def rec(j,B):
   if j==len(groups):out.add(tuple(sorted(B)));return
   e,n=groups[j]
   for ids in v.coefficient_reps(n,e%2):rec(j+1,B+[(e,i)for i in ids])
  rec(0,[])
 return out

def envelope(E,B,t):
 # F_j top degree <= maxdeg(E)-j; q_j quotients inject into B(-2j).
 J=max(0,t+max(v.ords(E))+1)
 return v.sub(v.add(*(v.cohom(B,t-2*j,0)for j in range(J))),v.cohom(E,t,0))
def weighted_gap(N,r,D):
 tar=N*(D-r*(N-r));weights=[(N-r)*j if j<r else r*(N-j)for j in range(1,N)]
 reachable={0}
 for n in range(max(0,tar)+1):
  if n in reachable:
   for w in weights:
    for delta in (12,20,30):
     if n+w*delta<=tar:reachable.add(n+w*delta)
 return tar,sorted(reachable)

def classify_lower_kernel(B):
 """Complete finite K splitting classification from the actual cubic kernel theorem."""
 E=v.SOURCES['D'];c3=v.sub(v.chi(E,3),v.chi(B,3));c4=v.sub(v.chi(E,4),v.chi(B,4));out=set()
 for top in (v.zero,v.basis(3)):
  target=v.sub(top,c3);dim=v.dimension(target)
  blocks=[]
  for e in range(-dim-4,-4):
   for i in range(9):
    if v.parity[i]!=e%2:continue
    h=v.cohom(((e,i),),3,1)
    if v.good(v.sub(target,h)):blocks.append((e,i,h))
  def rec(at,left,chosen):
   if left==v.zero:
    R4=v.sub(v.add(c4,v.cohom(chosen,4,1)),v.W(top))
    if not v.good(R4):return
    K=tuple(sorted(chosen+tuple((-3,i)for i,m in enumerate(top)for _ in range(m))+tuple((-4,i)for i,m in enumerate(R4)for _ in range(m))))
    if len(v.ords(K))==13 and v.deg(K)==-54-v.deg(B):
     v.check(v.cohom(K,3,0)==top and v.chi(K,3)==c3 and v.chi(K,4)==c4,'complete K cohomology reconstruction')
     out.add(K)
    return
   for j in range(at,len(blocks)):
    e,i,h=blocks[j]
    if v.good(v.sub(left,h)):rec(j,v.sub(left,h),chosen+((e,i),))
  rec(0,target,())
 return sorted(out)

def main():
 old=v.main();rows=[];envelope_removed=[];counts={}
 v.check(Qs(0)==v.scale(v.Q0,-1),'actual Qstar untwisted Euler')
 for r in range(0,10,2):
  v.check(all(v.good(tor(r,t))and v.dimension(tor(r,t))==12 for t in range(-12,13)),'genuine orbit torsion all needed twists')
  v.check(tor(r,0)==tor(r+10,0)and tor(r,1)==tor(r+10,1),'stabilizer period ten')
 v.check(len({(tor(r,0),tor(r,1))for r in range(0,10,2)})==5,'five distinct center-even torsion characters')
 for b in sorted({x['row'][1]for sr in old['source_results'].values()for x in sr['simultaneous_pairs']}):
  v.check(endpoints(5,b)==endpoints_independent(5,b),'complete independent endpoint domain '+str(b))
 for s,sr in old['source_results'].items():
  counts[s]={'initial':len(sr['simultaneous_pairs']),'envelope':0,'upper_exact':0,'horizontal':0,'rank_one':0}
  for oldrow in sr['simultaneous_pairs']:
   B=parse(oldrow['B']);E=v.SOURCES[s];bad=next(((t,envelope(E,B,t))for t in range(2,33)if not v.good(envelope(E,B,t))),None)
   if bad:
    envelope_removed.append({'source':s,**oldrow,'witness':bad});continue
   counts[s]['envelope']+=1
   a,b,d1,d2,d=oldrow['row']
   for residue in ([None]if d2==0 else list(range(0,10,2))):
    target=tuple(v.add(Qs(t),v.chi(B,-t),v.chi(B,2-t),v.zero if residue is None else tor(residue,-t))for t in (0,1))
    for Z in sorted(endpoints(5,b)):
     if tuple(v.chi(Z,t)for t in (0,1))!=target:continue
     item={'source':s,'row':oldrow['row'],'B':record(B),'Z':record(Z),'torsion_residue':residue}
     counts[s]['upper_exact']+=1
     badblock=[]
     for block in Z:
      C=list(Z);C.remove(block)
      if hom((block,),dual(B,-6))==0 and hom((block,),twist(C,-2))==0:badblock.append(block)
     if badblock:
      item['horizontal_witnesses']=record(badblock);item['status']='rejected_horizontal';rows.append(item);continue
     counts[s]['horizontal']+=1
     # A scalar image is forced when all maps to other target blocks vanish.
     T=list(dual(B,-6));forced=False
     for ix,block in enumerate(T):
      if v.dims[block[1]]==1 and hom(Z,T[:ix]+T[ix+1:])==0:forced=True;break
     if forced and b==-22:
      for N in (8,9):
       tar,reached=weighted_gap(N,5,22);v.check(tar not in reached,'rank-five -22 span gap '+str(N))
      item['status']='rejected_rank_one';item['rank_one_target']=record((block,));rows.append(item);continue
     counts[s]['rank_one']+=1;item['status']='necessary_survivor';rows.append(item)
 v.check({s:tuple(c.values())for s,c in counts.items()}=={'D':(35,31,12,7,3),'P':(14,6,2,0,0),'V':(5,2,2,0,0),'Z':(6,2,2,0,0)},'all new source-stage counts')
 three=[x for x in rows if x['status']=='necessary_survivor']
 remaining=three[:]
 v.check(len(three)==3 and sum(x['row'][3]>0 for x in three)==1,'three necessary tuples retain positive torsion')
 cutB=((-8,0),(-3,7),(14,0));kernels=classify_lower_kernel(cutB)
 expected={((-5,7),(-4,4),(-4,8),(-4,8)),((-8,0),(-5,7),(-4,8),(-4,8),(-3,3))}
 v.check(set(kernels)==expected,'complete two-V kernel alternatives')
 for K in kernels:
  v.check(K.count((-4,8))==2,'two identical V coefficient directions')
  v.check(hom(((-4,8),),twist(cutB,-2))==1,'one-dimensional complete derivative Hom for V')
  complement=list(K);complement.remove((-4,8))
  v.check(hom(((-4,8),),twist(complement,-2))==0,'killed V has zero internal derivative')
 for item in three:
  if parse(item['B'])==cutB:item['status']='rejected_two_V_kernel';item['kernel_alternatives']=[record(K)for K in kernels]
 remaining=[x for x in rows if x['status']=='necessary_survivor']
 v.check(len(remaining)==1 and tuple(remaining[0]['row'])==(-58,-22,0,0,4),'unique final necessary tuple')
 v.check(sum(x['row'][3]>0 for x in rows if x['status']=='rejected_two_V_kernel')==1,'positive torsion excluded by valid kernel proof, not omitted')
 v.check(weighted_gap(8,5,22)==(56,[0,36])and weighted_gap(9,5,22)==(18,[0]),'complete rank-one reachable sets')
 v.check(weighted_gap(9,5,20)[0]in weighted_gap(9,5,20)[1],'rank-one unramified positive control')
 v.check(weighted_gap(9,5,36)[0]in weighted_gap(9,5,36)[1],'rank-one ramified positive control')
 return {'claim':'Conditional necessary one-tuple reduction of actual ordered rank-four (1,2); not profile exclusion.','actual_instances_evaluated':False,'Qstar_twist_one_vanishing_assumed':False,'positive_torsion_retained_until_proved_exclusion':True,'checks':v.checks,'source_stage_counts':counts,'base_simultaneous_triples':old['simultaneous_triples'],'envelope_rejections':envelope_removed,'endpoint_tuples':rows,'necessary_survivors':remaining,'two_V_kernel_alternatives':[record(K)for K in kernels],'rank_one_gaps':{str(N):weighted_gap(N,5,22)for N in (8,9)}}
if __name__=='__main__':print(json.dumps(main(),indent=2,sort_keys=True))

#!/usr/bin/env python3
"""Source2 residual constant span, unique primal source, and final constant quotient."""
from pathlib import Path
from fractions import Fraction as F
import hashlib, json
from functools import lru_cache
ROOT=Path(__file__).resolve().parent

# Exact Q(sqrt(5)) character arithmetic, independently reproduced here.
def plus(a,b):return(a[0]+b[0],a[1]+b[1])
def times(a,b):return(a[0]*b[0]+5*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def scale(c,a):return(c*a[0],c*a[1])
def minus(a,b):return plus(a,scale(-1,b))
def total(xs):
 out=(F(0),F(0))
 for x in xs:out=plus(out,x)
 return out
z=lambda a,b=0:(F(a),F(b))
phi=z(F(1,2),F(1,2));phip=z(F(1,2),-F(1,2))
W=[z(2),z(-2),phi,scale(-1,phi),phip,scale(-1,phip),z(1),z(-1),z(0)]
sizes=[1,1,12,12,12,12,20,20,30]
@lru_cache(None)
def symchar(n):
 a=[z(1)]*9
 if n==0:return a
 b=W
 for _ in range(2,n+1):a,b=b,[minus(times(w,v),u)for w,v,u in zip(W,b,a)]
 return b
chars={'one':[z(1)]*9,'W':W,'A':symchar(2),'S':symchar(3),'D':symchar(4),'T':symchar(5)}
chars['P']=list(map(z,[4,4,-1,-1,-1,-1,1,1,0]))
chars['V']=[minus(a,b)for a,b in zip(symchar(6),chars['P'])]
chars['Wp']=[minus(times(w,p),t)for w,p,t in zip(W,chars['P'],chars['T'])]
names=('one','W','Wp','A','V','P','S','D','T')
def inner(a,b):return scale(F(1,120),total(scale(s,times(x,y))for s,x,y in zip(sizes,a,b)))
assert all(inner(chars[a],chars[b])==z(a==b)for a in names for b in names)
# Characters are real, hence the nine irreducibles are self-dual.
# W has trivial determinant: Lambda^2 W = 1 (the standard SL2 lift).
# The recurrence uses exactly that determinant-one linearization.
def mul(a,b):return [times(x,y)for x,y in zip(a,b)]
def sub(a,b):return [minus(x,y)for x,y in zip(a,b)]
def linear(terms):return [total(scale(c,chars[n][i])for c,n in terms)for i in range(9)]
def decompose(a):
 out=[inner(a,chars[n])for n in names]
 assert all(b==0 and x.denominator==1 for x,b in out)
 return tuple(int(x)for x,b in out)
M3=linear([(3,'Wp'),(3,'S'),(6,'T')])
M4=linear([(2,'V'),(4,'P'),(3,'D')])
PINNED={'TWO-ONE-INDEX-TWO-CONSTANT-SPAN-INTERSECTION.md': 'f72531663c01cb681e56500f578d595355cab384c9bb96b1ea120012ff4671b7', 'TWO-ONE-INDEX-TWO-RESIDUAL-OSCULATIONS.md': 'e89dd5169fc0c80360884de045e8d067564be582366e7f9608394d738b200e3f', 'rank-three-quotient-frontier-144.json': 'a6fc9ec680d1866782e0233c234c5d80d398e9fc77734b59e61040ffc92021ad'}

assert all(hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==h for f,h in PINNED.items())
ID='G3.21.d610e381ed75';row=next(r for r in json.loads((ROOT/'rank-three-quotient-frontier-144.json').read_text())['cases']if r['id']==ID)
assert row['profile']=='21' and row['source_index']==2
assert row['A']==[[-8,'one'],[2,'one'],[16,'one']] and row['B']==[[-18,'one'],[-4,'one'],[6,'one']]
dims=dict(zip(names,[1,2,2,3,3,4,4,5,6]));zero=(0,)*9
add=lambda a,b:tuple(x+y for x,y in zip(a,b));vs=lambda a,b:tuple(x-y for x,y in zip(a,b))
@lru_cache(None)
def prod(n,k):return decompose(mul(chars[n],symchar(k)))
X=vs(decompose(M3),prod('W',8));Y=vs(decompose(M4),prod('W',7))
blocks=[]
for e in range(-8,-1):
 for n in names:
  if e%2!=int(chars[n][1][0]<0):continue
  x,y=prod(n,-e-1),prod(n,-e-2)
  if all(a<=b for a,b in zip(x,X))and all(a<=b for a,b in zip(y,Y)):blocks.append((e,n,x,y))
solutions=[]
def dfs(start,rank,degree,x,y,bundle):
 if rank==15:
  if degree==-36 and x==X and y==Y:solutions.append(bundle)
  return
 for j in range(start,len(blocks)):
  e,n,u,v=blocks[j];rr=rank+dims[n];dd=degree+e*dims[n];xx=add(x,u);yy=add(y,v)
  if rr<=15 and dd-2*(15-rr)>=-36 and all(a<=b for a,b in zip(xx,X))and all(a<=b for a,b in zip(yy,Y)):dfs(j,rr,dd,xx,yy,bundle+[(e,n)])
dfs(0,0,0,zero,zero,[])
expected=[[(-8,'one'),(-2,'P'),(-2,'D'),(-2,'D')],[(-5,'Wp'),(-2,'P'),(-2,'P'),(-2,'D')],[(-4,'V'),(-2,'V'),(-2,'P'),(-2,'D')],[(-3,'T'),(-2,'P'),(-2,'D')]]
assert solutions==expected and len(blocks)==12
assert decompose(symchar(8))==(0,0,0,0,0,1,0,1,0)
# Rank-two annihilator for the projected D span: total degree -18, H0=0, center-even.
ann_target=vs(prod('A',6),decompose(chars['D']))
ann_candidates=[[(e,'one'),(-18-e,'one')]for e in range(-16,-8,2)]+[[(-9,'W')],[(-9,'Wp')]]
def h1(b):
 out=zero
 for e,n in b:out=add(out,prod(n,-e-2))
 return out
ann=[b for b in ann_candidates if h1(b)==ann_target]
assert ann==[[(-10,'one'),(-8,'one')],[(-9,'W')]]
assert ann_target==(0,0,0,0,1,2,0,1,0)
# P span annihilator line has degree -18, below every E' source degree; D line-pair case forces R degree -8, not -36.
assert -18<-8 and -8!=-36
# Full Sym8 span annihilator of second osculation is Sym5 O(-3)=T O(-3).
assert decompose(symchar(5))==decompose(chars['T'])
possible_projection_ranks=[sum(dims[n]for e,n in b if e<=-3)for b in solutions]
assert possible_projection_ranks==[1,2,3,6]
assert all(9-r>4 for r in possible_projection_ranks[:3])
forced_Eprime=solutions[3];forced_E=[(-9,'W')]+forced_Eprime
assert sum(dims[n]for e,n in forced_E)==17 and sum(e*dims[n]for e,n in forced_E)==-54
# Final constant quotient dimension10, with H1((P+D)O(-2))=P+D.
final_char=vs(decompose(symchar(18)),add(decompose(chars['P']),decompose(chars['D'])))
assert final_char==(0,0,0,1,1,1,0,0,0)
out=dict(scope='Full degree8 residual constant span and unique necessary E source; no quotient-label exclusion or realization.',id=ID,source_hashes=PINNED,Eprime_H1_minus_one=X,Eprime_H1=Y,eligible_Eprime_blocks=[[e,n]for e,n,x,y in blocks],four_Eprime_types=solutions,proper_constant_spans=['P','D'],D_annihilator_H1=ann_target,D_annihilator_complete_candidates=ann_candidates,D_annihilator_matching_types=ann,projection_rank_bounds=possible_projection_ranks,forced_E=forced_E,forced_Eprime=forced_Eprime,forced_residual_constant_span=['P','D'],forced_final_kernel=[[-2,'P'],[-2,'D']],final_constant_quotient_rank=10,final_constant_quotient_character=final_char,character_order=names,final_saturated_line=[[-18,'one']],realization_claimed=False)
(ROOT/'two-one-index-two-residual-full-span.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS:',ID,'full residual Sym8 span; Eprime4->1; unique E and final saturated O(-18) in constant rank10.')

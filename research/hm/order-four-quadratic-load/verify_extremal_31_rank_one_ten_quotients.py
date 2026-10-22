"""Universal representation and bundle constraints, never actual-instance ranks."""
from pathlib import Path
import runpy,contextlib,io,itertools
ROOT=Path(__file__).parent
with contextlib.redirect_stdout(io.StringIO()):
 b=runpy.run_path(str(ROOT/'verify_extremal_31_last_remaining_quotient_reduction.py'))
 q=runpy.run_path(str(ROOT/'verify_exceptional_cubic_gauss_corner.py'))
r=b['reps'];va,vs,vm,sy,eu,se,ef,mu=[b[x] for x in ['va','vs','vm','sym','euler','sections','effective','mu']]
U=va(r['Wp'],vs(2,r['T']));dim=lambda v:sum(mu(v,R)*d for R,d in [(r[n],d) for n,d in [('one',1),('W',2),('Wp',2),('A',3),('V',3),('P',4),('D',5),('S',4),('T',6)]])
def margin(e,B):return va(*[vm(r[R],va(eu(n+3),se(n+1),se(n-1))) for R,n in B],vs(-1,va(U,sy(e-6))))
def hom(R,n,Q):return sum(c*mu(vm(r[R],vm(r[S],se(j-2-n))),r['one']) for j,S,c in Q)
base=[(('one',-4),('one',6)),(('one',2),('one',4)),(('one',2),('one',6)),(('one',4),('one',4)),(('one',4),('one',6)),(('W',3),),(('W',5),)]
extras={9:[(('one',-10),('one',6)),(('one',-4),('one',4))],11:[(('one',-8),('one',6))]}
kept=[]
for e in (9,11):
 candidates=[(('one',n),('one',m)) for n,m in itertools.combinations_with_replacement(range(e-19,7,2),2)]+[((R,n),) for R in ('W','Wp') for n in (1,3,5)]
 stage=[B for B in candidates if ef(margin(e,B))]
 assert len(stage)==(17 if e==9 else 13)
 good=[B for B in stage if any(all(hom(R,n,Q)>=B.count((R,n)) for R,n in B) for Q in q['profiles'])]
 assert set(good)==set(base+extras[e])
 for B in extras[e]:assert margin(e,B)==b['zero']
 for B in base:
  assert min(n+e-1 for R,n in B)>=-1
  M=margin(e,B);allowed=[]
  for j in range(5,dim(M)+5):
   for R in r:
    H=vm(r[R],sy(j-5))
    if ef(va(M,vs(-1,H))) and mu(vm(r[R],se(j-e-1)),r['one']):allowed.append((R,j))
  if e==11:
   expected=[] if B in [base[i] for i in (0,1,2,5)] else [('one',12)] if B==base[3] else [('one',12),('W',13)]
   assert set(allowed)==set(expected)
  if allowed:kept.append((e,B))
  print(e,B,'low blocks',allowed)
assert len(kept)==10
assert sum(e==9 for e,B in kept)==7 and sum(e==11 for e,B in kept)==3
# The only potentially nonsplit discarded case has H1(O(-2))=one.
assert eu(-2)==vs(-1,r['one'])
assert va(vm(r['W'],eu(-9+3)),vs(-1,va(eu(-8+3),eu(-10+3))))==b['zero']
assert max(j for Q in q['profiles'] for j,R,c in Q)==8
assert dim(U)==14
print('PASS: rank-one image leaves ten necessary split first quotients, seven at e9 and three at e11.')
print('No realization, full profile exclusion, or improved SF/square bound is claimed.')

"""Necessary (2,1) quotient characters only; no actual map instances."""
from pathlib import Path
import runpy,contextlib,io,itertools,json,hashlib,sys
ROOT=Path(__file__).parent
with contextlib.redirect_stdout(io.StringIO()):
 r=runpy.run_path(str(ROOT/'verify_adjacent_rank_three_gauss.py'))
for k in ('reps','va','vs','vm','sym','dimension','effective','hom','bundle_hom','zero','U','T','W','S'):globals()[k]=r[k]
from functools import lru_cache
@lru_cache(None)
def hc(B,t=0,euler=False):
 out=[zero]
 for e,n in B:
  d=e+t
  if d>=0:out.append(vm(reps[n],sym(d)))
  elif euler and d<=-2:out.append(vs(-1,vm(reps[n],sym(-d-2))))
 return va(*out)
def degree(B):return sum(e*dimension(reps[n]) for e,n in B)
def rank(B):return sum(dimension(reps[n]) for e,n in B)
def ordinary(B):return sorted(e for e,n in B for _ in range(dimension(reps[n])))
def degree_injection(A,B):return all(a<=b for a,b in zip(ordinary(A),ordinary(B)))
def shapes(lo,hi):
 lines=[(e,'one') for e in range(lo,hi+1) if e%2==0]
 yield from itertools.combinations_with_replacement(lines,3)
 for e in range(lo,hi+1):
  if e%2:
   for n in ('W','Wp'):
    for L in lines:yield tuple(sorted(((e,n),L)))
  else:
   for n in ('A','V'):yield ((e,n),)
chiE4=va(vm(r['M3'],sym(3)),vs(-1,vm(va(vs(2,reps['V']),vs(4,reps['P']),vs(3,reps['D'])),sym(4))))
chiE3=U
chiQ3=va(T,vs(-2,W),vs(-1,S))
chiE2=vs(-1,reps['V'])
chiQ2=va(vm(r['M3'],W),vs(-1,vm(r['M2'],sym(2))))
def envelope(B,C):return effective(va(hc(B,3,True),hc(B,1),vs(-1,C)))
# A source E(10) and B source Q*(28) are globally generated.
# Both upper limits are from the actual target splitting bounds.
Ac=[B for B in shapes(-10,26) if -2<=degree(B)<=18 and effective(va(hc(B,3,True),hc(B,1,True),vs(-1,chiE3))) and effective(va(hc(B,2,True),vs(-1,chiE2)))]
Ac=[A for A in Ac if effective(va(hc(A,0),hc(A,4,True),hc(A,2,True),vs(-1,chiE4)))]
Bc=[B for B in shapes(-28,8) if -24<=degree(B)<=-4 and envelope(B,chiQ3) and effective(va(hc(B,2,True),vs(-1,chiQ2)))]
# Full bundle-map eligibility, necessary only. A quotient requires nonzero
# projection to every target block. An injection requires nonzero restriction
# from every source block. No inference of fiber rank from Hom dimensions.
@lru_cache(None)
def bh(n,e,target):return bundle_hom(reps[n],e,[(d,reps[m]) for d,m in target])
def receives(B,source):return all(any(bh(n,d,((e,m),)) for d,n in source) for e,m in B)
def embeds(B,target):return all(bh(n,e,target) for e,n in B)
Es=[]
for co,R2,blocks in r['E_profiles']:
 E=tuple((-j,n) for j,R in blocks for n in reps for _ in range(int(r['multiplicity'](R,reps[n]))))
 Es.append((co,E,R2))
Qs=[]
for p in r['profiles']:
 Q=tuple((-j,n) for j,n,c in p for _ in range(c))
 Qs.append((p,Q,r['quadratic'](p)))
def negdual(B,twist=-2):return tuple((-e+twist,n) for e,n in B)
assert len(Es)==28 and len(Qs)==37
assert all(min(e for e,n in E)>=-10 for _,E,_ in Es)
assert all(min(e for e,n in Q)>=-28 and max(e for e,n in Q)<=-2 for _,Q,_ in Qs)
@lru_cache(None)
def h1(B,t):return va(hc(B,t),vs(-1,hc(B,t,True)))
@lru_cache(None)
def quotient_cohom(B,F):return all(effective(va(h1(F,t),vs(-1,h1(B,t)))) for t in range(-2,9))
records=[]
for co,E,R2 in Es:
 for qp,Q,RQ in Qs:
  aa=[A for A in Ac if receives(A,E) and quotient_cohom(A,E) and embeds(A,negdual(Q)) and effective(va(hc(A,2),vs(-1,R2)))]
  bb=[B for B in Bc if receives(B,Q) and quotient_cohom(B,Q) and embeds(B,negdual(E)) and effective(va(hc(B,2),vs(-1,RQ)))]
  for A in aa:
   for B in bb:
    t=-6-degree(A)-degree(B)
    if t not in (0,12,20):continue
    if not degree_injection(A,negdual(B)):continue
    if not embeds(A,negdual(B)) or not embeds(B,negdual(A)):continue
    # If t=0, equal-rank inclusion is an isomorphism, so exact splitting.
    if t==0 and sorted(A)!=sorted(negdual(B)):continue
    records.append(dict(E=co,Q=qp,A=A,B=B,defect=t))
print('preliminary A,B shape counts',len(Ac),len(Bc))
print('surviving formal records',len(records))
print('distinct A,B,pairs',len({str(x['A']) for x in records}),len({str(x['B']) for x in records}),len({(str(x['A']),str(x['B'])) for x in records}))
from collections import Counter
print('defects',dict(sorted(Counter(x['defect'] for x in records).items())))
print('E types',len({x['E'] for x in records}),'Q types',len({x['Q'] for x in records}))

pairs=sorted({(tuple(map(tuple,x['A'])),tuple(map(tuple,x['B'])),x['defect']) for x in records})
assert (len(Ac),len(Bc),len(records),len(pairs))==(340,188,877,13)
assert Counter(x['defect'] for x in records)=={0:837,12:40}
assert len({x['E'] for x in records})==22
assert len({x['Q'] for x in records})==24
assert sorted({degree(A) for A,B,t in pairs})==[0,2,4,6,10,12,14]
assert all(degree(A)==2 and B==((-18,'one'),(-8,'one'),(6,'one')) for A,B,t in pairs if t==12)
# The original defect12 is a line on the reduced twelve-point orbit.
# Its stabilizer is C10, and center-even characters are k=0,2,4,6,8.
for A,B,t in pairs:
 if t!=12:continue
 def torsion_difference(r):return va(hc(negdual(B),r,True),vs(-1,hc(A,r,True)))
 def orbit_character(k,r):return va(hc(((k,'one'),),r,True),vs(-1,hc(((k-12,'one'),),r,True)))
 matches=[k for k in range(0,10,2) if all(torsion_difference(r)==orbit_character(k,r) for r in (0,1))]
 assert matches==[6]
 assert all(torsion_difference(r)==orbit_character(6,r) for r in range(-2,9))
def defect_degrees(a):
 cap=4+2*a
 return sorted({12*i+20*j+30*k for i in range(cap//12+1) for j in range(cap//20+1) for k in range(cap//30+1) if 12*i+20*j+30*k<=cap})
assert defect_degrees(0)==defect_degrees(2)==[0]
summary=dict(scope='Necessary (2,1) quotient pairs only, not realizability or exclusion.',
 record_count=len(records),E_type_count=22,Q_type_count=24,original_defects=dict(Counter(x['defect'] for x in records)),
 pairs=[dict(A=A,B=B,original_defect=t,original_orbit_line=6 if t==12 else None,a=degree(A),b=degree(B),second_primal_defects=defect_degrees(degree(A)),records=sum(tuple(map(tuple,x['A']))==A and tuple(map(tuple,x['B']))==B and x['defect']==t for x in records)) for A,B,t in pairs],
 dependencies={f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in ('verify_adjacent_rank_three_gauss.py','verify_exceptional_cubic_gauss_corner.py','verify_equivariant_splitting_gauss_persistence.py','verify_negative_vertex_scalar.py')})
(ROOT/'two-one-primal-interior-quotient-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
if '--full' in sys.argv:
 (ROOT/'two-one-primal-interior-quotient-records.json').write_text(json.dumps(records,indent=2)+'\n')
for p in summary['pairs']:print(p)
print('PASS: 13 necessary pairs, a>=0, original defect 0 or12; both defect12 branches have second primal defect zero.')

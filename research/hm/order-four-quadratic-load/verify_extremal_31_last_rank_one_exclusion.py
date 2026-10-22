"""Universal exact characters and sheaf constraints; no instance data or ranks."""
from pathlib import Path
import runpy, contextlib, io, itertools
with contextlib.redirect_stdout(io.StringIO()):
 p=runpy.run_path(str(Path(__file__).with_name('verify_extremal_31_rank_one_degree_eleven_exclusion.py')))
r,va,vs,vm,sy,eu,se,ef,mu,dim=[p[k] for k in ['r','va','vs','vm','sy','eu','se','ef','mu','dim']]
z=p['z'];U=p['U'];E4=p['E4'];base=p['b']['base']
def add(*v):return va(*v) if v else z
def sub(a,b):return add(a,vs(-1,b))
def chi(bs,t):return add(*[vm(r[R],eu(n+t)) for R,n in bs])
def h0(bs,t):return add(*[vm(r[R],se(n+t)) for R,n in bs])
def hom(R,n,S,m):return mu(vm(r[R],vm(r[S],se(m-n))),r['one'])
def low(M,target):return p['low_blocks'](M,target)
def blocks(v,n):return [(R,n) for R in r for _ in range(mu(v,r[R]))]
def tails(M):
 candidates=[]
 for j in range(5,dim(M)+5):
  for R in r:
   cost=vm(r[R],sy(j-5))
   if ef(sub(M,cost)):
    cap=min(mu(M,r[S])//mu(cost,r[S]) for S in r if mu(cost,r[S]))
    candidates.append(((R,-j),cap))
 for counts in itertools.product(*[range(cap+1) for _,cap in candidates]):
  bs=[block for (block,_),c in zip(candidates,counts) for _ in range(c)]
  if ef(sub(M,vs(-1,chi(bs,3)))):yield bs

def split_candidates(C3,C4,M,rank,max_degree=-3):
 out=[]
 for ns in tails(M):
  H0=add(C3,vs(-1,chi(ns,3)))
  if not ef(H0) or (max_degree==-4 and H0!=z):continue
  R4=sub(sub(C4,chi(ns,4)),vm(H0,r['W']))
  if not ef(R4):continue
  bs=blocks(H0,-3)+blocks(R4,-4)+ns
  if sum(dim(r[R]) for R,n in bs)==rank:out.append(bs)
 return out

def canonical(bs):return tuple(sorted(bs))
full={}
for i in (3,4,6):
 B=list(base[i]);A0=B+[('one',-8)];D=[(R,n-2) for R,n in B]
 K3=sub(U,chi(A0,3));total=sum(dim(r[R])*n for R,n in D)
 # deg(K2)<=-33 bounds total determinant defect by 15 or 19.
 degK=-54-sum(dim(r[R])*n for R,n in A0)
 bound=total-10-(degK+33)
 assert bound==(15 if i==3 else 19) and bound<20
 # Positive defect is exactly 12. Projected-low defect is 0 or 12.
 defect=[D+[('one',-22)]];mx=max(n for R,n in D);d=total-12
 for a in range(d-mx,mx+1):
  c=d-a
  if a<=c<=mx and a%2==c%2==0:defect.append([('one',a),('one',c),('one',-10)])
 if d%2==0 and (d//2)%2:
  defect += [[(R,d//2),('one',-10)] for R in ('W','Wp')]
 for A1 in defect:
  assert min(n+10 for R,n in A1[:-1])>=-1 # Extension by O(-10) splits.
  C3=sub(K3,chi(A1,3));M=sub(h0(A1,1),C3)
  assert not ef(M) or low(M,24 if A1[-1][1]==-22 else 12)==[]
 A1=D+[('one',-10)];C3=sub(K3,chi(A1,3));M=sub(h0(A1,1),C3)
 assert low(M,12)==([('one',12)] if i==3 else [('one',12),('W',13)])
 if i!=3:
  cost=vm(r['W'],sy(8)); assert sub(M,cost)==z
  assert add(C3,cost)==add(r['S'],r['T']) and dim(add(C3,cost))>9
 # Forced O(-12), multiplicity one. Remove it as a bundle summand.
 C3y=sub(C3,chi([('one',-12)],3));C4y=sub(sub(sub(E4,chi(A0,4)),chi(A1,4)),chi([('one',-12)],4))
 My=sub(M,sy(7));assert My==(r['S'] if i==3 else add(r['S'],r['T']))
 ys=split_candidates(C3y,C4y,My,10)
 expected=[[('S',-3),('V',-4),('V',-4)]] if i==3 else [[('V',-4),('V',-4),('P',-4)],[('T',-3),('V',-4),('one',-10)]]
 assert set(map(canonical,ys))==set(map(canonical,expected));full[i]=(A0,A1,ys)
 if i==3:
  assert hom('S',-3,'one',0)==1 and hom('V',-4,'one',0)==0
 elif i==4:
  assert all(hom(R,n,'one',0)==0 for Y in ys for R,n in Y)
# Last W case: rank-three interior A2 has defect at most 10, hence zero.
A0,A1,ys=full[6];A2=[('W',1),('one',-12)]
assert (-10)-(-52+32)==10
C3=sub(sub(sub(U,chi(A0,3)),chi(A1,3)),chi(A2,3))
C4=sub(sub(sub(E4,chi(A0,4)),chi(A1,4)),chi(A2,4))
assert C3==vs(-1,add(r['S'],r['T'])) and C4==sub(r['V'],r['D'])
F=split_candidates(C3,C4,vs(-1,C3),8,-4)
assert len(F)==6
K2=[('V',-4),('V',-4),('P',-4),('one',-12)]
F=[bs for bs in F if all(sum(hom(R,n,S,m) for S,m in K2)>=bs.count((R,n)) for R,n in bs)]
expected=[[('V',-4),('D',-6)],[('V',-4),('V',-4),('Wp',-9)],[('V',-4),('P',-4),('one',-14)]]
assert set(map(canonical,F))==set(map(canonical,expected))
# Upper quintic jet has kernel S(-5); all complementary maps lift.
assert list(sy(5))==r['T'] and list(sy(3))==r['S']
assert -5-(-4)==-1 and -5-(-10)==5
# Endpoint supports, and lower Clebsch summands (not upper jet maps).
for active,n,others in [('S',-5,[('V',-4),('one',-10)]),('D',-6,[('V',-4)]),('Wp',-9,[('V',-4),('V',-4)])]:
 assert hom(active,n,'W',-1)==1 and hom(active,n,'one',-14)==0
 assert all(hom(R,j,'W',-1)==hom(R,j,'one',-14)==0 for R,j in others)
 degree=-n-2
 assert mu(sy(degree),r[active])==1 and mu(sy(degree+2),r[active])==0
 assert degree<12
# Exact Hom supports in the complete-evaluation descents.
for active,n,target,others in [('A',-6,-4,[('V',-4),('one',-10)]),('W',-7,-6,[('V',-4),('one',-10)]),('one',-8,-8,[('V',-4),('one',-10)]),('one',-10,-10,[('V',-4)]),('S',-7,-4,[('V',-4)]),('A',-8,-6,[('V',-4)]),('W',-9,-8,[('V',-4)]),('one',-10,-10,[('V',-4)])]:
 assert hom(active,n,'one',target)==1
 assert all(hom(R,j,'one',target)==0 for R,j in others)
assert hom('one',-16,'one',-4)==1 and hom('V',-4,'one',-4)==0
assert hom('V',-4,'one',-18)==0
assert all(hom(R,-4,'W',-1)==hom(R,-4,'one',-14)==0 for R in ('V','P'))
assert all(hom(R,-4,'one',-16)==0 for R in ('V','P'))
assert hom('V',-4,'one',-12)==0
print('PASS: final three rank-one shapes excluded by the accompanying actual-image and saturated-descent proof.')
print('Together with pinned prior cases, the full (3,1) profile is excluded. No stronger global SF bound is inferred.')

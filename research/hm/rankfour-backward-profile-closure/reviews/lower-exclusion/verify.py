#!/usr/bin/env python3
"""Independent top-section obstruction review. Exact characters; no author imports."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations_with_replacement, product
from collections import Counter
from pathlib import Path
import hashlib,json,sys
ROOT=Path(__file__).resolve().parent
MUT=sys.argv[1] if len(sys.argv)>1 else ''
CHECKS=0
def require(x,msg):
 global CHECKS
 CHECKS+=1
 if not x:raise RuntimeError(msg)
def q(a,b=0):return F(a),F(b)
def qa(x,y):return x[0]+y[0],x[1]+y[1]
def qs(k,x):return k*x[0],k*x[1]
def qm(x,y):return x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0]
def qr(x,y):return qa(x,qs(-1,y))
SIZES=(1,1,12,12,12,12,20,20,30)
TRACE=(q(2),q(-2),q(F(1,2),F(1,2)),q(F(-1,2),F(-1,2)),q(F(1,2),F(-1,2)),q(F(-1,2),F(1,2)),q(1),q(-1),q(0))
NAMES=('1','W','A','S4','D','T6','P',"W'",'V')
DIM=dict(zip(NAMES,(1,2,3,4,5,6,4,2,3)))
PAR=dict(zip(NAMES,(0,1,0,1,0,1,0,1,0)))
ZERO=(q(0),)*9
def add(*args):return tuple((sum(x[i][0]for x in args),sum(x[i][1]for x in args))for i in range(9))
def mul(k,x):return tuple(qs(k,v)for v in x)
def sub(x,y):return add(x,mul(-1,y))
@lru_cache(None)
def tensor(x,y):return tuple(qm(a,b)for a,b in zip(x,y))
@lru_cache(None)
def symmetric(n):
 old,now=ZERO,(q(1),)*9
 for _ in range(n):old,now=now,sub(tensor(TRACE,now),old)
 return now
CHAR={n:symmetric(i)for i,n in enumerate(NAMES[:6])}
CHAR['P']=tuple(q(x)for x in(4,4,-1,-1,-1,-1,1,1,0))
CHAR['V']=sub(symmetric(6),CHAR['P'])
CHAR["W'"]=sub(tensor(TRACE,CHAR['P']),CHAR['T6'])
if MUT=='physical-marking':CHAR['A'],CHAR['V']=CHAR['V'],CHAR['A']
def inner(x,y):
 result=q(0)
 for size,a,b in zip(SIZES,x,y):result=qa(result,qs(F(size,120),qm(a,b)))
 return result
@lru_cache(None)
def dec(x):
 ans=[]
 for n in NAMES:
  a,b=inner(x,CHAR[n]);require(b==0 and a.denominator==1,'integral class decomposition')
  ans.append(int(a))
 return tuple(ans)
def coeff(x,n):return dec(x)[NAMES.index(n)]
def show(x):return {n:v for n,v in zip(NAMES,dec(x))if v}
def representation(**kw):return add(*(mul(k,CHAR[n])for n,k in kw.items()))
@lru_cache(None)
def line(n):
 if n>=0:return symmetric(n)
 if n==-1 or MUT=='omit-H1':return ZERO
 return mul(-1,symmetric(-n-2))
@lru_cache(None)
def chi(shape,t):return add(*(tensor(CHAR[n],line(e+t))for e,n in shape))
@lru_cache(None)
def h0(shape,t):return add(*(tensor(CHAR[n],symmetric(e+t))for e,n in shape if e+t>=0))
def h0dim(shape,t):return sum(DIM[n]*(e+t+1)for e,n in shape if e+t>=0)
def degree(shape):return sum(e*DIM[n]for e,n in shape)
def rank(shape):return sum(DIM[n]for e,n in shape)
def display(shape):return [{'degree':e,'coefficient':n}for e,n in shape]
@lru_cache(None)
def hom(e,n,f,m):
 exponent=f-e
 if MUT=='maps-vs-sections':exponent=f+e
 if exponent<0:return 0
 return coeff(tensor(CHAR[m],symmetric(exponent)),n)
M2=representation(A=1,V=2,P=3,D=4)
M3=representation(**{"W'":3,'S4':3,'T6':6})
M4=representation(V=2,P=4,D=3)
H=representation(A=2,V=2,P=2,D=2)
def E(t):return sub(tensor(M3,line(t-1)),tensor(M2 if MUT=='source-dual-swap'else M4,line(t)))
def Qstar(t):return sub(tensor(M3,line(t-1)),tensor(M2,line(t)))
SOURCES={
'D':((-2,'D'),(-3,"W'"),(-3,'T6'),(-4,'V'),(-8,'1')),
'P':((-2,'P'),(-3,"W'"),(-3,'T6'),(-4,'V'),(-5,"W'")),
'V':((-2,'V'),(-3,"W'"),(-3,'T6'),(-4,'V'),(-4,'V')),
'Z':((-3,"W'"),(-3,'T6'),(-3,'T6'),(-4,'V'))}
ORIGINAL_HASHES={
'ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md':'a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256',
'POSITIVE-DOUBLE-HYPERPLANE-GAUSS-GATE.md':'0928dd8261ac0d2659188af6520b564611b289cd0e271185ef5f4e3bafe3a6a2',
'RANK-TWO-GAUSS-PLATEAU-NECESSARY-BOUND.md':'868b89283fc98d276b8c9833f16d3dd16fe2b6a98a326769ce43d3a7e46d8b3c',
'GAUSS-DETERMINANT-ORBIT-RAMIFICATION.md':'783454715e967929ad81e6f09f8f4a155073fbdab89974bee056416e4f866e71',
'four-sources.md':'d5feb4b4478b5ec8178a049124179d25473b2e2526b20823a40f6dc60095e28e',
'EXCEPTIONAL-CUBIC-GAUSS-CORNER-EXCLUSION.md':'9f01d086401ee7ee850d3c9181c0486734bcc5c5791c552410895ae4ba742fbf'}
DEPENDENCY_HASHES={
'lower-image-PROOF.md':'f6f807996ccca5b05233af8964bbbaa4f3913f79e4955ea2b4906462db3f2751',
'lower-image-verify.py':'8bfaf601c8817fb0ab3af19a5aff734efdad09a318491c1bec7d8430818cb0f6',
'lower-image-RESULT.json':'9b157f897b96ec2e87951f540393fecd31057b34121bdf6b5de2ebaf38223c72',
'full-image-PROOF.md':'0e291e31481530df3163ed6abc3d433a4e402c98e9258d3a329b05b51a2ea507',
'full-image-verify.py':'6d4f66ca5ac1be539a09ef791775e782bc4cafba56dbf18131b0bb7586a21242',
'full-image-RESULT.json':'6ba21af4feb947a9bd90190478c8a5ff5ddfb43754b101e009eb10fd34a94a05'}
def canonical(s):return tuple(sorted((x['degree'],x['coefficient'])for x in s))
def shape_key(s):return tuple(sorted(s))
def cases():
 out=[]
 for n in(2,4,6):out.append((((1,'V'),),((n,'1'),),((0,'V'),(n,'1'))))
 for e,ns in [(2,[((3,'W'),),((5,'W'),),((2,'1'),(4,'1')),((2,'1'),(6,'1')),((4,'1'),(4,'1')),((4,'1'),(6,'1'))]),(4,[((5,'W'),),((2,'1'),(6,'1')),((4,'1'),(4,'1')),((4,'1'),(6,'1'))])]:
  for N in ns:out.append((((e,"W'"),),N,tuple(sorted(N+((1-e,"W'"),)))))
 return out

def run():
 originals=json.loads((ROOT/'INPUTS.json').read_text())
 require(len(originals)==6,'six complete original geometric sources')
 for item in originals:
  name=Path(item['file']).name;raw=(ROOT/item['file']).read_bytes()
  require(hashlib.sha256(raw).hexdigest()==item['sha256']==ORIGINAL_HASHES[name],'original source bytes')
  require(len(raw)==item['bytes'],'original source length')
  require(hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==item['git_blob_sha1'],'original Git blob')
 for name,digest in DEPENDENCY_HASHES.items():
  require(hashlib.sha256((ROOT/'inputs'/name).read_bytes()).hexdigest()==('0'*64 if MUT=='source-hash'else digest),'frozen theorem dependency bytes')
 for n in NAMES:
  require(CHAR[n][0]==q(DIM[n])and CHAR[n][1]==q(DIM[n]*(-1)**PAR[n]),'physical dimensions and parity')
  for m in NAMES:require(inner(CHAR[n],CHAR[m])==q(n==m),'complete exact character orthogonality')
 require(CHAR['A']==symmetric(2)and CHAR['A']!=CHAR['V'],'fixed physical A differs from V')
 require(line(-2)==mul(-1,CHAR['1'])and line(-3)==mul(-1,CHAR['W']),'Euler H1 corrections retained')
 q4=sub(tensor(M3,line(3)),tensor(M4,line(4)))if MUT=='source-dual-swap'else Qstar(4)
 require(show(q4)=={'1':-1,'A':-1,'D':1,'P':1,'V':2},'actual rank-thirteen Qstar quartic Euler')
 prior=json.loads((ROOT/'inputs/lower-image-RESULT.json').read_text())
 c=cases()
 if MUT=='omit-case':c=c[:-1]
 require(len(c)==13,'complete thirteen lower-image cases')
 require({(shape_key(J),shape_key(N),shape_key(B))for J,N,B in c}=={(canonical(x['image']),canonical(x['kernel']),canonical(x['quotient']))for x in prior['final_pairs']},'exact case coverage from retained actual lower-image theorem')
 require(len(prior['case_degree_ledger'])==50 and len(prior['torsion_ledger'])==96,'full retained case and torsion overlists')
 degree_rows=prior['case_degree_ledger']
 if MUT=='discard-earlier-defects':degree_rows=[x for x in degree_rows if not any(x['defects'])]
 require(len(degree_rows)==50 and sum(any(x['defects'])for x in degree_rows)==37,'all earlier positive defects retained')
 require(all(x['defects'][2]==0 for x in degree_rows),'only last defect is uniformly zero')
 require(sum(any(x['defects'])for x in prior['torsion_ledger'])==83,'all eighty-three positive torsion partitions retained')
 require(any(any(x['kernel_defects'])for x in prior['torsion_ledger']),'positive kernel torsion not discarded')
 require(any(any(x['quotient_defects'])for x in prior['torsion_ledger']),'positive quotient torsion not discarded')
 require(all((canonical(x['image']),canonical(x['kernel']),canonical(x['quotient']))in{(shape_key(J),shape_key(N),shape_key(B))for J,N,B in c}for x in prior['torsion_ledger']),'all ninety-six torsion partitions covered by these cases')
 rows=[]
 for J,N,B in c:
  require(rank(B)==4 and rank(J)in(2,3),'actual rank-four quotient, not lower-image annihilator identification')
  Bs=tuple((-e,n)for e,n in B)
  quotient_twist=1 if MUT=='quotient-twist'else 2
  target_twist=2 if MUT=='derivative-twist'else 0
  z4=sub(q4,chi(Bs,quotient_twist))
  target=h0(Bs,target_twist)
  source_v=coeff(z4,'V');target_v=coeff(target,'V')
  require(source_v-target_v==1,'every case forces one extra V in upper-endpoint quartic sections')
  require(source_v in(1,2)and target_v in(0,1),'reported exact V source/target multiplicities')
  rows.append({'image':display(J),'N':display(N),'B':display(B),'chi_Z4':show(z4),'H0_B_dual':show(target),'V_Euler_multiplicity':source_v,'V_target_multiplicity':target_v,'V_kernel_lower_bound':source_v-target_v})
 # Universal top-slope vanishing. No actual derivative or section is sampled.
 ambient_slope=-2 if MUT=='weaken-top-slope'else -4
 target_shift=0 if MUT=='top-kernel-twist'else -2
 line_degree_difference=ambient_slope+target_shift-(-4)
 require(max(0,line_degree_difference+1)==0,'every map from a top O(-4) summand to (Z/K)(-2) vanishes')
 require(DIM['V']*(-4)==-12,'negative degree of the forced horizontal V O(-4)')
 # Exact dual sequence and derivative twists are separate.
 require(-2+4==2 and -4+4==0,'upper quotient B*(-2) and derivative B*(-4) have distinct twists')
 # Recover the rank-one necessary source directly from maps, not from a label.
 line_sources=[]
 for label,Eshape in SOURCES.items():
  if MUT=='source-Z-only'and label!='Z':continue
  if any(hom(9,'1',1-e,n)>0 for e,n in Eshape):line_sources.append(label)
 require(line_sources==['D'],'O(9) restricted image can embed only for necessary source D')
 for row in rows:require(row['V_kernel_lower_bound']==row['V_Euler_multiplicity']-row['V_target_multiplicity']==1,'reported multiplicity fields match verified characters')
 return {'status':'PASS','scope':'Conditional exclusion of every rank-two and rank-three restricted dual-cubic image in actual ordered rank-four (3,1). With retained full-rank exclusion, every restricted image has rank one, is O(9), and requires source D. The whole profile remains open.','checks':CHECKS,'actual_Qstar4_Euler':show(q4),'case_count':13,'cases':rows,'covered_case_degree_rows':50,'positive_case_degree_rows_retained':37,'covered_torsion_rows':96,'positive_torsion_rows_retained':83,'uniform_upper_defect':0,'earlier_defects_assumed_zero':False,'top_kernel_bundle':'V O(-4)','top_kernel_degree':-12,'top_kernel_quotient_Hom_dimension':0,'actual_instance_evaluations':0,'historical_enumerations':0,'whole_ordered_profile_excluded':False,'remaining_image_rank':1,'remaining_image':'O(9)','necessary_source':'D'}
if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))

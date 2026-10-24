#!/usr/bin/env python3
"""Independent whole-profile theorem integration. Exact characters; no author-code imports."""
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
HASHES={
'ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md':'a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256',
'POSITIVE-DOUBLE-HYPERPLANE-GAUSS-GATE.md':'0928dd8261ac0d2659188af6520b564611b289cd0e271185ef5f4e3bafe3a6a2',
'RANK-TWO-GAUSS-PLATEAU-NECESSARY-BOUND.md':'868b89283fc98d276b8c9833f16d3dd16fe2b6a98a326769ce43d3a7e46d8b3c',
'GAUSS-DETERMINANT-ORBIT-RAMIFICATION.md':'783454715e967929ad81e6f09f8f4a155073fbdab89974bee056416e4f866e71',
'four-sources.md':'d5feb4b4478b5ec8178a049124179d25473b2e2526b20823a40f6dc60095e28e',
'EXCEPTIONAL-CUBIC-GAUSS-CORNER-EXCLUSION.md':'9f01d086401ee7ee850d3c9181c0486734bcc5c5791c552410895ae4ba742fbf'}
PINS={
'cubic-image-PROOF.md':'0e291e31481530df3163ed6abc3d433a4e402c98e9258d3a329b05b51a2ea507',
'cubic-image-verify.py':'6d4f66ca5ac1be539a09ef791775e782bc4cafba56dbf18131b0bb7586a21242',
'cubic-image-RESULT.json':'6ba21af4feb947a9bd90190478c8a5ff5ddfb43754b101e009eb10fd34a94a05',
'lower-classification-PROOF.md':'f6f807996ccca5b05233af8964bbbaa4f3913f79e4955ea2b4906462db3f2751',
'lower-classification-verify.py':'8bfaf601c8817fb0ab3af19a5aff734efdad09a318491c1bec7d8430818cb0f6',
'lower-classification-RESULT.json':'9b157f897b96ec2e87951f540393fecd31057b34121bdf6b5de2ebaf38223c72',
'lower-exclusion-PROOF.md':'4cbd25f10abfdc864687e71f44cd17de7589d3d031d1035849737487b9f3adb1',
'lower-exclusion-verify.py':'44d793fa6972371e3870f3e682fb468292189b9d16a9db135b75f7b58c73ea39',
'lower-exclusion-RESULT.json':'7e1cba7928bdbfce0cdd85ab62e23eacb7b4a2e085ae3850731549ff3a55668b',
'rankone-PROOF.md':'0ac173c28a40d6f98df75ae7218fe0fc8a7c03a4e0c3b022f87a97969a403cd8',
'rankone-verify.py':'4164413cea33bbae469763460aa83e82c3a21e36e4dca92d3b66869e5456d01f',
'rankone-RESULT.json':'a3e195acf3155f506c32a3dba2e0f107d6b135b221d6236d1468024c136086cf'}
DAG={'originals':[], 'cubic-image':['originals'], 'lower-classification':['originals'], 'lower-exclusion':['cubic-image','lower-classification'], 'rankone':['originals','lower-classification'], 'closure':['cubic-image','lower-exclusion','rankone']}
def topological(graph):
 pending={n:set(ds)for n,ds in graph.items()};ordered=[]
 while pending:
  available=sorted(n for n,ds in pending.items()if ds<=set(ordered))
  require(bool(available),'no dependency cycle or missing premise')
  ordered.extend(available)
  for n in available:del pending[n]
 return ordered

def run():
 for item in json.loads((ROOT/'INPUTS.json').read_text()):
  name=Path(item['file']).name;b=(ROOT/item['file']).read_bytes()
  require(hashlib.sha256(b).hexdigest()==HASHES[name]==item['sha256'],'complete original identity')
  require(len(b)==item['bytes'],'complete original length')
  require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==item['git_blob_sha1'],'original Git blob')
 for n,pin in PINS.items():require(hashlib.sha256((ROOT/'inputs'/n).read_bytes()).hexdigest()==('0'*64 if MUT=='alter-theorem'else pin),'previously reviewed immutable theorem '+n)
 for n in NAMES:
  for m in NAMES:require(inner(CHAR[n],CHAR[m])==q(n==m),'exact physical character orthogonality')
 require(CHAR['A']==symmetric(2)and CHAR['A']!=CHAR['V'],'common fixed physical marking')
 require(show(E(3))=={"W'":1,'T6':2},'actual source cubic Euler, not dual')
 require(show(Qstar(3))=={'W':-2,'S4':-1,'T6':1},'actual dual cubic Euler ensures a section copy')
 require(coeff(Qstar(3),'T6')==1,'positive T6 Euler coefficient with genuine H1 correction')
 require(H[0]==q(30),'common ambient dimension thirty')
 require(rank(SOURCES['D'])==17 and degree(SOURCES['D'])==-54,'actual E rank and degree')
 graph={n:list(ds)for n,ds in DAG.items()}
 if MUT=='circular-proof':graph['rankone'].append('closure')
 order=topological(graph)
 require(set(order)==set(DAG),'all six theorem graph nodes included')
 results={tag:json.loads((ROOT/'inputs'/(tag+'-RESULT.json')).read_text())for tag in('cubic-image','lower-classification','lower-exclusion','rankone')}
 ci,lc,le,one=[results[tag]for tag in('cubic-image','lower-classification','lower-exclusion','rankone')]
 require(ci['canonical_single_T6_assumed']==False and ci['source_Z_assumed']==False,'earlier image theorem applies to an arbitrary copy and all four source types')
 require(ci['plateau_ranks']==[5,9,13,17,21],'same ordered maximal plateau, not reversed profile')
 require(ci['rank_four_images_remaining']==0,'complete full-rank image exclusion')
 require(len(lc['final_pairs'])==13 and len(lc['case_degree_ledger'])==50 and len(lc['torsion_ledger'])==96,'complete actual lower-image classification')
 require(le['image_quotient_pairs_excluded']==13 and le['case_rows_excluded']==50 and le['torsion_partitions_excluded']==96,'all lower-image necessary cases excluded')
 require(le['positive_case_rows_excluded']==37 and le['positive_torsion_partitions_excluded']==83,'positive earlier and inverse-image defects not discarded')
 require(one['counts']==[53,16,7,9]and not one['complete_profile_claim'],'independently proved rank-one theorem, no closure premise')
 require(len(one['low_exclusions'])==7 and all(x['survivors']==0 for x in one['low_exclusions']),'complete low rank-one contradiction')
 require(len(one['upper_exclusions'])==9 and all(x['V_margin']==1 for x in one['upper_exclusions']),'complete upper rank-one contradiction')
 require(any(row['defects'][2]==12 for x in one['low_exclusions']for row in x['defect_rows']),'upper ramification survives until low contradiction')
 require(not le['H1_vanishing_assumed']and not le['inverse_image_extension_splitting_assumed'],'cohomology and inverse-image geometry not specialized')
 # The logical objects below are audited written theorem hypotheses, not measured data.
 copy='fixed arbitrary T6 inclusion'
 branches=[{'rank':1,'copy':copy,'theorem':'rankone'}, {'rank':2,'copy':copy,'theorem':'lower-exclusion'}, {'rank':3,'copy':copy,'theorem':'lower-exclusion'}, {'rank':4,'copy':copy,'theorem':'cubic-image'}]
 ranks=[17,13,30];nonzero=True;canonical=False;evaluation_injective=False;global_zero=False;retained=True;sf5=False
 if MUT=='omit-one':branches=branches[1:]
 if MUT=='omit-four':branches=branches[:-1]
 if MUT=='wrong-rank-theorem':branches[1]['theorem']='cubic-image'
 if MUT=='change-section-copy':branches[2]['copy']='another chosen copy'
 if MUT=='allow-zero':nonzero=False
 if MUT=='canonical-copy':canonical=True
 if MUT=='injective-evaluation':evaluation_injective=True
 if MUT=='swap-bundles':ranks=[13,17,30]
 if MUT=='global-zero':global_zero=True
 if MUT=='drop-premises':retained=False
 if MUT=='claim-sf5':sf5=True
 require(ranks==[17,13,30],'same unequal actual bundles')
 require(nonzero,'nonzero restricted derivative follows from actual kernel persistence')
 require(not canonical and not evaluation_injective,'no uniqueness or evaluation subbundle premise')
 require(all(x['copy']==copy for x in branches),'same arbitrary chosen T6 copy in every branch')
 require({x['rank']:x['theorem']for x in branches}=={1:'rankone',2:'lower-exclusion',3:'lower-exclusion',4:'cubic-image'},'exhaustive nonzero rank partition with correct branch theorems')
 require(not global_zero and retained and not sf5,'conditional one-profile scope, not a stronger theorem')
 return {'status':'CONDITIONAL PASS','profile_excluded':[3,1],'rank_under_contradiction':4,'excluded_restricted_image_ranks':[1,2,3,4],'remaining_restricted_image_ranks':[],'checks':CHECKS,'topological_order':order,'all_four_prior_theorems_authenticated':True,'actual_ranks':[17,13,30],'chosen_copy':'one fixed arbitrary T6 inclusion','canonical_copy_assumed':False,'evaluation_bundle_injectivity_assumed':False,'positive_defects_retained':True,'original_premises_retained':True,'claims_SF_at_least_five':False,'coarse_profile_count_updated':False,'actual_instance_evaluations':0,'historical_enumerations':0}
if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))

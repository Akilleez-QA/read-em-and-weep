#!/usr/bin/env python3
"""Nine frozen originals; two fixed section tests; no historical enumeration."""
from pathlib import Path
from collections import Counter
import hashlib,json,sys
import characters as c
ROOT=Path(__file__).resolve().parent
checks=0
def require(ok,msg):
 global checks
 checks+=1
 if not ok:raise RuntimeError(msg)
for x in json.loads((ROOT/'INPUTS.json').read_text()):
 b=(ROOT/x['file']).read_bytes()
 require(len(b)==x['bytes'],x['file']+' bytes')
 require(hashlib.sha256(b).hexdigest()==x['sha256'],x['file']+' sha256')
 require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==x['git_blob_sha1'],x['file']+' Git blob')
SOURCES={
 'D': [[-2,'D'],[-3,'Wp'],[-3,'T'],[-4,'V'],[-8,'one']],
 'P': [[-2,'P'],[-3,'Wp'],[-3,'T'],[-4,'V'],[-5,'Wp']],
 'V': [[-2,'V'],[-3,'Wp'],[-3,'T'],[-4,'V'],[-4,'V']],
 'zero_top': [[-3,'Wp'],[-3,'T'],[-3,'T'],[-4,'V']]}
def h1(B,t):
 v=Counter()
 for e,R in B:v.update(c.product(R,-e-t-2))
 return v
def chi(B,t):
 v=c.h0(B,t);v.subtract(h1(B,t));return +v, -v
def envelope(A,r):
 v=Counter()
 for i in range(r-1):v.update(c.h0(A,r-2*i))
 return v
def hom(F,R,e):return any(c.product(R,e-f)[S]>0 for f,S in F)
def canon(A):return sorted(map(tuple,A))
base=json.loads((ROOT/'inputs/frontier182.json').read_text())['cases']
p12={r['source_index']:r for r in base if r['profile']=='12'}
p21={r['source_index']:r for r in base if r['profile']=='21'}
expected12={0:[[-10,'one'],[-8,'one'],[14,'one']],2:[[-10,'one'],[2,'one'],[4,'one']],4:[[-10,'one'],[4,'one'],[4,'one']],6:[[-8,'one'],[-8,'one'],[14,'one']],7:[[-8,'one'],[2,'one'],[4,'one']],8:[[-8,'one'],[2,'one'],[6,'one']],12:[[-9,'W'],[14,'one']],14:[[-3,'Wp'],[4,'one']],20:[[-10,'one'],[3,'W']],21:[[-8,'one'],[3,'W']]}
require(set(p12)==set(expected12),'complete original ten IDs')
for i,A in expected12.items():
 require(canon(p12[i]['A'])==canon(A),'profile12 exact shape'+str(i))
 require(canon(p12[i]['B'])==canon([[-e-2,R] for e,R in A]),'profile12 actual transpose'+str(i))
 require(p12[i]['original_defect']==0,'profile12 original defect'+str(i))
for name,E in SOURCES.items():
 require(sum(c.DIM[R] for e,R in E)==17,name+' source rank')
 require(sum(e*c.DIM[R] for e,R in E)==-54,name+' source degree')
 require(min(e for e,R in E)>=-8,name+' min source degree')
 require(sum(c.DIM[R] for e,R in E if e<=-8)<=1,name+' low rank budget')
 require(chi(E,4)==(Counter(V=3,P=3,D=2),Counter()),name+' exact Euler at4')
for i in (0,2,4,12,20):
 block=next((e,R) for e,R in p12[i]['A'] if e<-8)
 require(all(not hom(E,block[1],block[0]) for E in SOURCES.values()),'negative quotient impossible'+str(i))
require(c.visible(p12[8]['A'])[0] is False,'old8 cubic visibility')
require(c.h0(p12[8]['A'],3)==Counter(S=1,T=2),'old8 exact cubic character')
for i,expected in [(7,Counter(A=1,V=2,P=3,D=3)),(21,Counter(A=1,V=2,P=3,D=3)),(14,Counter(V=1,P=3,D=2))]:
 require(envelope(p12[i]['A'],4)==expected,'exact twist4 envelope'+str(i))
 require(expected['V']<3,'V deficit'+str(i))
# Original thirteen ordered profile21 rows, and every source-index association.
expected21={
0:[[-10,'one'],[6,'one'],[6,'one']],1:[[-8,'one'],[2,'one'],[6,'one']],2:[[-8,'one'],[2,'one'],[16,'one']],3:[[-8,'one'],[4,'one'],[6,'one']],4:[[-8,'one'],[4,'one'],[6,'one']],5:[[-8,'one'],[4,'one'],[16,'one']],6:[[-8,'one'],[5,'W']],7:[[-8,'one'],[5,'W']],8:[[-8,'one'],[6,'one'],[6,'one']],9:[[-8,'one'],[6,'one'],[16,'one']],10:[[-8,'one'],[9,'Wp']],11:[[-5,'Wp'],[16,'one']],12:[[-1,'Wp'],[6,'one']]}
require(set(p21)==set(expected21),'complete original13indices')
for i,A in expected21.items():
 require(canon(p21[i]['A'])==canon(A),'profile21 exact shape'+str(i))
 require(p21[i]['original_defect']==(12 if i in (3,6) else 0),'original profile21 defect'+str(i))
 B=([[-18,'one'],[-8,'one'],[6,'one']] if i in (3,6) else [[-e-2,R] for e,R in A])
 require(canon(p21[i]['B'])==canon(B),'original profile21 dual'+str(i))
require(all(not hom(E,'one',-10) for E in SOURCES.values()),'profile21 first row degree obstruction')
for i,expected in [(1,Counter(S=1,T=2)),(8,Counter(S=2,T=2)),(12,Counter(S=1,T=2))]:
 require(c.h0(p21[i]['A'],3)==expected,'profile21 cubic sections'+str(i))
 require(not c.visible(p21[i]['A'])[0],'profile21 primary exclusion'+str(i))
require(c.product('Wp',3)==Counter(V=1,D=1),'Wp Sym3=V+D')
require([k for k,E in SOURCES.items() if hom(E,'Wp',-5)]==['P'],'negative Wp quotient forces exactPsource')
source_trivial=c.h0(SOURCES['P'],10)['one']
target_trivial=envelope(p21[11]['A'],10)['one']
require(source_trivial==4 and target_trivial==3,'fixed r10 trivial deficit')
require([n for n in (26,24,22,20,18,16,14,12,10) if c.product('one',n)['one']]==[24,20,12],'exact invariant list')
for n in (5,3,1):require(c.product('Wp',n)['one']==0,'no trivial Wp term'+str(n))
retain=(2,3,4,5,6,7,9,10)
for i in retain:
 require([-8,'one'] in p21[i]['A'],'retained negative scalar')
 require([name for name,E in SOURCES.items() if hom(E,'one',-8)]==['D'],'same actualDsource forced')
rows=[dict(p21[i],forced_E='D O(-2)+(Wp+T)O(-3)+V O(-4)+O(-8)') for i in retain]
out={'scope':'Direct profile-specific coverage reduction, not COV or global rank3 exclusion','authenticated_originals':9,'checks':checks+c.checks,'profile12_excluded_old_indices':sorted(p12),'profile21_excluded_original_indices':[0,1,8,11,12],'profile21_retained':rows,'profile21_forced_actual_E':'D O(-2)+(Wp+T)O(-3)+V O(-4)+O(-8)','unresolved_profiles':['11','21'],'actual_instance_evaluated':False,'historical_enumeration_rerun':False,'global_rank3_exclusion':False}
text=json.dumps(out,indent=2,sort_keys=True)+'\n'
if '--write' in sys.argv:(ROOT/'RESULT.json').write_text(text)
else:require((ROOT/'RESULT.json').read_text()==text,'exact result replay')
print(text)

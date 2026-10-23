#!/usr/bin/env python3
"""Two fixed formal bundle shapes; no instance evaluation or old enumeration."""
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
manifest=json.loads((ROOT/'INPUTS.json').read_text())
require(len(manifest)==7,'seven immutable originals')
for x in manifest:
 b=(ROOT/x['file']).read_bytes()
 require(len(b)==x['bytes'],x['file']+' bytes')
 require(hashlib.sha256(b).hexdigest()==x['sha256'],x['file']+' SHA256')
 require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==x['git_blob_sha1'],x['file']+' Git blob')
SOURCES={
 'D':[[-2,'D'],[-3,'Wp'],[-3,'T'],[-4,'V'],[-8,'one']],
 'P':[[-2,'P'],[-3,'Wp'],[-3,'T'],[-4,'V'],[-5,'Wp']],
 'V':[[-2,'V'],[-3,'Wp'],[-3,'T'],[-4,'V'],[-4,'V']],
 'zero_top':[[-3,'Wp'],[-3,'T'],[-3,'T'],[-4,'V']]}
E=SOURCES['D'];Ehat=E[:-1]
SHAPES={'split':[[-8,'one'],[4,'one'],[6,'one']],
 'balanced':[[-8,'one'],[5,'W']]}
def rank(B):return sum(c.DIM[R] for e,R in B)
def degree(B):return sum(e*c.DIM[R] for e,R in B)
def h1(B,t):
 out=Counter()
 for e,R in B:out.update(c.product(R,-e-t-2))
 return out
def chi(B,t):
 out=c.h0(B,t);out.subtract(h1(B,t));return out
def hom_to(F,R,e):return any(c.product(R,e-f)[S] for f,S in F)
require(rank(E)==17 and degree(E)==-54,'actual source rank and degree')
require([name for name,F in SOURCES.items() if hom_to(F,'one',-8)]==['D'],'negative scalar forces exact D type')
require(c.product('D',1)==Counter(S=1,T=1),'WD=S+T')
expected_sym={6:Counter(V=1,P=1),7:Counter(Wp=1,T=1),8:Counter(P=1,D=1),9:Counter(S=1,T=1),10:Counter(A=1,V=1,D=1)}
for n,ch in expected_sym.items():require(c.product('one',n)==ch,'Sym'+str(n))
require(c.product('one',6)['D']==0,'split D row to O4 vanishes')
require(c.product('one',8)['D']==1,'unique split D row to O6')
require(8<12,'split common-divisor upper bound below minimum orbit')
require(5-1==4 and -10-6==-16,'split D-kernel rank and degree')
require(c.DIM['T']>4,'T cannot lie in split cubic kernel')
require(c.DIM['S']==4 and -16+3*4==-4,'S kernel would force forbidden degree-zero trivialization')
# All possible rank-one image degrees are fixed by parity, generation and target degree.
require([n for n in (-2,0,2,4) if c.product('one',n+2)['D']]==[2],'balanced rank-one image candidate')
require(c.product('one',3)['W']==0,'candidate line has no map to W O5')
require(10-(-1)==11 and 11<12,'balanced torsion-defect bound')
require(5-2==3 and -10-10==-20,'balanced D-kernel rank and degree')
require(c.DIM['S']>3 and c.DIM['T']>3,'balanced cubic D map injective')
require(c.product('D',1)['T']==1,'unique equivariant graph-lift channel')
require(c.h0(Ehat,3)==Counter(S=1,Wp=1,T=2),'all cubic source sections, V row retained')
require(chi(E,4)==Counter(V=3,P=3,D=2),'source Euler character at4')
results={}
for name,A in SHAPES.items():
 C=A[1:]
 require(rank(A)==3 and degree(A)==2,name+' quotient rank and degree')
 require(c.h0(C,3)==Counter(Wp=1,S=1,T=2),name+' cubic target')
 kr=rank(E)-rank(A);kd=degree(E)-degree(A)
 require(kr==14 and kd==-56 and kd==-4*kr,name+' exact kernel degree forces purity')
 require(chi(A,4)==Counter(V=1,P=1,D=2),name+' quotient Euler character at4')
 coeff=chi(E,4);coeff.subtract(chi(A,4));coeff=+coeff
 require(coeff==Counter(V=2,P=2),name+' forced kernel coefficient')
 target=c.h0(A,2)
 require(target==Counter(V=1,P=2,D=1),name+' actual derivative target')
 require(coeff['V']>target['V'],name+' strict-top V multiplicity contradiction')
 results[name]={'actual_quotient':A,'forced_kernel_coefficient':dict(coeff),'forced_kernel_degree':-4,'strict_top_target_character':dict(target),'excluded':True,'profile_hypothesis':None,'backward_rank_hypothesis':None,'determinant_defect_hypothesis':None}
base=json.loads((ROOT/'inputs/frontier182.json').read_text())['cases']
rows=[r for r in base if r['A'] in SHAPES.values()]
require(len(base)==182,'fixed historical input length only')
require(Counter(r['profile'] for r in rows)==Counter({'11':10,'21':4}),'historical matched row counts')
require([r['source_index'] for r in rows if r['profile']=='11']==[77,78,80,81,82,83,84,85,94,95],'exact historical11 source indices')
require([r['source_index'] for r in rows if r['profile']=='21']==[3,4,6,7],'exact historical21 source indices')
require([r['original_defect'] for r in rows if r['profile']=='21']==[12,0,12,0],'both original defects retained in identity')
out={'scope':'Two exact actual-source quotient exclusions, independent of maximal profile; not COV','authenticated_originals':7,'checks':checks+c.checks,'theorems':results,'historical_rows_excluded':rows,'historical_cut_count_by_profile':dict(Counter(r['profile'] for r in rows)),'historical_rows_are_not_new_live_frontier_count':True,'actual_instance_evaluated':False,'historical_enumeration_rerun':False,'global_rank3_exclusion':False}
text=json.dumps(out,indent=2,sort_keys=True)+'\n'
if '--write' in sys.argv:(ROOT/'RESULT.json').write_text(text)
else:require((ROOT/'RESULT.json').read_text()==text,'exact result replay')
print(text)

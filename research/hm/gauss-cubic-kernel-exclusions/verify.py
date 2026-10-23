#!/usr/bin/env python3
"""Fixed universal character checks only; no source-instance evaluation."""
from pathlib import Path
import sys, json, hashlib
from collections import Counter
import characters as c
ROOT=Path(__file__).resolve().parent
checks=0

def require(ok,msg):
    global checks
    checks+=1
    if not ok: raise RuntimeError(msg)

def sub(x,y):
    z=x.copy(); z.subtract(y); return z

def h1(blocks,t):
    z=Counter()
    for e,r in blocks: z.update(c.product(r,-e-t-2))
    return z

def euler(blocks,t): return sub(c.h0(blocks,t),h1(blocks,t))
def same(x,y): return not any(sub(x,Counter(y)).values())
def rank(B):return sum(c.DIM[r] for e,r in B)
def degree(B):return sum(e*c.DIM[r] for e,r in B)
def hom_to(F,R,e):return any(c.product(R,e-f)[S] for f,S in F)

manifest=json.loads((ROOT/'INPUTS.json').read_text())
require(len(manifest)==8,'eight complete immutable originals')
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
E=SOURCES['D']
require(rank(E)==17 and degree(E)==-54,'actual D-type rank and degree')
require([name for name,F in SOURCES.items() if hom_to(F,'one',-8)]==['D'],'negative scalar forces exact D type')
require(same(c.product('D',1),{'S':1,'T':1}),'WD=S+T')
require(c.DIM['T']>c.DIM['D']-1,'top T cannot lie in cubic top kernel')
require(c.DIM['S']==c.DIM['D']-1,'nonzero S kernel forces full rank-four kernel')
require(c.product('D',1)['T']==1,'unique graph-lift T channel')
require(same(c.h0(E,3),{'S':1,'Wp':1,'T':2}),'exact cubic source character')
require(-2*c.DIM['D']-(-3*c.DIM['S'])==2,'forced coherent image degree two')
require(c.product('one',4)==Counter(D=1),'forced line image gives complete quartic system')
require(same(c.product('one',2),{'A':1}),'Sym2')
require(same(c.product('one',6),{'V':1,'P':1}),'Sym6')
require(same(c.product('one',8),{'P':1,'D':1}),'Sym8')
require(same(euler(E,4),{'V':3,'P':3,'D':2}),'actual source Euler character at4')

A8=[[-8,'one'],[4,'one'],[8,'one']]
A10=[[-8,'one'],[4,'one'],[10,'one']]
expected=[
    ('A8',100,A8,{'A':1,'V':2,'P':1,'D':1},{'one':1,'P':2,'D':2}),
    ('A10',106,A10,{'one':1,'A':1,'V':1,'P':2,'D':1},{'V':1,'P':2,'D':2}),
]
base=json.loads((ROOT/'inputs/frontier182.json').read_text())['cases']
require(len(base)==182,'fixed historical input length')
matched=[r for r in base if r['A'] in [A8,A10]]
require([r['source_index'] for r in matched]==[98,100,104,106],'four exact historical source indices')
require(all(r['profile']=='11' for r in matched) and [r['original_defect'] for r in matched]==[12,0,12,0],'historical profile and defect identities')
results=[]
for name,i,A,h,ch in expected:
    require(c.h0(A,-2)['one']==0,name+' Hom_G(O(2),A) vanishes')
    require(same(c.h0(A,2),h),name+' quadratic target character')
    require(same(euler(A,4),ch),name+' fourth-twist Euler target character')
    envelope=c.h0(A,2); envelope.update(euler(A,4)); envelope.subtract(euler(E,4))
    require(envelope['V']==-1,name+' tightened envelope fails at V')
    results.append({'name':name,'A':A,'Hom_from_O2_dimension':0,'H0_A2':dict(c.h0(A,2)),
                    'chi_A4':dict(euler(A,4)),'chi_K4':dict(sub(euler(E,4),euler(A,4))),
                    'fourth_twist_envelope':dict(envelope),'excluded':True,
                    'profile_hypothesis':None,'backward_rank_hypothesis':None,'determinant_defect_hypothesis':None})
out={'scope':'Two exact actual-source quotient exclusions, independent of maximal profile; not COV',
     'authenticated_originals':len(manifest),'checks':checks+c.checks,'theorems':results,
     'historical_rows_excluded':matched,'historical_cut_count_by_profile':dict(Counter(r['profile'] for r in matched)),
     'historical_rows_are_not_new_live_frontier_count':True,'actual_instance_evaluated':False,
     'historical_enumeration_rerun':False,'global_rank3_exclusion':False}
text=json.dumps(out,indent=2,sort_keys=True)+'\n'
if '--write' in sys.argv:(ROOT/'RESULT.json').write_text(text)
else:require((ROOT/'RESULT.json').read_text()==text,'exact result replay')
print(text)

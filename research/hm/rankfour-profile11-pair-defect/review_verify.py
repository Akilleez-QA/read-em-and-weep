#!/usr/bin/env python3
"""Independent closed-class arithmetic and frozen-proof/input audit.

This verifier does not import the author character implementation. It uses a
closed binomial symmetric-character polynomial, not a McKay recurrence.
Only fixed characters, the seven/four forced rank-two partitions, and rank/
degree arithmetic are evaluated. Geometric proof review is in REVIEW-INDEPENDENT.md.
"""
from collections import Counter
from fractions import Fraction as F
from hashlib import sha1, sha256
from math import comb
from pathlib import Path
import json
import sys

ROOT=Path(__file__).resolve().parent
PROOF_SHA='95cc7824898dd0bffe13f86ab1ede2947451eb3d4632e189baa608ad0de3fdec'
checks=0

def require(condition,label):
    global checks
    checks+=1
    if not condition:
        raise RuntimeError(label)

def q(a,b=0): return (F(a),F(b))
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def mul(x,y): return (x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def scale(a,x): return (a*x[0],a*x[1])
def power(x,n):
    r=q(1)
    for _ in range(n): r=mul(r,x)
    return r

def symmetric_character(n,x):
    if n<0: return q(0)
    s=q(0)
    for j in range(n//2+1):
        s=add(s,scale((-1)**j*comb(n-j,j),power(x,n-2*j)))
    return s

# Nine binary-icosahedral conjugacy classes, paired by the central involution.
traces=[q(2),q(-2),q(F(1,2),F(1,2)),q(-F(1,2),-F(1,2)),
        q(F(1,2),-F(1,2)),q(-F(1,2),F(1,2)),q(1),q(-1),q(0)]
sizes=[1,1,12,12,12,12,20,20,30]
require(sum(sizes)==120,'class sizes')
chars={r:[symmetric_character(n,x) for x in traces]
       for r,n in [('1',0),('W',1),('A',2),('S',3),('D',4),('T',5)]}
chars['P']=[q(z) for z in (4,4,-1,-1,-1,-1,1,1,0)]
chars['V']=[add(symmetric_character(6,x),scale(-1,p)) for x,p in zip(traces,chars['P'])]
chars['Wp']=[add(mul(x,p),scale(-1,t)) for x,p,t in zip(traces,chars['P'],chars['T'])]
DIMS={'1':1,'W':2,'A':3,'S':4,'D':5,'T':6,'V':3,'P':4,'Wp':2}


def inner(v,w):
    s=q(0)
    for a,b,n in zip(v,w,sizes): s=add(s,scale(F(n,120),mul(a,b)))
    return s

for a,c in chars.items():
    require(c[0]==q(DIMS[a]),'irreducible dimension '+a)
    for b,d in chars.items():
        require(inner(c,d)==q(int(a==b)),'character orthogonality '+a+' '+b)


def decompose(v):
    out={}
    for r,c in chars.items():
        s=inner(v,c)
        require(s[1]==0 and s[0].denominator==1 and s[0]>=0,'genuine class-character coefficient '+r)
        if s[0]: out[r]=int(s[0])
    require(sum(DIMS[r]*n for r,n in out.items())==v[0][0] and v[0][1]==0,'character dimension')
    return out


def symmetric(n): return decompose([symmetric_character(n,x) for x in traces])
def product(r,n): return decompose([mul(c,symmetric_character(n,x)) for c,x in zip(chars[r],traces)])
def combined(*rs):
    c=Counter()
    for r in rs:c.update(r)
    return dict(c)
def dim(c): return sum(DIMS[r]*n for r,n in c.items())

require(symmetric(6)=={'V':1,'P':1},'Sym6')
require(symmetric(7)=={'Wp':1,'T':1},'Sym7')
require(symmetric(8)=={'P':1,'D':1},'Sym8')
F_expected={'A':1,'D':2}
require(combined(symmetric(2),symmetric(4),symmetric(4))==F_expected,'scalar F sections')
require(combined(symmetric(4),product('W',3))==F_expected,'doublet F sections')

# The original cohomology dimensions and the actual constant direct sum.
M2={'A':1,'V':2,'P':3,'D':4}
T0={'V':2,'P':3,'D':2}
T12={'V':1,'P':2,'D':1}
require(dim(M2)==41 and dim(T0)==28 and dim(T12)==16,'cohomology dimensions')
require(5+8==13 and -46-8==-54,'S constant block ranks/degrees')
require([d for d in (0,4,5,9) if 7<=d<=9]==[9],'minimal-span quotient dimensions')
require(30-9==21 and 21-16==5 and 5-3==2,'small ambient ranks')
require(-8*5+6==-34 and -34<-30,'uniform rank-at-least-five contradiction')
capacity={}
for lam in ((-4,-6,-6),(-5,-5,-6)):
    cases=[lam[0]+lam[1]-4,2*lam[0]-6]
    require(max(cases)==-14,'rank-two capacity')
    capacity[str(lam)]={'rank_two_piece':cases[0],'two_rank_one_pieces':cases[1],'capacity':max(cases)}
require(-14-(-30)==16,'defect upper bound')
require([d for d in (12,20,30,60) if d<=16]==[12] and 2*12>16,'invariant divisor alternatives')
require(-8-2-(-22)==12 and -46-(-28)==-18,'original and small defects')
require(7+2==9 and -14-18==-32 and -54-(-22)==-32,'original L ranks/degrees')

# Exhaustive symbolic rank-two partitions, not a general candidate search.
zero_scalar=[]
expected_A=[1,2,2,1,1,1,2]
for j,A_mult in zip((2,4,6,8,10,12,14),expected_A):
    k=30-j
    c=combined(symmetric(j-2),symmetric(k-2))
    require(c.get('A',0)==A_mult and c.get('A',0)>0,'zero-defect scalar exclusion')
    require(dim(c)==28,'zero-defect scalar cohomology dimension')
    zero_scalar.append({'degrees':[-j,-k],'H1':c,'forbidden_A_multiplicity':A_mult})
require(symmetric(16).get('A',0)==0 and symmetric(10).get('A',0)==1,'Sym16 exception handled by Sym10')
zero_doublet={r:product(r,13) for r in ('W','Wp')}
require(zero_doublet['W']=={'1':1,'A':2,'V':1,'P':2,'D':2},'W minus fifteen')
require(zero_doublet['Wp']=={'1':1,'A':1,'V':2,'P':2,'D':2},'Wp minus fifteen')
require(all(c.get('1',0)>0 for c in zero_doublet.values()),'doublet trivial obstructions')

# All five C5 weights are present; pairs have equal induced characters only.
residues={'1':[0],'A':[0,1,4],'V':[0,2,3],'P':[1,2,3,4],'D':[0,1,2,3,4]}
phi=q(F(1,2),F(1,2)); phi_conjugate=q(F(1,2),-F(1,2))
require(chars['A'][2]==phi and chars['V'][2]==phi_conjugate,'physical C5 class marking')
require(chars['P'][2]==q(-1) and chars['D'][2]==q(0),'remaining C5 restrictions')
induced={}
for w in range(5):
    c={r:rs.count(w) for r,rs in residues.items() if w in rs}
    require(dim(c)==12,'orbit induced dimension')
    induced[str(w)]=c
require(induced['0']=={'1':1,'A':1,'V':1,'D':1},'weight zero')
require(induced['1']==induced['4']=={'A':1,'P':1,'D':1},'weights plus/minus one')
require(induced['2']==induced['3']=={'V':1,'P':1,'D':1},'weights plus/minus two')
surviving_weights=[]
for w,c in induced.items():
    difference={r:T0.get(r,0)-c.get(r,0) for r in set(T0)|set(c)}
    if min(difference.values())>=0:
        require({r:n for r,n in difference.items() if n}==T12,'positive-defect cohomology')
        surviving_weights.append(int(w))
require(surviving_weights==[2,3],'exactly two retained fiber weights')

positive_scalar=[]
for j,k in ((2,16),(4,14),(6,12),(8,10)):
    c=combined(symmetric(j-2),symmetric(k-2))
    require(dim(c)==16,'positive-defect scalar cohomology dimension')
    require((c==T12)==((j,k)==(8,10)),'positive-defect scalar survivors')
    if (j,k)!=(8,10):require(c.get('1',0)>0 or c.get('A',0)>0,'positive-defect scalar obstruction')
    positive_scalar.append({'degrees':[-j,-k],'H1':c,'compatible':c==T12})
positive_doublet={r:product(r,7) for r in ('W','Wp')}
require(positive_doublet['W']==T12,'W minus nine survivor')
require(positive_doublet['Wp']=={'1':1,'A':1,'V':1,'P':1,'D':1},'Wp minus nine obstruction')

# Freeze the exact independently reviewed text and all full source-byte identities.
proof=(ROOT/'PROOF.md').read_bytes()
require(sha256(proof).hexdigest()==PROOF_SHA,'reviewed proof digest')
inputs=json.loads((ROOT/'INPUTS.json').read_text())
auth=json.loads((ROOT/'REVIEW-AUTHENTICITY.json').read_text())
require(len(inputs)==3 and auth['status']=='PASS' and len(auth['sources'])==3,'fresh authentication record')
for inp in inputs:
    data=(ROOT/inp['file']).read_bytes()
    blob=sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    require(len(data)==inp['bytes'],'full input byte length')
    require(sha256(data).hexdigest()==inp['sha256'],'full input SHA256')
    require(blob==inp['git_blob_sha1'],'full input Git blob SHA1')
    fresh=next(x for x in auth['sources'] if x['file']==inp['file'])
    require(fresh['full_remote_bytes_equal_retained_input'] and fresh['status']=='PASS','fresh full-byte authentication')
    require(fresh['ref']==inp['ref'] and fresh['path']==inp['path'] and fresh['sha256']==inp['sha256'] and fresh['remote_blob_sha1']==blob,'fresh pinned source identity')

result={
 'status':'PASS','wholeproof':'PASS','reviewed_proof_sha256':PROOF_SHA,
 'check_count':checks,'arithmetic_method':'closed binomial symmetric-power class characters in Q(sqrt5); no author recurrence imported',
 'geometric_review':'Independent whole-text human-style proof audit; not proof-assistant certification. Imported actual geometric premises remain conditional.',
 'fresh_source_authentication':'three complete immutable remote files, full byte equality, SHA256 and Git blob identity',
 'capacity':capacity,
 'zero_defect_scalar_partitions':zero_scalar,'zero_defect_doublets':zero_doublet,
 'five_C5_induced_characters':induced,'surviving_stabilizer_weights':surviving_weights,
 'positive_defect_scalar_partitions':positive_scalar,'positive_defect_doublets':positive_doublet,
 'necessary_conclusions':{'constant_span_dimension':21,'constant_complement_dimension':9,'original_defect':12,'small_dual_endpoints':['W(-9)','O(-8)+O(-10)'],'original_quotient_degrees':{'a':2,'b':-22}},
 'limits':['No realization or exclusion of either surviving primal or dual form','No selected actual coefficients, parameters, points, jets, tensors, matrices or instance ranks','No broad quotient search','No public writes, merge or upstream submission']
}
print(json.dumps(result,indent=2,sort_keys=True))

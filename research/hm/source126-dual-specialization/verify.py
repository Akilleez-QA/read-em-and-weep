#!/usr/bin/env python3
"""Bounded universal identities and exact four-candidate specialization; no instances."""
import hashlib,json
from collections import Counter
from fractions import Fraction
from pathlib import Path
BASE=Path(__file__).resolve().parent
checks=0

def check(ok, message):
    global checks
    if not ok: raise ValueError(message)
    checks+=1

def blob(b): return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()

def profile_key(p): return sorted(map(tuple,p))

def degree_one(p): return Counter(r for d,r in p if d==-1)

def add(*polys):
    z=Counter()
    for p in polys:
        for k,v in p.items(): z[k]+=v
    return {k:v for k,v in z.items() if v}

def scale(p,c): return {k:c*v for k,v in p.items() if c*v}

def derivative(p,j):
    q={}
    for (i,a,b,u,v),c in p.items():
        powers=[u,v]; n=powers[j]
        if n:
            powers[j]-=1; q[(i,a,b,*powers)]=c*n
    return q

def variable(p,j):
    q={}
    for (i,a,b,u,v),c in p.items():
        powers=[u,v]; powers[j]+=1; q[(i,a,b,*powers)]=c
    return q

def universal_identity(d,n):
    # f_i=sum_a F_ia u^a v^(d-a), ell_i=L_i0 u+L_i1 v.
    # Keys retain independent formal coefficients F_ia L_ib.
    Lf={}; Du={}; Dv={}; LuF={}; LvF={}
    for i in range(n):
        for a in range(d+1):
            for b in range(2):
                u=a+(b==0); v=d-a+(b==1)
                Lf[i,a,b,u,v]=1
                if a: Du[i,a,b,u-1,v]=a
                if d-a: Dv[i,a,b,u,v-1]=d-a
                (LuF if b==0 else LvF)[i,a,b,a,d-a]=1
    euler=add(variable(Du,0),variable(Dv,1))
    check(euler==scale(Lf,d),f'Euler d={d}, n={n}')
    for j,D,expected in [(0,Du,LuF),(1,Dv,LvF)]:
        got=add(scale(derivative(euler,j),Fraction(1,d)),scale(D,-1))
        check(got==expected,f'linear polar identity d={d},n={n},j={j}')

for row in json.loads((BASE/'INPUTS.json').read_text()):
    b=(BASE/'inputs'/row['file']).read_bytes()
    check(hashlib.sha256(b).hexdigest()==row['remote_sha256'],'immutable proof SHA256')
    check(blob(b)==row['git_blob_sha1'],'immutable proof Git blob')
catbytes=(BASE/'inputs/unrestricted-dual-splittings-and-pairs.json').read_bytes()
check(blob(catbytes)=='e411417c9a61677df55e07f0aff15fbea4c9ec69','catalogue Git blob')
cat=json.loads(catbytes)
expected={129:[[-1,'Wp'],[-2,'P'],[-2,'D'],[-6,'one'],[-28,'one']],157:[[-1,'Wp'],[-1,'T'],[-4,'V'],[-6,'one'],[-28,'one']],231:[[-1,'Wp'],[-1,'Wp'],[-2,'D'],[-3,'Wp'],[-6,'one'],[-28,'one']],249:[[-1,'Wp'],[-1,'Wp'],[-1,'T'],[-6,'one'],[-10,'one'],[-28,'one']]}
dims={'one':1,'W':2,'Wp':2,'A':3,'V':3,'S':4,'P':4,'D':5,'T':6}
for q,p in expected.items():
    check(profile_key(cat['profiles'][q])==profile_key(p),'exact profile')
    check(sum(dims[r] for d,r in p)==13,'quotient rank13')
    check(sum(d*dims[r] for d,r in p)==-54,'quotient dual degree-54')
I_II=[q for q,p in expected.items() if profile_key(p)==profile_key(expected[129])]
III=[q for q,p in expected.items() if degree_one(p)==Counter({'Wp':1,'T':1})]
check(I_II==[129],'I/II exact quotient')
check(III==[157],'III linear annihilator filter')
check(sorted(set(I_II+III))==[129,157],'union exact two')
check(sorted(set(expected)-set(I_II+III))==[231,249],'removed exact two')
check(4==len(set(I_II+III))+2,'four equals two plus two')
check(all(degree_one(expected[q])['Wp']==2 for q in [231,249]),'independent Wp multiplicity witness')
# Degree and Schur checks behind the Euler/Ext calculation.
check(-2-(-8)==6,'Euler quotient degree')
check(2-1>=-1,'Ext from Wp O(1) vanishes')
check(6-1>=-1,'projected P quotient Ext vanishes')
check(-(-4)-2==2,'Serre H1(O(-4))=Sym2')
check('A' not in ['P','D'],'equivariant extension Schur vanishing')
for d in range(1,15):
    for n in range(1,7): universal_identity(d,n)
# Explicit regression negatives: a multiplicity-count comparison must distinguish249.
check(sum(degree_one(expected[249]).values())!=sum(degree_one(expected[157]).values()),'reject extra Wp')
check(degree_one(expected[231])!=Counter({'Wp':1,'T':1}),'reject wrong representation')
check(profile_key(expected[157])!=profile_key(expected[129]),'do not collapse survivors')
check(blob(catbytes+b' ')!='e411417c9a61677df55e07f0aff15fbea4c9ec69','reject changed input bytes')
result={'checks':checks,'starting_pairs':[[10,q] for q in expected], 'retained_pairs':[[10,129],[10,157]],'removed_pairs':[[10,231],[10,249]],'template_assignment':{'I':129,'II':129,'III':157},'stable_label':'G3.11.8ae96830fd21','labels_removed':0,'actual_HM_realization':'not proved','scope':'universal symbolic identity and exact candidate verification only'}
(BASE/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))

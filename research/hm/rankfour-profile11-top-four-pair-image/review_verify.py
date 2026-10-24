#!/usr/bin/env python3
"""Independent finite universal-character and exact-sequence bookkeeping audit.
Closed class characters, no McKay recurrence; no actual-instance computation.
The only atom check is the local eight-dimensional H1 budget in this proof.
"""
from fractions import Fraction as Fr
from math import comb
from pathlib import Path
import hashlib, json
ROOT=Path(__file__).resolve().parent
checks=0

def require(test,label):
    global checks
    checks += 1
    if not test: raise RuntimeError(label)

def q(a,b=0): return (Fr(a),Fr(b))
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def scale(a,x): return (a*x[0],a*x[1])
def mul(x,y): return (x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def power(x,n):
    out=q(1)
    for _ in range(n): out=mul(out,x)
    return out
def total(xs):
    out=q(0)
    for x in xs: out=add(out,x)
    return out
# Closed Chebyshev polynomial evaluated on the nine binary-icosahedral classes.
traces=[q(2),q(-2),q(Fr(1,2),Fr(1,2)),q(Fr(-1,2),Fr(-1,2)),
        q(Fr(1,2),Fr(-1,2)),q(Fr(-1,2),Fr(1,2)),q(1),q(-1),q(0)]
sizes=[1,1,12,12,12,12,20,20,30]
def sym(n):
    if n<0:return tuple(q(0) for _ in traces)
    return tuple(total(scale((-1)**k*comb(n-k,k),power(x,n-2*k))
                       for k in range(n//2+1)) for x in traces)
def plus(*cs): return tuple(total(xs) for xs in zip(*cs)) if cs else sym(-1)
def scaled(k,c):return tuple(scale(k,x) for x in c)
def times(c,d):return tuple(mul(x,y) for x,y in zip(c,d))
chars={'1':sym(0),'W':sym(1),'A':sym(2),'S':sym(3),'D':sym(4),'T':sym(5),
       'P':tuple(q(x) for x in [4,4,-1,-1,-1,-1,1,1,0])}
chars['V']=plus(sym(6),scaled(-1,chars['P']))
chars['Wp']=plus(times(chars['W'],chars['P']),scaled(-1,chars['T']))
names=['1','W','Wp','A','V','P','S','D','T']
dims=dict(zip(names,[1,2,2,3,3,4,4,5,6]))
parity={'1':0,'W':1,'Wp':1,'A':0,'V':0,'P':0,'S':1,'D':0,'T':1}
def inner(c,d):return scale(Fr(1,120),total(scale(s,mul(x,y)) for s,x,y in zip(sizes,c,d)))
def decomp(c):
    out={}
    for r in names:
        v=inner(chars[r],c)
        require(v[1]==0 and v[0].denominator==1,'integer multiplicity '+r)
        if v[0]:out[r]=int(v[0])
    require(plus(*(scaled(n,chars[r]) for r,n in out.items()))==c,'character reconstruction')
    return out

def rep(**ds):return plus(*(scaled(n,chars[r]) for r,n in ds.items()))
def prod(r,n):return times(chars[r],sym(n))
def chi_line(n):return sym(n) if n>=0 else scaled(-1,sym(-n-2))
def chi(bs,t):return plus(*(times(chars[r],chi_line(d+t)) for r,d in bs))
def h0(bs,t):return plus(*(prod(r,d+t) for r,d in bs))
def h1(bs,t):return plus(*(prod(r,-d-t-2) for r,d in bs if d+t<=-2))
def hom(r,d,u,e):return decomp(prod(u,e-d)).get(r,0)
def contained(c,d):return all(n>=0 for n in decomp(plus(d,scaled(-1,c))).values())
def rk(bs):return sum(dims[r] for r,d in bs)
def degree(bs):return sum(dims[r]*d for r,d in bs)

require(sum(sizes)==120,'class-size sum')
for r in names:
    require(chars[r][0]==q(dims[r]),'dimension '+r)
    require(chars[r][1]==q((-1)**parity[r]*dims[r]),'central parity '+r)
    for s in names:require(inner(chars[r],chars[s])==q(int(r==s)),'orthonormal character table')
require(sum(d*d for d in dims.values())==120,'complete irreducible dimensions')
require(times(chars['Wp'],chars['Wp'])==rep(**{'1':1,'V':1}),'physical V marking')

ED=[('D',-2),('Wp',-3),('T',-3),('V',-4),('1',-8)]
E0=ED[:-1]
K=[('S',-3),('V',-4),('V',-4),('Wp',-5),('1',-10)]
Fs={'scalar':[('1',4),('1',4),('1',2)],'standard_doublet':[('1',4),('W',3)]}
quotients={name:F+[('1',-8)] for name,F in Fs.items()}
require((rk(ED),degree(ED),rk(E0),degree(E0),rk(K),degree(K))==(17,-54,16,-46,13,-56),'bundle rank-degree identities')
require(h0(K,3)==chars['S'],'cubic K')
require(h0(K,2)==sym(-1),'strict top')
require(chi(ED,3)==rep(Wp=1,T=2),'source cubic Euler')
require(chi(ED,4)==rep(V=3,P=3,D=2),'source quartic Euler')
records={}
for name,Aq in quotients.items():
    F=Fs[name]
    require((rk(Aq),degree(Aq))==(4,2),'quotient rank degree')
    require(plus(chi(ED,3),scaled(-1,chi(Aq,3)))==rep(S=1,Wp=-1,T=-1),'kernel cubic Euler')
    require(plus(chi(ED,4),scaled(-1,chi(Aq,4)))==rep(A=1,V=2),'kernel quartic Euler')
    require(h0(Aq,1)==rep(S=1,T=2),'cubic-row target')
    require(h0(Aq,2)==rep(V=2,P=2,D=1),'quartic-row target')
    require(plus(chi(ED,0),scaled(-1,chi(Aq,0)))==chi(K,0),'kernel total Euler')
    require(chi(F,2)==rep(V=2,P=2,D=1),'positive F sections twist two')
    require(plus(chi(F,0),scaled(-1,chi([('1',2)],0)))==chi([('1',4),('1',4)],0),'j quotient Euler')
    require(sum(hom('1',2,r,d) for r,d in F)==1,'unique j')
    require(sum(hom('S',-3,r,d-2) for r,d in F)==1,'unique S derivative row')
    require((rk(F),degree(F))==(3,10),'positive quotient rank degree')
    require((rk(F),degree(F)-2*rk(F))==(3,4),'image rank degree')
    records[name]={'Aq_sections_1':decomp(h0(Aq,1)), 'Aq_sections_2':decomp(h0(Aq,2)),
                   'chi_K3':decomp(plus(chi(ED,3),scaled(-1,chi(Aq,3)))),
                   'chi_K4':decomp(plus(chi(ED,4),scaled(-1,chi(Aq,4))))}

# Exhaust only the local eight-dimensional genuine H1(N(3)) budget.
# Each atom R(-j), j>=5, obeys (j-4)*dim R<=8, hence j<=12.
budget=rep(Wp=1,T=1)
atoms=[]
for j in range(5,13):
    for r in names:
        if parity[r]!=j%2 or (j-4)*dims[r]>8:continue
        if contained(prod(r,j-5),budget):atoms.append((r,-j))
expected=[('Wp',-5),('T',-5),('V',-6),('P',-6),('Wp',-7),('1',-10),('1',-12)]
require(atoms==expected,'seven local H1 atoms')
# Literal six partitions forced by the two irreducible budget multiplicities.
possible_tails=[ [('Wp',-5),('T',-5)], [('Wp',-5),('V',-6)],
                 [('Wp',-5),('Wp',-7)], [('Wp',-5),('1',-10)],
                 [('P',-6)], [('1',-12)] ]
tail_records=[]
for N in possible_tails:
    require(h1(N,3)==budget,'tail meets budget exactly')
    R4=plus(rep(V=2,D=-1),h1(N,4))
    cs=decomp(R4)
    tail_records.append({'N':N,'H1_N4':decomp(h1(N,4)),'R4':cs,'genuine':all(n>=0 for n in cs.values())})
require([x['N'] for x in tail_records if x['genuine']]==[[('Wp',-5),('1',-10)]],'unique genuine quartic coefficient')
require(h1(K[3:],4)==chars['D'],'forced H1 quartic')
require(plus(rep(A=1,V=2),scaled(-1,prod('S',1)),h1(K[3:],4))==rep(V=2),'forced R4')
require(not contained(rep(S=1),rep(Wp=1,T=1)),'R3 zero would give forbidden negative S multiplicity')

# Fixed source row factorization and its canonical binary evaluation sequences.
require([hom('S',-3,r,d) for r,d in ED]==[1,0,0,0,0],'S sits only in D row')
require(prod('D',1)==rep(S=1,T=1),'D times W')
require(prod('S',1)==rep(A=1,D=1),'S times W')
require(hom('1',2,'1',4)==0,'j has zero scalar-top components')
require(hom('1',2,'W',3)==1,'Euler j row unique')
require(hom('S',-3,'1',0)==1,'full cubic evaluation row unique')
require(hom('V',-4,'1',2)==1,'sextic V row unique')
require(sym(6)==rep(V=1,P=1),'sextic V plus P')
require(h0([('1',4)],0)==chars['D'],'j-twist section kernel D')
require(hom('V',-4,'1',-10)==0 and hom('S',-3,'1',-10)==0,'top rows have zero negative component')
require(all(hom(r,d,'1',-8)==0 for r,d in E0),'negative quotient projection only source tail')
require(hom('1',-8,'1',-8)==1,'nonzero source tail scalar')
require(60//5==12 and 6<12,'sextic degree below minimum A5 orbit size')
require(rk(K)-3==10 and degree(K)-4==-60,'actual derivative kernel rank degree')
require(degree(K)+10==-46 and rk(K)+3==16,'forward-pair rank degree')

# Authenticate the four full immutable local sources and the frozen first slice.
source_checks=[]
for m in json.loads((ROOT/'INPUTS.json').read_text()):
    b=(ROOT/m['file']).read_bytes()
    sha=hashlib.sha256(b).hexdigest()
    blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
    require(sha==m['sha256'] and len(b)==m['bytes'] and blob==m['git_blob_sha1'],'immutable source '+m['file'])
    source_checks.append({'file':m['file'],'sha256':sha,'git_blob_sha1':blob,'pass':True})
first_hash=hashlib.sha256((ROOT/'inputs/top-four-reduction.md').read_bytes()).hexdigest()
require(first_hash=='56bb8a0aa5ada0f550e0967ef9e535838e9162c2ff2e5ced039a3f6ddb2aacf0','first reduction hash')
proof=ROOT/'PROOF.md'
proof_sha=hashlib.sha256(proof.read_bytes()).hexdigest() if proof.exists() else None
require(proof_sha=='db1e23909dbabd423cbeb855f0f376e7e0fac53d557fdd8aef7685b5449edfdb','reviewed proof fingerprint')
auth=json.loads((ROOT/'REVIEW-AUTHENTICITY.json').read_text())
require(auth['status']=='PASS' and auth['source_count']==5 and len(auth['sources'])==5,'independent fresh authentication count')
auth_by_file={r['file']:r for r in auth['sources']}
for m in json.loads((ROOT/'INPUTS.json').read_text()):
    a=auth_by_file[m['file']]
    require(a['local_equals_fresh'] and a['all_manifest_fields_match'] and
            all(a[k]==m[k] for k in ['file','ref','path','url','git_blob_sha1','bytes','sha256']) and
            a['returned_git_blob_sha1']==m['git_blob_sha1'],'independent fresh authentication '+m['file'])
out={'status':'PASS','method':'closed class characters and local eight-dimensional H1 budget only',
     'checks':checks,'actual_instance_computations':False,'global_candidate_search':False,
     'proof_sha256':proof_sha,'first_reduction_sha256':first_hash,'sources':source_checks,
     'quotients':records,'local_atoms':atoms,'local_tail_partitions':tail_records,
     'K':K,'rank_K_minus':10,'degree_K_minus':-60,'rank_E0':16,'degree_E0':-46,
     'geometric_scope':'Manual review separately establishes canonical evaluations, basepoint-freeness, actual image and Gauss pair. Arithmetic does not certify imported actual geometric premises.'}
(ROOT/'REVIEW-RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

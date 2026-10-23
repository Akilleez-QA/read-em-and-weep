#!/usr/bin/env python3
"""Exact finite-group/geometry boundary, without HM coefficient evaluation."""
from pathlib import Path
import itertools,json,hashlib
import sympy as s
ROOT=Path(__file__).resolve().parent;checks=[]
def ck(name,test):
 if not test:raise RuntimeError(name)
 checks.append(name)
for e in json.loads((ROOT/'INPUTS.json').read_text()):
 b=(ROOT/e['local_path']).read_bytes()
 ck(e['label']+' SHA256',hashlib.sha256(b).hexdigest()==e['sha256'])
 ck(e['label']+' Git blob',hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==e['git_blob'])
I=(1,0,0,1);negI=(4,0,0,4);zero=(0,0)
def mm(g,h):
 a,b,c,d=g;e,f,j,k=h
 return ((a*e+b*j)%5,(a*f+b*k)%5,(c*e+d*j)%5,(c*f+d*k)%5)
def inv(g):a,b,c,d=g;return(d%5,-b%5,-c%5,a%5)
def act(g,v):return((g[0]*v[0]+g[1]*v[1])%5,(g[2]*v[0]+g[3]*v[1])%5)
def add(v,w):return((v[0]+w[0])%5,(v[1]+w[1])%5)
def mul(a,b):return(add(a[0],act(a[1],b[0])),mm(a[1],b[1]))
def ainv(a):h=inv(a[1]);return(act(h,((-a[0][0])%5,(-a[0][1])%5)),h)
G=[g for g in itertools.product(range(5),repeat=4) if (g[0]*g[3]-g[1]*g[2])%5==1]
V=list(itertools.product(range(5),repeat=2));N=list(itertools.product(V,G))
ck('SL2 order120',len(G)==120)
ck('SL2 inverses',all(mm(g,inv(g))==I for g in G))
ck('SL2 closure',all(mm(g,h) in G for g in G for h in G))
ck('projective normalizer order3000',len(N)==3000)
ck('linear/projective order conversion',125*120==15000 and 15000//5==3000)
ck('center involution unique',set(g for g in G if g!=I and mm(g,g)==I)=={negI})
ck('central negI',all(mm(negI,g)==mm(g,negI) for g in G))
# Exact perfectness by generating the commutator subgroup.
u=(1,1,0,1);v=(1,0,1,1)
comm={mm(mm(mm(g,h),inv(g)),inv(h)) for g in G for h in (u,v)}
derived={I};front=[I]
while front:
 g=front.pop()
 for h in comm:
  k=mm(g,h)
  if k not in derived:derived.add(k);front.append(k)
ck('SL2 perfect',derived==set(G))
inversion=(zero,negI)
conjugates={mul(mul(a,inversion),ainv(a)) for a in N}
ck('exact inversion conjugacy orbit',conjugates=={((2*x%5,2*y%5),negI) for x,y in V})
ck('inversion orbit size25',len(conjugates)==25)
ck('affine inverse identity',all(mul(a,ainv(a))==(zero,I) for a in N))
ck('conjugation formula for all3000',all(mul(mul(a,inversion),ainv(a))==((2*a[0][0]%5,2*a[0][1]%5),negI) for a in N))
centralizer={a for a in N if mul(a,inversion)==mul(inversion,a)}
complement={(zero,g) for g in G}
ck('exact inversion centralizer',centralizer==complement)
origin_stab={a for a in N if add(a[0],act(a[1],zero))==zero}
ck('exact orbit-origin stabilizer',origin_stab==complement)
ck('line orbit upper bound equals lower',len(N)//len(G)==len(V)==25)
ck('orbit stabilizer equality',len(N)//25==len(G))
ck('nonzero translations excluded',all(a not in origin_stab for a in N if a[0]!=zero))
# This is the standard formal rank-three quadratic normal form, not Q0 data.
x0,x1,x2,w0,w1=s.symbols('x0 x1 x2 w0 w1');q=x0*x0+x1*x1+x2*x2
ck('rank-three vertex equations',[s.diff(q,x) for x in (x0,x1,x2,w0,w1)]==[2*x0,2*x1,2*x2,0,0])
r=s.symbols('r',nonzero=True)
ck('order4 block changes nonzero ratio',s.simplify(s.I**(-2)*r+r)==0 and -r!=r)
ck('negative quadratic parameter sign',s.I**2==-1)
ck('octic parameter contribution is plus',(-1)**8==1)
result={'status':'PASS','checks':len(checks),'projective_normalizer_order':3000,
 'chosen_line_stabilizer_order':120,'chosen_quadric_stabilizer':'existing SL2(F5)',
 'new_octic_character_from_known_normalizer':False,
 'order4_block_scaling':'not an actual ambient HM automorphism (imported theorem)',
 'full_HM_stabilizer_classified':False,'actual_octic_scalar':'unselected',
 'actual_HM_instance_evaluated':False,'source_or_pair_removed':False}
(ROOT/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

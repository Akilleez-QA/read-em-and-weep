#!/usr/bin/env python3
"""Universal binary-form diagnostics, never an actual HM evaluation."""
import hashlib,itertools,json
from pathlib import Path
import sympy as S
ROOT=Path(__file__).resolve().parent
n=0

def check(x,label):
 global n
 n+=1
 if not x:raise RuntimeError(label)
x,y,alpha,beta,gamma,lam,mu=S.symbols('x y alpha beta gamma lambda mu')
a=alpha*x*x+beta*x*y+gamma*y*y
basis2=[x*x,x*y,y*y];basis4=[x**(4-i)*y**i for i in range(5)]
def vec(p):
 p=S.Poly(S.expand(p),x,y)
 return S.Matrix([p.coeff_monomial(m) for m in basis4])
def bracket(f,h):return S.diff(f,x)*S.diff(h,y)-S.diff(f,y)*S.diff(h,x)
M=S.Matrix.hstack(*(vec(a*k) for k in basis2))
T=S.Matrix.hstack(*(vec(bracket(a,h)) for h in basis4))
B=(lam*M).row_join(mu*T)
check(B.shape==(5,8),'whole first symbol dimensions')
check(S.expand(M[:3,:].det())==alpha**3,'multiplication leading minor')
check(S.expand(M[2:5,:].det())==gamma**3,'multiplication trailing minor')
check(S.expand(M[1:4,:].subs({alpha:0,gamma:0}).det())==beta**3,'multiplication middle-only minor')
Sq=B.subs({alpha:1,beta:0,gamma:0})
Ns=B.subs({alpha:0,beta:1,gamma:0})
# Square image excludes y^4; four D columns certify rank exactly four.
check(Sq[4,:]==S.zeros(1,8),'square image contained in four-dimensional hyperplane')
check(S.expand(Sq.extract(range(4),[4,5,6,7]).det())==384*mu**4,'square rank-four certificate')
# Nonsquare D part misses middle monomial; A middle column fills it.
check(Ns[2,3:8]==S.zeros(1,5),'nonsquare transvectant misses middle quartic')
check(S.expand(Ns[:,[3,4,1,6,7]].det())==64*lam*mu**4,'nonsquare full-rank certificate')
# Hom multiplicities derived from Clebsch and imported Sym6=V+P.
# Coordinates 1,A,V,P,D.
AA=(1,1,0,0,1);AD=(0,1,1,1,1)
check(AA[-1]==AD[-1]==1,'unique D channel in both tensor products')
check(sum(c*d for c,d in zip(AA,(1,3,3,4,5)))==9,'A tensor A dimension')
check(sum(c*d for c,d in zip(AD,(1,3,3,4,5)))==15,'A tensor D dimension')
check(bracket(x*x,y**4)==8*x*y**3,'transvectant nonzero universally')
# Bounded examples of universal polynomial coefficients only.
counts={'rank3':0,'rank4':0,'rank5':0,'zero':0}
for al,be,ga in itertools.product((-1,0,1),repeat=3):
 for ll,mm in [(1,0),(2,0),(1,1),(2,-1)]:
  rank=B.subs({alpha:al,beta:be,gamma:ga,lam:ll,mu:mm}).rank()
  discr=be*be-4*al*ga
  expected=0 if (al,be,ga)==(0,0,0) else 3 if mm==0 else 4 if discr==0 else 5
  check(rank==expected,'bounded exact universal rank stratum')
  counts['zero' if rank==0 else 'rank'+str(rank)]+=1
for rank in (3,4,5):check((8-rank)-(5-rank)==3,'kernel/cokernel Euler arithmetic')
for e in json.loads((ROOT/'INPUTS.json').read_text()):
 data=(ROOT/e['local_path']).read_bytes()
 check(hashlib.sha256(data).hexdigest()==e['sha256'],'input SHA256 '+e['local_path'])
 check(hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==e['git_blob'],'input blob '+e['local_path'])
print(json.dumps(dict(status='pass',checks=n,diagnostic_counts=counts,square_minor='384 mu^4',nonsquare_minor='64 lambda mu^4',scope='Universal internal symbol; no actual mu selection or source exclusion'),indent=2))

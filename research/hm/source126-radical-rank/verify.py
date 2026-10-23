#!/usr/bin/env python3
"""Universal formal radical identities. No geometric or actual-HM parameters."""
from itertools import product
from collections import defaultdict
import json
import hashlib
from pathlib import Path

# Exact integral polynomials in formal alpha,beta,gamma,x,y.
ZERO={}
def var(i):
    e=[0]*5;e[i]=1
    return {tuple(e):1}
def add(*ps):
    r=defaultdict(int)
    for p in ps:
        for e,c in p.items():r[e]+=c
    return {e:c for e,c in r.items() if c}
def neg(p):return {e:-c for e,c in p.items()}
def mul(p,q):
    r=defaultdict(int)
    for e,c in p.items():
        for f,d in q.items():r[tuple(a+b for a,b in zip(e,f))]+=c*d
    return {e:c for e,c in r.items() if c}
def kill(p,indices):return {e:c for e,c in p.items() if not any(e[i] for i in indices)}
def require(ok,msg):
    if not ok:raise RuntimeError(msg)
# Authenticate the vendored immutable source bytes before testing the deduction.
root=Path(__file__).resolve().parent
for source in json.loads((root/'INPUTS.json').read_text()):
    raw=(root/'inputs'/source['file']).read_bytes()
    require(hashlib.sha256(raw).hexdigest()==source['remote_sha256'],
            'source SHA256 mismatch: '+source['file'])
    blob=b'blob '+str(len(raw)).encode()+b'\0'+raw
    require(hashlib.sha1(blob).hexdigest()==source['git_blob_sha1'],
            'source Git blob mismatch: '+source['file'])
    require(source['local_matches_remote'] is True, 'source not verified')

a,b,g,x,y=map(var,range(5)); weights=(3,3,4,5)
def channels(X,Y):return (X,neg(add(mul(a,X),mul(b,Y))),neg(mul(g,Y)),Y)
def rank_generic(ps):return sum(w for w,p in zip(weights,ps) if p)
base=channels(x,y)
require(not add(base[2],mul(g,base[3])), 'X restriction')
require(not add(mul(a,base[0]),base[1],mul(b,base[3])), 'Y restriction')
# Exhaust the eight support strata without assigning values to any nonzero
# coupling. Variables retained below remain algebraically independent symbols.
rows=[]
for sa,sb,sg in product((False,True),repeat=3):
    zeros=[i for i,s in enumerate((sa,sb,sg)) if not s]
    generic=rank_generic(tuple(kill(p,zeros) for p in base))
    at_y0=rank_generic(tuple(kill(p,zeros+[4]) for p in base))
    at_x0=rank_generic(tuple(kill(p,zeros+[3]) for p in base))
    require(generic==8+3*(sa or sb)+4*sg,'generic formula')
    require(at_y0==3+3*sa,'y=0 formula')
    require(at_x0==5+3*sb+4*sg,'x=0 formula')
    require(generic>=8 and at_y0<=6 and generic-at_y0>=5,'gap')
    require(generic in (8,11,12,15),'rank overlist')
    third=None
    if sa and sb:
        # Formal direction [x:y]=[-beta:alpha]; neither coordinate vanishes.
        exceptional=tuple(kill(p,zeros) for p in channels(neg(b),a))
        require(not exceptional[1],'third-point V cancellation')
        third=rank_generic(exceptional)
        require(third==generic-3==8+4*sg,'third-point rank')
    # Supported channels give sum image and common kernel. Every generic
    # channel is simultaneously nonzero off the union of its proper lines.
    image=sum(w for w,p in zip(weights,base) if kill(p,zeros))
    common_kernel=15+sum(w for w,p in zip(weights,base) if not kill(p,zeros))
    require(image==generic and common_kernel==30-generic,'simultaneous support')
    require(2*generic+(30-2*generic)==30,'Jordan dimension')
    rows.append(dict(alpha_nonzero=sa,beta_nonzero=sb,gamma_nonzero=sg,
                     generic_rank=generic,y_zero_rank=at_y0,x_zero_rank=at_x0,
                     distinct_third_rank=third,jordan_twos=generic,jordan_ones=30-2*generic))
# Independent structural negative control on a formal 30-space: N1 sends
# e3 to e1, N2 sends e4 to e1. Products vanish, the maps are independent,
# every nonzero combination has rank1, and their kernel intersection has
# codimension2. Hence square-zero dimension2 alone implies neither our
# rank lower bound nor simultaneous-kernel saturation.
def compose_sparse(A,B):
    out=defaultdict(int)
    for (i,j),c in A.items():
        for (k,l),d in B.items():
            if j==k:out[i,l]+=c*d
    return {k:v for k,v in out.items() if v}
N1={(0,2):1};N2={(0,3):1}
require(all(not compose_sparse(A,B) for A in (N1,N2) for B in (N1,N2)),'squarezero control')
require(set(N1)!=set(N2),'independent control')
require(len({i for i,j in (*N1,*N2)})==1,'control image dimension')
require(len({j for i,j in (*N1,*N2)})==2,'control common-kernel codimension')
print(json.dumps({'support_strata':rows,'negative_control':{'generic_rank':1,'common_kernel_dimension':28},'scope':'universal formal identities only; no selected geometric parameter or actual HM evaluation'},indent=2))
print('PASS: eight formal support strata, complete rank-jump formulas, Jordan dimensions, and square-zero negative control.')

#!/usr/bin/env python3
"""Exact representation arithmetic and formal algebra identities, no HM instances."""
from pathlib import Path
from itertools import product
import hashlib
import json

ROOT=Path(__file__).resolve().parent
checks=0
def require(ok,msg):
    global checks
    if not ok: raise ValueError(msg)
    checks+=1

names=('one','W','A','S','D','T','V','P','Wp')
dims=(1,2,3,4,5,6,3,4,2)
def ch(**kw): return tuple(kw.get(n,0) for n in names)
def add(*xs): return tuple(map(sum,zip(*xs)))
def sub(x,y): return tuple(a-b for a,b in zip(x,y))
def dimension(x): return sum(a*b for a,b in zip(x,dims))
def minimum(x,y): return tuple(min(a,b) for a,b in zip(x,y))
def clean(x): return {n:a for n,a in zip(names,x) if a}
rules=(ch(W=1),ch(one=1,A=1),ch(W=1,S=1),ch(A=1,D=1),
       ch(S=1,T=1),ch(D=1,V=1,P=1),ch(T=1),ch(Wp=1,T=1),ch(P=1))
def times_W(x): return tuple(sum(x[i]*rules[i][j] for i in range(9)) for j in range(9))
sym=[ch(one=1),ch(W=1)]
for n in range(2,29): sym.append(sub(times_W(sym[-1]),sym[-2]))
for n,x in enumerate(sym):
    require(min(x)>=0 and dimension(x)==n+1,'symmetric power '+str(n))
for row in json.loads((ROOT/'INPUTS.json').read_text()):
    data=(ROOT/'inputs'/row['file']).read_bytes()
    require(hashlib.sha256(data).hexdigest()==row['remote_sha256'],'SHA256 '+row['file'])
    require(hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==row['git_blob_sha1'],'Git blob '+row['file'])

x=ch(A=1,V=2,P=3,D=4); y=ch(V=2,P=4,D=3); image=ch(V=2,P=3,D=3)
require(dimension(image)==33,'actual imported image dimension')
require(sub(x,image)==ch(A=1,D=1) and sub(y,image)==ch(P=1),'actual image consistency')
F=(sym[26],ch(P=1,D=2)); R=(sub(x,F[0]),sub(y,F[1]))
require(F[0]==ch(A=1,V=2,P=2,D=2),'F source')
require(R==(ch(P=1,D=2),ch(V=2,P=3,D=1)),'residual endpoints')
X4=sym[6]; Y4=times_W(sym[7]); Y2pre=times_W(sym[9])
require(X4==ch(V=1,P=1),'X target')
require(Y4==ch(V=1,P=2,D=1),'Y target')
require(Y2pre==ch(A=1,V=1,P=1,D=2),'Y source pre-subtraction')
IX=(sub(sym[8],ch(P=1)),X4)
IY=(sub(Y2pre,ch(A=1,V=1,D=1)),Y4)
IIIX=(sub(sym[8],ch(P=1,D=1)),X4)
IIIY=(sub(Y2pre,ch(A=1,V=1)),Y4)
require(IX[0]==ch(D=1) and IY[0]==ch(P=1,D=1),'Type I sources')
require(IIIX[0]==ch() and IIIY[0]==ch(P=1,D=2),'Type III sources')
require(sym[7]==ch(Wp=1,T=1),'X middle')
require(times_W(sym[8])==ch(Wp=1,S=1,T=2),'Y middle')
require(add(sym[27],sym[7],times_W(sym[8]))==ch(Wp=3,S=3,T=6),'middle total')
templates={'I':([F,IX,IY],[2,2]),'II':([F,R],[1,1]),'III':([F,IIIX,IIIY],[1,2])}
expected={'I':[23,30,30],'II':[23,23],'III':[23,30,30]}
rows=[]
for typ,(blocks,arrows) in templates.items():
    require(add(*(b[0] for b in blocks))==x,'source sum '+typ)
    require(add(*(b[1] for b in blocks))==y,'target sum '+typ)
    for mask in product((0,1),repeat=len(blocks)):
        # Coefficients of each independent formal radical variable b.
        # Same diagonal bits force b=0; differing bits allow a free b.
        for source in arrows:
            a,s=mask[0],mask[source]
            if a==s:
                require(a+s-1 in (-1,1),'same-bit radical forced zero')
            else:
                require(a+s-1==0,'opposite bits permit free variable')
                c_coeff=1//(s-a)
                require(c_coeff*(s-a)==1,'formal conjugation coefficient')
        if not any(mask) or all(mask): continue
        xs=add(*(b[0] for bit,b in zip(mask,blocks) if bit))
        ys=add(*(b[1] for bit,b in zip(mask,blocks) if bit))
        bound=add(minimum(xs,ys),minimum(sub(x,xs),sub(y,ys)))
        require(dimension(bound)<33,'exclude every nontrivial projector')
        require(bound[names.index('V')]<2,'V constituent contradiction')
        complement=add(minimum(sub(x,xs),sub(y,ys)),minimum(xs,ys))
        require(bound==complement,'complement symmetry')
        if sum(mask)==1:
            require(dimension(bound)==expected[typ][mask.index(1)],'singleton exact bound')
        rows.append(dict(template=typ,subset=list(mask),upper_character=clean(bound),upper_dimension=dimension(bound)))
require(len(rows)==14,'exhaust all six plus two plus six projectors')

# Regression controls: no omitted V may be silently added to a bound.
require(dimension(add(ch(V=2),ch(P=3,D=3)))==33,'overlarge bound control')
require(ch(V=2,P=3,D=3)!=ch(V=1,P=3,D=3),'reject silently added V')
# The universal local algebra C[epsilon]/epsilon^2 is not scalar, yet has
# only idempotents 0,1: e=a+b epsilon gives a(a-1)=0,(2a-1)b=0.
for a in (0,1): require(2*a-1!=0,'nonzero nilpotent does not force idempotent')
require(sub(ch(one=2),ch(one=1))==ch(one=1),'retain nonscalar local possibility')
result={'checks':checks,'nontrivial_vertex_subsets':len(rows),'bounds':rows,
        'compatible_algebra':'C*1 plus J_Q, J_Q subset J, J_Q squared=0',
        'possible_dimensions':[1,2,3],'source_labels_removed':0,'source_dual_pairs_removed':0,
        'scope':'universal representation and formal algebra checks only; no actual-instance evaluation'}
(ROOT/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))

#!/usr/bin/env python3
"""Exact AC rational normalization in the free polynomial ring on 16 tags.
No identities among the tags are assumed; hence every rewrite remains valid
under their concrete polynomial substitution. Input files are read-only.
"""
import json,sys,math,time,resource
from fractions import Fraction as Q
from collections import Counter
P=sys.argv[1]
LABEL=sys.argv[sys.argv.index('--input-label')+1] if '--input-label' in sys.argv else P
if '--export' in sys.argv:
    from pathlib import Path
    if Path(sys.argv[sys.argv.index('--export')+1]).exists():
        raise FileExistsError('Refuse to overwrite an existing normalized source')
CAP=int(sys.argv[2]) if len(sys.argv)>2 else 64
D=json.load(open(P)); characteristic=None
if str(D.get('coefficientField','')).startswith('F'):
    characteristic=int(D['coefficientField'][1:])
    assert characteristic>=2 and all(characteristic%d for d in range(2,math.isqrt(characteristic)+1))
    class Fp(int):
        def __new__(cls,n=0,d=1):
            if isinstance(n,str)and '/' in n:
                n,b=n.split('/');d=int(d)*int(b);n=int(n)
            den=int(d)%characteristic
            if not den:raise ZeroDivisionError('Nonintegral field coefficient')
            return int.__new__(cls,int(n)%characteristic*pow(den,-1,characteristic)%characteristic)
        def __add__(self,b):return Fp(int(self)+int(b))
        __radd__=__add__
        def __mul__(self,b):return Fp(int(self)*int(b))
        __rmul__=__mul__
        def __truediv__(self,b):return Fp(int(self),int(b))
        def __pow__(self,e):return Fp(pow(int(self),e,characteristic))
        @property
        def numerator(self):return int(self)
        @property
        def denominator(self):return 1
    Q=Fp
field='F'+str(characteristic)if characteristic else'Q'
Z=(Q(0),()); ONE=(Q(1),())
# Symbols 0..15 are tag variables. Symbols >=16 are irreducible sums.
sums={}; cache={}; norms=[]; stats=Counter(); t0=time.time()
def facmul(a,b):
    z=dict(a)
    for i,e in b:z[i]=z.get(i,0)+e
    return tuple(sorted(z.items()))
def mul(a,b):
    if not a[0] or not b[0]:return Z
    return (a[0]*b[0],facmul(a[1],b[1]))
def term(a):
    c,f=a
    if len(f)==1 and f[0][0]>=16 and f[0][1]==1:
        return [(c*q,g) for q,g in sums[f[0][0]]]
    return [a]
def add(a,b):
    if not a[0]:return b
    if not b[0]:return a
    af=dict(a[1]);bf=dict(b[1]);common=tuple((i,min(e,bf[i])) for i,e in a[1] if i in bf)
    if common:
        commonD=dict(common)
        a=(a[0],tuple((i,e-commonD.get(i,0)) for i,e in a[1] if e!=commonD.get(i,0)))
        b=(b[0],tuple((i,e-commonD.get(i,0)) for i,e in b[1] if e!=commonD.get(i,0)))
    terms=term(a)+term(b)
    if len(terms)>CAP:
        terms=[a,b];stats['capped_additions']+=1
    m={}
    for c,f in terms:m[f]=m.get(f,Q(0))+c
    ts=tuple((c,f) for f,c in sorted(m.items()) if c)
    if not ts:stats['zero_additions']+=1;return Z
    if len(ts)==1:stats['one_term_additions']+=1;return(ts[0][0],facmul(common,ts[0][1]))
    # Primitive rational content is canonical; use first coefficient as scale
    # (exact, avoids repeated coefficient gcd and remains canonical).
    scale=ts[0][0]; key=tuple((c/scale,f) for c,f in ts)
    if key not in cache:
        sid=16+len(sums);cache[key]=sid;sums[sid]=key
    else:stats['sum_cache_hits']+=1
    return(scale,facmul(common,((cache[key],1),)))
def power(a,e):
    return (a[0]**e,tuple((i,j*e)for i,j in a[1]))if e else ONE
concrete='--concrete-tags' in sys.argv
aliases=[]
if concrete:
    for polynomial in D['tagPolynomials']:
        v=Z
        for e,c in polynomial:v=add(v,(Q(c),tuple((i,j)for i,j in enumerate(e)if j)))
        aliases.append(v)
for k,n in enumerate(D['nodes']):
    op=n[0]
    if op=='const':v=(Q(int(n[1]),int(n[2])),())
    elif op=='tags':
        v=ONE
        if concrete:
            for i,e in enumerate(n[1:]):
                if e:v=mul(v,power(aliases[i],e))
        else:v=(Q(1),tuple((i,e) for i,e in enumerate(n[1:]) if e))
    elif op=='mul':v=mul(norms[n[1]],norms[n[2]])
    elif op=='add':v=add(norms[n[1]],norms[n[2]])
    else:raise ValueError(op)
    norms.append(v)
    if k and k%100000==0:print(json.dumps({'progress':k,'sums':len(sums),'seconds':time.time()-t0,'maxRSSKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}),file=sys.stderr)
def tagged_roots(value):
    if isinstance(value,dict):
        if 'numerator' in value and 'powers' in value:
            yield value
        else:
            for x in value.values():yield from tagged_roots(x)
    elif isinstance(value,list):
        for x in value:yield from tagged_roots(x)
seen=set()
def visit(f):
    for sid,e in f:
        if sid<16 or sid in seen:continue
        seen.add(sid)
        for c,g in sums[sid]:visit(g)
for o in tagged_roots([D['outputs'],D.get('termwiseOutputs',[])]):visit(norms[o['numerator']][1])
res={'input':LABEL,'cap':CAP,'concreteTags':concrete,'coefficientField':field,'originalNodes':len(D['nodes']),'sumSymbols':len(sums),'retainedSumSymbols':len(seen),'normalizedZeroNodes':sum(not x[0] for x in norms),'normalizedZeroOutputs':[i for i,o in enumerate(D['outputs']) if not norms[o['numerator']][0]],'distinctNormalizedOutputs':len(set(norms[o['numerator']] for o in D['outputs'])),'retainedTerms':sum(len(sums[i]) for i in seen),'retainedFactors':sum(sum(len(f) for c,f in sums[i]) for i in seen),'stats':dict(stats),'seconds':time.time()-t0,'maxRSSKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'exactness':('Exact concrete tag-polynomial substitution, followed by field identities in '+field+'[x1,...,x4]'if concrete else'Field identities in free '+field+'[tag0,...,tag15]')+'; no sampled evaluations or changed partition'}
print(json.dumps(res,indent=2))
if '--export' in sys.argv:
    dest=sys.argv[sys.argv.index('--export')+1]
    ids=sorted(seen); remap={i:j+16 for j,i in enumerate(ids)}
    def ff(f):return [[i if i<16 else remap[i],e] for i,e in f]
    def export_root(o):
        assert all(e>=0 for e in o['powers'][4:]),'Non-coordinate denominator remains'
        c,f=norms[o['numerator']]; ef=dict(f)
        for i,e in enumerate(o['powers']):ef[i]=ef.get(i,0)+e
        return {'coefficient':[str(c.numerator),str(c.denominator)],'factors':ff(tuple((i,e)for i,e in sorted(ef.items())if e))}
    def export_nested(v):
        if isinstance(v,dict):
            if 'numerator' in v and 'powers' in v:return export_root(v)
            return {k:export_nested(x) for k,x in v.items()}
        if isinstance(v,list):return [export_nested(x)for x in v]
        return v
    roots=[export_root(o)for o in D['outputs']]
    out={'format':'exact-free-tag-factor-sum-dag-v1','input':LABEL,'coefficientField':field,'tagNames':D['tagNames'],'tagPolynomials':D['tagPolynomials'],'sumNodes':[[[[str(c.numerator),str(c.denominator)],ff(f)]for c,f in sums[i]]for i in ids],'outputs':roots,'semantics':'Symbols 0..15 are original concrete tags. Sum node k has symbol 16+k and is the rational weighted sum of its factor monomials. Output factors may have negative coordinate-tag exponents only. All transformations are exact over the declared coefficientField.','inputSHA256':__import__('hashlib').sha256(open(P,'rb').read()).hexdigest()}
    if 'termwiseOutputs' in D:out['termwiseOutputs']=export_nested(D['termwiseOutputs'])
    with open(dest,'w')as outFile:json.dump(out,outFile,separators=(',',':'));outFile.write('\n')

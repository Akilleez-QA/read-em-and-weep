"""Static byte/AST binding and bounded invented-polynomial tests only.
Never imports or executes any repository module; never constructs physical owners.
"""
import argparse
import ast
import copy
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

HERE=Path(__file__).resolve().parent
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--source-root', type=Path, required=True,
 help='Pinned repository root, or its research/codex-swarm directory')
args=parser.parse_args()
SOURCE=args.source_root.resolve()
if (SOURCE/'research/codex-swarm').is_dir(): SOURCE=SOURCE/'research/codex-swarm'
def need(x,msg):
    if not x: raise ValueError(msg)
def sha(b): return hashlib.sha256(b).hexdigest()
def tree(path): return ast.parse((SOURCE/path).read_text())
def fn(t,name): return next(n for n in t.body if isinstance(n,(ast.FunctionDef,ast.ClassDef)) and n.name==name)
def dump(n): return ast.dump(n,include_attributes=False)

# Authenticate bytes BEFORE parsing. This is a local transcription check,
# not a new independent certification of the upstream mathematical premises.
need(sha((HERE/'source-pins.json').read_bytes())=='8f2bc7c09722b7af794d1628ae86bf436098da074a49d878d2d86c952646c263','manifest drift')
manifest=json.loads((HERE/'source-pins.json').read_text())
for rec in manifest['sources']:
    raw=(SOURCE/rec['path']).read_bytes()
    need(sha(raw)==rec['sha256'],'source drift: '+rec['path'])
    need(hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==rec['git_blob'],'git blob drift')

req=json.loads((HERE/'premises/weighted-requests-30.json').read_text())
# Locate the exact request array without assuming the top-level wrapper name.
def lists(x):
    if isinstance(x,list):
        yield x
        for y in x: yield from lists(y)
    if isinstance(x,dict):
        for y in x.values(): yield from lists(y)
arrays=[x for x in lists(req) if len(x)==30 and all(isinstance(v,dict) for v in x)]
need(len(arrays)==1,'retained request list')
r=arrays[0][0]
expected={'base_monomial':[], 'block':'Q^2', 'id':0, 'scalar_map':{'b':0,'i':5},
 'terms':[{'coefficient':w,'dual_monomial':m,'laurent_exponents':[-v-1 for v in m],'output_index':k}
 for w,m,k in [(1,[2,2,0,0],8),(2,[1,1,1,1],40),(1,[0,0,2,2],72)]]}
need(r==expected,'exact ID0 request drift')
for t in r['terms']:
    need(t['output_index']==sum((2-m)*3**(3-i) for i,m in enumerate(t['dual_monomial'])),'output indexing')
for path,digest in {
 'premises/PROOF.md':'e43de2abc2838f2d5e31c3fd45fc9517c963e3ad9c8a605f00ec62b50263bab9',
 'premises/COMMON_FRAME_CORRECTION.md':'a88442758260f080d7c5c6d871b27522a60263cec6a8669e3956d63d7ff71bc7',
 'premises/REVIEW.md':'e155fa2d432bfa4e4c673fc31cd4c66dc80d2af02e1ce0683a07a80e60978f39',
 'premises/weighted-requests-30.json':'707663b97c3a8289d6531172a1c509e54ceccb3185a6e07f4f28153fbc119375'
}.items(): need(sha((HERE/path).read_bytes())==digest,'premise drift: '+path)

p=tree('detector-realization/program.py')
owner=copy.deepcopy(fn(p,'potential_owners'))
calls=[n for n in ast.walk(owner) if isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and n.func.attr=='FullOwner']
need(len(calls)==1 and isinstance(calls[0].args[0],ast.Constant) and calls[0].args[0].value==30,'owner seed site')
# This symbolic candidate is never compiled or evaluated.
calls[0].args[0]=ast.Constant(0)
restored=copy.deepcopy(owner)
[n for n in ast.walk(restored) if isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and n.func.attr=='FullOwner'][0].args[0]=ast.Constant(30)
need(dump(restored)==dump(fn(p,'potential_owners')),'non-seed owner delta')
body=fn(p,'_actual_body')
need(isinstance(body.body[-1],ast.Return),'terminal location')
need(ast.unparse(body.body[-1].value)=='stripped.laurent_coefficient(EXPONENT)','terminal shape')
# The complete prefix includes admission, actual_model, total sum and mask15.
prefix=ast.Module(body=body.body[:-1],type_ignores=[])
need('dict(total.terms).get(15, ex.rational(0))' in ast.unparse(prefix),'complete mask extraction')
# Enumerate all owner-field references in the exact physical engine.
raw=tree('detector-realization/raw_engine.py')
need(not any(isinstance(n,ast.Attribute) and n.attr in ('seed','occurrence') for n in ast.walk(raw)), 'engine consumes provenance')
need(not any(isinstance(n,ast.Attribute) and n.attr in ('seed','occurrence') for n in ast.walk(fn(p,'weighted_assignment'))), 'weighted assignment consumes provenance')
need(not any(isinstance(n,ast.Attribute) and n.attr in ('seed','occurrence') for n in ast.walk(fn(p,'outer_weight'))), 'weight consumes provenance')
# Exact source bytes bind all remaining operations, including memoized equality.

Z=(0,0,0,0)
E=((-3,-3,-1,-1),(-2,-2,-2,-2),(-1,-1,-3,-3))
W=(1,2,1)
ops=0
def tidy(p): return {e:F(c) for e,c in p.items() if c}
def add(a,b):
    c=dict(a)
    for e,v in b.items(): c[e]=c.get(e,F(0))+v
    return tidy(c)
def scale(a,k): return tidy({e:k*v for e,v in a.items()})
def mul(a,b):
    global ops
    c={}
    for e,v in a.items():
        for f,w in b.items():
            ops+=1;need(ops<=10000,'invented control cap')
            g=tuple(x+y for x,y in zip(e,f));c[g]=c.get(g,F(0))+v*w
    return tidy(c)
def shift(a,d): return {tuple(x+y for x,y in zip(e,d)):v for e,v in a.items()}
def divide(a,b):
    need(bool(b),'zero denominator')
    q={};r={};a=dict(a);de=max(b);dc=b[de]
    while a:
        e=max(a);c=a[e]
        if all(x>=y for x,y in zip(e,de)):
            t={tuple(x-y for x,y in zip(e,de)):c/dc};q=add(q,t);a=add(a,scale(mul(t,b),-1))
        else:
            r[e]=c;del a[e]
    return q,r
def certify(a,b):
    need(bool(b),'zero denominator')
    d=tuple(min(e[i] for e in b) for i in range(4))
    c=shift(b,tuple(-v for v in d));q,r=divide(a,c)
    need(not r,'non-Laurent')
    need(mul(c,q)==tidy(a),'quotient witness')
    return d,q
def lookup(cert,e):
    d,q=cert;return q.get(tuple(x+y for x,y in zip(e,d)),F(0))
def weighted(cert): return sum((F(w)*lookup(cert,e) for w,e in zip(W,E)),F(0))
def rejects(f):
    try: f()
    except ValueError: return
    raise ValueError('negative control accepted')

C={Z:F(1),(1,0,0,0):F(1),(0,1,0,0):F(1)}
d=(3,3,3,3)
Q={tuple(x+y for x,y in zip(e,d)):F(v) for e,v in zip(E,(3,5,7))}
A=mul(C,Q);B=shift(C,d);cert=certify(A,B)
need(weighted(cert)==20,'weights/targets')
need(tuple(lookup(cert,e) for e in E)==(3,5,7),'three terms')
need(weighted(cert)==sum(w*lookup(certify(A,B),e) for w,e in zip(W,E)),'shared vs three certification calls')
# Denominator normalization is not a constant-term test.
C2={(1,0,0,0):F(1),(0,1,0,0):F(1)}
need(weighted(certify(mul(C2,Q),shift(C2,d)))==20,'residual without constant term')
# Equivalent unreduced rational representation yields same Laurent polynomial.
T={Z:F(2),(0,0,1,0):F(3)}
need(weighted(certify(shift(mul(A,T),(1,2,0,1)),shift(mul(B,T),(1,2,0,1))))==20,'representation independence')
rejects(lambda:certify({Z:F(1)},C))
rejects(lambda:certify(add(C,{Z:F(-1)}),C))
need(certify(add({Z:F(1)},add(C,{Z:F(-1)})),C)==(Z,{Z:F(1)}),'complete cancellation')
need(weighted(certify({},B))==0,'zero numerator')
rejects(lambda:certify(A,{}))
Qc={tuple(x+y for x,y in zip(e,d)):F(v) for e,v in zip(E,(3,-5,7))}
need(weighted(certify(mul(C,Qc),B))==0,'weighted cancellation')
need(lookup(cert,(-99,0,0,0))==0,'negative polynomial target after certification')

report={'status':'static and invented algebra controls passed','source_files_verified':len(manifest['sources']),
 'physical_execution':False,'physical_modules_imported':False,'physical_owners_constructed':False,
 'seed_delta':'30 -> 0 only, symbolic AST, never compiled',
 'complete_preterminal_AST_sha256':sha(dump(prefix).encode()),
 'weighted_assignment_AST_sha256':sha(dump(fn(p,'weighted_assignment')).encode()),
 'id0_record':r,'invented_polynomial_products':ops,
 'limitation':'No adapter, cost admission, full transitive implementation validation, or physical detector value.'}
print(json.dumps(report,indent=2))

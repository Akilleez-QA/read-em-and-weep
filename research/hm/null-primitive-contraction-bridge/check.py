"""Static metadata, invented formal words and tiny matrix controls only."""
import argparse, ast, hashlib, json
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def need(p,label):
    if not p: raise RuntimeError(label)

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--source-root',type=Path,default=ROOT/'inputs',help='Root containing the five input_path files in pins.json')
for name in ('raw-engine','source-formulas','first-order','model','historical-checker'):
    parser.add_argument('--'+name,type=Path,help='Explicit input override; immutable digest must still match')
args=parser.parse_args()
pins=json.loads((ROOT/'pins.json').read_text())
paths=[getattr(args,p['id']) or args.source_root/p['input_path'] for p in pins]
for p,path in zip(pins,paths):
    b=path.read_bytes()
    need(hashlib.sha256(b).hexdigest()==p['sha256'],'immutable SHA256 mismatch: '+p['id'])
    if 'git_blob_sha1' in p:need(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==p['git_blob_sha1'],'Git blob identity')
raw=paths[0].read_text()
tree=ast.parse(raw)
cl=next(n for n in tree.body if isinstance(n,ast.ClassDef) and n.name=='PhysicalModel')
expected='''
def polynomial(self,terms):
    out=self.ex.scalar(0)
    for key,c in terms:
        e=tuple(map(int,key.split(',')));term=self.ex.scalar(Q(c))
        for i,n in enumerate(e):term=term*power(self.v[i+1],n)
        out=out+term
    return out

def matrix(self,a,den):
    inv=self.polynomial(den).inverse()
    return tuple(tuple(self.polynomial(p)*inv for p in row)for row in a)
'''
for e in ast.parse(expected).body:
    a=next(n for n in cl.body if isinstance(n,ast.FunctionDef) and n.name==e.name)
    need(ast.dump(a,include_attributes=False)==ast.dump(e,include_attributes=False),e.name)
prim=next(n for n in cl.body if isinstance(n,ast.FunctionDef) and n.name=='primitive')
comp=next(n for n in ast.walk(prim) if isinstance(n,ast.DictComp))
need(ast.literal_eval(comp.generators[0].iter)==[('I','di'),('P','dp'),('H0','dh'),('H1','dh')],'denominator binding')
# JSON is inspected only as literal coefficient records, never evaluated or multiplied.
m=json.loads(paths[3].read_text())
shapes={'gamma':(15,5),'delta':(10,15),'ev':(2,10),'I':(15,2),'P':(2,15),'H0':(5,15),'H1':(15,10)}
def terms(p):
    keys=[]
    for key,c in p:
        e=key.split(',')
        need(len(e)==4 and all(x.isdigit() for x in e),'exponent record')
        need(type(c) is int and c!=0,'integer coefficient')
        keys.append(key)
    need(len(keys)==len(set(keys)),'duplicate exponent')
def matrix(a,shape):
    need(len(a)==shape[0] and all(len(r)==shape[1] for r in a),'rectangular shape')
    for row in a:
        for p in row: terms(p)
for k in ('gamma','delta','ev'):matrix(m[k],shapes[k])
for c in m['charts']:
    need(type(c['pivot']) is int and 0<=c['pivot']<5,'pivot')
    for k in ('I','P','H0','H1'):matrix(c[k],shapes[k])
    for k in ('di','dp','dh'):terms(c[k]);need(bool(c[k]),'nonzero formal denominator')
    for row in c['H1']:
        for h in range(2):need(row[5*h+c['pivot']]==[],'B_pol literal zero')
# Exact literal ev denotation, without polynomial multiplication or evaluation.
for h in range(2):
    for j in range(10):
        k=j%5
        key=','.join(str(int(i==k-1)) for i in range(4))
        want=[[key,1]] if j//5==h else []
        need(m['ev'][h][j]==want,'ev literal')
# Free associative words; rules are stated consequences/premises, not model tests.
def add(*ps):
    r={}
    for p in ps:
        for w,c in p.items():r[w]=r.get(w,0)+c
    return {w:c for w,c in r.items() if c}
def atom(s):return {tuple(s.split()):1}
def mul(*ps):
    r=atom('')
    for p in ps:r=add(*({a+b:c*d} for a,c in r.items() for b,d in p.items()))
    return r
one=atom(''); zero={}
rules={('W','L'):add(one,{('eta','ev'):-1}),('H1','eta'):zero,('ev','delta'):zero,
('L','W'):one,('ev','W'):zero,('L','eta'):zero,('ev','eta'):one}
def red(p):
    for w,c in p.items():
        for a in range(len(w)-1):
            if w[a:a+2] in rules:
                q=dict(p);del q[w]
                return red(add(q,*({w[:a]+v+w[a+2:]:c*d} for v,d in rules[w[a:a+2]].items())))
    return p
need(red(atom('H1 W L delta'))==atom('H1 delta'),'right inverse bridge')
# Q U = 1 follows mathematically from U Q = 1 (square over commutative field).
for q in ('H0','P','L delta'):
    for u in ('gamma','I','H1 W'):
        rules[tuple((q+' '+u).split())]=one if (q,u) in [('H0','gamma'),('P','I'),('L delta','H1 W')] else zero
# General subword matcher for these block equations.
def reduce(p):
    for w,c in p.items():
        for key,value in sorted(rules.items(),key=lambda kv:-len(kv[0])):
            for a in range(len(w)-len(key)+1):
                if w[a:a+len(key)]==key:
                    q=dict(p);del q[w]
                    return reduce(add(q,*({w[:a]+v+w[a+len(key):]:c*d} for v,d in value.items())))
    return p
for word in ('H0 H1 W L','P H1 W L','W L delta gamma','W L delta I'):
    need(reduce(atom(word))==zero,word)
need(reduce(atom('W L delta H1 W L'))==reduce(atom('W L')),'delta H1')
# Tiny invented rank-(1,3,2,1) controls, unrelated to physical coefficients.
def mm(a,b):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def ma(*aa):return [[sum(a[i][j] for a in aa) for j in range(len(aa[0][0]))] for i in range(len(aa[0]))]
g=[[1],[0],[0]];ii=[[0],[1],[0]];p=[[0,1,0]];h0=[[1,0,0]];h1=[[0,0],[0,0],[1,0]];d=[[0,0,1],[0,0,0]];ev=[[0,1]];eta=[[0],[1]]
eye=[[1,0,0],[0,1,0],[0,0,1]]
def premises(h0,h1,d):return [ma(mm(g,h0),mm(ii,p),mm(h1,d))==eye,mm(h1,eta)==[[0],[0],[0]],mm(ev,d)==[[0,0,0]]]
need(premises(h0,h1,d)==[True]*3,'toy baseline')
need(premises([[0,0,0]],h1,d)==[False,True,True],'resolution independent')
need(premises(h0,[[0,1],[0,0],[1,0]],d)==[True,False,True],'side condition independent')
need(premises(h0,h1,[[0,0,1],[1,0,0]])==[True,True,False],'complex condition independent')
# Verify the require mechanism cannot silently pass a false condition under -O.
try:need(False,'negative control')
except RuntimeError:pass
else:raise RuntimeError('disabled check')
print(json.dumps({'status':'PASS','scope':'conditional decoder/contraction reduction','pins':len(pins),'charts_metadata_checked':len(m['charts']),'H1_eta_literal_zero_charts':len(m['charts']),'independent_matrix_identity_families':3,'tiny_invented_independence_controls':3,'physical_evaluation':False,'production_import':False,'actual_model_polynomial_products':False},indent=2))

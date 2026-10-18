"""Offline static source and invented differential-symbol controls only."""
from pathlib import Path
import ast,hashlib,json
import sympy as S
root=Path(__file__).resolve().parent
counts={}
PINS={'source-contracts.json': '4217684fcbc10c0766b2d1e1fbbbdad1908461573edc1c6799be01ff3e92ce6c', 'branches.json': '335c9568efc9d15d0f94833e6d6635768724cab106b2e9e8ee5e83250e89cb9f', 'inputs/compiler.py.txt': '28e95b87adefaba0d4ec886a7ab272f252f376bbb1fc26e0a387bc05f896a386', 'inputs/program.py.txt': 'ad0603264992c2dfb425451f59d183a64d139b3c25db43b7866d7683851fc62a', 'inputs/raw_engine.py.txt': 'c9804022b362277d63217c7674c4d6d3dff5941ae4210c30f51f3b5cf3868da9'}
for filename,digest in PINS.items():
    if hashlib.sha256((root/filename).read_bytes()).hexdigest()!=digest:raise ValueError("independent packet pin "+filename)
def need(test,label):
    if not test:raise ValueError(label)
def bump(k):counts[k]=counts.get(k,0)+1
for record in json.loads((root/'source-contracts.json').read_text()):
    data=(root/record['file']).read_bytes()
    need(hashlib.sha256(data).hexdigest()==record['sha256'],'source hash');bump('source_hash')
    tree=ast.parse(data);found={}
    for n in tree.body:
        if isinstance(n,ast.FunctionDef):found[n.name]=ast.dump(n,include_attributes=False)
        if isinstance(n,ast.ClassDef):
            for f in n.body:
                if isinstance(f,ast.FunctionDef):found[n.name+'.'+f.name]=ast.dump(f,include_attributes=False)
    for key,value in record['contracts'].items():
        need(found.get(key)==value,'source AST '+key);bump('source_ast')
branches=json.loads((root/'branches.json').read_text())
expected=[(0,'L',1,'jk',1,[2,3]),(1,'L',0,'jk',-1,[2,3]),(1,'U',0,'ij',1,[2,3]),(0,'U',1,'ij',-1,[2,3]),(2,'L',3,'jk',1,[0,1]),(3,'L',2,'jk',-1,[0,1]),(3,'U',2,'ij',1,[0,1]),(2,'U',3,'ij',-1,[0,1])]
for b,(axis,kind,d,edge,sign,q) in zip(branches,expected):
    need(b['pair']==([0,1] if q==[2,3] else [2,3]),'E pair')
    need((b['axis'],b['current'],b['edge'],b['coefficient'],b['scalar_pair'])==(axis,[kind,d],edge,[sign,2],q),'E branch');bump('E_branch')
need(len(branches)==8,'eight E branches')
# Arbitrary one-variable curve functions, never the physical curve polynomial.
x=S.symbols('x0:4');C=[S.Function('C'+str(i))(x[i]) for i in range(4)]
a=S.Function('a')(*x);b=S.Function('b')(*x)
def mul(m,c,n,d):
    z=c*d
    for i in range(4):
        if (m&n)&(1<<i):z*=C[i]
    return m^n,z
def V(m,c,i):
    return m^(1<<i), S.diff(c,x[i]) if not m&(1<<i) else C[i]*S.diff(c,x[i])+S.diff(C[i],x[i])*c/2
def pi(t):return t[1] if t[0]==15 else S.Integer(0)
for i in range(4):
    for m in range(16):
        need(S.expand(pi(V(m,a,i))-S.diff(pi(mul(1<<i,1,m,a)),x[i]))==0,'deck derivative');bump('deck_derivative')
        for n in range(16):
            vn,vc=V(n,b,i);lhs=pi(mul(m,a,vn,vc))
            mn,cc=mul(m,a,n,b)
            flux=pi(mul(1<<i,1,mn,cc))
            vm,vc=V(m,a,i);rem=-pi(mul(vm,vc,n,b))
            need(S.expand(lhs-S.diff(flux,x[i])-rem)==0,'moving kernel IBP');bump('mask_pair_IBP')
# Invented Laurent moving-kernel countercontrol: no model/owner/source values.
i=0;m=14;n=0;k=1/S.prod(x);s=x[0]
lhs=pi(mul(m,k,*V(n,s,i)))
mn,cc=mul(m,k,n,s);flux=pi(mul(1,1,mn,cc))
rem=-pi(mul(*V(m,k,i),n,s))
need(S.simplify(lhs-1/S.prod(x))==0,'invented residue monomial')
need(S.diff(flux,x[0])==0 and S.simplify(rem-lhs)==0,'nonzero remainder')
need(S.simplify(lhs-S.diff(flux,x[0]))!=0,'drop kernel derivative mutation');bump('negative_mutation')
# Independent ordinary-coordinate normal-order formula, generic coefficients.
z=S.symbols('z');P,D,c,alpha,beta,C0,p=[S.Function(n)(z) for n in ['P','D','c','alpha','beta','C','p']]
expr=p*C0*(alpha*S.diff(c*P/D,z)+beta*c*P/D)
flux=p*C0*alpha*c*P/D
rem=(p*C0*beta-S.diff(p*C0*alpha,z))*c*P/D
need(S.expand(expr-S.diff(flux,z)-rem)==0,'ordinary normal order');bump('normal_order')
print(json.dumps({'status':'PASS','counts':counts,'physical_evaluations':0,'source_executions':0},sort_keys=True))

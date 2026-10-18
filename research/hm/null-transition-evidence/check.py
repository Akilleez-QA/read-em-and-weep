#!/usr/bin/env python3
"""Static AST checks and invented matrix controls. Never imports production."""
import ast, hashlib, json
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parent
INPUTS={k:ROOT/'inputs'/v for k,v in {
 'raw':'raw_engine.py.txt','compiler':'compiler.py.txt',
 'formulas':'source-formulas.js.txt','firstorder':'first-order-source.md.txt',
 'historical_report':'certificates__verification.json.txt'}.items()}
def need(x,msg):
 if not x: raise ValueError(msg)
def fun(tree,cl,name):
 c=next(x for x in tree.body if isinstance(x,ast.ClassDef) and x.name==cl)
 return next(x for x in c.body if isinstance(x,ast.FunctionDef) and x.name==name)
def body(s):return ast.parse(s).body
for pin in json.loads((ROOT/'pins.json').read_text()):
 need(hashlib.sha256((ROOT/pin['file']).read_bytes()).hexdigest()==pin['sha256'],'frozen input digest changed')
raw=ast.parse(INPUTS['raw'].read_text()); comp=ast.parse(INPUTS['compiler'].read_text())
def check_body(tree,cl,name,expected):
 actual=fun(tree,cl,name)
 need(ast.dump(ast.Module(body=actual.body,type_ignores=[]),include_attributes=False)==ast.dump(ast.Module(body=body(expected),type_ignores=[]),include_attributes=False),f'{cl}.{name} body changed')
check_body(raw,'PhysicalModel','g',"pa=self.primitive(a.carrier)['P'];ib=self.primitive(b.carrier)['I']\nreturn self.M.mul(self.Dframe(b),self.M.transpose(self.M.mul(pa,ib)),self.Dframe(a,True))")
check_body(raw,'PhysicalModel','Dframe',"n=self.nu(o);a,b=(n.inverse(),n)if inverse else(n,n.inverse());z=self.ex.scalar(0)\nreturn ((a,z),(z,b))")
check_body(raw,'Mat','inverse',"if self.shape(a)!=(2,2):raise ValueError('source adjugate only2x2')\nreturn ((a[1][1],-a[0][1]),(-a[1][0],a[0][0]))")
check_body(raw,'Mat','tf',"return self.add(a,self.smul(self.scale(self.trace(a),Q(-1,2)),self.eye(2)))")
check_body(comp,'Source','gi',"return self.c.inverse(self.g(a,b))")
check_body(comp,'Source','k',"c=self.c;u,v=p;G=self.g(a,b);Ginv=self.gi(a,b)\nreturn c.scale(c.add(c.mul(c.D(Ginv,u),c.D(G,v)),c.scale(c.mul(c.D(Ginv,v),c.D(G,u)),-1)),Q(-1,4))")
check_body(comp,'Source','F',"c=self.c;i,j,k=t\ncurvature=c.mul(self.gi(i,k),self.mu(p,self.g(j,k),self.g(i,j)))\nreturn c.add(self.b(p,t),c.scale(c.trace(curvature),Q(-1,2)))")
js=INPUTS['formulas'].read_text()
for snippet in ["const core=mtimes(charts[i].P,charts[j].I),li=[ji(charts[i].nu),charts[i].nu],rj=[charts[j].nu,ji(charts[j].nu)]", "inv=[[G[1][1],jn(G[0][1])],[jn(G[1][0]),G[0][0]]]", "R(1n,2n)),Z=msc(K,R(-1n,2n))"]:
 need(snippet in js,'JS transition/k anchor changed')
# Formal expansion P_i (Id-gamma H0_j-H1_j delta) I_k.
terms=[(1,('P_i','I_k')),(-1,('P_i','gamma','H0_j','I_k')),(-1,('P_i','H1_j','delta','I_k'))]
zero_pairs={('P_i','gamma'),('delta','I_k')}
reduced=[(c,w) for c,w in terms if not any(w[n:n+2] in zero_pairs for n in range(len(w)-1))]
need(reduced==[(1,('P_i','I_k'))],'formal cocycle reduction')
# Only invented matrices below; no model JSON is loaded.
def mat(a):return tuple(tuple(Q(v)for v in r)for r in a)
def mm(a,b):return tuple(tuple(sum(x*y for x,y in zip(row,col))for col in zip(*b))for row in a)
def add(*aa):return tuple(tuple(sum(a[i][j] for a in aa)for j in range(len(aa[0][0])))for i in range(len(aa[0])))
def eye(n):return mat([[int(i==j)for j in range(n)]for i in range(n)])
def zero(m,n):return mat([[0]*n for _ in range(m)])
def det(a):return a[0][0]*a[1][1]-a[0][1]*a[1][0]
def adj(a):return ((a[1][1],-a[0][1]),(-a[1][0],a[0][0]))
gamma=mat([[1],[0],[0],[0]]);h0=mat([[1,0,0,0]]);h1=mat([[0],[0],[0],[1]]);delta=mat([[0,0,0,1]])
i=mat([[0,0],[1,0],[0,1],[0,0]]);p=mat([[0,1,0,0],[0,0,1,0]])
j=mm(i,mat([[2,0],[0,1]]));pj=mm(mat([[Q(1,2),0],[0,1]]),p)
for a,b in [(i,p),(j,pj)]:
 need(mm(b,a)==eye(2),'invented PI')
 need(add(mm(gamma,h0),mm(a,b),mm(h1,delta))==eye(4),'invented resolution')
 need(mm(b,gamma)==zero(2,1) and mm(delta,a)==zero(1,2),'invented annihilations')
t=mm(p,j);need(det(t)==2 and mm(adj(t),t)!=eye(2),'det-one not forced')
# Different literal image, same quotient: add gamma to first inclusion column.
jshift=mat([[1,0],[1,0],[0,1],[0,0]]);hshift=mat([[1,-1,0,0]])
need(add(mm(gamma,hshift),mm(jshift,p),mm(h1,delta))==eye(4),'shift resolution')
need(all(v==0 for v in i[0]) and any(v!=0 for v in jshift[0]) and mm(p,jshift)==eye(2),'different image quotient control')
ai=mat([[1,0],[0,1],[0,0],[0,0]]);ap=mat([[1,0,0,0],[0,1,0,0]])
aj=mat([[0,0],[0,0],[1,0],[0,1]]);bp=mat([[0,0,1,0],[0,0,0,1]])
need(mm(ap,ai)==eye(2) and mm(bp,aj)==eye(2) and mm(ap,aj)==zero(2,2),'PI-only control')
# Universal traceless anticommutator checked as coefficient polynomials in four formal entries.
# Four basis pairs suffice by bilinearity: H,E,F span sl2 over Q.
basis=[mat([[1,0],[0,-1]]),mat([[0,1],[0,0]]),mat([[0,0],[1,0]])]
for a in basis:
 for b in basis:
  ab=mm(a,b);tr=ab[0][0]+ab[1][1]
  need(add(ab,mm(b,a))==mat([[tr,0],[0,tr]]),'sl2 bilinear identity')
# Additional exact source bodies: source is parsed, never imported or executed.
check_body(comp,'Circuit','tf',"r,c=self.shape(n);need(r==c==2,'tracefree rank two')\nreturn self.add(n,self.smul(self.scale(self.trace(n),Q(-1,2)),self.eye(2)))")
check_body(comp,'Circuit','inverse',"r,c=self.shape(n);need(r==c==2,'only physical two-by-two inverse')\nreturn self.node('matrix_inverse',(2,2),(n,),source_determinant='one, source theorem required')")
check_body(comp,'Source','mu',"c=self.c;a,b=p\nreturn c.scale(c.add(c.mul(c.D(B,a),c.D(A,b)),c.scale(c.mul(c.D(B,b),c.D(A,a)),-1)),Q(1,2))")
check_body(comp,'Source','b',"c=self.c;i,j,k=t;a,b=p\nqa=c.leaf('physical_q',(1,1),owners=[i,j],coordinate=a)\nqb=c.leaf('physical_q',(1,1),owners=[j,k],coordinate=b)\nreturn c.scale(c.mul(qa,qb),Q(15,4))")
check_body(raw,'PhysicalModel','nu',"out=self.ex.scalar(1)\nfor i in range(4):\n if(o.legal_mask>>i)&1:out=out*(self.y[i]/self.x[i])\nreturn out")

def read(name):return (ROOT/'inputs'/name).read_text()
def sha(data):return hashlib.sha256(data).hexdigest()
def reject(fn,label):
 try:fn()
 except (ValueError,KeyError,StopIteration):return label
 raise ValueError('Negative control unexpectedly accepted: '+label)

def check_producer(text):
 tree=ast.parse(text)
 # Exact critical loop AST, including order of failure and pair append.
 target=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='verify_model')
 loop=next(n for n in target.body if isinstance(n,ast.For) and isinstance(n.target,ast.Tuple))
 expected='''for i, a in enumerate(charts):
 for j, b in enumerate(charts):
  n = [[{} for _ in range(2)] for _ in range(2)]
  for r in range(2):
   for t in range(2):
    for k in range(15):
     n[r][t] = add(n[r][t], multiply(a['P'][r][k], b['I'][k][t]))
  det = add(multiply(n[0][0], n[1][1]), multiply(n[0][1], n[1][0]), -1)
  den = multiply(a['dp'], b['di'])
  if det != multiply(den, den):
   raise ValueError('Determinant identity failed for pair %s' % ((i,j),))
  pairs.append([i,j])'''
 need(ast.dump(loop,include_attributes=False)==ast.dump(ast.parse(expected).body[0],include_attributes=False),'producer normalized pair loop changed')
 for fragment in ["len(model['charts']) != 6", "raw = args.model.read_bytes()", 'result = verify_model(json.loads(raw))', "result['modelSHA256'] = hashlib.sha256(raw).hexdigest()"]:
  need(fragment in text,'producer metadata guard changed')
producer=read('checks__verify_determinants.py.txt');check_producer(producer)
receipt=json.loads(read('certificates__verification.json.txt'))['checks']['determinants']
model_bytes=(ROOT/'inputs/geo__data__model.json.txt').read_bytes()
# Metadata only: never decode or multiply a polynomial entry.
model=json.loads(model_bytes)
need(len(model['charts'])==6,'model chart count')
need([x['pivot'] for x in model['charts']]==[0,1,2,3,4,0],'model pivot metadata')

def check_receipt(r):
 need(r['status']=='PASS' and r['exactDeterminantOneIdentities']==36,'receipt count/status')
 need(r['orderedPairs']==[[i,j] for i in range(6) for j in range(6)],'receipt exact ordered coverage')
 need(r['modelSHA256']==sha(model_bytes),'receipt model binding')
 need(r['pointSamplesUsedAsProof'] is False,'receipt sampling claim')
check_receipt(receipt)
pinmap={p['file']:p for p in json.loads((ROOT/'pins.json').read_text())}
for p in pinmap.values():
 data=(ROOT/p['file']).read_bytes()
 if 'git_blob' in p:
  need(hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==p['git_blob'],'Git blob mismatch')
manifest=json.loads(read('manifest.json.txt'))['sha256']
for upstream,local in {'README.md':'README.md.txt','checks/verify_determinants.py':'checks__verify_determinants.py.txt','certificates/verification.json':'certificates__verification.json.txt','checks/verify_source.py':'checks__verify_source.py.txt','pins.json':'pins.json.txt','verify.py':'verify.py.txt','first-order-source.md':'first-order-source.md.txt'}.items():
 need(manifest[upstream]==sha((ROOT/'inputs'/local).read_bytes()),'selected attribution manifest binding')
deps=json.loads(read('pins.json.txt'))['dependencies']
need(deps['model']['sha256']==sha(model_bytes),'dependency model pin')
need(deps['sourceExcerpts']['sha256']==sha(INPUTS['formulas'].read_bytes()),'dependency formula pin')
geo=json.loads(read('geo__manifest.json.txt'))['sha256']
need(geo['data/model.json']==sha(model_bytes),'geometric model manifest')
need(geo['data/source-formulas.js']==sha(INPUTS['formulas'].read_bytes()),'geometric formula manifest')
need('I=evm(c.I,c.di),P=evm(c.P,c.dp)' in js,'source denominator normalization')
# Universal noncommutative expansion, independent of actual matrix entries.
def polyadd(*polys):
 out={}
 for p in polys:
  for w,c in p.items():out[w]=out.get(w,Q(0))+c
 return {w:c for w,c in out.items() if c}
def scale(p,c):return {w:v*c for w,v in p.items() if v*c}
def prod(a,b):return polyadd(*[{u+v:c*d}for u,c in a.items()for v,d in b.items()])
def comm(a,b):return polyadd(prod(a,b),scale(prod(b,a),-1))
Pa,Pb,Qa,Qb=[{(s,):Q(1)}for s in ['Pa','Pb','Qa','Qb']]
# K=-[log_a,log_b]/2. Delta subtracts K of the sum.
dK=scale(polyadd(comm(Pa,Pb),comm(Qa,Qb),scale(comm(polyadd(Pa,Qa),polyadd(Pb,Qb)),-1)),Q(-1,2))
expected=scale(polyadd(comm(Qa,Pb),scale(comm(Qb,Pa),-1)),Q(1,2))
need(dK==expected,'delta K free-word sign')
# Exhaustive basis combinations prove this multilinear sl2 identity.
def ms(a,c):return tuple(tuple(v*c for v in r)for r in a)
def mc(a,b):return add(mm(a,b),ms(mm(b,a),-1))
def tr(a):return a[0][0]+a[1][1]
for pa in basis:
 for pb in basis:
  for qa in basis:
   for qb in basis:
    C=ms(add(mm(qa,pb),ms(mm(qb,pa),-1)),Q(1,2))
    deltaK=ms(add(mc(qa,pb),ms(mc(qb,pa),-1)),Q(1,2))
    need(deltaK==add(ms(C,2),ms(eye(2),-tr(C))),'delta K sl2 identity')
    need(ms(deltaK,Q(-1,2))==add(ms(C,-1),ms(eye(2),tr(C)/2)),'delta k sign')
# Without trace hypotheses the claimed identity fails, despite K being traceless.
C=ms(basis[0],Q(1,2));need(zero(2,2)!=add(ms(C,2),ms(eye(2),-tr(C))),'trace-hypothesis counterexample')
negative=[]
negative.append(reject(lambda:need(sha(b'changed')==pinmap['inputs/raw_engine.py.txt']['sha256'],'pin mismatch'),'changed input digest'))
negative.append(reject(lambda:check_producer(producer.replace('multiply(den, den)','den')),'missing denominator square'))
negative.append(reject(lambda:check_producer(producer.replace("a['dp'], b['di']","a['di'], b['dp']")),'reversed denominator owners'))
negative.append(reject(lambda:check_receipt(dict(receipt,orderedPairs=receipt['orderedPairs'][:-1])),'missing ordered pair'))
negative.append(reject(lambda:check_receipt(dict(receipt,modelSHA256='0'*64)),'wrong model digest'))
negative.append(reject(lambda:need(scale(dK,-1)==expected,'delta K wrong sign'),'reversed delta K sign'))
wrong=ast.parse(INPUTS['raw'].read_text().replace('(n.inverse(),n)if inverse else(n,n.inverse())','(n,n.inverse())if inverse else(n.inverse(),n)'))
negative.append(reject(lambda:check_body(wrong,'PhysicalModel','Dframe',"n=self.nu(o);a,b=(n.inverse(),n)if inverse else(n,n.inverse());z=self.ex.scalar(0)\nreturn ((a,z),(z,b))"),'reversed reciprocal factors'))
need(len(negative)==7,'negative control count')
print(json.dumps({'status':'PASS','scope':'static source/AST/metadata and formal or invented controls only','optimization_safe_checks':True,'ast_methods':12,'historical_claim_pairs':36,'historical_execution_attested':False,'actual_model_determinants_recomputed':False,'negative_controls':negative,'sl2_basis_combinations':81},indent=2))

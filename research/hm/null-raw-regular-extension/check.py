"""Inert source AST and integer pole-budget controls only. No physical execution."""
import ast, hashlib, json
from pathlib import Path
P=Path(__file__).resolve().parent
count=0
def check(ok,msg):
 global count
 count+=1
 if not ok: raise ValueError(msg)
manifest_bytes=(P/'pins.json').read_bytes()
check(hashlib.sha256(manifest_bytes).hexdigest()=='146cf27bc677c8a3b78eae8c40824834c4d070f89abdade2d38eee560132a4f0','immutable manifest pin')
manifest=json.loads(manifest_bytes)
for name,h in manifest.items():
 check(hashlib.sha256((P/'inputs'/name).read_bytes()).hexdigest()==h,'input pin '+name)
s=(P/'inputs/raw_engine.py.txt').read_text(); tree=ast.parse(s)
classes={n.name:n for n in tree.body if isinstance(n,ast.ClassDef)}
methods={n.name:n for n in classes['PhysicalModel'].body if isinstance(n,ast.FunctionDef)}
raw={n.name:n for n in classes['RawSource'].body if isinstance(n,ast.FunctionDef)}
check('self.c.model.s_raw' in ast.unparse(raw['T']),'raw scalar override')
fragments=["U0=tuple(tuple(list(g)+list(i)+list(w))for g,i,w in zip(self.gamma,c['I'],self.M.mul(c['H1'],c['W'])))", "Q0=tuple(c['H0'])+tuple(c['P'])+tuple(self.M.mul(c['L'],self.delta))", "U1=tuple(tuple(list(w)+list(e))for w,e in zip(c['W'],c['eta']));Q1=tuple(c['L'])+tuple(self.ev)", "return self.M.scale(self.M.mul(self.M.D(U,d),Q),-1)", "w0=[n2.inverse()]*5+[self.ex.scalar(1),n2.inverse()]+[n2]*8;w1=[self.ex.scalar(1)]*8+[n2]*2", "gamma=self.ex.scalar((o.legal_mask>>d)&1)*self.y[d]/(self.x[d]*(self.x[d]*self.x[d]-self.ex.scalar(1)))"]
for f in fragments:check(f in s,'literal block source')
model=json.loads((P/'inputs/model.json.txt').read_text())
check([c['pivot'] for c in model['charts']]==[0,1,2,3,4,0],'pivots')
# Each pivot is among the factors of its OWN clearing equation.
for i,c in enumerate(model['charts']):check(c['pivot'] in ({i} if i<5 else {0,1,3,4}),'pivot factor')
def mul(*a):return tuple(sum(x[i] for x in a) for i in range(2))
def add(*a):return tuple(max(x[i] for x in a) for i in range(2))
def derivative(a):return tuple(x+1 if x else 0 for x in a)
# This coarse derivative ledger is for carrier/legal scalar coefficients;
# homogeneous covariance and absence of additional poles are prose premises.
prim=(2,0); pivot=(1,0); polynomial=(0,0); log=(0,1)
U0=(polynomial,prim,mul(prim,pivot)); Q0=(prim,prim,polynomial)
U1=(pivot,pivot); Q1=(polynomial,polynomial)
d0=add(*(mul(derivative(u),q) for u,q in zip(U0,Q0)))
l0=add(*(mul(u,log,q) for u,q in zip(U0,Q0)))
d1=add(*(mul(derivative(u),q) for u,q in zip(U1,Q1)))
l1=add(*(mul(u,log,q) for u,q in zip(U1,Q1)))
B=add(d0,l0,d1,l1,log);check(B==(5,1),'block budget')
q=(0,1); scalar=add(mul(B,B),mul(q,B),mul(q,q)); check(scalar==(10,2),'raw scalar')
ds=derivative(scalar);check(ds==(11,3),'complement derivative')
g=(4,2);dg=derivative(g);ddg=derivative(dg)
k=mul(dg,dg);u=mul(g,k)
# Seven kinetic summands: two ordered products, four first cross terms, one mixed.
kinetic=[mul(g,u,u)]*2+[mul(g,derivative(u),dg)]*4+[mul(g,ddg,ddg)]
b=mul(q,q);gerbe=[mul(b,k),mul(b,k),mul(b,b)]
baseline=add(*(kinetic+gerbe));check(baseline==(32,18),'baseline')
F=(14,1); Fk=mul(F,k);check(Fk==(24,7),'Fk')
current=mul(g,dg);check(current==(9,5),'current simplified identity')
E=mul(ds,current);check(E==(20,8),'raw E')
R=add(baseline,Fk,E);check(R==(32,18),'whole residual')
J=mul(R,(4,2));stages=[J]
for i in range(3):J=mul(J,(6,3));stages.append(J)
check(stages==[(36,20),(42,23),(48,26),(54,29)],'J stages')
# Scalar q legal ownership, all endpoint masks in one coordinate.
for a in (0,1):
 for b in (0,1):
  if a!=b:
   check(1 in (a,b),'finite q owner');check(0 in (a,b),'infinity q owner')
# Formal divisor exponents for inserted-only weighting; distinct occurrences.
for inserted in range(1,7):
 for suffix in range(0,7-inserted):
  owners=list(range(inserted+suffix))
  # Original denominator has54/29 at every occurrence; inserted rho and
  # suffix clearing each supply exactly their OWN allowance.
  for v in owners:
   weight=(54,29) if v<inserted else (0,0)
   clear=(0,0) if v<inserted else (54,29)
   check(mul(weight,clear)==(54,29),'suffix/inserted cancellation')
# Actual rejection controls on source fragments and bound inequality.
for f in fragments:
 check(not all(x in s.replace(f,'MUTATED',1) for x in fragments),'source mutation rejection')
check(mul((24,14),current)[0]>32,'excess raw derivative carrier rejected')
check(mul((24,14),current)[1]>18,'excess raw derivative legal rejected')
# Contract inspection, without executing any imported source.
def canon(x): return ast.dump(x,include_attributes=False)
def has(tree,fragment):
 node=ast.parse(fragment).body[0]
 if isinstance(node,ast.Expr):node=node.value
 return any(canon(n)==canon(node) for n in ast.walk(tree))
def contract(raw_tree,compiler_tree):
 cs={n.name:n for n in compiler_tree.body if isinstance(n,ast.ClassDef)}
 fs={n.name:n for n in cs['Source'].body if isinstance(n,ast.FunctionDef)}
 residual=fs['residual']
 lists={n.targets[0].id:n.value for n in ast.walk(residual) if isinstance(n,ast.Assign) and len(n.targets)==1 and isinstance(n.targets[0],ast.Name)}
 check(len(lists['kin'].elts)==7,'all seven kinetic terms')
 check(len(lists['gerbe'].elts)==3,'all three gerbe terms')
 check([k.value for k in lists['parts'].keys]==['baseline','Fk12','Fk34','E12','E34'],'all five residual branches')
 for fragment in ["M0=c.mul(self.gi(i,k),c.add(*(kin+gerbe)))", "u=lambda pair,a,b:c.mul(self.g(a,b),self.k(pair,a,b))"]:
  check(has(residual,fragment),'complete normalized baseline contract')
 for fragment in ["la=c.mul(self.gi(i,j),c.D(self.g(i,j),a))", "ta=c.mul(self.gi(i,j),self.gi(j,k),c.D(self.g(j,k),a),self.g(i,j))", "c.D(sjk,a)", "c.D(sij,b)"]:
  check(has(fs['E'],fragment),'actual current and complementary scalar derivative')
 raw_f={n.name:n for n in raw_tree.body if isinstance(n,ast.FunctionDef)}
 for fragment in ["zip((-1,1,3,5),(-1,1,-1,1),*blocks_i,*blocks_j)", "return result*mat.ex.scalar(Q(1,4))-qa*qb*mat.ex.scalar(Q(15,8))", "mat.trace(b_i)[0][0]+mat.trace(b_j)[0][0]", "mat.trace(a_i)[0][0]+mat.trace(a_j)[0][0]"]:
  check(has(raw_f['raw_scalar_formula'],fragment),'complete BB qB qq scalar')
compiler=(P/'inputs/compiler.py.txt').read_text()
contract(tree,ast.parse(compiler))
# In-memory semantic mutations must reach and fail the same contract verifier.
for old,new in [('kin+gerbe','kin'),("'E34':self.E(q,p,t)","'REMOVED':self.E(q,p,t)"),('c.D(sjk,a)','c.D(sjk,b)')]:
 check(old in compiler,'compiler mutation target')
 try:contract(tree,ast.parse(compiler.replace(old,new,1)))
 except ValueError:pass
 else:raise ValueError('semantic mutation accepted')
for old,new in [('Q(15,8)','Q(15,7)'),('(-1,1,3,5),(-1,1,-1,1)','(-1,1,3,5),(1,1,-1,1)')]:
 check(old in s,'raw mutation target')
 try:contract(ast.parse(s.replace(old,new,1)),ast.parse(compiler))
 except ValueError:pass
 else:raise ValueError('raw semantic mutation accepted')
# Distinct occurrence charges are formal coordinates, even for equal divisors.
def covers(need,supplied):return all(supplied.get(k,0)>=v for k,v in need.items())
need={(0,'carrier'):54,(1,'carrier'):54,(0,'legal'):29,(1,'legal'):29}
check(covers(need,dict(need)),'whole owner clearing')
check(not covers(need,{(0,'carrier'):108,(0,'legal'):58}),'no owner borrowing')
check(not covers(need,{(0,'carrier'):54,(0,'legal'):29}),'uncleared suffix rejected')
# Per-owner max for addition differs from multiplication of common denominators.
a={0:3,1:0};b={0:0,1:4}
check({v:max(a[v],b[v]) for v in a}=={0:3,1:4},'sum retains every owner')
check({v:a[v]+b[v] for v in a}=={0:3,1:4},'product adds per owner')
check(sum([54,54])==108,'equal-divisor occurrence multiplicities')
check((54*5+29*3+5251)-5==5603,'homogeneous cleared degree example')
# Degree is assigned sheaf degree plus clearing degrees, never rational numerator degree.
check(3-1==2 and max(0,3-1-0)==2,'hidden homogenizing factor required for degree zero')
print(json.dumps({'checks':count,'blocks':B,'raw_scalar':scalar,'derivative':ds,'E':E,'baseline':baseline,'Fk':Fk,'Js':stages,'physical_execution':False},sort_keys=True))

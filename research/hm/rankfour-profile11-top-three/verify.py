#!/usr/bin/env python3
"""Fixed universal representation checks for the top-degree-three boundary."""
from collections import Counter
from pathlib import Path
import hashlib,json,sys
import characters as c
P=Path(__file__).resolve().parent
checks=0

def req(ok,msg):
 global checks
 checks+=1
 if not ok:raise RuntimeError(msg)
def norm(v):return dict(sorted((r,n) for r,n in v.items() if n))
def rank(B):return sum(c.DIM[r] for e,r in B)
def deg(B):return sum(e*c.DIM[r] for e,r in B)
def h1(B,t):
 v=Counter()
 for e,r in B:
  if e+t<=-2:v.update(c.product(r,-e-t-2))
 return v
def chi(B,t):
 v=c.h0(B,t);v.subtract(h1(B,t));return v
def genuine(v):return all(n>=0 for n in v.values())
def hom(B,R,e):return sum(c.product(R,e-d)[r] for d,r in B)
def split(R3,R4,N):
 return [(-3,r) for r,n in R3.items() for _ in range(n)]+[(-4,r) for r,n in R4.items() for _ in range(n)]+N

for row in json.loads((P/'INPUTS.json').read_text()):
 b=(P/row['file']).read_bytes()
 req(len(b)==row['bytes'],row['file']+' bytes')
 req(hashlib.sha256(b).hexdigest()==row['sha256'],row['file']+' sha256')
 req(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==row['git_blob_sha1'],row['file']+' blob')
 req(row['ref'] in row['url'],row['file']+' immutable')

sources={
'D':[(-2,'D'),(-3,'Wp'),(-3,'T'),(-4,'V'),(-8,'one')],
'P':[(-2,'P'),(-3,'Wp'),(-3,'T'),(-4,'V'),(-5,'Wp')],
'V':[(-2,'V'),(-3,'Wp'),(-3,'T'),(-4,'V'),(-4,'V')],
'Z':[(-3,'Wp'),(-3,'T'),(-3,'T'),(-4,'V')]}
for key,E in sources.items():
 req(rank(E)==17 and deg(E)==-54,key+' rank degree')
 req(chi(E,3)==Counter(Wp=1,T=2),key+' chi3')
 req(chi(E,4)==Counter(V=3,P=3,D=2),key+' chi4')
H=[]
for key,E in sources.items():
 for R in ('W','Wp'):
  for e in (-7,-5,-3):
   d=hom(E,R,e)
   expected=int(R=='Wp' and e==-3 or key=='P' and R=='Wp' and e==-5 or key=='D' and R=='W' and e==-7)
   req(d==expected,'complete negative doublet Hom')
   H.append({'source':key,'target':[e,R],'dimension':d})
 req(hom(E,'one',0)==0,key+' scalar degree0 absent')
 req(hom(E,'one',-8)==int(key=='D'),key+' scalar minus8')
req([i for i,b in enumerate(sources['D']) if hom([b],'W',-7)]==[4],'W minus7 only source scalar rank1')
for key,E in sources.items():
 req([b for b in E if hom([b],'Wp',-3)]==[(-3,'Wp')],key+' Wp minus3 supported on displayed block')
req(6-2+9*(-1)>-8,'negative doublet degree minus1 excluded')
req(c.product('W',6)==Counter(Wp=1,T=2),'positive W cubic')
req(c.product('Wp',6)==Counter(W=1,Wp=1,S=1,T=1),'positive Wp cubic')

Q={
'a':[(3,'W'),(-3,'Wp')],
'b':[(3,'W'),(-5,'Wp')],
'c':[(3,'Wp'),(2,'one'),(-8,'one')],
'd':[(3,'W'),(2,'one'),(-8,'one')]}
exp3={'a':Counter(Wp=-1),'b':Counter(Wp=1),'c':Counter(W=-1),'d':Counter(S=1,T=-1)}
exp4={'a':Counter(V=2,D=1),'c':Counter(D=1,V=1,P=1,one=-1),'d':Counter(A=1,D=1,V=1)}
targets={'a':Counter(D=1,V=1,P=1),'b':Counter(D=1,V=1,P=1),'c':Counter(A=1,D=2,P=1),'d':Counter(D=2,V=1,P=1)}
euler={}
for key,A in Q.items():
 req(rank(A)==4,'rank4 quotient')
 x3=chi(sources['D'],3);x3.subtract(chi(A,3))
 x4=chi(sources['D'],4);x4.subtract(chi(A,4))
 req(norm(x3)==norm(exp3[key]),key+' cubic Euler')
 if key in exp4:req(norm(x4)==norm(exp4[key]),key+' quartic Euler')
 req(c.h0(A,2)==targets[key],key+' derivative target')
 euler[key]={'chi3':norm(x3),'chi4':norm(x4),'derivative_target':norm(c.h0(A,2))}
req(c.h0(Q['a'],1)==Counter(S=1,T=1),'a excludes Wp cubic kernel')
req(c.h0(Q['b'],1)==Counter(S=1,T=1),'b excludes Wp cubic kernel')

# At most 54 single-block products, under the proved H1 dimension-six bound.
allowed_targets=[Counter(Wp=1),Counter(W=1),Counter(S=1,Wp=1),Counter(S=1,W=1),Counter(T=1)]
even={'one','A','V','P','D'}
atoms=[]
for j in range(5,11):
 for R in c.NAMES:
  if j%2 != (0 if R in even else 1) or (j-4)*c.DIM[R]>6:continue
  v=c.product(R,j-5)
  if any(all(v[r]<=X[r] for r in v) for X in allowed_targets):
   atoms.append((-j,R))
expected_atoms=[(-5,'W'),(-5,'Wp'),(-5,'S'),(-5,'T'),(-6,'one'),(-6,'A'),(-6,'V'),(-7,'W'),(-7,'Wp'),(-8,'one'),(-10,'one')]
req(set(atoms)==set(expected_atoms),'complete fixed cohomology atom table')
atom_table=[{'block':[e,R],'H1_3':norm(h1([(e,R)],3)),'H1_4':norm(h1([(e,R)],4))} for e,R in expected_atoms]

# Explicit symbolic decompositions from the multiplicity-one table; no K multiset search.
choices={
'Wp':[[(-5,'Wp')]],
'W':[[(-5,'W')],[(-6,'one')]],
'S_Wp':[[(-5,'S'),(-5,'Wp')],[(-8,'one'),(-5,'Wp')]],
'S_W':[[(-5,'S'),(-5,'W')],[(-5,'S'),(-6,'one')],[(-8,'one'),(-5,'W')],[(-8,'one'),(-6,'one')],[(-6,'A')],[(-7,'W')]],
'T':[[(-5,'T')],[(-6,'V')],[(-7,'Wp')],[(-10,'one')]]}
chars={'Wp':Counter(Wp=1),'W':Counter(W=1),'S_Wp':Counter(S=1,Wp=1),'S_W':Counter(S=1,W=1),'T':Counter(T=1)}
for name,rows in choices.items():
 for N in rows:req(h1(N,3)==chars[name],name+' exact lower block contribution')

def check_branch(q,R3,option,expected_survivors):
 rows=[];surv=[]
 for N in choices[option]:
  R4=exp4[q].copy()
  for R,n in R3.items():
   z=c.product(R,1);R4.subtract({r:n*m for r,m in z.items()})
  R4.update(h1(N,4))
  ok=genuine(R4) and all(R4[r]<=targets[q][r] for r in R4)
  if ok:
   B=split(R3,+R4,N);req(rank(B)==13 and deg(B)==-54,'retained kernel rank degree');surv.append(B)
  rows.append({'N':N,'R4':norm(R4),'genuine':genuine(R4),'passes_near_top':ok})
 req(len(surv)==expected_survivors,q+option+' survivor count for explicit displayed rows')
 return rows,surv
records={};retained=[]
for label,q,R3,ch,n in [
('a_zero','a',Counter(),'Wp',0),('a_S','a',Counter(S=1),'S_Wp',0),
('c_zero','c',Counter(),'W',0),('c_S','c',Counter(S=1),'S_W',0),
('d_S','d',Counter(S=1),'T',3)]:
 records[label],res=check_branch(q,R3,ch,n)
 if res:retained=res
expected=[
[(-3,'S'),(-4,'V'),(-5,'T')],
[(-3,'S'),(-4,'V'),(-4,'P'),(-7,'Wp')],
[(-3,'S'),(-4,'V'),(-4,'D'),(-10,'one')]]
req({tuple(sorted(x)) for x in retained}=={tuple(sorted(x)) for x in expected},'exact final three K shapes')
for B in retained:
 req(c.h0(B,3)==Counter(S=1) and h1(B,3)==Counter(T=1),'final cubic cohomology')
 req(norm(chi(B,4))==norm(exp4['d']),'final quartic Euler')

mutations=[
('allow negative doublet minus1',lambda:req(4+9*(-1)<=-8,'scalar capacity')),
('pretend rank1 source onto doublet',lambda:req(c.DIM['one']>=c.DIM['W'],'source rank')),
('discard second T',lambda:req(c.product('Wp',6)['T']>=2,'two T')),
('allow P cubic Wp',lambda:req(c.h0(Q['b'],1)['Wp']>=1,'cubic visibility')),
('make negative coefficient genuine',lambda:req(genuine(Counter(V=2,A=-1)),'genuine R4')),
('double V target',lambda:req(targets['a']['V']>=2,'V multiplicity')),
('supply missing V in c target',lambda:req(targets['c']['V']>=1,'physical marking')),
('keep V minus6 option',lambda:req(records['d_S'][1]['passes_near_top'],'near-top V obstruction'))]
rejected=[]
for name,fn in mutations:
 try:fn()
 except RuntimeError:rejected.append(name)
 else:raise RuntimeError('mutation survived '+name)
req(len(rejected)==8,'all controls rejected')
out={'claim':'Top degree3 forces D source, W O3+O2+O-8 quotient, and three necessary K shapes',
'checks':checks+c.checks,'authenticated_inputs':9,'max_symmetric_degree':8,
'negative_doublet_Hom':H,'quotient_euler':euler,'cohomology_atoms':atom_table,'explicit_branch_checks':records,
'necessary_K_shapes':retained,'rejected_mutations':rejected,
'global_quotient_enumeration':False,'actual_instance_evaluated':False,'profile_closure':False,'realization_claim':False}
s=json.dumps(out,indent=2,sort_keys=True)+'\n'
if '--write' in sys.argv:(P/'RESULT.json').write_text(s)
else:req((P/'RESULT.json').read_text()==s,'exact result replay')
print(json.dumps({'checks':out['checks'],'authenticated_inputs':9,'mutations_rejected':8,'necessary_K_shapes':3,'result_sha256':hashlib.sha256(s.encode()).hexdigest()},sort_keys=True))

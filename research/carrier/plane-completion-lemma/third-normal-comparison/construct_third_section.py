#!/usr/bin/env python3
"""Exact cubic section equations for the literal completed third-middle gauge."""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib
import section_action_support as a
n=a.n;R=Path(__file__).resolve().parent
PINS={'THIRD_MIDDLE_COCHAINS.json':'011ba80d06f7b47a077845f377e9b22a5a9e51d808804e88e2ba4bf66c2306cd','SECOND_NORMAL_SECTION_CORRECTIONS.json':'c6f2120accbc6d8900a4ceef9fb2ba1258fcc790dd323657b47c48c7630e905f'}
for f,h in PINS.items():
 if hashlib.sha256((R/f).read_bytes()).hexdigest()!=h:raise ValueError(('input hash',f))
checks=[]
def zero(label,p):
 if p:raise ValueError((label,p))
 checks.append(label)
def vzero(label,v):
 for i,p in enumerate(v):zero(label+':'+str(i),p)
def exp(label):
 e=[0]*5
 if label!='1':
  for x in label.split('*'):e[['a','b','c','d','lambda'].index(x)]+=1
 return tuple(e)
def unpack_v(records):return {tuple(r['open']):[{tuple(e):Q(c) for e,c in p} for p in r['components']] for r in records}
def add(*ps):
 out={}
 for p in ps:
  for e,v in p.items():out[e]=n.vadd(out.get(e,n.Z4),v)
 return out
def scale(p,c):return {e:[n.scale(t,c) for t in v] for e,v in p.items()}
def act(qs,vs,inf,patch,ds=None):
 out={};ds=ds or {}
 for e,q in qs.items():
  for f,v in vs.items():
   k=tuple(x+y for x,y in zip(e,f));out[k]=n.vadd(out.get(k,n.Z4),a.act(q,v,ds.get(f,{}),inf,patch))
 return out
first=[n.data['origin'],*n.data['directions']]
eta={exp(name):tuple(n.tensor(obj[k]) for k in ['finite','infinity','mixed']) for name,obj in zip(['1','a','b','c','d'],first)}
kap={exp(name):tuple(a.cert_tensor(obj['original_cover_primitive'][k]) for k in ['finite_W_primitive','infinity_W_primitive','mixed_W_primitive']) for name,obj in a.cert['coefficients'].items()}
kap[exp('lambda')]=({}, {},{(i,):{(1,1):n.mono(z=-1)} for i in range(3)})
third=json.loads((R/'THIRD_MIDDLE_COCHAINS.json').read_text())
nu={exp(name):tuple(a.cert_tensor(obj['original_cover_primitive'][k]) for k in ['finite_W_primitive','infinity_W_primitive','mixed_W_primitive']) for name,obj in third.items()}
xi={exp(name):n.all_sections['origin' if name=='1' else name] for name in ['1','a','b','c','d']}
sigma={exp(name):{ch:unpack_v(v) for ch,v in obj.items()} for name,obj in json.loads((R/'SECOND_NORMAL_SECTION_CORRECTIONS.json').read_text()).items()}
v={exp('1'):[{},n.mono(),{},{}]};rhs=[]
for chart in range(3):
 inf=chart==1;opened=n.PAIRS if chart<2 else [(i,) for i in range(3)];cochain={}
 for ij in opened:
  patch=ij[0];ch='infinity' if inf else 'finite'
  A={e:q[chart].get(ij,{}) for e,q in eta.items()};B={e:q[chart].get(ij,{}) for e,q in kap.items()};C={e:q[chart].get(ij,{}) for e,q in nu.items()}
  x={e:q[ch].get((patch,),n.Z4) for e,q in xi.items()};s={e:q[ch].get((patch,),n.Z4) for e,q in sigma.items()};d={exp('1'):n.mono() if inf else n.z}
  Av=act(A,v,inf,patch);Bv=act(B,v,inf,patch)
  Ax=act(A,x,inf,patch,d)
  value=add(act(C,v,inf,patch),act(A,s,inf,patch),act(B,x,inf,patch,d),scale(act(A,Ax,inf,patch),Q(1,2)),scale(add(act(A,Bv,inf,patch),act(B,Av,inf,patch)),Q(1,2)),scale(act(A,act(A,Av,inf,patch),inf,patch),Q(1,6)))
  if any(e not in nu for e,q in value.items() if any(q)):raise ValueError('unexpected parameter monomial')
  cochain[ij]=value
 rhs.append(cochain)
result={};export={}
for name,obj in third.items():
 e=exp(name);ss=[];obstructions=[]
 for chart in range(2):
  inf=chart==1;r=n.rI if inf else n.rF;cochain={ij:q.get(e,n.Z4) for ij,q in rhs[chart].items()}
  dv=n.vdelta(cochain,1).get(n.TOP,n.Z4);f=n.shift(dv[3],X=-1,Y=-1)
  vzero(name+': closed modulo relation '+str(chart),n.vadd(dv,n.vscale(r,n.neg(f))))
  zero(name+': top obstruction '+str(chart),n.pi(f))
  zz=n.hom({n.TOP:f});zero(name+': relation primitive '+str(chart),n.add(n.delta(zz,1).get(n.TOP,{}),n.neg(f)))
  closed={ij:n.vadd(q,n.vscale(r,n.neg(zz.get(ij,{})))) for ij,q in cochain.items()}
  vzero(name+': B closed '+str(chart),n.vdelta(closed,1).get(n.TOP,n.Z4))
  tau=n.vhom(closed);dt=n.vdelta(tau,0)
  for ij in n.PAIRS:vzero(name+': plane primitive '+str((chart,ij)),n.vadd(dt.get(ij,n.Z4),n.vscale(closed[ij],n.mono(c=-1))))
  pd=[-6,-3,-7,-7];weights=[3,6,0,2] if inf else [3,0,2,2]
  for opened,vec in tau.items():
   for slot,p in enumerate(vec):
    for ex in p:
     if sum(ex[1:])!=pd[slot]:raise ValueError('plane degree')
     if 2*ex[0]+ex[1]+ex[2]!=weights[slot]+(-3 if inf else 3):raise ValueError('character')
     if any(ex[k+1]<0 for k in range(3) if k not in opened):raise ValueError('plane pole')
     if ex[0]>0 if inf else ex[0]<0:raise ValueError('base pole')
  checks.append(name+': regular graded '+str(chart));ss.append(tau)
 for i in range(3):
  residual=n.vadd(n.trans(ss[1].get((i,),n.Z4)),n.vscale(ss[0].get((i,),n.Z4),n.mono(c=-1)),n.vscale(rhs[2][(i,)].get(e,n.Z4),n.mono(c=-1)))
  f=n.shift(residual[3],X=-1,Y=-1);vzero(name+': mixed '+str(i),n.vadd(residual,n.vscale(n.rF,n.neg(f))))
 result[name]={'finite_terms':sum(len(p) for v in ss[0].values() for p in v),'infinity_terms':sum(len(p) for v in ss[1].values() for p in v)}
 export[name]={'finite':n.packc(ss[0]),'infinity':n.packc(ss[1])}
 print(name,result[name],flush=True)
(R/'THIRD_NORMAL_SECTION_CORRECTIONS.json').write_text(json.dumps(export,indent=2)+'\n')
(R/'THIRD_NORMAL_SECTION_CHECKS.json').write_text(json.dumps({'checks':checks,'count':len(checks),'all_passed':True,'coefficients':result,'inputs':PINS,'scope':'Order-three section on our completed plane with literal frozen third-middle gauge and +t0h pairing modulo h4.'},indent=2)+'\n')
print('THIRD SECTION PASS',len(checks),flush=True)

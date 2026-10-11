#!/usr/bin/env python3
"""Direct negative-exponential check of exported cubic sections."""
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
taus={exp(name):{ch:unpack_v(v) for ch,v in obj.items()} for name,obj in json.loads((R/'THIRD_NORMAL_SECTION_CORRECTIONS.json').read_text()).items()}
v={exp('1'):[{},n.mono(),{},{}]};residuals={}
def edge_residual(chart,ij):
 inf=chart==1;ch="infinity" if inf else "finite"
 i=ij[0];j=ij[-1]
 A={e:q[chart].get(ij,{}) for e,q in eta.items()};B={e:q[chart].get(ij,{}) for e,q in kap.items()};C={e:q[chart].get(ij,{}) for e,q in nu.items()}
 if chart<2:
  gx={e:q[ch].get((j,),n.Z4) for e,q in xi.items()}
  gx[exp('1')]=n.vadd(gx[exp('1')],n.vscale((n.wI if inf else n.wF)[ij],n.mono() if inf else n.z))
  gs={e:q[ch].get((j,),n.Z4) for e,q in sigma.items()}
  delta={e:n.vadd(q[ch].get((j,),n.Z4),n.vscale(q[ch].get((i,),n.Z4),n.mono(c=-1))) for e,q in taus.items()}
 else:
  gx={e:n.trans(q['infinity'].get((i,),n.Z4)) for e,q in xi.items()};gx[exp('1')]=n.vadd(gx[exp('1')],n.ks[i])
  gs={e:n.trans(q['infinity'].get((i,),n.Z4)) for e,q in sigma.items()}
  delta={e:n.vadd(n.trans(q['infinity'].get((i,),n.Z4)),n.vscale(q['finite'].get((i,),n.Z4),n.mono(c=-1))) for e,q in taus.items()}
 ds={exp('1'):n.mono() if inf else n.z}
 Agx=act(A,gx,inf,i,ds);Av=act(A,v,inf,i);Bv=act(B,v,inf,i)
 # Coefficient of h3 in exp(-hA-h2B-h3C) g(s_j)-s_i.
 residual=add(delta,scale(act(A,gs,inf,i),-1),scale(act(A,Agx,inf,i),Q(1,2)),scale(act(B,gx,inf,i,ds),-1),scale(act(C,v,inf,i),-1),scale(add(act(A,Bv,inf,i),act(B,Av,inf,i)),Q(1,2)),scale(act(A,act(A,Av,inf,i),inf,i),Q(-1,6)))
 return residual
for chart in range(3):
 inf=chart==1;opened=n.PAIRS if chart<2 else [(i,) for i in range(3)];r=n.rI if inf else n.rF
 for ij in opened:
  residual=edge_residual(chart,ij)
  for name,obj in third.items():
   e=exp(name);q=residual.get(e,n.Z4);f=n.shift(q[3],X=-1,Y=-1)
   vzero(name+': direct negative exponential '+str((chart,ij)),n.vadd(q,n.vscale(r,n.neg(f))))
   for p in q:
    for ex in p:
     if any(ex[k+1]<0 for k in range(3) if k not in ij):raise ValueError('residual has forbidden plane pole')
  residuals[(chart,ij)]=residual
# Change the actual finite X-patch E0 section coefficient by z³/X³.
# On edge01 this subtracts that monomial from the verified residual.
taus[exp('1')]['finite'][(0,)][1]=n.add(taus[exp('1')]['finite'][(0,)][1],n.mono(z=3,X=-3))
q=edge_residual(0,(0,1))[exp('1')];f=n.shift(q[3],X=-1,Y=-1)
try:vzero('negative control',n.vadd(q,n.vscale(n.rF,n.neg(f))))
except ValueError as exc:
 if exc.args[0][1]!=n.mono(z=3,X=-3,c=-1):raise ValueError('unexpected negative control failure')
 checks.append('actual finite X-patch origin E0 correction mutation rejected with exact -z³/X³ residual')
else:raise ValueError('section mutation accepted')
report={'scope':'Direct negative-exponential order-three section equation using source-side lower sections and actual baseline q transports; no positive-formula/generator import.','count':len(checks),'checks':checks,'all_passed':True,'input_sha256':hashlib.sha256((R/'THIRD_NORMAL_SECTION_CORRECTIONS.json').read_bytes()).hexdigest()}
(R/'THIRD_NORMAL_DIRECT_EQUATION_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n')
print('DIRECT NEGATIVE EXPONENTIAL PASS',len(checks),flush=True)

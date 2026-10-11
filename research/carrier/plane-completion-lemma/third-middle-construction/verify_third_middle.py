#!/usr/bin/env python3
"""Separate tensor-slot verification of raw cubic BCH and exported primitives."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations_with_replacement
import json,hashlib
import tensor_slot_support as n
R=Path(__file__).resolve().parent
PINS={'first_jet.json': '2be28aebeb2ff40754f17ca94f76b68eb40043f6492a1794bd91436bc27e1f10', 'certificate.json': 'c03a36fca19b7a73b8c483c7dc9e2a17f4a1ea422e9a61972966b734cd5597e4', 'order_3.json': 'e9aec49580b90c90c3acfb09683d5a5df3a101969e755373c221e20ff47efcf0', 'pinned_contraction.py': '5e8b20bc7f11dd9061336d9ff6be5efcb2b8fd86555d65dfb5f14e7eeac11168'}
for filename,digest in PINS.items():
 if hashlib.sha256((R/filename).read_bytes()).hexdigest()!=digest:raise ValueError("Input hash mismatch: "+filename)
checks=[]
def zero(name,q):
 for slot,p in q.items():
  if p:raise ValueError((name,slot,p))
 checks.append(name)
def tc(records):
 out={}
 for rec in records:
  q={}
  for ex,c in rec['terms']:
   ij=tuple(i for i,k in enumerate(ex[4:]) for _ in range(k))
   if len(ij)!=2:raise ValueError('not quadratic')
   q[ij]=n.add(q.get(ij,{}),{tuple(ex[:4]):Q(c)})
  out[tuple(rec['open'])]=q
 return out
def ts(q,c):return {ij:n.scale(p,c) for ij,p in q.items()}
def omega(i,j,chart):
 if i==j:return {}
 if i>j:return n.neg(omega(j,i,chart))
 return {(1,2):n.F,(1,3):n.shift(n.g,z=-1) if chart else n.g,(2,3):n.power(n.S,3) if chart else n.w}.get((i,j),{})
def bracket(p,q,chart):
 out={}
 for (i,j),a in p.items():
  for (k,l),b in q.items():
   ab=n.mul(a,b)
   for u,v,x,y in [(i,k,j,l),(i,l,j,k),(j,k,i,l),(j,l,i,k)]:
    ij=tuple(sorted((u,v)));out[ij]=n.add(out.get(ij,{}),n.mul(ab,omega(x,y,chart)))
 return {ij:p for ij,p in out.items() if p}
def exp(label):
 e=[0]*5
 if label!='1':
  for x in label.split('*'):e[['a','b','c','d','lambda'].index(x)]+=1
 return tuple(e)
def add(*ps):
 out={}
 for p in ps:
  for e,q in p.items():out[e]=n.ta(out.get(e,{}),q)
 return out
def scale(p,c):return {e:ts(q,c) for e,q in p.items()}
def br(p,q,chart):
 out={}
 for e,u in p.items():
  for f,v in q.items():
   k=tuple(a+b for a,b in zip(e,f));out[k]=n.ta(out.get(k,{}),bracket(u,v,chart))
 return out
def N(x,y,c):return add(br(x,br(x,y,c),c),br(y,br(y,x,c),c))
def at(cs,ch,o,tr=False):return {e:n.transport_tensor(c[ch].get(o,{})) if tr else c[ch].get(o,{}) for e,c in cs.items()}
cert=json.loads((R/'certificate.json').read_text());out=json.loads((R/'THIRD_MIDDLE_COCHAINS.json').read_text())
etas={exp(name):tuple(n.tensor(obj[k]) for k in ['finite','infinity','mixed']) for name,obj in zip(['1','a','b','c','d'],[n.data['origin'],*n.data['directions']])}
kappas={exp(name):tuple(tc(rec['original_cover_primitive'][k]) for k in ['finite_W_primitive','infinity_W_primitive','mixed_W_primitive']) for name,rec in cert['coefficients'].items()}
kappas[exp('lambda')]=({}, {},{(i,):{(1,1):n.mono(z=-1)} for i in range(3)})
raw=[]
for ch in [0,1]:
 x,y=at(etas,ch,(0,1)),at(etas,ch,(1,2));u,v=at(kappas,ch,(0,1)),at(kappas,ch,(1,2))
 raw.append(add(scale(add(br(x,v,ch),br(u,y,ch)),Q(1,2)),scale(N(x,y,ch),Q(-1,12))))
rawh={}
for i,j in n.PAIRS:
 hi,hj,F,I=at(etas,2,(i,)),at(etas,2,(j,)),at(etas,0,(i,j)),at(etas,1,(i,j),True)
 ki,kj,KF,KI=at(kappas,2,(i,)),at(kappas,2,(j,)),at(kappas,0,(i,j)),at(kappas,1,(i,j),True)
 rawh[(i,j)]=add(scale(add(br(hi,KI,0),br(ki,I,0),scale(br(F,kj,0),-1),scale(br(KF,hj,0),-1)),Q(1,2)),scale(add(N(hj,F,0),scale(N(I,hi,0),-1)),Q(1,12)))
terms=0
for name,rec in out.items():
 e=exp(name)
 if tuple(rec['parameter_exponents'])!=e:raise ValueError('parameter label')
 p=rec['original_cover_primitive'];nus=tuple(tc(p[k]) for k in ['finite_W_primitive','infinity_W_primitive','mixed_W_primitive'])
 for chart in [0,1]:
  n.quotient_tensor(n.ta(n.td(nus[chart],1).get(n.TOP,{}),n.tn(raw[chart].get(e,{}))),n.rI if chart else n.rF,name+': raw plane'+str(chart))
  saved=tc([{'open':[0,1,2],'terms':rec['raw_stages']['infinity_BCH' if chart else 'finite_BCH']}])[n.TOP]
  zero(name+': independently rebuilt plane '+str(chart),n.ta(saved,n.tn(raw[chart].get(e,{}))))
 for ij in n.PAIRS:
  q=n.ta(n.transport_tensor(nus[1].get(ij,{})),n.tn(nus[0].get(ij,{})),n.tn(n.td(nus[2],0).get(ij,{})),n.tn(rawh[ij].get(e,{})))
  n.quotient_tensor(q,n.rF,name+': raw mixed '+str(ij))
 savedh=tc(rec['raw_stages']['mixed_BCH'])
 for ij in n.PAIRS:zero(name+': independently rebuilt mixed '+str(ij),n.ta(savedh.get(ij,{}),n.tn(rawh[ij].get(e,{}))))
 for ch,chain in enumerate(nus):
  d=[3,6,0,2] if ch==1 else [3,0,2,2];pd=[-3,0,-4,-4]
  for opened,q in chain.items():
   for (i,j),poly in q.items():
    for ex in poly:
     terms+=1
     if sum(ex[1:])!=pd[i]+pd[j]-1:raise ValueError('plane degree')
     if 2*ex[0]+ex[1]+ex[2]!=d[i]+d[j]+(-5 if ch==1 else -1):raise ValueError('character')
     if any(ex[k+1]<0 for k in range(3) if k not in opened):raise ValueError('plane pole')
     if ch!=2 and (ex[0]>0 if ch==1 else ex[0]<0):raise ValueError('base pole')
 checks.append(name+': all exported grades and regularity')
 if e[4]:
  old=cert['lambda_order_three']['coefficients'][name.replace('*lambda','').replace('lambda','1')]['original_cover_primitive']
  if p!=old:raise ValueError(('lambda slice differs',name))
  checks.append(name+': exact supplied lambda-slice agreement')
# An actual tensor coefficient corruption must fail the same quotient gate.
mut=tc(out['1']['original_cover_primitive']['finite_W_primitive']);bad={(1,1):n.mono(X=-1,Y=-1,W=1)}
mut[(0,1)]=n.ta(mut.get((0,1),{}),bad)
try:n.quotient_tensor(n.ta(n.td(mut,1).get(n.TOP,{}),n.tn(raw[0].get((0,)*5,{}))),n.rF,'mutation')
except ValueError as exc:
 if exc.args[0][1]!=bad[(1,1)]:raise ValueError('unexpected mutation residual')
 checks.append('actual origin finite01 primitive mutation rejected with exact E0² X^-1Y^-1W residual')
else:raise ValueError('mutation accepted')
report={'scope':'Separate tensor-slot reconstruction of all cubic RHS and quotient equations; no generator or contraction import.','coefficient_count':len(out),'exported_terms':terms,'checks':checks,'quotient_checks':n.checks,'count':len(checks)+len(n.checks),'all_passed':True,'output_sha256':hashlib.sha256((R/'THIRD_MIDDLE_COCHAINS.json').read_bytes()).hexdigest()}
(R/'THIRD_MIDDLE_INDEPENDENT_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n')
print('INDEPENDENT PASS',report['count'],'checks',terms,'terms')

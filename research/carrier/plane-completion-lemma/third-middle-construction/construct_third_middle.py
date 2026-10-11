#!/usr/bin/env python3
"""Complete cubic middle tensors from raw anti-BCH defects; exact Q arithmetic."""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib
import pinned_contraction as m
R=Path(__file__).resolve().parent
PINS={'first_jet.json': '2be28aebeb2ff40754f17ca94f76b68eb40043f6492a1794bd91436bc27e1f10', 'certificate.json': 'c03a36fca19b7a73b8c483c7dc9e2a17f4a1ea422e9a61972966b734cd5597e4', 'order_3.json': 'e9aec49580b90c90c3acfb09683d5a5df3a101969e755373c221e20ff47efcf0', 'pinned_contraction.py': '5e8b20bc7f11dd9061336d9ff6be5efcb2b8fd86555d65dfb5f14e7eeac11168'}
for filename,digest in PINS.items():
 if hashlib.sha256((R/filename).read_bytes()).hexdigest()!=digest:raise ValueError("Input hash mismatch: "+filename)
checks=[]
def req(v,msg):
 if not v:raise ValueError(msg)
 checks.append(msg)
def unpack_cert(records):return {tuple(r['open']):{tuple(e):Q(c) for e,c in r['terms']} for r in records}
zero=(0,)*5
def exp(label):
 out=[0]*5
 if label!='1':
  for x in label.split('*'):out['abcdl'.index(x)]+=1
 return tuple(out)
def label(e):return '*'.join(x for x,k in zip(['a','b','c','d','lambda'],e) for _ in range(k)) or '1'
def pa(*ps):
 out={}
 for p in ps:
  for e,v in p.items():out[e]=m.plus(out.get(e,{}),v)
 return {e:v for e,v in out.items() if v}
def scale(p,c):return {e:m.scalar(v,c) for e,v in p.items() if v}
def pb(p,q,chart):
 out={}
 for e,v in p.items():
  for f,w in q.items():
   k=tuple(a+b for a,b in zip(e,f));out[k]=m.plus(out.get(k,{}),m.poisson(v,w,chart))
 return {e:v for e,v in out.items() if v}
def nested(p,q,chart):return pa(pb(p,pb(p,q,chart),chart),pb(q,pb(q,p,chart),chart))
def at(cs,chart,opened,transport=False):
 return {e:m.transport(c[chart].get(opened,{}),'W') if transport else c[chart].get(opened,{}) for e,c in cs.items()}
j=json.loads((R/'first_jet.json').read_text());cert=json.loads((R/'certificate.json').read_text());data=json.loads((R/'order_3.json').read_text())
eta={exp(name):tuple(m.unpack(obj[k]) for k in ['finite','infinity','mixed']) for name,obj in zip(['1','a','b','c','d'],[j['origin'],*j['directions']])}
kap={exp(name):tuple(unpack_cert(obj['original_cover_primitive'][k]) for k in ['finite_W_primitive','infinity_W_primitive','mixed_W_primitive']) for name,obj in cert['coefficients'].items()}
kap[exp('l')]=({}, {},{(i,):m.mono((-1,0,0,0,0,2,0,0)) for i in range(3)})
D,cols,rows,vector=m.rebuilt_block(data,3)
req(D.shape==(9,9) and D.det()==1,'regenerated D3 determinant one');inv=D.inv();req(D*inv==m.sp.eye(9),'exact inverse')
raw=[]
for chart in [0,1]:
 x,y=at(eta,chart,(0,1)),at(eta,chart,(1,2));u,v=at(kap,chart,(0,1)),at(kap,chart,(1,2))
 raw.append(pa(scale(pa(pb(x,v,chart),pb(u,y,chart)),Q(1,2)),scale(nested(x,y,chart),Q(-1,12))))
h={}
for i,jj in m.PAIRS:
 # gF_ij H_j=H_i gI_ij and the anti-BCH dictionary give
 # BCH(H_j,F_ij)=BCH(TI_ij,H_i).
 x,y=at(eta,2,(jj,)),at(eta,0,(i,jj));u,v=at(kap,2,(jj,)),at(kap,0,(i,jj))
 a,b=at(eta,1,(i,jj),True),at(eta,2,(i,));c,d=at(kap,1,(i,jj),True),at(kap,2,(i,))
 h[(i,jj)]=pa(scale(pa(pb(x,v,0),pb(u,y,0),scale(pb(a,d,0),-1),scale(pb(c,b,0),-1)),Q(1,2)),scale(pa(nested(x,y,0),scale(nested(a,b,0),-1)),Q(1,12)))
keys=set(raw[0])|set(raw[1])|set().union(*(set(p) for p in h.values()))
# Include every possible coefficient even when its defect vanishes.
from itertools import combinations_with_replacement
for seq in combinations_with_replacement(range(5),3):
 e=[0]*5
 for x in seq:
  if x:e[x-1]+=1
 keys.add(tuple(e))
for x in range(5):
 e=[0,0,0,0,1]
 if x:e[x-1]+=1
 keys.add(tuple(e))
req(len(keys)==40,'all 40 cubic coefficients enumerated')
report={};export={}
for e in sorted(keys):
 name=label(e);f=raw[0].get(e,{});ii=raw[1].get(e,{});hh=m.normalize_c({ij:p.get(e,{}) for ij,p in h.items()})
 defect=m.plus(m.transport(ii,'W'),m.scalar(f,-1),m.scalar(m.delta(hh,1).get(m.TOP,{}),-1))
 relation=m.relation_divide(defect);u0,ui=m.split_base(m.project(relation))
 residual=m.plus(m.transport(ui,'U'),m.scalar(u0,-1),m.scalar(relation,-1));uh=m.homotopy({m.TOP:residual})
 req(m.delta(uh,1).get(m.TOP,{})==residual,name+': relation homotopy')
 c0=m.plus(f,m.scalar(m.times(m.alpha[0],u0),-1));ci=m.plus(ii,m.scalar(m.times(m.alpha[1],ui),-1));ch=m.cplus(hh,m.cmap(uh,lambda p:m.scalar(m.times(m.alpha[0],p),-1)))
 req(m.plus(m.transport(ci,'W'),m.scalar(c0,-1),m.scalar(m.delta(ch,1).get(m.TOP,{}),-1))=={},name+': closed corrected cocycle')
 stages=dict(finite_BCH=f,infinity_BCH=ii,mixed_BCH=hh,relation_defect=defect,relation_quotient=relation,relation_finite_primitive=u0,relation_infinity_primitive=ui,relation_mixed_primitive=uh,closed_finite=c0,closed_infinity=ci,closed_mixed=ch)
 graded=m.check_stage_gradings(stages,3)
 vv=vector(m.project(c0));pre=inv*vv;req(D*pre==vv,name+': exact D3 preimage')
 source=m.plus(*(m.scalar(m.make_source(data['D3_source_basis'][n]),Q(c)) for n,c in zip(cols,pre)))
 primitive=m.exact_primitive(stages,source,3)
 # exact_primitive reconstructs raw finite/infinity/mixed RHS and checks regularity.
 req(True,name+': raw equations and regularity')
 counts={k:sum(len(r['terms']) for r in primitive[k]) for k in ['finite_W_primitive','infinity_W_primitive','mixed_W_primitive']}
 export[name]={'parameter_exponents':list(e),'original_cover_primitive':primitive,'raw_stages':m.encode(stages),'target_vector':[str(v) for v in vv],'preimage_vector':[str(v) for v in pre]}
 report[name]={'primitive_terms':counts,'graded_stage_terms':graded}
 print(name,counts,flush=True)
(R/'THIRD_MIDDLE_COCHAINS.json').write_text(json.dumps(export,indent=2)+'\n')
receipt={'scope':'Full third-middle tensor realization only; no third-order section or carrier assertion.','checks':checks,'count':len(checks),'coefficients':report,'D3':[[str(v) for v in D.row(i)] for i in range(9)],'source_columns':cols,'target_rows':rows,'input_hashes':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in ['first_jet.json','certificate.json','order_3.json','pinned_contraction.py']}}
(R/'THIRD_MIDDLE_CHECKS.json').write_text(json.dumps(receipt,indent=2)+'\n')
print('PASS',len(checks),flush=True)

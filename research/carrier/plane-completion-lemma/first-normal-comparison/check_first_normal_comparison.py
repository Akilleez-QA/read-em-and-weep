#!/usr/bin/env python3
"""Independent Laurent-Cech first-normal comparison; no producer code imports."""
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import hashlib,json

HERE=Path(__file__).resolve().parent
INPUT=HERE/'first_jet.json'
PIN='2be28aebeb2ff40754f17ca94f76b68eb40043f6492a1794bd91436bc27e1f10'
if hashlib.sha256(INPUT.read_bytes()).hexdigest()!=PIN:raise ValueError('Unpinned first jet')
data=json.loads(INPUT.read_text())
checks=[]

def add(*ps):
 out={}
 for p in ps:
  for e,c in p.items():
   out[e]=out.get(e,Q(0))+c
   if not out[e]:del out[e]
 return out

def scale(p,c):return {e:v*c for e,v in p.items() if v*c}
def mul(p,q):
 out={}
 for e,a in p.items():
  for f,b in q.items():
   k=tuple(x+y for x,y in zip(e,f));out[k]=out.get(k,Q(0))+a*b
   if not out[k]:del out[k]
 return out

def mono(z=0,X=0,Y=0,W=0,c=1):return {(z,X,Y,W):Q(c)} if c else {}
def shift(p,z=0,X=0,Y=0,W=0,c=1):return mul(p,mono(z,X,Y,W,c))
def power(p,n):
 out=mono()
 for _ in range(n):out=mul(out,p)
 return out

def neg(p):return scale(p,-1)
def vadd(*vs):return [add(*(v[i] for v in vs)) for i in range(len(vs[0]))]
def vscale(v,p):return [mul(q,p) for q in v]
def cross(u,v):return [add(mul(u[1],v[2]),neg(mul(u[2],v[1]))),add(mul(u[2],v[0]),neg(mul(u[0],v[2]))),add(mul(u[0],v[1]),neg(mul(u[1],v[0])))]
def dot(u,v):return add(*(mul(p,q) for p,q in zip(u,v)))
def zero(label,p):
 if p:raise ValueError((label,p))
 checks.append(label)

def vzero(label,v):
 for i,p in enumerate(v):zero(label+':'+str(i),p)

def delta(c,degree):
 out={}
 for ij in combinations(range(3),degree+2):
  p=add(*(scale(c.get(ij[:i]+ij[i+1:],{}),(-1)**i) for i in range(len(ij))))
  if p:out[ij]=p
 return out

def hom(c):
 out={}
 for ij,p in c.items():
  for e,v in p.items():
   choices=[i for i in range(3) if e[i+1]>=0]
   if choices and choices[0] in ij:
    q=choices[0];key=tuple(j for j in ij if j!=q)
    out[key]=add(out.get(key,{}),{e:v*(-1)**ij.index(q)})
 return {k:v for k,v in out.items() if v}

def pi(p):return {e:c for e,c in p.items() if all(x<0 for x in e[1:])}
def vdelta(c,degree):
 ds=[delta({k:v[i] for k,v in c.items()},degree) for i in range(4)]
 keys=set().union(*(d.keys() for d in ds));return {k:[d.get(k,{}) for d in ds] for k in keys}

def vhom(c):
 hs=[hom({k:v[i] for k,v in c.items()}) for i in range(4)]
 keys=set().union(*(d.keys() for d in hs));return {k:[h.get(k,{}) for h in hs] for k in keys}

def regular(label,c):
 for ij,p in c.items():
  for e in p:
   if any(e[k+1]<0 for k in range(3) if k not in ij):raise ValueError(('Nonregular',label,ij,e))
 checks.append(label+':regular')

def vregular(label,c):
 for j in range(4):regular(label+':'+str(j),{k:v[j] for k,v in c.items()})

z,X,Y,W=[mono(**{v:1}) for v in ['z','X','Y','W']]
S=add(power(X,2),power(Y,2));F=mul(X,Y);a=add(power(X,3),power(Y,3));w=power(W,6)
g=add(S,neg(mul(z,power(W,2))));C=add(power(S,2),mul(z,mul(S,power(W,2))),mul(power(z,2),power(W,4)))
T=add(scale(S,-3),scale(F,2));rF=[neg(a),w,neg(g),F];rI=[neg(a),power(S,3),neg(shift(g,z=-1)),F]
TOP=(0,1,2);PAIRS=list(combinations(range(3),2));Z4=[{},{},{},{}]

def trans(v):return [shift(v[0],z=3),add(v[1],shift(mul(C,v[2]),z=1)),shift(v[2],z=4),shift(v[3],z=3)]

def lambdas(inf):
 ls=[]
 for coord in ['X','Y']:
  q=power(X if coord=='X' else Y,2)
  last=mul(F,add(power(F,2),neg(power(S,2)),scale(mul(S,q),-2)))
  if inf:ls.append([shift(mono(),**{coord:-6}),{},shift(last,**{coord:-8})])
  else:ls.append([shift(mono(z=3),**{coord:-6}),neg(shift(C,**{coord:-6})),shift(last,**{coord:-8})])
 if inf:ls.append([mono(z=-3,W=-6),shift(C,z=-2,W=-6),{}])
 else:ls.append([mono(W=-6),{},{}])
 return ls

def plane(inf):
 r=rI if inf else rF;ls=lambdas(inf);label='infinity' if inf else 'finite'
 for i,l in enumerate(ls):zero(label+':lambda:'+str(i),add(dot(l,r[1:]),neg(mono())))
 d=dot(ls[0],cross(ls[1],ls[2]));central=mul(power(a,2),d)
 zero(label+':central_top_projection',pi(central))
 cs=hom({TOP:neg(central)})
 zero(label+':central_primitive',add(delta(cs,1).get(TOP,{}),central))
 ws={ij:[cs.get(ij,{})]+vscale(cross(ls[ij[0]],ls[ij[1]]),a) for ij in PAIRS}
 vzero(label+':presentation_triple',vadd(vdelta(ws,1).get(TOP,Z4),vscale(r,neg(mul(a,d)))))
 vregular(label+':plane_shift',ws)
 return ls,d,ws

LF,dF,wF=plane(False);LI,dI,wI=plane(True)
# Cross-base shifts for these standard-coordinate local completions.
bs=[]
for i in range(3):
 mu=[shift(LI[i][0],z=3),add(neg(mul(C,LI[i][0])),shift(LI[i][1],z=-1)),LI[i][2]]
 zero('cross_mu_unit:'+str(i),add(dot(mu,rF[1:]),neg(mono())))
 bs.append([{}]+vscale(cross(LF[i],mu),mul(z,a)))
kappa={}
for i,j in PAIRS:
 dv=vadd(bs[i],trans(wI[(i,j)]),vscale(wF[(i,j)],neg(z)),vscale(bs[j],mono(c=-1)))
 coeff=shift(dv[3],X=-1,Y=-1)
 vzero('cross_precentral:'+str((i,j)),[add(dv[k],neg(mul(coeff,rF[k]))) for k in [1,2,3]])
 kappa[(i,j)]=add(dv[0],mul(a,coeff))
zero('cross_central_closed',delta(kappa,1).get(TOP,{}))
ts=hom(kappa)
for ij in PAIRS:zero('cross_central_primitive:'+str(ij),add(delta(ts,0).get(ij,{}),neg(kappa[ij])))
ks={i:[ts.get((i,),{})]+bs[i][1:] for i in range(3)}
vregular('cross_shift',{(i,):ks[i] for i in range(3)})

# Direct action A_eta(E0)={eta,E0}, with diagonal terms counted twice.
def evaluation(records,inf):
 # omega(B_j,E0)=(0,0,-F,-g_chart).
 om=[{},{},neg(F),neg(shift(g,z=-1) if inf else g)]
 out={}
 for rec in records:
  v=[{},{},{},{}]
  for (i,j),e,c in rec['terms']:
   p={tuple(e):Q(c)};v[i]=add(v[i],mul(p,om[j]));v[j]=add(v[j],mul(p,om[i]))
  out[tuple(rec['open'])]=v
 return out

def section_primitive(ev,inf,origin):
 r=rI if inf else rF;d=dI if inf else dF;ws=wI if inf else wF
 t0=mono() if inf else z
 y={ij:vadd(ev.get(ij,Z4),vscale(ws[ij],neg(t0)) if origin else Z4) for ij in PAIRS}
 dy=vdelta(y,1).get(TOP,Z4);scalar=shift(dy[3],X=-1,Y=-1)
 vzero(('I' if inf else 'F')+':section_relation',vadd(dy,vscale(r,neg(scalar))))
 zero(('I' if inf else 'F')+':section_obstruction',pi(scalar))
 zz=hom({TOP:scalar});zero('section_relation_primitive',add(delta(zz,1).get(TOP,{}),neg(scalar)))
 closed={ij:vadd(y[ij],vscale(r,neg(zz.get(ij,{})))) for ij in PAIRS}
 vzero('section_B_closed',vdelta(closed,1).get(TOP,Z4))
 ss=vhom(closed)
 ds=vdelta(ss,0)
 for ij in PAIRS:vzero('section_B_primitive:'+str(ij),vadd(ds.get(ij,Z4),vscale(closed[ij],mono(c=-1))))
 vregular('section_primitive_regular',ss)
 weights=[3,6,0,2] if inf else [3,0,2,2]
 for opened,vec in ss.items():
  for slot,poly in enumerate(vec):
   for ex in poly:
    if (ex[0]>0 if inf else ex[0]<0):raise ValueError(('Base pole in section primitive',inf,opened,slot,ex))
    if 2*ex[0]+ex[1]+ex[2] != weights[slot]+(-5 if inf else 1):raise ValueError(('Section character mismatch',inf,opened,slot,ex))
 checks.append(('infinity' if inf else 'finite')+':section_base_regular_and_homogeneous')
 return ss,zz

results={};all_sections={}
for name,obj in [('origin',data['origin'])]+[(q['name'],q) for q in data['directions']]:
 ef=evaluation(obj['finite'],False);ei=evaluation(obj['infinity'],True);eh=evaluation(obj['mixed'],False)
 for inf,ev,r in [(False,ef,rF),(True,ei,rI)]:
  dv=vdelta(ev,1).get(TOP,Z4);c=shift(dv[3],X=-1,Y=-1)
  vzero(name+':evaluated_plane_cocycle',vadd(dv,vscale(r,neg(c))))
 for ij in PAIRS:
  dv=vadd(trans(ei.get(ij,Z4)),vscale(ef.get(ij,Z4),mono(c=-1)),vscale(vdelta(eh,0).get(ij,Z4),mono(c=-1)))
  c=shift(dv[3],X=-1,Y=-1);vzero(name+':evaluated_mixed_cocycle',vadd(dv,vscale(rF,neg(c))))
 eftriple=vdelta(ef,1).get(TOP,Z4);ec=pi(shift(eftriple[3],X=-1,Y=-1))
 expected=pi(mul(z,mul(a,dF))) if name=='origin' else {}
 zero(name+':class_comparison',add(ec,neg(expected)))
 sf,zf=section_primitive(ef,False,name=='origin');si,zi=section_primitive(ei,True,name=='origin')
 # exp(-h A_eta) transition convention: section correction has boundary +ev(eta).
 for i in range(3):
  mismatch=vadd(ks[i] if name=='origin' else Z4,trans(si.get((i,),Z4)),vscale(sf.get((i,),Z4),mono(c=-1)),vscale(eh.get((i,),Z4),mono(c=-1)))
  coeff=shift(mismatch[3],X=-1,Y=-1)
  vzero(name+':section_mixed_match:'+str(i),vadd(mismatch,vscale(rF,neg(coeff))))
  regular(name+':section_mixed_relation_regular',{(i,):coeff})
 results[name]={'evaluated_class':[[list(e),str(c)] for e,c in sorted(ec.items())],
                'section_correction_terms_finite':sum(len(p) for v in sf.values() for p in v),
                'section_correction_terms_infinity':sum(len(p) for v in si.values() for p in v)}
 all_sections[name]={'finite':sf,'infinity':si,'finite_relation':zf,'infinity_relation':zi}
 print(name,results[name],flush=True)

# The full middle cochains, not only their evaluation on E0, descend to n.
SLOTS=list(combinations(range(4),2))+[(i,i) for i in range(4)]
def tensor(records):
 out={}
 for rec in records:
  v={}
  for ij,e,c in rec['terms']:
   key=tuple(ij);v[key]=add(v.get(key,{}),{tuple(e):Q(c)})
  out[tuple(rec['open'])]=v
 return out

def ta(*qs):return {ij:add(*(q.get(ij,{}) for q in qs)) for ij in SLOTS}
def tn(q):return {ij:neg(p) for ij,p in q.items()}
def td(c,degree):
 out={}
 for opened in combinations(range(3),degree+2):
  out[opened]=ta(*({ij:scale(p,(-1)**j) for ij,p in c.get(opened[:j]+opened[j+1:],{}).items()} for j in range(len(opened))))
 return out

def transport_tensor(q):
 cols=[{0:mono(z=3)},{1:mono()},{1:shift(C,z=1),2:mono(z=4)},{3:mono(z=3)}]
 out={}
 for (i,j),p in q.items():
  for k,x in cols[i].items():
   for l,y in cols[j].items():
    slot=tuple(sorted((k,l)));out[slot]=add(out.get(slot,{}),shift(mul(p,mul(x,y)),z=-4))
 return out

def quotient_tensor(q,r,label):
 xx=[{}, {}, {}, shift(q.get((3,3),{}),X=-1,Y=-1)]
 for i in range(3):xx[i]=shift(add(q.get((i,3),{}),neg(mul(r[i],xx[3]))),X=-1,Y=-1)
 for i,j in SLOTS:
  expected=mul(r[i],xx[j]) if i==j else add(mul(r[i],xx[j]),mul(r[j],xx[i]))
  zero(label+':'+str((i,j)),add(q.get((i,j),{}),neg(expected)))

for name,obj in [('origin',data['origin'])]+[(q['name'],q) for q in data['directions']]:
 tf=tensor(obj['finite']);ti=tensor(obj['infinity']);th=tensor(obj['mixed'])
 quotient_tensor(td(tf,1).get(TOP,{}),rF,name+':middle_finite')
 quotient_tensor(td(ti,1).get(TOP,{}),rI,name+':middle_infinity')
 for ij in PAIRS:
  quotient_tensor(ta(transport_tensor(ti.get(ij,{})),tn(tf.get(ij,{})),tn(td(th,0).get(ij,{}))),rF,name+':middle_mixed:'+str(ij))

# All artifacts contain coefficients, formulas or exact mathematical check receipts only.
def pack(p):return [[list(e),str(c)] for e,c in sorted(p.items())]
def packc(c):return [{'open':list(ij),'components':[pack(p) for p in v]} for ij,v in sorted(c.items())]
sections={name:{'finite':packc(v['finite']),'infinity':packc(v['infinity'])} for name,v in all_sections.items()}
output={'scope':'First-normal comparison for our completed plane object; transition convention exp(-h A_eta); no ancestor identification.',
        'first_jet_sha256':PIN,'results':results,'checks':checks,'count':len(checks),'all_passed':True}
(HERE/'FIRST_NORMAL_COMPARISON_CHECKS.json').write_text(json.dumps(output,indent=2)+'\n')
(HERE/'FIRST_NORMAL_SECTION_CORRECTIONS.json').write_text(json.dumps(sections,indent=2)+'\n')
print('PASS',len(checks),'exact checks',flush=True)

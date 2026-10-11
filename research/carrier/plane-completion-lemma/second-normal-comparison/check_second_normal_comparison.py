#!/usr/bin/env python3
"""Exact order-two middle/section realization on the constructed completion."""
from fractions import Fraction as Q
from pathlib import Path
import hashlib,json
from itertools import combinations_with_replacement
import first_order_support as n

HERE=Path(__file__).resolve().parent
PIN='c03a36fca19b7a73b8c483c7dc9e2a17f4a1ea422e9a61972966b734cd5597e4'
source=HERE/'certificate.json'
if hashlib.sha256(source.read_bytes()).hexdigest()!=PIN:raise ValueError('Second primitive input hash mismatch')
cert=json.loads(source.read_text())
checks=[]

def zero(label,p):
 if p:raise ValueError((label,p))
 checks.append(label)

def vzero(label,v):
 for i,p in enumerate(v):zero(label+':'+str(i),p)

def tensor_zero_mod_relation(q,r,label):
 xx=[{}, {}, {}, n.shift(q.get((3,3),{}),X=-1,Y=-1)]
 for i in range(3):xx[i]=n.shift(n.add(q.get((i,3),{}),n.neg(n.mul(r[i],xx[3]))),X=-1,Y=-1)
 for i,j in n.SLOTS:
  expected=n.mul(r[i],xx[j]) if i==j else n.add(n.mul(r[i],xx[j]),n.mul(r[j],xx[i]))
  zero(label+':'+str((i,j)),n.add(q.get((i,j),{}),n.neg(expected)))

def cert_tensor(records):
 result={}
 for rec in records:
  q={}
  for ex,c in rec['terms']:
   inds=[i for i,k in enumerate(ex[4:]) for _ in range(k)]
   if len(inds)!=2:raise ValueError('Not quadratic primitive')
   ij=tuple(inds);q[ij]=n.add(q.get(ij,{}),{tuple(ex[:4]):Q(c)})
  result[tuple(rec['open'])]=q
 return result

def tscale(q,c):return {ij:n.scale(v,c) for ij,v in q.items()}
def omega(i,j,inf):
 if i==j:return {}
 if i>j:return n.neg(omega(j,i,inf))
 return {(1,2):n.F,(1,3):n.shift(n.g,z=-1) if inf else n.g,(2,3):n.power(n.S,3) if inf else n.w}.get((i,j),{})

def bracket(p,q,inf):
 out={}
 for (i,j),v in p.items():
  for (k,l),w in q.items():
   vw=n.mul(v,w)
   for u1,u2,a,b in [(j,l,i,k),(j,k,i,l),(i,l,j,k),(i,k,j,l)]:
    ij=tuple(sorted((u1,u2)));out[ij]=n.add(out.get(ij,{}),n.mul(vw,omega(a,b,inf)))
 return out

def act(q,vec,d,inf,patch):
 lam=(n.LI if inf else n.LF)[patch]
 psi=[n.mono()]+[n.mul(n.a,p) for p in lam]
 pairing=[n.add(*(n.mul(omega(i,j,inf),vec[j]) for j in range(4)),n.mul(psi[i],d)) for i in range(4)]
 out=[{},{},{},{}]
 for (i,j),p in q.items():
  out[i]=n.add(out[i],n.mul(p,pairing[j]));out[j]=n.add(out[j],n.mul(p,pairing[i]))
 return out

basis=[n.data['origin'],*n.data['directions']];names=['1','a','b','c','d']
eta=[tuple(n.tensor(obj[k]) for k in ['finite','infinity','mixed']) for obj in basis]
v=[{},n.mono(),{},{}]
firstsections=[n.all_sections['origin']]+[n.all_sections[x] for x in ['a','b','c','d']]
result={};export={}

for ii,jj in combinations_with_replacement(range(5),2):
 label='1' if ii==jj==0 else names[jj] if ii==0 else names[ii]+'*'+names[jj]
 ordered=[(ii,jj)] if ii==jj else [(ii,jj),(jj,ii)]
 primitive=cert['coefficients'][label]['original_cover_primitive']
 kap=tuple(cert_tensor(primitive[k]) for k in ['finite_W_primitive','infinity_W_primitive','mixed_W_primitive'])
 # Recompute the raw quadratic correction RHS from the actual frozen first tensors.
 rawF={};rawI={};rawH={ij:{} for ij in n.PAIRS}
 for i,j in ordered:
  rawF=n.ta(rawF,tscale(bracket(eta[i][0].get((0,1),{}),eta[j][0].get((1,2),{}),False),Q(1,2)))
  rawI=n.ta(rawI,tscale(bracket(eta[i][1].get((0,1),{}),eta[j][1].get((1,2),{}),True),Q(1,2)))
  for k,l in n.PAIRS:
   h=n.ta(bracket(eta[i][2].get((k,),{}),n.transport_tensor(eta[j][1].get((k,l),{})),False),n.tn(bracket(eta[i][0].get((k,l),{}),eta[j][2].get((l,),{}),False)))
   rawH[(k,l)]=n.ta(rawH[(k,l)],tscale(h,Q(1,2)))
 tensor_zero_mod_relation(n.ta(n.td(kap[0],1).get(n.TOP,{}),n.tn(rawF)),n.rF,label+':raw_middle_finite')
 tensor_zero_mod_relation(n.ta(n.td(kap[1],1).get(n.TOP,{}),n.tn(rawI)),n.rI,label+':raw_middle_infinity')
 for ij in n.PAIRS:
  tensor_zero_mod_relation(n.ta(n.transport_tensor(kap[1].get(ij,{})),n.tn(kap[0].get(ij,{})),n.tn(n.td(kap[2],0).get(ij,{})),n.tn(rawH[ij])),n.rF,label+':raw_middle_mixed:'+str(ij))
 # All middle primitive coefficients have the stated order-two grades and domains.
 for chart,cochain in enumerate(kap):
  inf=chart==1;weights=[3,6,0,2] if inf else [3,0,2,2];pdeg=[-3,0,-4,-4]
  for opened,q in cochain.items():
   for (i,j),poly in q.items():
    for ex in poly:
     if any(ex[k+1]<0 for k in range(3) if k not in opened):raise ValueError('Middle plane pole')
     if chart!=2 and (ex[0]>0 if inf else ex[0]<0):raise ValueError('Middle base pole')
     if sum(ex[1:])!=pdeg[i]+pdeg[j]:raise ValueError('Middle plane grade')
     if 2*ex[0]+ex[1]+ex[2]!=(-6 if inf else -2)+weights[i]+weights[j]:raise ValueError('Middle character')
 checks.append(label+':middle_regular_and_graded')
 rhs=[]
 for chart in range(3):
  inf=chart==1;opens=n.PAIRS if chart<2 else [(i,) for i in range(3)];cochain={}
  for opened in opens:
   patch=opened[0]
   value=act(kap[chart].get(opened,{}),v,{},inf,patch)
   for i,j in ordered:
    q=eta[i][chart].get(opened,{})
    s=firstsections[j]['infinity' if inf else 'finite'].get((patch,),n.Z4)
    d=(n.mono() if inf else n.z) if j==0 else {}
    term=act(q,s,d,inf,patch)
    inner=act(eta[j][chart].get(opened,{}),v,{},inf,patch)
    square=n.vscale(act(q,inner,{},inf,patch),n.mono(c=Q(1,2)))
    value=n.vadd(value,term,square)
   cochain[opened]=value
  rhs.append(cochain)
 # Exact regular primitives in G I²; no appeal to stored rank flags.
 sigmas=[]
 for chart in range(2):
  inf=chart==1;r=n.rI if inf else n.rF;cochain=rhs[chart]
  dv=n.vdelta(cochain,1).get(n.TOP,n.Z4);f=n.shift(dv[3],X=-1,Y=-1)
  vzero(label+':section_closed:'+str(chart),n.vadd(dv,n.vscale(r,n.neg(f))))
  zero(label+':section_top_class:'+str(chart),n.pi(f))
  zz=n.hom({n.TOP:f});zero(label+':relation_primitive:'+str(chart),n.add(n.delta(zz,1).get(n.TOP,{}),n.neg(f)))
  closed={ij:n.vadd(cochain[ij],n.vscale(r,n.neg(zz.get(ij,{})))) for ij in n.PAIRS}
  vzero(label+':B_closed:'+str(chart),n.vdelta(closed,1).get(n.TOP,n.Z4))
  ss=n.vhom(closed);ds=n.vdelta(ss,0)
  for ij in n.PAIRS:vzero(label+':section_primitive:'+str((chart,ij)),n.vadd(ds.get(ij,n.Z4),n.vscale(closed[ij],n.mono(c=-1))))
  weights=[3,6,0,2] if inf else [3,0,2,2];pdeg=[-5,-2,-6,-6]
  for opened,vec in ss.items():
   for slot,poly in enumerate(vec):
    for ex in poly:
     if any(ex[k+1]<0 for k in range(3) if k not in opened):raise ValueError(('Section plane pole',label,chart,opened,ex))
     if ex[0]>0 if inf else ex[0]<0:raise ValueError('Section base pole')
     if sum(ex[1:])!=pdeg[slot]:raise ValueError('Section plane grade')
     if 2*ex[0]+ex[1]+ex[2] != weights[slot]+(-4 if inf else 2):raise ValueError('Section character')
  checks.append(label+':section_regular_and_graded:'+str(chart));sigmas.append(ss)
 for i in range(3):
  mismatch=n.vadd(n.trans(sigmas[1].get((i,),n.Z4)),n.vscale(sigmas[0].get((i,),n.Z4),n.mono(c=-1)),n.vscale(rhs[2].get((i,),n.Z4),n.mono(c=-1)))
  coeff=n.shift(mismatch[3],X=-1,Y=-1)
  vzero(label+':mixed_section:'+str(i),n.vadd(mismatch,n.vscale(n.rF,n.neg(coeff))))
 result[label]={'finite_terms':sum(len(p) for v in sigmas[0].values() for p in v),'infinity_terms':sum(len(p) for v in sigmas[1].values() for p in v)}
 export[label]={'finite':n.packc(sigmas[0]),'infinity':n.packc(sigmas[1])}
 print(label,result[label],flush=True)

# The lambda second-middle class is mixed z^-1 E0². Its section contribution
# at this order is identically zero, with no first-order lambda term.
kappa_lambda={(1,1):n.mono(z=-1)}
for i in range(3):vzero('lambda:section_zero:'+str(i),act(kappa_lambda,v,{},False,i))
lambda_cochain={(i,):kappa_lambda for i in range(3)}
for ij in n.PAIRS:
 for slot,poly in n.td(lambda_cochain,0).get(ij,{}).items():zero('lambda:plane_constancy:'+str((ij,slot)),poly)
for ex in kappa_lambda[(1,1)]:
 if sum(ex[1:])!=0 or 2*ex[0]+ex[1]+ex[2]!=-2:raise ValueError('Lambda grade')
checks.append('lambda:regular_mixed_order_two_character')
# A targeted coefficient mutation has a nonzero quotient residual.
# Add X^-1 Y^-1 W² E0² to kappa_F,01 only; its triangle defect is that
# same monomial and is not divisible by r. It must fail this exact gate.
mutation={(1,1):n.mono(X=-1,Y=-1,W=2)}
mutant=cert_tensor(cert['coefficients']['1']['original_cover_primitive']['finite_W_primitive'])
mutant[(0,1)]=n.ta(mutant[(0,1)],mutation)
origin_raw=tscale(bracket(eta[0][0].get((0,1),{}),eta[0][0].get((1,2),{}),False),Q(1,2))
mutant_defect=n.ta(n.td(mutant,1).get(n.TOP,{}),n.tn(origin_raw))
try: tensor_zero_mod_relation(mutant_defect,n.rF,'negative_control')
except ValueError as exc:
 if exc.args[0][1]!=mutation[(1,1)]:raise ValueError(('Control failed for an unexpected residual',exc.args))
 control={'gate':'order-two finite middle cocycle modulo relation','result':'rejected_as_required','residual_slot':'E0^2','residual_coefficient':'X^-1 Y^-1 W^2','mutation':'add1 to the actual origin finite01 primitive coefficient at geometric exponents(0,-1,-1,2), symmetric slot E0^2'}
else:raise ValueError('Sensitive negative control failed to reject')
receipt={'scope':'Actual order-two tensor and section realization with exp(-h A_eta-h² A_kappa), relative to our explicit completion and selected primitive gauge; no ancestor/carrier/defect identification.',
 'inputs':{'first_jet_sha256':n.PIN,'second_certificate_sha256':PIN},'coefficients':result,'checks':checks,'count':len(checks),'all_passed':True,'negative_control':control,'lambda_second_section_zero':True}
(HERE/'SECOND_NORMAL_COMPARISON_CHECKS.json').write_text(json.dumps(receipt,indent=2)+'\n')
(HERE/'SECOND_NORMAL_SECTION_CORRECTIONS.json').write_text(json.dumps(export,indent=2)+'\n')
print('ORDER TWO PASS',len(checks),flush=True)

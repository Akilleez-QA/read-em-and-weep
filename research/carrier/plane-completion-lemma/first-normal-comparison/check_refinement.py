#!/usr/bin/env python3
"""Verify the explicit common-refinement bridge to the earlier plane frames."""
import json
from pathlib import Path
import sympy as s
import check_first_normal_comparison as n

z,X,Y,W=s.symbols('z X Y W');S=X**2+Y**2;F=X*Y;a=X**3+Y**3;w=W**6
u=1/z;g=S-z*W**2;C=S**2+z*S*W**2+z**2*W**4;T=-3*S+2*F;D=C/z**2;k=-g/z
r0=s.Matrix([-a,w,-g,F]);ri=s.Matrix([-a,S**3,k,F])
TB=s.diag(z**3,1,z**4,z**3);TB[1,2]=z*C
kx=Y**2*(2*X**3+Y**3)/X**7;ky=X**2*(X**3+2*Y**3)/Y**7
TF=[[C*kx/w,C*ky/w,2*Y**2/w],[-z**3*kx/g,-z**3*ky/g,(2*Y**2-T*F/g)/w],[0,0,(2*Y**2+C/F)/w]]
TI=[[0,0,(2*u**2*Y**2-D*T*F/S**3)/w],[kx/k,ky/k,(2*u**2*Y**2+u**3*T*F/k)/w],[0,0,(2*u**2*Y**2+D/F)/w]]
checks=[]

def conv(p):return sum(s.Rational(c.numerator,c.denominator)*z**e[0]*X**e[1]*Y**e[2]*W**e[3] for e,c in p.items())
def zero(label,obj):
 vv=list(obj) if isinstance(obj,s.MatrixBase) else [obj]
 for v in vv:
  if s.cancel(v)!=0:raise ValueError((label,s.factor(s.cancel(v))))
 checks.append({'check':label,'entries':len(vv)})
def modrel(label,v,r):
 coeff=s.cancel(v[3]/F);zero(label,v-coeff*r)

def get(ws,i,j):return ws[(i,j)] if i<j else -ws[(j,i)] if i>j else s.zeros(4,1)
def fullform(r,lam):
 r1,r2,r3=list(r)[1:];o=s.zeros(5);o[1,2]=r3;o[1,3]=-r2;o[2,3]=r1;o[0,4]=1
 for j in range(3):o[j+1,4]=a*lam[j]
 return o-o.T

def fullmap(b):
 m=s.eye(5);m[:4,4]=b;return m

def oldplane(r,inf):
 r1,r2,r3=list(r)[1:]
 cs=[-T*F/(r1*r2),-1/(r2*r3),0] if inf else [T*F/(w*g),z**3/(g*F),C/(w*F)]
 return {(0,1):s.Matrix([cs[0],0,0,a/(r1*r2)]),(1,2):s.Matrix([cs[1],a/(r2*r3),0,0]),(0,2):s.Matrix([-cs[2],0,-a/(r3*r1),0])}

bridges=[]
for inf,r,lsp,wsp,ts in [(False,r0,n.LF,n.wF,TF),(True,ri,n.LI,n.wI,TI)]:
 tag='infinity' if inf else 'finite'
 ls=[s.Matrix([conv(p) for p in q]) for q in lsp];ws={ij:s.Matrix([conv(p) for p in q]) for ij,q in wsp.items()};os=oldplane(r,inf)
 oldls=[s.eye(3)[:,i]/r[i+1] for i in range(3)]
 bs={}
 for i in range(3):
  for j in range(3):
   b=a*oldls[i].cross(ls[j]);bs[(i,j)]=s.Matrix([ts[i][j],*list(b)])
   m=fullmap(bs[(i,j)])
   zero(tag+':refinement_form:'+str((i,j)),m.T*fullform(r,oldls[i])*m-fullform(r,ls[j]))
   zero(tag+':refinement_relation:'+str((i,j)),m*s.Matrix([*list(r),0])-s.Matrix([*list(r),0]))
   for q in range(4):zero(tag+':refinement_fixes_B:'+str((i,j,q)),m*s.eye(5)[:,q]-s.eye(5)[:,q])
 for i in range(3):
  for j,l in [(0,1),(0,2),(1,2)]:modrel(tag+':refinement_new_overlap:'+str((i,j,l)),bs[(i,j)]+get(ws,j,l)-bs[(i,l)],r)
 for j in range(3):
  for i,l in [(0,1),(0,2),(1,2)]:modrel(tag+':refinement_old_overlap:'+str((i,l,j)),bs[(i,j)]-get(os,i,l)-bs[(l,j)],r)
 bridges.append(bs)
# Compare with the actual previous base-overlap isometry, not only an abstract one.
kold=[s.Matrix([z*C*T*F/(w*S**3),0,0,-z*C*a/(w*S**3)]),s.zeros(4,1),s.zeros(4,1)]
knew=[s.Matrix([conv(p) for p in n.ks[i]]) for i in range(3)]
for i in range(3):
 for j in range(3):modrel('refinement_base_overlap:'+str((i,j)),kold[i]+TB*bridges[1][(i,j)]-z*bridges[0][(i,j)]-knew[j],r0)
receipt={'scope':'Exact common-refinement maps to the earlier completed plane quotient, no ancestor identification.','count':len(checks),'entries':sum(v['entries'] for v in checks),'checks':checks,'all_passed':True}
Path(__file__).with_name('REFINEMENT_CHECKS.json').write_text(json.dumps(receipt,indent=2)+'\n')
print('REFINEMENT PASS',receipt['count'],receipt['entries'],flush=True)

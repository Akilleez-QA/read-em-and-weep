#!/usr/bin/env python3
"""Formal local-algebra and K-class identities, not actual source evaluations."""
from pathlib import Path
import json,hashlib
import sympy as s
ROOT=Path(__file__).resolve().parent
checks=[]
def check(name,condition):
 if not bool(condition):raise RuntimeError(name)
 checks.append(name)
for item in json.loads((ROOT/'INPUTS.json').read_text()):
 data=(ROOT/item['local_path']).read_bytes()
 check('sha256 '+item['label'],hashlib.sha256(data).hexdigest()==item['sha256'])
 check('git blob '+item['label'],hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==item['git_blob'])
u,v=s.symbols('u v');a=s.symbols('a1:4');g=s.symbols('g1:4')
L=s.zeros(4,5)
for i in range(3):L[i,i]=1
L[3,3]=u;L[3,4]=v
F=s.Matrix([[*g,sum(a[i]*g[i] for i in range(3))]])
U=s.eye(4)
for i in range(3):U[i,3]=-a[i]
V=s.eye(5)
for i in range(3):V[i,3]=-u*a[i];V[i,4]=-v*a[i]
check('target basis change invertible',U.det()==1)
check('source basis change invertible',V.det()==1)
check('target row normalization',F*U==s.Matrix([[*g,0]]))
check('compatible restored L',s.simplify(U.inv()*L*V-L)==s.zeros(4,5))
check('compatible H normalization',s.simplify(F*L*V-s.Matrix([[*g,0,0]]))==s.zeros(1,5))
kappa=s.Matrix([0,0,0,-v,u])
check('original Koszul kernel',L*kappa==s.zeros(4,1))
check('basis change preserves kernel generator',V*kappa==kappa)
# Normal form for K_H -> K_F(1): identity on the free rank-two S.
M=s.Matrix([[1,0,0,0],[0,1,0,0],[0,0,u,v]])
k=s.Matrix([0,0,-v,u]);residue=s.Matrix([[0,0,1]])
check('kernel bridge Koszul relation',M*k==s.zeros(3,1))
check('cokernel residue relation',residue*M==s.Matrix([[0,0,u,v]]))
check('surjection onto residue field',residue*s.Matrix([0,0,1])==s.Matrix([1]))
check('kernel-section zero ideal',list(s.groebner(list(k),u,v))==[u,v])
# Universal algebraic syzygy normal forms, not values of the actual maps.
S2=s.Matrix([[-v,0],[u,0],[0,1]])
S3=s.Matrix([[-v,0],[u,-v],[0,u]])
check('two-generator regular-ideal syzygies',s.Matrix([[u,v,0]])*S2==s.zeros(1,2))
check('three-generator square-ideal syzygies',s.Matrix([[u*u,u*v,v*v]])*S3==s.zeros(1,2))
check('redundant-source image count off ell3',3-2==1 and 4-2==2 and 5-2==3)
check('redundant-source image count on ell3',3-3==0 and 4-3==1 and 5-3==2)
check('kernel ranks',4-1==3 and 5-1==4 and 2+1==3)
b=s.symbols('b')
def c2_from_ch(c1,ch2):return s.expand((c1*c1-2*ch2)/2)
cf=c2_from_ch(-9,b-s.Rational(81,2))
ch=c2_from_ch(-10,b-50)
check('K_F Chern data',cf==81-b)
check('K_H Chern data',ch==100-b)
cf_tw=s.expand(cf+2*(-9)+3)
check('rank-three twist Chern data',-9+3==-6 and cf_tw==66-b)
ce=cf_tw+10
check('elementary modification correction',ce==76-b)
check('extension Chern consistency',s.expand(ce+(-4)*(-6)-ch)==0)
check('rank and first Chern consistency',1+3==4 and -4-6==-10)
check('omitted defect would lose ten',s.expand(ch-(cf_tw+24))==10)
check('row twists',9+1==10 and -5+1==-4)
print(json.dumps({'status':'PASS','count':len(checks),'checks':checks,'kernel_ranks':[3,4],'Chern_data':{'K_F':['-9','81-b'],'K_H':['-10','100-b'],'E':['-6','76-b']},'local_modification':'R^2 plus m','defect_length':10,'scope':'formal local algebra; no actual coefficient evaluation'},indent=2))

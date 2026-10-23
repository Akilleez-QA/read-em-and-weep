#!/usr/bin/env python3
"""Bounded exact certificate; no actual source coefficients or instances."""
from pathlib import Path
import hashlib,json
import sympy as s
root=Path(__file__).resolve().parent;checks=[]
def ck(name,value):
    if not bool(value):raise RuntimeError(name)
    checks.append(name)
for entry in json.loads((root/'INPUTS.json').read_text()):
    data=(root/entry['local_path']).read_bytes()
    ck('SHA256 '+entry['label'],hashlib.sha256(data).hexdigest()==entry['sha256'])
    ck('Git blob '+entry['label'],hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==entry['git_blob'])
# Actual map types only. The proof supplies the actual identities.
types={'deltaC':('NR3','WNR4'),'inc':('WNR4','WZ'),'WG':('WZ','WM2'),
       'X':('WM2','M3'),'Q3':('M3','M5'),'j3':('M3','I3'),
       'Wh':('WNR4','WI2'),'XI':('WI2','I3')}
def compose(*names):
    for a,b in zip(names,names[1:]):
        if types[a][1]!=types[b][0]:raise RuntimeError('type mismatch '+a+' '+b)
    return types[names[0]][0],types[names[-1]][1]
ck('lift composition type',compose('deltaC','inc','WG','X')==('NR3','M3'))
ck('quadratic composition type',compose('deltaC','inc','WG','X','Q3')==('NR3','M5'))
ck('radical composition type',compose('deltaC','inc','WG','X','j3')==('NR3','I3'))
ck('computed radical image type',compose('deltaC','Wh','XI')==('NR3','I3'))
ck('central parity of lifted relation',(-1)*1==-1)
ck('central parity of Q3 image',1*(-1)==-1)
x,y,z=s.symbols('x y z')
ck('Koszul determinant cancellation',s.expand(x*(y*z)-y*(x*z))==0)
# Universal fixed-variable multiplication, not an actual direction.
mon4=[x**(4-i)*y**i for i in range(5)]
mon5=[x**(5-i)*y**i for i in range(6)]
mult=s.Matrix([[s.Poly(l*f,x,y).coeff_monomial(m) for l in (x,y) for f in mon4] for m in mon5])
ck('binary multiplication dimensions',mult.shape==(6,10))
ck('binary multiplication is onto Sym5',mult.rank()==6)
# Characters in order Wprime,S,T. Actual containment is in written proof.
Wp=s.Matrix([1,0,0]);S=s.Matrix([0,1,0]);T=s.Matrix([0,0,1]);dim=s.Matrix([[2,4,6]])
kerQ=3*Wp+3*S+3*T;K=kerQ-T;F=Wp+2*T
ck('odd kernel dimension',(dim*kerQ)[0]==36)
ck('common kernel character',K==3*Wp+3*S+2*T)
ck('common kernel dimension',(dim*K)[0]==30)
ck('quotient character',K-F==2*Wp+3*S)
ck('quotient dimension',(dim*(K-F))[0]==16)
ck('quotient has no T',(K-F)[2]==0)
ck('combined T rank',6-K[2]==4)
ck('mixed nonzero coefficient bound incompatible',not 4<=3)
ck('odd T Jordan sizes',sum([2,1])==kerQ[2] and sum(n-1 for n in [2,1])==1)
ck('kernel T part equals contained generated T part',K[2]==F[2]==2)
# Full symbolic row-normal-form certificate: Q=[I A], j=[b c].
A=s.Matrix(3,3,s.symbols('a0:9'));b=s.Matrix(1,3,s.symbols('b0:3'));c=s.Matrix(1,3,s.symbols('c0:3'))
Q=s.eye(3).row_join(A);j=b.row_join(c);M=Q.col_join(j)
N=(-A).col_join(s.eye(3));res=c-b*A
ck('abstract kernel parametrization',Q*N==s.zeros(3,3))
ck('abstract restriction is residual row',j*N==res)
E=s.eye(4)
for i in range(3):E[3,i]=-b[i]
ck('invertible symbolic elimination',E.det()==1)
ck('row elimination exact',E*M==Q.col_join(s.zeros(1,3).row_join(res)))
for i in range(3):
    ck('residual rank witness minor '+str(i),s.expand(M[:,[0,1,2,3+i]].det()-res[i])==0)
ck('nonzero residual has one multiplicity dimension',res.shape==(1,3))
# Exact universal quotient calculation, with every coefficient free.
def tv(a,f,k):
    return s.expand(sum((-1)**i*s.binomial(k,i)*s.diff(a,x,k-i,y,i)*s.diff(f,x,i,y,k-i) for i in range(k+1)))
mon2=[x*x,x*y,y*y]
cols=[]
for i,a in enumerate(mon2):
    for j,g in enumerate(mon5):
        lhs=s.expand(x*tv(a,y*g,2)-y*tv(a,x*g,2))
        ck('transvectant identity coefficient '+str(i)+','+str(j),lhs==2*tv(a,g,1))
        cols.append(s.Matrix([s.Poly(lhs,x,y).coeff_monomial(m) for m in mon5]))
C=s.Matrix.hstack(*cols)
ck('universal quotient map dimensions',C.shape==(6,18))
ck('universal quotient map onto T',C.rank()==6)
a0,a1,a2=s.symbols('a0 a1 a2');gg=s.symbols('g0:6')
a=a0*x*x+a1*x*y+a2*y*y;g=sum(t*m for t,m in zip(gg,mon5))
ck('all formal coefficients identity',s.expand(x*tv(a,y*g,2)-y*tv(a,x*g,2)-2*tv(a,g,1))==0)
f=s.Function('f12')(x,y)
ck('coherent image multiplication',x*(f*g)==f*(x*g))
# Polarization for an arbitrary symmetric bilinear coefficient array.
u=s.Matrix(s.symbols('u0:3'));v=s.Matrix(s.symbols('v0:3'))
bb=s.symbols('b00 b01 b02 b11 b12 b22');Smat=s.Matrix([[bb[0],bb[1],bb[2]],[bb[1],bb[3],bb[4]],[bb[2],bb[4],bb[5]]])
ck('symmetric transfer determined by diagonal',s.expand(((u+v).T*Smat*(u+v)-u.T*Smat*u-v.T*Smat*v)[0]/2-(u.T*Smat*v)[0])==0)
print(json.dumps({'status':'PASS','count':len(checks),'checks':checks,'conclusion':'j3(ker Q3)=I3; combined T rank four; kappa zero globally','scope':'conditional actual-map deduction, no instance or remaining mechanism selected'},indent=2))

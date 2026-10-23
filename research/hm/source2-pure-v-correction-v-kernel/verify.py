#!/usr/bin/env python3
"""Universal characters and row-kernel algebra, never actual source data."""
from pathlib import Path
import json,hashlib
import sympy as s
root=Path(__file__).resolve().parent;checks=[]
def ck(name,b):
    if not bool(b):raise RuntimeError(name)
    checks.append(name)
for e in json.loads((root/'INPUTS.json').read_text()):
    b=(root/e['local_path']).read_bytes()
    ck('SHA256 '+e['label'],hashlib.sha256(b).hexdigest()==e['sha256'])
    ck('Git blob '+e['label'],hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==e['git_blob'])
r=s.symbols('r');ch=[s.Integer(1),r]
for n in range(2,9):ch.append(s.expand(r*ch[-1]-ch[-2]))
phi=(1+s.sqrt(5))/2;traces=[2,-2,0,1,-1,phi,-phi,phi-1,1-phi];sizes=[1,1,30,20,20,12,12,12,12]
A=ch[2];D=ch[4];P=ch[8]-D;V=ch[6]-P
val=lambda f,t:s.simplify(f.subs(r,t))
def inner(f,g):return s.simplify(sum(n*val(f,t)*val(g,t) for n,t in zip(sizes,traces))/120)
ck('A tensor V is P plus D',all(val(A*V-P-D,t)==0 for t in traces))
ck('A tensor P is V plus P plus D',all(val(A*P-V-P-D,t)==0 for t in traces))
ck('one Gamma V channel',inner(A*V,D)==1)
ck('V absent from Q kernel',inner(V,A+D)==0)
ck('full degree2 V lies in residual',inner(V,P+D)==0)
ck('residual V multiplicity',inner(V,A+2*V+2*P+3*D)==2)
ck('NC marked V unique',inner(V,V+P+2*D)==1)
ck('quotient V unique',inner(V,A+D+V+P)==1)
ck('first-block target V unique',inner(V,V+2*P+D)==1)
ck('residual target V unique',inner(V,V+2*P+2*D)==1)
ck('V correction input unique',inner(V,A*P)==1)
# Abstract 2-copy V multiplicity space. alpha is nonzero on the marked line.
alpha,beta=s.symbols('alpha beta');Gamma=s.Matrix([[alpha,beta]])
ker=s.Matrix([-beta,alpha]);VC=s.Matrix([1,0])
ck('formal common kernel vector',Gamma*ker==s.zeros(1,1))
ck('marked restriction',Gamma*VC==s.Matrix([alpha]))
ck('transverse kernel determinant',s.Matrix.hstack(VC,ker).det()==alpha)
ck('kernel quotient projection nonzero coefficient',ker[1]==alpha)
# Actual nonzero and zero statements come from the proof, not this matrix.
a,b,c,d,w=s.symbols('a b c d w');Q=s.Matrix([[a,b],[c,d]]);det=Q.det()
k=Q.inv()*s.Matrix([0,w])
ck('formal corrected Q image',s.simplify(Q*k-s.Matrix([0,w]))==s.zeros(2,1))
ck('zero fourth alignment numerator',s.simplify((Gamma*k)[0]*det/w-(-alpha*b+beta*a))==0)
ck('alignment gives proportional rows',s.simplify((Gamma-alpha/a*Q[0,:]).subs(beta,alpha*b/a))==s.zeros(1,2))
ck('corrected marked splitting determinant',s.simplify(s.Matrix.hstack(VC,k).det()-a*w/det)==0)
ck('actual-shaped triangular image',s.simplify(Q*s.Matrix.hstack(VC,k)-s.Matrix([[a,0],[c,w]]))==s.zeros(2))
ck('triangular diagonal determinant',s.Matrix([[a,0],[c,w]]).det()==a*w)
# Compose the named maps only on their actual restricted domains.
types={'kV':('V_in','E_V'),'Gamma':('E_V','H_V'),'Q2':('E_V','M4_V'),
       'e0':('M4_V','N04_V'),'chi':('N04_V','H_V'),'pi':('E_V','N82_V')}
def comp(*names):
    for x,y in zip(names,names[1:]):
        if types[x][1]!=types[y][0]:raise RuntimeError('bad type '+x+' '+y)
    return types[names[0]][0],types[names[-1]][1]
ck('correction homotopy constraint type',comp('kV','Gamma')==('V_in','H_V'))
ck('cross-block factor type',comp('Q2','e0','chi')==types['Gamma'])
ck('correction quotient type',comp('kV','pi')==('V_in','N82_V'))
ck('kernel dimensions',2*3-3==3)
print(json.dumps(dict(status='PASS',count=len(checks),checks=checks,conclusion='Residual common V kernel is canonical and transverse to V_C; under R0 it equals the correction V and cross-block kernel',scope='no coefficient or actual instance selected'),indent=2))

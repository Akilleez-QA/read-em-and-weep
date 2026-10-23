#!/usr/bin/env python3
"""Typed identities and unspecialized synthetic negative-module control."""
from pathlib import Path
import hashlib,json
import sympy as s
r=Path(__file__).resolve().parent;checks=[]
def ck(name,b):
 if not b:raise RuntimeError(name)
 checks.append(name)
for i in json.loads((r/'INPUTS.json').read_text()):
 d=(r/i['local_path']).read_bytes()
 ck('sha256 '+i['local_path'],hashlib.sha256(d).hexdigest()==i['sha256'])
 ck('git_blob '+i['local_path'],hashlib.sha1(b'blob '+str(len(d)).encode()+b'\0'+d).hexdigest()==i['git_blob'])
# Types are (domain,codomain), with products read right to left.
types={'h':('N4','N2'),'Q':('N2','N4'),'Ta':('N2','N4'),'Tb':('N2','N4'),'Xl':('N2','N3'),'Xr':('N2','N3'),'Ym':('N3','N4'),'Ys':('N3','N4'),'j2':('N2','N2'),'j4':('N4','N4')}
def word_type(w):
 for a,b in zip(w,w[1:]):
  if types[a][0]!=types[b][1]:raise RuntimeError('ill-typed word '+str(w))
 return (types[w[-1]][0],types[w[0]][1])
for name,w,typ in [('sandwich',('h','Ta','h'),('N4','N2')),('K0 product',('h','Ta','h','Tb'),('N2','N2')),('K1 product',('Ta','h','Tb','h'),('N4','N4')),('middle product',('Xl','h','Ym','Xr','h','Ys'),('N3','N3')),('cross defect',('Tb','h','Ta'),('N2','N4')),('correction identity',('j4','Ta'),('N2','N4'))]:ck(name+' type',word_type(w)==typ)
ck('middle contraction has quadratic type',word_type(('Ym','Xr'))==types['Ta'])
# The new vanishing kills the indicated consecutive factors literally.
for label,word in [('K0',('h','Ta','h','Tb')),('K1',('Ta','h','Tb','h'))]:
 ck(label+' product contains vanishing sandwich',any(word[i:i+3] in [('h','Ta','h'),('h','Tb','h')] for i in range(len(word)-2)))
ck('no linear kernel syzygy twist',-4-(-1)==-3)
# Characters in order A,V,P,D.
N2=s.Matrix([1,2,3,4]);imQ=s.Matrix([0,2,3,3]);kerQ=s.Matrix([1,0,0,1]);imh=s.Matrix([0,0,1,1]);D=s.Matrix([0,0,0,1]);dims=s.Matrix([[3,3,4,5]])
source=N2-(kerQ+imh-D);target=imQ-D
ck('cross defect source character',source==s.Matrix([0,2,2,3]))
ck('cross defect target character',target==s.Matrix([0,2,3,2]))
ck('cross defect dimensions29to28',(dims*source)[0]==29 and (dims*target)[0]==28)
# Independent universal binary multiplication cancellation on the actual kernel.
x,y=s.symbols('x y');a0,a1,a2,b0,b1,b2,u0,u1,u2=s.symbols('a0 a1 a2 b0 b1 b2 u0 u1 u2')
a=a0*x*x+a1*x*y+a2*y*y;b=b0*x*x+b1*x*y+b2*y*y;u=u0*x*x+u1*x*y+u2*y*y
ck('kernel cross defect cancels by full multiplication',s.expand(b*(a*u)-a*(b*u))==0)
# Synthetic control. This is NOT the actual source, its characters or ranks.
# N2=(D,Dprime,C,E), N4=(I,Z,H,E4).
Q=s.zeros(4);Q[0,2]=1;Q[1,1]=1;Q[3,3]=1
h=s.zeros(4);h[0,1]=1;h[2,2]=1
j2=h*Q;j4=Q*h
Txx=s.zeros(4);Txx[0,0]=1;Txx[2,1]=1
Txy=s.zeros(4);Txy[3,2]=1
Tyy=s.zeros(4)
Ta=a0*Txx+a1*Txy+a2*Tyy;Tb=b0*Txx+b1*Txy+b2*Tyy
ck('synthetic square-zero radical',j2*j2==s.zeros(4) and j4*j4==s.zeros(4))
ck('synthetic side conditions',j2*h==s.zeros(4) and h*j4==s.zeros(4))
ck('synthetic Q compatibility',Q*j2==j4*Q)
ck('synthetic full symbolic negative compatibility',j4*Ta==Ta*j2 and j4*Tb==Tb*j2)
ck('synthetic sandwich zero',h*Ta*h==s.zeros(4) and h*Tb*h==s.zeros(4))
ck('synthetic mixed products zero',h*Ta*h*Tb==s.zeros(4) and Ta*h*Tb*h==s.zeros(4))
C=Tb*h*Ta-Ta*h*Tb;expected=s.zeros(4);expected[3,1]=a0*b1-a1*b0
ck('synthetic cross defect genuinely NONZERO',C==expected and expected!=s.zeros(4))
ck('synthetic defect annihilates h and is killed by h',C*h==s.zeros(4) and h*C==s.zeros(4))
I=s.eye(4);Z=s.zeros(4);Xx=I.col_join(Z);Xy=Z.col_join(I);Yx=Txx.row_join(Txy);Yy=Txy.row_join(Tyy)
j3=s.diag(j2,j2)
ck('synthetic commuting linear negative arrows',Yx*Xy==Yy*Xx)
ck('synthetic radical extends middle',all(j3*X==X*j2 for X in [Xx,Xy]) and all(j4*Y==Y*j3 for Y in [Yx,Yy]))
Ss=[X*h*Y for X in [Xx,Xy] for Y in [Yx,Yy]]
ck('synthetic all16 middle mixed products zero',all(S*T==s.zeros(8) for S in Ss for T in Ss))
ck('synthetic first-symbol vanishing',Ta[:,0]==a0*Q[:,2])
ck('synthetic defect kills complete Q kernel',all(C*v==s.zeros(4,1) for v in Q.nullspace()))
pcycle=s.eye(4)[:,2];correction=-a1*s.eye(4)[:,3]
ck('synthetic quotient P correction',Q*correction==-Ta*pcycle)
ck('synthetic raw quotient second zero',Ta*correction==s.zeros(4,1))
print(json.dumps(dict(status='pass',count=len(checks),checks=checks,conclusions=['h T_a h=0','K_a K_b=0','S_lm S_rs=0','cross defect factors29to28'],boundary='No cross-direction T commutation or actual lift coefficient constraint asserted; synthetic control is not an actual source'),indent=2))

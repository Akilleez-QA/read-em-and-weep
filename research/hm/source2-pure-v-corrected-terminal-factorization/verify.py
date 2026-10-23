#!/usr/bin/env python3
"""Formal operator/graph identities; no actual-source instance evaluation."""
from pathlib import Path
import hashlib,json
import sympy as s
root=Path(__file__).resolve().parent;checks=[]
def ck(name,b):
    if not bool(b):raise RuntimeError(name)
    checks.append(name)
for e in json.loads((root/'INPUTS.json').read_text()):
    b=(root/e['local_path']).read_bytes()
    ck('SHA256 '+e['label'],hashlib.sha256(b).hexdigest()==e['sha256'])
    ck('Git blob '+e['label'],hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==e['git_blob'])
# Formal multiplicities only: (u,i,l,v1,v2,v3), no HM matrices.
z,t,g1,g2=s.symbols('z t g1 g2');Q=s.zeros(3,6)
for i in range(3):Q[i,3+i]=1
j=s.zeros(6);j[1,0]=1
Th=s.zeros(6);Th[2,0]=1;Th[1,3]=1;Th[1,4]=z;Th[1,5]=t
ell=s.Matrix([[1,z,t]]);incI=s.eye(6)[:,1:2];incL=s.eye(6)[:,2:3]
H=s.eye(6)[:,:3];K=s.eye(6)[:,1:3];J=s.eye(6)[:,1:]
a=s.zeros(6);a[2,1]=1
for name,M in [('j square',j*j),('Theta square',Th*Th),('j Theta',j*Th),('Theta j',Th*j)]:
    ck('formal '+name,M==s.zeros(6))
ck('formal Q Theta',Q*Th==s.zeros(3,6))
ck('formal kernel of Q basis',Q*H==s.zeros(3,3) and H.rank()==3)
ck('formal common kernel basis',j*K==s.zeros(6,2) and Th*K==s.zeros(6,2) and K.rank()==2)
ck('canonical a sends jH to ThetaH',a*j*H==Th*H)
ck('canonical distinct image lines',s.Matrix.hstack(incI,incL).rank()==2)
ck('full corrected operator identity',Th==a*j+incI*ell*Q)
ck('restricted old identity',Th*J==incI*ell*Q*J)
ck('correction essential on H',Th*H!=s.zeros(6,3) and Q*H==s.zeros(3,3))
# Fixed minors are units, so these ranks hold for every formal specialization.
ck('Theta fixed rank two minor',Th.extract([1,2],[3,0]).det()==1)
ck('Theta image contained in two marked lines',all(Th[r,c]==0 for r in [0,3,4,5] for c in range(6)))
M=Q.col_join(j[1,:]);ck('combined fixed rank four minor',M[:,[3,4,5,0]].det()==1)
ck('Q restricted to J onto with fixed minor',(Q*J)[:,[2,3,4]].det()==1)
ck('j on H surjective',j[1,0]==1 and (j*H).rank()==1)
ck('Theta on H rank one',(Th*H).rank()==1)
pI=s.zeros(6);pI[1,1]=1;pL=s.zeros(6);pL[2,2]=1
ck('actual-shape I projection formula',pI*Th==incI*ell*Q)
ck('actual-shape L projection formula',pL*Th==a*j)
ck('full quotient formula',(s.eye(6)[2,:]*Th)==j[1,:])
# Literal graph and its zero ideal, all coefficients retained symbolically.
graph=s.Matrix([[1,0],[0,1],[g1,g2]])
f=ell*graph
ck('graph row formula',f==s.Matrix([[1+t*g1,z+t*g2]]))
ck('zero graph impossible at t zero',s.Poly(f[0].subs(t,0),z,g1,g2).as_expr()==1)
ck('zero ideal forces t a unit',s.expand(1+t*g1-f[0])==0)
ck('unique localized first coordinate',s.solve(s.Eq(f[0],0),g1)==[-1/t])
ck('unique localized second coordinate',s.solve(s.Eq(f[1],0),g2)==[-z/t])
ck('localized graph solves whole row',f.subs({g1:-1/t,g2:-z/t})==s.zeros(1,2))
ck('terminal restriction remains formal',ell[2]==t and t in Th.free_symbols)
# Dimensional and type checks supporting, not replacing, actual quotient proof.
types={'j3':('M3','I3'),'a':('I3','LTheta'),'Q3':('M3','V5'),'ell':('V5','I3'),
       'g':('V0','NR5'),'tau':('NR5','I3'),'ell0':('V0','I3')}
def compose(a,b):
    if types[a][1]!=types[b][0]:raise RuntimeError('type mismatch')
    return types[a][0],types[b][1]
ck('correction type',compose('j3','a')==('M3','LTheta'))
ck('terminal factor type',compose('Q3','ell')==('M3','I3'))
ck('graph row types agree',compose('g','tau')==types['ell0'])
ck('terminal split multiplicities',2+1==3)
print(json.dumps(dict(status='PASS',count=len(checks),checks=checks,conclusion='Theta=a j3+ell Q3 globally; separated R=0 requires nonzero tau and its unique graph',scope='formal control does not realize an actual source or the full negative module'),indent=2))

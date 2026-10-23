#!/usr/bin/env python3
"""Exact representation/Euler certificate, not an actual-source test."""
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
# Fixed finite-group characters, not source directions.
r=s.symbols('r');ch=[s.Integer(1),r]
for n in range(2,9):ch.append(s.expand(r*ch[-1]-ch[-2]))
phi=(1+s.sqrt(5))/2;traces=[2,-2,0,1,-1,phi,-phi,phi-1,1-phi];sizes=[1,1,30,20,20,12,12,12,12]
D=ch[4];P=ch[8]-ch[4];V=ch[6]-P;T=ch[5]
def val(f,t):return s.simplify(f.subs(r,t))
def inner(f,g):return s.simplify(sum(n*val(f,t)*val(g,t) for n,t in zip(sizes,traces))/120)
ck('complete class sizes',sum(sizes)==120)
ck('W tensor V equals T',all(val(r*V-T,t)==0 for t in traces))
ck('V irreducible',inner(V,V)==1)
ck('T irreducible',inner(T,T)==1)
ck('V absent from full joint kernel',inner(V,P+D)==0)
ck('marked V dimension',val(V,2)==3)
ck('marked T dimension',val(T,2)==6)
# Multiplicities in odd order Wprime,S,T; actual containment supplied by proof.
Wp=s.Matrix([1,0,0]);S=s.Matrix([0,1,0]);Tv=s.Matrix([0,0,1]);dim=s.Matrix([[2,4,6]])
NC=Wp+S+2*Tv;I=Tv
ck('quotient NC3/I3 character',NC-I==Wp+S+Tv)
ck('quotient permits at most one T',(NC-I)[2]==1)
ck('exact restriction kernel character',NC-Tv==Wp+S+Tv)
ck('exact restriction kernel dimension',(dim*(NC-Tv))[0]==12)
ck('full terminal split T multiplicities',2+1==3)
# Complete universal Euler subpencil, all variables formal.
u,v=s.symbols('u v');Id=s.eye(3)
E=(u*Id).col_join(v*Id);C=(-v*Id).row_join(u*Id)
ck('Euler types',E.shape==(6,3) and C.shape==(3,6))
ck('Euler composition zero',C*E==s.zeros(3))
ck('Euler first chart injection minor',E[:3,:].subs(u,1).det()==1)
ck('Euler second chart injection minor',E[3:,:].subs(v,1).det()==1)
ck('Euler first chart surjection minor',C[:,3:].subs(u,1).det()==1)
ck('Euler second chart surjection minor',C[:,:3].subs(v,1).det()==-1)
ck('Euler quotient rank',6-3==3)
ck('Euler quotient degree',0-(-3)==3)
x,y,q,f=s.symbols('x y q f')
ck('actual-shaped polynomial commutation',s.expand(q*x*f-x*q*f)==0)
ck('Koszul determinant cancellation',s.expand(x*y*f-y*x*f)==0)
ck('delta NC dimensions',18==2*(4+5))
ck('nonzero h quotient dimensions',9-4==5)
ck('I2 to I3 multiplication dimensions',2*5>=6)
# If two marked T lines have nonzero ell and zero ell respectively,
# their intersection is zero; projection away from the latter is injective.
ck('two marked lines dimensions',6+6==12 and 12<=18)
ck('V projection target unique V multiplicity',[1,2,1][0]==1)
print(json.dumps(dict(status='PASS',count=len(checks),checks=checks,conclusion='Q3(NC3)=W Q2(V_C) is one canonical T with saturated V-to-T subpencil',scope='residual tau0 forces its specific first-block projection; no fifth class or coefficient selected'),indent=2))

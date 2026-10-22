#!/usr/bin/env python3
"""Complete abstract representation identities and formal operator assembly.
No actual HM/source coefficient assignment, instance, matrix rank, or scan.
"""
import sympy as S
from functools import lru_cache
from collections import defaultdict
x,y,z,X,Y=S.symbols('x y z X Y')
q=x*z-y*y
lap=lambda P:S.diff(P,x,z)-S.diff(P,y,2)/4
@lru_cache(None)
def lift_mon(i,j):
    assert (i+j)%2==0
    m=(i+j)//2; parity=i%2
    P=x**((i-parity)//2)*y**parity*z**((j-parity)//2)
    ans=P; coeff=S.Integer(1); dd=P
    for r in range(1,m//2+1):
        dd=lap(dd)
        coeff=-coeff/(r*(S.Rational(2*m+1,2)-r))
        ans+=coeff*q**r*dd
    ans=S.expand(ans)
    assert S.expand(lap(ans))==0
    assert S.expand(ans.subs({x:X*X,y:X*Y,z:Y*Y})-X**i*Y**j)==0
    return ans

def lift(P):
    if P==0:return S.Integer(0)
    return S.expand(sum(c*lift_mon(i,j) for (i,j),c in S.Poly(P,X,Y).terms()))

def tau(P,R,r):
    return S.expand(sum((-1)**i*S.binomial(r,i)*S.diff(P,X,r-i,Y,i)*S.diff(R,X,i,Y,r-i) for i in range(r+1)))

def B1(P,R,m,n):
    if min(m,n)<1:return S.Integer(0)
    return tau(P,R,2)/(2*(2*m-1)*(2*n-1)*(2*m+2*n-1))

def B2(P,R,m,n):
    if min(m,n)<2:return S.Integer(0)
    return tau(P,R,4)/(8*(2*m-1)*(2*m-3)*(2*n-1)*(2*n-3)*(2*m+2*n-3)*(2*m+2*n-5))

count=0
pairs=[(m,n) for m in range(5) for n in range(5)]+[(2,5),(5,2)]
for m,n in pairs:
    for i in range(2*m+1):
        for j in range(2*n+1):
            P=X**i*Y**(2*m-i);R=X**j*Y**(2*n-j)
            defect=S.expand(lift(P)*lift(R)-lift(P*R)-q*lift(B1(P,R,m,n))-q*q*lift(B2(P,R,m,n)))
            assert S.reduced(defect,[q**3],x,y,z)[1]==0
            count+=1
assert count==735
# A genuine q³ term exists; the formula is not falsely claimed exact.
P=X**6;R=Y**6
remainder=S.expand(lift(P)*lift(R)-lift(P*R)-q*lift(B1(P,R,3,3))-q*q*lift(B2(P,R,3,3)))
assert remainder!=0
assert S.reduced(remainder,[q**3],x,y,z)[1]==0
print('PASS: all 735 complete abstract basis pairs modulo q³; nonzero next term retained.')

# All-degree coefficient proof, with formal m,n (no values assigned).
m,n=S.symbols('m n',integer=True,positive=True)
N=m+n
lap2factor=(2*N-3)*(2*N-5)/2
fall4m=(2*m)*(2*m-1)*(2*m-2)*(2*m-3)
fall4n=(2*n)*(2*n-1)*(2*n-2)*(2*n-3)
c2=1/(8*(2*m-1)*(2*m-3)*(2*n-1)*(2*n-3)*(2*N-3)*(2*N-5))
assert S.cancel(c2*fall4m*fall4n*lap2factor-m*(m-1)*n*(n-1))==0
print('PASS: all-degree Δ² and fourth-transvectant normalization identity.')

# Universal free-bilinear assembly: B_j(U,V) is an ORDERED matrix product tag.
# This checks every mixed term independently of any chosen matrix entries.
rho=S.symbols('rho')
def series(*items):return [{name:S.Integer(1)} if name else {} for name in items]
def star(U,V):
    out=[defaultdict(lambda:S.Integer(0)) for _ in range(3)]
    for a,ua in enumerate(U):
        for b,vb in enumerate(V):
            for j in range(3-a-b):
                for left,cl in ua.items():
                    for right,cr in vb.items():out[a+b+j][(j,left,right)]+=cl*cr
    return out

def combine(*terms):
    out=[defaultdict(lambda:S.Integer(0)) for _ in range(3)]
    for sign,T in terms:
        for a in range(3):
            for key,val in T[a].items():out[a][key]+=sign*val
    return out

def clean(d):return {key:S.expand(val) for key,val in d.items() if S.expand(val)!=0}
NN=series('n','t','s');AA=series('A','K','J');LL=series('lam','lam1','lam2')
DD=[{'Dn':S.Integer(1)},{'Dt':S.Integer(1),'t':rho},{'Ds':S.Integer(1),'s':2*rho}]
RR=combine((1,star(series('H',None,None),DD)),(1,star(AA,NN)),(-1,star(NN,AA)),(-1,star(LL,NN)))
expected={
 (0,'H','Ds'):1,(0,'H','s'):2*rho,(0,'lam','s'):-1,
 (0,'A','s'):1,(0,'s','A'):-1,(0,'K','t'):1,(0,'t','K'):-1,
 (0,'J','n'):1,(0,'n','J'):-1,(0,'lam1','t'):-1,(0,'lam2','n'):-1,
 (1,'H','Dt'):1,(1,'H','t'):rho,(1,'A','t'):1,(1,'t','A'):-1,
 (1,'K','n'):1,(1,'n','K'):-1,(1,'lam','t'):-1,(1,'lam1','n'):-1,
 (2,'H','Dn'):1,(2,'A','n'):1,(2,'n','A'):-1,(2,'lam','n'):-1}
assert clean(RR[2])==clean(expected)
print('PASS: exact second-normal operator coefficient, including all mixed B1 terms.')

EE=series(None,'R1','R2')
anticom=combine((1,star(NN,EE)),(1,star(EE,NN)))
expected_anti={(0,'n','R2'):1,(0,'R2','n'):1,(0,'t','R1'):1,(0,'R1','t'):1,
               (1,'n','R1'):1,(1,'R1','n'):1}
assert clean(anticom[2])==expected_anti
print('PASS: second-error tangency requires the retained first-error terms.')

# Equation-unit transport: t0=t/nu, s0=s/nu² and rho0=rho+Dnu/nu.
nu,dnu,tt,dtt,ss,dss=S.symbols('nu dnu tt dtt ss dss',nonzero=True)
rho0=rho+dnu/nu
assert S.cancel(dtt/nu-tt*dnu/nu**2+rho0*tt/nu-(dtt+rho*tt)/nu)==0
assert S.cancel(dss/nu**2-2*ss*dnu/nu**3+2*rho0*ss/nu**2-(dss+2*rho*ss)/nu**2)==0
print('PASS: physical equation-unit transport retains derivative/connection terms.')
# Generic regular-pair identity only: f,g,J remain independent symbols.
f,g,j11,j12,j21=S.symbols('f g j11 j12 j21')
Nmat=S.Matrix([[f*g,-f*f],[g*g,-f*g]])
Jmat=S.Matrix([[j11,j12],[j21,-j11]])
assert S.expand((Jmat*Nmat-Nmat*Jmat)[0,0]-j12*g*g-j21*f*f)==0
assert Nmat*Nmat==S.zeros(2)
print('PASS: universal regular-pair diagonal eliminates the new J term only.')
print('Universal local identities only: the actual midpoint has no extension to 3Q.')

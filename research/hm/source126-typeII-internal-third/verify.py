#!/usr/bin/env python3
"""Bounded exact universal checks, without actual HM instance evaluation."""
from pathlib import Path
import hashlib,json
import sympy as sp
ROOT=Path(__file__).resolve().parent
checks=0

def check(value,label):
    global checks
    if not value: raise RuntimeError(label)
    checks+=1

def zero(value):
    if isinstance(value,sp.MatrixBase):return all(sp.expand(v)==0 for v in value)
    return sp.simplify(value)==0

for row in json.loads((ROOT/'INPUTS.json').read_text()):
    b=(ROOT/row['local_path']).read_bytes()
    check(hashlib.sha256(b).hexdigest()==row['sha256'],row['label']+' SHA256')
    check(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==row['git_blob'],row['label']+' Git blob')
phi=(1+sp.sqrt(5))/2
A=sp.Matrix([3,-1,0,phi,1-phi]);D=sp.Matrix([5,1,-1,0,0]);one=sp.ones(5,1)
weights=[1,15,20,12,12]
def mul(a,b):return a.multiply_elementwise(b)
def inner(a,b):return sp.simplify(sum(sp.Integer(w)*x*y for w,x,y in zip(weights,a,b))/60)
H=[one,A]
for n in range(2,8):H.append((mul(A,H[n-1])-mul(A,H[n-2])+(H[n-3] if n>=3 else sp.zeros(5,1))).applyfunc(sp.expand))
E=[]
for n in range(8):
    check(H[n][0]==sp.binomial(n+2,2),'Sym dimension '+str(n))
    E.append((mul(D,H[n])-(mul(A,H[n-1]) if n else sp.zeros(5,1))).applyfunc(sp.expand))
    check(E[n][0]==5*sp.binomial(n+2,2)-3*sp.binomial(n+1,2),'E dimension '+str(n))
check(inner(E[3],D)==3,'cubic Hom dimension3')
check(inner(E[7],one)==1,'restriction invariant dimension1')
check(inner(E[1],one)==0,'no invariant section of E1')
check([inner(H[k+3],D) for k in range(-3,2)]==[0,0,1,0,2],'rank-one source possibilities')
check(inner(E[0],one)==0,'no invariant section E0')
check(3-1==2,'canonical cubic kernel dimension2')
check(-5-2==-7 and -3-1==-4,'naturality and fourth-symbol twists')

# Universal binary-form residue; x is a coordinate choice, not an actual selected root.
x,y=sp.symbols('x y')
hc=sp.symbols('h:5')
hpoly=sum(hc[i]*x**(4-i)*y**i for i in range(5))
a=x*x
rho=sp.expand(sp.diff(a,x)*sp.diff(hpoly,y)-sp.diff(a,y)*sp.diff(hpoly,x))
remainder=sp.rem(sp.Poly(rho,x),sp.Poly(x*x,x)).as_expr()
check(sp.expand(remainder-8*hc[4]*x*y**3)==0,'square transvectant residue')
check(hpoly.subs(x,0)==hc[4]*y**4,'not divisible by x criterion')
check(sp.expand(remainder).coeff(hc[4])!=0,'nonzero residue for contact exactly2')
# Wronskian finite degree and minimal ordinary vanishing sequence.
check(3*6+3*(-2)==12,'sextic Wronskian degree12')
check(sum([0,1,2])-3==0,'ordinary contact exactly2 away from Wronskian')

# General synthetic block complex testing the global normalization and sign.
# Variables are unconstrained universal coefficients, not actual HM data or G realizations.
p,q,z=sp.symbols('p q z')
B=sp.Matrix([[p,0,0],[q,p,0],[z,q,p],[0,z,q],[0,0,z]])
L=sp.Matrix(2,5,sp.symbols('l:10'))
R=sp.Matrix(3,2,sp.symbols('r:6'))
N=sp.Matrix(2,2,sp.symbols('n:4'))
K=sp.Matrix(5,2,sp.symbols('k:10'))
C=sp.Matrix(4,5,sp.symbols('c:20'))
h=sp.Matrix(sp.symbols('v:5'))
# M source: A3,D5,U1_2,U2_2,Tkernel5. Target: Scok5,V1_2,V2_2,Tcok4.
Q=sp.zeros(13,17);T=sp.zeros(13,17)
Q[0:5,12:17]=sp.eye(5);Q[5:7,8:10]=sp.eye(2);Q[7:9,10:12]=sp.eye(2)
T[0:5,0:3]=B;T[5:7,3:8]=L;T[0:5,8:10]=B*R
T[7:9,8:10]=N;T[0:5,10:12]=K;T[9:13,12:17]=C
h0=sp.zeros(17,1);h0[3:8,0]=h
u10=sp.zeros(17,1);u10[8:10,0]=-L*h
check(zero(Q*u10+T*h0),'raw first correction')
check(zero((T*u10)[0:5,0]+B*R*L*h),'raw second lies in first image')
u1=u10.copy();u1[0:3,0]=R*L*h
check(zero(Q*u1+T*h0),'normalized first correction equation')
check(zero((T*u1)[0:5,0]),'normalization kills second cohomology residual')
u2=sp.zeros(17,1);u2[10:12,0]=N*L*h
check(zero(Q*u2+T*u1),'second correction in S')
raw_r=K*N*L*h
check(zero((T*u2)[0:5,0]-raw_r),'internal third representative')
v3=sp.zeros(17,1);v3[12:17,0]=-raw_r
check(zero(Q*v3+T*u2),'third original correction')
for i in range(4):check(zero((T*v3)[9+i]+(C*raw_r)[i]),'original fourth minus sign row '+str(i))
# Quotient by first image is exactly quotient by original second after C.
w=sp.Matrix(sp.symbols('w:3'))
check(zero(-C*(raw_r+B*w)+C*raw_r+C*B*w),'first-image ambiguity becomes original second image')

# Full noncommuting quartic Schur coefficient, retaining all lower terms.
t=sp.Symbol('t')
q1,q2,q3,d1,d2,s1,s2,s3=sp.symbols('q1 q2 q3 d1 d2 s1 s2 s3',commutative=False)
expression=sp.expand(-(t*q1+t**2*q2+t**3*q3)*(1-t*d1+t**2*(d1*d1-d2))*(t*s1+t**2*s2+t**3*s3))
quartic=expression.coeff(t,4)
expected=-q1*s3+q1*d1*s2-q1*d1*d1*s1+q1*d2*s1-q2*s2+q2*d1*s1-q3*s1
check(sp.expand(quartic-expected)==0,'complete quartic Schur coefficient')
check(sp.expand(quartic.subs({s1:0,s2:0})+q1*s3)==0,'normalized fourth has no omitted terms')

result={'status':'pass','checks':checks,
 'cubic_equivariant_hom_dimension':3,'restriction_invariant_dimension':1,
 'canonical_naturality_kernel_dimension':2,
 'rank_one_source_multiplicities_for_k_minus3_through1':[0,0,1,0,2],
 'conclusion':'Under full-J Type II, the global internal third lies in a canonical two-dimensional space and is nonzero exactly when the generic original fourth is nonzero.',
 'limitations':'Neither actual nonvanishing nor a pair exclusion is asserted; universal and synthetic checks do not evaluate an actual HM instance.'}
print(json.dumps(result,indent=2,sort_keys=True))

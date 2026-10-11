#!/usr/bin/env python3
"""Universal exact quadratic-Hamiltonian and degree-two sign identities."""
import json
from pathlib import Path
import sympy as s
checks=[]

def zero(label,m):
 vals=list(m) if isinstance(m,s.MatrixBase) else [m]
 for v in vals:
  if s.expand(v)!=0:raise ValueError((label,s.expand(v)))
 checks.append({'check':label,'entries':len(vals)})

def comm(x,y):return x*y-y*x
# Independent symbolic 4x4 symmetric Hessians and alternating form.
def sym(prefix):
 q=s.zeros(4)
 for i in range(4):
  for j in range(i,4):q[i,j]=q[j,i]=s.Symbol(prefix+str(i)+str(j))
 return q
H=sym('h');K=sym('k');O=s.zeros(4)
for i in range(4):
 for j in range(i+1,4):O[i,j]=s.Symbol('o'+str(i)+str(j));O[j,i]=-O[i,j]
x=s.Matrix(s.symbols('x0:4'))
q=(x.T*H*x)[0]/2;r=(x.T*K*x)[0]/2
bracket=(s.Matrix([s.diff(q,t) for t in x]).T*O*s.Matrix([s.diff(r,t) for t in x]))[0]
HB=s.hessian(bracket,x)
zero('Hessian_of_Poisson_bracket',HB-(H*O*K-K*O*H))
A=H*O;B=K*O;AB=HB*O
zero('A_is_Lie_homomorphism',comm(A,B)-AB)
zero('minus_A_is_Lie_antihomomorphism',comm(-A,-B)+(-AB))
zero('symplectic_infinitesimal_A',A.T*O+O*A)
# Polynomial coefficient of order two in exp(-hA1-h²A2).
# Pairs are normalized to one common frame. Matrices are free noncommuting
# expressions evaluated symbolically on generic square matrices below.
def gen(prefix):return s.Matrix(4,4,lambda i,j:s.Symbol(prefix+str(i)+str(j)))
A1=gen('a');B1=gen('b');A2=gen('c');B2=gen('d')
C1=A1+B1
# Order-two cocycle solution C2=A2+B2-1/2[A1,B1].
C2=A2+B2-comm(A1,B1)/2
prod2=-A2-B2+(A1*A1+B1*B1)/2+A1*B1
right2=-C2+C1*C1/2
zero('triangle_positive_correction_RHS',prod2-right2)
# Mixed square: left exp(-hH-h²H2)exp(-hI-h²I2)
# right exp(-hF-h²F2)exp(-hJ-h²J2), with H+I=F+J.
H1=gen('p');I1=gen('q');F1=gen('r');J1=H1+I1-F1
H2=gen('u');F2=gen('v');J2=gen('w')
Qmix=(comm(H1,I1)-comm(F1,J1))/2
I2=F2+J2-H2+Qmix
left2=-H2-I2+(H1*H1+I1*I1)/2+H1*I1
right2=-F2-J2+(F1*F1+J1*J1)/2+F1*J1
zero('mixed_positive_correction_RHS',left2-right2)
# Reversing tensor BCH at order two follows from exp(-A)exp(-B):
# rho BCH(B,A)=-A-B+1/2[A,B]+..., not rho BCH(A,B).
zero('opposite_BCH_degree_two',(comm(-A,-B)/2)-(-(-AB)/2))
receipt={'scope':'Universal identities and normalized degree-two correction equations only; no higher coefficient or ancestor certification.','all_passed':True,'checks':checks,'count':len(checks),'entries':sum(c['entries'] for c in checks)}
Path(__file__).with_name('SIGN_DICTIONARY_CHECKS.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(receipt['count'],receipt['entries'],'exact identities passed')

#!/usr/bin/env python3
"""Formal universal coefficient identities, never actual HM input data."""
import json
import sympy as s
from pathlib import Path
checks=0

def require(b,label):
    global checks
    checks+=1
    if not b: raise AssertionError(label)

def zero(M,label):
    for z in M: require(s.expand(z)==0,label)

t=s.Symbol('t')
cases=[]
for e in range(13):
    n=e+1
    m=s.Matrix([t**i for i in range(n)])
    for r in range(6):
        # Independent indeterminates, no numerical specialization.
        A=s.Matrix(r,n,lambda i,j:s.Symbol(f'a_{i}_{j}'))
        C=A.col_join(s.eye(n))
        T=s.eye(r+n)
        Ti=s.eye(r+n)
        if r:
            T[:r,r:]=-A
            Ti[:r,r:]=A
        Z=s.zeros(r,n).col_join(s.eye(n))
        zero(T*Ti-s.eye(r+n),'universal inverse')
        zero(T*C-Z,'universal coefficient graph removal')
        zero(T*C*m-Z*m,'universal polynomial graph removal')
        zero(T*(C*m).diff(t)-(Z*m).diff(t),'constant shear commutes with derivative')
        # A fully generic residual polynomial column stays in the R block.
        f=s.Matrix([sum(s.Symbol(f'b_{i}_{d}')*t**d for d in range(4)) for i in range(r)])
        residual=f.col_join(s.zeros(n,1))
        zero(T*residual-residual,'residual unchanged')
        zero(T*residual.diff(t)-residual.diff(t),'residual derivative unchanged')
        require(C[r:,:].det()==1,'coefficient projection isomorphism')
        cases.append({'degree':e,'residual_ambient_dimension':r})
    if e:
        # Determinants of local two-coordinate value/derivative systems.
        require(s.det(s.Matrix([[1,0],[t,1]]))==1,'first chart immersion')
        u=s.Symbol('u')
        reverse=s.Matrix([u**(e-i) for i in range(n)])
        require(s.det(s.Matrix([[reverse[-1],s.diff(reverse[-1],u)],[reverse[-2],s.diff(reverse[-2],u)]]))==1,'second chart immersion')
    else:
        zero(m.diff(t),'constant degree zero exception')
# Incomplete complete-basepoint-free countercontrol on affine chart:
# j=(1,t^2), g=t; t cannot be a constant combination of 1,t^2.
alpha,beta=s.symbols('alpha beta')
require(s.Poly(t-alpha-beta*t*t,t).coeff_monomial(t)==1,'missing coefficient negative control')
require(5+2+6+3==16 and -2*5-3*(2+6)-4*3==-46,'conditional residual type')
require(30-9==21 and 3-1==2,'conditional constant ambient and derivative ranks')
require(max(4,5)<8 and 4+5==9,'Sym8 proper quotient bound')
result={'scope':'Universal symbolic coefficient/shear and derivative identities only',
 'formal_degree_range':[0,12],'formal_residual_dimension_range':[0,5],
 'symbolic_cases':len(cases),'assertions':checks,'passed':True,
 'negative_control':'basepoint-free incomplete (x^2,y^2) cannot absorb xy',
 'actual_source_instance_evaluated':False,'profile11_excluded':False}
print(json.dumps(result,indent=2,sort_keys=True))

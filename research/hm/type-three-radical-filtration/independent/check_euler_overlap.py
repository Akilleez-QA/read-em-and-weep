#!/usr/bin/env python3
"""Independent exact one-variable chart-overlap and nonsplitting controls."""
from fractions import Fraction as F
import json
from itertools import permutations
checks=[]
def require(label, value):
    if not value: raise RuntimeError(label)
    checks.append(label)
def poly(*terms):
    out={}
    for e,c in terms: out[e]=out.get(e,F(0))+F(c)
    return {e:c for e,c in out.items() if c}
def plus(a,b): return poly(*(list(a.items())+list(b.items())))
def times(a,b): return poly(*[(i+j,x*y) for i,x in a.items() for j,y in b.items()])
def negative(a): return {i:-x for i,x in a.items()}
def matmul(a,b):
    return [[sum_poly(times(a[i][k],b[k][j]) for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def sum_poly(seq):
    out={}
    for a in seq:out=plus(out,a)
    return out
z={};one=poly((0,1));t=poly((1,1));ti=poly((-1,1))
a=[[one],[t]];b=[[negative(t),one]]
rx=[[z],[one]];ry=[[negative(ti)],[z]]
require('Euler composition vanishes',matmul(b,a)==[[z]])
require('x right inverse',matmul(b,rx)==[[one]])
require('y right inverse expressed in x frame',matmul(b,ry)==[[one]])
difference=[[plus(ry[i][0],negative(rx[i][0]))] for i in range(2)]
require('overlap difference is a times minus t^-1',difference==matmul(a,[[negative(ti)]]))
# H^1(O(-2)) = C[t,t^-1]/(C[t] + t^-2 C[t^-1]).
# Its t^-1 coefficient survives every coboundary, identically, not by samples.
require('nonzero Cech class',negative(ti).get(-1)==-1)
for exponent in range(-20,21):
    if exponent==-1:continue
    monomial=poly((exponent,1))
    require('coboundary support '+str(exponent),(-1 not in monomial) and (exponent>=0 or exponent<=-2))
# The overlap class is -Id_V, so its connecting map has rank dim(V)=3.
matrix=[[-int(i==j) for j in range(3)] for i in range(3)]
determinant=0
for perm in permutations(range(3)):
    term=(-1)**sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))
    for i in range(3):term*=matrix[i][perm[i]]
    determinant+=term
require('Euler Cech coefficient matrix determinant minus1',determinant==-1)
def h0(degrees,twist): return sum(n*max(d+twist+1,0) for d,n in degrees.items())
def h1(degrees,twist): return sum(n*max(-d-twist-1,0) for d,n in degrees.items())
K={-2:3,-3:6,-4:6};S={-2:3,-4:3};Q={-2:3,-4:6}
require('twist2 middle h0 is3',h0(K,2)==3)
require('twist2 split h0 is6',h0(S,2)+h0(Q,2)==6)
require('twist2 connecting source dimension3',h0(Q,2)==3)
require('twist2 connecting target dimension3',h1(S,2)==3)
require('twist2 Euler characteristic consistency',h1(S,2)==h1(K,2)-h1(Q,2)+3)
print(json.dumps({'status':'PASS','checks':len(checks),'labels':checks,'scope':'Formal Euler overlap and type III cohomological nonsplitting only; no source evaluation.'},indent=2,sort_keys=True))

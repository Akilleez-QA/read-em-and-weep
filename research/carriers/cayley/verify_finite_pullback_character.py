"""Exact exterior-algebra check of the unequal-degree normalization.

This checks the Chern-character annihilator and the 10+6 source decomposition.
It does NOT compute End-valued Atiyah evaluations or prove source Delta != 0.
Those are supplied by the geometric proof and the Cayley source calculation.
"""
from fractions import Fraction as Q
from itertools import combinations
import sympy as s

def add(a,b,k=1):
    r=a.copy()
    for w,v in b.items():
        r[w]=r.get(w,0)+k*v
        if not r[w]: del r[w]
    return r

def wedge(a,b):
    r={}
    for u,x in a.items():
        for v,y in b.items():
            if set(u)&set(v): continue
            sign=(-1)**sum(i>j for i in u for j in v)
            w=tuple(sorted(u+v)); r[w]=r.get(w,0)+sign*x*y
    return {w:v for w,v in r.items() if v}

def con(a,i):
    return {w[:w.index(i)]+w[w.index(i)+1:]:v*(-1)**w.index(i)
            for w,v in a.items() if i in w}

def biv(a,i,j): return con(con(a,i),j)
def kap(a,i,j): return wedge({(4+j,):1},con(a,i))
def scale(a,k): return {w:k*v for w,v in a.items() if k*v}

# Holomorphic forms are e0..e3; antiholomorphic forms are e4..e7.
# lambda_i=m_i e_i f_i, theta=(sum lambda_i)/2.
degrees=(2,3,5,7)
theta={(i,4+i):Q(degrees[i],2) for i in range(4)}
t2=wedge(theta,theta); t4=wedge(t2,t2)
d=3
ch=add(add({():2},t2,-d),t4,Q(d*d,12))
labels=[]; cols=[]
pairs=list(combinations(range(4),2))
for i,j in pairs:
    labels.append(('b',i,j)); cols.append(wedge({(4+i,4+j):1},ch))
for i in range(4):
    for j in range(4):
        labels.append(('kappa',i,j)); cols.append(kap(ch,i,j))
for i,j in pairs:
    labels.append(('beta',i,j)); cols.append(biv(ch,i,j))
words=[w for n in range(9) for w in combinations(range(8),n)]
M=s.Matrix([[c.get(w,0) for c in cols] for w in words])
assert M.rank()==12 and len(M.nullspace())==16
known=[]
for i,j in pairs:
    pi=scale(biv(t2,i,j),Q(1,2))
    v=s.zeros(28,1); v[labels.index(('beta',i,j))]=1
    for (a,b),n in pi.items(): v[labels.index(('b',a-4,b-4))]=d*n
    known.append(v)
for i in range(4):
    v=s.zeros(28,1); v[labels.index(('kappa',i,i))]=degrees[i]
    known.append(v)
K=s.Matrix.hstack(*known)
assert K.rank()==10 and M*K==s.zeros(256,10)
for i,j in pairs:
    v=s.zeros(28,1)
    v[labels.index(('kappa',i,j))]=Q(degrees[j],2)
    v[labels.index(('kappa',j,i))]=Q(degrees[i],2)
    known.append(v)
all_directions=s.Matrix.hstack(*known)
assert all_directions.rank()==16 and M*all_directions==s.zeros(256,16)
print('PASS: degrees (2,3,5,7), theta=(sum lambda_i)/2, centered c2=3 theta^2')
print('Chern-character action rank 12; annihilator dimension 16')
print('6 compensated Poisson +4 diagonal directions: independent dimension 10')
print('6 half-normalized, degree-weighted mixed directions complete the annihilator')
print('No actual Ext evaluation or source Delta vanishing computed by this script.')

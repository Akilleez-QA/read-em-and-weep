#!/usr/bin/env python3
"""Universal coherent-quotient Chern accounting, not an actual HM rank test."""
def product(a,b):
    return (a[0]+b[0],a[1]+b[1]+a[0]*b[0])
def quotient(total,sub):
    c1=total[0]-sub[0]
    return (c1,total[1]-sub[1]-sub[0]*c1)
A=(-6,21)  # S7*
C=(-4,10)  # S5*
E4=(-10,55)
K8=(24,300)
assert product(A,C)==E4
Q6=quotient(K8,A)
assert Q6==(30,459)
assert product(A,Q6)==K8
assert (K8[0]**2-2*K8[1])-(A[0]**2-2*A[1])==Q6[0]**2-2*Q6[1]==-18
print('PASS: exact root-Euler Chern sequence; coherent Q6 has rank6,c1=30,c2=459.')
print('No actual map or rank evaluated; Q6 is not assumed locally free or torsion-free.')

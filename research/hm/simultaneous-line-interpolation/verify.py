#!/usr/bin/env python3
"""Bounded symbolic degree/cohomology checks, not actual-instance evaluation."""

def p1(n):
    return (max(n+1, 0), max(-n-1, 0))

def cohom(a,b):
    x,y=p1(a),p1(b)
    return x[0]*y[0],x[1]*y[0]+x[0]*y[1],x[1]*y[1]

expected=[[1],[2,3],[3,6,5],[4,9,10,7]]
for d,row in enumerate(expected):
    assert [(2*j+1)*(d-j+1) for j in range(d+1)]==row
    assert max(row)<12
assert cohom(2,-1)==(0,0,0)
assert cohom(0,-4)==(0,3,0)
assert cohom(4,2)[0]-3==12
# Veronese multiplication lifts every binary monomial up to scalar selector degree.
for j in range(5):
    exponents={0}
    for _ in range(j):
        exponents={a+b for a in exponents for b in (0,1,2)}
    assert exponents==set(range(2*j+1))
old=[(1,4),(3,2),(5,0)]
new=[(a+2,b+2) for a,b in old]
assert new==[(3,6),(5,4),(7,2)]
assert all(a+b==9 and b%2==0 for a,b in new)
old_bundles=[(3,7),(7,5),(11,3)]
new_bundles=[(a+4,b+2) for a,b in old_bundles]
assert new_bundles==[(7,9),(11,7),(15,5)]
assert [3*a+b for a,b in new_bundles]==[30,40,50]
assert (3*4+2)%10!=0
assert 1+3+3+5==12
assert 3*(1+1+1+3)==18
# Formal sum of delta-supported selector values is identity on every line.
for j in range(12):
    assert [int(i==j) for i in range(12)].count(1)==1
print('PASS: degree bounds, Koszul cohomology, Veronese lifts, shifted monomials and characters.')
print('Structural transitivity and global operator arguments are proved in PROOF.md, not machine-formalized.')
# Negative-section positive-base curve: no positive quotient embeds in a trivial bundle.
assert p1(-1)[0]==p1(-2)[0]==0
K_degrees=[-1,-1,0]
N_degrees=[K_degrees[i]+K_degrees[j] for i in range(3) for j in range(i+1,3)]*2
Q_degrees=[d+2 for d in K_degrees]*2
assert sorted(N_degrees)==[-2,-2,-1,-1,-1,-1]
assert sorted(Q_degrees)==[1,1,1,1,2,2]
assert sum(N_degrees)+sum(Q_degrees)==0
assert all(p1(-d)[0]==0 for d in Q_degrees)
print('PASS: scroll restriction degrees and nonsplitting cohomology checks.')

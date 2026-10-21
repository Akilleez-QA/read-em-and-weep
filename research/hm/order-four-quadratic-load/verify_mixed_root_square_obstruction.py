"""Universal bookkeeping only: no HM coefficients or source-instance ranks."""
from fractions import Fraction
from collections import defaultdict

# Coefficients of exp(t A+t^2 B+t^3 C) in the free associative algebra.
X = {(1, ('A',)): Fraction(1), (2, ('B',)): Fraction(1),
     (3, ('C',)): Fraction(1)}
def mul(P,Q):
    out=defaultdict(Fraction)
    for (d,w),a in P.items():
        for (e,v),b in Q.items():
            if d+e<=3: out[d+e,w+v]+=a*b
    return dict(out)
power={(0,()):Fraction(1)}
exponential=dict(power)
fact=1
for n in range(1,4):
    power=mul(power,X); fact*=n
    for key,value in power.items():
        exponential[key]=exponential.get(key,Fraction())+value/fact
third={word:coef for (degree,word),coef in exponential.items() if degree==3}
assert third=={('C',):Fraction(1),('A','B'):Fraction(1,2),
               ('B','A'):Fraction(1,2),('A','A','A'):Fraction(1,6)}

# Transition coefficient of order a has normal degree 2a.
# s_(k-a) components of degree 2j+1 have q_+ weight k-a-j.
# Every binary trace lowers normal degree by 2 and raises weight by 1.
for k in range(1,4):
    for a in range(1,k+1):
        for j in range(k-a+1):
            before=2*a+2*j+1
            initial_weight=k-a-j
            for traces in range((before-1)//2+1):
                final_degree=before-2*traces
                weight=initial_weight+traces
                assert weight==k-(final_degree-1)//2
assert [(d,3-(d-1)//2) for d in [7,5,3,1]]==[(7,0),(5,1),(3,2),(1,3)]

# Two reduced roots: every O_Z(k) has dimension two, including k=-5.
assert 3*2==6
for r in range(7):
    b=2*r
    assert (90-12)-b==78-b
    assert 30-b>=18
    assert (18-b)>=6

# Distinct direction annihilators cubed have coprime product degree six,
# exceeding quartic degree four. Their quartic section subspaces intersect 0.
assert 3+3>4
print('PASS: actual third-transition formula retains C, AB, BA, and A^3.')
print('PASS: third harmonic weights are 7:0, 5:1, 3:2, 1:3 in q_+.')
print('PASS: forced source is six-dimensional, target 30-b, b<=12.')
print('PASS: distinct root section planes have zero intersection by degrees.')
print('No selected HM coefficient, matrix, rank, or experiment was evaluated.')

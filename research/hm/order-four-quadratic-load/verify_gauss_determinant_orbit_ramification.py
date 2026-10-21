#!/usr/bin/env python3
"""Universal orbit-degree arithmetic for saturated Gauss flags.

No actual coefficients, matrices, map ranks, or local models are evaluated.
Finite enumeration is only of bounded hypothetical integer degree profiles.
Geometric inclusion, saturation, and projection arguments are in the proof.
"""
import sympy as s


def zero(expr):
    assert s.simplify(s.expand(expr)) == 0, expr


def in_semigroup(n, generators):
    if n < 0:
        return False
    values = {0}
    for t in range(n+1):
        if t in values:
            values.update(t+g for g in generators if t+g <= n)
    return n in values


def weights(k,l):
    return [l*j if j<k else k*(k+l-j) for j in range(1,k+l)]


# Projective stabilizers: cyclic orders 1,2,3,5, hence orbit sizes 60,30,20,12.
assert [60//h for h in (1,2,3,5)] == [60,30,20,12]
assert 15*2 == 30
assert 20*2//2 == 20
assert 24*2//4 == 12
assert in_semigroup(60, (12,20,30))

# Orbit-only refinement of the frozen plateau.
old_allowed, fully_unramified = [], []
for K in range(1,9):
    for L in range(1,7):
        C=20*K+10*L-K*L*(K+L-3)
        if C < 0:
            continue
        assert in_semigroup(C,(K,L))
        old_allowed.append((K,L))
        if all(not in_semigroup(C-6*w,(K,L)) for w in weights(K,L)):
            fully_unramified.append((K,L))
assert fully_unramified == [(3,6),(4,5),(5,4),(7,3)]
assert 23-18 == 5 and not in_semigroup(5,(3,7))

# Strong endpoint bounds a<=-pm, b<=-qm.
k,l,eta=s.symbols('k l eta',integer=True)
m=k+l
p,q=17-2*k,13-2*l
zero(l*p+k*q+2*k*l-(17*l+13*k-2*k*l))
strong=(54*m-l*(p*m+eta)-k*(q*m+eta)-2*k*l*m)/2
zero(strong-m*(54-(17*l+13*k-2*k*l)-eta)/2)
alpha,beta,R=s.symbols('alpha beta R',integer=True)
a,b=-p*m-eta-2*alpha,-q*m-eta-2*beta
zero((54*m+l*a+k*b-2*k*l*m-2*R)/2-(strong-l*alpha-k*beta-R))

five=[]
strong_values={}
for K in range(1,9):
    for L in range(1,7):
        base=17*L+13*K-2*K*L
        if base<=54:
            five.append((K,L))
            M=K+L
            numerator=M*(54-base-(M%2))
            assert numerator%2==0
            strong_values[K,L]=numerator//2
assert five == [(1,1),(1,2),(2,1),(2,2),(3,1)]
assert strong_values == {(1,1):26,(1,2):15,(2,1):21,(2,2):4,(3,1):8}

# (2,2): all plateau divisors vanish; degree parity fixes alpha=beta=1.
C=strong_values[2,2]
assert all(6*w>C for w in weights(2,2))
choices=[(aa,2-aa) for aa in range(3) if (aa-3)%2==0]
assert choices == [(1,1)]
assert 13*4 <= 54 < 13*5
assert 17*(54-13*4)==34 < 12*4
assert not in_semigroup(34,(12*13,20*13,30*13,12*4,20*4,30*4))

# (3,1): only epsilon_1=0 or 6 can occur in the plateau.
assert weights(3,1)==[1,2,3]
assert [n for n in range(9) if in_semigroup(n,(6,10,15))] == [0,6]
assert 11*4 <= 44 <= 48 < 11*5  # Both relevant constant spans have dimension 15.
endpoint_generators=(12*11,20*11,30*11,12*4,20*4,30*4)
assert 15*(46-44)==30 and not in_semigroup(30,endpoint_generators)
assert 15*(48-44)==60 and not in_semigroup(60,endpoint_generators)
# Upper degree 46/48 excluded, hence beta=0.  epsilon_1=6 would give
# lower degree 48 and the same impossible endpoint weight 60.
remaining=[(aa,ee) for aa in range(9) for ee in (0,6) if aa+ee==8]
assert remaining==[(2,6),(8,0)]
remaining=[pair for pair in remaining if pair[0]!=2]
assert remaining==[(8,0)]
assert 11*(15-11)==44
assert 12*(15-12)==36
# Saturated projection of E has rank 3 and degree -36 or smaller.
assert 17-3==14
kernel_degree_lower_bound=-54-(-36)
kernel_degree_upper_bound=-2*14
assert kernel_degree_lower_bound==-18 > kernel_degree_upper_bound==-28

remaining_profiles=[p for p in five if p not in [(2,2),(3,1)]]
assert remaining_profiles==[(1,1),(1,2),(2,1)]
print('PASS: projective orbit degrees 12,20,30,60 and half-degree semigroup <6,10,15>.')
print('PASS: exact orbit-only unramified profiles:',fully_unramified)
print('PASS: stronger endpoint identity leaves five hypothetical profiles.')
print('PASS: (2,2) violates the minimum rank-one invariant-ramification weight.')
print('PASS: (3,1) reduces to the stated unramified endpoint and projection contradiction.')
print('REMAINING necessary rank-two profiles:',remaining_profiles)
print('NOT PROVED: exclusion or realization of the remaining profiles, or actual SF rank >=3.')

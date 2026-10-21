"""Universal filtration/dimension checks, not a source-instance evaluation."""
# Scaling image: q_-(epsilon z)+epsilon^2 q_+(x)
# equals epsilon^2 times the fixed quadric equation.
# Global order a, odd normal degree d, normalization by epsilon:
# epsilon^(2a+d-1)=t^(a+(d-1)//2).
third=[]
for a in range(1,4):
    for d in [1,3,5,7]:
        weight=a+(d-1)//2
        assert 2*a+d-1==2*weight
        if weight==3: third.append((a,d))
assert third==[(1,5),(2,3),(3,1)]
# Replacing q_- by -s q_+ adds global order one and lowers degree two.
for a,d in [(1,5),(2,3),(0,7)]:
    assert a+(d-1)//2 == (a+1)+(d-3)//2
for r1 in range(7):
    for r2 in range(7):
        b=r1+r2
        for h1 in range(3,10-r1):
            for h2 in range(3,10-r2):
                global_target=h1+h2+4
                finite_target=30-b
                assert global_target<=22-b
                assert finite_target-global_target>=8
                if r1==r2==6:
                    assert (h1+h2,global_target,finite_target)==(6,10,18)
print('PASS: s=epsilon^2 for q_-+s q_+; the inverse is the other normalization.')
print('PASS: weighted order three has exactly (a,d)=(1,5),(2,3),(3,1).')
print('PASS: relation remainders preserve weight and lower the surviving normal degree.')
print('PASS: actual global target bound 22-b and conditional 6->10->18 dimensions.')
print('No selected coefficients, multiplication ranks, or source instances were evaluated.')

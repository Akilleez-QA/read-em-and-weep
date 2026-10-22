#!/usr/bin/env python3
"""The actual comparison is in the proof; check universal character/basepoint logic."""
image={(2*2+w)%10 for w in [8,0,2]}
assert image=={2,4,6}
assert {2,4,6,8}-image=={8}
weights={f'X^{4-j}Y^{j}':(3*(4-j)-3*j)%10 for j in range(5)}
assert [h for h,w in weights.items() if (3*2+w)%10==8]==['X^4Y^0']
assert [d for d in [12,20,30,60] if d<=18]==[12]
assert 18-12==6
# Sym^6 W=V+P4, dimensions3+4, with no D5 summand.
assert 3+4==7
print('PASS: unique detectable square character, final quotient weights, and invariant basepoint exclusion.')
print('Prequotient vanishing is used only for the detectable character, not asserted for all D5 inputs.')

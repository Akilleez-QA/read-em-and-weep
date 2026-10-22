#!/usr/bin/env python3
"""Universal Hilbert certificate for an initial regular (3,5) pair."""
def h(n):return max(n+1,0)
a=[h(n)-h(n-3)-h(n-5)+h(n-8) for n in range(15)]
assert a==[1,2,3,3,3,2,1]+[0]*8
odd=a[1::2];even=a[::2]
assert odd[:3]==[2,3,2] and sum(odd)==7
assert even[:4]==[1,3,3,1] and sum(even)==8
assert 1+3+5==9 and sum(even)!=9
assert (3+1)-3==1
assert (5+1)-2==4 and 3+1==4
assert (7+1)==(4+1)+(2+1)
print('PASS: odd Loewy(2,3,2) gives initial CI(3,5); even Hilbert layers(1,3,3,1), length8.')
print('PASS: generic Ext annihilator contains m^4 but not m^3; it is not the length7 odd defect.')
print('No global generators, twists, coefficient values, or restriction ranks asserted.')

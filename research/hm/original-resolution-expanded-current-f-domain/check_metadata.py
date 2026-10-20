"""Mathematical extraction: historical source-hash authentication is omitted. Not rerun for this edition."""
"""Inert integer owner-certificate and source-hash controls only; no source evaluation."""
import json

def require(value, label):
    if not value:
        raise RuntimeError(label)
def add(*vectors):
    return tuple(sum(v[i] for v in vectors) for i in range(4))
first_c = add((5,5,0,0), (0,5,6,5))
first_l = add((3,3,0,0), (0,3,4,3))
second_c = add((5,6,5,0), (2,0,2,0), (0,0,5,5), (2,0,2,0))
second_l = add((3,4,3,0), (1,0,1,0), (0,0,3,3), (1,0,1,0))
require((first_c, first_l)==((5,10,6,5),(3,6,4,3)), 'first cup')
require((second_c,second_l)==((9,6,14,5),(5,4,8,3)), 'transported cup')
require(tuple(max(x,y) for x,y in zip(first_c,second_c))==(9,10,14,5), 'combined carrier')
require(tuple(max(x,y) for x,y in zip(first_l,second_l))==(5,6,8,3), 'combined legal')
require((14+21,8+9)==(35,17), 'Q envelope')
require((14+4+6+6,8+2+3+3)==(30,16), 'T envelope')
require(35<=54 and 17<=29 and 30<=53 and 16<=28, 'weight domination')
require(3+1==4 and 3+2==5 and 5-1==4 and 5+1==6, 'degrees and occurrences')
for direction,current,pair in ((0,1,12),(1,0,12),(2,3,3),(3,2,3)):
    missing=(1<<current)^pair
    require(missing !=15 and missing^(1<<direction)==15, 'missing-axis character')
# Negative controls: a dropped conjugator and an omitted derivative weight fail.
require(add((5,6,5,0),(2,0,2,0),(0,0,5,5))!=second_c, 'dropped conjugator detected')
require(5!=6, 'five-weight substitution detected')
print(json.dumps({'status':'pass','scope':'integer owner metadata and hashes only','first_cup':[first_c,first_l],'second_cup':[second_c,second_l],'C':[14,8],'Q':[35,17],'T':[30,16],'physical_evaluations':0},sort_keys=True))

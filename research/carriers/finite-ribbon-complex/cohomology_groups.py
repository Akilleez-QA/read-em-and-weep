#!/usr/bin/env python3
"""Exact E1 line-bundle cohomology inventories; no survival claim."""
from collections import Counter,defaultdict
from math import comb
from model import build

def h_line(a,b):
    if a>=0: qa,ha=0,a+1
    elif a<=-2: qa,ha=1,-a-1
    else:return None
    if b>=0: qb,hb=0,comb(b+3,3)
    elif b<=-4: qb,hb=3,comb(-b-1,3)
    else:return None
    return qa+qb,ha*hb

def inventory(twist):
    terms=build()['terms_F']; out=defaultdict(Counter)
    for i,srcs in terms.items():
        for j,dsts in terms.items():
            for sa,sb in srcs:
                for da,db in dsts:
                    ab=(da-sa+twist[0],db-sb+twist[1]); h=h_line(*ab)
                    if h:out[j-i][(h[0],ab)]+=1
    return dict(out)

def table(twist):
    inv=inventory(twist); dims=defaultdict(int)
    for p,groups in inv.items():
        for (q,ab),n in groups.items():dims[p,q]+=n*h_line(*ab)[1]
    return dict(dims)

if __name__=='__main__':
    for tw in [(-2,-1),(0,0),(-2,0),(-2,-2)]:
        print('\nEnd(F)'+str(tw))
        print('q\\p',*[str(p).rjust(7) for p in range(-3,4)])
        tb=table(tw)
        for q in [4,3,1,0]:print(q,*[str(tb.get((p,q),0)).rjust(7) for p in range(-3,4)])
        print('Nonzero summands (p,q,bidegree,multiplicity,dimension):')
        for p,groups in sorted(inventory(tw).items()):
            for (q,ab),n in sorted(groups.items()):print(p,q,ab,n,n*h_line(*ab)[1])

#!/usr/bin/env python3
"""Independent integer McKay-graph replay; only abstract representations."""
from itertools import combinations_with_replacement
from pathlib import Path
import re
def require(condition):
    if not condition: raise RuntimeError("independent replay check failed")
names=('1','W','Wp','A','V','P','S','D','T')
dims=(1,2,2,3,3,4,4,5,6)
parity=(0,1,1,0,0,0,1,0,1)
# Tensoring by the defining W is the affine E8 adjacency operator.
edges=(('1','W'),('W','A'),('A','S'),('S','D'),('D','T'),('T','V'),('T','P'),('P','Wp'))
adj={n:[] for n in names}
for a,b in edges: adj[a].append(b);adj[b].append(a)
def times_w(v): return tuple(sum(v[names.index(k)] for k in adj[n]) for n in names)
def sym_times(i):
    old=(0,)*9
    cur=tuple(int(j==i) for j in range(9));out=[cur]
    for d in range(1,27):
        nxt=tuple(a-b for a,b in zip(times_w(cur),old))
        require(min(nxt)>=0)
        require(sum(x*y for x,y in zip(nxt,dims))==dims[i]*(d+1))
        out.append(nxt);old,cur=cur,nxt
    return out
products=[sym_times(i) for i in range(9)]
H=(1,0,0,3,1,2,0,2,0)
E=(0,2,1,0,0,0,2,0,2)
atoms=[(i,d) for i,r in enumerate(dims) if r<=5 for d in range(27//r+1) if d*r<=26 and d%2==parity[i]]
solutions=[];numerical_candidates=0
# Enumerate rank partitions first, then degree partitions, with no character pruning.
for length in range(1,6):
 for inds in combinations_with_replacement(range(len(atoms)),length):
    if sum(dims[atoms[k][0]] for k in inds)!=5: continue
    if sum(dims[atoms[k][0]]*atoms[k][1] for k in inds)!=26: continue
    numerical_candidates+=1
    h=tuple(sum(products[atoms[k][0]][atoms[k][1]][j] for k in inds) for j in range(9))
    e=tuple(sum(products[atoms[k][0]][atoms[k][1]-1][j] for k in inds if atoms[k][1]) for j in range(9))
    if h==H and e==E: solutions.append(tuple(sorted((names[atoms[k][0]],atoms[k][1]) for k in inds)))
proof=Path(__file__).with_name('PROOF.md').read_text()
expected=[];stars=[]
for row,body in re.findall(r'^\s*(\d+)\. (.+)$',proof,re.M):
 if ' + ' not in body: continue
 star='*' in body;body=body.replace('*','').strip()
 if not re.fullmatch(r"[\d+ W'AVP\[\]]+",body):continue
 parts=[]
 for term in body.split(' + '):
    m=re.fullmatch(r"([A-Z]'?)\[(\d+)\]",term)
    parts.append((m[1].replace("W'",'Wp'),int(m[2])) if m else ('1',int(term)))
 expected.append(tuple(sorted(parts)))
 if star:stars.append(int(row))
require(len(expected)==21 and len(set(expected))==21)
require(set(solutions)==set(expected) and len(solutions)==21)
ext=lambda sol:sum(products[0][d-12][names.index(n)] for n,d in sol if d>=12)
require([i+1 for i,s in enumerate(expected) if ext(s)]==stars==[8,9,11,16,21])
require(all(ext(s) in (0,1) for s in solutions))
require([products[0][d][0] for d in range(0,15,2)]==[1,0,0,0,0,0,1,0])
require(products[0][7]==(0,0,1,0,0,0,0,0,1))
print('PASS independent McKay/rank-degree enumeration:',len(atoms),'unpruned atoms;',numerical_candidates,'rank-degree candidates;',len(solutions),'types; starred rows',stars)

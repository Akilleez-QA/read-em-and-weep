#!/usr/bin/env python3
"""Synthetic exact regressions; no geometric instance data."""
from contextlib import redirect_stdout
from fractions import Fraction
from itertools import permutations
from pathlib import Path
import io
import json
import runpy

with redirect_stdout(io.StringIO()):
    module=runpy.run_path(str(Path(__file__).with_name('check_euler_overlap.py')))
det=module['exact_determinant']
checks=0
def require(value,label):
    global checks
    if not value: raise RuntimeError(label)
    checks+=1

def elimination(matrix):
    """Independent exact row elimination, not a permutation expansion."""
    a=[list(map(Fraction,row)) for row in matrix]
    n=len(a); result=Fraction(1)
    for j in range(n):
        pivot=next((i for i in range(j,n) if a[i][j]),None)
        if pivot is None: return Fraction(0)
        if pivot!=j:
            a[j],a[pivot]=a[pivot],a[j];result=-result
        p=a[j][j];result*=p
        for i in range(j+1,n):
            q=a[i][j]/p
            for k in range(j,n):a[i][k]-=q*a[j][k]
    return result

# A literal recurrence of the published defect, used only as a negative control.
def old_six(matrix):
    total=0
    for perm in permutations(range(6)):
        term=(-1)**sum(perm[i]>perm[j] for i in range(6) for j in range(i+1,3))
        for i in range(6):term*=matrix[i][perm[i]]
        total+=term
    return total

mutation_mismatches=0
for perm in permutations(range(6)):
    matrix=[[int(perm[i]==j) for j in range(6)] for i in range(6)]
    expected=elimination(matrix)
    require(det(matrix)==expected,'permutation '+str(perm))
    mutation_mismatches+=old_six(matrix)!=expected
require(mutation_mismatches>0,'old implementation must be rejected')
swap=[[int((4 if i==3 else 3 if i==4 else i)==j) for j in range(6)] for i in range(6)]
require(det(swap)==-1 and old_six(swap)==1,'last-block transposition witness')
minus_identity=[[-int(i==j) for j in range(6)] for i in range(6)]
require(det(minus_identity)==old_six(minus_identity)==1,'original input unchanged')
for n in range(7):
    cases=[[[int(i==j)*(i+1) for j in range(n)] for i in range(n)],
           [[i+2*j+1 for j in range(n)] for i in range(n)],
           [[Fraction((i+1)**j, i+j+1) for j in range(n)] for i in range(n)]]
    for k,a in enumerate(cases):require(det(a)==elimination(a),f'exact case {n}/{k}')
for bad in [[[1,2]],[[1],[2]]]:
    try:det(bad)
    except ValueError:checks+=1
    else:raise RuntimeError('nonsquare accepted')
print(json.dumps({'status':'PASS','checks':checks,'permutation_matrices':720,
                  'old_implementation_mismatches':mutation_mismatches,
                  'original_minus_identity_determinant':1,
                  'scope':'Synthetic exact determinant regressions only; no geometric instance data.'},indent=2,sort_keys=True))

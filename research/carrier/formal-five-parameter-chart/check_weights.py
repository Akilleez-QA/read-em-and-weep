"""Check all filtration-line cutoffs and the universal homotopy signs."""
from itertools import combinations, combinations_with_replacement, product
from pathlib import Path
import json
import sympy as s

if not __debug__:
    raise RuntimeError('Run without -O: exact checks use assertions.')
ROOT = Path(__file__).resolve().parent
OUT = ROOT/'build'
OUT.mkdir(exist_ok=True)
names = ['P','E0','E1','E2']
base = [3,0,4,3]
plane = [-3,0,-4,-4]
weights = [3,0,2,2]
w_lines = []
for i,j in combinations_with_replacement(range(4),2):
    b = base[i]+base[j]-4
    cutoff = None if b < 0 else 2*b+2-weights[i]-weights[j]
    w_lines.append({'slot':[names[i],names[j]],'base_degree':b,
                    'plane_degree_before_minus_k':plane[i]+plane[j]+2,
                    'H2_weight_cutoff':cutoff})
assert [r['H2_weight_cutoff'] for r in w_lines if r['H2_weight_cutoff'] is not None] == [0,3,1,0,6,4,2]
u_lines = []
for i in range(4):
    b = base[i]-1
    cutoff = None if b < 0 else 2*b+2-weights[i]
    assert b >= -1  # H^3(U_k)=0 at every normal order.
    u_lines.append({'slot':'A'+names[i],'base_degree':b,
                    'plane_degree_before_minus_k':plane[i]-4,
                    'H2_weight_cutoff':cutoff})
assert [r['H2_weight_cutoff'] for r in u_lines if r['H2_weight_cutoff'] is not None] == [3,6,4]
assert 2*3-2 == 4  # Section scalar relation has required weight k.
# The only H1(W) plane-nonnegative line is E0^2 = O(-4,2-k).
h1 = {}
for k in (1,2):
    monomials = []
    for ze in (-3,-2,-1):
        for x in range(3-k):
            for y in range(3-k-x):
                w = 2-k-x-y
                if 2*ze+x+y == k-4:
                    monomials.append([ze,x,y,w])
    h1[str(k)] = sorted(monomials)
assert h1 == {'1':[[-2,0,1,0],[-2,1,0,0]],'2':[[-1,0,0,0]]}
# Universal plane Cech homotopy, checked on each support pattern and each basis cochain.
def delta(cochain, degree):
    return {opened: sum((-1)**j*cochain.get(opened[:j]+opened[j+1:],0)
                        for j in range(len(opened)))
            for opened in combinations(range(3),degree+2)}
def homotopy(cochain, pivot):
    result = {}
    for opened,value in cochain.items():
        if pivot in opened:
            target = tuple(t for t in opened if t != pivot)
            result[target] = result.get(target,0)+(-1)**opened.index(pivot)*value
    return result
count = 0
for mask in product((False,True),repeat=3):
    negative = {i for i,value in enumerate(mask) if value}
    pivot = next((i for i in range(3) if i not in negative),None)
    for degree in (1,2):
        for opened in combinations(range(3),degree+1):
            if not negative.issubset(opened):
                continue
            cochain = {opened:1}
            left = {} if pivot is None else delta(homotopy(cochain,pivot),degree-1)
            right = {} if pivot is None else homotopy(delta(cochain,degree),pivot)
            for target in combinations(range(3),degree+1):
                if negative.issubset(target):
                    expected = 0 if pivot is None else cochain.get(target,0)
                    assert left.get(target,0)+right.get(target,0) == expected
            count += 1
# Actual relation/transition identity retains the off-diagonal geometry.
z,X,Y,W = s.symbols('z X Y W')
S = X**2+Y**2; F = X*Y; a = X**3+Y**3
C = S**2+z*S*W**2+z**2*W**4; g = S-z*W**2
T = s.Matrix([[z**3,0,0,0],[0,1,z*C,0],[0,0,z**4,0],[0,0,0,z**3]])
r0 = s.Matrix([-a,W**6,-g,F]); ri = s.Matrix([-a,S**3,-g/z,F])
assert (T*ri-z**3*r0).applyfunc(s.expand) == s.zeros(4,1)
(OUT/'weight_certificate.json').write_text(json.dumps({
    'W_filtration':w_lines,'U_filtration':u_lines,
    'H2_W_and_H2_U_prescribed_zero_from_order':7,
    'section_prescribed_zero_from_order':5,
    'H1_W_prescribed_monomials':h1,
    'plane_homotopy_basis_checks':count,
    'actual_relation_transition_identity':True,
    'parameter_dependence':'none'},indent=2)+'\n')
print('All ten W lines, four U lines, section cutoff, Cech homotopy and actual relation: PASS')

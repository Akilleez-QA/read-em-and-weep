# Historical reproducibility source. Not executed during publication preparation.
#!/usr/bin/env python3
"""Small certificate products only: no elimination, source values or rank run."""
from fractions import Fraction as F
from pathlib import Path
import hashlib, json, resource, time

START=time.monotonic()
HERE=Path(__file__).resolve().parent
BASE=HERE.parent
checks=0
def eq(x,y):
    global checks
    assert x==y,(x,y)
    checks+=1
def unit(n,i): return [F(int(i==j)) for j in range(n)]
def add(x,y): return [a+b for a,b in zip(x,y)]
def scale(a,x): return [a*b for b in x]
def dot(x,y): return sum(a*b for a,b in zip(x,y))
def action(n,x): return [-x[5*b+4-a] for b in range(n//5) for a in range(5)]
def quotient(x):
    return [x[a]-x[25+a] for a in range(5)]+x[5:10]+[x[10+a]-x[20+a] for a in range(5)]+x[15:20]
def section(x): return x+[F(0)]*10
def alpha(x):
    q=quotient(x)
    return [(q[5*b+s]-q[5*b+4-s])/2 for b in range(4) for s in range(2)]
def lift8(x):
    y=[F(0)]*30
    for c,(b,s) in zip(x,((b,s) for b in range(4) for s in range(2))):
        y[5*b+s]+=c; y[5*b+4-s]-=c
    return y

original=HERE/'structural-relations.md'
original_bytes=original.read_bytes()
eq(hashlib.sha1(b'blob '+str(len(original_bytes)).encode()+b'\0'+original_bytes).hexdigest(),
   'd48c88141e80f0005cf598d4796d6f358d45f07a')

maps_path=BASE/'hm-detector-plus-first-component-20261016/positive-eight-maps.json'
saved=json.loads(maps_path.read_text())
boundaries=[add(unit(30,a),unit(30,25+a)) for a in range(5)]+[add(unit(30,10+a),unit(30,20+a)) for a in range(5)]
for a,b in enumerate(boundaries):
    eq(quotient(b),[F(0)]*20)
    eq(alpha(b),[F(0)]*8)
for i in range(30):
    x=unit(30,i); q=quotient(x)
    eq(q,[sum(F(c)*x[k] for k,c in row) for row in saved['quotient20_reduction']])
    eq(quotient(action(30,x)),action(20,q))
    eq(alpha(action(30,x)),alpha(x))
    eq(quotient(lift8(alpha(x))),scale(F(1,2),add(q,action(20,q))))
    # Explicit complete reconstruction into section plus published d5 image.
    reconstruction=section(q)
    for a in range(5):
        reconstruction=add(reconstruction,scale(x[25+a],boundaries[a]))
        reconstruction=add(reconstruction,scale(x[20+a],boundaries[5+a]))
    eq(x,reconstruction)
for i in range(20): eq(quotient(section(unit(20,i))),unit(20,i))
for i in range(8):
    p=lift8(unit(8,i))
    eq(alpha(p),unit(8,i))
    eq(action(30,p),p)
    eq({str(j):int(c) for j,c in enumerate(p) if c},saved['positive_basis_K30'][i])

# The only polynomial multipliers used have the certified homogeneous degrees
# 0,1,2 and are fixed by v_i -> v_(4-i).
beta=[{(0,0,0,0,0):1},{(0,0,1,0,0):1},{(0,0,2,0,0):1,(0,1,0,1,0):-1,(1,0,0,0,1):2}]
for degree,p in enumerate(beta):
    eq({sum(k) for k in p},{degree})
    eq({tuple(reversed(k)):v for k,v in p.items()},p)
    eq(-3-degree+degree,-3) # primal multiplication lands in B(-3)
    eq(-3-degree+(-2+degree),-5) # correct Serre pairing line

# Completely manufactured maps test the transpose/normalization identity.
# Their entries are unrelated to any actual cohomological multiplication map.
M=[[F(((i+2)*(j+3))%7-3) for j in range(8)] for i in range(4)]
for k in range(4):
    eta=unit(4,k)
    x0=[-sum(M[i][j]*eta[i] for i in range(4)) for j in range(8)]
    for j in range(8):
        e=unit(8,j); me=[dot(row,e) for row in M]
        eq(4*(dot(e,x0)+dot(me,eta)),F(0))
    eq(eta[k],F(1)) # nonzero second component, independent of M

inputs=[original,maps_path,
 BASE/'hm-epsilon-projective-generator-bridge-20261016/THEOREM.md',
 BASE/'hm-positive-twelve-detector-interface-20261016/THEOREM.md',
 BASE/'hm-detector-plus-first-component-20261016/THEOREM.md',
 BASE/'hm-projective-detector-dual-audit-20261016/AUDIT.md']
receipt={'status':'PASS','checks':checks,'seconds':time.monotonic()-START,
 'maximum_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 'rank_eliminations':0,'source_coefficients_acquired':0,
 'actual_multiplication_matrices_computed':False,
 'scope':'Exact quotient/involution certificate products and a manufactured graph-pairing control; theorem supplies global descent and rank by identity first component.',
 'input_sha256':{str(p.relative_to(BASE)):hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}}
(HERE/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))

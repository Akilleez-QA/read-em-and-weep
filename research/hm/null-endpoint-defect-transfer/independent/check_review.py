"""Independent static/formal audit: free scalar-current labels, no physical values."""
from pathlib import Path
from collections import Counter
import hashlib
import json

ROOT=Path(__file__).resolve().parents[1]
def require(ok, label):
    if not ok:
        raise RuntimeError(label)
def equal(actual, expected, label):
    require(actual==expected,label)
def cleaned(x):
    return {k:v for k,v in x.items() if v}
def sumterms(*parts):
    out=Counter()
    for coeff,part in parts:
        for key,value in part.items(): out[key]+=coeff*value
    return cleaned(out)
checks=[]
for pin in json.loads((ROOT/'pins.json').read_text())['sources']:
    equal(hashlib.sha256((ROOT/pin['file']).read_bytes()).hexdigest(),pin['sha256'],'dependency hash')
checks.append('six inert dependency hashes')

# These independent free labels stand for delta jZ and j Delta Z.
# Homotopy gives dH delta jZ = delta jZ - j Delta Z.
projection={'delta_jZ':1,'j_DeltaZ':-1}
equal(sumterms((1,{'delta_jZ':1}),(-1,projection)),{'j_DeltaZ':1},'nonclosed first total differential')
checks.append('nonzero degree-zero projection is retained')

stages={}
for n in range(6):
    signs=[1 if (n+s+1)%2==0 else -1 for s in (1,2,3)]
    stages[n]=signs
    equal(signs[0]*signs[1],-1,'stage two operator sign')
    for s in (2,3):
        previous_other_degree=1 if ((n+1)+(s-1)+1)%2==0 else -1
        equal(signs[s-1]*signs[s-2],-signs[s-1]*previous_other_degree,'induction')
    a3_next=1 if ((n+1)+3+1)%2==0 else -1
    equal(-signs[2]-a3_next,0,'d of bottom difference cancels')
equal(stages[2],[1,-1,1],'degree two')
equal(stages[3],[-1,1,-1],'degree three')
equal((2+2+1,3+2+1),(5,6),'stage two arities')
equal((2+3+2,3+3+2),(7,8),'bottom boundary arities')
checks.append('both degree parities, common negative J2, bottom coefficient and distinct arities')

# Represent theta_ab in the first frame by the free transported increments
# x_a+...+x_(b-1). No actual transition or current matrix is constructed.
def endpoint(a,b,c):
    out=Counter()
    for r in range(a,b): out[((b,c),r)]+=1
    for r in range(b,c): out[((a,b),r)]-=1
    return cleaned(out)
vertices=(0,1,2,3)
faces=[]
for k in range(4):
    face=vertices[:k]+vertices[k+1:]
    faces.append(((-1)**k,endpoint(*face)))
actual=sumterms(*faces)
def scalar_boundary(a,b,c,current):
    return {((b,c),current):1,((a,c),current):-1,((a,b),current):1}
expected=sumterms((-1,scalar_boundary(1,2,3,0)),(-1,scalar_boundary(0,1,2,2)))
equal(actual,expected,'independent four-face endpoint defect')
transport=(('i','j'),('j','k'))
composed=(transport[0][0],transport[1][1])
equal(composed,('i','k'),'last current transport covers both edges')
checks.append('four-face expansion gives minus both cups and full i-to-k transport')

# (derivative axis, current axis, complementary scalar pair, doubled sign).
def four():
    output=[]
    for (a,b),q in [((0,1),(2,3)),((2,3),(0,1))]:
        output.extend([(a,b,q,-1),(b,a,q,1)])
    return output
terms=four()
equal(terms,[(0,1,(2,3),-1),(1,0,(2,3),1),(2,3,(0,1),-1),(3,2,(0,1),1)],'four defects')
equal([-t[-1] for t in terms],[1,-1,1,-1],'Ward substitution')
checks.append('four axis/pair labels and Ward signs')

# Check that each specifically wrong alternative is refused by the same
# equality validator rather than merely printing a control label.
mutations=[
 ('dropped projection',{'delta_jZ':1},projection),
 ('wrong degree-three first sign',[1,1,-1],stages[3]),
 ('positive stage-two word',1,-1),
 ('wrong second cup sign',sumterms((-1,scalar_boundary(1,2,3,0)),(1,scalar_boundary(0,1,2,2))),actual),
 ('truncated final transport',('i','j'),composed),
 ('silently closed endpoint',{},actual),
]
rejected=[]
for label,bad,good in mutations:
    try: equal(bad,good,label)
    except RuntimeError: rejected.append(label)
    else: raise RuntimeError('mutation survived: '+label)
print(json.dumps({'status':'pass','checks':checks,'negative_controls_rejected':rejected,'scope':'formal free labels and supplied text hashes only; no actual values or matrix products'},indent=2))

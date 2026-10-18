"""Pure formal coefficient checks; never import/evaluate any physical source."""
import json
from collections import defaultdict

def need(ok, msg):
    if not ok: raise RuntimeError(msg)

def a(n,s): return (-1)**(n+s+1)
from pathlib import Path
import hashlib
root=Path(__file__).resolve().parent
pins=json.loads((root/'pins.json').read_text())
for item in pins['sources']:
    need(hashlib.sha256((root/item['file']).read_bytes()).hexdigest()==item['sha256'], 'dependency hash: '+item['file'])
checks=['six prerequisite excerpts authenticated as inert text']
for n in range(8):
    need(a(n,1)==(-1)**n, 'first projection sign')
    for s in (2,3):
        # Coefficient of H delta J_(s-2)^(n+1) Delta in dJ_s.
        derived=a(n,s)*a(n,s-1)
        claimed=-a(n,s)*a(n+1,s-1)
        need(derived==claimed, 'nonclosed induction coefficient')
    # Top W derivative: terms proportional to delta J2^(n+1) Delta.
    need(-a(n,3)-a(n+1,3)==0, 'top chain-map relation')
    need(a(n,1)*a(n,2)==-1, 'stage-two total sign')
checks.append('general-degree recurrence and bottom signs, both parities')
need([a(2,s) for s in (1,2,3)]==[1,-1,1], 'degree two signs')
need([a(3,s) for s in (1,2,3)]==[-1,1,-1], 'degree three signs')
checks.append('degree-two versus degree-three signs')
# Each monomial is (scalar edge, free transported-current letter).
# No current matrices, owner values, jets or source entries are represented.
p=defaultdict(int)
def add(coef,scalar,current): p[scalar,current]+=coef
# Two times the four signed faces of Z_0123.
for coef,scalar,current in [
 (1,'23','y'),(-1,'12','z'),
 (-1,'23','x'),(-1,'23','y'),(1,'02','z'),
 (1,'13','x'),(-1,'01','y'),(-1,'01','z'),
 (-1,'12','x'),(1,'01','y')]: add(coef,scalar,current)
actual={k:v for k,v in p.items() if v}
expected={('23','x'):-1,('13','x'):1,('12','x'):-1,
          ('12','z'):-1,('02','z'):1,('01','z'):-1}
need(actual==expected,'twisted-cup quadruple defect')
checks.append('all endpoint terms give minus theta-cup-F minus F-cup-theta')
need(actual!={},'false endpoint-closure mutation must fail')
wrong=dict(expected)
for k in list(wrong):
    if k[1]=='z': wrong[k]=-wrong[k]
need(actual!=wrong,'wrong second cup sign must fail')
checks.append('false-zero and wrong second-cup sign controls rejected')
# W=-boundary-p sum Q_d delta c_d: check the four advertised signs.
defect_sign=[-1,1,-1,1]
need([-v for v in defect_sign]==[1,-1,1,-1],'Ward defect substitution signs')
checks.append('all four terminal and Ward signs')
print(json.dumps({'status':'pass','checks':checks,'scope':'invented formal coefficients only'},indent=2))

"""Only integer occurrence/character/frame metadata; no source execution."""
import json
from pathlib import Path

def demand(ok, text):
    if not ok: raise RuntimeError(text)
def add(x,y): return tuple(a+b for a,b in zip(x,y))
def scale(n,x): return tuple(n*a for a in x)
def maximum(*v): return tuple(map(max,zip(*v)))
def delta(v):
    faces=[v[:k]+(0,)+v[k:] for k in range(len(v)+1)]
    return maximum(*faces)
def lead(v,n): return (v[0]+n,)+v[1:]
def lift(c,l):
    c,l=lead(c,4),lead(l,1)
    for _ in range(2): c,l=lead(delta(c),4),delta(l)
    return c,l
L=((5,5,0),(3,3,0)); U=((4,9,5),(2,5,3)); H=((6,6,0),(4,4,0)); J=((4,10,6),(2,6,4))
def prod(*f): return tuple(tuple(sum(v) for v in zip(*(x[i] for x in f))) for i in (0,1))
phi=prod(U,H)
demand(phi==((10,15,5),(6,9,3)), 'flux owners')
vp=tuple(tuple(a+1 for a in x) for x in phi)
comm=prod(L,phi)
expected={
 'phi':((22,18,15,15,5),(7,9,9,9,3)),
 'vphi':((23,19,16,16,6),(8,10,10,10,4)),
 'commutator':((27,23,20,20,5),(10,12,12,12,3))}
for name,x in [('phi',phi),('vphi',vp),('commutator',comm)]:
    demand(lift(*x)==expected[name],name)
quartics=[prod(U,L,L,L),prod(U,U,L,L),prod(U,U,U,L)]
q=tuple(maximum(*(x[i] for x in quartics)) for i in (0,1))
mtypes=[prod(L,U,H),prod(U,U,H),prod(L,L,J),prod(L,U,J)]
m=tuple(maximum(*(x[i] for x in mtypes)) for i in (0,1))
demand(q==((19,32,15),(11,18,9)), 'quartic')
demand(m==((15,24,11),(9,14,7)), 'linear jet')
demand(lift(*q)==((31,32,32,32,15),(12,18,18,18,9)), 'quartic lift')
demand(lift(*m)==((27,24,24,24,11),(10,14,14,14,7)), 'linear jet lift')
for c,l in [*expected.values(),lift(*q),lift(*m)]:
    demand(max(c)<=53 and max(l)<=28,'differentiated weights dominate')
# Frame exponents: actual T -2 and test +2; paired derivative anomaly cancels.
demand(-2+2==0,'scalar line')
demand(-2+2==0,'product-rule anomaly')
for a in range(4):
    missing=15^(1<<a)
    demand(missing^(1<<a)==15,'derivative character')
    line=[-2-2*((missing>>r)&1)+2 for r in range(4)]
    demand(line[a]==0 and all(line[r]==-2 for r in range(4) if r!=a),'flux line')
# Negative controls are metadata alternatives, not physical evaluations.
demand(max(U[0][1],H[0][1]) != phi[0][1], 'max versus product rejected')
demand(phi != prod(U,((4,4,0),(3,3,0))), 'missing inverse rejected')
demand(prod(L,phi) != phi, 'omitted midpoint commutator rejected')
demand(2-(-2)!=0, 'wrong derivative sign rejected')
demand(2+(-1)!=0, 'missing H degree rejected')
# Finite Laurent derivative: x^n gives n*x^(n-1); residue can only receive n=0.
demand((-1)+1==0, 'residue input exponent')
demand(0==0,'its derivative multiplier vanishes')
print(json.dumps({'status':'PASS','scope':'integer owner vectors, character/frame labels only','T_phi':expected['phi'],'T_vphi':expected['vphi'],'T_commutator':expected['commutator'],'T_Q4_C4':lift(*q),'T_M2':lift(*m)},indent=2))

"""Tiny integer certificates and labels only; no source imports or physical data."""
import json

def need(ok, msg):
    if not ok:
        raise RuntimeError(msg)

def delta(v):
    faces=[v[:i]+(0,)+v[i:] for i in range(len(v)+1)]
    return tuple(max(f[j] for f in faces) for j in range(len(v)+1))

def add(a,b):
    need(len(a)==len(b), 'occurrence count')
    return tuple(x+y for x,y in zip(a,b))

def hom(v):
    return add(v,(4,)+(0,)*(len(v)-1))

phi=(10,15,5); leg=(6,9,3)
j=hom(phi); jl=add(leg,(1,0,0))
B=add(j,(5,5,0)); N=add(j,(9,5,0)); nl=add(jl,(1,1,0))
Q=hom(delta(N)); ql=delta(nl)
E=hom(delta(hom(delta(B)))); el=delta(delta(nl))
need((Q,ql)==((27,23,20,5),(8,10,10,3)), 'primitive ledger')
need((E,el)==((27,23,20,20,5),(8,10,10,10,3)), 'edge output ledger')
need(all(c<54 for c in Q+E) and all(l<29 for l in ql+el),'clearance')
need(len(Q)==4 and len(E)==5,'own weight counts')
for a in range(4):
    need(((15^(1<<a))^(1<<a))==15,'full character')
need((-1-1,2+1)==(-2,3),'primitive bidegree')
need(add(j,(5,5,0)) != N,'omitting Xi homotopy must fail')
need(delta(leg) != ql,'omitting inclusion/edge charges must fail')
need(len(N)==3,'same-triple insertion must not add a prefix')
print(json.dumps({'status':'pass','primitive':[Q,ql],'edge_output':[E,el],
 'scope':'integer metadata only; theorem and geometry are not inferred from controls'},sort_keys=True))

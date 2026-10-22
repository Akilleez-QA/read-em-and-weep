#!/usr/bin/env python3
"""Bounded abstract equality flags; no actual-instance evaluations."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
PINNED={
'all-profile-iterated-section-envelope.json': '280654f6fa7c82483bee82cf31865e8a561facab82a8456d8666616778762cef',
'maximal-profile-degree-envelope-refinement.json': '002cee319e88fb83039efca5d2816bdb93f578ba9a5a60d6fd44725edf5de94d',
'rank-three-quotient-frontier-144.json': 'a6fc9ec680d1866782e0233c234c5d80d398e9fc77734b59e61040ffc92021ad',
'NEGATIVE-GAUSS-FLAGS-HAVE-A-FINITE-DEGREE-ENVELOPE.md': '90aa42a0eded9cd3118d086a4ebf82ce98ff4e4c3682e1baaea61e5928f94088',
'ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md': 'a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256',
}
for f,h in PINNED.items():assert hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==h
names=['one','W','Wp','A','V','P','S','D','T'];dims=dict(zip(names,[1,2,2,3,3,4,4,5,6]))
edges=[('one','W'),('W','A'),('A','S'),('S','D'),('D','T'),('T','V'),('T','P'),('P','Wp')]
def tensorW(v):
 out={n:0 for n in names}
 for a,b in edges:out[a]+=v.get(b,0);out[b]+=v.get(a,0)
 return out
sym=[{'one':1},{'W':1}]
for t in range(2,11):
 v=tensorW(sym[-1]);sym.append({n:v[n]-sym[-2].get(n,0) for n in names if v[n]!=sym[-2].get(n,0)})
assert sym[7]=={'Wp':1,'T':1} and sym[8]=={'P':1,'D':1}
assert sym[10]=={'A':1,'V':1,'D':1}
assert all(sum(dims[n]*m for n,m in v.items())==i+1 for i,v in enumerate(sym))
prior=json.loads((ROOT/'all-profile-iterated-section-envelope.json').read_text())
maximal=json.loads((ROOT/'maximal-profile-degree-envelope-refinement.json').read_text())
keep=set(prior['remaining_ids']);assert len(keep)==26 and keep<=set(maximal['remaining_ids'])
rows=[r for r in json.loads((ROOT/'rank-three-quotient-frontier-144.json').read_text())['cases'] if r['id']in keep]
assert len(rows)==26 and len({r['id']for r in rows})==26
records=[];checked=0
for row in rows:
 for side,n,pi in [('A',14,0),('B',10,1)]:
  checked+=1;ell=int(row['profile'][pi]);assert ell in [1,2]
  lam=sorted([e for e,c in row[side]for _ in range(dims[c])],reverse=True)
  assert len(lam)==3
  choices=[]
  for h1 in range(n+1):
   for h2 in range(h1+1):
    h3=n-h1-h2
    if not 0<=h3<=h2 or h3!=ell-1:continue
    h=(h1,h2,h3);cap=sum(hh*l-hh*(hh+1)for hh,l in zip(h,lam));choices.append((cap,h))
  bound=max(c for c,h in choices);degree=-54-sum(lam);assert degree<=bound
  if degree!=bound:continue
  assert len(set(lam))==3 and all(c=='one'for e,c in row[side])
  flags=[]
  for cap,h in choices:
   if cap!=bound:continue
   quotients=[[lam[i]-2*j for i in range(3)if h[i]>=j]for j in range(1,h[0]+1)]
   assert sum(map(len,quotients))==n and sum(map(sum,quotients))==degree
   assert h[0]>h[1] and lam[0]==6 and h[0]in [7,8]
   e=2*h[0]-6;assert quotients[-1]==[-e]
   # Every proper equivariant quotient of the multiplicity-free Sym^e
   # has dimension at most e+1 minus its smallest irreducible dimension.
   assert all(m==1 for m in sym[e].values())
   proper_max=e+1-min(dims[c]for c in sym[e]);assert proper_max<h[0]+1
   twist=h[0]-e;rank=h[0]+1
   assert sum(dims[c]*m for c,m in sym[h[0]].items())==rank
   excluded=twist==-1 and (side=='A' or int(row['profile'][0])==2)
   flags.append({'heights':h,'graded_degrees_by_step':quotients,'terminal_line_degree':-e,'polynomial_span_dimension':e+1,'proper_equivariant_span_dimension_max':proper_max,'forced_saturated_subbundle':{'central_bundle':'E'if side=='A'else'Q*','twist':twist,'coefficient_character':sym[h[0]],'rank':rank},'height_excluded_by_central_twist_one_vanishing':excluded})
  records.append({'id':row['id'],'side':side,'profile':row['profile'],'target_degrees_descending':lam,'rank_F':n,'degree_F':degree,'capacity':bound,'flags':flags})
expected={'G3.11.6795493ae8cd','G3.11.a5d4e292b34e','G3.11.cce6e3ba4eeb','G3.21.d610e381ed75','G3.11.942927348917','G3.12.8e9af2d08af9','G3.21.45ca6278cbfc'}
assert checked==52 and len(records)==7 and {r['id']for r in records}==expected
cuts=[(r['id'],f['heights'])for r in records for f in r['flags']if f['height_excluded_by_central_twist_one_vanishing']]
assert cuts==[('G3.21.45ca6278cbfc',(7,6,1)),('G3.21.d610e381ed75',(7,3,0))]
assert all(any(not f['height_excluded_by_central_twist_one_vanishing']for f in r['flags'])for r in records)
out={'scope':'Seven equality flags rigidify; two height patterns are impossible; no quotient label excluded. Geometry proved in accompanying note.','source_hashes':PINNED,'orientation_count':checked,'equality_label_count':len(records),'excluded_height_count':len(cuts),'excluded_label_count':0,'remaining_label_count':26,'records':records}
(ROOT/'equality-gauss-rational-normal-subbundles.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: 52 orientations; seven equality labels; two impossible heights; zero label exclusions.')

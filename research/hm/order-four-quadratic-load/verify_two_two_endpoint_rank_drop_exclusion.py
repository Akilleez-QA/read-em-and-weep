"""Bounded abstract bundle/character proof; no actual matrices, points, or ranks."""
from pathlib import Path
import contextlib,io,json,hashlib,functools
ROOT=Path(__file__).resolve().parent
ns={'__file__':str(ROOT/'verify_two_two_second_interior_euler.py')}
with contextlib.redirect_stdout(io.StringIO()):
 exec((ROOT/'verify_two_two_second_interior_euler.py').read_text().split('raw=(ROOT/')[0],ns)
chi,names,dims=[ns[k] for k in ('chi','names','dims')]
sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
expand=lambda N:tuple((-j,n) for j,n,m in N for _ in range(m))
parity=lambda n,j:ns['r'][n][1][0]==(-1)**j*ns['r'][n][0][0]
def h0(F,t):return chi(tuple((e,n) for e,n in F if e+t>=0),t)
@functools.lru_cache(None)
def candidates(rank,degree,base,c0,c1):
 excess=-degree-base*rank
 assert excess>=0
 allowed=[(j,n) for j in range(base+2,base+excess+1) for n in names if (j-base)*dims[n]<=excess and parity(n,j)]
 out=[]
 def go(i,blocks,left):
  if i<len(allowed):
   j,n=allowed[i];cost=(j-base)*dims[n]
   for m in range(left//cost+1):go(i+1,blocks+([(j,n,m)] if m else []),left-m*cost)
   return
  F=expand(blocks);r0=sub(c0,chi(F,base))
  if min(r0)<0:return
  B0=tuple((-base,n) for n,m in zip(names,r0) for _ in range(m))
  r1=sub(sub(c1,chi(F,base+1)),chi(B0,base+1))
  if min(r1)<0:return
  if any(m and not parity(n,j) for j,rs in ((base,r0),(base+1,r1)) for n,m in zip(names,rs)):return
  B=[(base,n,m) for n,m in zip(names,r0) if m]+[(base+1,n,m) for n,m in zip(names,r1) if m]+blocks
  if sum(dims[n]*m for j,n,m in B)!=rank or -sum(j*dims[n]*m for j,n,m in B)!=degree:return
  out.append(B)
 go(0,[],excess)
 return out
raw=(ROOT/'two-two-endpoint-top-slope-records.json').read_bytes()
assert hashlib.sha256(raw).hexdigest()=='2247e4b21614baeca644e9e165960e978f08c994557d4737f50d9c3380344cc2'
records=json.loads(raw);assert len(records)==354
pairs={json.dumps([x['A'],x['B']],separators=(',',':')) for x in records};assert len(pairs)==3
summary=[]
for key in sorted(pairs):
 xs=[x for x in records if json.dumps([x['A'],x['B']],separators=(',',':'))==key]
 A,B=json.loads(key);b=sum(e*dims[n] for e,n in B)
 J=tuple((e-2,n) for e,n in B)
 classes={(sub(chi(expand(L),4),chi(J,4)),sub(chi(expand(L),5),chi(J,5))) for x in xs for L in x['L_splittings']}
 assert len(classes)==1
 c0,c1=next(iter(classes));degree=-48-2*b
 cs=candidates(7,degree,4,c0,c1)
 filtered=[N for N in cs if min(sub(h0(tuple(map(tuple,B)),0),h0(expand(N),4)))>=0]
 if degree==-32:
  assert filtered==[[(4,'V',1),(5,'W',1),(5,'Wp',1)]]
  # Every component of the derivative except O(2) has negative Hom degree.
  target=[(e-4,n) for e,n in B]
  assert [(e,n) for e,n in target if any(e+j>=0 for j,_,_ in filtered[0])]==[(2,'one')]
  # Backward rank-one identity: sum gaps weighted i = r*d_last-r*(r-1)-degree.
  assert 7*2-7*6-degree==4<12
  assert (7*6+degree)%7!=0
 else:
  assert degree==-36
  assert filtered==[[(4,'V',1),(5,'Wp',1),(7,'W',1)],[(4,'V',1),(5,'Wp',1),(6,'one',1),(8,'one',1)]]
  target=[(e-4,n) for e,n in B]
  reachable=[[(e,n) for e,n in target if any(e+j>=0 for j,_,_ in N)] for N in filtered]
  assert [set(v) for v in reachable]==[{(2,'one')},{(2,'one'),(-8,'one')}]
  assert 7*2-7*6-degree==8<12
  assert (7*6+degree)%7!=0
 summary.append(dict(A=A,B=B,endpoint_degree=degree,before_top_injection=cs,endpoint_splittings=filtered))
# Only rank-two endpoint branch: N -> C, invariant determinant length t.
N=((4,'V',1),(5,'Wp',1),(6,'one',1),(8,'one',1));C=((2,'one'),(-8,'one'))
assert -36-sum(e*dims[n] for e,n in C)==-30
assert -5*5-(-30)==5<12 # forces t=0
c0=sub(chi(expand(N),5),chi(C,5));c1=sub(chi(expand(N),6),chi(C,6))
ps=candidates(5,-30,5,c0,c1)
assert sorted(ps)==sorted([[(6,'one',1),(6,'P',1)],[(5,'Wp',1),(6,'one',1),(7,'Wp',1)]])
assert all(j<10 for P in ps for j,n,m in P)
# P derivative reaches only O(0) in C(-2). Its last line degree d obeys
# 0 <= 5*d+10 <= 10; every nonzero invariant gap is >=12.
assert 5*0-5*4-(-30)==10<12
assert (5*4-30)//5==-2
assert 0-(-2)==2<12 # impossible invariant zeros of its map to O(0)
result=dict(input_sha256=hashlib.sha256(raw).hexdigest(),records=354,pairs=summary,rank_two_branch_kernel_splittings=ps,remaining_pairs=0,scope='Abstract endpoint rank-drop and equivariant line-divisor proof; no actual-instance computation.')
(ROOT/'two-two-endpoint-rank-drop-summary.json').write_text(json.dumps(result,indent=2)+'\n')
assert (ROOT/'two-two-endpoint-top-slope-records.json').read_bytes()==raw
print('PASS: exhaustive bounded endpoint splitting characters and top injections.')
print('PASS: rank-one backward invariant-gap contradictions for both endpoint degrees.')
print('PASS: sole rank-two branch has zero determinant torsion and two kernel splittings.')
print('PASS: next rank-one branch forces a forbidden invariant degree-two divisor.')
print('CONCLUSION: all three residual quotient pairs, hence the (2,2) profile, are excluded.')

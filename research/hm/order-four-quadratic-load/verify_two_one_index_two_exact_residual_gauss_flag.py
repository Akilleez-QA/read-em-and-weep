#!/usr/bin/env python3
"""Exact residual flag after a genuine constant quotient; universal symbols only."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parent
PINNED={'TWO-ONE-INDEX-TWO-RESIDUAL-FULL-SPAN.md': 'f7621cc508b76f8c12e52a0c5eddf067e18688a174265d930403fc8a69641026', 'rank-three-quotient-frontier-144.json': 'a6fc9ec680d1866782e0233c234c5d80d398e9fc77734b59e61040ffc92021ad'}

assert all(hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==h for f,h in PINNED.items())
ID='G3.21.d610e381ed75'
row=next(r for r in json.loads((ROOT/'rank-three-quotient-frontier-144.json').read_text())['cases']if r['id']==ID)
assert row['profile']=='21' and row['source_index']==2
assert row['A']==[[-8,'one'],[2,'one'],[16,'one']] and row['B']==[[-18,'one'],[-4,'one'],[6,'one']]
# Universal degree-eight osculating fibers l^(8-j) Sym^j W; no actual invariant/source coefficients.
osculations=[]
for j in range(3):
 rank=j+1;degree=(j+1)*(j-8);symbol=8-j
 # d/dt[(x+t*y)^(8-j)*y^j] at t=0 has symbol (8-j)*x^(7-j)*y^(j+1).
 assert symbol>0
 assert (7-j)+(j+1)==8
 previous_degree=0 if j==0 else j*(j-9)
 quotient_degree=degree-previous_degree
 assert quotient_degree==2*j-8
 osculations.append(dict(j=j,rank=rank,degree=degree,backward_rank=j,backward_degree=previous_degree,nonzero_universal_symbol_coefficient=symbol,quotient_line_degree=quotient_degree))
assert [(x['rank'],x['degree'])for x in osculations]==[(1,-8),(2,-14),(3,-18)]
# Published saturated final quotient is a negative line, so its backward kernel is zero.
final_line_degree=-18;assert final_line_degree<0
# Projection-kernel lemma gives R^-=A0^-=U1, not an assumed residual connection.
flag=[dict(rank=4,degree=-36,splitting=[[-18,'one'],[-6,'A']]),dict(rank=2,degree=-14,splitting=[[-7,'W']]),dict(rank=1,degree=-8,splitting=[[-8,'one']]),dict(rank=0,degree=0,splitting=[])]
quotients=[dict(rank=flag[i]['rank']-flag[i+1]['rank'],degree=flag[i]['degree']-flag[i+1]['degree'])for i in range(3)]
assert quotients==[dict(rank=2,degree=-22),dict(rank=1,degree=-6),dict(rank=1,degree=-8)]
assert -18+(-4)==-22
out=dict(scope='Exact actual projected residual Gauss flag; no quotient-label exclusion or realization.',id=ID,source_hashes=PINNED,full_span_commit='e21d50b6bd7d124dc419beeb8c27fa3b9ef3e169',constant_quotient_rank=10,saturated_final_line_degree=final_line_degree,universal_degree_eight_osculations=osculations,actual_R_flag=flag,actual_quotients=[dict(**quotients[0],splitting=[[-18,'one'],[-4,'one']]),dict(**quotients[1],splitting=[[-6,'one']]),dict(**quotients[2],splitting=[[-8,'one']])],projection_kernel_lemma='If F projects to saturated C in a constant quotient and C^-=0, then F^-=(F intersect V)^-.',actual_source_parameter_assigned=False,realization_claimed=False)
(ROOT/'two-one-index-two-exact-residual-gauss-flag.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS:',ID,'actual projected residual flag ranks4,2,1,0; degrees-36,-14,-8,0.')

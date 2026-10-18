"""Verify the recorded exact certificate; never load or evaluate the source."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
HERE=Path(__file__).resolve().parent
RESULT_SHA='a6290391e3cfdf7f211bec87dcbc3fd516471377642e4f839f0bc9efd85babe2'
def need(ok,msg):
 if not ok:raise RuntimeError(msg)
def mul(a,b):return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def components(a):return [(a[0][0]-a[1][1])/2,a[0][1],a[1][0]]
def main():
 raw=(HERE/'one-attempt-result.json').read_bytes()
 need(hashlib.sha256(raw).hexdigest()==RESULT_SHA,'recorded result digest')
 d=json.loads(raw)
 need(d['result_complete'] and d['physical_source_evaluated'] and d['child_returncode']==0,'completed source result')
 need(d['independent_chain_rule_and_direct_frame_checks'] and d['PI_determinant_and_cocycle_germ_checks'],'recorded checks')
 need(d['x_rationals']==['2','13/6','7/3','5/2'],'fixed point')
 need(d['physical_vertices']==[{'carrier':0,'legal_mask':0},{'carrier':1,'legal_mask':5},{'carrier':2,'legal_mask':10}],'fixed vertices')
 H=[[[F(x) for x in row] for row in a] for a in d['H']]
 J=[[[F(x) for x in row] for row in a] for a in d['J']]
 O=[[F(0) for _ in range(2)] for _ in range(2)];C=[[F(0) for _ in range(3)] for _ in range(3)]
 for i,j,s in ((0,3,1),(1,2,-1),(2,1,-1),(3,0,1)):
  a,b=mul(J[i],H[j]),mul(H[j],J[i]);u,v=components(J[i]),components(H[j])
  for x in range(2):
   for y in range(2):O[x][y]+=F(s,8)*(a[x][y]-b[x][y])
  for x in range(3):
   for y in range(3):C[x][y]+=s*u[x]*v[y]
 need(O==[[F(x) for x in row] for row in d['omega_stripped']],'commutator recomputation')
 need(C==[[F(x) for x in row] for row in d['gram']],'cross Gram recomputation')
 need([C[1][2]-C[2][1],C[0][1]-C[1][0],C[2][0]-C[0][2]]==list(map(F,d['skew'])),'all skews')
 need(O[0][0]+O[1][1]==0 and O[0][0]!=0,'tracefree nonzero')
 need(all(F(x['value'])!=0 and x['nonzero'] for x in d['denominator_checks']),'recorded denominators')
 w=O[0][0];need(w.denominator%101!=0,'modular unit')
 need(w.numerator*pow(w.denominator,-1,101)%101==7,'small exact nonzero witness')
 print('PASS: recorded exact Omega and cross-Gram agree; Omega00 = 7 mod101 with unit denominator; no source rerun')
if __name__=='__main__':main()

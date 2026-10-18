"""Authenticate sparse source metadata; never evaluate a source polynomial."""
from pathlib import Path
import hashlib
import json
import sys
SHA='635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926'
def need(ok,msg):
 if not ok:raise RuntimeError(msg)
def terms(p):return {tuple(map(int,e.split(','))):c for e,c in p}
def shift(p,k):return {(e[0]+k,)+e[1:]:c for e,c in terms(p).items()}
def degree(p):return max((e[0] for e in terms(p)),default=None)
def lead(p):
 d=degree(p);return {(e[1:]):c for e,c in terms(p).items() if e[0]==d}
def main(path):
 raw=path.read_bytes();need(hashlib.sha256(raw).hexdigest()==SHA,'model digest')
 m=json.loads(raw);c0,c1=m['charts'][:2]
 need(c0['pivot']==0 and c1['pivot']==1,'selected carrier pivots')
 for c in (c0,c1):need(c['di']==c['dp'],'separate I/P denominator mismatch')
 need(terms(c0['I'][0][0])==terms(c0['di']),'I0 row0 unit')
 need(terms(c0['I'][5][1])==terms(c0['di']),'I0 row5 unit')
 need(terms(c1['I'][1][0])==terms(c1['di']),'I1 row1 unit')
 need(terms(c1['I'][6][1])==shift(c1['di'],1),'I1 row6 equals t')
 need(terms(c1['P'][1][6])==shift(c1['dp'],-1),'P1 col6 equals inverse t')
 for carrier,c in enumerate((c0,c1)):
  for i in range(2):
   for j in range(2):
    found=[k for k in range(15) if c['P'][i][k] and c['I'][k][j]]
    expected=([0] if i==j==0 else [5] if i==j==1 else []) if carrier==0 else ([1] if i==j==0 else [6] if i==j==1 else [])
    need(found==expected,'connection support intersection')
 # All-carrier diagonal connection certificate, using exact term shifts only.
 for c,ch in enumerate(m['charts']):
  a,b=(c,c+5) if c<5 else (5,14)
  need(terms(ch['I'][a][0])==terms(ch['di']),'all-carrier first unit')
  need(terms(ch['P'][0][a])==terms(ch['dp']),'all-carrier first inverse unit')
  for i in range(2):
   for j in range(2):
    rows=[k for k in range(15) if ch['P'][i][k] and ch['I'][k][j]]
    need(rows==([a] if i==j==0 else [b] if i==j==1 else []),'all-carrier support')
  if c<5:
   def move(poly,amount):
    out={}
    for e,v in terms(poly).items():
     ee=list(e)
     if c:ee[c-1]+=amount
     out[tuple(ee)]=v
    return out
   need(terms(ch['I'][b][1])==move(ch['di'],1),'primary second I')
   need(terms(ch['P'][1][b])==move(ch['dp'],-1),'primary second P')
  else:
   need(terms(ch['di'])=={(2,0,1,1):-1},'aux denominator I')
   need(terms(ch['dp'])=={(2,0,1,1):-1},'aux denominator P')
   need(terms(ch['I'][b][1])=={(0,0,1,2):1},'aux second I')
   need(terms(ch['P'][1][b])=={(4,0,1,0):1},'aux second P')
 need(degree(c0['di'])==1 and lead(c0['di'])=={(1,1,1):1},'d0 leading')
 need(degree(c1['di'])==5 and lead(c1['di'])=={(0,0,0):-1},'d1 leading')
 expected={(0,0):[(1,1),(4,-2),(7,-1)],(0,1):[(4,0),(7,-1)],(1,0):[(1,0),(4,-4),(5,-2),(7,-2)],(1,1):[(4,-2),(5,-2),(7,-2)]}
 for i,j in expected:
  found=[]
  for k in range(15):
   p,q=c0['P'][i][k],c1['I'][k][j]
   if p and q:found.append((k,degree(p)-degree(c0['dp'])+degree(q)-degree(c1['di'])))
  need(found==expected[i,j],'transition degree table')
 need(lead(c0['P'][0][4])=={(1,0,1):-1},'K01 first leading numerator')
 need(lead(c1['I'][4][1])=={(1,0,1):1},'K01 second leading numerator')
 need(lead(c0['P'][1][1])=={(0,2,0):-1},'K10 first leading numerator')
 need(terms(c1['I'][1][0])==terms(c1['di']),'K10 second factor unit')
 print(json.dumps(dict(status='PASS',model_sha256=SHA,source_values_evaluated=False,polynomial_evaluator_called=False,actual_point_selected=False,connection_supports=True,all_six_diagonal_connections=True,transition_degree_table=True,unique_leading_terms=True)))
if __name__=='__main__':
 default=Path(__file__).resolve().parents[2]/'null-one-point-launcher'/'sources'/'model.json'
 main(Path(sys.argv[1]) if len(sys.argv)==2 else default)

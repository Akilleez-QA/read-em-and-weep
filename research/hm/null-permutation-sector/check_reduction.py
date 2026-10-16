"""Exact representation arithmetic and invented Hessian arrays; no source input."""
from fractions import Fraction as F
from itertools import combinations
import json

def need(ok,msg):
 if not ok:raise RuntimeError(msg)

def matrices(a,b):
 return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def comm(a,b):
 x,y=matrices(a,b),matrices(b,a)
 return [[x[i][j]-y[i][j] for j in range(2)] for i in range(2)]
def zero():return [[F(0),F(0)],[F(0),F(0)]]
def omega(H,J,p,q):
 a,b=p;c,d=q
 terms=[((a,c),(b,d),1),((a,d),(b,c),-1),((b,c),(a,d),-1),((b,d),(a,c),1)]
 out=zero()
 for u,v,s in terms:
  x=comm(J[tuple(sorted(u))],H[tuple(sorted(v))])
  for i in range(2):
   for j in range(2):out[i][j]+=F(s,8)*x[i][j]
 return out

def main():
 cycles=[4,3,2,2,1];sgn=[1,-1,1,1,-1]
 irreps=[[1]*5,[3,1,-1,0,-1],[2,0,2,-1,0],[3,-1,-1,0,1],sgn]
 W=[[1]*5,[2**c-5 for c in cycles],[3**c-5*2**c+10 for c in cycles],[4**c-5*3**c+10*2**c-10 for c in cycles]]
 need(W[1]==[3*irreps[1][i]+irreps[2][i] for i in range(5)],'W1')
 need(W[2]==[3*irreps[3][i]+irreps[2][i] for i in range(5)],'W2')
 need(W[3]==sgn,'W3')
 full=[sgn[i]*(2*W[0][i]+10*W[1][i]+20*W[2][i]+20*W[3][i]) for i in range(5)]
 need(full==[352,48,-8,-8,-12],'full character')
 multiplicities=[20,60,30,30,2]
 need(full==[sum(m*r[i] for m,r in zip(multiplicities,irreps)) for i in range(5)],'S4 decomposition')
 d8=[F(r[0]-2*r[1]+3*r[2]-2*r[4],8) for r in irreps]
 need(d8==[0,0,1,0,1],'D8 signs')
 need(sum(m*d for m,d in zip(multiplicities,d8))==32,'sector dimension')
 basis=[[[F(1),F(0)],[F(0),F(-1)]],[[F(0),F(1)],[F(0),F(0)]],[[F(0),F(0)],[F(1),F(0)]]]
 slots=list(combinations(range(4),2));count=0
 for hs in slots:
  for js in slots:
   for hb in basis:
    for jb in basis:
     H={s:zero() for s in slots};J={s:zero() for s in slots};H[hs]=hb;J[js]=jb
     out=[omega(H,J,(0,1),(2,3)),omega(H,J,(0,2),(1,3)),omega(H,J,(0,3),(1,2))]
     need(all(out[0][i][j]-out[1][i][j]+out[2][i][j]==0 for i in range(2) for j in range(2)),'alternating Omega')
     count+=1
 print(json.dumps(dict(status='PASS',full_character=full,sector_dimension=32,alternating_rank=2,complement_dimension=30,invented_symbol_basis_pairs=count,source_evaluation=False,rank_inputs_recomputed=False)))

if __name__=='__main__':main()

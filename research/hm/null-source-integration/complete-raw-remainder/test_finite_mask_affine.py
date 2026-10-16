"""Invented first-jet matrix control. No actual-source input or imports."""
from fractions import Fraction as F
from itertools import combinations

def M(a):return tuple(tuple(map(F,r)) for r in a)
def add(a,b):return tuple(tuple(x+y for x,y in zip(r,s)) for r,s in zip(a,b))
def scale(a,t):return tuple(tuple(x*t for x in r) for r in a)
def sub(a,b):return add(a,scale(b,-1))
def mul(a,b):return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def inv(a):
 d=a[0][0]*a[1][1]-a[0][1]*a[1][0]
 return scale(((a[1][1],-a[0][1]),(-a[1][0],a[0][0])),1/d)
def tr(a):return a[0][0]+a[1][1]
def tf(a):return sub(a,scale(ID,tr(a)/2))
def conj(k,a):return mul(mul(k,a),inv(k))
ID=M(((1,0),(0,1)));h=M(((1,0),(0,-1)))
K=M(((1,2),(0,1)));B=M(((1,0),(3,1)));KB=mul(K,B)
# Arbitrary rational reference connection/current coefficients, all invented.
gi=[M(((a+1,2-a),(a,1))) for a in range(4)]
gj=[M(((2,a+1),(1-a,3))) for a in range(4)]
dK=[mul(M(((a,1),(2,-a))),K) for a in range(4)]
dB=[mul(M(((1-a,a),(3,a-1))),B) for a in range(4)]
Q=[sub(sub(conj(K,gj[a]),mul(dK[a],inv(K))),gi[a]) for a in range(4)]
Z=[scale(mul(dB[a],inv(B)),-1) for a in range(4)]
u=list(map(F,[1,2,-1,3]));v=list(map(F,[2,-2,4,1]));r=list(map(F,[1,3,2,5]))
Aj=[tr(mul(tf(q),conj(K,h))) for q in Q]
Ak=[tr(mul(tf(q),conj(KB,h))) for q in Q]
pairs=list(combinations(range(4),2))
def wedge(a,b,c,d):return a[c]*b[d]-a[d]*b[c]
def ref(j,k):
 ellj=[r[a]*((j>>a)&1) for a in range(4)]
 ellk=[r[a]*((k>>a)&1) for a in range(4)]
 ans=[]
 for c,d in pairs:
  base=tr(sub(mul(tf(Q[c]),conj(K,Z[d])),mul(tf(Q[d]),conj(K,Z[c]))))-2*wedge(u,v,c,d)
  ans.append(base+wedge([Aj[a]-19*u[a] for a in range(4)],ellj,c,d)+wedge([19*u[a]-Ak[a] for a in range(4)],ellk,c,d))
 return ans

def direct(i,j,k):
 ell=[[r[a]*((m>>a)&1) for a in range(4)] for m in (i,j,k)]
 q=[];z=[]
 for a in range(4):
  GammaI=add(gi[a],scale(h,ell[0][a]));GammaJ=add(gj[a],scale(h,ell[1][a]))
  dg=add(sub(dK[a],mul(scale(h,ell[0][a]),K)),mul(K,scale(h,ell[1][a])))
  q.append(sub(sub(conj(K,GammaJ),mul(dg,inv(K))),GammaI))
  db=add(sub(dB[a],mul(scale(h,ell[1][a]),B)),mul(B,scale(h,ell[2][a])))
  z.append(conj(K,scale(mul(db,inv(B)),-1)))
 if q!=Q:raise RuntimeError('first-mask connection cancellation failed')
 scalar=[38*(ell[2][a]-ell[1][a])-4*v[a] for a in range(4)]
 return [tr(sub(mul(tf(q[c]),z[d]),mul(tf(q[d]),z[c])))+wedge(u,scalar,c,d)/2 for c,d in pairs]

def main():
 baseline=ref(0,0)
 cj=[[x-y for x,y in zip(ref(1<<a,0),baseline)] for a in range(4)]
 ck=[[x-y for x,y in zip(ref(0,1<<a),baseline)] for a in range(4)]
 for j in range(16):
  for k in range(16):
   target=ref(j,k)
   affine=[baseline[s]+sum(cj[a][s]*((j>>a)&1)+ck[a][s]*((k>>a)&1) for a in range(4)) for s in range(6)]
   if target!=affine:raise RuntimeError('affine mask reconstruction failed')
   for i in (0,15):
    if direct(i,j,k)!=target:raise RuntimeError('direct physical-jet comparison failed')
 for s,(c,d) in enumerate(pairs):
  for a in range(4):
   if a not in (c,d) and (cj[a][s] or ck[a][s]):raise RuntimeError('pair support failed')
 print('PASS: 512 direct first-jet gauge comparisons, 256 affine reconstructions, six pair-support checks; invented data only')
if __name__=='__main__':main()

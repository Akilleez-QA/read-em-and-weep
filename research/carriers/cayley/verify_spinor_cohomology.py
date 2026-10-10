import itertools
import sympy as s
from collections import defaultdict
# n = x,y,z,u,v; [x,y]=z, [x,z]=u, [y,z]=v
nc=[-1,-1,-2,-3,-3]; nh=[1,-1,0,1,-1]
br={(0,1):2,(0,2):3,(1,2):4}
# S=s0,a,b,c; central weights and h eigenvalues
sc=[0,-1,-1,-2]; sh=[0,1,-1,0]
# adjoint Levi module A=a^2, B=ab, D=b^2
mh=[2,0,-2]
# V=End0(C) S(-2), represented (m,t)
vc={(m,t):sc[t]-4 for m in range(3) for t in range(4)}
vh={(m,t):mh[m]+sh[t] for m in range(3) for t in range(4)}
# spinor action [x,y]=z, action z:s0->2c
act={(0,0):{1:1},(0,2):{3:1},(1,0):{2:1},(1,1):{3:-1},(2,0):{3:2}}
def wedge(I,J):
    if set(I)&set(J):return None,0
    L=I+J
    return tuple(sorted(L)),(-1)**sum(L[i]>L[j] for i in range(len(L)) for j in range(i+1,len(L)))
def basis(q,h=0):
 return [(m,t,I) for m,t in vc for I in itertools.combinations(range(5),q) if vc[m,t]-sum(nc[i] for i in I)==0 and vh[m,t]-sum(nh[i] for i in I)==h]
def differential(v):
 m,t,I=v; out=defaultdict(int)
 # module action
 for i in range(5):
  J,sg=wedge((i,),I)
  if J is not None:
   for t2,a in act.get((i,t),{}).items():out[m,t2,J]+=sg*a
 # form action
 for k,n in enumerate(I):
  for (i,j),r in br.items():
   if r!=n:continue
   J,sg=wedge(I[:k],(i,j))
   if J is None:continue
   J,sg2=wedge(J,I[k+1:])
   if J is not None:out[m,t,J]+=(-1)**k*(-1)*sg*sg2
 return {k:a for k,a in out.items() if a}
def raising(v):
 m,t,I=v; out=defaultdict(int)
 # e on Sym2 standard: B->A, D->2B
 if m==1:out[0,t,I]+=1
 if m==2:out[1,t,I]+=2
 if t==2:out[m,1,I]+=1
 # e on dual n: x*->-y*, u*->-v*
 for k,n in enumerate(I):
  if n not in (0,3):continue
  new=n+1
  J,sg=wedge(I[:k],(new,))
  if J is None:continue
  J,sg2=wedge(J,I[k+1:])
  if J is not None:out[m,t,J]+=-sg*sg2
 return {k:a for k,a in out.items() if a}
def matrix(f,src,dst):
 ix={k:i for i,k in enumerate(dst)}; M=s.zeros(len(dst),len(src))
 for j,b in enumerate(src):
  for c,v in f(b).items():
   assert c in ix,(b,c,v)
   M[ix[c],j]+=v
 return M
Bs=[basis(q) for q in range(6)]
Es=[matrix(raising,Bs[q],basis(q,2)) for q in range(6)]
Ks=[s.Matrix.hstack(*E.nullspace()) if E.nullspace() else s.zeros(E.cols,0) for E in Es]
Ds=[matrix(differential,Bs[q],Bs[q+1]) for q in range(5)]
for q in range(4):assert Ds[q+1]*Ds[q]==s.zeros(len(Bs[q+2]),len(Bs[q]))
rs=[]
print('Degree, torus-zero dimension, invariant dimension, differential rank')
for q in range(6):
 r=(Ds[q]*Ks[q]).rank() if q<5 else 0;rs.append(r)
 print(q,len(Bs[q]),Ks[q].cols,r)
 if Ks[q].cols:
  print('Basis',Bs[q]);print('Invariants',Ks[q]);print('d invariants',Ds[q]*Ks[q] if q<5 else None)
print('Cohomology dimensions',[Ks[q].cols-rs[q]-(rs[q-1] if q else 0) for q in range(6)])

# Assert the certificate, rather than merely printing ranks.
assert [K.cols for K in Ks] == [0,0,2,2,0,0]
assert rs == [0,0,2,0,0,0]
small,params=Ks[3].gauss_jordan_solve(Ds[2]*Ks[2])
assert params.rows == 0
assert small == s.Matrix([[1,-1],[-2,-1]])
assert small.det() == -3
print('PASS: invariant differential is exactly [[1,-1],[-2,-1]], determinant -3.')

# Calibrate the same Lie/Levi conventions on the two endpoint line twists.
for twist, expected_degree in [(-2,2),(-3,3)]:
    vc={(m,0):2*twist for m in range(3)}
    vh={(m,0):mh[m] for m in range(3)}
    act={}
    Bs=[basis(q) for q in range(6)]
    Es=[matrix(raising,Bs[q],basis(q,2)) for q in range(6)]
    Ks=[s.Matrix.hstack(*E.nullspace()) if E.nullspace() else s.zeros(E.cols,0) for E in Es]
    Ds=[matrix(differential,Bs[q],Bs[q+1]) for q in range(5)]
    for q in range(4):
        assert Ds[q+1]*Ds[q] == s.zeros(len(Bs[q+2]),len(Bs[q]))
    ranks=[(Ds[q]*Ks[q]).rank() if q<5 else 0 for q in range(6)]
    cohom=[Ks[q].cols-ranks[q]-(ranks[q-1] if q else 0) for q in range(6)]
    assert cohom == [int(i==expected_degree) for i in range(6)]
    print('PASS: End0(C)('+str(twist)+') endpoint invariant cohomology',cohom)

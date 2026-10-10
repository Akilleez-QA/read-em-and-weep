import itertools,sympy as s
forms=[[(0,0,0,0)],[(1,1,1,1)],[(0,0,0,1),(0,0,1,0),(0,1,0,0),(1,0,0,0)],[(0,1,1,1),(1,0,1,1),(1,1,0,1),(1,1,1,0)],[(0,0,1,1),(1,1,0,0)],[(0,1,0,1),(1,0,1,0)],[(0,1,1,0),(1,0,0,1)]]
for n in (1,2,3):
 src=list(itertools.product(range(n),range(n),range(n+1),range(n+1)))
 dst=list(itertools.product(range(n+1),range(n+1),range(n+2),range(n+2))); inds={x:i for i,x in enumerate(dst)}
 M=s.zeros(len(dst),len(src)*7)
 for j,m in enumerate(src):
  for k,f in enumerate(forms):
   for v in f:M[inds[tuple(m[a]+v[a] for a in range(4))],7*j+k]+=1
 from sympy.polys.matrices import DomainMatrix
 rank=DomainMatrix.from_Matrix(M).convert_to(s.GF(32003)).rank()
 print(n,'to',n+1,'shape',M.shape,'rank',rank,'missing',len(dst)-rank,flush=True)

"""Universal coefficients and representation checks, never actual-instance values."""
from universal_complete_identity_w_spin_symbols import *
FB,FC,FD=s.symbols('FB FC FD',nonzero=True)
f=s.Matrix([[0,0,FC,0],[-9*FB*FC/FD,0,0,0],[0,0,0,FD],[0,FB,0,0]])
zero_matrix(f.T*J3*f-3*FB*FC*J3)
q=s.symbols('qH0:5');H0=op4(sum(c*m for c,m in zip(q,mon(4))))
R=s.Matrix(4,4,s.symbols('test_R0:16'))
for A0,A1 in [(binary_E,E1),(binary_F,F1),(binary_H,H1)]:
 zero_matrix(partial_spin(comm(A0,H0),R)+partial_spin(H0,comm(A0,R))-comm(A1,partial_spin(H0,R)))
print('PASS: full SL2 equivariance of the partial-trace coefficient map.',flush=True)
rq,rh=build_identity_w_spin_symbols(f,H0)
vars0=(*q,h,k,l,u,w)
co=s.symbols('free_spin_co0:6')
Q=sum((co[i]*K[4:,4:] for i,(_,K) in enumerate(rq)),s.zeros(2))
rows=[]
for entry in Q:
 for _,val in s.Poly(s.expand(entry),*vars0).terms():
  rows.append([s.factor(s.diff(val,c)) for c in co])
# Exact coefficient elimination with only Laurent-monomial pivots.
# This proves identities over ALL nonzero frame scales, not one value.
pivots=[];used=set()
for col in range(6):
 found=None
 for j,row in enumerate(rows):
  if j in used or row[col]==0:continue
  num,den=s.fraction(s.factor(row[col]))
  if len(s.Poly(num,FB,FC,FD).terms())==len(s.Poly(den,FB,FC,FD).terms())==1:
   found=j;break
 assert found is not None,(col,'No universally invertible coefficient pivot found')
 used.add(found);piv=rows[found][col];pivots.append(piv)
 rows[found]=[s.cancel(v/piv) for v in rows[found]]
 for j,row in enumerate(rows):
  if j==found or row[col]==0:continue
  fac=row[col];rows[j]=[s.cancel(a-fac*b) for a,b in zip(row,rows[found])]
print('PASS: six coefficient directions are independent with Laurent-unit pivots:',pivots,flush=True)
assert any(s.expand(v)!=0 for v in rh[0][1])
for name,K in rq+rh:
 zero_matrix(K[:4,:]);zero_matrix(K[:,:4])
 for e in K:
  if e==0:continue
  for powers,coefficient in s.Poly(s.expand(e),h,k,l,u,w).terms():
   if coefficient==0:continue
   assert sum(powers[:3])==2 and sum(powers[3:])==2,(name,powers)
print('PASS: all seven symbols have pure SS support and exact D-degree2, base-degree2.',flush=True)
# Character arithmetic provides completeness ONLY in this coefficient block.
p=(1+s.sqrt(5))/2;sizes=[1,15,20,12,12]
ca=s.Matrix([3,-1,0,p,1-p]);cv=s.Matrix([3,-1,0,1-p,p]);c5=s.Matrix([5,1,-1,0,0]);one=s.ones(5,1)
N=(one+c5).multiply_elementwise(ca);end=one+cv
inner=lambda a,b:s.simplify(sum(n*x*y for n,x,y in zip(sizes,a,b))/60)
assert inner(c5.multiply_elementwise(N),end)==6 and inner(N,end)==1
print('PASS: the complete equivariant SS coefficient spaces have dimensions6 and1.')
print('No independence of exterior middle operators or successful source completion is claimed.')

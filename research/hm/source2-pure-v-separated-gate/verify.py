from pathlib import Path
import hashlib,json
r=Path(__file__).resolve().parent;checks=[]
def ck(n,b):
 if not bool(b):raise RuntimeError(n)
 checks.append(n)
for v in json.loads((r/'INPUTS.json').read_text()):
 b=(r/v['local_path']).read_bytes()
 ck(v['label']+' sha256',hashlib.sha256(b).hexdigest()==v['sha256'])
 ck(v['label']+' git blob',hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==v['git_blob'])
# Only this bounded universal representation model is executed.
exec((r/'inputs/model.py').read_text())
def pol(v,n):return sum(v[i]*x**(n-i)*y**i for i in range(n+1))
def tv(a,f,k):return s.expand(sum((-1)**j*comb(k,j)*s.diff(a,x,k-j,y,j)*s.diff(f,x,j,y,k-j) for j in range(k+1)))
f12=-2*x**12-s.Rational(44,5)*z*x**10*y**2+66*x**8*y**4+s.Rational(88,5)*z*x**6*y**6+66*x**4*y**8-s.Rational(44,5)*z*x**2*y**10-2*y**12
f8=[tv(f12,pol(E[:,j],6),5) for j in range(4)]
U8=s.Matrix.hstack(*[cv(-tv(a*a,f,4)/20,4) for f in f8])
def flat(M):return s.Matrix([s.expand(e).coeff(p,i).coeff(q,j).coeff(t,2-i-j) for e in M for i in range(3) for j in range(3-i)])
k5=6131220480*z
ck('Sym5 channel exact gate coefficients',all(s.simplify(e)==0 for e in flat(U8)-k5*flat(R1-4*R2)))
# General Spencer matrix row conventions quartic output input indices.
Sp=s.Matrix.hstack(*[s.Matrix.vstack(*[cv(x*x**(4-i)*y**i*int(j==k+1)-y*x**(4-i)*y**i*int(j==k),5) for k in range(4)]) for i in range(5) for j in range(5)])
ck("Spencer rank24",Sp.rank()==24)
Us=[]
for f in f8:
 target=s.Matrix.vstack(*[cv(tv(f12,tv(x**(3-k)*y**k,f,2),7),5) for k in range(4)])
 sol=next(iter(s.linsolve((Sp,target))))
 free=set().union(*(v.free_symbols for v in sol)); sol=[v.subs({v:0 for v in free}) for v in sol]
 # scalar adjustment to trace zero gives canonical equivariant inverse
 U=s.Matrix(5,5,sol);U-=s.trace(U)*s.eye(5)/5
 ck("Spencer full coefficient inverse "+str(len(Us)),Sp*s.Matrix(list(U))==target)
 Us.append(U)
U7=s.Matrix.hstack(*[U*cv(a*a,4) for U in Us])
k7=-78316384529940480000
ck('Sym7 T channel exact gate coefficients',all(s.simplify(e)==0 for e in flat(U7)-k7*flat(3*R1+2*R2)))

Vpol=[pol(v,6) for v in Pi.nullspace()]
wr=s.expand(s.Matrix([[s.diff(f.subs(y,1),x,k) for f in Vpol] for k in range(3)]).det())
ck('invariant f12 is exact pinned Wronskian',s.expand(s.Poly(wr,x).homogenize(y).as_expr()-f12)==0)
E8=s.Matrix.hstack(*[cv(f,8) for f in f8]);ck('nonzero equivariant P8 inclusion rank4',E8.rank()==4)
J7=s.Matrix.hstack(*[cv(tv(f12,x**(7-i)*y**i,7),5) for i in range(8)])
ck('Sym7 to T projection rank6',J7.rank()==6)
C5=s.Matrix.hstack(*[cv(tv(x**(3-i)*y**i,f,3),5) for i in range(4) for f in f8])
C7=s.Matrix.hstack(*[cv(tv(f12,tv(x**(3-i)*y**i,f,2),7),5) for i in range(4) for f in f8])
ck('individual cubic channel ranks6',C5.rank()==6 and C7.rank()==6)
ck('joint cubic channel rank12',C5.col_join(C7).rank()==12)
ck('channel line determinant14',s.Matrix([[1,3],[-4,2]]).det()==14)
ck('all36 octavic Spencer transvectant identities',all(s.expand(x*tv(y*x**(3-i)*y**i,x**(8-j)*y**j,4)-y*tv(x*x**(3-i)*y**i,x**(8-j)*y**j,4)+20*tv(x**(3-i)*y**i,x**(8-j)*y**j,3))==0 for i in range(4) for j in range(9)))
ck('gate basis is independent',s.Matrix.hstack(flat(R1),flat(R2)).rank()==2)
print(json.dumps(dict(status='PASS',count=len(checks),checks=checks,Sym5_line=[1,-4],Sym7_line=[3,2],Sym5_factor=str(k5),Sym7_factor=str(k7),scope='Universal full coefficients; actual graph and row scalars unselected'),indent=2))

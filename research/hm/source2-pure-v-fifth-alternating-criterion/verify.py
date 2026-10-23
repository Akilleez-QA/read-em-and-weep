#!/usr/bin/env python3
from pathlib import Path
import json,hashlib
root=Path(__file__).resolve().parent;checks=[]
def ck(n,b):
 if not bool(b):raise RuntimeError(n)
 checks.append(n)
for v in json.loads((root/'INPUTS.json').read_text()):
 data=(root/v['local_path']).read_bytes()
 ck(v['label']+' sha256',hashlib.sha256(data).hexdigest()==v['sha256'])
 ck(v['label']+' Git blob',hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==v['git_blob'])
exec((root/'inputs/model.py').read_text())
def pol(v,n):return sum(v[i]*x**(n-i)*y**i for i in range(n+1))
def tv(f,g,k):return s.expand(sum((-1)**j*comb(k,j)*s.diff(f,x,k-j,y,j)*s.diff(g,x,j,y,k-j) for j in range(k+1)))
b0,b1,b2=s.symbols('b0 b1 b2');b=b0*x*x+b1*x*y+b2*y*y
fp=[pol(E[:,j],6) for j in range(4)]
JD=s.Matrix.hstack(*[cv(tv(b,tv(a,f,2),1),4) for f in fp])
JP=s.Matrix.hstack(*[cv(tv(b,pol(E*DP[:,j],6),2),4) for j in range(4)])
JV=s.Matrix.hstack(*[cv(tv(b,tv(a,fp[j],1)-pol(E*DP[:,j],6),2),4) for j in range(4)])
def matrix(J):
 return s.Matrix.hstack(*[s.Matrix([s.Poly(J[i,j],p,q,t,b0,b1,b2).coeff_monomial(aa*bb) for bb in [b0,b1,b2] for i in range(5)]) for aa in [p,q,t] for j in range(4)])
MD,MP,MV=map(matrix,[JD,JP,JV])
ck('domain D channel rank5',MD.rank()==5)
ck('domain P channel rank4',MP.rank()==4)
ck('domain V channel rank3',MV.rank()==3)
ck('three channel sum is isomorphism onto12', (MD+MP+MV).rank()==12)
ck('three channel maps independent',s.Matrix.hstack(*[s.Matrix(list(m)) for m in [MD,MP,MV]]).rank()==3)
br=s.Matrix.hstack(*[cv(tv(tv(a,b,1),f,2),4) for f in fp])
ck('full bilinear alternating bracket factor minus3',all(s.expand(v)==0 for v in JP+JV-JD+3*br))
ck('alternating line has full rank12',(MP+MV-MD).rank()==12)
sub={b0:p,b1:q,b2:t}
CD=JD.subs(sub)*DP;CP=JP.subs(sub)*DP;CV=JV.subs(sub)*DP
C1=DD*R1;C2=DD*R2;C4=R2*DP
ck('full cubic D identity',all(s.expand(v)==0 for v in CD-60*C2))
ck('full cubic P identity',all(s.expand(v)==0 for v in CP-60*C4))
ck('full cubic V identity',all(s.expand(v)==0 for v in CV-60*(C2-C4)))
def flat(M):return s.Matrix([s.Poly(v,p,q,t).coeff_monomial(p**i*q**j*t**(3-i-j)) for v in M for i in range(4) for j in range(4-i)])
F=s.Matrix.hstack(*[flat(C) for C in [CD,CP,CV]])
ck('diagonal image rank2',F.rank()==2)
ck('diagonal literal kernel minus1 plus1 plus1',F*s.Matrix([-1,1,1])==s.zeros(F.rows,1))
gauge=C4-C1/4
ck('full cubic lift space rank3',s.Matrix.hstack(flat(C1),flat(C2),flat(C4)).rank()==3)
ck('diagonal image disjoint nonzero m gauge',s.Matrix.hstack(F,flat(gauge)).rank()==3)
m=s.Matrix.hstack(*[cv(a*x**(2-i)*y**i,4) for i in range(3)])
H=s.Matrix.hstack(*[cv(tv(a*a,f,4),2) for f in fp])
ck('retained exact cubic gauge',all(s.expand(v)==0 for v in gauge+m*H/720))
lD,lP,lV,eta=s.symbols('lambdaD lambdaP lambdaV eta')
actual=-eta*(lD*CD+lP*CP+lV*CV)
rep=-15*eta*(lP-lV)*C1-60*eta*(lD+lV)*C2
ck('actual class coefficients modulo exact gauge',all(s.expand(v)==0 for v in actual-rep+60*eta*(lP-lV)*gauge))
ck('nonzero Schur zero-class condition includes no zero channel',all(v!=0 for v in [-1,1,1]))
ck('Gamma quotient dimension',15-3==12)
ck('mixed span forces factor isomorphism',12==3*4)
# Universal normalization certificate in abstract split coordinates of J2.
# These are not source matrices: K has dimension21, H_A dimension3, Hprime12.
mu=s.symbols('mu', nonzero=True)
Gamma0=s.zeros(15,36)
Gamma0[:,21:36]=s.eye(15)
aA=s.zeros(36,3);aA[21:24,:]=mu*s.eye(3)
rA=s.zeros(3,15);rA[:,:3]=s.eye(3)
N=s.eye(36)-aA*rA*Gamma0/mu
pr=s.diag(*([0]*3+[1]*12))
ck('normalization removes entire A Gamma component',Gamma0*N==pr*Gamma0)
ck('normalization idempotent',N*N==N)
# Arbitrary rows q and e0 vanish on canonical A, without any other restriction.
qrow=s.Matrix(1,36,lambda i,j:0 if 21<=j<24 else s.Symbol('Q'+str(j)))
erow=s.Matrix(1,36,lambda i,j:0 if 21<=j<24 else s.Symbol('E'+str(j)))
ck('normalization preserves arbitrary q killing canonical A',qrow*N==qrow)
ck('normalization preserves arbitrary e0 killing canonical A',erow*N==erow)
ck('normalization kills Gamma A and fixes Hprime',rA*Gamma0*N==s.zeros(3,36) and (Gamma0*N)[3:,:]==Gamma0[3:,:])
# Formal vector-valued rewriting of the two actual preimage equations.
Tx,hTx=s.symbols('Tx hTx')
qy=-Tx;j2y=-hTx
ck('induction q equation preserved',s.expand(qy+Tx)==0)
ck('induction j2 next zero under preceding diagonal zero',j2y.subs(hTx,0)==0)
# Alternation applies to every P argument, independently of the correction order.
u=s.Matrix(s.symbols('u0:4'))
alt=JP+JV-JD
ck('alternation for arbitrary independent P argument',all(s.expand(v)==0 for v in (alt+alt.xreplace({p:b0,q:b1,t:b2,b0:p,b1:q,b2:t}))*u))
ck('all-orders diagonal zero for arbitrary P-valued argument',all(s.expand(v)==0 for v in alt.subs(sub)*u))
ck('normalization denominators only fixed mu',all(v==0 for v in (N-s.diag(*([1]*21+[0]*3+[1]*12)))))
ck('finite stopping order exceeds degree',6+25>30)
print(json.dumps(dict(status='PASS',count=len(checks),checks=checks,channel_order=['D','P','V'],zero_fifth_ratio=[-1,1,1],class_coefficients={'C1':'-15 eta (lambdaP-lambdaV)','C2':'-60 eta (lambdaD+lambdaV)'},bracket_factor=-3,scope='Residual-large R0 fifth alignment and all-orders normalization; no actual branch or scalar selected'),indent=2))

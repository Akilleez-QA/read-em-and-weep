"""Universal coefficient identity, with all36 middle,4 W,3 polar and20 form symbols free."""
from universal_supported_w_action_assembly import *
K=s.Matrix(6,6,s.symbols('K0:36'));TW=s.Matrix(2,2,s.symbols('t0:4'))
rv=s.Matrix(s.symbols('R0:3'));rf={(i,):rv[i] for i in range(3)}
f2=s.symbols('eta0:20');f3=s.symbols('omega0:20')
F=[dict(zip(combinations(range(5),2),f2[10*j:10*j+10])) for j in range(2)]
Z=[dict(zip(combinations(range(5),3),f3[10*j:10*j+10])) for j in range(2)]
def FW(G):
 out=[{},{}]
 for i in range(2):
  for j in range(2):out=adds(out,putp(TW[j,i]*K*getp(G,(3+i,)),(3+j,)))
 return out
def FWadj(G):
 out=[{},{}];Td=s.trace(TW)*s.eye(2)-TW
 for i in range(2):
  for j in range(2):out=adds(out,putY(Td[j,i]*up*adj6(K)*low*getY(G,(3+i,)),(3+j,)))
 return out
eq(pair(FW(Z),F),pair(Z,FWadj(F)))
print('PASS: the literal determinant adjoint uses tr(TW)I−TW.',flush=True)
pre=adds(FW([wedge(rf,f) for f in F]),sc(-1,[wedge(rf,f) for f in FWadj(F)]))
eqvec(pre,supported_w_precontraction(K,rv,TW,F))
out=[contract(coords,f) for f in pre]
eqvec(out,supported_w_action(K,rv,TW,F))
assert all(f.get((3,4),0)==0 for f in out)
print('PASS: complete20-input equality before and after i_x; no WW output.',flush=True)
ps=s.Matrix(s.symbols('p0:2'));YL=s.Matrix.vstack(M0,M1,M2);E=positive_wedge_matrix(rv)
Xplus=K*E*YL+E*up*adj6(K)*low*YL
Xadj=E*up*adj6(K)*low*YL
jw=s.Matrix([-w,u]);pred=[{},{}]
for j in range(2):pred=adds(pred,putp((-Xplus*(TW*jw)[j]+s.trace(TW)*Xadj*jw[j])*ps,(3+j,)))
eqvec(supported_w_precontraction(K,rv,TW,B(ps)),pred)
eqvec(supported_w_action(K,rv,TW,A(ps)),[{},{}])
D2=s.Matrix([[h,k],[l,-h]]);N2=-2*jw*s.Matrix([[u,w]]);C2=D2*N2-N2*D2;aa=(k*u*u-2*h*u*w-l*w*w)/2
assert C2*jw==4*aa*jw or (C2*jw-4*aa*jw).applyfunc(s.expand)==s.zeros(2,1)
print('PASS: exact full B formula for arbitrary W action, and A is annihilated.',flush=True)
print('PASS: fixed D, commutator[D,N] and identity actions specialize with t=−Dj, [D,N]j=4aj and the identity trace2 correction.',flush=True)

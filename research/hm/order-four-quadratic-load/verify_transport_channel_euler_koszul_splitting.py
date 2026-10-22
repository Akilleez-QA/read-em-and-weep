"""Universal Euler/Koszul channel splitting, no actual-instance evaluation."""
import sympy as S
from pathlib import Path
import runpy,contextlib,io
x=S.symbols('a0:3'); av=S.Matrix(x)
def generic(tag,d):
    mons=[x[0]**i*x[1]**j*x[2]**(d-i-j) for i in range(d+1) for j in range(d+1-i)]
    return sum(c*m for c,m in zip(S.symbols(tag+':'+str(len(mons))),mons))
def grad(f):return S.Matrix([S.diff(f,z) for z in x])
def div(F):return sum(S.diff(F[i],x[i]) for i in range(3))
def curl(F):return S.Matrix([S.diff(F[2],x[1])-S.diff(F[1],x[2]),S.diff(F[0],x[2])-S.diff(F[2],x[0]),S.diff(F[1],x[0])-S.diff(F[0],x[1])])
def zero(v):assert v.applyfunc(S.expand)==S.zeros(3,1)
T=S.Matrix([generic('T'+str(i)+'_',3) for i in range(3)])
Q=av.dot(T);R=-curl(T)/4
zero(av.cross(curl(T))-grad(Q)+4*T)
zero(T-grad(Q)/4-av.cross(R));assert S.expand(div(R))==0
Rq=S.Matrix([generic('R'+str(i)+'_',2) for i in range(3)])
zero(curl(av.cross(Rq))-av*div(Rq)+4*Rq)
ell=generic('ell_',1);assert S.expand(div(av*ell)-4*ell)==0
Q4=generic('Q_',4);assert S.expand(av.dot(grad(Q4))/4-Q4)==0
with contextlib.redirect_stdout(io.StringIO()):
    ch=runpy.run_path(str(Path(__file__).with_name('verify_pure_cross_block_couplings.py')))
add,vm,inn=ch['add'],ch['vm'],ch['inner']
one,A,V,P=ch['one'],ch['A'],ch['V'],ch['P'];D=ch['sy'](4)
from functools import reduce
def plus(*args):return [reduce(add,col) for col in zip(*args)]
S2=plus(one,D);S3=plus(A,V,P);S4=plus(one,P,D,D)
assert vm(S2,A)==plus(A,A,V,P,D)
assert inn(vm(vm(P,A),S3),D)==10
assert inn(vm(P,S4),D)==5
assert inn(vm(vm(P,A),S2),D)==6
assert inn(vm(P,A),D)==1
assert inn(vm(A,S2),D)==1
assert 6-1==5 and 10-(5-1)==6
print('PASS: full free-coefficient Euler/curl decomposition and unique divergence-free Koszul preimage.')
print('PASS: exact ten= five+five and final six= five+one channel arithmetic.')
print('No actual coefficient or fourth value is determined.')

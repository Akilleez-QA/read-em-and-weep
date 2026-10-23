"""Exact all234-coefficient representative-change transport, both source ends.

The full middle identity is checked before applying exterior contraction, in
the18 coordinates (mixed12,VWW6). This retains both higher weights, every
derivative of the physical positive-linear B, and the marking units.
"""
from time import monotonic
from universal_q_middle_quotient_coefficients import *
from universal_q_middle_completion_transport import homogeneous_partner
from universal_graded_c_orthogonal_module import graded_module

start=monotonic()
def eq(a,b):assert s.cancel(s.expand(a-b))==0,s.factor(a-b)
def meq(A,B):
    assert A.shape==B.shape
    for a,b in zip(A,B):eq(a,b)
def report(t):print('PASS: '+t+' [%.1fs]'%(monotonic()-start),flush=True)

m=graded_module();C,R,D,Zeta=(m[k] for k in ('C','R','D','Zeta'))
vs=(x,y,z);kap,cm,theta=s.symbols('boundary_kappa boundary_cm boundary_theta',nonzero=True)
q=(x*y+z*z)/theta
cs=s.symbols('boundary_linear_leg0:36')
l=s.Matrix([sum(cs[3*i+j]*v for j,v in enumerate(vs)) for i in range(12)])
partner=homogeneous_partner(l,1)['Z']
Ps=[partner.jacobian([cs[3*i+j] for i in range(12)]) for j in range(3)]
Z1=lambda Y:sum((P*Y.diff(v) for P,v in zip(Ps,vs)),s.zeros(6,Y.cols))
meq(Z1(l),partner)
for P in Ps:meq(P*C,s.zeros(6,3))
ZQ=sum((P*s.diff(q,v)/2 for P,v in zip(Ps,vs)),s.zeros(6,12))
for j in range(12):meq(ZQ[:,j],homogeneous_partner(q*s.eye(12)[:,j],2)['Z'])
report('literal homogeneous partners give exact differential matrices; all12 q-column partners and all C-source annihilations checked')

B=s.Matrix(12,12,lambda i,j:sum(s.Symbol('boundary_B_%s_%s_%s'%(a,min(i,j),max(i,j)))*v for a,v in enumerate(vs)))
data=project_physical_coefficient(B);M,N,F=(data[k] for k in ('M','N','L'))
delta=B-data['representative']
meq(delta,data['difference'])
ZB=Z1(delta);ZMt=Z1(M.T)
meq(ZB,ZMt*C.T)
meq(Z1(F),ZMt)
Q=(q*s.eye(12)).col_join(-kap*ZQ)
Ldelta=delta.col_join(-kap*ZB)
Cfull=C.col_join(s.zeros(6,3))
Hmt=M.T.col_join(-kap*ZMt)
H=(Q*M.T+q*Hmt-q*Cfull*N)/2
meq(Q*C,q*Cfull)
meq(H[:12,:],q*F)
meq(H[12:,:],-kap*(ZQ*F+q*Z1(F))/2)
middle=(Ldelta*Q.T+Q*Ldelta.T)/2
boundary=Cfull*H.T+H*Cfull.T
meq(middle,boundary)
report('all234 free physical B coefficients: entire18x18 prescribed completion difference equals the explicit C-source factor, including both higher weights and every derivative')

# The public exported boundary adapter agrees with the same explicit formula.
# Its argument is one wholly free linear leg; this covers each F column.
c=C*s.Matrix(s.symbols('boundary_c_label0:3'))
public=completed_C_factor_boundary(c,l,q,cm)
meq(public['Hmixed'],q*l)
meq(public['Hpartner'],(ZQ*l+q*Z1(l))/2)
eq(public['source_homotopy_scale'],1/cm)
report('public completed_C_factor_boundary keeps the required half, q0 scaling, full derivative partners, and nonzero1/cm')

# All full source endpoint corrections, with the fixed negative-dual sign.
# alpha is wholly formal; isotropy is applied only after exposing its residual.
J=s.Matrix([[0,0,1,0],[0,0,0,1],[-1,0,0,0],[0,-1,0,0]])
alpha=s.Matrix(4,3,lambda i,j:s.Symbol('boundary_alpha_%s_%s'%(i,j)))
beta=alpha.T*J
source=s.Matrix(s.symbols('boundary_source_label0:3'))/cm
leg=s.Matrix(s.symbols('boundary_full_leg0:4'))
h=source*leg.T*J;hd=leg*source.T
P=h*alpha;Pd=beta*hd;Tmiddle=alpha*h+hd*beta
meq(Pd,-P.T)
meq(Tmiddle*alpha-alpha*P,hd*(beta*alpha))
meq(beta*Tmiddle-Pd*beta,(beta*alpha)*h)
meq(Tmiddle.T*J+J*Tmiddle,s.zeros(4))
report('both full source ends P=h alpha and Pd=beta hd=-P^t are exact; both chain residuals are displayed multiples of beta alpha before isotropy')
print('No source columns, actual-instance system, source solve, lower-only quotient, equivariant section, or obstruction conclusion is used.',flush=True)

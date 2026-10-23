"""Explicit generating set for all 54 Rq and 10 Rh identity-W coefficient channels.
The Rq list is intentionally redundant; no actual-instance rank is evaluated.
"""
from universal_complete_identity_w_spin_symbols import *

def sextic(R):
 cc=[R[0,3]/6,-R[0,2],5*R[0,1]/2,-10*R[0,0]/3,-5*R[1,0]/6,-R[2,0]/3,-R[3,0]/6]
 return s.expand(sum(c*m for c,m in zip(cc,mon(6))))

def quadratic(R):
 return s.expand(R[0,1]*S*S-2*R[0,0]*S*T/3-R[1,0]*T*T/3)

def marked_twelve(f):
 qe,qf,qh=[sextic(f*R*f.inv()) for R in (binary_E,binary_F,binary_H)]
 return s.expand(qh*qh/20+qe*qf/5)

def negative_casimir(f,R):
 E0,F0,H0=[f*A*f.inv() for A in (binary_E,binary_F,binary_H)]
 return comm(H0,comm(H0,R))/4+(comm(E0,comm(F0,R))+comm(F0,comm(E0,R)))/2

def split_six(f,p):
 R=op6(p);RA=(12*R-negative_casimir(f,R))/10
 return [('A',sextic(RA)),('P4',sextic(R-RA))]

def typed_outputs(f,g12,p,degree):
 if degree==0:return [('1',p)]
 if degree==2:return [('V',p)]
 if degree==4:return [('D5',p)]
 if degree==6:return split_six(f,p)
 if degree==8:return [('D5',tv(g12,p,8)),('P4',tv(g12,p,7))]
 if degree==10:return [('V',tv(g12,p,10)),('D5',tv(g12,p,9)),('A',tv(g12,p,8))]
 raise ValueError(degree)

def coefficient_embeddings(kind,p):
 out=[]
 def cc(R):
  Q=s.zeros(6);Q[:4,:4]=R;return Q
 def cs(R):
  Q=s.zeros(6);Q[:4,4:]=R;return Q
 def sc0(R):
  Q=s.zeros(6);Q[4:,:4]=(-J1/3).inv()*R.T*(-J3/2);return Q
 if kind=='1':return [('C_scalar',cc(p*s.eye(4))),('S_scalar',spin_block(p*s.eye(2)))]
 if kind in ('A','P4'):return [('C_'+kind,cc(op6(p)))]
 if kind=='V':
  mix=s.Matrix.hstack(*[coeff(p*z,3) for z in mon(1)])
  return [('C_V',cc(op2(p))),('S_V',spin_block(op2spin(p))),('CS_V',cs(mix)),('SC_V',sc0(mix))]
 if kind=='D5':
  mix=mixed5(p)
  return [('C_D5',cc(op4(p))),('CS_D5',cs(mix)),('SC_D5',sc0(mix))]
 raise ValueError(kind)

def negative_inputs(f):
 d=k*S*S-2*h*S*T-l*T*T;n=(-w*S+u*T)**2
 tr=lambda R:f*R*f.inv()
 A1=tr(op2(d*tv(d,n,2)));A2=tr(op2(n*tv(d,d,2)))
 D4=tr(op4(tv(d*d,n,1)));Q6=tr(op6(d*d*n))
 V6=(12*Q6-casimir(Q6))/10;P6=Q6-V6
 return [('A_first','A',sextic(A1),6),('A_second','A',sextic(A2),6),
         ('V_sextic','V',quadratic(V6),2),('P4_sextic','P4',sextic(P6),6),
         ('D5_quartic','D5',quartic(D4),4)]

def build_complete_identity_w_coefficients(f,H0):
 """Return87 Rq generators spanning54 channels and10 Rh basis coefficients.
 f is the actual G-equivariant cubic marking, with all scales unassigned.
 Every output is a balanced Cartan4+Spin2 coefficient for identity-on-W.
 """
 g12=marked_twelve(f);qh=quartic(H0);rq=[];rh=[]
 for name,kind,p,degree in negative_inputs(f):
  for label,M in coefficient_embeddings(kind,p):rh.append((name+'_'+label,M))
  for order in range(min(4,degree)+1):
   product=tv(qh,p,order);outdegree=4+degree-2*order
   for outkind,q in typed_outputs(f,g12,product,outdegree):
    for label,M in coefficient_embeddings(outkind,q):
     rq.append((name+'_tv'+str(order)+'_'+label,M))
 assert len(rq)==87 and len(rh)==10
 return rq,rh

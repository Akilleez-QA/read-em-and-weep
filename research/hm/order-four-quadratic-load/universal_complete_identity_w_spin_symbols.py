"""Seven universal identity-W Spin-to-Spin coefficient symbols.
No family solve or actual-coefficient evaluation. Six Rq symbols and one Rh.
"""
from universal_source_balance_helpers import *

# Canonical positive cubic Clebsch frame, extracted from the full polynomial A(v)r.
r0,r1=s.symbols('positive_r0 positive_r1'); rr=s.Matrix([r0,r1])
Ap=s.Matrix.hstack(*[extract*getp(A(s.eye(2)[:,j])) for j in range(2)])
pure=Ap.subs({x:r0*r0,y:-r1*r1,z:-r0*r1},simultaneous=True)*rr
Pstd=s.Matrix.hstack(*[s.Matrix([s.Poly(e,r0,r1).coeff_monomial(r0**(3-j)*r1**j) for e in pure])/s.binomial(3,j) for j in range(4)])

def comm(A,B):return A*B-B*A

def casimir(R):
 return comm(binary_H,comm(binary_H,R))/4+(comm(binary_E,comm(binary_F,R))+comm(binary_F,comm(binary_E,R)))/2

def op2(p):return rep(lambda z:tv(p,z,1)/2,3)
def op2spin(p):return s.Matrix([[ -s.diff(p,S,T)/2,s.diff(p,S,2)/2],[-s.diff(p,T,2)/2,s.diff(p,S,T)/2]])

def spin_from_rank_one(R):
 return s.Matrix([[R[0,0]/3,R[0,1]],[R[1,0]/3,-R[0,0]/3]])

def positive_h6(H0):
 Q=Pstd*H0*Pstd.inv()
 vals={ha:-Q[0,0],hf:Q[0,1]/2,hd:-Q[0,2],hc:3*Q[1,0]/2,hb:-3*Q[2,0]}
 return HH.subs(vals,simultaneous=True)

def partial_spin(H0,R):
 Q=positive_h6(H0)*Kinc*Pstd*R*Pstd.inv()*extract
 return sum((Q[2*i:2*i+2,2*i:2*i+2] for i in range(3)),s.zeros(2))

def spin_block(Q):
 out=s.zeros(6);out[4:,4:]=Q
 return out

def build_identity_w_spin_symbols(f,H0):
 """f maps negative cubic monomials into the canonical positive cubic frame.
 H0 is the actual positive quartic endomorphism in that frame.
 The returned matrices use Cartan-four plus Spin-two balanced coordinates.
 """
 d=k*S*S-2*h*S*T-l*T*T;n=(-w*S+u*T)**2
 transport=lambda R:f*R*f.inv()
 R1=transport(op2(d*tv(d,n,2)))
 R2=transport(op2(n*tv(d,d,2)))
 R4=transport(op4(tv(d*d,n,1)))
 R6=transport(op6(d*d*n))
 V6=(12*R6-casimir(R6))/10
 P6=R6-V6
 QH=quartic(H0);Q4=quartic(R4)
 rq=[('SS_A_first',partial_spin(H0,R1)),
     ('SS_A_second',partial_spin(H0,R2)),
     ('SS_D5_scalar',partial_spin(H0,R4)),
     ('SS_D5_vector',op2spin(tv(QH,Q4,3))),
     ('SS_V_sextic',partial_spin(H0,V6)),
     ('SS_P4_sextic',partial_spin(H0,P6))]
 rh=[('SS_V_sextic_probe',spin_from_rank_one(V6))]
 return [(name,spin_block(Q)) for name,Q in rq],[(name,spin_block(Q)) for name,Q in rh]

if __name__=='__main__':
 q=s.symbols('universal_quartic0:5'); H0=op4(sum(c*m for c,m in zip(q,mon(4))))
 zero_matrix(Pstd.inv()*extract*positive_h6(H0)*Kinc*Pstd-H0)
 for order,Q in [(1,op2(S*S)),(2,op4(S**4)),(3,op6(S**6))]:
  zero_matrix(casimir(Q)-order*(order+1)*Q)
  Z=partial_spin(H0,Q)
  assert any(s.expand(v)!=0 for v in Z)
  if order==2:zero_matrix(Z-s.eye(2)*s.trace(Z)/2)
  else:assert s.expand(s.trace(Z))==0
 print('PASS: positive Clebsch normalization, Casimir eigenvalues, and all three partial-trace channel maps are nonzero universal polynomial identities.')

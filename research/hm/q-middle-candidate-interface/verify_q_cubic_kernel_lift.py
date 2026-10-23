"""Free-symbol exact lower-middle q correction, not a completed-source solve."""
from universal_q_cubic_kernel_lift import *

# Every coefficient of a completely free quadratic residual stays formal.
mons=[x*x,x*y,x*z,y*y,y*z,z*z]
r=s.Matrix([sum(c*p for c,p in zip(s.symbols(f'free_symmetric_residual_{i}_0:6'),mons)) for i in range(3)])
B=symmetric_linear_inverse(r)
assert (B-B.T).applyfunc(s.expand)==s.zeros(3)
assert (B*positive-r).applyfunc(s.expand)==s.zeros(3,1)
print('PASS: explicit symmetric linear inverse for all18 independent formal quadratic RHS coefficients.',flush=True)

# Complete homogeneous syzygies in degree2, with all9 potential coefficients.
h=s.Matrix([sum(c*v for c,v in zip(s.symbols(f'free_skew_potential_{i}_0:3'),positive)) for i in range(3)])
r=KOSZUL2*h;B=skew_linear_inverse(r)
assert (B+B.T).applyfunc(s.expand)==s.zeros(3)
assert (B*positive-r).applyfunc(s.expand)==s.zeros(3,1)
print('PASS: exact skew linear inverse for the full quadratic Koszul-syzygy module.',flush=True)

# All eight leg-square/cross terms with all three positive-linear coefficients
# remain independent formal symbols; no family coefficient is selected.
G=standard_q_orthogonal_legs();K=s.zeros(8)
for i in range(8):
 for j in range(i,8):
  K[i,j]=K[j,i]=sum(c*v for c,v in zip(s.symbols(f'free_q8_coefficient_{i}_{j}_0:3'),positive))
T=G*K*G.T
out=q_cubic_lift(T,known_defect=G*K[:,:3])
assert (out['exact']+quadratic*out['correction']-T).applyfunc(s.expand)==s.zeros(12)
print('PASS: all108 free positive-linear coefficients of Sym²(A+D5) have a literal physical T=T_exact+q B decomposition, with B symmetric linear and T_exact C=0.',flush=True)

# Actual q0=quadratic/theta differs by its retained invariant-frame unit.
theta=s.symbols('free_positive_quadratic_frame',nonzero=True)
assert ((quadratic/theta)*(theta*out['correction'])-quadratic*out['correction']).applyfunc(s.expand)==s.zeros(12)
print('PASS: invariant quadratic-frame unit retained: q0=q/theta uses correction theta B, never theta=1.',flush=True)

m=graded_module()
c=s.Matrix(s.symbols('free_q_leg_C0:3'))
a=s.Matrix(s.symbols('free_q_leg_A0:4'))
b=s.Matrix(s.symbols('free_q_leg_D0:5'))
rho=s.Matrix(s.symbols('free_q_leg_new0:3'))
yy=m['C']*(x*c)+m['Acoeff']*a+m['Y']*b+G[:,:3]*rho
rr=reconstruct_q_leg(yy,1)
assert (rr['A_new']-rho).applyfunc(s.expand)==s.zeros(3,1)
print('PASS: complete q-orthogonal leg reconstruction retains the actual C and A source shifts plus all3 new q-pairing and5 exact coefficients.',flush=True)
print('No claim that q B may be discarded from the full cochain: its full-U completion, divided-arrow change, source ends and C,C anomaly remain required.',flush=True)
print('No points, actual coefficient/marking assignments, instance ranks, broad family solve, frozen edits, or external writes.',flush=True)

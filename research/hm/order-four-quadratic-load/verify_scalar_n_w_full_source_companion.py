from universal_supported_w_action_assembly import *
rv=s.Matrix(s.symbols('rp0:3'));rf={(i,):rv[i] for i in range(3)}
j=s.Matrix([-w,u]);jform={(3,):-w,(4,):u};N=-2*j*s.Matrix([[u,w]])
coeffs=s.symbols('p3_0:20');G3=[dict(zip(combinations(range(5),3),coeffs[10*i:10*i+10])) for i in range(2)]
F=[contract(coords,f) for f in G3];vv=putp(getp(F));ivvv=[contract([x,y,z,0,0],f) for f in vv]
rho=rv.dot(s.Matrix([x,y,z]))
pred=sc(-4*rho,[wedge(f,jform) for f in ivvv])
eqvec(supported_w_action(s.eye(6),rv,N,F),pred)
eqvec(supported_w_action(s.eye(6),rv,N,A(p)),[{},{}])
eqvec(supported_w_action(s.eye(6),rv,N,B(p)),[{},{}])
print('PASS: scalar-N full source formula for every closed two-form; A and B annihilated.')
print('rho physical',s.factor(sum(r[i]*coords[i] for i in range(3))))
D2=s.Matrix([[h,k],[l,-h]])
Delta=s.trace(D2*D2)/2
assert s.expand(Delta-h*h-k*l)==0
rhoH=s.expand(sum(rh[i]*coords[i] for i in range(3)))
assert s.expand(rhoH-(ha*x*y+hb*x*x/2+hd*y*y/2+2*hc*x*z+2*hf*y*z-2*ha*z*z)/theta)==0
assert s.expand(sum(r[i]*coords[i] for i in range(3))-phys)==0
# The inverse-metric trace character distinguishes rhoH from q0.
assert s.expand(4*s.diff(rhoH,x,y)+s.diff(rhoH,z,2))==0
assert s.expand(4*s.diff(phys,x,y)+s.diff(phys,z,2))==6/theta
print('PASS: the q-polar branch has an explicit q0 factor; the H-polar branch has the discriminant factor Delta=h²+kl and a trace-free positive quadratic.')
print('No operator-independence, source-quotient nonzero or fourth-value claim.')

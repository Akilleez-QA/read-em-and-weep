from universal_supported_w_action_assembly import *
K=s.Matrix(6,6,s.symbols('kn0:36'))
rv=s.Matrix(s.symbols('rp0:3'))
j=s.Matrix([-w,u]); jf={(3,):-w,(4,):u};N=-2*j*s.Matrix([[u,w]])
cc=s.symbols('f3_0:20');G=[dict(zip(combinations(range(5),3),cc[i*10:i*10+10])) for i in range(2)]
F=[contract(coords,g) for g in G]
VV=putp(getp(F));iv=[contract([x,y,z,0,0],g) for g in VV]
# Convert the positive one-form with its U factor into the six-vector.
q=s.Matrix([iv[a].get((i,),0) for i in range(3) for a in range(2)])
# Use the assembler's own positive wedge and low/up conventions explicitly.
Er=positive_wedge_matrix(rv)
plus=K*Er+Er*up*adj6(K)*low
Gv=putp(plus*q)
expected=sc(-2,[wedge(contract([x,y,z,0,0],g),jf) for g in Gv])
eqvec(supported_w_action(K,rv,N,F),expected)
eqvec(supported_w_action(K,rv,N,A(p)),[{},{}])
eqvec(supported_w_action(K,rv,N,B(p)),[{},{}])
print('PASS: all36 K symbols, all20 closed-input coefficients, exact N-source formula and full A/B zero')
from universal_n_w_source_balanced_coefficients import *
eqvec(expected,n_w_closed_action(K,rv,F))
Jbalanced=s.diag(-J3/2,-J1/3)
zero_matrix(B6.T*J6*B6-Jbalanced)
Kphys=physical_six_coefficient(K)
zero_matrix(adj6(Kphys)-B6*Jbalanced.inv()*K.T*Jbalanced*B6inv)
eqvec(n_w_balanced_closed_action(K,rv,F),n_w_closed_action(Kphys,rv,F))
eqvec(n_w_balanced_closed_action(K,rv,F),supported_w_action(Kphys,rv,N,F))
Z=s.diag(1,1,1,1,0,0)
zero_matrix(physical_six_coefficient(Z)-Pi)
assert Z!=Pi
print("PASS: balanced-to-physical frame and all36-symbol adjoint transport; Cartan scalar maps to Pi.")
assert all(e==0 for e in getp(expected))
eqvec(n_w_closed_action(K,rv,expected),[{},{}])
FB,FC,FD=s.symbols('FB FC FD',nonzero=True)
f=s.Matrix([[0,0,FC,0],[-9*FB*FC/FD,0,0,0],[0,0,0,FD],[0,FB,0,0]])
qq=s.symbols('Hq0:5');qH=sum(c*m for c,m in zip(qq,mon(4)));H0=op4(qH)
d=k*S*S-2*h*S*T-l*T*T
zero_matrix(op4(quartic(f*op4(d*d)*f.inv()))-f*op4(d*d)*f.inv())
rq,rh=n_w_coefficients(f,H0)
for cat,items in [('Rq',rq),('Rh',rh)]:
    assert len({name for name,M in items})==len(items)
    for name,M in items:
        assert any(s.expand(z0)!=0 for z0 in M),name
        for e in M:
            for powers,c0 in s.Poly(e,h,k,l,*qq).terms():
                if c0:
                    assert sum(powers[:3])==2
                    assert sum(powers[3:])==(cat=='Rq')
        assert not any(e.has(u,w,x,y,z) for e in M)
        Mphys=physical_six_coefficient(M)
        zero_matrix(adj6(Mphys)-B6*Jbalanced.inv()*M.T*Jbalanced*B6inv)
print('PASS: all23 explicit N_W coefficients retain degree-two D input and the required H degree; f transport is exact.')
phi=(1+s.sqrt(5))/2
sizes=[1,15,20,12,12]
chars={'1':s.ones(5,1),'A':s.Matrix([3,-1,0,phi,1-phi]),'V':s.Matrix([3,-1,0,1-phi,phi]),'P4':s.Matrix([4,0,1,-1,-1]),'D5':s.Matrix([5,1,-1,0,0])}
end6=2*chars['1']+chars['A']+4*chars['V']+chars['P4']+3*chars['D5']
N0=chars['1']+chars['D5']
inner=lambda a0,b0:s.simplify(sum(n*a*b for n,a,b in zip(sizes,a0,b0))/60)
assert inner(N0,end6)==5
assert inner(chars['D5'].multiply_elementwise(N0),end6)==18
print('PASS: coefficient dimensions18+5; pairwise compositions vanish on closed inputs.')
print('No independence on the monad, source-quotient nonzero, completed source solution or fourth-value claim.')

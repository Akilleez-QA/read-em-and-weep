#!/usr/bin/env python3
"""Universal finite nilpotent and harmonic-order identities only."""
import sympy as S

f,g,df,dg,H,lam,s,ds,a,b,c,v1,v2=S.symbols(
    'f g df dg H lambda s Ds a b c v1 v2')
I=S.eye(2)
J=S.Matrix([[0,-1],[1,0]])
sigma=S.Matrix([f,g]); dsigma=S.Matrix([df,dg])
n=sigma*sigma.T*J
dn=dsigma*sigma.T*J+sigma*dsigma.T*J
A=S.Matrix([[a,b],[c,-a]])
E=H*dn+A*n-n*A-lam*n
F=I-s*n; Finv=I+s*n
dF=-ds*n-s*dn

def zero(expr):
    if isinstance(expr,S.MatrixBase):
        for entry in expr: zero(entry)
    else:
        assert S.expand(expr)==0,S.expand(expr)

zero(n*n);zero(F*Finv-I)
zero(n*E+E*n)
transport=F*A*Finv-H*dF*Finv
zero(transport-A-(H*ds+lam*s)*n-s*E-s*s*E*n)
zero(F*E*Finv-E-2*s*E*n)
zero(S.trace(transport))
print('PASS: exact finite connection and error transport, including quadratic terms.')

# Independent noncommutative bookkeeping of the q coefficient.
q,rho,lam1=S.symbols('q rho lambda1')
N,T,AA,K,DN,DT,R=S.symbols('n T A K Dn DT R',commutative=False)
BH_DN,BA_N,BN_A,Blam_N,BC_N=S.symbols(
    'B1_H_Dn B1_A_n B1_n_A B1_lambda_n B1_C_n',commutative=False)
derivative=DN+q*(DT+rho*T)
symbol_product=H*derivative+q*BH_DN
commutator=(AA+q*K)*(N+q*T)-(N+q*T)*(AA+q*K)+q*(BA_N-BN_A)
scalar_product=(lam+q*lam1)*(N+q*T)+q*Blam_N
error=S.expand(symbol_product+commutator-scalar_product)
expected_R=H*DT+(H*rho-lam)*T+AA*T-T*AA+K*N-N*K-lam1*N+BH_DN+BA_N-BN_A-Blam_N
zero(error.coeff(q,1)-expected_R)
C=H*ds+lam*s
product_C_N=C*N+q*(C*T+s*lam1*N+BC_N)
full_transformed=AA+q*K+product_C_N+s*q*R+s*s*q*R*N
expected_K=K+BC_N+C*T+s*lam1*N+s*R+s*s*R*N
zero(S.expand(full_transformed).coeff(q,1)-expected_K)
print('PASS: first-normal error and transformed coefficient retain every B1 and error term.')

V=S.Matrix([v1,v2]);w=f*v2-g*v1
tau=lambda vector:sigma*vector.T*J+vector*sigma.T*J
zero(n*V+w*sigma)
zero(tau(V)*n-w*n)
zero(F*V-V-s*w*sigma)
zero(tau(F*V)-tau(V)-2*s*w*n)
print('PASS: error transport equals the full Serre-vector transport with the positive scalar sign.')

nu,dnu,dT=S.symbols('nu Dnu DT_scalar',nonzero=True)
tt=S.symbols('T_scalar')
zero((dT/nu-tt*dnu/nu**2)+(rho+dnu/nu)*tt/nu-(dT+rho*tt)/nu)
print('PASS: physical equation-frame derivative correction cancels exactly.')
print('No actual source coefficients, rank tests, or normal extension are supplied.')

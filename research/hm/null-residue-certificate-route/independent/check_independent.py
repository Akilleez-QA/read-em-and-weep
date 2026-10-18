import sympy as s
x=s.symbols('x1:5'); a,b,c,d=x
u=a*b; v=c*d
p=(u+v)**2
F=2/u**3/v-1/u**2/v**2
G=-3/a/b**2-c*d/a**2/b**3-a/c**2/d**2
D=a**3*b**3*c**2*d**2*(1+a+b*c)
N=s.cancel(D*F); A=s.cancel(D*G)
s.Poly(N,*x); s.Poly(A,*x)  # Raises for a non-polynomial numerator.
check=s.expand(p*N*D-(D*s.diff(A,a)-A*s.diff(D,a)))
if check != 0: raise RuntimeError('m=1 certificate failed')
if s.Poly(A,*x).total_degree() > s.Poly(p*N,*x).total_degree()+1: raise RuntimeError('degree bound failed')
for j,z in enumerate(x):
    if s.degree(A,z)>s.degree(p*N,z)+(1 if j==0 else 0): raise RuntimeError('multidegree bound failed')
Nbad=s.cancel(D*(F+1/u**2/v**2))
if s.expand(p*Nbad*D-(D*s.diff(A,a)-A*s.diff(D,a))) == 0: raise RuntimeError('mutation accepted')
print({'invented_control':'passed','nonmonomial_denominator':True,'m':1,'deg_A':s.Poly(A,*x).total_degree(),'degree_bound':s.Poly(p*N,*x).total_degree()+1,'mutated_weighted_residue':2,'source_evaluations':0})

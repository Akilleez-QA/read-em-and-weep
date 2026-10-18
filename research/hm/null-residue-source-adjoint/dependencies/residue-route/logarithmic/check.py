import sympy as s
x,y,z,w=s.symbols('x y z w'); xs=(x,y,z,w)
C=1+x+y*z; D=x**2*y*z*w*C; N=C*(1+x**2)
h=x**2-1; A=C*x*h
checks={
 'tangent_to_C':s.expand(A*s.diff(C,x)-(x*h*s.diff(C,x))*C)==0,
 'weighted_Euler':s.expand(C*(x*s.diff(h,x)-h)-N)==0,
 'original_m1':s.expand(D*s.diff(A,x)-A*s.diff(D,x)-N*D)==0,
 'rational_divergence':s.cancel(s.diff(A/D,x)-N/D)==0,
 'negative_mutation_rejected':s.expand(D*s.diff(A,x)-A*s.diff(D,x)-(N+C*x)*D)!=0,
 'full_total_bound':s.Poly(A,*xs).total_degree()<=s.Poly(N,*xs).total_degree()+1,
}
# Incomplete family: C*x*d/dx cannot produce C*y; adding second field does.
D2=x*y*z*w*C; A2=C*y*y
checks['second_generator_succeeds']=s.expand(D2*s.diff(A2,y)-A2*s.diff(D2,y)-C*y*D2)==0
if not all(checks.values()): raise RuntimeError(checks)
print({'checks':checks,'invented_positive_residue':0,'invented_mutation_residue':1,'actual_source_evaluations':0})

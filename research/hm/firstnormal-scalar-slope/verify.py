import sympy as S
t=S.symbols('t');F=S.Function('F')(t);G=S.Function('G')(t);u=S.symbols('u');d=lambda x,n:S.diff(x,t,n)
n=[u*F*G,-u*F**2,u*G**2]
T=[u*(6*F*d(G,2)-16*d(F,1)*d(G,1)+20*d(F,2)*G)/112,u*(d(F,1)**2/5-3*F*d(F,2)/10),u*(5*G*d(G,2)/36-d(G,1)**2/9)]
c1=lambda degree:S.Rational(1,2*(degree-1))
c2=lambda degree:S.Rational(1,8*(degree-1)*(degree-3))
a1=[T[i]+c1(deg)*d(n[i],2) for i,deg in enumerate([8,6,10])]
a2=[c1(deg-4)*d(T[i],2)+c2(deg)*d(n[i],4) for i,deg in enumerate([8,6,10])]
d2=S.expand(a1[0]**2+a1[1]*a1[2]+2*n[0]*a2[0]+n[1]*a2[2]+n[2]*a2[1])
jets={d(F,j):S.Symbol('F'+str(j)) for j in range(4)}; jets.update({d(G,j):S.Symbol('G'+str(j)) for j in range(6)})
out=S.factor(d2.xreplace(jets).subs(S.Symbol('F0'),0)); print(out)
expected=u**2*S.Symbol('G0')**2*(3*S.Symbol('F2')**2-8*S.Symbol('F1')*S.Symbol('F3'))/48
assert S.expand(out-expected)==0
print('PASS free-jet identity; no form coefficients or points assigned')
# Independently check the zeroth and first ordinary square coefficients.
assert S.expand(n[0]**2+n[1]*n[2])==0
assert S.expand(2*n[0]*a1[0]+n[1]*a1[2]+n[2]*a1[1])==0
print('PASS zeroth and first square coefficients vanish exactly')
# Harmonic coefficient recurrence in x^m H(t,Q), t=y/x, Q=q/x².
D,j=S.symbols('D j'); cj=S.symbols('c_j')
cnext=cj/(2*(j+1)*(D-1-2*j))
assert S.cancel((j+1)*(D/S.Integer(2)-S.Rational(1,2)-j)*cnext-cj/4)==0
print('PASS all-degree harmonic chart recurrence')

# Universal cubic leading coefficient test, not a selected cubic.
c0,c1,c2,c3=S.symbols('c0 c1 c2 c3'); Fc=c3*t**3+c2*t**2+c1*t+c0
assert S.expand(3*S.diff(Fc,t,2)**2-8*S.diff(Fc,t)*S.diff(Fc,t,3)-(-36*c3**2*t**2-24*c3*c2*t+12*c2**2-48*c3*c1))==0
print('PASS universal nonzero quadratic expression')

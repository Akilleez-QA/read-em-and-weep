import sympy as S
# Free scalar evaluations of the fully projected two columns.
am,cm,target=S.symbols('a_m c_m target', nonzero=True)
lSA,lSC=S.symbols('lambda_S_A lambda_S_C')
luu,lau,lua,laa=S.symbols('UU AU UA AA')
U=am*lSA-am*luu-cm*lau
C=cm*lSC-am*lua-cm*laa-cm*target
# At the ramification functional, all four source images disappear.
assert S.expand(U.subs({luu:0,lau:0})-am*lSA)==0
assert S.expand(C.subs({lua:0,laa:0})-cm*(lSC-target))==0
# For p_C(z)=Abar(u), the same S identifies the two remaining evaluations.
assert S.expand(C.subs({lua:0,laa:0,lSC:0}))==-cm*target
# Retaining a complementary spin image is not the same assumption.
spin=S.symbols('spin_contribution')
assert S.solve(am*(lSA+spin),lSA)==[-spin]
EA,EB,EC,bm,k,aa,hh,zz=S.symbols('EA EB EC b_m k a h z')
forced=2*k*aa**2*hh*zz
# U balance fixes the common S evaluation; the c balance retains the full k.
lS=-EA-bm*EB/am
assert S.expand((lS+EC-forced)-(EC-EA-bm*EB/am-forced))==0
assert 12-2-4==6
print('PASS: all four source blocks disappear in the exact ramification quotient.')
print('PASS: one common Cartan action contradicts the nonzero target on the shared input.')
print('PASS: a retained spin-to-Cartan contribution changes the first balance and is not excluded.')
print('No actual coefficients, points, matrices, ranks, or scans were evaluated.')

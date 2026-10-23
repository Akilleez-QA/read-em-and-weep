"""Universal polarized234 q-middle source/error/division bridge, without solving.

Exercises frozen constructors unchanged. All physical scales and all source
error channels remain independent; no actual instance or rank is evaluated.
"""
from universal_q_middle_C_interface import *
from universal_orthogonal_leg_source_map_extension import q as q0,C_action,cliff,getp
# Polynomial polarization is universal for the entire symmetric-linear space:
# the distinct monomials phi_k*g_i*g_j recover every one of its234 coefficients.
phi=sum(c*v for c,v in zip(s.symbols('q_polar_bridge_phi0:3'),positive))
g=s.Matrix(s.symbols('q_polar_bridge_g0:12'))
BB=phi*g*g.T
it=extend_q_middle_C_source(BB)
ex=it['source_extension']
print('PASS: all234 qB coefficients by free polynomial polarization pass the actual-q0 C-source extension, including its high/low reconstruction identities and all off-image errors.',flush=True)
am,bm,cm,kAt=s.symbols('q_bridge_am q_bridge_bm q_bridge_cm q_bridge_kAt',nonzero=True);kap=bm/am
restored=restore_q_middle_companion(it,am,bm,cm,kAt)
assert restored['source_right']==-restored['source_left'].T
fullV=[];fullE=[]
for j,sp in enumerate(mon(2)):
 N=adds(sc(1/kap,it['quotient_Y'][j]),sc(-1,vww_leg(it['quotient_Z'][:,j])))
 V=adds(ex['high'][j]['Vnorm'],sc(-1,N))
 middle=sc(1/kap,it['action'](C_column(sp)[0],am,bm))
 residual=adds(middle,sc(-1,A(ex['Pc'][:,j])),sc(-kap,B(ex['Pc'][:,j])),C_action(ex['y'][:,j]))
 err=adds(ex['high'][j]['high_full_remainder'],
          [wedge({(i,):ex['high'][j]['Lharm'][2*i+b] for i in range(3)},{(3,):-w,(4,):u}) for b in range(2)],
          sc(kap,ex['low_literal'][j]))
 eqvec(adds(residual,sc(q0,V)),err)
 for ff,ee in zip(V,err):eq(scale(q0,contract(coords,ff)),contract(coords,ee))
 eqvec(restored['divided_left'][j+2],sc(kAt*cm,V))
 fullV.append(V);fullE.append(err)
 WW=s.Matrix([ff.get((3,4),0) for ff in ex['low_literal'][j]])
 assert (cliff*getp(ex['high'][j]['R'])-WW).applyfunc(s.expand)==s.zeros(2,1)
print('PASS: literal complete residual+q0*Vactual=all source errors, including Pc/y ends, exterior-closure defects and exact high-spin/low-tail coupling.',flush=True)
alpha=[adds(sc(am,A(s.eye(2)[:,i])),sc(bm,B(s.eye(2)[:,i]))) for i in range(2)]+[sc(cm,C_column(sp)[0]) for sp in mon(2)]
Vcols=[[{},{}],[{},{}]]+[sc(kAt*cm,V) for V in fullV]
Ecols=[[{},{}],[{},{}]]+[sc(kAt*cm,E) for E in fullE]
for i in range(5):
 for j in range(i+1,5):
  dv=add(pair(alpha[i],Vcols[j]),scale(-1,pair(alpha[j],Vcols[i])))
  de=add(pair(alpha[i],Ecols[j]),scale(-1,pair(alpha[j],Ecols[i])))
  eq(scale(q0,dv),de)
print('PASS: all ten five-source skew pairs obey q0*d(Vactual)=d(errors) with fixed negative dual and all am,bm,cm,kAt factors. Closure follows only conditionally after joint errors vanish.',flush=True)
print('No coefficient assignments, points, ranks, restricted source solve, frozen changes or external writes.',flush=True)

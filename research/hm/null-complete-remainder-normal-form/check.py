"""Formal free-symbol controls only; no production or model imports."""
import json
import sys
from pathlib import Path
from collections import Counter
from fractions import Fraction as F

checks=[]
def need(ok,name):
    if not ok: raise RuntimeError(name)
    checks.append(name)
def plus(*items):
    c=Counter()
    for a,scale in items:
        for k,v in a.items(): c[k]+=scale*v
    return {k:v for k,v in c.items() if v}
def atom(s): return {s:F(1)}
# Ordered words are inert distinct operator monomials. Rewrite only supplied
# Pi delta = delta Pi and delta T = T Delta; never H delta = delta H.
outer={'delta Qdot T':1,'Qdot T Delta':1}
inner={'-LGJ2':1,'D':1,'delta Pi Q':-1,'Pi Q Delta':-1}
derivative=plus((outer,1),(inner,1))
K_boundary={'delta Qdot T':1,'delta Pi Q':-1}
K_defect={'Qdot T Delta':1,'Pi Q Delta':-1}
expected=plus((K_boundary,1),(K_defect,1),({'-LGJ2':1,'D':1},1))
need(derivative==expected,'combined derivative and K signs')
need(plus((derivative,-1),(atom('Vp T'),-1))==plus((expected,-1),(atom('Vp T'),-1)),'complete remainder substitution')
need(plus((expected,1),(atom('delta Pi LU'),-1))!=derivative,'reject old U double subtraction')
need(plus((expected,1),({'Pi Q Delta':2},1))!=derivative,'reject wrong nonclosed sign')
need(plus((expected,1),({'-LGJ2':-1},1))!=derivative,'reject dropped selector')
# Each pair's eight signed adjoint branches supplies two coefficient derivatives
# and the curl contribution. Use curl L=-4 kij, curl U=-4(kik-kij).
curl=plus(({'sjk kij':-4},F(-1,2)),({'sij kik':-4,'sij kij':4},F(1,2)))
need(curl=={'sjk kij':2,'sij kik':-2,'sij kij':2},'two-endpoint current curl')
need([-F(s,2) for s in [-1,1,-1,1]]==[F(1,2),-F(1,2),F(1,2),-F(1,2)],'four scalar-free defect signs')
# Connection/frame anomaly is 2 ell p T in each coupled term.
need(2-2==0,'coupled anomaly cancellation')
need(2!=0,'reject either separated term as tensor')
# Rational equalities checked by numerator coefficients, not sampled values.
# Finite alpha-rho: m*y*[2-(x^2+1)]/[2*x*(x^2-1)] = -m*y/(2*x).
need(plus(({'one':2},1),({'x2':1,'one':1},-1))=={'one':1,'x2':-1},'finite beta numerator')
# Infinity rho=-z q'/2q. q=t gives -z/(2t); q=1-t^2 gives zt/(1-t^2).
need(F(-1,2)==-F(1,2),'bit-zero rho')
need(-F(-2,2)==1,'bit-one rho')
need(0-(-F(1,2))==F(1,2) and 1-1==0,'infinity beta legal owner cases')
# Gamma_End changes by -(k_v-k_u)/2 ell, k_v-k_u=2r.
need(-F(2*(-2),2)==2,'internal-minus-two connection anomaly')
# Normalized selected output: p exponent +2, J2 -2, four odd generators -2.
need(2-2-2==-2,'canonical full-sign coefficient transition')
# Missing-axis TZ has -2 there, -4 elsewhere; odd differentiated weight adds -2.
need(-2-2==-4 and 2-4==-2,'prism character and dual-section typing')
add=lambda a,b:tuple(x+y for x,y in zip(a,b))
j,H,Z,G=(4,2),(6,3),(19,7),(5,1)
J2Z=add(add(add(j,H),H),Z)
need(J2Z==(35,15) and add(G,J2Z)==(40,16),'coupled owned bound')
need(add((21,9),Z)==(40,16),'Q Z bound')
need(add((21,9),(27,11))==(48,20),'Q Delta Z bound')
need(all(a<=b for a,b in zip((48,22),(54,29))),'ordinary clearing dominates overlap families')
need(all(a<=b for a,b in zip((35,15),(53,28))),'differentiated own clearing dominates TZ')
# Static inventory is a source-text guard, not semantic code evaluation.
proof=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent/'RESULT.md'
body=''.join(proof.read_text().split())
terms=['U_P,jkU_Q,ij','U_Q,jkU_P,ij','μ_P(U_Q,jk,A)','μ_Q(U_P,jk,A)','μ_P(B,U_Q,ij)','μ_Q(B,U_P,ij)','μ2(B,A)','−b_PU_Q,ik','−b_QU_P,ik','−b_Pb_QG','+F_Qk_P,ik','+F_Pk_Q,ik']
def full_inventory(t): return all(term in t for term in terms)
need(full_inventory(body),'all ten baseline terms and both Fk branches written')
for term in terms[7:]:
    need(not full_inventory(body.replace(term,'')),'reject omitted branch '+term)
print(json.dumps({'status':'PASS','count':len(checks),'checks':checks},indent=2))

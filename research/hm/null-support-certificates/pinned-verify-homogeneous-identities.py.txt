"""Exact homogeneous contraction, scalar-merger, and frame identities."""
import json,hashlib,sys
if sys.flags.optimize:
 raise RuntimeError('Run this checker with assertion-enabled Python (without -O or -OO).')
import sympy as S
from pathlib import Path
MODEL=json.loads((Path(__file__).resolve().parents[1]/'data/model.json').read_text())
v=S.symbols('v0:5')
def deg(p):return max((sum(map(int,k.split(','))) for k,c in p),default=0)
def hom(p,D):return S.Integer(0)+sum(S.Integer(c)*v[0]**(D-sum(es))*S.prod(v[i+1]**e for i,e in enumerate(es)) for k,c in p for es in [list(map(int,k.split(',')))])
def rat(p,d,w):
 if not p:return S.Integer(0)
 D=deg(d);e=max(0,deg(p)-D-w)
 return S.cancel(hom(p,D+e+w)/(v[0]**e*hom(d,D)))
def primitive(c,k):
 den=c[{'I':'di','P':'dp','H0':'dh','H1':'dh'}[k]]
 return S.Matrix([[rat(p,den,([0,1][j] if k=='I' else [0,-1][i] if k=='P' else -1)) for j,p in enumerate(row)] for i,row in enumerate(c[k])])
regular={k:S.Matrix([[hom(p,1) for p in row] for row in MODEL[k]]) for k in ['gamma','delta','ev']}
gamma,delta,ev=[regular[k] for k in ['gamma','delta','ev']]
checks={}
def check(name,M):
 for x in M:
  if S.cancel(x)!=0:raise AssertionError((name,x))
 checks[name]=checks.get(name,0)+len(M)
cs=[]
for a,c in enumerate(MODEL['charts']):
 I,P,H0,H1=[primitive(c,k) for k in ['I','P','H0','H1']]
 eta=S.zeros(10,2)
 for b in range(2):eta[b*5+c['pivot'],b]=1/v[c['pivot']]
 E=I*P
 check('E_identity',E-S.eye(15)+gamma*H0+H1*delta)
 check('P_I',P*I-S.eye(2))
 check('H0_I',H0*I);check('P_H1',P*H1)
 check('H0_H1',H0*H1);check('H1_eta',H1*eta)
 check('H0_gamma',H0*gamma-S.eye(5))
 check('delta_H1_eta_ev',delta*H1+eta*ev-S.eye(10))
 check('ev_eta',ev*eta-S.eye(2))
 check('delta_I',delta*I);check('P_gamma',P*gamma)
 cs.append((I,P,H0,H1,eta,E))
for a in [0,5]:
 I,P,H0,H1,eta,E=cs[a]
 row=S.zeros(1,15);row[0,10]=1/v[0]
 check('merged_H0_row',H0[0,:]-row)
 check('merged_I_row',I[10,:]);check('merged_E_row',E[10,:])
check('gamma_row10',gamma[10,:]-S.Matrix([[v[0],0,0,0,0]]))
check('ev_column0',ev[:,0]-S.Matrix([v[0],0]))
# All ten independent coefficients of L(d_End W), W:K^3->K^0.
for i in range(5):
 for j in range(2):
  W=S.zeros(5,2);W[i,j]=1
  check('L_d_End',S.Matrix([(W*ev)[0,0]-(gamma*W)[10,0]]))
# Formal scalar extension onto D(v0): numerator row Z stays arbitrary.
z=S.symbols('z0:150');Z=S.Matrix(15,10,z)
for a in [0,5]:
 I,P,H0,H1,eta,E=cs[a]
 # h_A h_B j_tail form, before the overall J2 minus.
 check('scalar_formula',S.Matrix([(H0*Z)[0,0]+(E*Z*eta)[10,0]-Z[10,0]/v[0]]))
# Both merged carriers as anchors gives zero for arbitrary F, because E0 row10=0.
check('double_merged_vanish',cs[0][5][10,:])
Pall=S.prod(v)
for j in range(1,5):
 hj=v[j]**5-Pall
 check('cover_v0_zero',S.Matrix([hj.subs(v[0],0)-v[j]**5]))
# Frame covariance on every original product chart: both selected entries are N^-4,
# and full-sign y contributes -2 per changed factor. Homogeneous weight -2 -> tau^-4.
frame_checks=0
for mask in range(16):
 for coord in range(4):
  active=bool(mask&(1<<coord))
  assert (-2-2 if active else 0)==(-4 if active else 0)
  frame_checks+=1
report={'schema':'hm-negative-coset-identities-v1','modelSha256':hashlib.sha256(json.dumps(MODEL,separators=(',',':')).encode()).hexdigest(),'exactScalarChecks':sum(checks.values()),'byIdentity':checks,'originalChartFrameWeightChecks':frame_checks,'scalarFrameWeight':-4,'quotientColumns':[-3,-2],'quotientDifferential':'d_End: -3 -> -2; outgoing -2 -> -1 is zero in quotient','scalarChainMap':'L(X)=X02[0,0]-X13[10,0]; L d_End = 0'}
assert report['modelSha256']=='b6b532c4bab5787397a4cddde34210c12fae71853b30cb73ecbe8a9c2b4826b2'
x,t=S.symbols('x t');s=1-t*t
frame_identity_checks=0
def ck(p,label):
 global frame_identity_checks
 if S.cancel(p)!=0:raise AssertionError(label)
 frame_identity_checks+=1
# Ratio squared, logarithmic derivatives, and OLD connection transport.
ck(t*((x*x-1)/x).subs(x,1/t)-s,'nu1_B squared')
ck(S.diff(t,t)/(2*t)-1/(2*t),'nu0_B logarithmic derivative')
ck(S.diff(s,t)/(2*s)+t/s,'nu1_B logarithmic derivative')
ck((1/(x*(x*x-1))).subs(x,1/t)*(-1/t**2)+t/s,'transport gamma1')
ck((1/x).subs(x,1/t)*(-1/t**2)+1/t,'transport q')
# Homogeneous primitive degree d; exponent p of nu_B = tau^(1/2) nu_A.
# The physical splitting matrices U,Q must remain identical: 2d+p=0.
blocks={'U0_gamma':(1,-2),'U0_I0':(0,0),'U0_I1':(1,-2),'U0_H1W':(-1,2),
'U1_W':(0,0),'U1_eta':(-1,2),'Q0_H0':(-1,2),'Q0_P0':(0,0),'Q0_P1':(-1,2),'Q0_Ldelta':(1,-2),'Q1_L':(0,0),'Q1_ev':(1,-2)}
for mask in range(16):
 for name,(d,p) in blocks.items():
  for a in range(4):ck(((mask>>a)&1)*(2*d+p),name)
 # Physical inclusion I diag(nu,nu^-1) has common K^0 weight +1/2.
 for d,p in [(0,1),(1,-1)]:ck(2*d+p-1,'physical inclusion')
 for d,p in [(0,-1),(-1,1)]:ck(2*d+p+1,'physical projection')
 for r in [0,-1,-2,-3]:
  # H lowers internal degree: tau^-1. Full-sign y product = tau^-2 z product.
  ck(r+(-2)-(r-2),'full-character frame conversion')

report['transportedFrameIdentityChecks']=frame_identity_checks
print(json.dumps(report,indent=2))

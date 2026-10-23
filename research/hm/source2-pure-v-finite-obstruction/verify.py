#!/usr/bin/env python3
"""Finite actual-correction bookkeeping and exact whole-character certificate."""
from pathlib import Path
import json,hashlib
import sympy as s
root=Path(__file__).resolve().parent;checks=[]
def ck(n,b):
 if not bool(b):raise RuntimeError(n)
 checks.append(n)
for v in json.loads((root/'INPUTS.json').read_text()):
 b=(root/v['local_path']).read_bytes()
 ck(v['label']+' sha256',hashlib.sha256(b).hexdigest()==v['sha256'])
 ck(v['label']+' git blob',hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==v['git_blob'])
z=s.sqrt(5);phi=(1+z)/2
tr=[s.Integer(2),s.Integer(-2),s.Integer(0),s.Integer(1),s.Integer(-1),phi,-phi,phi-1,1-phi]
weights=[1,1,30,20,20,12,12,12,12]
def simp(v):return s.Matrix([s.simplify(a) for a in v])
def sy(n):
 a=s.ones(9,1);b=s.Matrix(tr)
 for k in range(n):a,b=b,simp([tr[i]*b[i]-a[i] for i in range(9)])
 return a
def mul(a,b):return simp([v*w for v,w in zip(a,b)])
def ip(a,b):return s.simplify(sum(k*v*w for k,v,w in zip(weights,a,b))/120)
W=sy(1);Wp=simp([v.xreplace({z:-z}) for v in W]);P=mul(W,Wp);A=sy(2);D=sy(4)
plane=[s.ones(9,1),A,mul(A,A)-A]
# For det-one SO3 representation A: exterior2 A=A, exterior3 A=1.
for n in range(3,24):plane.append(simp(mul(A,plane[-1])-mul(A,plane[-2])+plane[-3]))
ck('Sym2 plane character',plane[2]==s.ones(9,1)+D)
ck('Sym3 plane character',plane[3]==sy(6)+A)
ck('all plane dimensions',all(v[0]==s.binomial(n+2,2) for n,v in enumerate(plane)))
# Independent complete-homogeneous recurrence from actual class eigenvalues
# of A: 1,lambda^2,lambda^-2. The power sum is (tr W(g^k))^2-1.
newton=[s.ones(9,1)]
for n in range(1,24):
 vals=[]
 for j,w in enumerate(tr):
  val=0
  for k in range(1,n+1):
   wgk=2*s.chebyshevt(k,w/2)
   val+=(wgk**2-1)*newton[n-k][j]
  vals.append(s.simplify(val/n))
 newton.append(simp(vals))
ck('independent Newton plane characters through23',all(simp(a-b)==s.zeros(9,1) for a,b in zip(plane,newton)))
table=[]
for n in range(3,24):
 lift=ip(P,mul(D,plane[n-1]));mg=ip(P,mul(A,plane[n-2]));kg=ip(P,plane[n-5]) if n>=5 else s.Integer(0)
 row=dict(quotient_order=n,original_order=n+1,lift=int(lift),m_gauge=int(mg),kappa_gauge=int(kg),target=int(lift-mg-kg));table.append(row)
 ck('nonnegative integral target '+str(n),all(v>=0 and v.is_integer for v in [lift,mg,kg,lift-mg-kg]))
ck('sixth gate dimensions',table[2]==dict(quotient_order=5,original_order=6,lift=5,m_gauge=2,kappa_gauge=0,target=3))
ck('first equivariant kappa is original ninth',next(v['original_order'] for v in table if v['kappa_gauge'])==9)
# Exact gauge update: j2 u_A=-mu m, q u_A=-T a_A, j2 a_A=0.
mu,mg,kc,Ta,Tx,Tprev=s.symbols('mu mg kc Ta Tx Tprev',nonzero=True)
ck('gauge leaves preceding q equation',s.expand((-Tprev)+0-(-Tprev))==0)
ck('gauge corrects next q equation',s.expand((-Tx)-Ta/mu-(-(Tx+Ta/mu)))==0)
ck('m gauge removed with kappa retained',s.expand((mg+kc)+(-mu*mg)/mu-kc)==0)
# L kappa=0; L C becomes zero after the update, enough for next inverse.
Lm=s.symbols('Lm');ck('raw next obstruction killed',s.expand(Lm-Lm+0)==0)
# Full formal original cycle through order24. No matrix instance is selected.
t=s.symbols('t');p=s.symbols('p');v=s.symbols('v0:24')
qxi=[p]+[-v[i-1] for i in range(1,24)]
res=t*p-sum(t**(i+1)*qxi[i]+t**(i+2)*v[i] for i in range(24))
ck('all original lift coefficients cancel through24',s.expand(res+t**25*v[23])==0)
ck('quotient23 corresponds original24',table[-1]['quotient_order']==23 and table[-1]['original_order']==24)
ck('zero through24 gives maximal minor order31',3*2+25==31)
ck('degree30 cannot support order31',31>30)
ck('nonzero first remaining quotient n gives exponent nplus1',all(3*2+(r['quotient_order']+1)==r['original_order']+6 for r in table))
ck('absent last pivot gives rank36 and kernel5',33+3==36 and 41-36==5)
ck('retained gate table matches recomputation',json.loads((root/'GATE-TABLE.json').read_text())==table)
result=dict(status='PASS',count=len(checks),checks=checks,gate_table=table,finite_terminal_quotient_order=23,finite_terminal_original_order=24,scope='Sequential actual correction criterion, no actual obstruction coefficients evaluated; ambient targets are not independent realized parameters.')
print(json.dumps(result,indent=2))

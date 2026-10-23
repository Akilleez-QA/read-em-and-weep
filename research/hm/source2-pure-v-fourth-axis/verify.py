#!/usr/bin/env python3
"""Exact whole-orbit certificates. No sampled roots or actual source values."""
from pathlib import Path
import hashlib,json
from itertools import permutations,combinations_with_replacement
from model import *
ROOT=Path(__file__).resolve().parent
checks=[]
def check(name,condition):
 if not bool(condition): raise RuntimeError(name)
 checks.append(name)
for item in json.loads((ROOT/'INPUTS.json').read_text()):
 data=(ROOT/item['local_path']).read_bytes()
 check('sha256 '+item['label'],hashlib.sha256(data).hexdigest()==item['sha256'])
 check('git blob '+item['label'],hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==item['git_blob'])
def gb(fs,*variables): return s.groebner(fs,*variables,extension=z)
def lm(G): return [f.LM(order=G.order).exponents for f in G.polys]
def length(G):
 leading=lm(G); bounds=[]
 for i in range(2):
  bounds.append(min(m[i] for m in leading if m[i] and all(m[j]==0 for j in range(2) if j!=i)))
 return sum(not any(i>=a and j>=b for a,b in leading) for i in range(bounds[0]) for j in range(bounds[1]))
def detpoly(mat):
 out=s.Poly(0,p,q,t,extension=z)
 for perm in permutations(range(mat.rows)):
  term=s.Poly((-1)**sum(perm[i]>perm[j] for i in range(mat.rows) for j in range(i+1,mat.rows)),p,q,t,extension=z)
  for row,col in enumerate(perm):term*=s.Poly(mat[row,col],p,q,t,extension=z)
  out+=term
 return out.as_expr()
B=s.Matrix.hstack(*[Pi*cv(a*a*x**(2-i)*y**i,6) for i in range(3)])
N=s.Matrix([[(-1)**i*detpoly(B[[j for j in range(4) if j!=i],:]) for i in range(4)]])
check('determinant cokernel map',all(s.expand(f)==0 for f in N*B))
F1=(N*L*R1).applyfunc(s.expand);F2=(N*L*R2).applyfunc(s.expand)
H1=(F1*L).applyfunc(s.expand);H2=(F2*L).applyfunc(s.expand)
check('nonic degree',all(s.Poly(f,p,q,t).is_homogeneous and s.Poly(f,p,q,t).total_degree()==9 for f in [*F1,*F2]))
check('original-fourth determinant degree',all(s.Poly(f,p,q,t).is_homogeneous and s.Poly(f,p,q,t).total_degree()==10 for f in [*H1,*H2]))
I3=[s.expand(detpoly(L[:,[j for j in range(5) if j!=i]]).subs(p,1)) for i in range(5)]
I=gb(I3,q,t)
expected=[q*q+s.Rational(27,2)*t**5+s.Rational(27,10)*z*t**4+6*t**3-3*z*t*t-s.Rational(11,2)*t-s.Rational(57,10)*z,q*t**4-q,t**6+s.Rational(2,3)*z*t**5+t**4-t*t-s.Rational(2,3)*z*t-1]
check('entire reduced ten-axis basis',list(I)==expected)
check('entire orbit colength',length(I)==10)
I2=gb([s.prod(v) for v in combinations_with_replacement(list(I),2)],q,t)
I3power=gb([s.prod(v) for v in combinations_with_replacement(list(I),3)],q,t)
check('ordinary square length',length(I2)==30)
check('ordinary cube length',length(I3power)==60)
affine=[[s.expand(f.subs(p,1)) for f in H] for H in [H1,H2]]
for j,row in enumerate(affine):
 check('whole orbit inclusion '+str(j),all(I.reduce(f)[1]==0 for f in row))
rems=[[s.expand(I2.reduce(f)[1]) for f in row] for row in affine]
for i in range(5):check('complete first-jet coefficient identity '+str(i),s.expand(rems[0][i]-2*rems[1][i])==0)
check('nonzero first-jet witness',s.Poly(rems[0][0],q,t).coeff_monomial(q*q*t**3)==-s.Rational(1675264,27))
check('whole-pencil first-jet formula',all(s.expand(aa*r+bb*s0-(aa+bb/2)*r)==0 for r,s0 in zip(*rems)))
C=gb(list(I2)+rems[0],q,t)
check('off-line exact Nakayama certificate',list(C)==list(I))
minus=[s.expand(f-2*g) for f,g in zip(*affine)]
check('exceptional row belongs to ordinary square',all(I2.reduce(f)[1]==0 for f in minus))
C=gb(list(I3power)+[I3power.reduce(f)[1] for f in minus],q,t)
check('exceptional-line exact Nakayama certificate',list(C)==list(I2))
check('twists',6-(-4)==10 and 6-(-3)==9)
print(json.dumps({'status':'PASS','count':len(checks),'checks':checks,'orbit_power_lengths':[10,30,60],'exceptional_coefficient_line':'2alpha+beta=0','C3_local_ideals':{'off_line':'m','on_line':'m^2'},'projective_component_ideal_equality':True},indent=2))

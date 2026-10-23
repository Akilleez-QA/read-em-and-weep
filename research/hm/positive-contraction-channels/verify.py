from itertools import product
import json,hashlib
from pathlib import Path
import sympy as s
c0,c1,c2=s.symbols('c0 c1 c2')
e=[s.eye(3)[:,i] for i in range(3)]
checks=[]
def ck(n,b):
 if not bool(b): raise RuntimeError(n)
 checks.append(n)
root=Path(__file__).resolve().parent
for entry in json.loads((root/'INPUTS.json').read_text()):
 data=(root/entry['path']).read_bytes()
 ck('input SHA256 '+entry['label'],hashlib.sha256(data).hexdigest()==entry['sha256'])
 ck('input Git blob '+entry['label'],hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==entry['git_blob'])
def F(x,y,z):
 return [x*(y.dot(z)), y*x.dot(z)-z*x.dot(y), y*x.dot(z)+z*x.dot(y)-s.Rational(2,3)*x*y.dot(z)]
def T(x,y,z):return sum((c*f for c,f in zip([c0,c1,c2],F(x,y,z))),s.zeros(3,1))
for i,j,k in product(range(3),repeat=3):
 x,y,z=e[i],e[j],e[k]
 ck('commutation tensor '+str((i,j,k)),s.simplify(T(x,y,z)-T(y,x,z)-(c0-c1-s.Rational(5,3)*c2)*(x*y.dot(z)-y*x.dot(z)))==s.zeros(3,1))
for k in range(3):
 z=e[k]
 for a,v in enumerate([1,-2,s.Rational(10,3)]):
  ck('channel trace '+str((a,k)),sum((F(x,x,z)[a] for x in e),s.zeros(3,1))==v*z)
vecs=[]
for a in range(3):vecs.append(s.Matrix([F(e[i],e[j],e[k])[a][l] for i,j,k,l in product(range(3),repeat=4)]))
ck('three universal tensors independent',s.Matrix.hstack(*vecs).rank()==3)
ck('zero trace solution',s.linsolve([c0-c1-s.Rational(5,3)*c2,c0-2*c1+s.Rational(10,3)*c2],(c0,c1,c2))==s.FiniteSet((s.Rational(20,3)*c2,5*c2,c2)))
for a in range(3):
 subs={c0:0,c1:0,c2:0};subs[[c0,c1,c2][a]]=1
 ck('one effective channel fails '+str(a),s.simplify((c0-c1-s.Rational(5,3)*c2).subs(subs))!=0)
ck('allowed first image ranks',sorted({sum(d for d,b in zip([1,3,5],bits) if b) for bits in product([0,1],repeat=3) if sum(bits)>=2})==[4,6,8,9])
for i,j,k in product(range(3),repeat=3):
 x,y,z=e[i],e[j],e[k]
 ck('sharpness product '+str((i,j,k)),x*y.dot(z)+x.cross(y.cross(z))==T(x,y,z).subs({c0:1,c1:1,c2:0}))
a=s.Matrix.hstack(*(s.Matrix([y.dot(z),*y.cross(z)]) for y,z in product(e,repeat=2)))
ck('universal example first image rank four',a.rank()==4)
print(json.dumps({'status':'PASS','checks':len(checks),'scope':'fixed universal representation tensors only'},sort_keys=True))

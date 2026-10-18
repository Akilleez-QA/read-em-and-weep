"""Independent formal controls; no production imports or physical data execution."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
class P:
    def __init__(self,d=None): self.d={w:F(c) for w,c in (d or {}).items() if c}
    def __add__(self,o):
        d=dict(self.d)
        for w,c in o.d.items(): d[w]=d.get(w,0)+c
        return P(d)
    def __neg__(self):return P({w:-c for w,c in self.d.items()})
    def __sub__(self,o):return self+-o
    def __mul__(self,o):
        d={}
        for w,c in self.d.items():
            for v,e in o.d.items():d[w+v]=d.get(w+v,0)+c*e
        return P(d)
    def scale(self,c):return P({w:c*x for w,x in self.d.items()})
    def __eq__(self,o):return self.d==o.d

def letter(s):return P({(s,):1})
def require(ok,msg):
    if not ok:raise RuntimeError(msg)
def T(A,B,C):return -(B*A)+A*C-B*(C-B)
def cob(f):return f(Y,C,D)-f(X+Y,B,D)+f(X,B,C)
X,Y,B,C,D=map(letter,['X','Y','B','C','D'])
rhs=X*Y-(X+C-B)*(Y+D-C)
require(cob(T)==rhs,'ordered transgression')
mutations=[
 lambda A,B,C: -(B*A).scale(2)-B*(C-B),
 lambda A,B,C: -(B*A)+A*B-B*(C-B),
 lambda A,B,C: -(B*A)+A*C+B*(C-B),
 lambda A,B,C: -(B*A)+A*C-(C-B)*B,
]
for n,f in enumerate(mutations):require(cob(f)!=rhs,'undetected endpoint/sign mutation '+str(n))
require(sum(e*r*k*k for e,r,k in zip((-1,1,-1,1),(5,15,10,2),(-1,1,3,5)))==-30,'weights')
# Commutative scalar specialization: sort words, without imposing any such rule above.
def comm(p):
    d={}
    for w,c in p.d.items():
        v=tuple(sorted(w));d[v]=d.get(v,0)+c
    return P(d)
xa,xb,ya,yb=map(letter,['xa','xb','ya','yb'])
dr=comm(ya*yb-(xa+ya)*(xb+yb)+xa*xb)
qab,qba=comm(xa*yb),comm(xb*ya)
require(dr==-(qab+qba),'gerbe edge coboundary')
for sign in [1,-1]:
    result=(qab-qba).scale(F(15,8))-dr.scale(sign*F(15,8))
    require((result==qab.scale(F(15,4)))==(sign==1),'ordered correction sign')
# Coefficient transpose reverses two matrix letters; no Cech interchange.
Pa,Pb,Qa,Qb=map(letter,['Pa','Pb','Qa','Qb'])
column_contraction=Qb*Pa-Qa*Pb
Ctrace_before_trace=(Qa*Pb-Qb*Pa).scale(F(1,2))
require(column_contraction==Ctrace_before_trace.scale(-2),'transpose order')
# Trace of a local two-letter commutator is zero by ordinary coefficient cyclicity.
def trace_two(p):
    d={}
    for w,c in p.d.items():
        require(len(w)==2,'trace control only accepts two coefficient letters')
        v=min(w,w[::-1]);d[v]=d.get(v,0)+c
    return P(d)
require(trace_two(Pa*Pb-Pb*Pa)==P(),'local coefficient trace')
# Chain-map identity-pair diagonal blocks cancel with the actual grading.
u,v,w,h=map(letter,['diag5','diag8','diag2','cohomology2'])
require(-u+(u+h+v)-(v+w)+w==h,'paired supertrace')
# Bind read-only sources, never import/execute them.
root=Path(__file__).parent
pins=json.loads((root/'pins.json').read_text())
for item in pins:
    data=(root/item['path']).read_bytes()
    require(hashlib.sha256(data).hexdigest()==item['sha256'],'changed source '+item['name'])
# Common-frame exponent check; no actual matrices or model data.
weights=(-1,1,3,5)
prescribed=((0,),(-2,0,-2,2),(0,2),(0,))
common=tuple(tuple(k+x for x in row) for k,row in zip(weights,prescribed))
require(common==((-1,),(-1,1,-1,3),(3,5),(5,)), 'ambient and column weights')
require(common[0][0]==common[1][0] and common[1][3]==common[2][0] and common[2][1]==common[3][0], 'paired frame transport')
require(common[1][1:3]==(1,-1), 'cohomology reciprocal frame')
require(prescribed[1][1:3]!=(1,-1), 'omitted ambient factor undetected')
# A non-chain endomorphism need not have paired diagonal cancellation.
require(-u+(u+h+v)-(v+w)+(w+letter('defect'))!=h, 'nonchain cancellation control')
require(column_contraction!=Ctrace_before_trace.scale(2), 'transpose sign control')
require((qab-qba).scale(F(15,8))!=qab.scale(F(15,4)), 'dropped gerbe control')
# Exact AST binding of the reviewed scalar function, not execution of source.
import ast
source=(root/'inputs/raw_engine.py.txt').read_text()
node=next(n for n in ast.parse(source).body if isinstance(n,ast.FunctionDef) and n.name=='raw_scalar_formula')
expected=ast.parse((root/'inputs/scalar-contract.py.txt').read_text()).body[0]
require(ast.dump(node,include_attributes=False)==ast.dump(expected,include_attributes=False),'scalar source contract')
print(json.dumps({'result':'PASS','formal_transgression':True,'negative_controls':9,'ordered_gerbe':True,'row_column_reversal':True,'paired_supertrace':True,'common_ambient_weights':True,'scalar_AST_contract':True,'source_hashes':len(pins),'physical_execution':False},sort_keys=True))

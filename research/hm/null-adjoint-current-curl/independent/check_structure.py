"""Independent source-shape and abstract current algebra controls; inert AST only."""
import ast,json
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
root=Path(__file__).resolve().parents[1]
def need(ok,label):
    if not ok:raise RuntimeError(label)
tree=ast.parse((root/'inputs/compiler.py.txt').read_text())
source=next(x for x in tree.body if isinstance(x,ast.ClassDef) and x.name=='Source')
methods={x.name:x for x in source.body if isinstance(x,ast.FunctionDef)}
def assignments(method):
    return {n.targets[0].id:n.value for n in ast.walk(methods[method]) if isinstance(n,ast.Assign) and len(n.targets)==1 and isinstance(n.targets[0],ast.Name)}
a=assignments('residual')
need(len(a['kin'].elts)==7,'seven kinetic terms')
need(len(a['gerbe'].elts)==3,'three gerbe terms')
need(all(isinstance(x,ast.Call) and x.func.attr=='scale' and ast.literal_eval(x.args[-1])==-1 for x in a['gerbe'].elts),'negative gerbe signs')
need([ast.literal_eval(k) for k in a['parts'].keys]==['baseline','Fk12','Fk34','E12','E34'],'complete residual parts')
need(ast.dump(a['M0'])==ast.dump(ast.parse('c.mul(self.gi(i,k),c.add(*(kin+gerbe)))',mode='eval').body),'left normalization')
need(ast.unparse(a['parts'].values[0])=='c.tf(M0)','trace-free baseline')
need(ast.unparse(a['parts'].values[1])=='c.smul(self.F(q, t), self.k(p, i, k))','first Fk')
need(ast.unparse(a['parts'].values[2])=='c.smul(self.F(p, t), self.k(q, i, k))','second Fk')
raw=ast.parse((root/'inputs/raw_engine.py.txt').read_text())
r=next(x for x in raw.body if isinstance(x,ast.ClassDef) and x.name=='RawSource')
need([x.name for x in r.body if isinstance(x,ast.FunctionDef)]==['T'],'RawSource overrides T alone')
# Independent associative word expansion with four arbitrary current letters.
# No matrix entries, actual source values, inverse algebra or main-checker import.
def plus(*ps):
    out=Counter()
    for p in ps:
        for w,c in p.items():out[w]+=c
    return {w:c for w,c in out.items() if c}
def times(p,q):
    out=Counter()
    for w,c in p.items():
        for v,d in q.items():out[w+v]+=c*d
    return dict(out)
def scale(p,c):return {w:c*v for w,v in p.items() if c*v}
def bracket(p,q):return plus(times(p,q),scale(times(q,p),-1))
la,lb,ua,ub=[{(x,):F(1)} for x in 'lmuv']
kl=scale(bracket(la,lb),F(1,4));kt=scale(bracket(plus(la,ua),plus(lb,ub)),F(1,4))
cu=scale(plus(bracket(ua,ub),bracket(la,ub),bracket(ua,lb)),-1)
need(plus(cu,scale(plus(kt,scale(kl,-1)),4))=={},'transported curvature')
need(plus(cu,bracket(ua,ub))!={},'naive MC negative control')
# Abstract K is linear; append independent derivative symbols to ensure retention.
qL={('kernel_a_Lb',):F(1),('kernel_b_La',):F(-1)}
qU={('kernel_a_Ub',):F(1),('kernel_b_Ua',):F(-1)}
oldjk=scale(plus(qL,scale(kl,-4)),F(-1,2))
oldij=scale(plus(qU,cu),F(1,2))
need(oldjk==plus(scale(qL,F(-1,2)),scale(kl,2)),'jk adjoint')
need(oldij==plus(scale(qU,F(1,2)),scale(plus(kl,scale(kt,-1)),2)),'ij adjoint')
need(oldjk!=scale(kl,2) and oldij!=scale(plus(kl,scale(kt,-1)),2),'both kernel derivatives indispensable')
print(json.dumps({'status':'PASS','static_checks':9,'abstract_checks':5,'source_executions':0,'matrix_evaluations':0},sort_keys=True))

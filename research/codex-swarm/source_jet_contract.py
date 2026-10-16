#!/usr/bin/env python3
"""Lazy finite-chart metadata binder; never expands/evaluates an HM polynomial.
Input JSON: {"schema":"hm-finite-second-jet-v1","owners":[i,j,k]}, each
owner={"standard":[0,0,0,0],"model_chart":0..5,"mask":[0|1]*4}.
model_chart is the literal pinned charts[] index, not an external carrier ID.
Infinity charts and external owner-to-chart dictionaries are intentionally rejected.
Run: python FILE --repo PATH --input request.json; --self-test for tiny controls.
Output contains lazy matrix/scalar AST demands, not a symmetry verdict. Primitive
partial nodes mean exact formal rational derivatives w.r.t. e1..e4 of the named
pinned matrix numerator / denominator; they are not computed here. Denominator
nonvanishing is a symbolic localization obligation, never a checked open point.
"""
import argparse, hashlib, itertools, json, subprocess
from pathlib import Path
REV='08b73637d4136f91606aad332c46cafd064417f8'
NEW='5df68750f766b18a746e50bff662b09829225ab1'
BASE='research/hm/current-scalar-geometric-dependencies/data/'
CERT='research/hm/null-support-certificates/source-second-jet-degeneracy-certificate.md'
PINS=[(REV,BASE+'model.json','635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926'),(REV,BASE+'source-formulas.js','c4f65ff831092d0e56b3e33a0357f44182169fda45943ea780c8c551b4023f94'),(NEW,CERT,'bffd6fb6bbc8ede344dfe0915364d00812df91c51b746de885e88359c23dfb06')]
def require(ok,msg):
    if not ok: raise ValueError(msg)
def authenticate(repo,reader=None):
    reader=reader or (lambda rev,path:subprocess.check_output(['git','show',rev+':'+path],cwd=repo))
    data=[]
    for rev,path,digest in PINS:
        raw=reader(rev,path)
        require(hashlib.sha256(raw).hexdigest()==digest,'missing/corrupt binding: '+path)
        data.append(raw)
    return json.loads(data[0])
class AST:
    def __init__(self): self.nodes=[]; self.index={}
    def n(self,op,*args):
        key=json.dumps([op,*args],separators=(',',':'),sort_keys=True)
        if key not in self.index:
            require(len(self.nodes)<10000,'metadata node cap')
            self.index[key]=len(self.nodes);self.nodes.append([op,*args])
        return self.index[key]
    def add(self,*xs):return self.n('add',*xs)
    def mul(self,*xs):return self.n('ordered_mul',*xs)
    def neg(self,x):return self.n('neg',x)
    def es(self,r,omitted):
        # e_r on remaining coordinates: a compact exact combinatorial definition.
        coords=[a for a in range(1,5) if a not in omitted]
        return self.n('elementary_symmetric',r,coords)
    def primitive(self,owner,block,axes=()):
        def leaf(multi):return self.n('rational_matrix_e_partial',owner,block,list(multi))
        if not axes:return leaf(())
        if len(axes)==1:
            return self.add(*(self.mul(leaf((r,)),self.es(r-1,axes)) for r in range(1,5)))
        a,b=axes;require(a!=b,'distinct-coordinate contract')
        first=[self.mul(leaf((r,s)),self.es(r-1,(a,)),self.es(s-1,(b,))) for r in range(1,5) for s in range(1,5)]
        hessian=[self.mul(leaf((r,)),self.es(r-2,(a,b))) for r in range(2,5)]
        return self.add(*first,*hessian)
    def core(self,u,v,axes=()):
        if not axes: return self.n('transpose',self.mul(self.primitive(u,'P'),self.primitive(v,'I')))
        if len(axes)==1:
            a=axes[0];return self.n('transpose',self.add(self.mul(self.primitive(u,'P',(a,)),self.primitive(v,'I')),self.mul(self.primitive(u,'P'),self.primitive(v,'I',(a,)))))
        a,b=axes
        return self.n('transpose',self.add(self.mul(self.primitive(u,'P',(a,b)),self.primitive(v,'I')),self.mul(self.primitive(u,'P',(a,)),self.primitive(v,'I',(b,))),self.mul(self.primitive(u,'P',(b,)),self.primitive(v,'I',(a,))),self.mul(self.primitive(u,'P'),self.primitive(v,'I',(a,b)))))
    def q(self,u,a,derivative=None):
        # Endpoint Q=m_ua*(x_a^2+1)/(2*x_a*(x_a^2-1))*diag(1,-1).
        # partial_b Q is retained as an exact derivative node, including b!=a.
        return self.n('endpoint_Q',u,a,derivative)
    def L(self,u,v,a,x):return self.add(self.mul(self.q(v,a),x),self.neg(self.mul(x,self.q(u,a))))
    def jet(self,u,v,a,b):
        K=self.core(u,v);Ka=self.core(u,v,(a,));Kb=self.core(u,v,(b,))
        # nabla_b nabla_a K, including derivative of endpoint Q_a.
        return self.add(self.core(u,v,(a,b)),self.L(u,v,a,Kb),self.L(u,v,b,Ka),self.L(u,v,b,self.L(u,v,a,K)),self.mul(self.q(v,a,b),K),self.neg(self.mul(K,self.q(u,a,b))))
def build(request,model,features=('Q','Hessian')):
    require(set(features)=={'Q','Hessian'},'omitted Q/Hessian forbidden')
    require(isinstance(request,dict) and set(request)=={'schema','owners'},'exact request fields; external carrier maps forbidden')
    require(request.get('schema')=='hm-finite-second-jet-v1','schema')
    owners=request.get('owners');require(isinstance(owners,list) and len(owners)==3,'three ordered owners required')
    for owner in owners:
        require(isinstance(owner,dict) and set(owner)=={'standard','model_chart','mask'},'owner fields')
        require(isinstance(owner['standard'],list) and len(owner['standard'])==4 and all(type(x) is int and x==0 for x in owner['standard']),'only literal finite standard bits supported')
        require(type(owner['model_chart']) is int and 0<=owner['model_chart']<len(model['charts']),'literal chart index')
        require(isinstance(owner['mask'],list) and len(owner['mask'])==4 and all(type(x) is int and x in (0,1) for x in owner['mask']),'mask')
    A=AST();K=A.core(0,1);B=A.core(1,2);ki=A.n('inverse',K);bi=A.n('inverse',B)
    H=[];J=[]
    for a,b in ((1,3),(1,4),(2,3),(2,4)):
        H.append(A.n('traceless',A.mul(ki,A.jet(0,1,a,b))))
        J.append(A.n('traceless',A.mul(ki,bi,A.jet(1,2,a,b),K)))
    def component(x,c):return A.n('sl2_component',x,c)
    def gram(c,d):
        return A.add(*(A.n('scale',sign,A.mul(component(J[i],c),component(H[k],d))) for i,k,sign in ((0,3,1),(1,2,-1),(2,1,-1),(3,0,1))))
    outputs={c+d:A.add(gram(c,d),A.neg(gram(d,c))) for c,d in (('e','f'),('h','e'),('f','h'))}
    lookup=[]
    for o in owners:
        chart=model['charts'][o['model_chart']]
        require(all(k in chart for k in ('P','I','dp','di')),'primitive schema')
        lookup.append({'P':[len(chart['P']),len(chart['P'][0])],'I':[len(chart['I']),len(chart['I'][0])],'numerators':['P','I'],'denominators':['dp','di']})
    return {'schema':'hm-lazy-second-jet-contract-v1','pins':PINS,'owners':owners,'primitive_lookup':lookup,'slots':[[1,3],[1,4],[2,3],[2,4]],'nodes':A.nodes,'Hbar_traceless':H,'Jbar_traceless':J,'skew_demands':outputs,'semantics':{'e_partial':'formal derivative of entire rational matrix incl denominator','elementary_symmetric':'e_r of listed x coords; e_0=1, e_r=0 for r<0 or r>number coords','endpoint_Q':'mask[axis-1]*(x_axis^2+1)/(2*x_axis*(x_axis^2-1))*diag(1,-1); optional third field is partial derivative axis','sl2_component':'h=(M00-M11)/2,e=M01,f=M10','inverse':'symbolic matrix inverse, localized at det nonzero'},'domain_obligations':['finite-chart legal denominators x_i*(x_i^2-1) nonzero','all bound primitive dp/di denominators nonzero','K01,K12 invertible','source carrier-label to model_chart map external; no ordinal reinterpretation'],'physical_polynomials_evaluated':False,'symmetry_verdict':'not computed'}
def self_test(repo):
    model=authenticate(repo)
    o={'standard':[0]*4,'model_chart':0,'mask':[0,1,0,1]};r={'schema':'hm-finite-second-jet-v1','owners':[o,o,o]}
    result=build(r,model);require(len(result['skew_demands'])==3,'skew slots')
    ast=AST();ast.primitive(0,'P',(1,3));require(any(n==['elementary_symmetric',0,[2,4]] for n in ast.nodes),'e2 Hessian term missing')
    require(any(n[0]=='endpoint_Q' and n[3] is not None for n in result['nodes']),'Q derivatives absent')
    for feat in (('Q',),('Hessian',)):
        try:build(r,model,feat)
        except ValueError:pass
        else:raise ValueError('omission accepted')
    for bad in (b'',b'corrupt'):
        try:authenticate(repo,lambda *_:bad)
        except ValueError:pass
        else:raise ValueError('corrupt binding accepted')
    bad_requests=[dict(r,carrier_map={}),dict(r,owners=[None,o,o]),dict(r,owners=[dict(o,standard=[1,0,0,0]),o,o]),dict(r,owners=[dict(o,standard=[0.0]*4),o,o]),dict(r,owners=[dict(o,standard=[False]*4),o,o])]
    for bad in bad_requests:
        try:build(bad,model)
        except ValueError:pass
        else:raise ValueError('unsupported owner/chart/schema accepted')
    print(json.dumps({'status':'pass','checks':'binding corruption, Q/Hessian omissions, Hessian chain node, Q derivative, exact schema and finite-bit types, infinity rejection','nodes':len(result['nodes']),'physical_polynomials_evaluated':False}))
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--repo',required=True);p.add_argument('--input',type=Path);p.add_argument('--self-test',action='store_true');a=p.parse_args()
    if a.self_test:self_test(a.repo)
    else:
        require(a.input is not None,'--input required');require(a.input.stat().st_size<=8192,'request cap')
        print(json.dumps(build(json.loads(a.input.read_text()),authenticate(a.repo)),sort_keys=True))
if __name__=='__main__':main()

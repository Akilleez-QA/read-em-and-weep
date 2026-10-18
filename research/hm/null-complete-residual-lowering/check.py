#!/usr/bin/env python3
"""Restricted source AST interpretation in invented formal symbols, never imports source."""
import ast, hashlib, json, copy
from pathlib import Path
from fractions import Fraction as Q
from functools import reduce
HERE=Path(__file__).resolve().parent
SOURCE=HERE/'sources/e93cf712f9da4926a8450cc870ed45a7bfc379ab/research/codex-swarm/scalar-compiler/compiler.py.txt'
def need(v,msg):
    if not v: raise ValueError(msg)
# Keys: (commuting scalar atom multiset, NONCOMMUTATIVE matrix word).
class P:
    def __init__(self,t=None): self.t={k:Q(v) for k,v in (t or {}).items() if v}
    def __add__(self,b):
        d=self.t.copy()
        for k,v in b.t.items(): d[k]=d.get(k,0)+v
        return P(d)
    def __mul__(self,b):
        d={}
        for (s,w),v in self.t.items():
            for (t,z),u in b.t.items():
                k=(tuple(sorted(s+t,key=repr)),w+z); d[k]=d.get(k,0)+v*u
        return P(d)
    def __eq__(self,b): return isinstance(b,P) and self.t==b.t
    def scale(self,c): return P({k:v*c for k,v in self.t.items()})
def atom(kind,*args,scalar=False):
    x=(kind,args,())
    return P({((x,),()) if scalar else ((),(x,)):1})
def one(): return P({((),()):1})
def add(*xs): return reduce(lambda x,y:x+y,xs,P())
def mul(*xs): return reduce(lambda x,y:x*y,xs,one())
def trace(x):
    out=P()
    for (s,w),v in x.t.items():
        if not w: out=out+P({(s,()):2*v})
        else: out=out+P({(tuple(sorted(s+(('tr',w,()),),key=repr)),()):v})
    return out
def derivative_atom(x,d,scalar):
    kind,args,ds=x
    if kind=='tr': return trace(D(P({((),args):1}),d))
    y=(kind,args,tuple(sorted(ds+(d,))))
    return P({((y,),()) if scalar else ((),(y,)):1})
def D(x,d):
    out=P()
    for (s,w),v in x.t.items():
        for i,a in enumerate(s):
            out=out+mul(P({(s[:i]+s[i+1:],w):v}),derivative_atom(a,d,True))
        for i,a in enumerate(w):
            out=out+mul(P({(s,w[:i]):v}),derivative_atom(a,d,False),P({((),w[i+1:]):1}))
    return out
class Algebra:
    add=staticmethod(add); mul=staticmethod(mul); smul=staticmethod(mul); D=staticmethod(D); trace=staticmethod(trace)
    scale=staticmethod(lambda x,c:x.scale(c))
    tf=staticmethod(lambda x:add(x,trace(x).scale(Q(-1,2))))
    eye=staticmethod(lambda n:one())
    def leaf(self,name,shape,**kw):
        if name=='g_phys': return atom('g',*kw['owners'])
        need(name=='physical_q','only abstract q/g leaves');return atom('q',*kw['owners'],kw['coordinate'],scalar=True)
    def inverse(self,x):
        need(len(x.t)==1,'inverse only single invented g'); ((s,w),v),=x.t.items()
        need(not s and len(w)==1 and v==1 and w[0][0]=='g','inverse g shape')
        return atom('inv',*w[0][1])
class Return(Exception):
    def __init__(self,x): self.x=x
class Source:
    def __init__(self,tree):
        cls=next(n for n in tree.body if isinstance(n,ast.ClassDef) and n.name=='Source')
        self.methods={n.name:n for n in cls.body if isinstance(n,ast.FunctionDef)}
        self.c=Algebra();self.memo={};self.baselines={};self.components={}
    def T(self,p,a,b): return atom('s',tuple(p),a,b,scalar=True)
    def __getattr__(self,k):
        need(k in ('g','gi','k','mu','mu2','b','F','E','residual'),'unapproved source method '+k)
        def call(*args):
            fn=self.methods[k]; e=dict(zip([a.arg for a in fn.args.args],[self]+list(args)))
            try: statements(fn.body,e)
            except Return as r:return r.x
            raise ValueError('missing return')
        return call
def assign(n,v,e):
    if isinstance(n,ast.Name):e[n.id]=v
    elif isinstance(n,ast.Tuple):
        need(len(n.elts)==len(v),'unpack arity')
        for a,b in zip(n.elts,v):assign(a,b,e)
    elif isinstance(n,ast.Subscript): ev(n.value,e)[ev(n.slice,e)]=v
    else:raise ValueError('unsupported assignment '+ast.dump(n))
def ev(n,e):
    if isinstance(n,ast.Constant):return n.value
    if isinstance(n,ast.Name):return e[n.id] if n.id in e else {'Q':Q,'tuple':tuple}[n.id]
    if isinstance(n,ast.Attribute):return getattr(ev(n.value,e),n.attr)
    if isinstance(n,(ast.Tuple,ast.List)):return (tuple if isinstance(n,ast.Tuple) else list)(ev(a,e) for a in n.elts)
    if isinstance(n,ast.Dict):return {ev(k,e):ev(v,e) for k,v in zip(n.keys,n.values)}
    if isinstance(n,ast.Subscript):return ev(n.value,e)[ev(n.slice,e)]
    if isinstance(n,ast.UnaryOp) and isinstance(n.op,ast.USub):return -ev(n.operand,e)
    if isinstance(n,ast.BinOp) and isinstance(n.op,ast.Add):return ev(n.left,e)+ev(n.right,e)
    if isinstance(n,ast.Compare):
        need(len(n.ops)==1 and isinstance(n.ops[0],ast.In),'only memo membership');return ev(n.left,e) in ev(n.comparators[0],e)
    if isinstance(n,ast.Lambda):
        def lam(*args):return ev(n.body,{**e,**dict(zip([a.arg for a in n.args.args],args))})
        return lam
    if isinstance(n,ast.Call):
        args=[]
        for a in n.args:
            if isinstance(a,ast.Starred):args.extend(ev(a.value,e))
            else:args.append(ev(a,e))
        return ev(n.func,e)(*args,**{k.arg:ev(k.value,e) for k in n.keywords})
    raise ValueError('unsupported expression '+ast.dump(n))
def statements(ns,e):
    for n in ns:
        if isinstance(n,ast.Assign):
            v=ev(n.value,e)
            for target in n.targets:assign(target,v,e)
        elif isinstance(n,ast.Return):raise Return(ev(n.value,e))
        elif isinstance(n,ast.For):
            need(not n.orelse,'no for else')
            for v in ev(n.iter,e):assign(n.target,v,e);statements(n.body,e)
        elif isinstance(n,ast.If):statements(n.body if ev(n.test,e) else n.orelse,e)
        elif isinstance(n,ast.Expr):ev(n.value,e)
        else:raise ValueError('unsupported statement '+ast.dump(n))
# Independent handwritten formula from accepted RS §§3–4 / BI eq(3).
def expected():
    g=lambda a,b:atom('g',a,b); inv=lambda a,b:atom('inv',a,b)
    def K(r,a,b):
        u,v=r
        return add(mul(D(inv(a,b),u),D(g(a,b),v)),mul(D(inv(a,b),v),D(g(a,b),u)).scale(-1)).scale(Q(-1,4))
    def mu(r,B,A):
        u,v=r
        return add(mul(D(B,u),D(A,v)),mul(D(B,v),D(A,u)).scale(-1)).scale(Q(1,2))
    def b(r):return mul(atom('q','i','j',r[0],scalar=True),atom('q','j','k',r[1],scalar=True)).scale(Q(15,4))
    p=(0,1);q=(2,3);A=g('i','j');B=g('j','k');G=g('i','k');N=inv('i','k')
    U=lambda r,a,z:mul(g(a,z),K(r,a,z))
    jets=add(mul(D(D(B,0),2),D(D(A,1),3)),mul(D(D(B,0),3),D(D(A,1),2)).scale(-1),mul(D(D(B,1),2),D(D(A,0),3)).scale(-1),mul(D(D(B,1),3),D(D(A,0),2))).scale(Q(1,4))
    kin=[mul(U(p,'j','k'),U(q,'i','j')),mul(U(q,'j','k'),U(p,'i','j')),mu(p,U(q,'j','k'),A),mu(q,U(p,'j','k'),A),mu(p,B,U(q,'i','j')),mu(q,B,U(p,'i','j')),jets]
    gerbe=[mul(b(p),U(q,'i','k')).scale(-1),mul(b(q),U(p,'i','k')).scale(-1),mul(b(p),b(q),G).scale(-1)]
    M=mul(N,add(*(kin+gerbe)))
    F=lambda r:add(b(r),trace(mul(N,mu(r,B,A))).scale(Q(-1,2)))
    def E(r,t):
        a,z=r;sij=atom('s',t,'i','j',scalar=True);sjk=atom('s',t,'j','k',scalar=True)
        L=lambda d:mul(inv('i','j'),D(A,d))
        T=lambda d:mul(inv('i','j'),inv('j','k'),D(B,d),A)
        return add(mul(D(sjk,a),L(z)),mul(D(sjk,z),L(a)).scale(-1),mul(D(sij,z),T(a)),mul(D(sij,a),T(z)).scale(-1)).scale(Q(1,2))
    parts={'baseline':add(M,trace(M).scale(Q(-1,2))),'Fk12':mul(F(q),K(p,'i','k')),'Fk34':mul(F(p),K(q,'i','k')),'E12':E(p,q),'E34':E(q,p)}
    return kin,gerbe,M,parts

def check(text):
    s=Source(ast.parse(text));out=s.residual(('i','j','k'));kin,gerbe,M,parts=expected();t=('i','j','k')
    need(s.baselines[t]['kinetic_terms']==kin,'seven ordered kinetic terms')
    need(s.baselines[t]['gerbe_terms']==gerbe,'three negative gerbe terms')
    need(s.baselines[t]['M0']==M,'left normalization')
    need(s.components[t]==parts,'all five complete components')
    need(out==add(*parts.values()),'complete sum')
    return {'kinetic_expanded_word_counts':[len(x.t) for x in kin],'gerbe_expanded_word_counts':[len(x.t) for x in gerbe],'component_expanded_word_counts':{k:len(v.t) for k,v in parts.items()},'total_expanded_words':len(out.t)}

PIN_MANIFEST_SHA256 = '347f5c01b4c668917a3e446a55f0d56c8198402ebd49fd2bfe6d5b2a44ee741b'
def verify_record(p, raw):
    need(len(raw)==p['bytes'], 'input byte count drift')
    need(hashlib.sha256(raw).hexdigest()==p['sha256'], 'input SHA256 drift')
    need(hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==p['git_blob'], 'input Git blob drift')
def authenticate():
    raw=(HERE/'pins.json').read_bytes()
    need(hashlib.sha256(raw).hexdigest()==PIN_MANIFEST_SHA256, 'pin manifest drift')
    for p in json.loads(raw):
        path=HERE/p['bundle_path']
        need(path.resolve().is_relative_to(HERE), 'pin path escape')
        verify_record(p,path.read_bytes())
def check_negative_pins():
    rejected=[]
    for p in json.loads((HERE/'pins.json').read_bytes()):
        raw=(HERE/p['bundle_path']).read_bytes()
        for label,record,data in [
            ('bytes',p,raw+b'!'),
            ('same-length bytes',p,bytes([raw[0]^1])+raw[1:]),
            ('SHA256',dict(p,sha256='0'*64),raw),
            ('Git blob',dict(p,git_blob='0'*40),raw),
            ('byte count',dict(p,bytes=p['bytes']+1),raw)]:
            try:verify_record(record,data)
            except ValueError:rejected.append(p['bundle_path']+': '+label)
            else:raise ValueError('accepted negative pin '+label)
    need(hashlib.sha256((HERE/'pins.json').read_bytes()+b' ').hexdigest()!=PIN_MANIFEST_SHA256,'manifest negative control')
    return {'input_drifts_rejected':len(rejected),'manifest_drift_rejected':True}

def main():
    authenticate()
    negative_pins=check_negative_pins()
    text=SOURCE.read_text();counts=check(text)
    mutations=[('kinetic order','c.mul(u(p,j,k),u(q,i,j))','c.mul(u(q,i,j),u(p,j,k))'),('mu wedge sign','Q(1,2))\n    def mu2','Q(-1,2))\n    def mu2'),('mixed Moyal coefficient','return c.scale(c.add(*terms),Q(1,4))','return c.scale(c.add(*terms),Q(1,8))'),('mixed jet sign','(0,3,1,2,-1)','(0,3,1,2,1)'),('gerbe sign','c.smul(bp,u(q,i,k)),-1','c.smul(bp,u(q,i,k)),1'),('gerbe last omitted','kin+gerbe','kin+gerbe[:2]'),('normalization side','c.mul(self.gi(i,k),c.add(*(kin+gerbe)))','c.mul(c.add(*(kin+gerbe)),self.gi(i,k))'),('F trace sign','c.scale(c.trace(curvature),Q(-1,2))','c.scale(c.trace(curvature),Q(1,2))'),('Fk pair swap','self.F(q,t),self.k(p,i,k)','self.F(p,t),self.k(p,i,k)'),('E transport order','self.gi(i,j),self.gi(j,k),c.D(self.g(j,k),a)','self.gi(j,k),self.gi(i,j),c.D(self.g(j,k),a)'),('E endpoint omission','c.D(sij,b),ta','c.D(sjk,b),ta'),('E minus sign','c.D(sij,a),tb),-1','c.D(sij,a),tb),1'),('k factor','Q(-1,4))','Q(-1,2))')]
    rejected=[]
    # Use semantic omission without introducing unsupported slice AST.
    mutations[5]=('gerbe last omitted','kin+gerbe','kin+[gerbe[0],gerbe[1]]')
    for label,old,new in mutations:
        need(old in text,'mutation anchor '+label)
        try:check(text.replace(old,new,1))
        except ValueError as e:
            need(not str(e).startswith('unsupported'),'mutation must fail semantically');rejected.append(label)
        else:raise ValueError('accepted mutation '+label)
    # Bind tf and raw dispatch to actual parsed source, without importing it.
    raw= (HERE/'sources/e93cf712f9da4926a8450cc870ed45a7bfc379ab/research/codex-swarm/detector-realization/raw_engine.py.txt').read_text()
    rt=ast.parse(raw)
    rc=next(n for n in rt.body if isinstance(n,ast.ClassDef) and n.name=='RawSource')
    need(ast.unparse(rc.bases[0])=='SC.Source','raw class inherits Source')
    need([n.name for n in rc.body if isinstance(n,ast.FunctionDef)]==['T'],'only raw T override')
    tfun=next(n for n in rc.body if isinstance(n,ast.FunctionDef))
    need(ast.dump(tfun.body[0].value,include_attributes=False)==ast.dump(ast.parse('((self.c.model.s_raw(tuple(p), a, b),),)',mode='eval').body,include_attributes=False),'raw scalar wrapper and endpoint/pair order')
    for tree,classname in [(ast.parse(text),'Circuit'),(rt,'Mat')]:
        classes=[n for n in tree.body if isinstance(n,ast.ClassDef)]
        cls=next((n for n in classes if n.name==classname),None)
        if cls is None:
            cls=next(n for n in classes if any(isinstance(f,ast.FunctionDef) and f.name=='tf' for f in n.body))
        tf=next(n for n in cls.body if isinstance(n,ast.FunctionDef) and n.name=='tf')
        result=next(n.value for n in tf.body if isinstance(n,ast.Return))
        need(ev(result,{'self':Algebra(),'n':atom('X'),'a':atom('X')})==Algebra.tf(atom('X')),'actual tf AST')
    # Rank-two trace checks, explicitly active under -O.
    x=atom('X');need(trace(Algebra.tf(x))==P(),'tf trace zero')
    need(Algebra.tf(one())==P(),'central identity removed')
    return {'status':'PASS','negative_pin_controls':negative_pins,'counts':counts,'semantic_mutations_rejected':rejected,'physical_execution':False,'ID0_claim':False,'production_imports':False}
if __name__=='__main__': print(json.dumps(main(),indent=2))

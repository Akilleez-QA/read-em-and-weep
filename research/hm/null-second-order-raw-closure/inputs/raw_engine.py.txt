"""Literal fresh raw source/HPL program over RF exact field operations.

No physical constructor or entry point may run without existing aggregate
admission. None exists in this package. ArtificialFrames is a separate tiny
explicit fixture, not a replacement physical model or a callback interface.
"""
from fractions import Fraction as Q
from functools import lru_cache
import importlib.util
from pathlib import Path
import sys

BASE=Path(__file__).resolve().parent.parent

def load(name,path):
    if name in sys.modules:
        if Path(sys.modules[name].__file__).resolve()!=Path(path).resolve():raise ValueError('foreign module path')
        return sys.modules[name]
    spec=importlib.util.spec_from_file_location(name,path);mod=importlib.util.module_from_spec(spec)
    sys.modules[name]=mod;spec.loader.exec_module(mod);return mod

RF=load('sr01_RF',BASE/'exact-curve-field/field.py')
SC=load('sr01_SC',BASE/'scalar-compiler/compiler.py')
JC=load('sr01_JC',BASE/'full-lift-domain/lift.py')
I=JC.I


def require_aggregate_admission():
    raise I.PhysicalAdmissionMissing('No reconciled existing aggregate admission for SR01/RF/outer route; physical requests refused before arithmetic')


def power(x,n):
    if type(n)is not int:raise ValueError('literal power')
    if n<0:return power(x.inverse(),-n)
    out=x.ex.scalar(1)
    while n:
        if n&1:out=out*x
        n//=2
        if n:x=x*x
    return out


class Mat:
    def __init__(self,ex):self.ex=ex;self.events={}
    def zero(self,r,c):return tuple(tuple(self.ex.scalar(0)for _ in range(c))for _ in range(r))
    def eye(self,n):return tuple(tuple(self.ex.scalar(int(i==j))for j in range(n))for i in range(n))
    def shape(self,a):return len(a),len(a[0])
    def add(self,*aa):
        r,c=self.shape(aa[0]);out=self.zero(r,c)
        for a in aa:
            if self.shape(a)!=(r,c):raise ValueError('matrix addition shape')
            out=tuple(tuple(out[i][j]+a[i][j]for j in range(c))for i in range(r))
        return out
    def scale(self,a,c):return tuple(tuple(v*self.ex.scalar(Q(c))for v in row)for row in a)
    def mul(self,*aa):
        out=aa[0]
        for b in aa[1:]:
            r,k=self.shape(out);l,c=self.shape(b)
            if k!=l:raise ValueError('ordered matrix product shape')
            key=('matmul',r,k,c);self.events[key]=self.events.get(key,0)+1
            out=tuple(tuple(sum((out[i][j]*b[j][h]for j in range(k)),self.ex.scalar(0))for h in range(c))for i in range(r))
        return out
    def smul(self,s,a):return tuple(tuple(s[0][0]*v for v in row)for row in a)
    def transpose(self,a):return tuple(zip(*a))
    def trace(self,a):return ((sum((a[i][i]for i in range(len(a))),self.ex.scalar(0)),),)
    def tf(self,a):return self.add(a,self.smul(self.scale(self.trace(a),Q(-1,2)),self.eye(2)))
    def inverse(self,a):
        if self.shape(a)!=(2,2):raise ValueError('source adjugate only2x2')
        # Actual determinant-one theorem is an imported premise. Artificial
        # fixtures independently check their SL2 frames.
        return ((a[1][1],-a[0][1]),(-a[1][0],a[0][0]))
    def D(self,a,d):return tuple(tuple(v.V(d)for v in row)for row in a)
    def leaf(self,name,shape,**data):return self.model.leaf(name,shape,**data)


def raw_scalar_formula(mat,blocks_i,blocks_j,qa,qb):
    """Pinned globalBuild2.first: all4 block traces, both endpoint terms."""
    result=mat.ex.scalar(0);ta=qa*mat.ex.scalar(Q(1,2));tb=qb*mat.ex.scalar(Q(1,2))
    for k,sign,a_i,b_i,a_j,b_j in zip((-1,1,3,5),(-1,1,-1,1),*blocks_i,*blocks_j):
        wedge=mat.trace(mat.mul(a_i,b_j))[0][0]-mat.trace(mat.mul(b_i,a_j))[0][0]
        linear=(ta*(mat.trace(b_i)[0][0]+mat.trace(b_j)[0][0])-tb*(mat.trace(a_i)[0][0]+mat.trace(a_j)[0][0]))*mat.ex.scalar(k)
        result=result+(wedge+linear)*mat.ex.scalar(sign)
    return result*mat.ex.scalar(Q(1,4))-qa*qb*mat.ex.scalar(Q(15,8))


class PhysicalModel:
    """Fixed pinned HM primitive/raw source body; execution is hard held.

    _build_body is concrete code below, not an arbitrary source callback.
    It remains inaccessible under the current absent aggregate admission.
    """
    dims=(5,15,10,2)
    def __init__(self,ex,model):
        require_aggregate_admission()  # before storing/evaluating physical data
        self._build_body(ex,model)
    def _build_body(self,ex,model):
        require_aggregate_admission()  # direct private invocation also refuses
        self.ex=ex;self.M=Mat(ex);self.M.model=self;self.data=model
        self.x=[ex.x(i)for i in range(4)];self.y=[ex.y(i)for i in range(4)]
        self.v=[ex.scalar(1)]+[ex.scalar(0)for _ in range(4)]
        for x in self.x:
            for j in range(4,0,-1):self.v[j]=self.v[j]+x*self.v[j-1]
        one=[['0,0,0,0',1]]
        self.gamma=self.matrix(model['gamma'],one);self.delta=self.matrix(model['delta'],one);self.ev=self.matrix(model['ev'],one)
    def polynomial(self,terms):
        out=self.ex.scalar(0)
        for key,c in terms:
            e=tuple(map(int,key.split(',')));term=self.ex.scalar(Q(c))
            for i,n in enumerate(e):term=term*power(self.v[i+1],n)
            out=out+term
        return out
    def matrix(self,a,den):
        inv=self.polynomial(den).inverse()
        return tuple(tuple(self.polynomial(p)*inv for p in row)for row in a)
    @lru_cache(maxsize=None)
    def primitive(self,c):
        ch=self.data['charts'][c];out={k:self.matrix(ch[k],ch[d])for k,d in [('I','di'),('P','dp'),('H0','dh'),('H1','dh')]}
        p=ch['pivot'];W=[list(r)for r in self.M.zero(10,8)];eta=[list(r)for r in self.M.zero(10,2)];L=[list(r)for r in self.M.zero(8,10)]
        for h in range(2):
            eta[h*5+p][h]=self.v[p].inverse()
            for k in range(1,5):
                kk=(p+k)%5;col=h*4+k-1
                W[h*5+kk][col]=self.ex.scalar(1);W[h*5+p][col]=-self.v[kk]/self.v[p];L[col][h*5+kk]=self.ex.scalar(1)
        out.update(W=tuple(map(tuple,W)),eta=tuple(map(tuple,eta)),L=tuple(map(tuple,L)));return out
    @lru_cache(maxsize=None)
    def nu(self,o):
        out=self.ex.scalar(1)
        for i in range(4):
            if(o.legal_mask>>i)&1:out=out*(self.y[i]/self.x[i])
        return out
    def Dframe(self,o,inverse=False):
        n=self.nu(o);a,b=(n.inverse(),n)if inverse else(n,n.inverse());z=self.ex.scalar(0)
        return ((a,z),(z,b))
    @lru_cache(maxsize=None)
    def g(self,a,b):
        pa=self.primitive(a.carrier)['P'];ib=self.primitive(b.carrier)['I']
        return self.M.mul(self.Dframe(b),self.M.transpose(self.M.mul(pa,ib)),self.Dframe(a,True))
    def q(self,a,b,d):return self.ex.scalar(((b.legal_mask>>d)&1)-((a.legal_mask>>d)&1))*(self.y[d]/self.x[d])
    @lru_cache(maxsize=None)
    def blocks(self,o,d):
        c=self.primitive(o.carrier);n2=power(self.nu(o),2)
        U0=tuple(tuple(list(g)+list(i)+list(w))for g,i,w in zip(self.gamma,c['I'],self.M.mul(c['H1'],c['W'])))
        Q0=tuple(c['H0'])+tuple(c['P'])+tuple(self.M.mul(c['L'],self.delta))
        U1=tuple(tuple(list(w)+list(e))for w,e in zip(c['W'],c['eta']));Q1=tuple(c['L'])+tuple(self.ev)
        w0=[n2.inverse()]*5+[self.ex.scalar(1),n2.inverse()]+[n2]*8;w1=[self.ex.scalar(1)]*8+[n2]*2
        def moving(U,Q,w):
            U=tuple(tuple(v*w[j]for j,v in enumerate(row))for row in U)
            Q=tuple(tuple(v/w[i]for v in row)for i,row in enumerate(Q))
            return self.M.scale(self.M.mul(self.M.D(U,d),Q),-1)
        B0=moving(U0,Q0,w0);B1=moving(U1,Q1,w1)
        gamma=self.ex.scalar((o.legal_mask>>d)&1)*self.y[d]/(self.x[d]*(self.x[d]*self.x[d]-self.ex.scalar(1)))
        out=[]
        for dim,k,B in zip(self.dims,(-1,1,3,5),(None,B0,B1,None)):
            B=B or self.M.zero(dim,dim);out.append(self.M.add(B,self.M.scale(self.M.smul(((gamma,),),self.M.eye(dim)),-k)))
        return tuple(out)
    @lru_cache(maxsize=None)
    def s_raw(self,p,a,b):
        u,v=p
        return raw_scalar_formula(self.M,(self.blocks(a,u),self.blocks(a,v)),(self.blocks(b,u),self.blocks(b,v)),self.q(a,b,u),self.q(a,b,v))
    def leaf(self,name,shape,**data):
        if name=='g_phys':return self.g(*data['owners'])
        if name=='physical_q':return ((self.q(*data['owners'],data['coordinate']),),)
        o=data['owner'];c=self.primitive(o.carrier)
        # Common scalar nu factors in actual Iphys/Pphys cancel in j and IP.
        if name=='I_phys':return self.M.mul(c['I'],self.Dframe(o))
        if name=='P_phys':return self.M.mul(self.Dframe(o,True),c['P'])
        return c[name]


class RawSource(SC.Source):
    def T(self,p,a,b):return ((self.c.model.s_raw(tuple(p),a,b),),)


def source_and_lift(model,owners,stage=2):
    """Actual literal source and accepted block HPL recurrence; no callbacks."""
    M=model.M;M.model=model;source=RawSource(M)
    schema=load('sr01_lift_schema',BASE/'transport-binding/lift_schema.py').closed_lift_schema()
    lift=SC.Lift(M,source.residual,schema,dims=model.dims)
    return source,lift.at(stage,tuple(owners))

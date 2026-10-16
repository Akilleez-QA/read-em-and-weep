"""Demand-only exact polynomial coefficients; matrix lowering is ordered metadata.
Physical catalogs are structurally bindable but every coefficient call fails closed.
"""
from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import combinations,product
from interfaces import FullOwner,need,exponent,require_synthetic,sorted_source

@dataclass
class Budget:
    max_queries:int=100000
    max_splits:int=200000
    max_cache:int=100000
    max_nodes:int=40000
    max_owner_terms:int=4096
    queries:int=0
    splits:int=0
    owner_terms:int=0
    def debit(self,kind,n=1):
        need(type(n)is int and n>=0,'budget debit')
        setattr(self,kind,getattr(self,kind)+n)
        need(getattr(self,kind)<=getattr(self,'max_'+kind),'synthetic shared budget exhausted: '+kind)

class Ring:
    def __init__(self,mode,budget):self.mode=mode;self.budget=budget;self.nodes=[];self.ids={};self.cache={};self.bounds={}
    def node(self,op,*args):
        key=(op,*args)
        if key not in self.ids:
            need(len(self.nodes)<self.budget.max_nodes,'metadata node cap');self.ids[key]=len(self.nodes);self.nodes.append(key)
        return self.ids[key]
    def const(self,c):c=Q(c);return self.node('constant',c.numerator,c.denominator)
    def x(self,i):need(type(i)is int and 0<=i<4,'axis');return self.node('coordinate',i)
    def elementary(self,k):need(type(k)is int and 0<=k<=4,'elementary index');return self.node('elementary',k)
    def plus(self,*a):return self.node('sum',tuple(a))
    def times(self,*a):
        if not a:return self.const(1)
        out=a[0]
        for b in a[1:]:out=self.node('product',out,b)
        return out
    def power(self,a,n):need(type(n)is int and n>=0,'nonnegative polynomial power');return self.node('power',a,n)
    def partial(self,a,i):need(type(i)is int and 0<=i<4,'derivative coordinate');return self.node('partial',a,i)
    def polynomial(self,terms):
        return self.plus(*(self.times(self.const(c),*(self.power(self.x(i),e)for i,e in enumerate(exponent(m))if e))for m,c in terms.items()))
    def bound(self,r):
        if r in self.bounds:return self.bounds[r]
        op,*a=self.nodes[r]
        if op=='constant':b=None if a[0]==0 else(0,0,0,0)
        elif op=='coordinate':b=tuple(int(i==a[0])for i in range(4))
        elif op=='elementary':b=(0,0,0,0)if a[0]==0 else(1,1,1,1)
        elif op=='sum':
            bs=[self.bound(v)for v in a[0]];bs=[v for v in bs if v is not None]
            b=tuple(max(v[i]for v in bs)for i in range(4))if bs else None
        elif op=='product':
            l,h=self.bound(a[0]),self.bound(a[1]);b=None if l is None or h is None else tuple(x+y for x,y in zip(l,h))
        elif op=='power':
            v=self.bound(a[0]);b=(0,0,0,0)if a[1]==0 else None if v is None else tuple(a[1]*x for x in v)
        elif op=='partial':
            v=self.bound(a[0]);b=None if v is None or v[a[1]]==0 else tuple(x-int(i==a[1])for i,x in enumerate(v))
        else:raise ValueError('unknown polynomial node')
        self.bounds[r]=b;return b
    def coefficient(self,r,e):
        require_synthetic(self.mode);return self._coefficient(r,exponent(e))
    def _coefficient(self,r,e):
        require_synthetic(self.mode);key=(r,e)
        if key in self.cache:return self.cache[key]
        self.budget.debit('queries');b=self.bound(r)
        if b is None or any(x<0 or x>h for x,h in zip(e,b)):return Q(0)
        op,*a=self.nodes[r]
        if op=='constant':out=Q(a[0],a[1])if not any(e)else Q(0)
        elif op=='coordinate':out=Q(int(e==tuple(int(i==a[0])for i in range(4))))
        elif op=='elementary':out=Q(int(all(x in(0,1)for x in e)and sum(e)==a[0]))
        elif op=='sum':out=sum((self._coefficient(n,e)for n in a[0]),Q(0))
        elif op=='partial':
            ee=list(e);ee[a[1]]+=1;out=(e[a[1]]+1)*self._coefficient(a[0],tuple(ee))
        elif op=='power':
            base,n=a
            out=Q(int(not any(e)))if n==0 else self._coefficient(base,e)if n==1 else self._coefficient(self.times(self.power(base,n//2),self.power(base,n-n//2)),e)
        elif op=='product':
            left,right=a;lo,hi=self.bound(left),self.bound(right);out=Q(0)
            if lo is not None and hi is not None:
                ranges=[range(max(0,e[i]-hi[i]),min(e[i],lo[i])+1)for i in range(4)]
                for u in product(*ranges):
                    self.budget.debit('splits');v=tuple(x-y for x,y in zip(e,u))
                    out+=self._coefficient(left,u)*self._coefficient(right,v)
        else:raise ValueError('unknown coefficient operation')
        need(len(self.cache)<self.budget.max_cache,'synthetic cache cap');self.cache[key]=out;return out

@dataclass(frozen=True)
class Scalar:
    node:int

class Catalog:
    """Sparse STORED v1..v4 numerators plus synthetic or unexecuted physical H."""
    def __init__(self,mode,charts,synthetic_H=None):self.mode=mode;self.charts=charts;self.synthetic_H=synthetic_H
    def H(self,owner,ring):
        if self.mode=='synthetic':
            need(self.synthetic_H is not None,'synthetic H oracle required');return ring.polynomial(self.synthetic_H[owner.carrier])
        v=[ring.elementary(k)for k in range(5)];a=ring.times(v[1],v[3],v[4])
        return a if owner.carrier==5 else ring.plus(ring.power(v[owner.carrier],5),ring.times(ring.const(-1),*v))
    def cleared(self,owner,name,ring):
        data=self.charts[owner.carrier][name];need(name in('P','I'),'catalog block')
        multiplier=ring.times(ring.const(-1),ring.elementary(3),ring.elementary(4))if owner.carrier==5 else ring.times(ring.const(-1),self.H(owner,ring))
        out=[]
        for row in data:
            rr=[]
            for terms in row:
                children=[]
                for powers,c in terms:
                    es=tuple(map(int,powers.split(',')));need(len(es)==4 and min(es)>=0,'stored numerator exponents')
                    children.append(ring.times(ring.const(c),*(ring.power(ring.elementary(k+1),n)for k,n in enumerate(es)if n)))
                rr.append(Scalar(ring.times(multiplier,ring.plus(*children))))
            out.append(rr)
        return out

def shape(v):return()if isinstance(v,Scalar)else(len(v),len(v[0]))
def scale(v,c,R):return Scalar(R.times(R.const(c),v.node))if isinstance(v,Scalar)else[[scale(x,c,R)for x in row]for row in v]
def plus(values,R):
    need(bool(values),'empty matrix sum');s=shape(values[0]);need(all(shape(v)==s for v in values),'sum shape mismatch')
    return Scalar(R.plus(*(v.node for v in values)))if not s else[[plus([v[i][j]for v in values],R)for j in range(s[1])]for i in range(s[0])]
def times(a,b,R):
    if isinstance(a,Scalar):return Scalar(R.times(a.node,b.node))if isinstance(b,Scalar)else[[times(a,x,R)for x in row]for row in b]
    if isinstance(b,Scalar):return[[times(x,b,R)for x in row]for row in a]
    need(shape(a)[1]==shape(b)[0],'ordered matrix product mismatch')
    return[[plus([times(a[i][k],b[k][j],R)for k in range(len(b))],R)for j in range(len(b[0]))]for i in range(len(a))]
def partial(v,i,R):return Scalar(R.partial(v.node,i))if isinstance(v,Scalar)else[[partial(x,i,R)for x in row]for row in v]

class ClearedSourceProgram:
    def __init__(self,nodes,root,catalog,owners,budget=None):
        need(len(owners)==3 and all(isinstance(v,FullOwner)for v in owners),'source triple')
        need(tuple(owners)==sorted_source(owners)[0],'source must already be sorted; use alternating wrapper once')
        need(type(nodes)is list and len(nodes)<=4000 and type(root)is int and 0<=root<len(nodes),'source DAG')
        self.mode=catalog.mode;self.catalog=catalog;self.owners=tuple(owners);self.budget=budget or Budget();self.ring=Ring(self.mode,self.budget);R=self.ring;values=[]
        for index,(op,*args)in enumerate(nodes):
            def child(i):need(type(i)is int and 0<=i<index,'topological source DAG');return values[i]
            if op=='catalog_cleared_primitive':v=catalog.cleared(owners[args[0]],args[1],R)
            elif op=='owned_polynomial_factor':
                slot,kind,axis=args[0];o=owners[slot]
                if kind=='H':v=Scalar(catalog.H(o,R))
                else:
                    need(kind=='ell'and type(axis)is int and 0<=axis<4,'owned factor');m=(o.legal_mask>>axis)&1
                    v=Scalar(R.plus(R.power(R.x(axis),3),R.times(R.const(-1),R.x(axis))))if m else Scalar(R.const(1))
            elif op=='mask_times_x_squared_plus_one_over_two':
                slot,axis=args;m=(owners[slot].legal_mask>>axis)&1;v=Scalar(R.times(R.const(Q(m,2)),R.plus(R.power(R.x(axis),2),R.const(1))))
            elif op=='binary_mask_q_numerator':
                a,b,axis,sign=args;ma=(owners[a].legal_mask>>axis)&1;mb=(owners[b].legal_mask>>axis)&1
                c=mb*(1-ma)if sign==1 else-ma*(1-mb)
                v=Scalar(R.times(R.const(c),R.plus(R.power(R.x(axis),2),R.const(-1))))
            elif op=='polynomial_diagonal':
                a=child(args[0]);need(isinstance(a,Scalar),'diagonal scalar');z=Scalar(R.const(0));v=[[a,z],[z,scale(a,-1,R)]]
            elif op=='transpose':a=child(args[0]);need(bool(shape(a)),'transpose matrix');v=[list(x)for x in zip(*a)]
            elif op=='trace':a=child(args[0]);need(shape(a)[0]==shape(a)[1],'square trace');v=plus([a[i][i]for i in range(len(a))],R)
            elif op=='scale':n,d,a=args;need(type(n)is int and type(d)is int and d!=0,'rational scale');v=scale(child(a),Q(n,d),R)
            elif op=='sum':v=plus([child(a)for a in args],R)
            elif op=='ordered_product':
                v=Scalar(R.const(1))
                for a in args:v=times(v,child(a),R)
            elif op=='power':
                a,n=args;a=child(a);need(isinstance(a,Scalar),'scalar owned polynomial power');v=Scalar(R.power(a.node,n))
            elif op=='polynomial_partial_after_elementary_substitution':a,i=args;v=partial(child(a),i,R)
            else:raise ValueError('unsupported actual source operation '+op)
            values.append(v)
        self.root=values[root];need(isinstance(self.root,Scalar),'cleared F root scalar')
    def degree_upper(self):return self.ring.bound(self.root.node)
    def coefficient(self,e):
        require_synthetic(self.mode)
        if len({o.physical_key for o in self.owners})<3:return Q(0)
        return self.ring.coefficient(self.root.node,e)

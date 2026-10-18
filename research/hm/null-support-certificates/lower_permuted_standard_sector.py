"""Selected full-owner E12 rational-to-factored-Laurent lowering; no evaluation.

Physical source polynomials remain factored arithmetic DAGs. Outer multinomial
sums remain bounded integer-index sum nodes, never enumerated.
"""
from pathlib import Path
from itertools import combinations
from math import comb
import json, hashlib
import owned_scalar_denominator_binding as owned
import physical_current_source_binding as source
import outer_partition_source_binding as outer

def contraction_certificate():
    """Read-only provenance check; never executes the historical polynomial checker."""
    hashes={'pinned-homogeneous-identities.json':'55e78bbc838a971b64531379788192acf8877c04f2d797fb13b4f4a68e47b018',
            'pinned-verify-homogeneous-identities.py.txt':'ad6fdb925262b9661bd51c0f65fe1a48d8f4ab1927bbf14b23786a4f0e1503bf'}
    blobs={'pinned-homogeneous-identities.json':'e55dae1fccef9b66bd5735b04fc09bd5590180fc','pinned-verify-homogeneous-identities.py.txt':'25816d9ba8699ffaf20c562d9dd8403f049ae383'}
    for filename,digest in hashes.items():
        raw=Path(__file__).with_name(filename).read_bytes()
        if hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()!=blobs[filename]:raise ValueError('pinned Git blob changed')
        if hashlib.sha256(Path(__file__).with_name(filename).read_bytes()).hexdigest()!=digest:raise ValueError('contraction certificate provenance changed')
    cert=json.loads(Path(__file__).with_name('pinned-homogeneous-identities.json').read_text())
    canonical=hashlib.sha256(json.dumps(source.authenticate(),separators=(',',':')).encode()).hexdigest()
    if cert['modelSha256']!=canonical:raise ValueError('contraction certificate model mismatch')
    identities={'E_identity':1350,'P_I':24,'delta_I':120,'P_gamma':60}
    if any(cert['byIdentity'].get(k)!=v for k,v in identities.items()):raise ValueError('missing contraction identity')
    return {'status':'existing pinned source certificate verified by read-only provenance and canonical model binding',
            'canonical_model_sha256':canonical,'files_sha256':hashes,'git_blobs':blobs,'identities':identities,'historical_checker_executed_now':False,
            'proof_specialization':'E_b=Id-gamma H0_b-H1_b delta; P_a gamma=0; delta I_a=0; P_a I_a=Id'}

def composition_sum(g,dimension,j,T,cs,vl):
    s=dimension-1;L=dimension*(T-1)+1
    domain={'dimension':s+1,'total':L,'chosen':j,'threshold':T,'earlier_upper':T-1}
    body={'coefficient':{'op':'multiply_binomials','factors':[{'top':{'constant':L,'coefficients':[-1 if h<i else 0 for h in range(s+1)]},'bottom':{'constant':0,'coefficients':[int(h==i) for h in range(s+1)]}} for i in range(s+1)]},
          'powers':[{'base':base,'exponent':{'constant':offset,'coefficients':[int(h==i) for h in range(s+1)]}} for i in range(s+1) for base,offset in ((cs[i],0),(vl[i],-T if i==j else 0))]}
    return g.node('bounded_composition_sum',domain,body)

class DAG:
    def __init__(self): self.nodes=[]; self.ids={}; self.derivatives={}
    def node(self,op,*args):
        key=json.dumps([op,*args],sort_keys=True,separators=(',',':'))
        if key not in self.ids:
            self.ids[key]=len(self.nodes);self.nodes.append([op,*args])
        return self.ids[key]
    def c(self,n,d=1):return self.node('rational',n,d)
    def add(self,*xs):
        xs=tuple(x for x in xs if x!=self.c(0))
        return self.c(0) if not xs else xs[0] if len(xs)==1 else self.node('add',*xs)
    def mul(self,*xs):
        if self.c(0) in xs:return self.c(0)
        xs=tuple(x for x in xs if x!=self.c(1))
        return self.c(1) if not xs else xs[0] if len(xs)==1 else self.node('multiply',*xs)
    def pow(self,x,n):return self.c(1) if n==0 else x if n==1 else self.node('power',x,n)
    def diff(self,x,d):
        key=(x,d)
        if key in self.derivatives:return self.derivatives[key]
        op,*a=self.nodes[x]
        if op=='rational':r=self.c(0)
        elif op=='coordinate':r=self.c(int(a[0]==d))
        elif op=='add':r=self.add(*(self.diff(t,d) for t in a))
        elif op=='multiply':r=self.add(*(self.mul(*(self.diff(t,d) if j==i else t for j,t in enumerate(a))) for i in range(len(a))))
        elif op=='power':r=self.mul(self.c(a[1]),self.pow(a[0],a[1]-1),self.diff(a[0],d))
        else:raise ValueError('unlowered differentiation '+op)
        self.derivatives[key]=r;return r

class Lower:
    def __init__(self,vertices):
        keys=[(v.carrier,v.legal_mask,v.standard_tag) for v in vertices]
        if keys!=sorted(keys) or len(set(keys))!=3:raise ValueError('source-first distinct owners required')
        if sorted(v.standard_tag for v in vertices)!=[3,11,15]:raise ValueError('selected staircase multiset only')
        self.g=DAG();self.vs=vertices;self.model=source.authenticate();self.factors={};self.blocks={}
        g=self.g;self.x=[g.node('coordinate',i) for i in range(4)]
        self.v=[g.c(1)]+[g.add(*(g.mul(*(self.x[i] for i in inds)) for inds in combinations(range(4),k))) for k in range(1,5)]
        for v in vertices:
            if v.carrier not in range(1,5):raise ValueError('selected source-first carrier1 sector only')
            for name in ('di','dp','dh'):
                got={tuple(map(int,e.split(','))):c for e,c in self.model['charts'][v.carrier][name]}
                exponent=tuple(5 if i==v.carrier-1 else 0 for i in range(4))
                if got!={(1,1,1,1):1,exponent:-1}:raise ValueError('pinned denominator is not -H')
            self.factors[self.key(v,'H')]=g.add(g.pow(self.v[v.carrier],5),g.mul(g.c(-1),*self.v))
            for i in range(4):
                self.factors[self.key(v,'L',i)]=g.mul(self.x[i],g.add(g.pow(self.x[i],2),g.c(-1)))
                self.factors[self.key(v,'Z',i)]=self.x[i]
    def key(self,v,kind,i=None):return json.dumps([list(v.data()),kind,i],separators=(',',':'))
    def rat(self,n,den=None):return (n,{k:e for k,e in (den or {}).items() if e})
    def mul(self,a,b):
        d=a[1].copy()
        for k,e in b[1].items():d[k]=d.get(k,0)+e
        return self.rat(self.g.mul(a[0],b[0]),d)
    def add(self,a,b):
        d={k:max(a[1].get(k,0),b[1].get(k,0)) for k in sorted(a[1].keys()|b[1].keys())}
        def lift(r):return self.g.mul(r[0],*(self.g.pow(self.factors[k],e-r[1].get(k,0)) for k,e in d.items()))
        return self.rat(self.g.add(lift(a),lift(b)),d)
    def neg(self,a):return self.rat(self.g.mul(self.g.c(-1),a[0]),a[1])
    def diff(self,a,i):
        out=self.rat(self.g.diff(a[0],i),a[1])
        for k,e in a[1].items():
            d=a[1].copy();d[k]+=1
            out=self.add(out,self.rat(self.g.mul(self.g.c(-e),a[0],self.g.diff(self.factors[k],i)),d))
        return out
    def poly(self,p):
        g=self.g
        return g.add(*(g.mul(g.c(c),*(g.pow(self.v[i+1],e) for i,e in enumerate(map(int,exps.split(','))))) for exps,c in p))
    def block(self,v,name):
        key=(v,name)
        if key not in self.blocks:
            self.blocks[key]=[[self.rat(self.g.mul(self.g.c(-1),self.poly(p)),{self.key(v,'H'):1}) for p in row] for row in self.model['charts'][v.carrier][name]]
        return self.blocks[key]
    def mm(self,a,b):
        out=[]
        for row in a:
            result=[]
            for col in zip(*b):
                val=self.rat(self.g.c(0))
                for x,y in zip(row,col):val=self.add(val,self.mul(x,y))
                result.append(val)
            out.append(result)
        return out
    def ma(self,a,b):return [[self.add(x,y) for x,y in zip(r,s)] for r,s in zip(a,b)]
    def mn(self,a):return [[self.neg(x) for x in r] for r in a]
    def core(self,a,b):return list(map(list,zip(*self.mm(self.block(a,'P'),self.block(b,'I')))))
    def log(self,v,d):
        z=self.rat(self.g.c(0))
        if not owned.decode_legal_mask(v.legal_mask)[d]:return [[z,z],[z,z]]
        ell=self.rat(self.g.mul(self.g.c(1,2),self.g.add(self.g.pow(self.x[d],2),self.g.c(1))),{self.key(v,'L',d):1})
        return [[ell,z],[z,self.neg(ell)]]
    def tangent(self,a,b,d):
        k=self.core(a,b)
        return self.ma(self.ma([[self.diff(x,d) for x in r] for r in k],self.mm(self.log(b,d),k)),self.mn(self.mm(k,self.log(a,d))))
    def current(self,kind,d):
        a,b,c=self.vs
        if kind=='L':return self.mm(self.core(b,a),self.tangent(a,b,d))
        return self.mm(self.mm(self.mm(self.core(b,a),self.core(c,b)),self.tangent(b,c,d)),self.core(a,b))
    def tracefree(self,R):
        half=self.mul(self.rat(self.g.c(1,2)),self.add(R[0][0],R[1][1]))
        return [[self.add(R[i][j],self.neg(half)) if i==j else R[i][j] for j in range(2)] for i in range(2)]
    def edge_inverse(self,edge):
        den={}
        for o in edge:
            v=self.vs[o];den[self.key(v,'H')]=14
            for i,bit in enumerate(owned.decode_legal_mask(v.legal_mask)):
                if bit:den[self.key(v,'L',i)]=1
            for i,bit in enumerate(owned.decode_standard_tag(v.standard_tag)):
                if bit:den[self.key(v,'Z',i)]=5250
        return self.rat(self.g.c(1),den)
    def quotient(self,v):
        """Exact finite-sum AST in local coordinates, pulled back once to x.
        Composition sum body is a typed template with integer affine powers.
        No physical sum is enumerated.
        """
        g=self.g;bits=owned.decode_standard_tag(v.standard_tag);s=sum(bits)
        xs=[g.pow(x,-1) if bit else x for x,bit in zip(self.x,bits)]
        vl=[]
        for j in range(5):
            vl.append(g.add(*(g.mul(*(g.c(1) if bits[i] else xs[i] for i in A),*(xs[i] if bits[i] else g.c(1) for i in range(4) if i not in A)) for A in combinations(range(4),j))))
        av=g.mul(vl[0],vl[1],vl[3],vl[4]);h=g.add(g.pow(vl[v.carrier],5),g.mul(g.c(-1),*vl))
        if v.carrier>s or (s==4 and v.carrier!=4):return g.c(0)
        # Complete homogeneous polynomials H_k for k<=4, tiny combinatorial
        # definitions remain factored monomial sums, never x-expanded.
        finite=[xs[i] for i in range(4) if not bits[i]]
        def complete(k,start=0):
            if k==0:return g.c(1)
            return g.add(*(g.mul(finite[i],complete(k-1,i)) for i in range(start,len(finite))))
        cs=[g.mul(g.c((-1)**(s-i)),complete(s-i)) for i in range(s+1)]
        T=535;L=(s+1)*(T-1)+1;j=v.carrier
        B=composition_sum(g,s+1,j,T,cs,vl[:s+1])
        C=g.add(*(g.mul(g.c(comb(107,k)),g.pow(h,k-54),g.pow(g.mul(vl[2],av),107-k)) for k in range(54,108)))
        out=g.mul(B,C)
        for i,bit in enumerate(bits):
            m=owned.decode_legal_mask(v.legal_mask)[i]
            if not bit:
                if m:return g.c(0)
                continue
            t=xs[i];q=g.add(g.c(1),g.mul(g.c(-1),g.pow(t,2)))
            if m:line=g.add(*(g.mul(g.c(comb(57,k)),g.pow(t,2*k),g.pow(q,57-k-29)) for k in range(29)))
            else:line=g.add(*(g.mul(g.c(comb(57,k)),g.pow(t,2*k-29),g.pow(q,57-k)) for k in range(29,58)))
            out=g.mul(out,line)
        return out
    def cancel(self,r):
        g=self.g;parts=[r[0]];ledger=[]
        if not set(r[1])<=set(self.factors):raise ValueError('unmatched denominator owner')
        for v in self.vs:
            H=r[1].get(self.key(v,'H'),0);Ls=[r[1].get(self.key(v,'L',i),0) for i in range(4)];Zs=[r[1].get(self.key(v,'Z',i),0) for i in range(4)]
            if any(Zs[i] and not owned.decode_standard_tag(v.standard_tag)[i] for i in range(4)):raise ValueError('unmatched standard factor')
            if H>54 or max(Ls)>29 or max(Zs)>5251:raise ValueError('AST-derived denominator exceeds outer clearance')
            parts.extend([self.quotient(v),g.pow(self.factors[self.key(v,'H')],54-H)])
            for i,m in enumerate(owned.decode_legal_mask(v.legal_mask)):
                if m:parts.append(g.pow(self.factors[self.key(v,'L',i)],29-Ls[i]))
                elif Ls[i]:raise ValueError('unowned legal divisor')
                parts.append(g.pow(self.x[i],-Zs[i]))
                if owned.decode_standard_tag(v.standard_tag)[i]:
                    parts.append(g.pow(self.x[i],-(5*54+(3 if m else 1)*29)))
            ledger.append({'owner':v.data(),'carrier':H,'legal':Ls,'standard':Zs})
        return {'root':g.mul(*parts),'derived_denominators':ledger}

def build(masks=(0,0,0), carriers=(1,2,4), standards=(11,3,15)):
    if len(masks)!=3 or any(type(m) is not int or not 0<=m<16 for m in masks):raise ValueError('three legal masks required')
    if len(carriers)!=3 or any(type(b) is not int or b not in range(1,5) for b in carriers):raise ValueError('primary carriers 1..4 only; star5 not implemented')
    outer.authenticate_public_sources()
    inverse_certificate=contraction_certificate()
    vs=tuple(owned.VertexLabel(4,o,b,m,t) for o,(b,m,t) in enumerate(zip(carriers,masks,standards)))
    lo=Lower(vs);g=lo.g;v=lo.v
    terms=[]
    for edge,d,kind,c,sign in (((1,2),0,'L',1,1),((1,2),1,'L',0,-1),((0,1),1,'U',0,1),((0,1),0,'U',1,-1)):
        R=lo.tracefree(lo.current(kind,c))
        # Use the full pinned selected entry, avoiding an additional unproved
        # trace-free shortcut for each isolated current summand.
        I=lo.block(vs[0],'I');P=lo.block(vs[0],'P')
        contraction=lo.rat(g.c(0))
        for u in range(2):
            for w in range(2):contraction=lo.add(contraction,lo.mul(lo.mul(I[12][u],R[w][u]),P[w][6]))
        C=lo.mul(lo.rat(g.c(-2*sign,2)),contraction)
        inv=lo.edge_inverse(edge)
        terms.append({'edge':edge,'coordinate':d,'current':[kind,c],'E_sign':sign,'A':lo.cancel(lo.mul(C,lo.diff(inv,d))),'B':lo.cancel(lo.mul(C,inv))})
    return {'schema':'selected-full-owner-kernel-lowering-v1','scope':'one parameterized source-first primary-carrier full-owner tuple, seed4 row2 standard permutation of(3,11,15), all four E12 terms; star5 excluded','owners':[v.data() for v in vs],'sorting_sign':(-1)**sum(standards[i]>standards[j] for i in range(3) for j in range(i+1,3)),'staircase':[3,11,15],'selector_terminal_coefficient_included_once':-2,'selector_rule':'full pinned -2*(I_a transpose(tf(R)) P_a)[12,6]; tf(R)=R-tr(R)/2 Id explicitly; no assumption tr(R)=0','frame':'global finite; normalized current after matching physical conjugation cancellation; outer scalar weights pulled back once; no section twist on scalar rho','transition_inverse_rewrite':{'rule':'inverse(C_ab)=C_ba','C_ab':'transpose(P_a I_b)','proof':'P_a I_a=Id; d I_a=0; P_a d=0; I_b P_b=Id-dH_b-H_bd imply (P_a I_b)(P_b I_a)=Id and reverse. Transposition gives C_ba C_ab=Id and C_ab C_ba=Id.','source_certificate':inverse_certificate},'dag':g.nodes,'terms':terms,'unresolved':['Independently verify the bounded-composition-sum lowering and full-owner pullback certificate.','Extend to every remaining full-owner label in the selected symbolic sector and then other kernel sectors.','Supply arithmetic schedule and peak-byte certificate before admission.'],'actual_factorization_accepted':False,'execution_release':False,'physical_polynomial_expansion':False,'physical_polynomial_evaluation':False,'held_limits':{'private_resource_configuration_omitted':True},'pinned_model_sha256':source.MODEL_SHA256}


#!/usr/bin/env python3
"""Executable symbolic dependency traversal; no physical source arithmetic."""
import json, hashlib
from collections import Counter

BOX = [[-1668,5248]]*4
FRAME = 'common-finite-frame'
class ContractError(ValueError): pass

def bits(v): return tuple((v >> (3-i)) & 1 for i in range(4))
def vertex(b): return sum(x << (3-i) for i,x in enumerate(b))
def triangles(edge):
    a,b=edge; z=vertex(tuple(min(x,y) for x,y in zip(bits(a),bits(b))))
    raw=[(1,(z,a,b))]; cur=list(bits(a))
    for d in (3,2,1,0):
        if cur[d]!=bits(b)[d]:
            old=vertex(cur);cur[d]=bits(b)[d];raw.append((-1,(z,old,vertex(cur))))
    out=Counter()
    for sign,t in raw:
        if len(set(t))<3: continue
        sign*=(-1)**sum(t[i]>t[j] for i in range(3) for j in range(i+1,3))
        out[tuple(sorted(t))]+=sign
    return [(s,list(t)) for t,s in sorted(out.items()) if s]

def ah_paths(edge,pair):
    """Threshold predicates retain symbolic eta; impossible chart cases pruned."""
    a,b=map(bits,edge); n=[-2 if i in pair else 0 for i in range(4)];out=[]
    for d in range(4):
        if a[d]==b[d]:continue
        cell=['B' if x else 'A' for x in a[:d]]+['C']+['B' if x else 'A' for x in b[d+1:]]
        for j in range(4):
            if cell[j]=='C':continue
            conditions=[];target=cell[:];sign=1 if a[d]<b[d] else -1;valid=True
            for i in range(j):
                if n[i]==0:
                    if cell[i]=='C':valid=False;break
                    conditions.append([i,'eq',0]);target[i]='B'
                else:
                    if cell[i]!='C':valid=False;break
                    conditions.append([i,'eq',-1])
            if not valid:continue
            if cell[j]=='A':conditions.append([j,'ge',0]);sign*=-1
            else:conditions.append([j,'le',min(-1,n[j])])
            sign*=(-1)**cell[:j].count('C');target[j]='C'
            active=[i for i,x in enumerate(target) if x=='C']
            if len(active)!=2:raise ContractError('degree mismatch')
            for perm,sgn in ((active,1),(active[::-1],-1)):
                cur=[int(x=='B') for x in target];vs=[vertex(cur)]
                for i in perm:cur[i]=1;vs.append(vertex(cur))
                out.append({'sign':sign*sgn,'standard':vs,'eta_guards':conditions,'eta_box':BOX,'cell':''.join(target)})
    return out

class DAG:
    def __init__(self):self.nodes=[]
    def add(self,op,inputs=(),**kw):
        node={'id':len(self.nodes),'op':op,'inputs':list(inputs),**kw};self.nodes.append(node);return node['id']
    def source(self,name,tuple_,**kw):
        frame=('bare-carrier-rank2' if name.startswith('selector_') else 'scalar-character' if name.startswith('F_') else 'true-physical-unnormalized-line-constants')
        return self.add('source_leaf',name=name,tuple=list(tuple_),source_frame=frame,pointwise_nu_normalization=False,**kw)
    def solver(self,pair,edge):
        tag='p' if pair==(0,1) else 'q';a,b=edge;std={'a':3,'b':11,'c':15};se=(std[a],std[b]);paths=[]
        for sign,tup,labels in ((1,('u',a,b),['u']),(-1,('u','v',b),['u','v'])):
            leaf=self.source('F_'+tag,tup,alternating_sort='source-first; retain permutation sign',domain='rational_pending')
            paths.append(self.add('inserted_partition_sum',[leaf],sign=sign,labels=labels,standard_tags=[se[0]]+([se[1]] if len(labels)==2 else []),partition=['inner',14,1],required='exact inserted-denominator cancellation before derivative'))
        for sign,tup in triangles(se):
            leaf=self.source('F_'+tag,('z0','z1','z2'),domain='rational_pending')
            paths.append(self.add('Pi_inner',[leaf],standard=tup,sign=sign,eta_box=BOX,partition=['inner',14,1]))
        ah=[]
        for path in ah_paths(se,pair):
            leaf=self.source('F_'+tag,('z0','z1','z2'),domain='rational_pending')
            ah.append(self.add('Pi_inner_coefficient_family',[leaf],**path,partition=['inner',14,1],coefficient='eta',state='blocked_until_exact_quotient'))
        paths+=ah
        return self.add('T_edge',paths,pair=tag,edge=list(edge),standard_edge=list(se),K_survivors=len(triangles(se)),AHS_survivors=len(ah),frame=FRAME)
    def residual(self,entry):
        tail=('a','b','c');parts=[self.source('M0_tracefree',tail,entry=entry,baseline='full gerbe retained')]
        for f,k in (('q','p'),('p','q')):
            F=self.source('F_'+f,tail,domain='rational_pending')
            K=self.source('k_'+k,('a','c'),entry=entry,domain='rational_pending')
            parts.append(self.add('multiply',[F,K],owners=['a','b','c']))
        for current_pair,scalar_pair in (((0,1),(2,3)),((2,3),(0,1))):
            x,y=current_pair
            for edge,d,current,sign in ((('b','c'),x,('L',y),1),(('b','c'),y,('L',x),-1),(('a','b'),y,('U',x),1),(('a','b'),x,('U',y),-1)):
                T=self.solver(scalar_pair,edge)
                D=self.add('derivative_request',[T],coordinate=d,state='rational_pending',required_order=['cancel_inserted','differentiate_regularized'],coefficient_pullback={'requested':'xi','input':'eta=xi+unit(d)','factor':'xi[d]+1'},ready=False)
                C=self.source('current_'+current[0],tail if current[0]=='U' else ('a','b'),coordinate=current[1],entry=entry,domain='rational_pending')
                parts.append(self.add('multiply',[C,D],coefficient=[sign,2],owners=['a','b','c']))
        return self.add('sum',parts,entry=entry)

def build():
    g=DAG();rs=[g.residual([1,0]),g.residual([0,0])];terms=[]
    for R,col,sign in zip(rs,(0,1),(-2,2)):
        R=g.add('rank2_frame_conversion',[R],owner='a',from_frame='physical-normalized-rank2',to_frame='bare-carrier-rank2',entry=[1,0] if col==0 else [0,0],factor='nu(a)^2' if col==0 else '1',identity='Rbar=D_a^-1 Rphysical D_a; D_a=diag(nu(a),nu(a)^-1)',state='formal_factor_pending')
        I=g.source('selector_homogeneous',('a',),column=col,expression='2*v1*(v1^2*v4+v0*v3^2)/h1' if col==0 else '2*v0*v1*(v0*v1^2+v2^2*v3)/h1',homogeneous_weight=-1 if col==0 else 0)
        terms.append(g.add('owned_weighted_coefficient',[I,R],coefficient=1,extra_factor='none',outer_partition=['outer',54,29],weighted_owners=['a','b','c'],kappa=[-1,-2,-2,-2],state='rational_pending'))
    root=g.add('sum',terms)
    return {'schema':'hm-selected-demand-dag-v1','scope':{'row':2,'staircase':[3,11,15],'orientation':1,'sector':'already source-first (a,b,c), carrier(a)=1','tail_carriers_may_repeat':True,'uncovered':'other staircase and source-first sorting sectors'},'root':root,'nodes':g.nodes,'support_certificates':{'Pi_inner_F':BOX,'Rsharp_owned_poles':{'carrier':32,'legal':18,'standard_boundary':5251},'outer_partition':[54,29]},'selector_identity':{'chart':'v0=1; restore homogeneous frame before coefficient extraction','Rbar10':'2*v1*(v1^2*v4+v3^2)/h1','Rbar00':'2*v1*(v1^2+v2^2*v3)/h1','homogeneous_Rbar10':'2*v1*(v1^2*v4+v0*v3^2)/h1','homogeneous_Rbar00':'2*v0*v1*(v0*v1^2+v2^2*v3)/h1','status':'homogenization proved from assigned weights; coefficient evaluation unresolved'},'unresolved':['outer weighted coefficient cancellation/convolution','homogeneous selector-kernel and nu(a)^2 frame-factor coefficients','M0 full-gerbe coefficient circuits','F scalar complete trace contraction circuits','k/current entry coefficient circuits','inserted exact quotient witnesses','Pi_inner bounded coefficient family contraction','outer carrier/legal label sums'], 'source_convention':'true physical line constants, not pinned pointwise nu[0]=1 jets; adapting those jets requires a separate witness','physical_polynomial_evaluation':False,'product_budget_pass':False}

def validate(d):
    if json.dumps(d,sort_keys=True,separators=(',',':'))!=json.dumps(build(),sort_keys=True,separators=(',',':')):raise ContractError('noncanonical dependency graph')
    for n in d['nodes']:
        if any(i>=n['id'] or i<0 for i in n['inputs']):raise ContractError('not a backwards dependency DAG')
    return d

def encode(d):
    validate(d);b=json.dumps(d,sort_keys=True,separators=(',',':')).encode()
    if len(b)>65536:raise ContractError('metadata byte cap')
    return b

if __name__=='__main__':
    if not __debug__:raise SystemExit('optimized execution disabled')
    print(encode(build()).decode())
